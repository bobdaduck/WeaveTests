## Weave Test Framework

Run tests by pytest from the repository's root directory specifying the "Test_cases" directory: `

```"pytest Test_Cases --html="results.html"```.


## SETUP
To setup, you must install the chromedriver version for your operating system into the root folder. Chromedriver can be downloaded from https://chromedriver.chromium.org/downloads for any operating system, but you must download the version of chromedriver that matches the version of google chrome installed on your computer (found on chrome's about page). You may also need to add `chromedriver` to your `PATH`: https://www.howtogeek.com/658904/how-to-add-a-directory-to-your-path-in-linux/

You must install the requirements from the requirements.txt file, which can be done with the command

```pip install -r requirements.txt```

or individually, by running 
```pip install pytest
pip install pytest-html
pip install selenium
pip install requests```


It is advised to create a virtual environment first, which causes the packages installed by pip to be installed only for python running within the virtual environment, rather than be installed at the system level, but this is not strictly necessary. 


## Explanation of packages used

Pytest is a popular python test runner
Pytest-html generates a report html file which can then be emailed or consumed with test failures, stack traces, and successes.
Selenium is a browser automation framework
Requests is python's standard library for REST requests.



