from unittest import TestCase
from ..utils import bouncy


class BouncyTestCase(TestCase):

    @staticmethod
    def test_first_number_bouncy():
        assert bouncy.is_bouncy(101)

    @staticmethod
    def test_first_number_is_not_bouncy():
        assert bouncy.is_bouncy(1) is False

    @staticmethod
    def test_proportion_start_is_more_than_proportion_end():
        assert bouncy.minimun_number(proportion_start=0.5, proportion_end=0.3) == -1

    @staticmethod
    def test_minimun_number_bouncy_to_proportion_99_percent():
        assert bouncy.minimun_number() == 1587000

    @staticmethod
    def test_minimun_number_bouncy_to_proporttion_50_percent():
        assert bouncy.minimun_number(0,0.0,0.5) == 538

    @staticmethod
    def test_minimun_number_bouncy_to_proportion_90_percent():
        assert bouncy.minimun_number(538,0.5,0.90) == 21780


