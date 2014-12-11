from django.test import TestCase
from cms.forms import ImpressionForm
from cms.models import Impression


class ImpressionFormTests(TestCase):
    def test_valid1(self):
        """正常な入力を行えばエラーにならないことを検証"""
        params = dict(comment='感想')
        impression = Impression()
        form = ImpressionForm(params, instance=impression)
        self.assertTrue(form.is_valid())

    def test_valid2(self):
        """コメントは省略可能であることを検証"""
        params = dict()
        impression = Impression()
        form = ImpressionForm(params, instance=impression)
        self.assertTrue(form.is_valid())
