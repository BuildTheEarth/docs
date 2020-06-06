Contributing to this Guide
============

Requirements
------------
All contributors will need these things:

* A Text Editor
* Git
* Python >3.6
* A Github Account

Whether you're translating or just adding new information, these will be your tools, so get familiar with them! If you need help getting set up, contact us in `#support <https://discordapp.com/channels/690908396404080650/691034211464773684>`_. If noone responds, DM ``@EzraEn#4291``.


We're using Sphinx with ReadTheDocs to run the Guide. For those unfamiliar with it, we suggest you look into the `basics of reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_. We do have the option for Markdown, however many features are not supported by it (e.g., tables, other common extensions), so going forward we will be investing in Sphinx.

Resources
~~~~~~~~~

Git/Github
""""""""""
See the **Github Flow** section, it's pretty good.
https://guides.github.com/introduction/git-handbook/#basic-git
https://guides.github.com/activities/forking/
If you use VSCode, I `highly recommend` using GitLens. Seriously. It helps. A lot. 

reST
""""
These are a few highly recommended resources we've found on getting started with reST/rST.

https://docs.typo3.org/m/typo3/docs-how-to-document/master/en-us/WritingReST/CheatSheet.html
https://stackoverflow.com/questions/2746692/restructuredtext-tool-support/2747041#2747041
https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#tables
https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html
If you're using VSCode (seeing a trend?) definitely install the `reStructuredText <https://marketplace.visualstudio.com/items?itemName=lextudio.restructuredtext>`_ extension.

Setting up your Environment
---------------------------

Once you have `Git configured with your Github Account <>`_, make a new directory and open Git there. Fork this repo and clone your version of it to your new directory.

Once you've got your version of the repo cloned, run ``pip -r requirements.txt`` in the working directory and wait for everything to install. 

To contribute directly to the source files, find them in /source/. 
If you are looking to create a new document, make sure the corresponding ``index.rst`` for it's directory includes it in it's `toctree` directive. This applies whether you choose to write in Markdown or reStructuredText (preferred). 


Translating
-----------

Once you've done all of the above, translating is the next step for every document that is added.
In order to streamline the translation process, we suggest using `Poedit <https://poedit.net>`_ for modifying the .po files. If you're familiar with platforms like CrowdIn, this will be a similar process, however everything must be done locally. 

If you language is already in the process of being translated, you will find it in a Git branch in the format `lang-xx`, where xx is the `Language code <https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes>`_ as listed under the 639-1 column.

If your target language hasn't been started on yet, you can create the branch yourself by running these commands:

**Windows:**
.. code-block::
    git checkout -b lang-xx
    ./make.bat gettext
    sphinx-intl update -p build/gettext -l xx

**Linux/Other:**
.. code-block::
    git checkout -b lang-xx
    make.bat gettext
    sphinx-intl update -p build/gettext -l xx

Once that's done, you may start editing the .po files in /locale/xx/.


Optional Quality-of-Life
------------------------

You can install `sphinx-autobuild` with the guide, though it only seems to be compatible with Python versions less than 3.8. We don't recommend installing an older version of Python just for that, but if you really want to, you can. If you find that the package `does work` with 3.8, please notify ``@EzraEn#4291`` as we'd like to see that as a default install. 

Installing sphinx-autobuild is as simple as ``pip install sphinx-autobuild``.
If you want to use live-reload, run ``make livehtml`` (or ``./make.bat livehtml``) and visit http://localhost:8000 to see your changes.