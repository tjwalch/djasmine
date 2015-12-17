# -*- coding: utf-8 -*-
from django import test
from . import testcase
from django.core.exceptions import ImproperlyConfigured
from django.core.urlresolvers import reverse
from selenium.webdriver.phantomjs.webdriver import WebDriver


class TestTheTest(testcase.JasmineRunnerTestCase):
    webdriver = WebDriver

    def test_reports_failure(self):
        self.assertRaises(
            AssertionError,
            self.assertSpecPasses,
            'javascripts/test_test.spec.js'
        )


class DjasmineTest(test.TestCase):

    def test_class_setup(self):
        class IncompleteSetup(testcase.JasmineRunnerTestCase):
            pass
        self.assertRaises(
            ImproperlyConfigured,
            IncompleteSetup.setUpClass
        )

    def test_run_all(self):
        response = self.client.get(reverse('jasmine-run-spec'))
        self.assertContains(response, 'test_test.spec.js')
