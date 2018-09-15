from nose.tools import *
import Alice

def setup():
	print("SETUP!")


def teardown():
	print("DESTRUIR!")


def test_basic():
	print("EXECUTANDO", end= '')
