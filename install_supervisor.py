import os
import sys
import re
f=open("/usr/bin/pip",'r')
f.next()
line=f.next()
m=re.search('pip==(\d\.\d)',line)
v=float(m.group(1))
#With pip >= 1.4
#pip -q install supervisor --pre;

#With previous versions of pip:
#pip -q install supervisor;
if v>=1.4:
	os.system("pip -q install supervisor --pre")
else:
	os.system("pip -q install supervisor")
