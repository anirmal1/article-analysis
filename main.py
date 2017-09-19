#!/usr/bin/python3.6
from parse_articles.news_sources import *
from parse_articles.ngrams import *

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

def main():
	source_papers = process_news_sources(news_sources)
	
if __name__ == '__main__':
	main()