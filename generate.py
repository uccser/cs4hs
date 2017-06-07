
""" CS4HS Website Generator
AUTHOR: Jack Morgan
REQUIRES: Python >= 3.4.1
"""

CURRENT_DIRECTORY = '.'
OUTPUT_DIRECTORY = './output/'
TEXT_FOLDER = './text/'
FOLDERS_TO_COPY = ['css', 'files', 'img', 'js']

import os
import os.path
import shutil
import argparse
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
            os.chmod(file_name, 0o644)
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
        os.chmod(dest_folder, 0o2775)
        apply_file_permissions_to_folder(dest_folder)
        print("Copied {} folder".format(folder))


def apply_file_permissions_to_folder(folder_name):
    for root, folders, files in os.walk(folder_name):
        for folder in folders:
            folder_path = os.path.join(root, folder)
            os.chmod(folder_path, 0o2775)
        for file_name in files:
            file_path = os.path.join(root, file_name)
            os.chmod(file_path, 0o644)


def command_line_args():
    """Setup arg parser, and add required argument handling. Return
    namespace generated by parser arguments
    """
    argsparser = argparse.ArgumentParser(description='CS4HS Generator Argument')

    argsparser.add_argument('--pre-conference', '-p',
                            dest='pre_conference',
                            action='store_true',
                            help='Creates only index page for pre-conference')

    return argsparser.parse_args()


def main():
    """Create template engine and process all HTML files
    in the top directory"""
    cmd_args = command_line_args()

    website_generator = WebsiteGenerator()

    if cmd_args.pre_conference:
        files = ['pre-index.html']
    else:
        files = os.listdir(TEXT_FOLDER)
        files.remove('pre-index.html')

    # Render all HTML files in top directory
    for file in files:
        if file.endswith('.html'):
            file_path = os.path.join(TEXT_FOLDER, file)
            html = website_generator.render_html(file_path)
            if cmd_args.pre_conference:
                write_html(html, 'index.html')
            else:
                write_html(html, file)
    copy_files()


if __name__ == "__main__":
    main()
