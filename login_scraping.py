import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
#coding:utf-8

#メールアドレスとパスワードの指定
User = "aaaaa"
Pass = "aaaaa"

# #セッションするよ
# session = requests.session()

#ログイン
login_info = {
    "username_mmlbbs6":User,
    "password_mmlbbs6":Pass,
    "back":"index.php",
    "mml_id":"0"
}
#セッションするよ
session = requests.session()

#実装するよ
url_login = "https://uta.pw/sakusibbs/users.php?action=login&m=try"
res = session.post(url_login, data=login_info)
res.raise_for_status() # エラーならここで例外を発生させる
#text書き込み
f = open('/Users/aochaaaaannnn/lesson/python/login_scraping_demo/result.txt','a')
f.write(res.text)

f.close()
#-----------------------

# マイページのURLをとる
soup = BeautifulSoup(res.text,"html.parser")
a = soup.select_one(".islogin a")# isloginクラス要素内のaタグ
print(a)
if a is None:
    print("マイページが取得できませんでした")
    quit()

# 相対URLを絶対URLに変換
url_mypage = urljoin(url_login, a.attrs["href"])
print("マイページ=", url_mypage)
#-----------------------

#マイページのHTML
res = session.get(url_mypage)
res.raise_for_status()
f = open('/Users/aochaaaaannnn/lesson/python/login_scraping_demo/mypage.txt','a')

f.write(res.text)

f.close()
#-----------------------

#お気に入りのタイトル取得
soup = BeautifulSoup(res.text,"html.parser")
links = soup.select("#favlist li > a")
for a in links:
    href = urljoin(url_mypage, a.attrs["href"])
    title = a.get_text()
    print("- {} > {}".format(title,href))
