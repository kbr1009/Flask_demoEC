from dataclasses import dataclass
import uuid

@dataclass
class TopData:
    def main(self):
        products = self.get_products()
        context = {
                "products": products
                }
        return context


    def get_products(self):
        products = [{
                "productname": "スエット",
                "sku": 6471846819461,
                "price": 3000,
                "product_info": "ぶかぶかスエット",
                "thumbnail": "https://yamawa-product-img.s3.ap-northeast-1.amazonaws.com/product_img/bonbon%E3%82%B9%E3%82%A6%E3%82%A7%E3%83%83%E3%83%88.jpg"
                },
                {
                "productname": "ポロシャツ",
                "sku": 5432341435254,
                "price": 2300,
                "product_info": "イケイケポロシャツ",
                "thumbnail": "https://yamawa-product-img.s3.ap-northeast-1.amazonaws.com/product_img/bonbon%E3%83%92%E3%82%99%E3%83%83%E3%82%AF%E3%82%99%E3%82%B7%E3%83%AB%E3%82%A8%E3%83%83%E3%83%88%E3%83%9B%E3%82%99%E3%83%BC%E3%82%BF%E3%82%99%E3%83%BC%E3%83%9B%E3%82%9A%E3%83%AD.jpg"
                }]
        return products

    def get_uuid(self):
        cart_uuid = uuid.uuid1()
        return cart_uuid


@dataclass
class DetailData:
    product_id : str

    def get_product(self):
        if self.product_id == 6471846819461:
            product_detail = {
                    "productname": "スエット",
                    "sku": 6471846819461,
                    "price": 3000,
                    "product_info": "ぶかぶかスエット",
                    "thumbnail": "https://yamawa-product-img.s3.ap-northeast-1.amazonaws.com/product_img/bonbon%E3%82%B9%E3%82%A6%E3%82%A7%E3%83%83%E3%83%88.jpg"
                    }

        if self.product_id == 5432341435254:
            product_detail = {
                    "productname": "ポロシャツ",
                    "sku": 5432341435254,
                    "price": 2300,
                    "product_info": "イケイケポロシャツ",
                    "thumbnail": "https://yamawa-product-img.s3.ap-northeast-1.amazonaws.com/product_img/bonbon%E3%83%92%E3%82%99%E3%83%83%E3%82%AF%E3%82%99%E3%82%B7%E3%83%AB%E3%82%A8%E3%83%83%E3%83%88%E3%83%9B%E3%82%99%E3%83%BC%E3%82%BF%E3%82%99%E3%83%BC%E3%83%9B%E3%82%9A%E3%83%AD.jpg"
                    }
        return product_detail
