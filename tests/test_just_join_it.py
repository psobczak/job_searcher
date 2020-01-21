import unittest

from pages.just_join_it import JustJoinIT


class TestJustJoinIt(unittest.TestCase):

    def test_city_should_raise_attribute_error(self):
        self.assertRaises(AttributeError, lambda: JustJoinIT('city', 'city'))

    def test_category_should_raise_attribute_error(self):
        self.assertRaises(AttributeError, lambda: JustJoinIT('wroclaw', 'category'))

    def test_finding_job_offers(self):
        just = JustJoinIT('wroclaw', 'testing')
        count_job_offers = len(just.create_job_offers().job_offers)
        self.assertGreater(count_job_offers, 0)


if __name__ == '__main__':
    unittest.main()
