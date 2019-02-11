from setuptools import setup, find_packages

version = {}
with open('PayneLabData/version.py') as fp:
	exec(fp.read(), version)

setup(name='PayneLabData',
	version=version['__version__'],
	description='Data for Professor Samuel Payne\'s research lab at Brigham Young University',
	url='http://github.com/PayneLab/PayneLabData',
	author='Dr. Samuel Payne',
	author_email='sam_payne@byu.edu',
	license='Apache 2.0',
	packages=[
		'PayneLabData',
		'PayneLabData.CPTAC',
        'PayneLabData.BurkholderiaTimeCourse'
		],
	#packages=find_packages(),
	install_requires=[
		'numpy',
		'pandas'
	],
	include_package_data=True
	)
