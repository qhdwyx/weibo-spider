from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from weibo.login import get_session
from weibo.usersettings import cookies, username, password


if __name__ == "__main__":
    session = get_session(username, password)
    for key in session.cookies.get_dict():
        cookies[key] = session.cookies.get_dict()[key]
    process = CrawlerProcess(get_project_settings())
    process.crawl('weiboImg')
    process.start()
