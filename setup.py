try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
version = "0.0.1"

setup(
	name = 'coinserve',
	version = version,
	scripts = ['coinserve'],
	
	package_dir = {
		'cfetch': 'cfetch'
	},

	install_requires = ['coinfetch'],

	package_data = {
		'': ['README']
	},
	include_package_data=True,

	author = 'Justyn Temme',
	author_email = 'justyntemme@gmail.com',
	description = 'Web server for coinfetch API',
	license = 'AGPLV3',
	keywords = '',
	url = 'http://github.com/justyntemme/coinserve.git'
)
