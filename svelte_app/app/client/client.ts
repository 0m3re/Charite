// IMPORTS
require('@c4dt/nativescript-websockets');
import { writable } from 'svelte/store';

export const errorStore = writable("");  // Store for error messages
export const responseStore = writable("");  // Store for response messages

let ws: WebSocket | null = null;

// Creates a new WebSocket and sets up event listeners
function createWebSocket() {
    ws = new WebSocket('ws://10.0.2.2:8765', []);  // WebSocket connection: Using IP 10.0.2.2 to connect to a server running on the host machine from an Android emulator. Read Android Studio doc for more informations.

    // Event listener for when WebSocket connection opens
    ws.addEventListener('open', function (evt) {
        console.log("WebSocket connection opened");
    });

    // Event listener for receiving messages from the server
    ws.addEventListener('message', function(evt) {
        let data = JSON.parse(evt.data);
    
        // Handle different types of messages (error, response, or others)
        if (data.error) { 
            errorStore.set(data.error);
            console.log("Message from server:", data);
            setTimeout(() => errorStore.set(""), 5000);
        } else if (data.response) {
            responseStore.set(data.response);
            console.log("Message from server:", data);
            setTimeout(() => responseStore.set(""), 5000);
        } else {
            errorStore.set("");
            responseStore.set("");
            console.log("Message from server:", data);
        }
    });

    // Event listener for WebSocket connection closure
    ws.addEventListener('close', function(evt) {
        console.log("WebSocket connection closed:", evt.code, evt.reason);
        ws = null;
        if (evt.code === -1) {
            console.error("Can't open WebSocket, check if the server is running.");
        }
    });

    // Event listener for WebSocket connection errors
    ws.addEventListener('error', function(evt: Event) {
        const errorEvent = evt as ErrorEvent;
        console.error("WebSocket connection error:", errorEvent.message);
    });
}

// Function for connecting the Websocket
export function connectWebSocket() {
    if (!ws || ws.readyState === WebSocket.CLOSED) {
        createWebSocket();
    } else {
        console.warn('WebSocket is already open.');
    }
}

// Function to close the WEbsocket
export function closeWebSocket() {
    if (ws && ws.readyState === WebSocket.OPEN) {
        ws.close();
    } else {
        console.error('WebSocket is not connected');
    }
}

// Function to send messages to the server
export function sendMessage(command: string) {
    if (ws && ws.readyState === WebSocket.OPEN) {
        const message = JSON.stringify({ command });
        ws.send(message);
    } else {
        console.warn('WebSocket is not connected');
    }
}

// Function to send announcments to the server (beta)
export function sendAnnouncement(title: string, body: string, dateTime: string, creator: string) {
    if (ws && ws.readyState === WebSocket.OPEN) {
        const announcement = {
            command: "create_announcement",
            data: { title, body, dateTime, creator }
        };
        ws.send(JSON.stringify(announcement));
    } else {
        console.warn('WebSocket is not connected');
    }
}

// Function to KILL the server. Carefull dangerous :)
export function sendKill() {
    sendMessage("kill");
    if (ws) {
        ws.close();
    }
}