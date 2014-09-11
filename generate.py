import feedparser
from hn import HN
import time
from random import randint
import urllib2
import json

hn = HN()

def space():
	section = []
	feed = feedparser.parse('http://www.nasa.gov/rss/dyn/image_of_the_day.rss')
	section.append('NASA Image of the Day')
	section.append('---------------------\n')
	section.append('![IOTD](' + feed.entries[0]['links'][1]['href'] + ')\n') #image url
	section.append(feed.entries[0]['description'][0:250] + '...\n') #description)
	section.append('[Read More...](' + feed.entries[0]['link'] + ')\n') #entry url

	return section

def nasa():
	section = []
	feed = feedparser.parse('http://www.nasa.gov/rss/dyn/universe.rss')
	for entry in feed.entries[1:10]:
		print entry.title

def xkcd():
	section = []
	req = urllib2.urlopen('http://xkcd.com/info.0.json')
	maxNum = json.loads(req.read().decode('utf8'))['num']
	comicNum = str(randint(1, maxNum))
	req = urllib2.urlopen('http://xkcd.com/' + comicNum + '/info.0.json')
	comicData = json.loads(req.read().decode('utf8'))
	section.append('Random XKCD Comic')
	section.append('-----------------\n')
	section.append('[' + comicData['title'] + '](http://xkcd.com/' + str(comicData['num']) + ')\n')
	section.append('![' + comicData['title'] + '](' + comicData['img'] + ')\n')
	section.append('[Read More...](http://xkcd.com)\n')

	return section

def topX(url, limit, home):
	section = []
	feed = feedparser.parse(url)
	section.append(feed['feed']['title'])
	section.append('----------------------------------')

	for entry in feed.entries[0:limit]:
		section.append("+ [" + entry.title + "](" + entry.link + ")")

	section.append("\n[Read More...](" + home + ")")
	return section

def hackaday():
	section = []
	feed = feedparser.parse('http://feeds2.feedburner.com/hackaday/LgoM')
	section.append(feed['feed']['title'])
	section.append('----------------------------------')

	for entry in feed.entries[0:5]:
		section.append("+ [" + entry.title + "](" + entry.link + ")")
		# try:
		# 	section.append("<img src='" + entry.media_content[2]['url'] +"'>")
		# except:
		# 	pass
	section.append("\n[Read More...](http://hackaday.com)")
	return section

def infog(url):
	section = []
	feed = feedparser.parse(url)
	num = randint(0, len(feed.entries))
	section.append(" + [" + feed.entries[num]['title'] + "](" + feed.entries[num]['link'] + ")")
	return section
	
def hackerNews():
	section = []
	section.append('HackerNews')
	section.append('----------------------------------')

	for story in hn.get_stories(story_type='', limit=5):
		section.append(" + [" + story.title + "](" + story.link + ")")

	section.append("\n[Read More...](http://news.ycombinator.com)")
	return section

def topTor():
	section = []
	section.append('Top Pirated Movies')
	section.append('----------------------------------')
	feed = feedparser.parse('http://kickass.to/movies/?rss=2')
	for entry in feed.entries:
		print entry['title']

def whatIf():
	section = []
	feed = feedparser.parse('https://what-if.xkcd.com/feed.atom')
	section.append("XKCD 'what-if' of the week")
	section.append('---------------------------\n')
	section.append(feed.entries[0]['summary'] + '\n')
	section.append('[Read More...](http://what-if.xkcd.com)')

	return section

def build():
	today = time.strftime("%m-%d-%Y")
	letter = open(today + '.txt', 'w').close
	letter = open(today + '.txt', 'a')

	letter.write( 'IHackEverything Newsletter - ' + today + '\n')
	letter.write( '=======================================' + '\n')
	letter.write( """The following links are automatically pulled from their respected websites 
each day and delivered straight to you for your convenience!  View the source at [Github!](http://github.com/kf5jak/newsletter)  Enjoy!\n(Be sure to allow images from this sender if you haven't already!)\n""")
	letter.write( '_______________________________________\n')
	letter.write('\n\n')

	print 'Retrieving XKCD Comic'
	for line in xkcd():
		letter.write(line.encode('ascii', 'ignore') + '\n')

	print 'Retrieving CNN'
	for line in topX('http://rss.cnn.com/rss/cnn_topstories.rss', 2, 'http://cnn.com'):
		letter.write(line.encode('ascii', 'ignore') + '\n')

	letter.write('\n')

	print 'Retrieving Wired'
	for line in topX('http://feeds.wired.com/wired/index', 5, 'http://wired.com'):
		letter.write(line.encode('ascii', 'ignore') + '\n')

	letter.write('\n')

	print 'Retrieving Art Of Manliness'
	for line in topX('http://www.artofmanliness.com/feed/', 5, 'http://www.artofmanliness.com'):
		letter.write(line.encode('ascii', 'ignore') + '\n')

	letter.write('\n')

	print 'Retrieving HackerNews'
	for line in hackerNews():
		letter.write(line.encode('ascii', 'ignore') + '\n')

	letter.write('\n')

	print 'Retrieving RollingStone'
	for line in topX('http://www.rollingstone.com/movies/reviews.rss', 5, 'http://rollingstone.com'):
		letter.write(line.encode('ascii', 'ignore') + '\n')

	letter.write('\n')

	print 'Retrieving HackADay'
	for line in hackaday():
		letter.write(line.encode('ascii', 'ignore') + '\n')

	letter.write('\n')

	print 'Retrieving IGN'
	for line in topX('http://feeds.ign.com/ign/games-all?format=xml', 5, 'http://ign.com'):
		letter.write(line.encode('ascii', 'ignore') + '\n')

	letter.write('\n')

	print 'Retrieving iflscience'
	for line in topX('http://www.iflscience.com/rss.xml', 5, 'http://iflscience.com'):
		letter.write(line.encode('ascii', 'ignore') + '\n')

	letter.write('\n')

	print 'Retrieving lifehacker'
	for line in topX('http://lifehacker.com/rss', 5, 'http://lifehacker.com'):
		letter.write(line.encode('ascii', 'ignore') + '\n')

	letter.write('\n')

	print 'Retrieving Infograph from Mashable'
	letter.write('Infograph (Mashable)'+'\n')
	letter.write('----------------------------------' + '\n')
	for line in infog('http://mashable.com/category/mashable-infographics/rss/'):
		letter.write(line.encode('ascii', 'ignore') + '\n')

	letter.write('\n')

	print 'Retrieving XKCD what-if article'
	for line in whatIf():
		letter.write(line.encode('utf8') + '\n')

build()






