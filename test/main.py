from http.server import HTTPServer, BaseHTTPRequestHandler
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        header = self.headers.get('X-Forwarded-For', 'not found') #not found для перестраховки и отладки
        response = f"X-Forwarded-For: {header}\n"
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        self.wfile.write(response.encode())
HTTPServer(('0.0.0.0', 8080), Handler).serve_forever() #без роутов ибо зачем
