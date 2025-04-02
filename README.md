# Ascii bot

This Python bot participates in an r/place-like art event using ASCII art ("artscii"). It fetches pixel instructions from a server and automatically draws them on the canvas.

## Overview

This project consists of a client bot and a server.

* **Client:** Periodically requests pixel data from the server and uses the `artscii` command-line tool to draw those pixels on the art canvas.
* **Server:** Transforms images into a series of pixel instructions (coordinates, foreground color, background color) and serves this data to the client bots.

This setup allows multiple users running this bot to collaboratively create a larger ASCII art piece

## Usage

1.  **Ensure the server is running:** This bot relies on a server providing the pixel data. Start the server application.
2.  **Configure flags:** By default some flags for debugging purposes are turned on by default. Make sure to change server urls and turn these off.
3.  **Run the bot:** Execute the Python script. It will continuously fetch and draw pixels.

## TODO

* Implement a smarter drawing algorithm to avoid redrawing correct pixels.
* Implement synchronization mechanisms for collaborative drawing (e.g., for animations).
