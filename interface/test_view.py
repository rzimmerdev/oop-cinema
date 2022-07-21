import unittest
from interface.view import ViewFactory
from manager.franchise import FranchiseFactory


class TestViewFactory(unittest.TestCase):

    def setUp(self) -> None:
        self.franchise = FranchiseFactory("MarketPlace", 1999)
        self.facade = ViewFactory(self.franchise)

    def test_config_view(self):
        self.fail()

    def test_show(self):
        self.fail()

    def test_set_background(self):
        self.fail()

    def test_show_src(self):
        self.fail()

    def test_show_movies(self):
        self.fail()

    def test_show_review(self):
        self.fail()


if __name__ == "__main__":
    unittest.main()
