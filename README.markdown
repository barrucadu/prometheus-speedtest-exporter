prometheus-speedtest-exporter
=============================

![Some example metrics in Grafana](metrics.png)

A simple [Speedtest][] exporter for [Prometheus][].

For example:

```
# HELP speedtest_ping_latency Ping time in ms
# TYPE speedtest_ping_latency gauge
speedtest_ping_latency{ip="81.98.99.65",iface="eth0",isp="Virgin Media",server="hari-speedtest-1.server.virginmedia.net"} 10.16
# HELP speedtest_ping_jitter Ping jitter in ms
# TYPE speedtest_ping_jitter gauge
speedtest_ping_jitter{ip="81.98.99.65",iface="eth0",isp="Virgin Media",server="hari-speedtest-1.server.virginmedia.net"} 4.636
# HELP speedtest_download Download speed in bytes/s
# TYPE speedtest_download gauge
speedtest_download{ip="81.98.99.65",iface="eth0",isp="Virgin Media",server="hari-speedtest-1.server.virginmedia.net"} 47833486
# HELP speedtest_upload Upload speed in bytes/s
# TYPE speedtest_upload gauge
speedtest_upload{ip="81.98.99.65",iface="eth0",isp="Virgin Media",server="hari-speedtest-1.server.virginmedia.net"} 4586990
```

Unlike other Speedtest exporters I've looked at, like [jeanralphaviles/prometheus_speedtest][] and
[nlamirault/speedtest_exporter][], this is designed to use the [official speedtest.net client][],
so it reports speeds consistent with what you see in your browser.

Download the Linux tarball, extract it, and put the `speedtest` binary
in this directory.  Then run `docker build .`.

[Speedtest]: https://www.speedtest.net/
[Prometheus]: https://prometheus.io/
[jeanralphaviles/prometheus_speedtest]: https://github.com/jeanralphaviles/prometheus_speedtest
[nlamirault/speedtest_exporter]: https://github.com/nlamirault/speedtest_exporter
[official speedtest.net client]: https://www.speedtest.net/apps/cli
