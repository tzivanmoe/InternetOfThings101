#!/usr/bin/python

import subprocess

class Alive(object):

    def __init__(self):
        pass

    def report(self):
        message = 'Hello IoT Py Learners, What will you make?'
        print message
        command = ['libraries/voicerss.sh', message]
        proc = subprocess.call(command)

# End of File