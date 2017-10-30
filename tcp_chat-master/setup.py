try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

setup(
	name = 'tcp_chat' , 
	version = '0.1.1',
	description = 'A chat app built over TCP',
	author = 'Sunil Yadav' , 
	author_email = 'sunilyadav747884@gmail.com',
	url = 'https://github.com/Sunil8239/tcp_chatapp' ,
	license='MIT',
	packages = ['tcp_chat'],
	install_requires = ['clint'],
	download_url = 'https://github.com/pdhoot/tcp_chat/tarball/0.1' ,
	keywords = ['chat' , 'tcp-chat'],
	entry_points = {
		'console_scripts' : ['tcp_chat = tcp_chat.tcp_chat:main']
	}
)
