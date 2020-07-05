Installing the Modpack
=========================

This section will walk you through the process of installing the BTE modpack required for building and contributing to the project.

Using the Automated Installer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To begin you first need to download the correct installer for your operating system. These can be found in #downloads on the discord, or below.

* `Windows Installer <https://bte-installer.s3.amazonaws.com/public/installer/v1.11/BTEInstaller-1.11-windows.zip>`_
* `Mac Installer <https://bte-installer.s3.amazonaws.com/public/installer/v1.11/BTEInstaller-1.11-mac.dmg>`_
* `Linux Installer <https://bte-installer.s3.amazonaws.com/public/installer/v1.11/BTEInstaller-1.11-linux.tar.gz>`_

Next, simply run the file by double clicking it.

Common problems that can occur:

* Windows: Press "More Info", then "Run Anyways" if Windows blocks the installer

* Mac: The installer unfortunately only runs on MacOS 10.15.x, you will need to do a manual install, listed below


Performing a Manual Installation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In a manual installation, you will download the files and add them to your mods manually.
Please note that this method will have a harder time updating, should any updates come.
A manual install may also have issues with worlds, and the automated installer is always recommended over a manual install, if possible.

#. Install forge from `this link <https://files.minecraftforge.net/maven/net/minecraftforge/forge/index_1.12.2.html>`_. 
#. Download the modpack file from `here <https://bte-installer.s3.amazonaws.com/public/modpack_versions/BuildTheEarthPack_1.6.zip>`_
#. Extract the file a folder of your choice.
#. Go into the extracted folder, then the overrides folder.
#. Move all the mods from the :code:`mods` folder to your mods folder of :code:`.minecraft`
#. Move the :code:`Build The Earth (new projection)` folder from the :code:`saves` folder to your own :code:`saves` folder
#. Run the forge profile in the minecraft launcher, then make a new world with `these settings <https://cdn.discordapp.com/attachments/691034211464773684/711678233179062283/settings.png>`_