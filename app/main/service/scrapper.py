# coding: utf-8

"""
Scrappers
"""

from bs4 import BeautifulSoup
import requests


def get_page_source(url: str) -> str:
	"""Downloads website's source
	"""
	res = requests.get(url)
	return res.content


def scrap_text(url: str) -> str:
	"""Some basic scrapper
	"""
	html_page = get_page_source(url)
	soup = BeautifulSoup(html_page, 'html.parser')
	text = soup.find_all(text=True)

	output = ''
	blacklist = [
		'[document]',
		'noscript',
		'header',
		'html',
		'meta',
		'head',
		'input',
		'script',
	]

	for t in text:
		if t.parent.name not in blacklist:
			output += f'{t} '

	return output


def scrap_images(url: str):
	"""Scraps all images
	"""
	html = get_page_source(url)
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup.findAll('img')
	for i, tag in enumerate(tags):
		if not tag['src'].startswith('http'):
			tag['src'] = url + tag['src']
		download_image(tag['src'], f'{i}.png')


def download_image(url: str, target_fname: str):
	"""Downloads an image
	"""
	with open(target_fname, 'wb') as file_handler:
		file_handler.write(requests.get(url).content)
