===============================
Python Kafka Logging Handler
===============================
.. image:: https://pypip.in/download/python-kafka-logging/badge.svg
    :target: https://pypi.python.org/pypi//python-kafka-logging/
    :alt: Downloads
.. image:: https://pypip.in/version/python-kafka-logging/badge.svg
    :target: https://pypi.python.org/pypi/python-kafka-logging/
    :alt: Latest Version
.. image:: https://pypip.in/license/python-kafka-logging/badge.svg
    :target: https://pypi.python.org/pypi/python-kafka-logging/
    :alt: License

Simple python logging handler for forwarding logs to a kafka server.

The handler uses a logstash formatter.


Installing
==========

.. code-block:: shell

	$ pip install python_kafka_logging


How to use 
==========
Example for using the handler within a native logging.conf file

.. code-block:: shell

	example/logging.conf
   


Get the project
===============

	1. Clone the git repository
	
	.. code-block:: shell
	
		$ git clone https://github.com/taykey/python-kafka-logging/

	2. Install a virtualenv
	
	.. code-block:: shell
	
		$ sudo apt-get install python-virtualenv

	3. Create a new virtualenv
	
	.. code-block:: shell
	
		$ virtualenv python_kafka_logging_ve

	4. Install project's requirements
	
	.. code-block:: shell
	
		$ python_kafka_logging_ve/bin/pip install -r requirements.txt



Reporting Issues
================
If you have suggestions, bugs or other issues specific to this library, file them `here`_ or contact me at avihoo <at> taykey <dot> com.



keywords: python, logging, handler, example, kafka, logs, logstash, formatter

.. _here: https://github.com/taykey/python-kafka-logging/issues

