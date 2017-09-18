# Newspaper documentation https://newspaper.readthedocs.io/en/latest/
import newspaper

# Based on chart shown in Business Insider article 
# http://www.businessinsider.com/what-your-preferred-news-outlet-says-about-your-political-ideology-2014-10
news_sources = {
	'BBC': {
		'url': 'http://www.bbc.com/news',
		'bias': 'liberal',
		'bias_factor': 3.5
	},
	'Fox': {
		'url': 'http://www.foxnews.com/',
		'bias': 'conservative',
		'bias_factor': 2
	},
	'Al Jazeera': {
		'url': 'http://www.aljazeera.com/news/',
		'bias': 'liberal',
		'bias_factor': 5
	},
	'Breitbart': {
		'url': 'http://www.breitbart.com/',
		'bias': 'conservative',
		'bias_factor': 6
	},
	'Drudge Report': {
		'url': 'http://www.drudgereport.com/',
		'bias': 'conservative',
		'bias_factor': 4.5
	},
	'Blaze': {
		'url': 'http://www.theblaze.com/',
		'bias': 'conservative',
		'bias_factor': 6
	},
	'Slate': {
		'url': 'http://www.slate.com/',
		'bias': 'liberal',
		'bias_factor': 5.5
	}
}

def get_articles(news_source):
	source_info = news_sources[news_source]
	print('Processing ' + news_source + '...', end='', flush=True)
	paper = newspaper.build(source_info['url'], memoize_articles=False)
	print(str(len(paper.articles)) + ' articles...')
	return paper

def list_news_sources(bias):
	for news_source in news_sources:
		if news_sources[news_source]['bias'] == bias:
			print(news_source)

def list_liberal_news_sources():
	print('### LIBERAL NEWS SOURCES ###')
	list_news_sources('liberal')
	print('')

def list_conservative_news_sources():
	print('### CONSERVATIVE NEWS SOURCES ###')
	list_news_sources('conservative')
	print('')

def process_news_sources():
	list_liberal_news_sources()
	list_conservative_news_sources()
	source_papers = {}
	for news_source in news_sources:
		paper = get_articles(news_source)
		source_papers[news_source] = paper
	print('Done processing news sources.')
	return source_papers

# TODO get rid of this after testing
def main():
	source_papers = process_news_sources()

if __name__ == '__main__':
	main()
