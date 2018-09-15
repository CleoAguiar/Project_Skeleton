try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Alice',
	'autor': 'Cleo Aguiar'
	'url': 'github.com/CleoAguiar',
	'download_url': 'github.com/CleoAguiar',
	'author_email:' 'cleotaisas@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['Alice'],
	'scripts': [],
	'name': 'alice_pela_toca_do_coelho'
}

setup(**config)