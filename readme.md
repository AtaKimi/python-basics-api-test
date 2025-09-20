# Python API Integration Test

This project is a Python application designed to demonstrate API integration. It fetches current weather data from the OpenWeatherMap API for a predefined list of cities and writes the results to a newly created Google Sheet using the Google Sheets API. This was developed as a submission for a technical assessment.

---

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python:** Version 3.8 or higher is required (3.10.6 recommended).
- **Git:** Required for cloning the repository.

---

## Configuration

### 3. Google Cloud Project Setup (OAuth 2.0)
 
​This script uses OAuth 2.0 to authenticate as a regular Google user. Because the app is in "Testing" mode, you must add authorized users who can grant permission.

​1. Create a Google Cloud Project

​Go to the Google Cloud Console. ​Click the project drop-down menu at the top of the page and click "New Project". ​Give your project a name (e.g., "Python Sheets API") and click "Create".

​2. Enable the APIs

​You need to enable the Google Drive and Google Sheets APIs for your new project. ​In your new project, navigate to the "APIs & Services" dashboard. ​Click on "+ ENABLE APIS AND SERVICES".
​Search for and enable the following two APIs:
a. ​Google Drive API
b. ​Google Sheets API

​3. Configure the OAuth Consent Screen

​This screen is what users see when they grant the script permission.

​Go to "APIs & Services" -> "OAuth consent screen".
​Select "External" as the user type and click "CREATE".

​Fill in the required fields (App name, User support email, Developer contact email). 
​Click "SAVE AND CONTINUE" until you get to the "Test users" page.

​Important: Leave the app in its default "Testing" status. Do not publish it.

​4. Add Test Users

​While your app is in testing mode, only registered test users can authorize it.

​On the "OAuth consent screen" page, click the "+ ADD USERS" button in the "Test users" section.
​Enter the Google email address (@gmail.com) of the person who will be running the script. You can add multiple emails.

​Click "SAVE". The user is now authorized to use your app.

​5. Create an OAuth 2.0 Client ID

​This will generate the credentials.json file your script needs.

​Go to "APIs & Services" -> "Credentials". Click "+ CREATE CREDENTIALS" and select "OAuth client ID".

​For the "Application type", select "Desktop app".
​Give it a name (e.g., "Desktop Client 1") and click "CREATE".

​A window will pop up. Click "DOWNLOAD JSON".

​6. Final Steps

​Rename the downloaded JSON file to credentials.json and move it into your project's root directory.

​Run the script for the first time. A browser window will open, asking you to log in to the Google account you added as a test user.

To run this application, you must configure API access for both Google Cloud and OpenWeatherMap.

### 2. Google Cloud Credentials

The script requires OAuth 2.0 credentials to access the Google Sheets and Drive APIs on your behalf.

1.  Enable the **Google Drive API** and **Google Sheets API** in your Google Cloud Project.
2.  Create an **OAuth 2.0 Client ID** for a **Desktop app**.
3.  Download the generated JSON credential file.
4.  Place the file in the root of the project directory and rename it to **`client_secret.json`**.

For detailed instructions, refer to the official gspread documentation on OAuth Client ID for End-Users: https://docs.gspread.org/en/latest/oauth2.html#for-end-users-using-oauth-client-id

### 3. OpenWeatherMap API Key

An API key is required to fetch data from the OpenWeatherMap service.

1.  Sign up for an account on the OpenWeatherMap website.
2.  Obtain an API key by subscribing to an appropriate plan, such as the "One Call by Call" subscription.
3.  Create a new file named **`.env`** in the project root by making a copy of the **`.env.copy`** template.
4.  Open the `.env` file and set the `WEATHER_API_KEY` variable to the key you obtained.

Further details can be found in the OpenWeatherMap API documentation: https://openweathermap.org/api/one-call-3

---

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/AtaKimi/python-basics-api-test.git](https://github.com/AtaKimi/python-basics-api-test.git)
    cd python-basics-api-test
    ```
2.  **Create and activate a virtual environment (recommended):**

    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

To execute the application, run the main script from the project's root directory:

```bash
python script.py
```

There is a link on where the script is created on the command line. It could be used to access the created google sheet.
