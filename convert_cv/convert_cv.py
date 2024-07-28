#!/usr/bin/env python
# encoding: utf-8

r"""Script to convert CV contents into publications in hugo format.

Note the paper entry is defined in Latex as follows:
 \newcommand{\PaperEntry}[6]{
		\noindent #1, ``\href{#6}{#2}", \textit{#3}, #4 (#5).}
Where:
	1 = author list
	2 = title
	3 = publication venue
	4 = where conference located
	5 = year
	6 = URL

An example is:
\PaperEntry{Ndousse, K., Eck, D., Levine, S., \& \underline{Jaques, N.}}
			{Learning Social Learning}
			{NeurIPS Cooperative AI Workshop \textbf{Best Paper} }
			{Virtual}
			{2020}
			{https://arxiv.org/abs/2010.00581}

The script will then create a new folder for the publication and insert a cite.bib
and index.md file. An empty index.md can be found in this directory.
"""

import os
import sys
from datetime import datetime

BASE_PATH = '/Users/natashajaques/Developer/professional_website'  #/usr/local/google/home/natashajaques/developer/professional_website
CV_PATH = os.path.join(BASE_PATH, 'convert_cv/cv.tex')
PUB_PATH = os.path.join(BASE_PATH, 'content/publication')
MD_PATH = os.path.join(BASE_PATH, 'convert_cv/empty_pub.md')
TRUNCATE_TITLES = 70
DATE_FORMAT = '"%Y-%m-%dT%H:%M:%SZ"'

# Paper titles of publications that have already been created under different directory names
# Or which should not be replaced because of custom features
ALREADY_ADDED = ["Emergent Social Learning via Multi-agent Reinforcement Learning",
				 "Learning Social Learning",
				 "Emergent Complexity and Zero-Shot Transfer via Unsupervised Environment Design",
				 "Social and Affective Machine Learning",
				 "Way Off-Policy Batch Deep Reinforcement Learning of Implicit Human Preferences in Dialog",
				 "Multi-task Learning for Predicting Health, Stress, and Happiness",
				 "Personalized Multitask Learning for Predicting Tomorrow's Mood, Stress, and Health",
				 "Predicting students' happiness from physiology, phone, mobility, and behavioral data",
				 "Interactive Musical Improvisation with Magenta",
				 "Predicting Affect in an Intelligent Tutoring System", 
				 "Environment Generation for Zero-Shot Compositional Reinforcement Learning"]


class Author:
	def __init__(self, first, last, contribution):
		self.first = first
		self.last = last
		self.contribution = contribution
		self.name = first + ' ' + last


