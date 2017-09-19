# Newspaper documentation https://newspaper.readthedocs.io/en/latest/
import newspaper

def get_articles(news_source, source_info):
	print('Processing ' + news_source + '...', end='', flush=True)
	paper = newspaper.build(source_info['url'], memoize_articles=False)
	print(str(paper.size()) + ' articles...')
	return paper

def list_news_sources(bias, news_sources):
	for news_source in news_sources:
		if news_sources[news_source]['bias'] == bias:
			print(news_source)

def list_liberal_news_sources(news_sources):
	print('### LIBERAL NEWS SOURCES ###')
	list_news_sources('liberal', news_sources)
	print('')

def list_conservative_news_sources(news_sources):
	print('### CONSERVATIVE NEWS SOURCES ###')
	list_news_sources('conservative', news_sources)
	print('')

def process_news_sources(news_sources):
	list_liberal_news_sources(news_sources)
	list_conservative_news_sources(news_sources)
	source_papers = {}
	for news_source in news_sources:
		paper = get_articles(news_source, news_sources[news_source])
		source_papers[news_source] = paper
	print('Done processing news sources.')
	return source_papers
