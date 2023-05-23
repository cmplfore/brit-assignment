# brit-assignment
 
Creating a basic framework for the Brit Insurance assigment


# Setup

Assumptions have been made that you're running the latest version of Python and using MacOS.

1. Clone the repository onto machine. 
2. Run `python -m venv venv` within the project. The second `venv` can be the name of the virtual environment. 
3. Once created activate the virtual environment by running `source ./venv/bin/activate`.
4. Once activated install the project dependencies running `pip install requirements.txt`

# Running the tests

1. Once the setup above has been completed, you can run the tests using `pytest tests --headed --slowmo 1000`
   1. The headed and the slowmo allows you to see the tests running, and at a slower speed. Remove these as required.


# Improvements

~~1. Convert both tests to use Page Object Pattern.~~
2. Improve the locators - I've currently used Xpaths and some built in Playwright locating methods. Would be better to keep it consistent throughout and also use unique test ids or just ids.
3. Reports for the results could be added to show results of test runs.
4. Currently, both tests are in the 1 test file, this could be better split up to make it easier to understand what is being tested.
5. Part of the test accepts the cookies, to help improve performance we might want to set the cookie in code for some tests.