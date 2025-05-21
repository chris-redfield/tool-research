default: check-lint format test run

install:
  pip install -r requirements.txt

test:
  pytest test/

check-lint:
  flake8 src/

format folder="src":
  black {{folder}}

run:
  python src/main.py