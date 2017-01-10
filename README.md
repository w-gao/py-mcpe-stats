# py-mcpe-stats
[![PyPI](https://img.shields.io/pypi/v/py_mcpe_stats.svg)](https://pypi.python.org/pypi/py_mcpe_stats/)

![py-mcpe-stats](https://github.com/w-gao/py-mcpe-stats/blob/master/images/logo.png)

## Introduction
------------
py-mcpe-stats is a Python software that allows you to ping a Minecraft Pocket:Edition server for basic information.

## Install
-------
You are required to have Python 3 installed on your computer

#### Install via pip
Run `pip install py_mcpe_stats` in your terminal and it will download the latest version of this project.

## Usage
-----
#### Run Directly

Simply execute `python main.py` in the root folder of this project.

It will automatically query the host and port that are set in the `main.py` file.


#### Use as a module

Include the following code in your project:

```python
from py_mcpe_stats import Query

host = 'localhost'
port = 19132

q = Query(host, port)
server_data = q.query()
```

## License
-------

MIT &copy; 2016 w-gao