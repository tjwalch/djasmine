========
Djasmine
========

.. image:: https://travis-ci.org/tjwalch/djasmine.png
   :alt: Build Status
   :target: https://travis-ci.org/tjwalch/djasmine
.. image:: https://coveralls.io/repos/tjwalch/djasmine/badge.svg?branch=master&service=github
   :alt: Coverage Status
   :target: https://coveralls.io/github/tjwalch/djasmine?branch=master 

This app integrates Jasmine JavaScript tests with the Django test framework in a simple but effective DRY way. Using it
you can easily write and run tests that integrates your frontend and backend in a manner that is much easier to maintain
than selenium tests interacting with full web pages.

You can either run individual jasmine spec files and check the result from within your Django test suit or open an url 
from your devserver and run all specs at once, checking the result on the webpage.

Getting started
---------------
1. Add ``'djasmine'`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = [
        ...
        'djasmine',
    ]

2. Include the djasmine URLconf in your project ``urls.py`` like this::

    url(r'^djasmine/', include('djasmine.urls')),

3. Add the following to your project settings::
    
    import jasmine_core
    
    JASMINE_SPEC_ROOT = BASE_DIR + '/path/to/spec/files'
    
    STATICFILES_DIRS = [
        jasmine_core.__path__[0],
        JASMINE_SPEC_ROOT,
    ]

4. Now you need to get your site's JavasSript files included by the Djasmine runner view. You probably already have them written out in your ``'base.html'`` template or similar. In order to keep DRY you don't want to provide this list again in some test setup file, and with Djasmine you don't have to. Instead break out the list of javascript tags into a special top-level template called ``'javascripts.html'`` and include this in your ``'base.html'`` (or similar). This template will also be picked up by the spec runner code. If you are using e g compressor preprocessing tags the template include approach allows you to use these also for the test running code.

  For more specialized needs you can provide your own ``'djasmine/specrunner.html'`` template.

Running Jasmine specs from Django tests
---------------------------------------
Create your Django tests by using ``djasmine.testcase.JasmineRunnerTestCase`` as base class for your test cases. There is one 
required class property, ``webdriver``, that should specify the Selenium WebDriver class you wish to use for the test, 
e g ``selenium.webdriver.firefox.webdriver.WebDriver``.

Run and check result of a Jasmine spec file with the ``assertSpecPasses`` method, which takes one argument: the name
of your spec file.

Example::

    from djasmine.testcase import JasmineRunnerTestCase
    from selenium.webdriver.firefox.webdriver import WebDriver

    
    class MyIntegrationTest(JasmineRunnerTestCase):
        webdriver = WebDriver
        
        def test_all_works_nicely(self):
            self.assertSpecPasses('my_tests.spec.js')  # Runs everything in this spec file and checks result

            ...
            (other checks of backend state possible here)
            ...
            

