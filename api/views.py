from apiserv import app
from flask import Blueprint, request, abort, jsonify

# Import Task model and db
from task.models import Task, db

# Not very elegant but works
def define_json_errorhandler(error_code):
    # Check that there isn't any existing handlers defined    
    if type(app.error_handlers) is dict:        
        if error_code not in app.error_handlers:
            app.logger.debug("API.views: Registering errorhandler for code %d" % error_code)
            @app.errorhandler(error_code)
            def handle_error(error):
                # import pdb; pdb.set_trace()
                err = {
                    'message': error.description,
                    'error_code': error.code
                }
                return jsonify(err)
        else:
            app.logger.debug("API.views: Handler for error code %d is already registered." % error_code)

"""

"""
def debug_response():
    req_json = request.json
    resp = {
        'request': {
            'url': request.url,
            'json': request.json,
            'method': request.method
        }            
    }
    return jsonify(resp)

def add_new_task():
    resp = {
        'action': 'add_new_task',
        'result': False
    }

    if db:
        resp['database_connection'] = True
    else:
        resp['database_connection'] = False

    return jsonify(resp)

# Define some generic error handlers if missing
error_codes = [404, 405]
for error_code in error_codes:
    define_json_errorhandler(error_code)

blueprint_config = {
    'url_prefix': '/api',
    'template_folder': 'templates'
}

api = Blueprint(
    'api',
    __name__,
    **blueprint_config
)

# POST routes
@api.route('/task', methods=['POST'])
def handle_post_task():
    resp = debug_response()
    if request.is_json:              
        resp = add_new_task()
    else:
        resp = debug_response()
    return resp
