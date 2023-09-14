#!/usr/bin/env python3

from SessionManager import SessionManager

myManager = SessionManager(host="localhost", port=10071)

myManager.killall_sessions()

