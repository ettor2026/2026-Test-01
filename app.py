from __future__ import annotations

import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import urlparse

from services.poster_generator import generate_poster_pack
from services.riddle_generator import generate_riddles

ROOT = Path(__file__).resolve().parent


class Handler(BaseHTTPRequestHandler):
    def _send(self, code: int, body: bytes, content_type: str = "text/plain; charset=utf-8"):
        self.send_response(code)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _serve_file(self, relative_path: str, content_type: str):
        file_path = ROOT / relative_path
        if not file_path.exists():
            self._send(404, b"Not found")
            return
        self._send(200, file_path.read_bytes(), content_type)

    def do_GET(self):
        path = urlparse(self.path).path
        if path == "/":
            return self._serve_file("templates/index.html", "text/html; charset=utf-8")
        if path == "/static/style.css":
            return self._serve_file("static/style.css", "text/css; charset=utf-8")
        if path == "/static/app.js":
            return self._serve_file("static/app.js", "application/javascript; charset=utf-8")
        self._send(404, b"Not found")

    def do_POST(self):
        path = urlparse(self.path).path
        content_length = int(self.headers.get("Content-Length", "0"))
        raw = self.rfile.read(content_length) if content_length else b"{}"
        payload = json.loads(raw.decode("utf-8")) if raw else {}

        if path == "/api/riddles":
            try:
                data = generate_riddles(
                    topic=payload.get("topic", "mixed"),
                    count=int(payload.get("count", 10)),
                    tone=payload.get("tone", "fun"),
                )
            except ValueError as exc:
                return self._send(400, json.dumps({"error": str(exc)}).encode("utf-8"), "application/json")
            return self._send(200, json.dumps({"items": data}, ensure_ascii=False).encode("utf-8"), "application/json")

        if path == "/api/poster":
            data = generate_poster_pack(
                style=payload.get("style", "new_chinese"),
                visual_focus=payload.get("visual_focus", "所城里与海岸灯笼"),
                palette=payload.get("palette", "朱红+鎏金"),
            )
            return self._send(200, json.dumps(data, ensure_ascii=False).encode("utf-8"), "application/json")

        self._send(404, b"Not found")


def run_server(host: str = "0.0.0.0", port: int = 5000):
    server = HTTPServer((host, port), Handler)
    print(f"Server running at http://{host}:{port}")
    server.serve_forever()


if __name__ == "__main__":
    run_server()
