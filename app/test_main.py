import unittest
import datetime
from unittest import mock
from app.main import outdated_products


class TestOutdatedProducts(unittest.TestCase):

    def setUp(self) -> None:
        self.test_date = datetime.date(2022, 2, 2)

    def test_some_outdated_products(self) -> None:
        products = [
            {
                "name": "salmon",
                "expiration_date": datetime.date(2022, 2, 10),
                "price": 600
            },
            {
                "name": "chicken",
                "expiration_date": datetime.date(2022, 2, 5),
                "price": 120
            },
            {
                "name": "duck",
                "expiration_date": datetime.date(2022, 2, 1),
                "price": 160
            }
        ]
        with mock.patch("datetime.date") as mock_date:
            mock_date.today.return_value = self.test_date
            result = outdated_products(products)
            self.assertEqual(result, ["duck"])

    def test_all_products_outdated(self) -> None:
        products = [
            {
                "name": "expired milk",
                "expiration_date": datetime.date(2022, 1, 1),
                "price": 50
            },
            {
                "name": "stale bread",
                "expiration_date": datetime.date(2022, 1, 15),
                "price": 30
            }
        ]
        with mock.patch("datetime.date") as mock_date:
            mock_date.today.return_value = self.test_date
            result = outdated_products(products)
            self.assertEqual(result, ["expired milk", "stale bread"])

    def test_no_outdated_products(self) -> None:
        products = [
            {
                "name": "fresh vegetables",
                "expiration_date": datetime.date(2022, 3, 1),
                "price": 200
            },
            {
                "name": "frozen fish",
                "expiration_date": datetime.date(2022, 4, 15),
                "price": 700
            }
        ]
        with mock.patch("datetime.date") as mock_date:
            mock_date.today.return_value = self.test_date
            result = outdated_products(products)
            self.assertEqual(result, [])

    def test_mixed_products(self) -> None:
        products = [
            {
                "name": "old cheese",
                "expiration_date": datetime.date(2022, 1, 30),
                "price": 300
            },
            {
                "name": "new yogurt",
                "expiration_date": datetime.date(2022, 2, 3),
                "price": 90
            },
            {
                "name": "aged wine",
                "expiration_date": datetime.date(2021, 12, 31),
                "price": 1200
            }
        ]
        with mock.patch("datetime.date") as mock_date:
            mock_date.today.return_value = self.test_date
            result = outdated_products(products)
            self.assertEqual(result, ["old cheese", "aged wine"])

    def test_expiration_day_today_not_outdated(self) -> None:
        products = [
            {
                "name": "fresh milk",
                "expiration_date": datetime.date(2022, 2, 2),
                "price": 50
            },
            {
                "name": "expired bread",
                "expiration_date": datetime.date(2022, 1, 30),
                "price": 30
            }
        ]
        with mock.patch("datetime.date") as mock_date:
            mock_date.today.return_value = self.test_date
            result = outdated_products(products)
            self.assertEqual(result, ["expired bread"])
