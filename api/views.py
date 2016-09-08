from apiserv import app
from flask import Blueprint, request, abort, jsonify

# Import Task model and db
from task.models import Task, db

def define_handlers():
    # Define some generic error handlers if missing
    error_codes = [404, 405]
    for error_code in error_codes:
        define_json_errorhandler(error_code)

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
Compile debug response
"""
def debug_response():
    req_json = request.json
    resp = {
        'request': {
            'url': request.url,
            'json': request.json,
            'method': request.method
        },
        "db_connection": db is not None           
    }
    return resp

def handle_add_task():
    resp = {
        'action': 'add_new_task',
        'result': False,
        'success': [],
        'failed': []
    }
    resp['debug'] = debug_response()

    # If db connection and Task model exists/is imported
    if db and Task:
        if 'items' in request.json:
            resp['items'] = True
            items = request.json['items']
        else:
            items = [request.json]
        failed = []
        success = []
        for item in items:
            result = add_new_task(item)
            item_details = {
                'item': item,
                'result': result['result'],
                'message': result['message']
            }
            if result['result']:
                success.append(item_details)
            else:
                failed.append(item_details)

        resp['success'] = success
        resp['failed'] = failed

        try:
            db.session.commit()
        except Exception as ex:
            app.logger.error(ex)
            db.session.rollback()

    return resp


def add_new_task(item):
    result = False 
    message = "no process"   
    # app.logger.debug(item)
    query_result = Task.query.filter(Task.id == item['id']).first()
    if item['id'] and not query_result:
        try:
            task = Task(**item)
            db.session.add(task)
            db.session.flush()
            if task.id:
                result = True
                message = "success"
            else:
                message = "failed"
        except Exception as ex:
            err = "Exception while processing item %s" % item['id']
            app.logger.error(err, ex)
            message = err
    else:
        message = "duplicate entry"
        result = True
        app.logger.warning(message)

    r = {
        'result': result,
        'message': message
    }
    return r

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
    if request.is_json:              
        resp = jsonify(handle_add_task())
    else:
        resp = jsonify(debug_response())
    return resp
