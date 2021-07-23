#! /usr/local/bin/python

import cgitb; cgitb.enable()

def printHeader(status=None):
   if(status):  ## probably unused, cgitb handling all exceptions 
      import sys
      sys.stderr = sys.stdout
      print status 
   print "Content-Type: text/plain"
   print

raise Hell
printHeader()
print "Hellow Orld"


