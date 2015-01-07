#!/usr/bin/env python

from flask import Flask, make_response, render_template
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def home():
  r = make_response(render_template('home.html'))
  r.set_cookie('normal', 'no CORS needed here')
  return r

@app.route('/api')
@cross_origin(expose_headers=['X-Cookies'], supports_credentials=True, send_wildcard=False)
def api():
  r = make_response(render_template('api.html'))

  # Set cookies normally (These will never be accepted by a standards compliant browser AJAX call)
  r.set_cookie('key1', 'value1')
  r.set_cookie('key2', 'value2')

  # Build a list of response cookies
  cookies = []
  for k, v in r.headers:
      if k == 'Set-Cookie':
          cookies.append(v)

  # Set the JSON encoded X-Cookies header (This will be accepted by a browser with CORS negotiation)
  if cookies:
      r.headers['X-Cookies'] = json.dumps(cookies)

  return r

if __name__ == '__main__':
    app.run(debug=True, port=8090)

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

