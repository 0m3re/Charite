# Charité App

## Dependencies
To get started, ensure you have the following installed:
- Android Studio (latest version - visit the [official website](https://developer.android.com/studio))
- Python (latest version - visit the [official website](https://www.python.org/downloads/))
- Node.js (latest version) with npm (visit the [official website](https://nodejs.org/))
- NativeScript (latest version - can be installed with `npm install -g nativescript`)

## Installation
### The Project Itself
1. Clone the repository: `git clone [repository URL]`
2. Navigate to the project directory: `cd svelte_app`
3. Install Node dependencies: `npm install`

### Android Studio
1. Install Android Studio, ensuring the Virtual Device Manager is included.
2. Set the `ANDROID_HOME` environment variable.
3. Navigate to the SDK Manager and install the appropriate SDK (14.0) and SDK Tools (33.*).
4. Create a virtual device using the Virtual Device Manager, selecting the correct SDK.

## Usage
- To start the server, use `python main.py`. Ensure you are in the server folder or specify the path in the command.
- To start the NS app, use `ns run`. You must be in the svelte_app folder. Note: being in a subfolder will not work.
