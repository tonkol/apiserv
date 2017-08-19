#!/usr/bin/env python
import os, sys

# Add working directory to sys.path
# Just in case to avoid duplicate entries..
package_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if package_path not in sys.path:
	sys.path.insert(1, package_path)

from flask_script import Manager, Server
from . import app

# Define manager for the app to access shell in Flask application context
# and modify runtime settings
manager = Manager(app)

manager_options = {
	'use_debugger': True,
	'use_reloader': True,
	'host': os.getenv('HOST_IP', '0.0.0.0'),
	'port': int(os.getenv('PORT', 5001))
}

manager.add_command("runserver", Server(**manager_options))

if __name__ == "__main__":
	manager.run()
