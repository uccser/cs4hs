
""" CS4HS Website Generator
AUTHOR: Jack Morgan
REQUIRES: Python >= 3.4.1
"""

CURRENT_DIRECTORY = '.'
OUTPUT_DIRECTORY = './output/'
FOLDERS_TO_COPY = ['css', 'files', 'img', 'js']

"""Check and install dependencies"""
import pip
# Update pip if needed and install dependencies
pip.main(['install', '--upgrade', 'pip>=7.0.3'])
pip.main(['install', 'jinja2>=2.7.3'])

import os
import os.path
import shutil
from jinja2 import Environment, FileSystemLoader


class WebsiteGenerator:
    """Object for generating CS4HS website"""
    def __init__(self):
        # Load files from this folder and templates folder
        self.env = Environment(loader=FileSystemLoader([CURRENT_DIRECTORY, 'templates/']))

    def render_html(self, template):
        """Return a rendered template"""
        return self.env.get_template(template).render()


def write_html(html, file):
    """Render each file to output folder"""
    file_name = os.path.join(OUTPUT_DIRECTORY, file)
    try:
        with open(file_name, 'w', encoding='utf8') as output_file:
            output_file.write(html)
            print('Created {}'.format(file))
    except:
        print("Cannot write {0}".format(file))


def copy_files():
    """Copy all required files to destination folder"""
    for folder in FOLDERS_TO_COPY:
        src_folder = os.path.join(CURRENT_DIRECTORY, folder)
        dest_folder = os.path.join(OUTPUT_DIRECTORY, folder)
        if os.path.exists(dest_folder):
            shutil.rmtree(dest_folder)
        shutil.copytree(src_folder, dest_folder)
        print("Copied {} folder".format(folder))


def main():
    """Create template engine and process all HTML files
    in the top directory"""
    website_generator = WebsiteGenerator()
    files = os.listdir(CURRENT_DIRECTORY)
    # Render all HTML files in top directory
    for file in files:
        if file.endswith('.html'):
            html = website_generator.render_html(file)
            write_html(html, file)
    copy_files()


if __name__ == "__main__":
    main()
