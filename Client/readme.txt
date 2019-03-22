Readme:
=======

how to setup:  -- do from command like or using any IDE like pycharm
-------------
1. Install 'python3' and 'pip'

2. Install python virtualenv library
	-- pip install virtualenv

3. Create Virtual environment
	-- virtualenv <virtual env name>

4. Activate Virtula Env
	-- open path <virtual env name>/Scripts/
	-- Run Active script

5. Copy and Untar the tar file, go the path OTT_Client

6. run requirements.txt using below command
	-- pip install -r requirements.txt
	



how to run testsuite:
---------------------
1. Do provide/modify the 'Test_cases.cfg' file, to provide the test cases information to the framework

2. Do change, email report configs in 'email_report.cfg'

3. run execute.py file
	-- python execute.py Test_cases.cfg

4. Once the test gets executed, logs and reports gets generated in below path
	-- LOGS path: ./log/
	-- reports path: ./report/


