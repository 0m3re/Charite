#IMPORTS
import websockets
import asyncio
import json

class WebSocketServer:
    def __init__(self, ip, port):
        self.address = ip
        self.port = port
        self.server = None
        print("Initializing WebSocket server")

    # Starts the WebSocket server
    async def start(self):
        self.server = await websockets.serve(self.handle_connection, self.address, self.port)
        print(f"Listening on ws://{self.address}:{self.port}")
        await self.server.wait_closed()

    # Handles incoming WebSocket connections
    async def handle_connection(self, websocket, path):
        try:
            # Handles messages from the connected WebSocket
            async for message in websocket:
                await self.handle_data(message, websocket)
        except websockets.exceptions.ConnectionClosedOK as e:
            print(f"Connection closed by the client, no issues")
        except websockets.exceptions.ConnectionClosedError as e:
            print(f"Connection closed with error code: {e.code} reason: {e.reason}")
        except Exception as e:
            print(f"Error in connection handler: {e}")

    # Processes incoming data from a WebSocket connection
    async def handle_data(self, data, websocket):
        try:
            data_json = json.loads(data)  # Parse the received JSON data
            command = data_json.get("command")  # Extract command from JSON

            # Handle different commands
            if command == "kill":
                print("Server shutdown requested")
                await self.close_all_connections()
                self.server.close()
                print("Server has been shut down by kill")
            elif command == "hello":
                print("Hello from client")
                response = {"response": "Hello from server"}
                await websocket.send(json.dumps(response))
            elif command == "create_announcement":
                # Extracting announcement details from the announcement
                announcement_data = data_json.get("data", {})
                title = announcement_data.get("title", "No title")
                body = announcement_data.get("body", "No body")
                dateTime = announcement_data.get("dateTime", "No date/time")
                creator = announcement_data.get("creator", "Anonymous")

                print(f"Announcement Received:\n"
                      f"  Title: {title}\n"
                      f"  Body: {body}\n"
                      f"  Date/Time: {dateTime}\n"
                      f"  Creator: {creator}")
            else:
                print("Unknown command received. Notified the client about it.")
                response = {"error": "Unknown command", "suggestion": "try 'hello', or 'kill', but second one is restricted"}
                await websocket.send(json.dumps(response))
        except json.JSONDecodeError:
            print("Invalid JSON received")

    # Closes all active WebSocket connections
    async def close_all_connections(self):
        for ws in set(self.server.websockets):
            await ws.close(code=1001, reason="Server shutdown")
