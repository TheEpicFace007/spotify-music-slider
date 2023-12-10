// ==UserScript==
// @name         Spotify Slider WebSocket Client
// @namespace    https://github.com/TheEpicFace007/spotify-music-slider
// @version      0.1
// @description  Connect to WebSocket server for Spotify Slider
// @author       Charlie
// @match        http*://open.spotify.com/*
// @grant        GM_xmlhttpRequest
// @license      GPL-3.0
// ==/UserScript==

(function() {
    'use strict';

    // Adjust the WebSocket server URL accordingly
    const wsServerURL = 'ws://localhost:13337';
    let didConnected = false;

    // Function to establish a WebSocket connection
    let connectIntervalLoop;
    function connectWebSocket() {
        const socket = new WebSocket(wsServerURL);

        socket.onopen = function(event) {
            console.log('WebSocket connection opened:');
            // You can send a message after the connection is established, if needed
            // socket.send('connected');
            didConnected = true;
            if (typeof connectIntervalLoop == "number"  && didConnected){
                if (connectIntervalLoop){
                    clearInterval(connectIntervalLoop);
                    connectIntervalLoop = null;
                }
                console.log("Sucessfully reconnected")
            }
        }

        socket.onmessage = function(event) {
            console.log('WebSocket message received:', event.data);
            // Handle the received message from the server
            // Example: Update volume on the page
            if (event.data.startsWith('vol:')) {
                const volume = Number(event.data.substring(4));
                console.log("volume: %d", volume)

                // Update the volume on the page
                // Example: document.getElementById('volumeElementId').innerText = 'Volume: ' + volume;
            }
        }

        socket.onclose = function(event) {
            console.log('WebSocket connection closed:', event);
            didConnected = false;
            socket.close(200);

            connectIntervalLoop = setInterval(() => {
                console.log("Attempting to reconnect...");
                if (didConnected !== null || didConnected !== undefined ){
                    connectWebSocket();
                }
            }, 10_000);
        }
    }

    // Wait for the page to fully load before connecting to WebSocket
    window.addEventListener('load', function() {
        connectWebSocket();
        // }
    });

})();