class Publication:

	def __init__(self, title, authors, url, venue, location, year):
		self.title = title
		self.authors = authors
		self.url = url
		self.venue = venue
		self.location = location
		self.year = year
		self.extract_awards_from_venue()

		# Format title into directory name
		format_title = ''.join(e for e in title if e.isalnum() or e == ' ')
		self.dir_name = format_title.replace(' ', '-')[:TRUNCATE_TITLES]
		self.dir_path = os.path.join(PUB_PATH, self.dir_name)
		self.md_file_path = os.path.join(self.dir_path, 'index.md')
		self.bib_file_path = os.path.join(self.dir_path, 'cite.bib')

		# Find publication type
		""" 0 = Uncategorized; 1 = Conference paper; 2 = Journal article; 3 = Preprint / Working Paper; 
		4 = Report; 5 = Book; 6 = Book section;7 = Thesis; 8 = Patent """
		self.publication_type = '1'  # Conference paper
		if 'Journal' in venue or 'Transactions' in venue:
			self.publication_type = '2'  # Journal
		elif 'submitted' in location or 'Unpublished' in venue or 'preprint' in venue:
			self.publication_type = '3'  # Preprint
		elif 'Thesis' in location:
			self.publication_type = '7'  # Thesis

	def extract_awards_from_venue(self):
		awards_loc = self.venue.find('*')
		if awards_loc == -1:
			self.awards = ''
			return

		self.awards = self.venue[awards_loc:]
		self.venue = self.venue[:awards_loc].strip()

	def write_to_disk(self):
		if not os.path.exists(self.dir_path):
			os.makedirs(self.dir_path)

		# Load and overwrite markdown file
		md_lines = self.load_existing_markdown()
		md_lines = self.insert_info_into_markdown(md_lines)
		write_lines_to_file(self.md_file_path, md_lines)

		# Write cite.bib file
		bib_lines = self.generate_bib_entry_lines()
		write_lines_to_file(self.bib_file_path, bib_lines)
		
	
	def insert_info_into_markdown(self, md_lines):
		# Loop through to locate and replace title, date, publication, url
		# Keep track of author start/end lines to replace later
		for i, line in enumerate(md_lines):
			# Directly replace this info
			if 'title:' in line:
				md_lines[i] = 'title: "' + self.title +  '"\n'
			if 'date:' in line or 'publishDate:' in line:
				loc = line.find(':')
				date_type = line[:loc+1]
				date_str = line[loc+1:].strip()
				dt = datetime.strptime(date_str, DATE_FORMAT)
				dt = dt.replace(year=int(self.year))
				new_date_str = dt.strftime(DATE_FORMAT)
				md_lines[i] = date_type + ' ' + new_date_str + '\n'
			if 'publication:' in line or 'publication_short:' in line:
				pub_type = line[:line.find(':')+1]
				venue = self.venue
				if 'submitted' in self.location:
					venue += ' (submitted)'
				md_lines[i] = pub_type + ' In *' + venue + '* ' + self.awards + '\n'
			if 'publication_types:' in line:
				md_lines[i] = 'publication_types: ["' + self.publication_type + '"]\n'
			if 'url_pdf:' in line:
				existing_url = line[len('url_pdf: '):].strip()
				if 'http' in existing_url and existing_url != self.url:
					print("Eek! Not sure if it's okay to overwrite existing url for", self.title)
					print("Existing URL:", existing_url)
					print("CV URL:", self.url)
					response = input('Overwrite (o), keep existing (e) or quit (default)?')
					if response == 'o':
						md_lines[i] = 'url_pdf: ' + self.url +  '\n'
					elif response == 'e':
						continue
					else:
						print('Quitting!')
						sys.exit()
						import pdb; pdb.set_trace()  # should never get here
				else:
					md_lines[i] = 'url_pdf: ' + self.url +  '\n'

			# Track this info
			if 'authors:' in line:
				authors_idx = i
			if 'author_notes:' in line:
				author_notes_idx = i

		# Create markdown for authors & contributions
		author_lines = []
		contribution_lines = []
		for author in self.authors:
			if 'Jaques' in author.last:
				name = 'admin'
			else:
				name = author.name
			author_lines.append('- ' + name + '\n')
			contribution_lines.append('- ' + author.contribution + '\n')

		# Remove existing author lines and replace
		next_line_idx = authors_idx + 1
		while '- ' in md_lines[next_line_idx]:
			next_line_idx += 1
		md_lines = md_lines[:authors_idx+1] + author_lines + md_lines[next_line_idx:]

		# Remove existing contribution lines and replace
		lines_removed = next_line_idx - authors_idx - 1
		lines_added = len(author_lines)
		author_notes_idx += lines_added - lines_removed  # Adjust index for changed lines
		next_line_idx = author_notes_idx + 1
		while '- ' in md_lines[next_line_idx]:
			next_line_idx += 1
		md_lines = md_lines[:author_notes_idx+1] + contribution_lines + md_lines[next_line_idx:]

		return md_lines

	def load_existing_markdown(self):
		if os.path.exists(self.md_file_path):
			f = open(self.md_file_path, 'r')
			return f.readlines()
		else:
			f = open(MD_PATH, 'r')
			return f.readlines()

	def generate_bib_entry_lines(self):
		""" Generate a bibtex entry with the following format:
		@article{ndousse2020learning,
		  title={Learning Social Learning},
		  author={Ndousse, Kamal and Eck, Doug and Levine, Sergey and Jaques, Natasha},
		  journal={Internation Conference on Machine Learning (ICML)},
		  year={2021}
		}
		"""
		# Strip special characters for creating bib entry
		title_first_word = self.title.split(' ')[0].lower()
		title_first_word = ''.join(e for e in title_first_word if e.isalnum())
		first_author_last = self.authors[0].last.lower()
		first_author_last = ''.join(e for e in first_author_last if e.isalnum())
		
		# Entry and title
		lines = []
		lines.append('@article{' + first_author_last + self.year + title_first_word + ',\n')
		lines.append('\ttitle={' + self.title + '},\n')

		# Authors
		authors_line = '\tauthor={'
		for i, author in enumerate(self.authors):
			if i > 0:
				authors_line += ' and '
			authors_line += author.last + ', ' + author.first
		lines.append(authors_line + '},\n')

		# Journal and year
		if self.publication_type != '3':
			lines.append('\tjournal={' + self.venue + '},\n')
		lines.append('\tyear={' + self.year + '},\n')
		lines.append('}\n')

		return lines


