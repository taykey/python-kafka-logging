from distutils.core import setup
setup(
  name = 'python-kafka-logging',
  packages = ['python-kafka-logging'], # this must be the same as the name above
  version = '0.1',
  description = 'Simple python logging handler for forwarding logs to a kafka queue.',
  author = 'Avihoo Mamka',
  author_email = 'avihoo@taykey.com',
  url = 'https://github.com/taykey/python-kafka-logging', # use the URL to the github repo
  download_url = 'https://github.com/taykey/python-kafka-logging/tarball/0.1',
  keywords = ['kafka', 'logging', 'python'], # arbitrary keywords
  classifiers = [],
)
