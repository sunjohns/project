from django.utils.safestring import mark_safe
def page(baseurl,totalnum,currentpage):
    perpage=20#定义每页的数量20个记录
    pagenum=11#一共在inex.html展现11页
    temp=divmod(totalnum,20)#用divmod方法，把总记录除以20，得到商和余数
    totalpage=temp[0]#temp[0]是商,temp[1]是余数
    if temp[1]:#是否存在余数，如果有的话，把所有余数给他另增一页
       totalpage +=1
    if totalpage<=11:#如果总页数小于11，就开始的页数是1，结束的页是11
        start=1
        end=totalpage
    else:#如果你的总页数大于11

      if currentpage>6:#如果当前你selected选中的页数是大于6
         start=currentpage-5#开始的页数是比如7-5=2
         end=currentpage+6#结束的页数是7+6-1=12
      else:
          start=1#如果单签selected选中的页数不大于6，第一页就是1.最后一页就是end=12-1=11
          end=12
      if end>totalpage:#如果一共15页，你选中了13页，并不会13+6-1=18，而是最后一页就是15，
          end=totalpage
          start=end-11#开始的页数就是15-11=4


    html=[]#定义html为空，把a标签放到里面
    for i in range(start,end):
        url = baseurl + str(i)
        if i==currentpage:
          html.append('<a class="selected" href="'+url+'">'+str(i)+'</a>')#i是显示的页，一点击选中就会跳转到/index/页数
        else:

            html.append('<a  href="'+url+'">'+str(i)+'</a>')#否则就不被选中
    return mark_safe(''.join(html))#最后把这些循环结果都放到html列表，然后返回到view方法，输出为p，最后作为模版语言方法index.html，会有selected的样式展出
#一开始要导入mark_safe