def parse_paper_entry(line):
	line = fix_formatting(line)

	# Extract authors
	raw_authors, offset = extract_next_component(line)
	authors = parse_authors(raw_authors)

	# Extract title
	title, offset = extract_next_component(line, offset)

	# Skip entries that have been manually curated (usually featured pubs)
	if title in ALREADY_ADDED:
		print(title, 'has already been added, skipping.')
		return False

	# Extract remaining info
	venue, offset = extract_next_component(line, offset)
	location, offset = extract_next_component(line, offset)
	year, offset = extract_next_component(line, offset)
	url, offset = extract_next_component(line, offset)

	# Verify we reached the end of the entry
	if(offset != len(line) - 2):  # Subtract two for '\n'
		import pdb; pdb.set_trace()

	# Create publication
	pub = Publication(title, authors, url, venue, location, year)
	return pub

def remove_format(line, cmd=r'\underline', replace_with=''):
	"""Returns true if an underline was removed"""
	underline_i = line.find(cmd)
	if underline_i == -1:
		return line, False
	close_bracket_i = line[underline_i:].find('}') + underline_i
	new_str = line[:underline_i] + replace_with + \
			  line[underline_i+len(cmd + '{'):close_bracket_i] + replace_with + \
			  line[close_bracket_i+1:]
	return new_str, True

def fix_formatting(line):
	# Remove accent aigu
	line = line.replace("\\'{a}", 'a')

	# Remove all underlines
	line, format_removed = remove_format(line)
	while format_removed:
		line, format_removed = remove_format(line)

	# Replace all bolds
	line, format_removed = remove_format(line, cmd='\\textbf', replace_with='**')
	while format_removed:
		line, format_removed = remove_format(line, cmd='\\textbf', replace_with='**')
	return line

def extract_next_component(line, offset=0):
	remaining_line = line[offset+1:]
	open_bracket_i = remaining_line.find('{')
	close_bracket_i = remaining_line.find('}')
	component = remaining_line[open_bracket_i+1:close_bracket_i]
	return component, close_bracket_i + offset + 1

def parse_authors(raw_authors):
	raw_authors = raw_authors.replace('. \\&', '., \\&')
	raw_authors = raw_authors.replace('.*,', '*.,')
	author_list = raw_authors.split('.,')
	author_list = [a for a in author_list if a != '']
	authors = []

	for i, author in enumerate(author_list):
		if '*' in author:
			contribution = '"Equal contribution"'
			author = author.replace('*', '')
		else:
			contribution = '""'

		comma_loc = author.find(',')
		last = author[:comma_loc]
		last = last.replace('\\&', '').strip()
		initials = author[comma_loc+1:]
		if initials[-1] != '.':
			initials += '.'
		initials = initials.strip()
		authors.append(Author(initials, last, contribution))

	return authors

def write_lines_to_file(path, lines):
	f = open(path, "w")
	for line in lines:
	    f.write(line)
	f.close()

def main():
	f = open(CV_PATH, 'r')
	lines = f.readlines()
	for i, line in enumerate(lines):
		if '\PaperEntry' in line and 'newcommand' not in line:
			print('Found paper entry at line', i)
			pub = parse_paper_entry(line)
			if pub:
				pub.write_to_disk()
				print('Wrote files for', pub.title)
	print('Finished finding paper entries')

if __name__ == "__main__":
    main()
