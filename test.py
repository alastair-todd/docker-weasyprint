#!/usr/bin/env python3.5

import subprocess
import unittest
from urllib.request import Request, urlopen

html_data = '''
<!DOCTYPE html>
<html>
<head>
    <title>Test File</title>
</head>
<body>
    <h1>Hello World</h1>
</body>
</html>
'''.encode('utf-8')


import urllib.request
req = urllib.request.Request('http://www.example.com/')
req.add_header('Referer', 'http://www.python.org/')
r = urllib.request.urlopen(req)


def request_factory(path='/'):
    url = 'http://127.0.0.1:5001%s' % path
    headers = {
        'Content-Type': 'application/html'
    }
    return Request(url, data=html_data, headers=headers, method='POST')


class TestAPI(unittest.TestCase):

    def setUp(self):
        request = request_factory('/sample')
        self.response = urllib.request.urlopen(request)

    def tearDown(self):
        self.response.close()

    def test_response_code(self):
        self.assertEqual(self.response.getcode(), 200)

    def test_headers(self):
        self.assertEqual(self.info().headers, [
            'Content-Type: application/pdf',
            'Content-Disposition: inline; filename=sample.pdf'
        ])

    def test_body(self):
        self.assertEqual(response.read()[:4], b'%PDF')


if __name__ == '__main__':
    unittest.main()