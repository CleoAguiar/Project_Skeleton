try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'My Project',
	'autor': 'Cleo Aguiar'
	'url': 'github.com/CleoAguiar',
	'download_url': 'github.com/CleoAguiar',
	'author_email:' 'cleotaisas@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'projectname'
}

setup(**config)