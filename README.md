[![PyPI](https://img.shields.io/pypi/v/meteomatics.svg)](https://pypi.python.org/pypi/meteomatics)

[![logo](https://static.meteomatics.com/meteomatics-logo.png)](http://www.meteomatics.com "Meteomatics - Your Experts in Weather Data Processing")

Python connector to the [Meteomatics Weather API](https://www.meteomatics.com/en/api/overview/ "Documentation Overview")
===================================================================================


Meteomatics provides a REST-style API to retrieve historic, current, and forecast data globally. This includes model data and observational data in time series and areal formats. Areal formats are also offered through a WMS/WFS-compatible interface. Geographic and time series data can be combined in certain file formats, such as NetCDF.


Install by typing `pip install meteomatics` in your favourite shell.

For a start we recommend to run the example script.

## Local mock server

A minimal fake API is included under `mock_server/` for offline development. It serves canned responses for `query_user_limits` and `query_station_list` — enough as a template for extending to other endpoints.

```
pip install flask
python -m mock_server &
export METEOMATICS_API_BASE_URL=http://127.0.0.1:9999
python examples/99_mock_server_demo.py
```

The connector reads `METEOMATICS_API_BASE_URL` at import time, so any `query_*` call will be routed to the mock server while that variable is set. Unset it to go back to the real API.
