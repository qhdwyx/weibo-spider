# import json
# import datetime
# import redis
from bs4 import BeautifulSoup
# from decorators import parse_decorator
# password = REDIS_ARGS.get('password', '')
# cookies_db = REDIS_ARGS.get('cookies', 1)
# host = REDIS_ARGS.get('host', '127.0.0.1')
# port = REDIS_ARGS.get('port', 6379)
# cookies_con = redis.Redis(host=host, port=port, password=password, db=cookies_db)

# @parse_decorator(False)
def is_403(html):
    if "['uid']" not in html and "['nick']" not in html and "['islogin']='1'" in html:
        return True

    if 'Sina Visitor System' in html:
        return True

    # verify code for search page
    # todo  solve the problem of verify_code when searching
    if 'yzm_img' in html and 'yzm_input' in html:
        return True

    soup = BeautifulSoup(html, 'html.parser')
    if soup.title:
        if '访问受限' in soup.title.text or '解冻' in soup.title.text:
            return True
        else:
            return False
    else:
        return False


# class Cookies(object):
#     @classmethod
#     def store_cookies(cls, name, cookies, proxy):
#         pickled_cookies = json.dumps(
#             {'cookies': cookies, 'loginTime': datetime.datetime.now().timestamp(), 'proxy': proxy})
#         cookies_con.hset('account', name, pickled_cookies)
#         cls.push_in_queue(name)
