import __main__
__main__.__requires__ = ['SQLAlchemy >= 0.7', 'jinja2 >= 2.4']
import pkg_resources

# http://stackoverflow.com/questions/8007176/500-error-without-anything-in-the-apache-logs
import logging
import sys
logging.basicConfig(stream=sys.stderr)

from autocloud.web.app import app as application
#application.debug = True  # Nope.  Be careful!

# vim: set ft=python:
