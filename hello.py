def application(environ,start_response):
    print(environ['PATH_INFO'].encode('iso-8859-1').decode('utf-8'))

    start_response('200 OK',[('Content-Type','text/html; charset=utf-8')])

    body = '<h1>Hello,%s!</h1>' % ((environ['PATH_INFO'].encode('iso-8859-1').decode('utf-8'))[1:] or 'web')

    return [body.encode('utf-8')]