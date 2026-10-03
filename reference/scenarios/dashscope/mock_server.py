"""Local DashScope text-generation response for the SDK scenario."""

import argparse
import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/health":
            self.send_error(404)
            return
        self.send_response(200)
        self.send_header("Content-Length", "2")
        self.end_headers()
        self.wfile.write(b"ok")

    def do_POST(self):
        if self.path != "/api/v1/services/aigc/text-generation/generation":
            self.send_error(404)
            return
        request = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        if not request.get("model") or not request.get("input", {}).get("messages"):
            self.send_error(400)
            return
        body = json.dumps(
            {
                "request_id": "dashscope-mock-001",
                "output": {
                    "choices": [{"finish_reason": "stop", "message": {"role": "assistant", "content": "Hello."}}]
                },
                "usage": {"input_tokens": 8, "output_tokens": 2, "total_tokens": 10},
            }
        ).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", type=int, required=True)
    args = parser.parse_args()
    HTTPServer(("127.0.0.1", args.port), Handler).serve_forever()
