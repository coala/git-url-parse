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


@pytest.fixture()
def first_match_urls():
    return {
        'http://example.com/owner/repo.git': {
            'pathname': '/owner/repo.git',
            'protocols': ['http'],
            'protocol': 'http',
            'href': 'http://example.com/owner/repo.git',
            'resource': 'example.com',
            'user': None,
            'port': None,
            'name': 'repo',
            'owner': 'owner',
        },
        'http://example.com/owner/repo': {
            'pathname': '/owner/repo',
            'protocols': ['http'],
            'protocol': 'http',
            'href': 'http://example.com/owner/repo',
            'resource': 'example.com',
            'user': None,
            'port': None,
            'name': 'repo',
            'owner': 'owner',
        },
        'http://user@example.com/user/repo': {
            'pathname': '/user/repo',
            'protocols': ['http'],
            'protocol': 'http',
            'href': 'http://user@example.com/user/repo',
            'resource': 'example.com',
            'user': 'user',
            'port': None,
            'name': 'repo',
            'owner': 'user',
        },
        'http://example.com:29418/owner/repo.git': {
            'pathname': '/owner/repo.git',
            'protocols': ['http'],
            'protocol': 'http',
            'href': 'http://example.com:29418/owner/repo.git',
            'resource': 'example.com',
            'user': None,
            'port': '29418',
            'name': 'repo',
            'owner': 'owner',
        },
        'http://user@example.com:29418/user/repo': {
            'pathname': '/user/repo',
            'protocols': ['http'],
            'protocol': 'http',
            'href': 'http://user@example.com:29418/user/repo',
            'resource': 'example.com',
            'user': 'user',
            'port': '29418',
            'name': 'repo',
            'owner': 'user',
        },
        'http://example.com/repo': {
            'pathname': '/repo',
            'protocols': ['http'],
            'protocol': 'http',
            'href': 'http://example.com/repo',
            'resource': 'example.com',
            'user': None,
            'port': None,
            'name': 'repo',
            'owner': None,
        },
        'https://example.com/owner/repo.git': {
            'pathname': '/owner/repo.git',
            'protocols': ['https'],
            'protocol': 'https',
            'href': 'https://example.com/owner/repo.git',
            'resource': 'example.com',
            'user': None,
            'port': None,
            'name': 'repo',
            'owner': 'owner',
        },
        'https://example.com/owner/repo': {
            'pathname': '/owner/repo',
            'protocols': ['https'],
            'protocol': 'https',
            'href': 'https://example.com/owner/repo',
            'resource': 'example.com',
            'user': None,
            'port': None,
            'name': 'repo',
            'owner': 'owner',
        },
        'https://user@example.com/user/repo': {
            'pathname': '/user/repo',
            'protocols': ['https'],
            'protocol': 'https',
            'href': 'https://user@example.com/user/repo',
            'resource': 'example.com',
            'user': 'user',
            'port': None,
            'name': 'repo',
            'owner': 'user',
        },
        'https://example.com:29418/owner/repo.git': {
            'pathname': '/owner/repo.git',
            'protocols': ['https'],
            'protocol': 'https',
            'href': 'https://example.com:29418/owner/repo.git',
            'resource': 'example.com',
            'user': None,
            'port': '29418',
            'name': 'repo',
            'owner': 'owner',
        },
        'https://user@example.com:29418/user/repo': {
            'pathname': '/user/repo',
            'protocols': ['https'],
            'protocol': 'https',
            'href': 'https://user@example.com:29418/user/repo',
            'resource': 'example.com',
            'user': 'user',
            'port': '29418',
            'name': 'repo',
            'owner': 'user',
        },
        'https://example.com/repo': {
            'pathname': '/repo',
            'protocols': ['https'],
            'protocol': 'https',
            'href': 'https://example.com/repo',
            'resource': 'example.com',
            'user': None,
            'port': None,
            'name': 'repo',
            'owner': None,
        },
        'rsync://example.com/owner/repo.git': {
            'pathname': '/owner/repo.git',
            'protocols': ['rsync'],
            'protocol': 'rsync',
            'href': 'rsync://example.com/owner/repo.git',
            'resource': 'example.com',
            'user': None,
            'port': None,
            'name': 'repo',
            'owner': 'owner',
        },
        'git://example.com/owner/repo.git': {
            'pathname': '/owner/repo.git',
            'protocols': ['git'],
            'protocol': 'git',
            'href': 'git://example.com/owner/repo.git',
            'resource': 'example.com',
            'user': None,
            'port': None,
            'name': 'repo',
            'owner': 'owner',
        },
        'ssh://user@example.com/owner/repo.git': {
            'pathname': '/owner/repo.git',
            'protocols': ['ssh'],
            'protocol': 'ssh',
            'href': 'ssh://user@example.com/owner/repo.git',
            'resource': 'example.com',
            'user': 'user',
            'port': None,
            'name': 'repo',
            'owner': 'owner',
        },
        'ssh://user@example.com:29418/owner/repo.git': {
            'pathname': '/owner/repo.git',
            'protocols': ['ssh'],
            'protocol': 'ssh',
            'href': 'ssh://user@example.com:29418/owner/repo.git',
            'resource': 'example.com',
            'user': 'user',
            'port': '29418',
            'name': 'repo',
            'owner': 'owner',
        },
        'ssh://example.com/owner/repo.git': {
            'pathname': '/owner/repo.git',
            'protocols': ['ssh'],
            'protocol': 'ssh',
            'href': 'ssh://example.com/owner/repo.git',
            'resource': 'example.com',
            'user': None,
            'port': None,
            'name': 'repo',
            'owner': 'owner',
        },
        'ssh://example.com:29418/owner/repo.git': {
            'pathname': '/owner/repo.git',
            'protocols': ['ssh'],
            'protocol': 'ssh',
            'href': 'ssh://example.com:29418/owner/repo.git',
            'resource': 'example.com',
            'user': None,
            'port': '29418',
            'name': 'repo',
            'owner': 'owner',
        },
        # https://github.com/retr0h/git-url-parse/issues/29
        'https://github.com/sphinx-doc/sphinx.git': {
            'pathname': '/sphinx-doc/sphinx.git',
            'protocols': ['https'],
            'protocol': 'https',
            'href': 'https://github.com/sphinx-doc/sphinx.git',
            'resource': 'github.com',
            'user': None,
            'port': None,
            'name': 'sphinx',
            'owner': 'sphinx-doc',
        },
        # https://github.com/retr0h/git-url-parse/issues/33
        'https://github.com/tterranigma/Stouts.openvpn': {
            'pathname': '/tterranigma/Stouts.openvpn',
            'protocols': ['https'],
            'protocol': 'https',
            'href': 'https://github.com/tterranigma/Stouts.openvpn',
            'resource': 'github.com',
            'user': None,
            'port': None,
            'name': 'Stouts.openvpn',
            'owner': 'tterranigma',
        },
        # https://github.com/retr0h/git-url-parse/issues/33
        'https://github.com/tterranigma/Stouts.openvpn.git': {
            'pathname': '/tterranigma/Stouts.openvpn.git',
            'protocols': ['https'],
            'protocol': 'https',
            'href': 'https://github.com/tterranigma/Stouts.openvpn.git',
            'resource': 'github.com',
            'user': None,
            'port': None,
            'name': 'Stouts.openvpn',
            'owner': 'tterranigma',
        },
    }


