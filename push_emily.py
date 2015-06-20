#!/usr/bin/env python

from daemon import Daemon
import sys
import logging
import redis

LOGFILE = '/var/log/push_emily.log'
PIDFILE = '/var/run/push_emily.pid'

logging.basicConfig(filename=LOGFILE, level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

class MyDaemon(Daemon):
    def run(self):
        r_server = redis.Redis('localhost')
        while True:
            notif = r_server.lpop("notifyq")



if __name__ == "__main__":
   daemon = MyDaemon(PIDFILE, LOGFILE)
   if len(sys.argv) > 1:
       if 'start' == sys.argv[1]:
           daemon.start()
       elif 'stop' == sys.argv[1]:
           daemon.stop()
       elif 'restart' == sys.argv[1]:
           daemon.restart()
       elif 'status' == sys.argv[1]:
           daemon.status()
       else:
           print "Unknown command"
           sys.exit(2)
       sys.exit(0)
   else:
       daemon.restart()