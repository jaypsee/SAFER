from SimpleHTTPServer import SimpleHTTPRequestHandler

class Serv(SimpleHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found!"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

httpd = SimpleHTTPRequestHandler(('localhost', 8080), Serv, )
httpd.serve_forever()