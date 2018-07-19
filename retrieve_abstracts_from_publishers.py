import re
from pprint import pprint

def strip_html_tags(my_str):

	my_str=re.sub(r'\<\/?.*?\>','',my_str)
	my_str=re.sub(r'\s\s+',' ',my_str)

	return my_str.strip()

def retrieve_pubmed_abstract(pubmed_id):

	with open('pubmed_ncbi.html','r') as f:
		html_lines=f.read().splitlines()

	html_lines=''.join(html_lines)
	my_re=re.search(r'\<.*?class="abstr".*?\>\<p\>(.+?)\</p\>.*?\<div.*?class=".*?"',html_lines)

	if my_re:
		return strip_html_tags(my_re.group(1))
	else:
		return False
		
def retrieve_doaj_abstract(doaj_id):

	with open('doaj.html','r') as f:
		html_lines=f.read().splitlines()

	html_lines=''.join(html_lines)
	my_re=re.search(r'\<div.*?class=".*?"\>.*?\<strong\>.*?Abstract.*?\<\/strong\>.*?\<p\>(.+?)\<\/p\>.*?\<div.*?class=".*?"',html_lines)

	if my_re:
		return strip_html_tags(my_re.group(1))
	else:
		return False

def retrieve_wos_abstract(wos_id):

	with open('wos.html','r') as f:
		html_lines=f.read().splitlines()

	html_lines=''.join(html_lines)
	my_re=re.search(r'\<div.*?class=".*?".*?\>.*?Abstract.*?\<\/div\>.*?\<p.*?\>(.+?)\<\/p\>.*?\<div.*?class=".*?"',html_lines)

	if my_re:
		return strip_html_tags(my_re.group(1))
	else:
		return False

def retrieve_scopus_abstract(scopus_id):

	with open('scopus.html','r') as f:
		html_lines=f.read().splitlines()

	html_lines=''.join(html_lines)
	my_re=re.search(r'\<\/section\>.*?\<.*?name="abstract".*?\>.*?\<p\>(.+?)\<\/p\>\<\/section\>',html_lines)

	if my_re:
		return strip_html_tags(my_re.group(1))
	else:
		return False

def retrieve_sciencedirect_abstract(sciencedirect_id):

	with open('sciencedirect.html','r') as f:
		html_lines=f.read().splitlines()

	html_lines=''.join(html_lines)
	my_re=re.search(r'class="section-title"\>Abstract\<\/.*?\<p.*?\>(.+?)\<\/p\>.*?\<.*?class=".*?"',html_lines)

	if my_re:
		return strip_html_tags(my_re.group(1))
	else:
		return False

def retrieve_europepmc_abstract(europepmc_id):

	with open('europepmc.html','r') as f:
		html_lines=f.read().splitlines()

	html_lines=''.join(html_lines)
	my_re=re.search(r'\<div id="abstract.*?property.*?\>(.+?)\<\/div',html_lines)

	if my_re:
		return strip_html_tags(my_re.group(1))
	else:
		return False

def retrieve_microsoft_academic_abstract(microsoft_academic_id):

	with open('microsoft_academic.html','r') as f:

		html_lines=f.read().splitlines()

	html_lines=''.join(html_lines)

	my_re=re.search(r'\<section class=".*?abstract.*?"\>.*?\<.*?\>(.+?)\<\/section',html_lines)

	if my_re:
		return strip_html_tags(my_re.group(1))
	else:
		return False

def retrieve_dimensions_app_abstract(dimensions_app_id):

	with open('dimensions_app.html','r') as f:

		html_lines=f.read().splitlines()

	html_lines=''.join(html_lines)

	my_re=re.search(r'\<div class="abstract.*?".+?\>(.+?)\<\/div',html_lines)

	if my_re:
		return strip_html_tags(my_re.group(1))
	else:
		return False

def retrieve_tandfonline_abstract(tandfonline_id):

	with open('tandfonline.html','r') as f:

		html_lines=f.read().splitlines()

	html_lines=''.join(html_lines)

	my_re=re.search(r'\<div.*?class="abstract.*?"\>.*?\<p.*?\>(.+?)\<div.*?class=".*?"',html_lines)

	if my_re:
		return strip_html_tags(my_re.group(1))
	else:
		return False

def retrieve_springer_link_abstract(springer_link_id):

	with open('springer_link.html','r') as f:

		html_lines=f.read().splitlines()

	html_lines=''.join(html_lines)

	my_re=re.search(r'\<section class="Abstract.+?\>(.+?)\<div class=".*?"',html_lines)

	if my_re:
		return strip_html_tags(my_re.group(1))
	else:
		return False

def retrieve_proquest_abstract(proquest_id):

	with open('proquest.html','r') as f:

		html_lines=f.read().splitlines()

	html_lines=''.join(html_lines)

	my_re=re.search(r'\<div class="abstract.+?id="abstractSum.*?\>\<p\>(.*?)\<\/p\>\<\/div\>\<script',html_lines)

	if my_re:
		return strip_html_tags(my_re.group(1))
	else:
		return False

def retrieve_iwaponline_abstract(iwaponline_id):

	with open('iwaponline.html','r') as f:

		html_lines=f.read().splitlines()

	html_lines=''.join(html_lines)

	my_re=re.search(r'\<.*?class="abstract"\>(.+?)\<a class=".*?"',html_lines)

	if my_re:
		return strip_html_tags(my_re.group(1))
	else:
		return False

