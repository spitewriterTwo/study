import requests        #网络请求模块
import json       #对json数据进行反序列化为python对象，编解码json数据

if __name__ == '__main__':
    url_jx = 'https://api.sigujx.com/zy/sigu_jx.php'
    link = 'https://v.qq.com/x/cover/ipmc5u3dwb48mv2/l0033wtb8cw.html'
    data = {"url":link}
    src_movie = requests.post(url_jx,data = data).text
    src_movie = json.loads(src_movie)    #对包含json文档的str进行反序列化
    print(src_movie)