# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright (c) 2017 John Dewey
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import pytest

from giturlparse import parser


def test_parse(git_urls):
    for url, d in git_urls.items():
        p = parser.Parser(url)
        result = p.parse()

        assert d['pathname'] == result.pathname
        assert d['protocols'] == result.protocols
        assert d['protocol'] == result.protocol
        assert d['href'] == result.href
        assert d['resource'] == result.resource
        assert d['user'] == result.user
        assert d['port'] == result.port
        assert d['name'] == result.name
        assert d['owner'] == result.owner


def test_parse_raises_on_invalid_url(invalid_urls):
    for url in invalid_urls:
        p = parser.Parser(url)
        with pytest.raises(parser.ParserError):
            p.parse()


def test_get_protocol_multiple_protocols():
    p = parser.Parser('git+ssh://git@example.com/Owner/Repository.git')

    assert ['git', 'ssh'] == p._get_protocols()


def test_get_protocol_no_protocols():
    p = parser.Parser('//example.com/foo')

    assert [] == p._get_protocols()


def test_get_protocol_one_protocols():
    p = parser.Parser('ssh://git@example.com/Owner/Repository.git')

    assert ['ssh'] == p._get_protocols()
