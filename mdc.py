import markdown2
import codecs

md = codecs.open('09-09-2014.txt', 'r').read()

html = markdown2.markdown(md.decode('utf-8').encode('ascii', 'xmlcharrefreplace'))

file('09-09-2014.html', 'w').write(html)