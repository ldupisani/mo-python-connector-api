"""Demo: running example queries against the local mock server.

Usage:
    pip install flask
    python -m mock_server &
    export METEOMATICS_API_BASE_URL=http://127.0.0.1:9999
    python examples/99_mock_server_demo.py
"""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

if "METEOMATICS_API_BASE_URL" not in os.environ:
    sys.exit(
        "METEOMATICS_API_BASE_URL is not set. "
        "Start the mock server (`python -m mock_server`) and "
        "export METEOMATICS_API_BASE_URL=http://127.0.0.1:9999 first."
    )

import meteomatics.api as api

print("Querying user limits against", os.environ["METEOMATICS_API_BASE_URL"])
limits = api.query_user_limits("demo", "demo")
for name, (used, hard) in limits.items():
    print(f"  {name}: {used} / {hard}")

print("\nQuerying station list")
stations = api.query_station_list("demo", "demo")
print(stations)
