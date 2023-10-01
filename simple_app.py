from wsgiref.simple_server import make_server
import json
import logging

def application(environ, start_response):
    content = {}
    for i in range(100000):
        content[str(i)] = str('Hello! My name is Kirill!')
    content = json.dumps(content).encode()
    status = '200 OK'
    response_headers = [('Content-Type', 'application/json'),
                        ('Content-Length', str(len(content)))]
    start_response(status, response_headers)
    return [content]

if __name__ == '__main__':
    try:
        port = 8006
        http_server = make_server('', port, application)
        print(f'Server has been created! Port: {port}')
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()
        print(f'Server has been closed!')
