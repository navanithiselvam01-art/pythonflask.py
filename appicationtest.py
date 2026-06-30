import unittest
import json
from app import app

class FlaskApplicationTest(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_page(self):
        response = self.client.get('/product/p1')
        self.assertEqual(response.status_code, 200)

    def test_invalid_product(self):
        response = self.client.get('/product/invalid')
        self.assertEqual(response.status_code, 404)

    def test_cart_get(self):
        response = self.client.get('/api/cart')
        self.assertEqual(response.status_code, 200)

    def test_add_to_cart(self):
        data = {
            "productId": "p1",
            "quantity": 1
        }

        response = self.client.post(
            "/api/cart",
            data=json.dumps(data),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)

    def test_orders(self):
        response = self.client.get('/api/orders')
        self.assertEqual(response.status_code, 200)

    def test_wishlist(self):
        response = self.client.get('/api/wishlist')
        self.assertEqual(response.status_code, 200)

    def test_checkout_empty_cart(self):
        response = self.client.post(
            "/api/checkout",
            data=json.dumps({}),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 400)

if __name__ == "__main__":
    unittest.main()