def retrieve_scientific_net_abstract(scientific_net_id):

	with open('scientific_net.html','r') as f:

		html_lines=f.read().splitlines()

	html_lines=''.join(html_lines)

	my_re=re.search(r'\<div class="abstract-.*?".*?\>.*?\<p class.*?\>(.+?)\</div\>.*?\<div class=".*?"',html_lines)

	if my_re:
		return strip_html_tags(my_re.group(1))
	else:
		return False

def retrieve_acs_pubs_abstract(acs_pubs_id):

	with open('acs_pubs.html','r') as f:

		html_lines=f.read().splitlines()

	html_lines=''.join(html_lines)

	my_re=re.search(r'\<meta name="dc\.Description" content="(.+?)"\>\<',html_lines)

	if my_re:
		return strip_html_tags(my_re.group(1))
	else:
		return False

def retrieve_ingenta_connect_abstract(ingenta_connect_id):

	with open('ingenta_connect.html','r') as f:

		html_lines=f.read().splitlines()

	html_lines=''.join(html_lines)

	my_re=re.search(r'\<div id="Abst" class=".*?"\>(.+?)\<\/div',html_lines)

	if my_re:
		return strip_html_tags(my_re.group(1))
	else:
		return False

def retrieve_wiley_online_abstract(wiley_online_id):

	with open('wiley_online.html','r') as f:

		html_lines=f.read().splitlines()

	html_lines=''.join(html_lines)

	my_re=re.search(r'\<section class=".*?\>Abstract\<\/h.*?\>.*?\<div class=".*?"\>(.+?)\<\/div>.*?\<\/section',html_lines)

	if my_re:
		return strip_html_tags(my_re.group(1))
	else:
		return False

def retrieve_harvard_edu_abstract(harvard_edu_id):

	with open('harvard_edu.html','r') as f:

		html_lines=f.read().splitlines()

	html_lines=''.join(html_lines)

	my_re=re.search(r'\<h3.*?\>.*?Abstract\<\/h3\>(.+?)\<hr\>',html_lines)

	if my_re:
		return strip_html_tags(my_re.group(1))
	else:
		return False

def retrieve_rsc_pubs_abstract(rsc_pubs_id):

	with open('rsc_pubs.html','r') as f:

		html_lines=f.read().splitlines()

	html_lines=''.join(html_lines)

	my_re=re.search(r'\<h3 class=.*?\>Abstract\<\/h3>.*?\<div class=".+?"\>.*?\<p.*?\>(.+?)\<div class=".*?"',html_lines)

	if my_re:
		return strip_html_tags(my_re.group(1))
	else:
		return False

def retrieve_ieee_abstract(ieee_id):

	with open('ieee.html','r') as f:

		html_lines=f.read().splitlines()

	html_lines=''.join(html_lines)

	my_re=re.search(r'\<div class="abstract-text.*?\>(.+?)\<\/div\>',html_lines)

	if my_re:
		return strip_html_tags(my_re.group(1))
	else:
		return False

def retrieve_hindawi_abstract(hindawi_id):

	with open('hindawi.xhtml','r') as f:

		html_lines=f.read().splitlines()

	html_lines=''.join(html_lines)

	my_re=re.search(r'\<meta name="citation_abstract" content="(.+?)".*?\/\>',html_lines)

	if my_re:
		return strip_html_tags(my_re.group(1))
	else:
		return False

def retrieve_sciencesocieties_abstract(sciencesocieties_id):

	with open('sciencesocieties.html','r') as f:

		html_lines=f.read().splitlines()

	html_lines=''.join(html_lines)

	my_re=re.search(r'\<div class="section abstract".*?\<p id=".*?"\>(.+?)&nbsp;&nbsp;.*?(Please view the pdf by using the Full Text)?.*?\<span xmlns=""\>Copyright',html_lines)

	if my_re:
		return strip_html_tags(my_re.group(1))
	else:
		return False

sciencesocieties_id=1
retrieve_sciencesocieties_abstract(sciencesocieties_id)

rsc_pubs_id=1
retrieve_rsc_pubs_abstract(rsc_pubs_id)

pubmed_id=1
retrieve_pubmed_abstract(pubmed_id)

doaj_id=1
retrieve_doaj_abstract(doaj_id)

wos_id=1
retrieve_wos_abstract(wos_id)

scopus_id=1
retrieve_scopus_abstract(scopus_id)

sciencedirect_id=1
retrieve_sciencedirect_abstract(sciencedirect_id)

europepmc_id=1
retrieve_europepmc_abstract(europepmc_id)

microsoft_academic_id=1
retrieve_microsoft_academic_abstract(microsoft_academic_id)

dimensions_app_id=1
retrieve_dimensions_app_abstract(dimensions_app_id)

tandfonline_id=1
retrieve_tandfonline_abstract(tandfonline_id)

springer_link_id=1
retrieve_springer_link_abstract(springer_link_id)

proquest_id=1
retrieve_proquest_abstract(proquest_id)

iwaponline_id=1
retrieve_iwaponline_abstract(iwaponline_id)

scientific_net_id=1
retrieve_scientific_net_abstract(scientific_net_id)

acs_pubs_id=1
retrieve_acs_pubs_abstract(acs_pubs_id)

ingenta_connect_id=1
retrieve_ingenta_connect_abstract(ingenta_connect_id)

wiley_online_id=1
retrieve_wiley_online_abstract(wiley_online_id)

harvard_edu_id=1
retrieve_harvard_edu_abstract(harvard_edu_id)

rsc_pubs_id=1
retrieve_rsc_pubs_abstract(rsc_pubs_id)

ieee_id=1
retrieve_ieee_abstract(ieee_id)

hindawi_id=1
retrieve_hindawi_abstract(hindawi_id)