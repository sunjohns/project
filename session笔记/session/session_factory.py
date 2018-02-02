import hashlib
import time
session_container={}#定义是空
class alex_session(object):
    def __init__(self,request):
        self.__request=request
        self.initialize()
    def initialize(self):
        id=self.__request.get__cookie('__oldboy_session')#得到的是cookie的value md5随机码
        if not id:
            ha=hashlib.md5()
            ha.update(str(time.time()))
            val=ha.hexdigest()
            self.__request.set cookie('__oldboy_session',val，expires_days=1)#过期时间就是在这时间内即使关闭浏览器，再次登录也是可以保存会话的
        self.__id=id
    def set_session(self,key,session_val):
        temp={key:session_val}
        session_container[self.__id]=temp
        print session_container
    def get_session(self,name):
        val=session_container[self.__id][name]#也就是得到{ md5随机码:{‘Loginfo’:}Loginfo里的value值，也就是登录列表
        return val