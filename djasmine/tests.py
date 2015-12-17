# -*- coding: utf-8 -*-
from . import testcase
from selenium.webdriver.firefox.webdriver import WebDriver


class TestTheTest(testcase.JasmineRunnerTestCase):
    webdriver = WebDriver

    def test_jaz(self):
        self.assertRaises(
            AssertionError,
            self.assertSpecPasses,
            'test_test.spec.js'
        )
