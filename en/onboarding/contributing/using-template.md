<!---
title: Using the Template
path: /onboarding/contributing/using-template
version: 1.0.0
authors:
    - @ezraen1
--->

Using the Template
===================

The [Template Page](/_sources/bteguide/en/onboarding/contributing/template-page.md.txt) contains the basis of a well-organised document. By following the directives set out within, we set the stage for a well-defined organisational structure for the entire **Guide**.

The Metadata
------------

```html
<!---
title: Long Title Here
path: /path/to/source
version: 1.0.0
last-updated: DD/MM/YYYY
authors:
    - @github-name-here <Alternate Name>
--->
```

The most important component of a standard page is the **Metadata**. It helps us keep track of changes to the documents we're working on, allows us to credit authors and helps translators keep track of what source data they're working with.

Above we see a sample template for the metadata that should be present in every source file (any document not _being_ translated).
The components present are as listed:

### Document Title `title:`
  The long-form title of your document. 
  
  This should be descriptive, yet concise. For most readers, this will be the only part of the document they see, so including specific context goes a long way in helping readers that are looking for your specific content.

### File Path `path:`
  The full path to your document, excluding the filetype. 
  
  The format of this value is more akin to a permalink, and serves as a accountable reference to your document, which allows you to both provide context (in the form of the folder your document resides within) and serves as a form of unique identification for your document (for documents with identical names).
  If your document is an "index" file (the main document linked to an enclosing directory), the path should be the directory itself. The path is essentially the shortest URL that RTFD would direct the reader to from the Table of Contents.

### Document Version `version:`
  The version of documentation the document is on. 
  
We follow the [SemVer](https://semver.org/) standard in denoting each document's version. For those who can't be bothered to read the documentation, here's a TL;DR. (but if you don't wanna read the docs, *should you really be writing them?*)

> Version Format: **MAJOR**.**MINOR**.**PATCH**

  - The first number (MAJOR) of your document's version should be 1. This is your document's first release, and if you're submitting a pull request, be proud! Your document is ready to be seen by the world! This should only be changed upon a major rewrite, or whenever significant content has changed in the interest of accuracy.
  - The second number (MINOR) comes into play whenever content is added that does not affect the basis of the document itself. Expanding upon relevant topics that are not already covered by a separate document falls into this category. Of course, whenever the coverage of a topic takes up enough of the page, it may be time to consider a MAJOR version bump and the transfer of content to a brand new document. 
  - The third number (PATCH) is used for small error corrections like typos and grammar mistakes. Rewording small portions of text for the sake of clarity can fall into this category, but when rewording more than 3 paragraphs worth of content, please bump MINOR instead.

  Each time a more major version is bumped (+1), the lower versions should be reset to 0 to reflect the hierarchy of changes. E.g., in the case of a MINOR bump to version `1.2.18`, version `1.3.0` will result.

### Last Updated `last-updated:`
  When the document was last updated for any reason.
  
  This should be updated every time the version is bumped, as it allows up to keep track of how well-maintained our knowledge-base is. This is really important, for translators especially!
  As we are catering to an international audience, the date format is formalised to be in [DMY little-endian order](https://en.wikipedia.org/wiki/Date_format_by_country) (`DD/MM/YYYY`). 
  
  Yes, that means we don't get Pi day, but this is a Minecraft project, not a math enthusiast software project. (though all software is math in the end isn't it?)

### Author List `authors:`
  This is a way for you (yes, you!) the author to be recognised for your work!
  
  Once you're done with your contribution to the document, add your GitHub handle (your username, with an @ prefixed) to the list. If we know you better by any other name, you can include it alongside your handle in \<angle brackets\>. E.g. `- @ezraen1 <EzraEn#4291>`.


Formatting
----------

We use basic Markdown for most of our documents, but since ReadTheDocs' support of Sphinx gives us so many extra features, we're not as restricted as the CommonMark standard may have you think.

### Headings
```markdown
Titles/Heading Ones are denoted by a ===== line underneath them that matches it's width.
Document Title
==============

Section Titles/Heading Twos and denoted by a matching ----- line instead.
Section Header
--------------

Heading Threes and below are denoted via # format.
### Heading 3

#### Heading 4

As with the above, all headings should also have a blank line underneath them before any content starts.
```


### Text Styling

Generally, following [GitHub-style Markdown](https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf) will do you well, except in the case of double-underscores (__) for italicization/emphasis. Please refrain from `__doing this__`, as Markdown compilers can be inconsistent in how they handle that case, you may not get what you expect.
```markdown
Using *single asterisks* for italicisation/emphasis and **double asterisks** for bolding will do you well for consistency's sake.
```


### Tables

Following [GitHub-style Markdown](https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf), this RTFD has Markdown tables enabled.

```markdown
First Header | Second Header
------------ | -------------
Content cell 1 | Content cell 2
Content column 1 | Content column 2
```
The code above will result in:

First Header | Second Header
------------ | -------------
Content cell 1 | Content cell 2
Content column 1 | Content column 2


### reStructuredText Support

For those of you *veteran documenters* that aren't afraid of Sphinx's preference for rST, ReCommonMark supports inline rST via some special syntax.

````markdown
```eval_rst
.. note:: Here's a Note Directive from rST living inside a Markdown document! 
```

````
The code above results in:

```eval_rst
.. note:: Here's a Note Directive from rST living inside a Markdown document! 
```