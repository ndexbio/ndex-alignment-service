from bottle import hook, response, route, request, run, error, HTTPResponse
import json
import alignment

@error(405)
def method_not_allowed(res):
    if request.method == 'OPTIONS':
        new_res = HTTPResponse()
        new_res.set_header('Access-Control-Allow-Origin', '*')
        new_res.headers['Access-Control-Allow-Methods'] = 'GET, POST, DELETE, PUT, PATCH, OPTIONS'
        new_res.headers['Access-Control-Allow-Headers'] = 'Content-Type, api_key, Authorization'

        return new_res
    res.headers['Allow'] += ', OPTIONS'
    return request.app.default_error_handler(res)


@hook('after_request')
def enable_cors():
    response.headers['Access-Control-Allow-Origin'] = '*'

@route('/')
def get_status():
    version = '1.0.0'
    status = {'status': 'available', 'version': version, 'service': 'alignment' }
    return status

@route('/expand', method='POST')
def expand():
    cx_dict = json.load( request.body)
    cx1 = cx_dict['cx1']
    cx2 = cx_dict['cx2']
    return json.dumps( alignment.expand(cx1, cx2) )

if __name__ == '__main__':
    run(host='0.0.0.0', port=8080, debug=True)