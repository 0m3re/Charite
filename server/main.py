# IMPORTS
import asyncio
from websocket_server import WebSocketServer

# Main execution
if __name__ == "__main__":
    print("Starting WebSocket server")

    HOST = "127.0.0.1"
    PORT = 8765

    server = WebSocketServer(HOST, PORT)

    try:
        asyncio.run(server.start())
    except KeyboardInterrupt:
        print("Server stopped by KeyboardInterrupt")
