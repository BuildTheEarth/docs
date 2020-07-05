Common Errors
=================

This section explains some common errors you can experience when installing or running the mod.

Installer Errors
~~~~~~~~~~~~~~~~
Before checking these errors, check that all minecraft windows and launchers are closed before attempting an installation.
Also make sure no other applications are using the java program.

An error occurred while running installer. Error code: (some non-zero number)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Unknown cause, you will have to attempt a manual install.

Unable to replace invaild library
+++++++++++++++++++++++++++++++++
Remember to close Minecraft and any other programs that could be using java.



Minecraft Errors
~~~~~~~~~~~~~~~~
Instant Crash
+++++++++++++
Make sure you dedicate enough ram to the modpack by changing the JVM arguments

Possible Fix:

1.a (Windows) Press the keys "Windows+R."

1.b. (MacOS) Open Finder.

1.c. (Linux) Open a terminal window by pressing "Control+Alt+T."

2.a. (Windows) Paste in this text 

.. code-block:: 

    %AppData%\.buildtheearth\options.txt

2.b. (MacOS) Paste in this text

.. code-block::

    ~/Library/Application/Support/.buildtheearth/options.txt

2.c. (Linux) Paste in this text, and then go to Step 6

.. code-block::

    sed 's/fullscreen:true/fullscreen:false/' ~/.buildtheearth/options.txt

3. Press "Ctrl+F."

4. Search for "fullscreen"

5. Replace "true" with "false"

6. Restart Minecraft
