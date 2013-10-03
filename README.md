nginx_supervisor_tornado
========================
a nginx+supervisor+tornado development environment automatically install and setup tool.<br>
running 2 nginx worker_processes and 4 servers (listening on 8000-8003)  by default;<br>
using a tornado hello world example as homepage.<br>
nginxd.service(not original nginx.service) and supervisord.service services will be enabled.<br>
##usage
	./install_init.sh
##dependencies
	yum 
##environment
  >nginx version: 1.4.2<br>
  >supervisor version:3.0<br>
  >Python version:2.7.5<br>
  >tornado version:1.2.1<br>
