# Simple Welcome Web Application

## Story: KAN-124

A minimal Flask web application that displays a welcome message when accessing the home page.

## Features

- Single endpoint (`/`) that returns "Hello Neurostack User"
- Returns HTTP 200 OK response
- Runs on port 5000

## Requirements

- Python 3.11+
- pip

## Setup

1. Clone the repository:
```bash
git clone https://github.com/parth-vadodaria-itp/neurostack_mini_sdlc_workflow_test_1.git
cd neurostack_mini_sdlc_workflow_test_1
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Copy the example environment file:
```bash
cp .env.example .env
```

5. Run the application:
```bash
python app.py
```

The application will start on `http://localhost:5000/`

## Usage

Navigate to `http://localhost:5000/` in your browser to see the welcome message.

## Acceptance Criteria

- ✅ The application starts successfully without errors
- ✅ Navigating to `http://localhost:5000/` displays "Hello Neurostack User"
- ✅ The endpoint returns an HTTP 200 OK response
- ✅ No additional pages or APIs are required

## Technology Stack

- **Language**: Python 3.11
- **Framework**: Flask 3.x
- **Package Manager**: pip

## Project Structure

```
.
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
├── README.md
├── config.py
├── app.py
├── routes/
│   ├── __init__.py
│   └── welcome_routes.py
├── models/
│   └── __init__.py
└── services/
    └── __init__.py
```