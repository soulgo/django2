#!/usr/bin/env python
#encoding:UTF-8
import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import json
from tornado.options import define,options
from tornado.web import RequestHandler,url

tornado.options.define("port",type=int,default=8000,help="服务器端口")

class IndexHandler(RequestHandler):
    def post(self):
        # subject = self.get_query_argument("subject")
        # subjects = self.get_query_arguments("k")
        # body_arg = self.get_body_argument("b")
        # body_args = self.get_body_arguments("b")
        #上面两者的综合体
        # a = self.get_argument("a")
        # ags = self.get_arguments("a")
        # self.write(str(body_args))
        #######################数据是json
        # print self.request.headers.get("Content-Type")
        # print self.request.body
        # json_data = self.request.body
        # json_args = json.loads(json_data)
        # self.write(str(json_args))
        #######################文件
        files = self.request.files
        img_files = files.get('img')
        if img_files:
            img_file = img_files[0]["body"]
            file = open("a","w+")
            file.write(img_file)
            file.close()
        self.write("OK")
if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        [(r"/",IndexHandler),
         ],debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()