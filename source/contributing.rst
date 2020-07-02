Contributing to the Wiki
==========================

Prerequisites
-------------

Before you can start translating this wiki you will need to install a few programs and set up your environment to interface with the Github repository in order to collaborate with the wiki editors. You will need the following:

**Python Version 3.6 or higher**

Python is a programming language. You do not need to know any Python to help translating but we need the language installed to setup the environment.

| You can find the download here: `Python download <https://www.python.org/downloads/>`_.
| The `Hitchhiker's Guide to Python <https://docs.python-guide.org/starting/installation/>`_ has a short tutorial on how to install python properly using the command line.

**git**

Git is a decentralized version control system that allows you to synchronize changes in a folder with remote repositories. It also allows to revert changes and split off parts of a project in independent project-branches.

You can download it here: `Git download <https://git-scm.com/downloads>`_. 

**A Github account**

Github is a web interface for collaboration using remote git repositories. The wiki is created in such a remote repository. You will need an account to collaborate with the team.

Create an account here: `Github <https://github.com/>`_.

**A text editor**

We recommend a coding interface such as `VS Code <https://code.visualstudio.com/>`_ because it can handle all the git commands as well as the text editing so it will give you some quality of life features. However any kind of text editor would do the trick.

**If you want to translate**

The translation of this wiki works internally by creating portable object (.po) files for each language. These files simplify the translation of web interfaces. To work with .po files we recommend a dedicated .po editor such as Poedit.

Download it here: `Poedit download <https://poedit.net>`_.

**General**

Whether you're translating or just adding new information, these will be your tools, so get familiar with them! If you need help getting set up, contact us in `#support <https://discordapp.com/channels/690908396404080650/691034211464773684>`_ or open a ticket with the BTE Support Bot! If nobody responds, DM ``@EzraEn#4291``.

We're using Sphinx with ReadTheDocs to run the guide. For those unfamiliar with it, we suggest you look into the `basics of reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_. We do have the option for Markdown, however many features are not supported by it (e.g., tables, other common extensions), so going forward we will be investing in Sphinx.

Setting up the environment
--------------------------

After you have created a Github account click the **Fork** buttom at the top right of the `bte-guide Github page <https://github.com/EzraEn1/bteguide>`_. This will create a copy of the whole wiki project on your own Github account. You can work on this copy without affecting any of the code on the main wiki. If you are a translator and want to work on a language for which a translation is already in progress, you can also request your co-translator to accept you as a direct collaborator on their fork of the repository.

The next step is to create a clone of the fork on your computer. This clone will be an ordinary folder that can be synchronized to both your forked repo and the main BTE wiki.
Click the green :green:`'Clone or download'` button on the top right and copy the link that appears.
Then, go to the folder you want to work in.

**Windows**
Shift + Right-click in the folder and open the Terminal/Powershell. A Terminal window will open.

**If you are using git for the first time** you will need to register your name and your e-mail address. This is essential for your collaborators to identify which changes are made by you. Type in the following commands (use the middle mouse button to paste a copied text into the git console):

.. code-block:: 

    git config --global user.name "Your Username" 
    git config --global user.name

If everything is correct your username should be returned to you after the second command.

.. code-block:: 

    git config --global user.email "email@example.com"
    git config --global user.email

Again, your e-mail address should be returned after the second command.

We can now **clone your github repository** and connect it to the main wiki for synchronization.

.. code-block:: 

    git clone [your link]
    cd .\bteguide
    git remote add upstream https://github.com/EzraEn1/bteguide.git

This downloads the repository into the folder you chose it will appear as a folder named **bteguide**. Now run:

.. code-block::

    cd .\bteguide
    pip install -r requirements.txt

This will install all packages you need to work on the wiki.
Congratulations! You are now set up and can start working on the wiki documents. 

Contributing to the wiki
------------------------

To contribute directly to the source files, find them in ``/source/``. 
If you are looking to create a new document, make sure the corresponding ``index.rst`` for it's directory includes it in it's `toctree` directive. This applies whether you choose to write in Markdown or reStructuredText (preferred). You might want to check out these resources.

Git/Github
~~~~~~~~~~
| Here is the **official Github tutorial** of how to setup git:
| https://help.github.com/en/github/getting-started-with-github/set-up-git
|
| See the **Github Flow** section, it's a pretty good overview if you've never used Git before.
| https://guides.github.com/introduction/git-handbook/#basic-git
| https://guides.github.com/activities/forking/
|
| If you use VSCode, I `highly recommend` using `GitLens <https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens>`_. Seriously. It helps. A lot. 

