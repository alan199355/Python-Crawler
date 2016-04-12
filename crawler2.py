# import urllib.request
# url="http://www.douban.com/"
# webPage=urllib.request.urlopen(url);
# data=webPage.read()
# print(data)
# print(type(webPage))
# print(webPage.geturl())
# print(webPage.info())
# print(webPage.getcode())
# input()

# import urllib.request
# weburl="http://www.douban.com/"
# webheader={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
# req=urllib.request.Request(url=weburl,headers=webheader)
# webpage=urllib.request.urlopen(req)
# data=webpage.read()
# print(data)
# print(type(webpage))
# print(webpage.geturl())
# print(webpage.info())
# print(webpage.getcode())
# input()

# import urllib.request
# import socket
# import re
# import sys
# import os
# targetDir=(r"D:\Python")
# print(os.getcwd())
# def destFile(path):
# 	if not os.path.isdir(targetDir):
# 		os.mkdir(targetDir)
# 	pos=path.rindex('/')
# 	t=os.path.join(targetDir,path[pos+1:])
# 	return t
# if __name__=="__main__":
# 	weburl="http://www.lan-bridge.com/lanbridge/about.aspx"
# 	webheader={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
# 	req=urllib.request.Request(url=weburl,headers=webheader)
# 	webpage=urllib.request.urlopen(req)
# 	contentBytes=webpage.read()	
# 	for link in set(re.findall(r'(http:[^s]*?(jpg|png|gif))', str(contentBytes))):
# 		print(link)		
# 		try:
# 			urllib.request.urlretrieve(link,destFile(link))
# 		except:
# 			print('failure')
# input()

# import urllib.request  
# import re    
# def fetch(baseUrl):  
  
#     # 第1步：模拟浏览器发送请求  
#     data = urllib.request.urlopen(baseUrl).read()  #二进制字节形式  
#     data = data.decode('utf-8')    
  
#     # 第2步：页面返回后，利用正则表达式提取想要的内容  
#     nameList=[]  
#     nameList = re.compile(r'target="_blank" title="(.*?)"',re.DOTALL).findall(data)  
  
#     # 第3步：返回在页面上析取的“标题名”  
#     return nameList  
      
# #######     执行    ########   
# if __name__ =="__main__":  
     
#     #要抓取的网页地址  
#     url = "http://www.lan-bridge.com/news"  
  
#     #存放到名字列表中  
#     NameList = fetch(url)  
  
#     # 输出 NameList  
#     Length = len(NameList)  
#     for i in range(0, Length):  
#         print("标题名%d:%s\n"%(i+1, NameList[i])) 

# from urllib import request
# import threading
# from time import sleep,ctime
# from html import parser
# def downjpg( filepath,FileName ="default.jpg" ):
#     try:
#         web = request.urlopen( filepath)
#         print("访问网络文件"+filepath+"\n")
#         jpg = web.read()
#         DstDir="E:\\GitHub File\\Python"
#         print("保存文件"+DstDir+FileName+"\n")
#         try:
#             File = open( DstDir+FileName,"wb" )
#             File.write( jpg)
#             File.close()
#             return
#         except IOError:
#             print("error\n")
#             return
#     except Exception:
#         print("error\n")
#         return
# def downjpgmutithread( filepathlist ):
#     print("共有%d个文件需要下载"%len(filepathlist))
#     for file in filepathlist:
#         print( file )
#     print("开始多线程下载")
#     task_threads=[] #存储线程
#     count=1
#     for file in filepathlist:
#         t= threading.Thread( target=downjpg,args=(file,"%d.jpg"%count) )
#         count=count+1
#         task_threads.append(t)
#     for task in task_threads:
#         task.start()
#     for task in task_threads:
#         task.join() #等待所有线程结束
#     print("线程结束")
# class parserLinks( parser.HTMLParser):
#     filelist=[]
#     def handle_starttag(self,tag,attrs):
#         if tag == 'img':
#             for name,value in attrs:
#                 if name == 'src':
#                     print( value)
#                     self.filelist.append(value)
#                     #print( self.get_starttag_text() )
#     def getfilelist(self):
#         return self.filelist
# def main(WebUrl):
#     #globals flist
#     if __name__ == "__main__":
#         lparser = parserLinks()
#         web = request.urlopen( WebUrl )
#         #context= web.read()
#         for context in web.readlines():
#             _str="%s"%context
#             try:
#                 lparser.feed( _str)
#             except parser.HTMLParseError:
#                 #print( "parser error")
#                 pass
#         web.close()
#         imagelist= lparser.getfilelist()
#         downjpgmutithread( imagelist)      
#         #downjpgmutithread( flist)
# #WebUrl="http://www.baidu.com/" #要抓去的网页链接,默认保存到e盘
# WebUrl="http://www.lan-bridge.com/lanbridge/about.aspx"
# main(WebUrl)

