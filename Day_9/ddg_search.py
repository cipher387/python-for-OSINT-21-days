from duckduckgo_search import ddg

keywords = 'osint'
results = ddg(keywords, region='us-en', safesearch='Off', time='y')
print(results)
