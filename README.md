
🤖 CDP Support Chatbot

This project is a Django-based chatbot designed to provide support and information regarding various Customer Data Platforms (CDPs) like Segment, mParticle, Lytics, and Zeotap. It uses TF-IDF (Term Frequency-Inverse Document Frequency) to find relevant answers from the documentation of these CDPs based on user queries.

🚀 Getting Started

Follow these steps to set up and run the chatbot on your local machine.

📋 Prerequisites-

o Python 3.6+
o pip (Python package installer)
o Virtual environment (recommended)

🛠️ Setup-

1.  Clone the repository:

    ```bash
    git clone <your_repository_url>
    cd <your_repository_directory>
    ```

2.  Create and activate a virtual environment (recommended):

    ```bash
    python -m venv venv

    # On Windows:
    venv\Scripts\activate

    # On macOS and Linux:
    source venv/bin/activate
    ```

3.  Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4.  Run migrations:

    ```bash
    python manage.py migrate
    ```

5.  Start the Django development server:

    ```bash
    python manage.py runserver
    ```

6.  Access the chatbot:

    Open your web browser and go to `http://127.0.0.1:8000/chatbot/`.


📂 Project Structure


CHATBOT_APP/                     # Root directory of the Django project
│── CDP_bot/                     # Main Django project directory (project settings and configurations)
│   │── __pycache__/              # Compiled Python files for optimization
│   │── __init__.py              # Marks this directory as a Python package
│   │── asgi.py                  # ASGI entry point for asynchronous support
│   │── settings.py               # Main Django settings file (database, installed apps, middleware, etc.)
│   │── urls.py                   # Project-level URL configurations
│   │── wsgi.py                   # WSGI entry point for deploying the project
│
│── chatapp/                      # Django app for chatbot functionality
│   │── __pycache__/              # Compiled Python files for optimization
│   │── migrations/               # Database migration files directory
│   │   │── __pycache__/          # Compiled migration files
│   │   │── __init__.py           # Marks this directory as a Python package
│   │── __init__.py               # Marks this directory as a Python package
│   │── admin.py                  # Admin panel configurations
│   │── apps.py                   # Application configuration
│   │── models.py                 # Database models (ORM)
│   │── tests.py                  # Test cases for the app
│   │── urls.py                   # App-level URL configurations
│   │── utils.py                  # Utility functions for chatbot operations
│   │── views.py                  # Views (API endpoints or page responses)
│
│── templates/chatapp/            # Directory for HTML templates
│   │── index.html                 # Frontend HTML file for the chatbot
│
│── venv/                         # Virtual environment for managing dependencies
│
│── .gitignore                    # Files to be ignored by Git
│── ~README.md                     # Temporary backup of README.md
│── cdp_docs_cache.json            # Cache file (probably related to documentation)
│── db.sqlite3                     # SQLite database file
│── demo_cache.sqlite              # Another SQLite cache database
│── manage.py                      # Django's command-line utility for managing the project
│── README.md                      # Project documentation
│── requirements.txt               # List of required dependencies for the project

![image](https://github.com/user-attachments/assets/a7c6b259-2042-4ecb-91ef-ccf3ae2d7134)

⚙️ How It Works

• Data Acquisition and Caching: The utils.py module fetches or loads data from specified CDP documentation URLs. It employs a caching mechanism (cdp_docs_cache.json) to store fetched data, minimizing redundant crawling.
• Text Processing and Indexing: Fetched text is segmented into sentences, and TF-IDF vectors are generated for indexing.
• Query Handling: User queries are processed, and TF-IDF vectors are generated.
• Similarity Matching: The system calculates cosine similarity between the query vector and indexed sentence vectors to find the most relevant answers.
• Response Generation: The chatbot returns the most relevant sentences along with their source URLs, providing users with accurate and contextually appropriate information.


🚀 Enhancements

• Advanced NLP Integration: Incorporate transformer-based models for enhanced semantic understanding.
• Interactive UI: Develop a more interactive and visually appealing user interface.
• Knowledge Base Expansion: Extend support to include a broader range of CDPs and documentation sources.
• Conversation Management: Implement features to manage conversation history and context for more coherent interactions.
• Performance Optimization: Optimize data processing and retrieval for faster response times.

