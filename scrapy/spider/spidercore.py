import scrapy
import json
from django_scrapy_quna.spider.scrapy.items import ScenicSpotItem


class ScenicSpotSpider(scrapy.Spider):
    name = "scenic_spot"
    allowed_domains = ["piao.qunar.com"]
    base_url = "http://piao.qunar.com/ticket/list.json?keyword={}&region=&from=mpl_search_suggest&page={}"

    def __init__(self, keyword="国庆旅游景点", *args, **kwargs):
        super(ScenicSpotSpider, self).__init__(*args, **kwargs)
        self.keyword = keyword

    def start_requests(self):
        for page in range(1, 36):
            url = self.base_url.format(self.keyword, page)
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        try:
            data = json.loads(response.text)
            if "data" in data and "sightList" in data["data"]:
                for sight in data["data"]["sightList"]:
                    item = ScenicSpotItem(
                        name=sight.get("sightName", ""),
                        region=sight.get("districts", ""),
                        score=sight.get("score", 0),
                        star=sight.get("star", "无"),
                        address=sight.get("address", ""),
                        comment=sight.get("intro", ""),
                        price=sight.get("qunarPrice", 0),
                        sale=sight.get("saleCount", 0),
                        province_city_region=sight.get("districts", "")
                    )
                    yield item
        except json.JSONDecodeError:
            self.logger.error("JSON 解析失败: %s", response.url)
