# from django.shortcuts import render
# from .utils import index_documentation, get_embeddings
# import torch
# import torch.nn.functional as F

# indexed_documents = index_documentation()

# def chatbot(request):
#     if request.method == 'POST':
#         question = request.POST.get('question', '')
#         answer = get_chatbot_response(question)
#         return render(request, 'index.html', {'question': question, 'answer': answer})
#     return render(request, 'index.html')

# def get_chatbot_response(question):
#     question_embedding = get_embeddings([question])
#     if "segment" in question.lower():
#         return find_answer(question_embedding, indexed_documents.get("Segment", None))
#     elif "mparticle" in question.lower():
#         return find_answer(question_embedding, indexed_documents.get("mParticle", None))
#     elif "lytics" in question.lower():
#         return find_answer(question_embedding, indexed_documents.get("Lytics", None))
#     elif "zeotap" in question.lower():
#         return find_answer(question_embedding, indexed_documents.get("Zeotap", None))
#     else:
#         return "I'm sorry, I cannot answer that question. Please ask a question related to Segment, mParticle, Lytics, or Zeotap."

# def find_answer(question_embedding, document_data):
#     if document_data is None:
#         return "Documentation not available."

#     sentences = document_data["sentences"]
#     embeddings = document_data["embeddings"]

#     similarities = F.cosine_similarity(question_embedding, embeddings)
#     best_match_index = torch.argmax(similarities).item()

#     if best_match_index < len(sentences):
#         return sentences[best_match_index]
#     else:
#         return "I could not find a relevant answer in the documentation."




# # chatbot_app/views.py
# from django.shortcuts import render
# from .utils import index_all_cdp_docs, get_embeddings
# import torch

# indexed_documents = index_all_cdp_docs() #Index on server start.

# def chatbot(request):
#     if request.method == 'POST':
#         question = request.POST.get('question', '')
#         answer = get_chatbot_response(question)
#         return render(request, 'index.html', {'question': question, 'answer': answer})
#     return render(request, 'index.html')

# def get_chatbot_response(question):
#     question_embedding = get_embeddings([question])
#     best_match = {"similarity": -1, "sentence": "I'm sorry, I cannot answer that question. Please ask a question related to Segment, mParticle, Lytics, or Zeotap.", "url": ""}

#     for url, data in indexed_documents.items():
#         sentences = data["sentences"]
#         embeddings = data["embeddings"]
#         similarities = torch.nn.functional.cosine_similarity(question_embedding, embeddings)

#         best_similarity, best_index = torch.max(similarities, 0)
#         if best_similarity > best_match["similarity"]:
#             best_match["similarity"] = best_similarity.item()
#             best_match["sentence"] = sentences[best_index.item()]
#             best_match["url"] = url

#     return f"{best_match['sentence']} (Source: {best_match['url']})"



# # chatbot_app/views.py
# from django.shortcuts import render
# from .utils import load_or_crawl_data, get_tfidf_response


# SPECIFIC_URLS = [
#     "https://segment.com/docs/?ref=nav",
#     "https://docs.mparticle.com/",
#     "https://docs.lytics.com/",
#     "https://docs.zeotap.com/home/en-us/",
#     # "https://docs.mparticle.com/guides/",
#     # "https://docs.mparticle.com/developers/",
#     # "https://docs.mparticle.com/integrations/",
#     # "https://docs.mparticle.com/developers/apis/json-reference/",
#     # "https://docs.mparticle.com/developers/apis/http/",
#     # "https://docs.mparticle.com/developers/client-sdks/web/",
#     # "https://docs.mparticle.com/developers/client-sdks/ios/",
#     # "https://docs.mparticle.com/developers/client-sdks/android/",
#     # "https://docs.mparticle.com/developers/quickstart/android/overview/"
# ]

# indexed_documents = load_or_crawl_data(SPECIFIC_URLS)

# def chatbot(request):
#     if request.method == 'POST':
#         question = request.POST.get('question', '')
#         answer = get_tfidf_response(question, indexed_documents)
#         return render(request, 'index.html', {'question': question, 'answer': answer})
#     return render(request, 'index.html')

# chatbot_app/views.py
from django.shortcuts import render
from .utils import load_or_crawl_data, get_tfidf_response

SPECIFIC_URLS = [
"https://segment.com/docs/?ref=nav",
"https://segment.com/docs/connections/spec/semantic/",
"https://segment.com/docs/connections/spec/common/",
"https://segment.com/docs/connections/spec/",
"https://segment.com/docs/guides/how-to-guides/",
"https://segment.com/docs/getting-started/",
    
    "https://docs.mparticle.com/",
    "https://docs.mparticle.com/guides/",
    "https://docs.mparticle.com/developers/",
    "https://docs.mparticle.com/integrations/",
    "https://docs.mparticle.com/developers/apis/json-reference/",
    "https://docs.mparticle.com/developers/apis/http/",
    "https://docs.mparticle.com/developers/client-sdks/web/",
    "https://docs.mparticle.com/developers/client-sdks/ios/",
    "https://docs.mparticle.com/developers/client-sdks/android/",
    "https://docs.mparticle.com/developers/quickstart/android/overview/"



"https://docs.lytics.com/",
"https://docs.lytics.com/docs/developer-quickstart",
"https://docs.lytics.com/reference/post_job-adroll-sync",
"https://docs.lytics.com/changelog",
"https://docs.lytics.com/discuss",
"https://docs.lytics.com/docs/what-is-vault",

"https://docs.zeotap.com/home/en-us/",
"https://docs.zeotap.com/articles/#!get-started-guide/getting-started/",
"https://docs.zeotap.com/articles/#!unify-customer/unify",
"https://docs.zeotap.com/articles/#!segment-customer/segment",
"https://docs.zeotap.com/articles/#!integrate-customer/integrate",
"https://docs.zeotap.com/articles/#!orchestrate-customer/orchestrate",
"https://docs.zeotap.com/articles/#!dashboard-customer/overview",

  
]

indexed_documents = load_or_crawl_data(SPECIFIC_URLS)

def chatbot(request):
    if request.method == 'POST':
        question = request.POST.get('question', '')
        cdp = None
        if "segment" in question.lower():
            cdp = "segment"
        elif "mparticle" in question.lower():
            cdp = "mparticle"
        elif "lytics" in question.lower():
            cdp = "lytics"
        elif "zeotap" in question.lower():
            cdp = "zeotap"

        answer = get_tfidf_response(question, indexed_documents, cdp_filter=cdp)
        return render(request, 'index.html', {'question': question, 'answer': answer})
    return render(request, 'index.html')