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


# https://stackoverflow.com/questions/2514859/regular-expression-for-git-repository
@pytest.fixture()
def git_urls():
    return {
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
    }


@pytest.fixture()
def invalid_urls():
    return [
        'https://example.com/owner',
        'git+ssh://example.com/owner/repo.git'
        'git+https://example.com/owner/repo.git'
        'https://example.com/owner',
        'example.com:repo.git',
        'user@example.com:repo.git',
    ]
