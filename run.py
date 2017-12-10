# run.py
# This is the file that is invoked to start up a development server. 
# It gets a copy of the app from your package and runs it. This won’t be used in production, but it will see a lot of mileage in development.
import sys
from app import app

if __name__ == "__main__":
	import logging
	from logging.handlers import RotatingFileHandler
	handler = logging.StreamHandler(sys.stdout)
	handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
	# FORMAT = "[%(asctime)s : %(levelname)s : %(filename)s : %(lineno)s : %(funcName)20s() ] %(message)s"
	# logging.basicConfig(filename="app/logs/logs.log", level=logging.DEBUG, format=FORMAT)
	# simple format  # "%(asctime)s - %(levelname)s - %(message)s")
	# logger = logging.getLogger("main")
	app.logger.addHandler(handler)
	app.logger.setLevel(logging.DEBUG)
	app.logger.info("started")
	# for linux
    # app.run(host='0.0.0.0')
	app.run(port=5050)
