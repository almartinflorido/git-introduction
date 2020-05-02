# git-introduction

## How to execute?
### 1. Create virtual environment for python 3
``
sudo apt install python3-venv
``

``
python3 -m venv pyimaging-venv
``

``
source pyimaging-venv/bin/activate
``
### 2. Install dependencies
``
pip install -r requirements.txt
``
### 3. Execute tests
```
export PYTHONPATH=`pwd`
cd tests/
python3 -m unittest
```
