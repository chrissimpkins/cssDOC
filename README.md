cssDOC
======

A Sublime Text 2/3 plugin that supports CSS documentation search from selections in the editor

## About

cssDOC allows you to view the [Mozilla Developer Network CSS documentation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference) for the selection in your editor.  If your selection matches a CSS entity, the documentation page is opened in your default browser.  If cssDOC is not able to identify the selection as a CSS entity, the default browser is opened and the Mozilla Developer Network documentation is searched (using a CSS filter).

## Install cssDOC

### Using Sublime Package Control

cssDOC can be installed using [Sublime Package Control](https://sublime.wbond.net/).  Open the command palette with:

##### Mac OSX
```
Cmd + Shift + P
```

##### Linux & Windows
```
Ctrl + Shift + P
```

Type `install` and select the menu item, `Package Control: Install Package`.

Type `cssDOC` and select the cssDOC package that is displayed.  This will install the package in your editor.

### Using Git

Use the Sublime Text menu items `Preferences -> Browse Packages` to locate your Packages directory.

Navigate to the directory in your terminal and clone the cssDOC source repository inside the Packages directory using the command:

``` bash
git clone https://github.com/chrissimpkins/cssDOC.git "cssDOC"
```

### Manual Install

Download the [zip compressed archive from GitHub](https://github.com/chrissimpkins/cssDOC/archive/master.zip).

Decompress the zip archive and rename the directory `cssDOC`.

Open your Sublime Text Packages directory using the `Preferences -> Browse Packages` menu items.

Move the entire `cssDOC` directory into your Sublime Text Packages directory.

## Use cssDOC

### Search with Right Click Menu

Select a CSS entity in your editor text, then use the `CSS Doc Search` menu item in the right click menu.

### Search with Keybinding

Select a CSS entity in your editor text, then use the following keybinding to perform the search:

##### CSS Documentation Search Keybinding

```
Ctrl-c
```

### Search with the Command Palette

Select a CSS entity in your editor text then enter the keybinding to open the command palette (see description above in the Sublime Package Control section).  Type 'cssdoc' and then select `CSS Doc Search (cssDOC)`.

## Issues

Having a problem? Let's fix it.  Here are a few steps that will lead to the most rapid fix:

1. Make sure that you selected text in the editor before attempting to use cssDOC.  It's not that good (yet...).

2. Open the Sublime Text console with <code>Ctrl-`</code> or <code>View -> Show Console</code>, then run cssDOC again.  It generally provides helpful hints for problems and any exceptions that are raised will be displayed.

3. Submit the issue on [the GitHub repository](https://github.com/chrissimpkins/cssDOC/issues) with as much detail as you can provide.  Please paste the console ouptut for any exceptions that are raised.

## License

[MIT License](https://github.com/chrissimpkins/cssDOC/blob/master/LICENSE)
