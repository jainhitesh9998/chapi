import functools
import http.server
import socketserver

PORT = 8791

class CORSHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-store')
        super().end_headers()

Handler = functools.partial(CORSHandler, directory='public')

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving ./public on port {PORT}")
    httpd.serve_forever()
