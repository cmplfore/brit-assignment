# brit-assignment
 
Creating a basic framework 


# Setup

Assumptions have been made that you're running the latest version of Python 3.10 > and using MacOS.

1. Clone repository onto machine. 
2. Run `python -m venv venv` within the project. The second `venv` can be the name of the virtual environment. 
3. Once created activate the virtual environment by running `source ./venv/bin/activate`.
4. Once activated install the project dependencies running `pip install requirements.txt`

# Running the tests

1. Once the setup above has been completed, you can run the tests using `pytest tests --headed --slowmo 1000`
   1. The headed and the slowmo allows you to see the tests running, and at a slower speed. Remove these as required.
2. 