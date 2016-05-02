from bottle import hook, response, route, request, run
import json
import alignment

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