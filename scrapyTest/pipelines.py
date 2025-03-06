import pymysql

class ScenicSpotPipeline:
    def __init__(self):
        self.connection = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="123123",
            database="python",
            charset="utf8mb4"
        )
        self.cursor = self.connection.cursor()

    def process_item(self, item, spider):
        sql = """
        INSERT INTO jingqu (name, region, score, star, address, comment, price, sale, province_city_region)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(sql, (
            item["name"], item["region"], item["score"], item["star"], item["address"],
            item["comment"], item["price"], item["sale"], item["province_city_region"]
        ))
        self.connection.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.connection.close()