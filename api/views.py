from apiserv import app

# Import models for task
from task.models import Task

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


# Define some generic error handlers if missing
error_codes = [404, 405]
for error_code in error_codes:
    define_json_errorhandler(error_code)