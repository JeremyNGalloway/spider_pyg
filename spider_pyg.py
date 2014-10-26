import requests
from lxml import html
import urlparse

url = 'http://rthrservices.com/'

def get_child_links(parent_url):
		linkIsTooLong = False
		edited_local_links = set()
		if len(parent_url) > 999:
			print "Long URL is loooong"
			linkIsTooLong = True
		if not linkIsTooLong:
			try:
				r = requests.get(parent_url, timeout=10)
			except (requests.exceptions.ConnectTimeout,requests.exceptions.ReadTimeout,requests.exceptions.ConnectionError):
				print parent_url + " timed out after 10 seconds\n"
			if not 'text/html' in r.headers['Content-Type']:
				pass
			tree = html.fromstring(r.text)
			#print parent_url
			all_links = [x[2] for x in tree.iterlinks()]
			# for link in all_links:
			# 	print link
			local_links = set([str(link) for link in all_links if link.startswith("/")])
			hard_links = set([str(link) for link in all_links if link.startswith(parent_url)])
			for link in hard_links:
				print link
			for link in local_links:
				if link.startswith('/'):
					link = urlparse.urljoin(parent_url, link)
					if link.startswith(url):
						edited_local_links.add(link)
			#parent_urls = link in local_links if link.notstartswith("ht")])
			#print local_links
		return edited_local_links



master_set = local_links = get_child_links(url)
count = 0

while count < 10:
	for link in local_links:
		if link.startswith(url):
			master_set = master_set | (get_child_links(link))  #union child link set and master set
			count = count + 1
		else:
			pass


for i in master_set:
	print i


#to_parse = {}    #dic to hold url (key) + link (values)
#for url in urls:
#	to_parse[url] = set([])  #build dict key

#print to_parse



#for url in urls:
#	base_url = url
#	get_child_links(url)


