#!/usr/bin/env python

import logging

from flask import Flask, request, make_response
from weasyprint import HTML

app = Flask('pdf')

@app.route('/health')
def index():
    return 'ok'


@app.before_first_request
def setup_logging():
    logging.addLevelName(logging.DEBUG, "\033[1;36m%s\033[1;0m" % logging.getLevelName(logging.DEBUG))
    logging.addLevelName(logging.INFO, "\033[1;32m%s\033[1;0m" % logging.getLevelName(logging.INFO))
    logging.addLevelName(logging.WARNING, "\033[1;33m%s\033[1;0m" % logging.getLevelName(logging.WARNING))
    logging.addLevelName(logging.ERROR, "\033[1;31m%s\033[1;0m" % logging.getLevelName(logging.ERROR))

    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]'
    ))
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.DEBUG)

@app.route('/<name>', methods=['POST'])
def generate(name='unnamed'):
    app.logger.info('POST  /%s' % name)
    html = HTML(string=request.data)
    pdf = html.write_pdf()
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=%s.pdf' % name
    app.logger.info('POST  /%s  ok' % name)
    return response


if __name__ == '__main__':
    app.run()