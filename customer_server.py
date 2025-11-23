import http.server
import socketserver
import json
import os
from urllib.parse import urlparse

PORT = 8000
ROOT = os.path.dirname(os.path.abspath(__file__))
CUSTOMERS_PATH = os.path.join(ROOT, 'customers.json')

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == '/customers' or parsed.path == '/customers/':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            if os.path.exists(CUSTOMERS_PATH):
                with open(CUSTOMERS_PATH, 'r', encoding='utf-8') as fh:
                    data = json.load(fh)
                self.wfile.write(json.dumps(data, ensure_ascii=False, indent=2).encode('utf-8'))
            else:
                self.wfile.write(b'[]')
            return
        elif parsed.path == '/' or parsed.path == '/index.html':
            # serve a small HTML viewer
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            html = '''<!doctype html>
<html><head><meta charset="utf-8"><title>Customers</title>
<style>body{font-family:Arial,Helvetica,sans-serif;padding:20px}pre{background:#f6f8fa;padding:15px;border-radius:6px}</style>
</head><body>
<h1>Customers</h1>
<p>JSON available at <a href="/customers">/customers</a></p>
<pre id="data">Loading…</pre>
<script>
fetch('/customers').then(r=>r.json()).then(d=>{
  document.getElementById('data').textContent = JSON.stringify(d,null,2);
}).catch(e=>{document.getElementById('data').textContent = 'Failed to load customers: '+e});
</script>
</body></html>'''
            self.wfile.write(html.encode('utf-8'))
            return
        else:
            # fallback to default file server behaviour
            return http.server.SimpleHTTPRequestHandler.do_GET(self)

if __name__ == '__main__':
    with socketserver.TCPServer(('127.0.0.1', PORT), Handler) as httpd:
        print(f"Serving customers from {CUSTOMERS_PATH} at http://127.0.0.1:{PORT}/customers")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print('Server stopped')
            httpd.server_close()
