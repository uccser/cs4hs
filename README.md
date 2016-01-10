# CS4HS Website Generator

This project generates the website for the CS4HS Conference held at the University of Canterbury, New Zealand located at [cosc.canterbury.ac.nz/cs4hs](http://www.cosc.canterbury.ac.nz/cs4hs/index.html).

**Current Version:** 2015.7 (CS4HS 2015 post-conference)

## Overview

Running `generate.py` will produce all the necessary files for the website, that can be copied and placed on the appropriate web server. The script will generate HTML pages using Jinja2, and copy all images, files, css, and js into the output folder as well.

    cs4hs/
    ├── css/
    │   └── CSS files
    ├── files/
    │   └── Files available for users to download
    ├── img/
    │   └── Images files
    ├── js/
    │   └── JavaScript files
    ├── output/
    │   └── Files and folders produced by the website generator (ignored by Git)
    ├── templates/
    │   └── HTML files used by the template engine Jinja2
    ├── generate.py
    ├── LICENSE
    ├── README.md
    └── HTML files to be processed

### Why use a template engine?

Over the past few years the CS4HS website has been created with 'hard coded' pages (created in the amazing [Brackets](http://brackets.io/)). We now want to use a template engine to manage repetitive code, and this small Python script using Jinja2 achieves this. This project also prepares us for the website creation aspect of the [CSFG](https://github.com/uccser/cs-field-guide) project.

### Future plans

- Minify CSS on output.
- Use SCSS for managing CSS.

## Usage

Run `generate.py` and the website will be located within the the `output` folder.

## Requirements

- Python 3.4 or higher
- Jinja2 2.7.3 or higher (this is installed by the `generate.py` script if not installed already)

## Found a problem?

If you notice a problem, raise an [issue here](https://github.com/uccser/cs4hs/issues).

## Contributing

Forks and pull requests are welcome. We use [Vincent Driessen's Git Branching Model](http://nvie.com/posts/a-successful-git-branching-model/) for managing development.
