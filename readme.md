# Python API Integration Test

This project is a Python application designed to demonstrate API integration. It fetches current weather data from the OpenWeatherMap API for a predefined list of cities and writes the results to a newly created Google Sheet using the Google Sheets API. This was developed as a submission for a technical assessment.

---

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python:** Version 3.8 or higher is required (3.10.6 recommended).
- **Git:** Required for cloning the repository.

---

## Configuration

To run this application, you must configure API access for both Google Cloud and OpenWeatherMap.

### 1. Google Cloud Credentials

The script requires OAuth 2.0 credentials to access the Google Sheets and Drive APIs on your behalf.

1.  Enable the **Google Drive API** and **Google Sheets API** in your Google Cloud Project.
2.  Create an **OAuth 2.0 Client ID** for a **Desktop app**.
3.  Download the generated JSON credential file.
4.  Place the file in the root of the project directory and rename it to **`client_secret.json`**.

For detailed instructions, refer to the official gspread documentation on OAuth Client ID for End-Users: https://docs.gspread.org/en/latest/oauth2.html#for-end-users-using-oauth-client-id

### 2. OpenWeatherMap API Key

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
