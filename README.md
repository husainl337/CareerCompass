# CareerCompass
AI-powered career recommendation engine with personalized feedback system to guide your professional journey.

## Installation

### Prerequisites

- Node.js and npm
- Python 3.x and pip
- Django
- NLTK

### Backend Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/chandima2000/career-path-recommendation-system.git
    cd career-path-recommendation-system/prediction
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
      ```
4. Create .env file inside prediction folder:

   GOOGLE_API_KEY = "YOUR_API_KEY"

5. Run the Django server:
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

### Frontend Setup

1. Navigate to the frontend directory:
    ```bash
    cd ../frontend
    ```

2. Install the dependencies:
    ```bash
    npm install
    ```

3. Run the React development server:
    ```bash
    npm run dev
    ```
