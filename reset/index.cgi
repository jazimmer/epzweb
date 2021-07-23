#! /usr/local/bin/python

import sys
sys.path.append('/home/protected')

import debug_log
import cgi,zipfile,re,os

who = "ethan"
writeDir = os.path.join("/home/protected", who)
 

html_wrap = """<!DOCTYPE html>
<html><head> <title>Site Uploader</title></head>
<body>%s</body></html>
"""

def respond(body): 
  print "Content-Type: text/html"
  print 
  print html_wrap % body


upload_form = """
<p>Compress the folder with your site's files and upload the resulting zip file.</p> 
<form method="post" enctype="multipart/form-data">
<input type="file" name="file" id="file"/><input type="submit" value="Upload"/>
</form>
"""

uploaded = """<p>Uploaded.  Wait overnight to see results.</p>"""

upload_error = """<p>
Error uploading file.  Several possible reasons.  Retry checking your steps as you go.  If that fails email J.Adrian.Zimmer using gmail.
</p> """

def bad_path(path_list):
   rx1 = r"\.\./"
   rx2 = r"gif$|png$|jpg$|htm$|css$|txt$"
   for p in path_list:
      if re.search(rx1,p): return True
      if not re.search(rx2,p,re.I): return True
   return False

try:
   form = cgi.FieldStorage()
   if form.has_key('file'):
      fileitem = form['file']
      fn =  os.path.join(writeDir,"uploaded.zip")
      dn = os.path.join(writeDir,"extracted") 
      with open(fn, 'wb') as fo:
         fo.write(fileitem.file.read())
      with zipfile.PyZipFile(fn) as z:
         if( bad_path(z.namelist()) ):
            debug_log.msg(who + "'s index.cgi: ../ found in path name")
         z.extractall(dn)
         respond(uploaded)
   else:
      respond(upload_form)
except Exception, e:
   debug_log.msg(str(e))
   respond(upload_error)


