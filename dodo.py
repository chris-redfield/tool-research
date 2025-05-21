def task_install():
  """Install packages for project dev"""
  return {
    "actions": [
        'pip install -r requirements.txt'
    ],
    'verbosity': 2,
  }

def task_test():
  """Test code"""
  return {
    "actions": [
        'pytest test/'
    ],
    'verbosity': 2,
  }

def task_check_lint():
  """Run flake8 for code check"""
  return {
    "actions": [
        'flake8 src/'
    ],
    'verbosity': 2,
  }

def task_format(folder="src"):
  """Format code using Black"""
  return {
    "actions": [
        f'black {folder}',
        'echo IT WORKED !!!!!!'
    ],
    'verbosity': 2,
  }

def task_run_now():
  """Run project code"""
  return {
    "actions": [
        f'python src/main.py'
    ],
    'verbosity': 2,
  }
