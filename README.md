# py-mcpe-stats

[![PyPI](https://img.shields.io/pypi/v/mcstats.svg)](https://pypi.python.org/pypi/mcstats)

## Introduction
------------
mcstats (aka py-mcpe-stats) is a Python software that allows you to ping a Minecraft: Bedrock edition server for basic 
information.

## Install
-------
You are required to have Python >= 3.6 installed on your computer.

#### Install via pip
Run `pip install mcstats` in your terminal, and it will install the latest version of this project in your Python 
environment.

#### Install from source
Clone this repository and run the following in the root folder of this project:
```
python setup.py build install
```

## Usage
-----

#### Query with CLI
After installation, the `mcstats` command will be available in your Python environment. You can perform a query with 
the following command: `mcstats localhost`.

Example:
```
$ mcstats play.lbsg.net
Ping id: 850756528
Server id: 123456789
Game id: MCPE
Server name: §3US§8> SM Become a Creeper
Game protocol: 422
Game version: 1.16.210
Num players: 5479
Max players: 38865
Hash code: -1
Motd: None
Gamemode: None
Hash code: 1189580737
```

You can also specify the port with the `-p` option (e.g.: `mcstats localhost -p 19133`). For more options, please run 
`mcstats --help`.


#### Use as a module
You can also use the API by writing the following code in your project:

```python
from mcstats import mcstats

host = "localhost"
port = 19132

with mcstats(host, port=port, timeout=10) as data:
    # data is a StatsServerData object
    print(data)
```

## License
-------

MIT &copy; 2016-2021 w-gao
