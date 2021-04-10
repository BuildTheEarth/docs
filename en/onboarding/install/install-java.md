---
title: Java Edition Installation
path: /onboarding/install/install-java
version: 1.0.0
authors:
    - "@cAtte_"
---

# Java Edition Installation

There's a few ways you can install our modpack on Java Edition. We've created a custom installer for you, which is the easiest way to go about it, but you might want to install it manually for whatever reason. We will see how to do both of those!

## Modpack installer

_You can also check out [this short tutorial](https://youtube.com/watch?v=6cx7rutu9Hk) to learn how to use the modpack installer on Windows._

1.  First off, download the latest version of the installer for your specific operating system:

    -   [Windows installer](https://bte-installer.s3.amazonaws.com/public/installer/v1.19.2/BTEInstaller-1.19.2-windows.zip) (`.exe`)
    -   [macOS installer](https://bte-installer.s3.amazonaws.com/public/installer/v1.19.2/BTEInstaller-1.19.2-mac.dmg) (`.dmg`), requires macOS Catalina
    -   [Linux installer](https://bte-installer.s3.amazonaws.com/public/installer/v1.19.2/BTEInstaller-1.19.2-linux.AppImage) (`.AppImage`)
    -   [Universal installer](https://bte-installer.s3.amazonaws.com/public/installer/v1.19.2/BTEInstaller-1.19.2-universal.jar) (`.jar`)

The universal installer can be launched on any operating system, and you may want to use it if the version specific to your OS isn't working. It's a Java Archive file and requires Java 8; if you don't know how to launch it, you can learn [here](https://lifewire.com/jar-file-4138386).

For the Windows version, you will have to extract the `zip` file (right-click, extract) and run the executable file (double-click) that's inside. If you get a warning from Windows, simply ignore it and run anyway; [it says that for all unrecognized apps](https://pcworld.com/article/3197443/how-to-get-past-windows-defender-smartscreen-in-windows-10.html).

2.  Before using the installer, make sure both Minecraft and its launcher aren't running.
3.  Once you've opened the installer, you can choose to toggle optional mods, like Terramap or ReplayMod, but the default mods are okay.
4.  Press the **Install** button (or **Update** if the modpack is already installed). It should take a few seconds and tell you once it's done.
5.  Launch Minecraft again, and you should see a **Build the Earth v2.0.0** profile. Select it, and press Play.
6.  If you get a warning about a modified installation, just ignore it. The launcher [does that for every mod](https://gaming.stackexchange.com/q/378315). You're done!

## Manual installation

The modpack installer is recommended over a manual installation, as a manual installation will be a bit harder to update in the future. However, you might be entirely unable to use the launcher, or you might want to install the modpack manually for other reasons, so we'll show you how to do it here. For a manual installation, you can either use [MultiMC](https://multimc.org) or install the mods manually using [Forge](https://minecraftforge.net).

### Using MultiMC

If you don't have it already, [install MultiMC](https://multimc.org/#Download) from their official website. The installation instructions should be pretty similar to any other app. Once you've installed it, follow these instructions to set up the modpack:

1.  If you've just installed MultiMC, set your account by clicking on **Accounts** in the top right corner. Click on the **Add** button and log in using your Mojang username and password.
2.  Create a new profile by pressing **Add Instance** in the top left corner.
3.  Go to the **Import from zip** tab and paste the following into the text box:
    -   `https://cdn.discordapp.com/attachments/705931174362611753/823296677024628786/BuildTheEarth_Pack_2.0.zip`
4.  Once that's done, click on **Edit Instance** and go to the **Settings** tab.
5.  Tick the **Memory** box and use the arrows to change the maximum amount of RAM allocated. We recommend somewhere between 4 GB and 8 GB; make sure your system can afford it.
6.  Launch the modpack by double-clicking its icon. You're done!

### Using Forge

If you've never installed mods before, using Forge may be a little more difficult, but there's a first time for everything! Please install Minecraft version 1.12.2 and [Forge for 1.12.2](https://files.minecraftforge.net/maven/net/minecraftforge/forge/index_1.12.2.html) if you don't have it already. Then, follow the instructions:

1.  Download the modpack zip from [here](https://bte-installer.s3.amazonaws.com/public/modpack_versions/BuildTheEarthPack_2.0.zip).
2.  Extract it with your favorite app, like Windows' built-in zip browser or macOS' [The Unarchiver](https://apps.apple.com/es/app/the-unarchiver/id425424353).
3.  Browse to the `overrides` then `mods` folder.
4.  Copy all of the mods there to the appropriate mods folder:
    -   On Windows: `%APPDATA%\.minecraft\mods`
    -   On macOS: `~/Library/Application Support/minecraft/mods`
    -   On Linux: `~/.minecraft/mods`
5.  Then, go back to `overrides` and into the `saves` folder.
6.  Copy the `Build The Earth (new projection)` folder into the appropriate saves folder:
    -   On Windows: `%APPDATA%\.minecraft\saves`
    -   On macOS: `~/Library/Application Support/minecraft/saves`
    -   On Linux: `~/.minecraft/saves`
7.  Open Minecraft, and select the **Forge 1.12.2** profile, then click Play. You're done!
