
# # chatbot_app/utils.py
# import requests
# from bs4 import BeautifulSoup
# from transformers import AutoTokenizer, AutoModel
# import torch

# tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-mpnet-base-v2")
# model = AutoModel.from_pretrained("sentence-transformers/all-mpnet-base-v2")

# def fetch_and_extract_text(url):
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         soup = BeautifulSoup(response.content, 'html.parser')
#         text = soup.get_text(separator='\n', strip=True)
#         return text
#     except requests.exceptions.RequestException as e:
#         print(f"Error fetching URL: {e}")
#         return None

# def mean_pooling(model_output, attention_mask):
#     token_embeddings = model_output[0]  # First element of model_output contains all token embeddings
#     input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
#     sum_embeddings = torch.sum(token_embeddings * input_mask_expanded, 1)
#     sum_mask = torch.clamp(input_mask_expanded.sum(1), min=1e-9)
#     return sum_embeddings / sum_mask

# def get_embeddings(texts):
#     encoded_input = tokenizer(texts, padding=True, truncation=True, return_tensors='pt')
#     with torch.no_grad():
#         model_output = model(**encoded_input)
#     sentence_embeddings = mean_pooling(model_output, encoded_input['attention_mask'])
#     return sentence_embeddings

# def index_documentation():
#     cdp_docs = {
#         "Segment": "https://segment.com/docs/",
#         "mParticle": "https://docs.mparticle.com/",
#         "Lytics": "https://docs.lytics.com/",
#         "Zeotap": "https://docs.zeotap.com/home/en-us/",
#     }
#     indexed_data = {}
#     for cdp, url in cdp_docs.items():
#         text = fetch_and_extract_text(url)
#         if text:
#             sentences = text.split('.') #Very simple sentence split.
#             embeddings = get_embeddings(sentences)
#             indexed_data[cdp] = {"sentences": sentences, "embeddings": embeddings}
#     return indexed_data


# # chatbot_app/utils.py
# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urljoin, urlparse
# from transformers import AutoTokenizer, AutoModel
# import torch
# import time
# import nltk
# import logging

# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-mpnet-base-v2")
# model = AutoModel.from_pretrained("sentence-transformers/all-mpnet-base-v2")

# def fetch_and_extract_text(url, timeout=10):
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
#     }
#     try:
#         response = requests.get(url, headers=headers, timeout=timeout)
#         response.raise_for_status()
#         soup = BeautifulSoup(response.content, 'html.parser')
#         text = soup.get_text(separator='\n', strip=True)
#         return text
#     except requests.exceptions.RequestException as e:
#         logging.error(f"Error fetching URL {url}: {e}")
#         return None

# def mean_pooling(model_output, attention_mask):
#     token_embeddings = model_output[0]
#     input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
#     sum_embeddings = torch.sum(token_embeddings * input_mask_expanded, 1)
#     sum_mask = torch.clamp(input_mask_expanded.sum(1), min=1e-9)
#     return sum_embeddings / sum_mask

# def get_embeddings(texts):
#     try:
#         encoded_input = tokenizer(texts, padding=True, truncation=True, return_tensors='pt')
#         with torch.no_grad():
#             model_output = model(**encoded_input)
#         sentence_embeddings = mean_pooling(model_output, encoded_input['attention_mask'])
#         return sentence_embeddings
#     except Exception as e:
#         logging.error(f"Error in get_embeddings: {e}")
#         return None

# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# def crawl_and_index(base_url, indexed_data, visited_urls, max_depth=3, current_depth=0):
#     start_time = time.time()
#     time.sleep(1)
#     if base_url in visited_urls or current_depth > max_depth:
#         return

#     try:
#         logging.info(f"Crawling {base_url}")
#         text = fetch_and_extract_text(base_url)
#         if text:
#             sentences = nltk.sent_tokenize(text)
#             if sentences:
#                 embeddings = get_embeddings(sentences)
#                 if embeddings is not None:
#                     indexed_data[base_url] = {"sentences": sentences, "embeddings": embeddings}
#                     logging.info(f"Indexed {len(sentences)} sentences from {base_url}")
#                 else:
#                     logging.warning(f"embeddings where None for {base_url}")

#             visited_urls.add(base_url)

#             soup = BeautifulSoup(requests.get(base_url).content, 'html.parser')

#             for link in soup.find_all('a', href=True):
#                 absolute_url = urljoin(base_url, link['href'])
#                 if urlparse(absolute_url).netloc == urlparse(base_url).netloc and absolute_url.startswith(urlparse(base_url).scheme):
#                     crawl_and_index(absolute_url, indexed_data, visited_urls, max_depth, current_depth + 1)
#         logging.info(f"Crawling {base_url} finished in {time.time() - start_time} seconds")
#     except Exception as e:
#         logging.error(f"Error crawling {base_url}: {e}")

# def index_all_cdp_docs():
#     cdp_docs = {
#         "Segment": "https://segment.com/docs/?ref=nav",
#         "mParticle": "https://docs.mparticle.com/",
#         "Lytics": "https://docs.lytics.com/",
#         "Zeotap": "https://docs.zeotap.com/home/en-us/",
#     }
#     indexed_data = {}
#     visited = set()
#     for cdp, url in cdp_docs.items():
#         crawl_and_index(url, indexed_data, visited)
#     return indexed_data


# chatbot_app/utils.py
# chatbot_app/utils.py
import requests
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
import time
import logging
import json
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
nltk.download('punkt')

CACHE_FILE = "cdp_docs_cache.json"

def fetch_and_extract_text(url, timeout=10):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text(separator='\n', strip=True)
        return text
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching URL {url}: {e}")
        return None

def crawl_and_index_specific_urls(urls):
    indexed_data = {}
    for url in urls:
        try:
            logging.info(f"Crawling {url}")
            text = fetch_and_extract_text(url)
            if text:
                sentences = nltk.sent_tokenize(text)
                indexed_data[url] = {"sentences": sentences}
                logging.info(f"Indexed {len(sentences)} sentences from {url}")
        except Exception as e:
            logging.error(f"Error crawling {url}: {e}")
    return indexed_data

def load_or_crawl_data(urls):
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            logging.warning("Cache file corrupted, recrawling.")
            os.remove(CACHE_FILE)

    indexed_data = crawl_and_index_specific_urls(urls)
    with open(CACHE_FILE, "w") as f:
        json.dump(indexed_data, f)
    return indexed_data

def get_tfidf_response(question, indexed_documents, cdp_filter=None):
    best_match = {"similarity": -1, "sentence": "I'm sorry, I cannot answer that question.", "url": ""}

    for url, data in indexed_documents.items():
        if cdp_filter:
            if cdp_filter not in url:
                continue

        sentences = data["sentences"]
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(sentences + [question])
        question_vector = tfidf_matrix[-1]
        sentence_vectors = tfidf_matrix[:-1]
        similarities = cosine_similarity(question_vector, sentence_vectors).flatten()
        best_similarity_index = similarities.argmax()

        if similarities[best_similarity_index] > best_match["similarity"]:
            best_match["similarity"] = similarities[best_similarity_index]
            best_match["sentence"] = sentences[best_similarity_index]
            best_match["url"] = url
    return f"{best_match['sentence']} (Source: {best_match['url']})"


