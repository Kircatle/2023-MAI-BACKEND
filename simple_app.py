from wsgiref.simple_server import make_server


def application(environ, start_response):
    response_body = b"Dattebayo!\n"
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/plain'),
        ('Content-Length', str(len(response_body)))
    ]
    start_response(status, response_headers)
    return [response_body]


if __name__ == '__main__':
    httpd = make_server('', 9000, application)
    print("Serving on port 9000...")
    httpd.serve_forever()