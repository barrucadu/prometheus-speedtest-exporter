#!/usr/bin/env python3

import flask
import json
import subprocess
import sys

app = flask.Flask(__name__)


def generate_metrics():
    print("starting speedtest...", file=sys.stderr)
    r = json.loads(
        subprocess.check_output(
            [
                "./speedtest",
                "--progress=no",
                "--format=json",
                "--accept-gdpr",
                "--accept-license",
            ]
        )
    )
    print("...test complete", file=sys.stderr)

    if r["type"] != "result":
        return None

    labels = ",".join(
        [
            f'{k}="{v}"'
            for k, v in {
                "ip": r["interface"]["externalIp"],
                "iface": r["interface"]["name"],
                "isp": r["isp"],
                "server": r["server"]["host"],
            }.items()
        ]
    )

    return "\n".join(
        [
            "# HELP speedtest_ping_latency Ping time in ms",
            "# TYPE speedtest_ping_latency gauge",
            f"speedtest_ping_latency{{{labels}}} {r['ping']['latency']}",
            "# HELP speedtest_ping_jitter Ping jitter in ms",
            "# TYPE speedtest_ping_jitter gauge",
            f"speedtest_ping_jitter{{{labels}}} {r['ping']['jitter']}",
            "# HELP speedtest_download Download speed in bytes/s",
            "# TYPE speedtest_download gauge",
            f"speedtest_download{{{labels}}} {r['download']['bandwidth']}",
            "# HELP speedtest_upload Upload speed in bytes/s",
            "# TYPE speedtest_upload gauge",
            f"speedtest_upload{{{labels}}} {r['upload']['bandwidth']}",
            "",
        ]
    )


@app.route("/metrics")
def serve_metrics():
    metrics = generate_metrics()
    if metrics is None:
        flask.abort(500)

    response = flask.make_response(metrics, 200)
    response.mimetype = "text/plain"
    return response


app.run(host="0.0.0.0", port=8888)
