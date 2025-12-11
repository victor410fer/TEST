# Vercel Python entrypoint that exposes the existing Flask app as a WSGI app.
# The Vercel Python runtime will serve the WSGI callable available as `app`.
#
# This file imports the Flask `app` from the repository root (app.py)
# and re-exports it as `app`, which the runtime will detect and serve.

from app import app as flask_app

# Expose the Flask WSGI app under the name `app`
app = flask_app
