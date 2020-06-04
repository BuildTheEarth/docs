Getting Started
===============

.. warning:: This document has been marked for deprecation. The information in the article may be outdated. 

Don’t feel confident enough to build?
-------------------------------------

Don't worry we all started small. You might think that all of us are master builders because you saw all those fancy buildings being showcased but in truth we all started with a dirt house and a door at some point.

The world is a big place and not every building is complicated to build.

Here are some tips for the beginner:

* Start with something small
* Start with something familiar
* Ask for advice whenever you are stuck

Choose one or two small houses in your local area that you know very well and start building

Go to the `Discord <https://discord.gg/buildtheearth>`_ #progress channel and ask for building tips (e.g. Which blocks to use for different materials).

If you want to improve your building technique check out some YouTube videos on "WorldEdit" and "Effortless Building". Both of these mods are included in the modpack and can save a lot of time.

Good luck and have fun!


The Solo-Builder Application
----------------------------
To become a builder you need to download the modpack . You can find the installer in `Discord <https://discord.gg/buildtheearth>`_ #downloads.

The first decision you have to make is where you want to build. Check out the `Map <https://buildtheearth.net/map>`_  to see which plots of land are still available. You can choose any of the unclaimed plots. Each plot is 512 x 512 meter (= Minecraft blocks) in size.

Before you can claim the plot you have to do some building to show that you are ready for the challenge.

Choose 2-5 buildings to build (these buildings should not be on the border with other plots) and start building.

When the buildings look like the real world buildings take a screenshot (The perspective of the screen shot should be the same as a real life reference image).

Upload your screenshot and the reference image separately to `imgur <https://imgur.com/>`_.

Head over to the `webpage <https://buildtheearth.net/>`_ and apply for the builder position.

Your application should be answered within approx. 3 days.

You can go on building until you get an answer.

You will get a direct message on Discord approving your application.

If your application is denied you will get some feedback on what to improve.


Bedrock version?
----------------
Unfortunately you can not become a builder when using the Bedrock version however you are welcome to join the Discord and help improve other people builds by giving feedback and suggestions in the #progress channel.
Another way you can help the project to help to map out the world on `Open Street Maps <file:///C:/Users/Ezra%20En/Desktop/BTE/Building%20Guidebook/BuildingGuidebook.html#kix.thj8vh7kmyzv>`_.


Settings for generating a new world
-----------------------------------
When you download the modpack a pre-generated world will be included. Sometimes you will have to generate a new world to deal with some bugs though.

.. table:: These are the current settings for generating a new world
   :widths: auto

   ====================  ==
   Custom
   ====================  ==
   Generate Structures:  ON
   CubicChunks:          Default
   Allow Cheats:         ON
   World Type:           Planet Earth
   Bonus Chest:          OFF
   ====================  ==

.. table:: 
   :widths: auto

   ====================== ==
   More World Options:
   ====================== ==
   Projection:            terra121.projection.bteairocean
   Orientation:           Upright
   Smooth Blending:       ON
   Spawn Roads:           ON
   Advanced Water:        ON
   Elevation Based Ores:  ON
   OSM Building Outlines: ON
   ====================== ==

Entering the world for the first time
-------------------------------------
If everything went correctly you should spawn on a mushroom island in the middle of the ocean. Welcome to “Null - Island”.

.. _tpll:

How to teleport
~~~~~~~~~~~~~~~
`Video tutorial <https://thumbs.gfycat.com/AdolescentWindingCentipede-mobile.mp4>`_

You can teleport to any location in the world using the command ``/tpll x y``, for example ``/tpll 40.708838, -73.999225`` to go to New York


To get the coordinates of any place in the world you can:

1. Copy them from the `Interactive Map <https://buildtheearth.net/map>`_
2. Go to Google maps, right-click onto your point of interest and click “What is here?” click on the coordinates showing up at the bottom of the screen. Now you can copy the coordinates in the toolbar on the left.

There is also a custom mod that has been made for this project only made by Smyler#7078, called `Terramap <https://www.curseforge.com/minecraft/mc-mods/terramap>`_. This mod allows you to easily teleport without having to copy-paste the gps coordinates from a web browser, or open various map websites at the desired location directly from the game.

After it is installed in your modpack, you can open the map with M, and then zoom in on the location you want to go to.


Before you build/Best Practices
-------------------------------
Everybody has their own way to go about starting a build, however there are some preparations that will help in the long run, especially in less densely populated areas.

1. Make sure that your plot is not already claimed.
2. :ref:`/tpll <tpll>` to your coordinates and have a look around the plot to see the layout, orientation and identify missing features. (to find the corners of your plot go to “MyBuildTheEarth” on the webpage and click on your region. You will find the x and y coordinates of the corners there.)
3. | Go to `OpenStreetMaps <https://www.openstreetmap.org/>`_ (OSM) and check if your area has been mapped completely and accurately. `More info on OSM <osmdoc>`_
   | :under:`If the mapping is not correct:`

   a. Create an account and edit the map on OSM
   b. Give the changes 30-60 min to update
   c. Select your plot using the WorldEdit ``//wand`` and use ``//regen`` to update

4. Fix your biomes if needed:

   a. Select your plot using the WorldEdit ``//wand``
   b. ``//setbiome [biometype]``, check ``//biomelist`` for all possible biomes
5. Check the elevation of your plot and fix it with WorldEdit.
6. Fix any bugged terrain generation using WorldEdit
7. Do a couple commands to change some gamerules. These commands are really sensitive to capital letters, so copying them into your game is the safest way to go. Even if you type without capitals, it will show a message that you have done it, even if nothing has changed.

   a. | ``/gamerule doDaylightCycle false`` (stops day night cycle)
      | You can then do ``/time set day`` or ``/time set night`` to change the time.
   b. | ``/gamerule doMobSpawning false`` (stops mobs from spawning)
      | Doing ``/butcher -abfgnprt`` will butcher every mob in the area, including NPC and pets. You can also do ``/kill @e[type=!Player]``
   c. ``/gamerule mobGriefing false`` (stops creepers/endermen from destroying your build)
   d. | ``/gamerule doWeatherCycle false`` (Stops rain and snowfall)
      | You can also do ``/weather clear`` to put the weather to sun. There is also ``rain`` and ``thunderstorm``.
8. We recommend to set the chunk loading distance as low as possible (otherwise the world file size will increase.)
9. You’re ready to start building!

Important Links
---------------
https://buildtheearth.net/

https://buildtheearth.net/map 