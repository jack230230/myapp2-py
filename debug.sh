#!/bin/bash

export NH_DEBUG=True

pip install -r requirements.txt
if [ "$NH_PLUGIN" == "VSCode" ]
then
    python3 -m debugpy --listen 9009 --wait-for-client app.py 5000
else
    python3 -m flask run
fi