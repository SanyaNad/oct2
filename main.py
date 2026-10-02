from http.server import BaseHTTPRequestHandler, HTTPServer
import json

missions = [
    {
        "name": "Moon",
        "year": 2030
    },
    {
        "name": "Mars",
        "year": 2050
    }
]

class MissionHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/missions":
            response = json.dumps(missions, ensure_ascii=False).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(response)
        else:
            self.send_error(404, "Path not found.")

server = HTTPServer(("127.0.0.1", 8000), MissionHandler)

print("The server has been activated")
print("Open: http://127.0.0.1:8000/missions")

server.serve_forever()