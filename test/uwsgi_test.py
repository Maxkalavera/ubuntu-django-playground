

def application(env, response):
    response('200 OK', [('Content-Type', 'text/html')])
    return [b"Hello World"]
