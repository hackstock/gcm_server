gcm_server
==========

A python module for pushing messages to Android clients via Google Cloud Messaging

USAGE INSTRUCTIONS
==================
After cloning this repository, 
1. CD into the directory where you cloned to
2. Execute "virtualenv venv --distribute" to create a virtual python environment 
3. Execute "source venv/bin/activate" to activate your newly created virtual environment
4. Execute "pip install -r requirements.txt" to install dependencies
5. Modify values for gcm_id and/or gcm_ids in run.py to that of your target device(s) appropriately
6. Execute "python run.py"
7. Wait for Google to do the magic!
8. Have fun!
