import os

from .app import app

if __name__ == "__main__":
    port = int(os.environ.get("MOCK_SERVER_PORT", 9999))
    app.run(host="127.0.0.1", port=port)
