# Build The Earth Guide
[![Documentation Status](https://readthedocs.org/projects/bteguide/badge/?version=latest)](https://bteguide.readthedocs.io/en/latest/?badge=latest)

Hey! If you're here, you're probably looking for the source, aren't you? Looking to contribute? Perfect!

## Contributing

We're using Sphinx with ReadTheDocs to run the Guide. For those unfamiliar with it, we suggest you look into the [basics of reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html). We do have the option for Markdown, however i18n may become an issue, so going forward we will be investing in Sphinx.

To setup your development environment, run `pip install -r requirements.txt`

We've included `sphinx-autobuild` with the guide, so if you want to use live-reload, run `make livehtml` (or `./make.bat livehtml`) and visit http://localhost:8000 to see your changes.

## Translation

We're working on enabling proper i18n for the guide! Ping **Xylotrupes#6278** or **EzraEn#4291** to have your work included!