@pytest.fixture()
def second_match_urls():
    return {
        'git+ssh://example.com/owner/repo.git': {
            'pathname': '/owner/repo.git',
            'protocols': ['git', 'ssh'],
            'protocol': 'ssh',
            'href': 'git+ssh://example.com/owner/repo.git',
            'resource': 'example.com',
            'user': None,
            'port': None,
            'name': 'repo',
            'owner': 'owner',
        },
        'git+https://example.com/owner/repo.git': {
            'pathname': '/owner/repo.git',
            'protocols': ['git', 'https'],
            'protocol': 'https',
            'href': 'git+https://example.com/owner/repo.git',
            'resource': 'example.com',
            'user': None,
            'port': None,
            'name': 'repo',
            'owner': 'owner',
        },
    }


@pytest.fixture()
def third_match_urls():
    return {
        'user@example.com:/owner/repo.git': {
            'pathname': '/owner/repo.git',
            'protocols': [],
            'protocol': 'ssh',
            'href': 'user@example.com:/owner/repo.git',
            'resource': 'example.com',
            'user': 'user',
            'port': None,
            'name': 'repo',
            'owner': 'owner',
        },
        'user@example.com:owner/repo.git': {
            'pathname': 'owner/repo.git',
            'protocols': [],
            'protocol': 'ssh',
            'href': 'user@example.com:owner/repo.git',
            'resource': 'example.com',
            'user': 'user',
            'port': None,
            'name': 'repo',
            'owner': 'owner',
        },
        'user@foo-example.com:owner/repo.git': {
            'pathname': 'owner/repo.git',
            'protocols': [],
            'protocol': 'ssh',
            'href': 'user@foo-example.com:owner/repo.git',
            'resource': 'foo-example.com',
            'user': 'user',
            'port': None,
            'name': 'repo',
            'owner': 'owner',
        },
    }


@pytest.fixture()
def fourth_match_urls():
    return {
        # NOTE(retr0h): This should really be handled by regexp group 3
        'user@example.com:repo.git': {
            'pathname': 'repo.git',
            'protocols': [],
            'protocol': 'ssh',
            'href': 'user@example.com:repo.git',
            'resource': 'example.com',
            'user': 'user',
            'port': None,
            'name': 'repo',
            'owner': None,
        },
        'example.com:/owner/repo.git': {
            'pathname': '/owner/repo.git',
            'protocols': [],
            'protocol': 'ssh',
            'href': 'example.com:/owner/repo.git',
            'resource': 'example.com',
            'user': None,
            'port': None,
            'name': 'repo',
            'owner': 'owner',
        },
        'example.com:owner/repo.git': {
            'pathname': 'owner/repo.git',
            'protocols': [],
            'protocol': 'ssh',
            'href': 'example.com:owner/repo.git',
            'resource': 'example.com',
            'user': None,
            'port': None,
            'name': 'repo',
            'owner': 'owner',
        },
        'example.com:repo.git': {
            'pathname': 'repo.git',
            'protocols': [],
            'protocol': 'ssh',
            'href': 'example.com:repo.git',
            'resource': 'example.com',
            'user': None,
            'port': None,
            'name': 'repo',
            'owner': None,
        },
    }


@pytest.fixture()
def invalid_strings():
    return ['', 'not a valid URL']
