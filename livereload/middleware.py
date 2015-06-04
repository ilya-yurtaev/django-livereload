"""
Middleware for injecting the live-reload script.
"""
from bs4 import BeautifulSoup

from django.utils.encoding import smart_str


class LiveReloadScript(object):
    """
    Inject the live-reload script into your webpages.
    """

    def process_response(self, request, response):

        if response.status_code != 200 or 'text/html' not in response.get('content-type', ''):
            return response

        soup = BeautifulSoup(smart_str(response.content),
                             'html.parser')
        script = soup.new_tag('script',
                              src='http://localhost:35729/livereload.js')
        soup.head.append(script)

        response.content = str(soup)

        return response
