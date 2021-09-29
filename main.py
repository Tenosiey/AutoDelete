#!/usr/bin python3

import os, time, sys

path = "/home/apartment10"

while True:
  now = time.time()

  for f in os.listdir(path):
    f = os.path.join(path, f)

    if os.stat(f).st_mtime < now - 3 * 86400:
      if os.path.isfile(f):
        os.remove(f)
        
  time.sleep(30)
