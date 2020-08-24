import asyncio
from asyncio import transports


class EchoServerClientProtocol(asyncio.Protocol):
    """Эхо сервер."""

    def connection_made(self, transport: transports.BaseTransport) -> None:
        """
        Действие при получении входящего подключения.
        """

        peername = transport.get_extra_info('peername')
        print(f'Connection from {peername}')

        self.transport = transport

    def data_received(self, data: bytes) -> None:
        """
        Ответ.
        """

        message = data.decode(encoding='utf-8')
        print(f'Data received: {message}')

        self.transport.write(('Echoed back: {}'.format(message)).encode())

        print('Close the client socket')
        self.transport.close()


def main(host: str = '127.0.0.1', port: int = 8888):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(EchoServerClientProtocol, host, port)
    server = loop.run_until_complete(coro)

    print('Serving on {}'.format(server.sockets[0].getsockname()))
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    # Close the server
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


if __name__ == '__main__':
    main()
