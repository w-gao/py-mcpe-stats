from mcstats.main import mcstats


host = 'play.lbsg.net'
port = 19132

with mcstats(host, port=port, timeout=5) as data:
    def key(k):
        return k.capitalize().replace('_', ' ')


    stdout: str = '\n'.join(f"{key(k)}: {v}" for k, v in data.__dict__.items())
    print(stdout)
