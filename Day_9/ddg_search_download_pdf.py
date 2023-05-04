from duckduckgo_search import ddg

keywords = 'open source intelligence filetype:pdf'
results = ddg(keywords, region='us-en', safesearch='Off', time='y', download=True)
