import tornado.ioloop
import tornado.web
import session_factory import alex_session#要有这句



class MainHandler(tornado.web.RequestHandler):
    def get(self):
        alex_session(self)#就会去调用alex_session类，执行初始化函数init，该方法会看客户端是否有cookie，没有就给他一个cookie，有的话服务端不做任何操作，此时效果就是会显示该用户的用户名和有自动登录功能（MainHandler的get方法会触发alex_session的初始化函数检测用户是否有cookie的key匹配的value，有的话得到cookie的value就会得到{ md5随机码:{‘Loginfo’:['alex','123']}} ）
        self.write("login.html")
    def post(self):#这里我们不管用户在login.html输入啥，内部定义就是alex和123
        name='alex'
        pwd='123'
        li=[name,pwd]
        #检验用户密码
        if name=='alex':
            session=alex_session(self)
            session.set_session('Logininfo',li)#把用户名和密码放到列表里，调用alex_session的set方法，存放为字典格式
            self.redirect('/index')#然后跳转到index方法，也就是application里的IndexHandler类里
        else:
            self.render('/login')
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        session=alex_session(self)
        se=session.get_session('Logininfo')#是否你能从alex_session的get方法得到key为logininfo的value值
        if se:
            se[0]
            self.write('index:'se[0])
        else:
            self.redirect('/login')

#这里在IndexHandler有if和else是因为如果下次关闭浏览器再次登录/index/就不能显示，会跳转到login方法
# 禁用cookie，就不能保存用户名，更别说记住密码，下次直接登录了
#一天最多投票10次就是cookie功能

application = tornado.web.Application([
    (r"/login", MainHandler),#当你url有login，就会触发MainHandler的方法
    (r"/index",InderHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()