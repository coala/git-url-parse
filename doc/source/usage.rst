Usage
=====

This tool will parse a GIT URL and return a `Parsed` object.

::

    import giturlparse

    p = giturlparse.parse('git@github.com:retr0h/ansible-etcd.git')
    p.pathname
    p.protocols
    p.protocol
    p.href
    p.resource
    p.user
    p.port
    p.name
    p.owner
