VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

all: 

#run: 
#. $(VENV)/bin/activate
#./obiecti FILE
# $(PYTHON) app

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

test:
	. $(VENV)/bin/activate 
	python3 -m unittest discover -s tests/ -v

clean:
	rm -rf __pycache__
 # rm -rf $(VENV)