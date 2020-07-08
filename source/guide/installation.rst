Installing the Modpack
=========================

This section will walk you through the process of installing the BTE modpack required for building and contributing to the project.

This page is split into 3 parts, using the automated installer, performing a manual installation, and installing Optifine.
Use the contents on the right to easily navigate through the page.

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
There are two ways to perform a manual install:

1. MultiMC
2. Forge

We recommend MultiMC for use with the Modpack, as the install won't affect your existing Minecraft installation.

MultiMC
+++++++
First, lets make sure you have MultiMC installed. `Download MultiMC <https://multimc.org/#Download>`_

Install and launch MultiMC, then follow the instructions below.

#. First, set your account by clicking on the Accounts on top right and pressing "Manage Accounts"
#. Click the :code:`Add` button, and log in using your Mojang username and password.
#. Create a new MultiMC profile by pressing :code:`Add Instance` in the top left.
#. Switch to the :code:`Import from zip` tab, then paste :code:`https://bte-installer.s3.amazonaws.com/public/modpack_versions/BuildTheEarthPack_1.6.zip` into the text box.
#. Once the importing has finished, click the :code:`Edit Instance` button, and then the :code:`Settings` tab.
#. Check the :code:`Memory` box, and use the arrow buttons to change the maximum memory allocated. The recommended amount of memory is about 4-8 GB.
#. Launch the modpack by double clicking the icon.

Forge
+++++

#. Install forge from `this link <https://files.minecraftforge.net/maven/net/minecraftforge/forge/index_1.12.2.html>`_. 
#. Download the modpack file `here <https://bte-installer.s3.amazonaws.com/public/modpack_versions/BuildTheEarthPack_1.6.zip>`_
#. Extract the file a folder of your choice.
#. Go into the extracted folder, then the overrides folder.
#. Move all the mods from the :code:`mods` folder to your mods folder of :code:`.minecraft`
#. Move the :code:`Build The Earth (new projection)` folder from the :code:`saves` folder to your own :code:`saves` folder
#. Run the forge 1.12.2 profile in the minecraft launcher, then make a new world with `these settings <https://cdn.discordapp.com/attachments/691034211464773684/711678233179062283/settings.png>`_


Installing Optifine
~~~~~~~~~~~~~~~~~~~~~~~~
This section is split into parts based on how you installed the modpack. Use the sidebar to navigate to each one.

Before starting, download the most recent version of Optifine 1.12.2 from `here <https://optifine.net/downloads>`_

Automated Installer
+++++++++++++++++++
Use the section corresponding to your operating system to install optifine.

Windows
""""""

#. Open up your :code:`.buildtheearth` folder. Press :code:`Win + R`, paste :code:`%AppData%/.buildtheearth` , and press enter.
#. Go into the :code:`mods` folder.
#. Move or copy the Optifine jar from the download location to the folder.

Mac
""""

#. Open up your :code:`.buildtheearth` folder. Open Spotlight with :code:`⌘ + Space`, paste :code:`~/Library/Application Support/buildtheearth` , and press enter.
#. Go into the :code:`mods` folder.
#. Move or copy the Optifine jar from the download location to the folder.


Linux
""""""

#. Open up your :code:`.buildtheearth` folder. Navigate to your main directory and go into :code:`.buildtheearth`
#. Go into the :code:`mods` folder.
#. Move or copy the Optifine jar from the download location to the folder.

MultiMC
+++++++

#. Open MultiMC, click the :code:`Build the Earth` profile, and press :code:`Edit Instance`
#. Click the :code:`Loader Mods` tab, and then :code:`Add` on the top right.
#. Naviage to where you downloaded Optifine, and double click it.
#. You're done!

Forge
+++++
Windows
""""""

#. Open up your :code:`.minecraft` folder. Press :code:`Win + R`, paste :code:`%AppData%/.minecraft` , and press enter.
#. Go into the :code:`mods` folder.
#. Move or copy the Optifine jar from the download location to the folder.

Mac
""""

#. Open up your :code:`.minecraft` folder. Open Spotlight with :code:`⌘ + Space`, paste :code:`~/Library/Application Support/minecraft` , and press enter.
#. Go into the :code:`mods` folder.
#. Move or copy the Optifine jar from the download location to the folder.


Linux
""""""

#. Open up your :code:`.minecraft` folder. Navigate to your main directory and go into :code:`.minecraft`
#. Go into the :code:`mods` folder.
#. Move or copy the Optifine jar from the download location to the folder.