reST
~~~~
These are a few highly recommended resources we've found on getting started with reST/rST.

| https://docs.typo3.org/m/typo3/docs-how-to-document/master/en-us/WritingReST/CheatSheet.html
| https://stackoverflow.com/questions/2746692/restructuredtext-tool-support/2747041#2747041
| https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
| https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html
| 
| If you're using VSCode (seeing a trend?) definitely install the `reStructuredText <https://marketplace.visualstudio.com/items?itemName=lextudio.restructuredtext>`_ extension.

Translating the Wiki
---------------------

Setting up for translation
~~~~~~~~~~~~~~~~~~~~~~~~~~

To begin to translate the wiki into a language you first need to find out if a translation into that language is already in the process of being translated.
Each language is translated in its own language branch (A branch is like a separated version of the project that is used to create features without disturbing the integrity of the hole project). 

the name of a language branch is ``lang-xx`` where ``xx`` is the `Language code <https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes>`_ for your intended translation as listed under the 639-1 column.

Open the command terminal inside of your **bteguide** folder and run ``git checkout lang-xx`` if the language is already in the process of being translated the output will tell you that you are now on the ``lang-xx`` branch.

If your target language hasn't been started on yet, you can create the branch yourself by running:

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

Working on the translation
~~~~~~~~~~~~~~~~~~~~~~~~~~

Once that's done, you will find the .po files in ``/locale/xx/``.

**A workflow guide**

#. **Synchronizing the repository before starting to work:**

   The first thing to do before you start the day or (if you are translating into multiple languages) to switch languages is to synchronize your local copy of the repository to the remote master file. This will download all changes that have been made by your collegues.
   Open your command terminal in the **bteguide** folder and run:

   .. codeblock::

      git checkout lang-xx 
      git pull origin\lang-xx
      sphinx-intl update -p build/gettext -l xx

   Where ``xx`` is the language code of the language you want to work on.

   Now your .po files are up to date. 


#. **Working with Poedit**

    Insert Explaination Here (pending link to a detailed explaination)

   In order to build the repo with your language, you will need to modify the ``language = 'xx'`` option in your ``conf.py``. Make sure that you're in the right branch before doing this, as the ``conf.py`` is very important. After modifying it from ``'en'``, run ``make html`` or ``make livehtml`` as per usual, and your changes should build!

#. **Staging and Commiting changes**

   After you have worked on a .po file and made your translations you need to store your changes in a commit. Commits are progress packages that enable us to revert to any former version of the project if anything goes wrong.
   Save the changes in the file and then open your command terminal in the folder.

   .. codeblock::

      git add [filename]
      git commit -m [commit message]

   The commit message should be a max 50 character explaniation of what changes you made e.g. ``First translation of index.po`` or ``Spellcheck discord.po``. These messages help to track changes so it is encouraged to add and commit after every finished task (e.g. a translated file) and before going on to the next tasks as well as when you finish working at the end of the day. It is better to commit once to often than not enough. These commits are saved locally on your computer and are not visible for collaborators.


#. **Publishing/Pushing changes to the fork and the main wiki project**

   Finally, you need to make your commits available for collaborators. For this you need to push your commits onto a Github repository. Your commits will be pushed onto your personal project fork first:

   .. codeblock::

      git pull lang-xx
      git push lang-xx

   This will update your changes to the fork. If everything goes correctly you should see a message on your Github account showing your last commit message. You can push your progress at any time during the process to update the remote repositories (be aware that only the changes that you commited earlier will be uploaded).

   To get your changes updated on the main project you need to do a pull request on Github. Open your Github fork and click the green `Pull Request` button. You have to write a short message about what changes you have made and submit the pull request. Your pull request will be accepted by the main wiki editors.


Optional Quality-of-Life
------------------------

You can install ``sphinx-autobuild`` with the guide, though it only seems to be compatible with Python versions less than 3.8. We don't recommend installing an older version of Python just for that, but if you really want to, you can. If you find that the package `does work` with 3.8, please notify ``@EzraEn#4291`` as we'd like to see that as a default install. 

Installing sphinx-autobuild is as simple as ``pip install sphinx-autobuild``.
If you want to use live-reload, run ``make livehtml`` (or ``./make.bat livehtml``) and visit http://localhost:8000 to see your changes.