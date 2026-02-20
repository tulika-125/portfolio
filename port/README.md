# Tulika Mahato - Portfolio Dashboard with AI Chatbot

A minimalist, dashboard-style portfolio website built with Flask, HTML, CSS, and an integrated AI chatbot powered by Groq.

## Features

- **Dashboard UI**: Clean, responsive grid layout displaying profile, skills, education, projects, and certifications.
- **AI Chatbot**: A context-aware chatbot (Llama 3.3 via Groq) that answers questions about Tulika's background and skills directly from her resume.
- **Resume Download**: One-click download of the official PDF resume.
- **Responsive Design**: Works seamlessly on desktop and mobile devices.

## Prerequisites

- **Python 3.8+**
- **Groq API Key**: You need an API key from [Groq Cloud](https://console.groq.com/).

## Installation

1.  **Clone or Download** this repository.
2.  **Navigate to the project directory**:
    ```bash
    cd path/to/portfolio
    ```
3.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configure Environment Variables**:
    - Create a `.env` file in the root directory.
    - Add your Groq API key:
      ```env
      GROQ_API_KEY=your_groq_api_key_here
      ```
      *(Note: The project is currently configured with a provided key, but for security, ensure `.env` is not shared publicly.)*

## Usage

1.  **Run the Application**:
    ```bash
    python app.py
    ```
2.  **Open in Browser**:
    Navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000).

## Project Structure

- `app.py`: Main Flask application containing routes and chatbot logic.
- `static/`:
  - `style.css`: Custom CSS for the dashboard and chat widget.
  - `chat.js`: Frontend JavaScript for handling chat interactions.
- `templates/`:
  - `base.html`: Base HTML layout.
  - `dashboard.html`: The main portfolio content page.
- `tulika.pdf`: The resume file served for download and used as context (extracted text).
- `requirements.txt`: Python dependencies.

## Customization

- **Modify Content**: Update the `data` dictionary in `app.py` to add new projects or skills.
- **Styling**: Edit `static/style.css` to change the color scheme or layout.
- **Chatbot Context**: Edit the `SYSTEM_PROMPT` in `app.py` to change how the AI behaves or what it knows.

## Technologies

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **AI/LLM**: Groq API (Llama 3.3-70b-versatile)
- **PDF Processing**: pypdf

## Deployment on Render (Recommended)

1.  **Create a New Web Service**:
    - Connect your GitHub repository: `https://github.com/tulika-125/portfolio.git`
    - Render will automatically detect the `Procfile` and `requirements.txt`.
2.  **Configuration**:
    - **Environment**: `Python 3`
    - **Build Command**: `pip install -r requirements.txt`
    - **Start Command**: `gunicorn app:app`
3.  **Environment Variables**:
    - Go to the **Environment** tab in your Render service settings.
    - Add `GROQ_API_KEY` with your actual API key from [Groq Cloud](https://console.groq.com/).
4.  **Automatic Deploy**:
    - Once configured, every push to the `main` branch will trigger a fresh deployment.
