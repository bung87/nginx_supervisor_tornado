import sys
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
port = int(sys.argv[1].split('=')[1])
class MainHandler(tornado.web.RequestHandler):
   def get(self):
      self.write("hello world")
def main():
   application =tornado.web.Application([
   (r"/",MainHandler),
   ])
   http_server = tornado.httpserver.HTTPServer(application)
   http_server.listen(port)
   tornado.ioloop.IOLoop.instance().start()
if __name__=="__main__":
   main();