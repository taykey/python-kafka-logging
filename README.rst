===============================
Python Kafka Logging Handler
===============================

Simple python logging handler for forwarding logs to a kafka server.

The Handler uses a logstash formatter.


Installing
==========

.. code-block:: shell

	$ pip install python-kafka-logging


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
	
		$ virtualenv python-kafka-logging-ve

	4. Install project's requirements
	
	.. code-block:: shell
	
		$ python-kafka-logging-ve/bin/pip install -r requirements.txt



Reporting Issues
================
If you have suggestions, bugs or other issues specific to this library, file them <a href="https://github.com/taykey/python-kafka-logging/issues">here</a> or contact me at avihoo <at> taykey <dot> com.



keywords: python, logging, handler, example, kafka, logs, logstash, formatter

