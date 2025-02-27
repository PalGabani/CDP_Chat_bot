
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

