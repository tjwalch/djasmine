# -*- coding: utf-8 -*-
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.exceptions import ImproperlyConfigured
from django.core.urlresolvers import reverse
from selenium.webdriver.support.wait import WebDriverWait


class JasmineRunnerTestCase(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super(JasmineRunnerTestCase, cls).setUpClass()
        try:
            cls.selenium = cls.webdriver()
        except (AttributeError, TypeError):
            raise ImproperlyConfigured(
                "Subclasses need to specify which Selenium webdriver to use through "
                "the 'webdriver' property."
            )

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(JasmineRunnerTestCase, cls).tearDownClass()

    def assertSpecPasses(self, spec):
        self.selenium.get('%s%s' % (self.live_server_url, reverse(
            'jasmine-run-spec', kwargs={'spec': spec})))
        WebDriverWait(self.selenium, 100).until(
            lambda driver:
            driver.execute_script("return jsApiReporter.finished;")
        )
        for result in self.selenium.execute_script(
                'return jsApiReporter.specs();'
        ):
            for fail in result['failedExpectations']:
                raise self.failureException(
                    fail['message']
                )
