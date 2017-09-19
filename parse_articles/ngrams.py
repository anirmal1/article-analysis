import newspaper

# Returns list of tuples of (article text, bias factor)
def get_articles_text_and_bias(source_papers, news_sources):
	articles_text_and_bias = []
	for news_source in news_sources:
		bias_factor = news_sources[news_source]['bias_factor']
		for article in source_papers[news_source].articles:
			article.download()
			article.parse()
			text = article.text
			articles_text_and_bias.append((text, bias_factor))
	return articles_text_and_bias

# params
#	n : n-gram
#	articles_text_and_bias : list of tuples
def get_ngrams(n, articles_text_and_bias):
	pass
