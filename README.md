
Selenium based automated testing.
This package requires **Python 3.5**!

==========================

Copernicus Climate test

==========================
Usage:
------

::

    $ virtualenv copenv
    $ source copenv/bin/activate
    $ pip3 install selenium
    $ download the browser webdrivers chromedriver and geckodriver 
    $ The given browser webdriver must be in your $PATH\n
    $ or given via the --browserpath option.
    $ help: python3 climateTestSuite.py -h
    $ for instance, it can be run on Firefox, 800x600 resolution,
     verbosity 2 as follows:
    $ python3 climateTestSuite.py -V -sw 800 -sh 600 -B firefox
    Run the test headless by using -H or --headless:
    $ python3 climateTestSuite.py -H -V


==========================

Copernicus Atmosphere test

==========================

Usage: 
------
::

    $ virtualenv copenv
    $ source copenv/bin/activate
    $ pip3 install selenium
    $ download the browser webdrivers for Firefox (geckodriver) and chromedriver
    $ The given browser webdriver must be in your $PATH\n
    $ or given via the --browserpath option.
    $ help: python3 atmTestSuite.py -h
    For instance, it can be run on Firefox, 800x600 resolution, 
    verbosity 2 as follows:
    $ python3 atmTestSuite.py -V -sw 800 -sh 600 -B firefox
    To run the test on a different url use -U command line argument
    $ python3 atmTestSuite.py -V -U https://test.atmosphere.copernicus.eu
    