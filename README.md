***This project has been replaced by the [cs4teachers system](https://github.com/uccser/cs4teachers), and has been archived.***

---

# CS4HS Website Generator

This project generates the website for the CS4HS workshops held at the University of Canterbury, New Zealand located at [cosc.canterbury.ac.nz/cs4hs](http://www.cosc.canterbury.ac.nz/cs4hs/index.html).

## Overview

Running `generate.py` will produce all the necessary files for the website, that can be copied and placed on the appropriate web server. The script will generate HTML pages using Jinja2, and copy all images, files, css, and js into the output folder as well. This program is not as efficient in generation as the [CSFG](https://github.com/uccser/cs-field-guide) project, however it does get the job done.

    cs4hs/
    ├── css/
    │   └── Files to style the website output
    ├── files/
    │   └── Files available for users to download through the website
    ├── img/
    │   └── Images to display on the website
    ├── js/
    │   └── JavaScript used in the website output
    ├── output/
    │   └── Files and folders produced by the website generator (ignored by Git)
    ├── templates/
    │   └── HTML files used by the template engine Jinja2
    ├── text/
    │   └── HTML files used to create pages by the template engine Jinja2
    ├── .gitignore
    ├── generate.py
    ├── LICENSE
    └── README.md

### Why use a template engine?

Over the past few years the CS4HS website has been created with 'hard coded' pages (created in the amazing [Brackets](http://brackets.io/)). We now want to use a template engine to manage repetitive code, and this small Python script using Jinja2 achieves this. This project prepared us for the website creation aspect of the [CSFG](https://github.com/uccser/cs-field-guide) project.

### Future plans

- Switch to an existing static site generator (Middleman, Jekyll, etc)

## Usage

Run `generate.py` and the website will be located within the the `output` folder.

## Requirements

- Python 3.4 or higher
- Jinja2 2.7.3 or higher (this is installed by the `generate.py` script if not installed already)

## Found a problem?

If you notice a problem, raise an [issue here](https://github.com/uccser/cs4hs/issues).

## Contributing

Forks and pull requests are welcome. We use [Vincent Driessen's Git Branching Model](http://nvie.com/posts/a-successful-git-branching-model/) for managing development.
