import scrapy

class ScenicSpotItem(scrapy.Item):
    name = scrapy.Field()  # 景点名称
    region = scrapy.Field()  # 地区
    score = scrapy.Field()  # 评分
    star = scrapy.Field()  # 评级
    address = scrapy.Field()  # 地址
    comment = scrapy.Field()  # 评语
    price = scrapy.Field()  # 价格
    sale = scrapy.Field()  # 销量
    province_city_region = scrapy.Field()  # 省市自治区信息
