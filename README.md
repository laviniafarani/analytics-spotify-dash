# Spotify Dash

This project leverages the Spotify API to create an interactive dashboard that displays various music-related insights. **Please note that this project is still under construction, and features are being actively developed.**

## Setup Instructions
Follow these steps to set up and run the project on your local machine.

### **Set Up a Virtual Environment**
To keep dependencies isolated, it’s recommended to set up a virtual environment.

1. Navigate to Your Project Directory:<br>
Open your terminal and navigate to the root directory of the project:

    ```bash
    cd /path/to/your/project
    ```

2. Create the Virtual Environment:<br>
Run the following command to create a virtual environment named venv:

    ```bash
    python3 -m venv venv
    ```
3. Activate the Virtual Environment:

    Linux/macOS:
    ```bash
    source venv/bin/activate
    ```

    Windows (PowerShell):
    ```powershell
    .\venv\Scripts\Activate
    ```

4. Install the Project Dependencies:<br>
With the virtual environment activated, install the necessary python packages by running:

    ```bash
    pip install -r requirements.txt
    ```


### Configure the .env File
To access the Spotify API, you'll need to set up authentication credentials.

1. Obtain Spotify API Credentials:<br>
Follow the Spotify [Getting Started Guide](https://developer.spotify.com/documentation/web-api/tutorials/getting-started#create-an-app) to create an app and retrieve your `client_id`, `client_secret`, and `redirect_uri`.

2. Create and Configure the .env File: <br>
In the root directory of your project, create a .env file and add the following variables:

    ```plaintext
    SPOTIFY_CLIENT_ID=your-client-id
    SPOTIFY_CLIENT_SECRET=your-client-secret
    SPOTIFY_REDIRECT_URI=your-redirect-uri
    ```

    Replace `your-client-id`, `your-client-secret`, and `your-redirect-uri` with your actual Spotify API credentials.

### Run the Project
With everything set up, you can now run the project.

Ensure the Virtual Environment is Activated:
If it’s not already activated, follow the activation steps in the Set Up a Virtual Environment section.

- Execute the Main Script<br>
Run the following command to start the application:

    ```bash
    python3 main.py
    ```
