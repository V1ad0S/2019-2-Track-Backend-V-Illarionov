import datetime

def app(environ, start_response):
	now = str( datetime.datetime.now() )[0:19]

	data = bytes(now, encoding = 'utf-8')
	headers = [('Content-Type', 'text/plain'), ('Content-Length', str(len(data)))]

	start_response('200 OK', headers)

	return iter([data])
