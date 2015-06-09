# CS4HS Website Generator

This project generates the website for the CS4HS Conference held at the University of Canterbury, New Zealand located at [cosc.canterbury.ac.nz/cs4hs](http://www.cosc.canterbury.ac.nz/cs4hs/index.html).

## Overview

Running `generate.py` will produce all the necessary files for the website, that can be copied and placed on the appropriate web server. The script will generate HTML pages using Jinja2, and copy all images, files, css, and js into the output folder as well.

    cs4hs/
    ├── templates/
    │   └── HTML files used by the template engine Jinja2
    ├── output/
    │   └── Files produced by the website generator. Ignored by Git.
    ├── files/
    │   └── Files available for download
    ├── img/
    │   └── Images files
    ├── css/
    │   └── CSS files
    ├── js/
    │   └── JavaScript files
    ├── generate.py
    ├── README.md
    ├── LICENSE
    └── HTML files to be processed

## Usage

Run `generate.py` and the website will be located within the the `output` folder.

## Requirements

- Python 3.4 or higher

## Found a problem?

If you notice a problem, raise an [issue here](https://github.com/uccser/cs4hs/issues).

## Contributing

Forks and pull requests are welcome.
