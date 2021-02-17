.. _osmdoc:

Open Street Maps (OSM)
======================
.. warning:: This document has been marked for deprecation. The information in the article may be outdated. 



What is OSM?
------------

Similar to BTE, OSM_ has the goal to map all of the world. While we are working on our Minecraft world, we can contribute to the OSM project and help them to achieve their goal. By editing the OSM database you not only make your own build easier but at the same time you can help identify infrastructure that might be crucial in future humanitarian work. This applies especially if you are working in a developing country where maps are hard to come by. OSM maps are also used by different mapping sevices such as Apple maps.


How to use OSM to add building outlines/roads
---------------------------------------------

You must create an account in OSM_ to be able to edit the maps. For this you only need an email address.
Click on **Edit** at the top of the screen and then **register**.
After the registration is done you will get into the Edit-mode. You will be presented with a short (15 min) tutorial that will teach you the basics of OSM_.
Please use the hashtag **#BTE** in your editing comments.

Misaligned satellite images
~~~~~~~~~~~~~~~~~~~~~~~~~~~

In remote areas of the world sometimes the satellite images are either not as good as you wish, or they do not align to the elements that have already been placed in OSM_. 
In the “edit” mode of OSM_ you will find a background settings icon on the right of the map. Here you can choose between different satellite and other map types. Sometimes features of buildings are more visible on one of the other images.
If there are already some structures mapped in your OSM_ region, but the underlying satellite image does not align correctly to these structures you have to move the satellite image. Go to the **background setting** to find **Adjust imagery offset** at the bottom. Use the arrows to move the satellite image to align to the pre-generated elements.

How to get changes into Minecraft
---------------------------------

It can take some time until the changes you made in OSM_ are registered in the database. After **30 - 60 min** you should be able to regenerate the part of the Minecraft world you edited to see the changes.
Select the area you edited in OSM_ using the WorldEdit ``//wand``. There is a bug that replaces roads with single stone brick lines therefore you should make sure not to select roads if possible. Then use the ``//regen`` command to regenerate the edited terrain.

How does it work behind the scenes?
-----------------------------------

.. _OSM: https://www.openstreetmap.org