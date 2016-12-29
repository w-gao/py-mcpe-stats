from Query import Query

host = 'localhost'
port = 19132

q = Query(host, port)
server_data = q.query()

if server_data is not None and server_data.SUCCESS:

    print('Ping Id: ', server_data.PING_ID)
    print('Server Id: ', server_data.SERVER_ID)

    print('Game Id: ', server_data.GAME_ID)
    print('Server Name:', server_data.SERVER_NAME)
    print('Protocol: ', server_data.GAME_PROTOCOL)
    print('Game Version: ', server_data.GAME_VERSION)
    print('Current Players: ', server_data.NUM_PLAYERS)
    print('Max Players: ', server_data.MAX_PLAYERS)

    if server_data.HASH_CODE is not -1:
        print('Hash: ', server_data.HASH_CODE)
        print('M.O.T.D: ', server_data.MOTD)
        print('Game mode: ', server_data.GAMEMODE)

    print('Success: ', server_data.SUCCESS)
else:
    print('O.o')
