# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright (c) 2017 John Dewey
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to
#  deal in the Software without restriction, including without limitation the
#  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
#  sell copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import collections
import re


class ParserError(Exception):
    """ Error raised when a URL can't be parsed. """
    pass


class Parser(object):
    """
    A class responsible for parsing a GIT URL and return a `Parsed` object.
    """

    def __init__(self, url):
        self._url = url

    def get_parsed(self):
        return collections.namedtuple('Parsed', [
            'pathname',
            'protocols',
            'protocol',
            'href',
            'resource',
            'user',
            'port',
            'name',
            'owner',
        ])

    def parse(self):
        """
        Parses a GIT URL and returns an object.  Raises an exception on invalid
        URL.

        :returns: Parsed object
        :raise: :class:`.ParserError`
        """
        d = {
            'pathname': None,
            'protocols': self._get_protocols(),
            'protocol': 'ssh',
            'href': self._url,
            'resource': None,
            'user': None,
            'port': None,
            'name': None,
            'owner': None,
        }
        regexes = [
            (r'^(?P<protocol>https?|git|ssh|rsync)\://'
             '(?:(?P<user>.+)@)*'
             '(?P<resource>[a-z0-9_.-]*)'
             '[:/]*'
             '(?P<port>[\d]+){0,1}'
             '(?P<pathname>\/(?P<owner>.+)/(?P<name>.+).git)'),
            (r'(git\+)?'
             '((?P<protocol>\w+)://)'
             '((?P<user>\w+)@)?'
             '((?P<resource>[\w\.\-]+))'
             '(:(?P<port>\d+))?'
             '(?P<pathname>(\/(?P<owner>\w+)/)?'
             '(\/?(?P<name>[\w\-]+)(\.git)?)?)'),
            (r'^(?:(?P<user>.+)@)*'
             '(?P<resource>[a-z0-9_.-]*)[:/]*'
             '(?P<port>[\d]+){0,1}'
             '[:](?P<pathname>\/?(?P<owner>.+)/(?P<name>.+).git)'),
            (r'((?P<user>\w+)@)?'
             '((?P<resource>[\w\.\-]+))'
             '[\:\/]{1,2}'
             '(?P<pathname>((?P<owner>\w+)/)?'
             '((?P<name>[\w\-]+)(\.git)?)?)'),
        ]
        for regex in regexes:
            if re.search(regex, self._url):
                m = re.search(regex, self._url)
                d.update(m.groupdict())
                break
        else:
            msg = "Invalid URL '{}'".format(self._url)
            raise ParserError(msg)

        p = self.get_parsed()

        return p(**d)

    def _get_protocols(self):
        try:
            index = self._url.index('://')

            return self._url[0:index].split('+')
        except ValueError:
            return []
