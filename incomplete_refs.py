import os,re,sys,html
from urllib.request import urlopen
from pprint import pprint

def convert_nonsense(my_str):

	if isinstance(my_str, str):
		my_str=html.unescape(my_str)
		return my_str
	else:
		my_str=[html.unescape(x) for x in my_str]
		return my_str

def retrieve_science_direct(art_url):

	try:
		html = urlopen(art_url)
		#print(html)
		mybytes = html.read()
		the_page = mybytes.decode("utf8")
		html.close()
	except:
		return 'Error 1'

	m=re.search(r'class.*?\>Abstracts?\<(.*?)\<\/div\>', the_page)
	try:
		abstract=convert_nonsense(m.group(1))
		abstract=re.sub(r'\<.*?\>','',abstract)
		print(abstract)
	except:
		print(the_page)
		print(art_url)
		sys.exit()
		return 'Error 1'

def detect_refs_with_no_abstract_available():

	my_refs=[]
	#for path, subdirs, files in os.walk('../'):
	for path, subdirs, files in os.walk('../../Google Scholar'):
	    for name in files:
	        my_refs.append(os.path.join(path, name))

	#print(list(set([x[-3:] for x in my_refs])))

	ris_files=[x for x in my_refs if x[-3:]=='ris']

	ris_refs_dict=dict()

	index=0

	for ris in ris_files:

		ris_refs=[]
		with open(ris, 'r') as f: 

			my_lines=f.readlines()
			my_lines
			split_range_a=0
		
			for i in range(len(my_lines)-2):
				#if re.match(r'\n',my_lines[i]) and re.match(r'\n',my_lines[i+1]):
				#	if re.match(r'\n',my_lines[i+2]):
				if re.match(r'\n',my_lines[i]):
						split_range_b=i
						ris_refs.append([x for x in my_lines[split_range_a:split_range_b]])
						split_range_a=i+1

		ris_refs.append([x for x in my_lines[split_range_a:]])

		for my_ref in ris_refs:

			art_title=''
			art_abstract=''

			for line in my_ref:
				#print(line)

				m1=re.search(r'^T[1|I]  - (.*?)$',line)
				if m1:
					art_title=convert_nonsense(m1.group(1))

				m2=re.search(r'^AB  - (.*?)$',line)
				if m2:
					art_abstract=convert_nonsense(m2.group(1))

				m3=re.search(r'^UR  - (.*?)$',line)
				if m3:
					art_url=convert_nonsense(m3.group(1))

			if re.search('Abstract not available', art_abstract) or art_abstract=='':
				print(art_url)
				#if re.search('sciencedirect',art_url):
				#	retrieve_science_direct(art_url)
				#	ris_refs_dict[index]=[art_title,art_abstract,art_url]
			index+=1

	sys.exit()

	return ris_refs_dict

ris_refs_dict=detect_refs_with_no_abstract_available()
pprint(ris_refs_dict)

#ore_files=[x for x in my_refs if x[-3:]=='ore']
#enw_files=[x for x in my_refs if x[-3:]=='enw']
#ciw_files=[x for x in my_refs if x[-3:]=='ciw']

	#pprint(ris_refs_dict)

'''my_lines=re.sub(r'\n','',my_lines)
m=re.findall(r'^([A-Z])+  - ',my_lines)
#m=re.search(r'TI  - (.*?) [A-Z]+  - ',my_lines)
if m:
	art_title=m.group(1)
	print('\n------------------------------------------\n')
	print()
	print(ris)
	print()
	print('Title:',art_title)
	print()
	print('\n------------------------------------------\n')
else:
	print('\n------------------------------------------\n')
	print()
	print(ris)
	print()
	print(lines)
	print()
	print('\n------------------------------------------\n')
'''