"""Test cam module."""
import pytest

from matrixscreener.cam import *


class EchoSocket(object):
    """Dummy echo socket for mocking."""

    msg = ''

    def send(self, msg):
        self.msg = msg
        return len(msg)

    def recv(self, buffer_size):
        return self.msg[0:buffer_size]

    def connect(self, where):
        pass

    def settimeout(self, timeout):
        pass

    def fileno(self):
        return 0

# TEST
# key (here cli) overrided if defined several times
# prefix added
# types (integer, float) should be converted to strings


def test_echo(monkeypatch):
    """Prefix + command sent should be same as echoed socket message."""
    # mock socket
    monkeypatch.setattr("socket.socket", EchoSocket)

    # setup cam
    cam = CAM()

    cmd = [('cli', 'custom'), ('cmd', 'enableall'), ('value', 'true'),
           ('integer', 1234), ('float', 0.00234)]

    # monkeypathced EchoSocket will never flush
    def flush():
        pass
    cam.flush = flush

    echoed = cam.send(cmd)[0]
    sent = tuples_as_dict(cam.prefix + cmd)

    assert sent == echoed


def test_commands(monkeypatch):
    """Short hand commands should work as intended."""
    # mock socket
    monkeypatch.setattr("socket.socket", EchoSocket)

    # setup cam
    cam = CAM()

    # monkeypathced EchoSocket will never flush
    def flush():
        pass
    cam.flush = flush

    # get_information
    cmd = cam.prefix + [
        ('cmd', 'getinfo'),
        ('dev', 'stage')
    ]

    information = cam.get_information()
    should_be = tuples_as_dict(cmd)

    assert information == should_be
