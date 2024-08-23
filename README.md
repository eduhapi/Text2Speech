To set up and use the `Text2Speech` project, a Python Django web application that converts text into MP3 audio using Google’s `gtts` library, follow these instructions:

### Overview

`Text2Speech` is a Django web application designed to convert text into speech and save it as an MP3 audio file using Google's `gtts` (Google Text-to-Speech) library. 
This project is useful for generating audio files from text content for various applications.

### Step-by-Step Installation and Usage Guide

#### 1. Clone the Repository

Begin by cloning the `Text2Speech` repository from GitHub to your local machine.

**Command:**
```bash
git clone https://github.com/eduhapi/Text2Speech.git
```

This command will create a local copy of the repository on your computer.

#### 2. Navigate to the Project Directory

Change your current directory to the `Text2Speech` project folder.

```bash
cd Text2Speech
```

#### 3. Set Up a Virtual Environment

To manage dependencies and avoid conflicts with other Python projects, set up a virtual environment.

**Create a virtual environment:**

- **Windows:**
  ```bash
  python -m venv venv
  ```

- **macOS/Linux:**
  ```bash
  python3 -m venv venv
  ```

**Activate the virtual environment:**

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```

- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

#### 4. Install the Required Dependencies

With the virtual environment activated, install the project's dependencies specified in the `requirements.txt` file.

**Command:**
```bash
pip install -r requirements.txt
```

This will install all the necessary libraries, including `gtts`.

#### 5. Apply Database Migrations

Set up the database schema by applying the migrations.

**Command:**
```bash
python manage.py migrate
```

This step initializes the database for your Django application.

#### 6. Run the Development Server

Start the Django development server to run the application locally.

**Command:**
```bash
python manage.py runserver
```

You can now access the application by opening a web browser and going to `http://127.0.0.1:8000/`.

#### 7. Use the Application

1. **Access the Text-to-Speech Interface:**
   - Navigate to the application’s URL in your web browser.

2. **Enter Text:**
   - Use the provided form to input the text you want to convert to speech.

3. **Generate MP3:**
   - Submit the form to generate an MP3 audio file of the entered text.

4. **Download the MP3 File:**
   - After processing, download the generated MP3 file from the provided link.

#### 8. Customize the Application

You can modify the application to suit specific needs, such as:
