Installing and Running a Server
=================================

Default Server
~~~~~~~~~~~~~~

Advanced Server Pack
~~~~~~~~~~~~~~~~~~~~~

This section will walk you through the process of setting up your own BTE server with permissions and plugins.

This section is for the Build Team Preconfigured server pack, use this if you plan on hosting a large Build Team or want permissions and plugins pre-installed. 
If your hosting for just you and a couple friends and don't want extra plugins, than use the Default server pack above.

Setting up the server
++++++++++++++++++++++++

#. Download the server pack from `this link <https://drive.google.com/file/d/1SGt735Q5N99HA8jd_S2bBgYp6ZsDbcRn/view?usp=sharing>`_ (press the download button in the top right)
#. Unzip the file to a location of your choice, then navigate to the folder.
#. Edit the :code:`RUN.bat` file. 
    Change :code:`xmx4096M` to how much RAM you want the server to use, 4096M is 4096 MB, or 4GB. For example, to use 6GB you would do 6*1024 to get 6144M, and type :code:`xmx6144M`.
#. Save the :code:`RUN.bat` file and start the server by double clicking the bat file. It may take some time for it to install the required files, so be patient.
#. When a prompt comes up asking if you would like to accept the EULA, type :code:`true` and press enter.

To stop the server, type :code:`stop` in the console window, or use the :code:`/stop` command in minecraft

Using Your Own World
""""""""""""""""""""""
#. Delete the :code:`TerraPreGenerated` world folder.
#. Move your world folder into the server folder.
#. Rename the world folder :code:`TerraPreGenerated` in order to keep the current settings and protection



Joining Your Server
++++++++++++++++++++

From the Host Computer
""""""""""""""""""""""
You should only run a server on the same computer that you play on if you have 12GB+ of RAM, since you will need it to run both modded Minecraft and the server at the same time.

Connect to the server using the IP :code:`localhost`

From an Another Computer
""""""""""""""""""""""""""
To allow another computer(eg. your friends) to connect to your server, you need to port forward to the server port.

#. Follow the instructions `here <https://www.noip.com/support/knowledgebase/general-port-forwarding-guide/>`_ to forward your port. The default server port is 25565.
#. Check if port forwarding worked using `<https://www.portchecktool.com>`_. Make sure to write down the IP and port, as other people will need it to connect to your server.



Using the Server
+++++++++++++++++

Obtaining OP
""""""""""""
To give yourself op, simply type :code:`op <username>` into the console.
You now have all the permissions.

Managing Permissions
""""""""""""""""""""
Permissions are managed by a permissions plugin called LuckPerms.

+--------------------+--------------------------------------------------------------+
| Permission Group   | Command                                                      |
+====================+==============================================================+
| Builder            | Adding the group:                                            |
|                    | :code:`/lp user <username> group add builder`                |
|                    +--------------------------------------------------------------+
|                    | Removing the group:                                          |
|                    | :code:`/lp user <username> group remove builder`             |
+--------------------+--------------------------------------------------------------+
| Helper             | Adding the group:                                            |
|                    | :code:`/lp user <username> group add helper`                 |
|                    +--------------------------------------------------------------+
|                    | Removing the group:                                          |
|                    | :code:`/lp user <username> group remove helper`              |
+--------------------+--------------------------------------------------------------+
| Moderator          | Adding the group:                                            |
|                    | :code:`/lp user <username> group add moderator`              |
|                    +--------------------------------------------------------------+
|                    | Removing the group:                                          |
|                    | :code:`/lp user <username> group remove moderator`           |
+--------------------+--------------------------------------------------------------+
| Administrator      | Adding the group:                                            |
|                    | :code:`/lp user <username> group add administrator`          |
|                    +--------------------------------------------------------------+
|                    | Removing the group:                                          |
|                    | :code:`/lp user <username> group remove administrator`       |
+--------------------+--------------------------------------------------------------+

Teleporting
""""""""""""
Unfortunately the :code:`/tpll` command will not work if you are not opped.

In order to get around this, the server pack replaces this with :code:`/cs tpll`.
To use it, run :code:`/cs tpll <latitude> <longitude>`

:code:`/cs tpll` also works with degree coordinates.

World Backups
"""""""""""""
To setup automatic world backups, move the mods from the :code:`extra-mods` folder to the :code:`mods` folder.

Reboot the server, then the server will start generating backups every 15 minutes.
Change the delay in the aromabackups config in the :code:`config` folder.