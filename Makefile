VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

all: 

#run: 
#. $(VENV)/bin/activate
#./obiecti FILE
# $(PYTHON) app

$(VENV)/bin/activate: requirements.txt
	$(PYTHON) -m venv $(VENV)
	$(PIP) install -r requirements.txt

test:
	. $(VENV)/bin/activate 
	$(PYTHON) -m unittest discover -s tests/ -v

coverage:
	. $(VENV)/bin/activate 
	$(PYTHON) -m unittest discover -s tests/ -v
	$(VENV)/bin/coverage run -m unittest discover -s tests/ -v
	$(VENV)/bin/coverage report -m
	$(VENV)/bin/coverage html

clean:
	rm -rf __pycache__
 # rm -rf $(VENV)