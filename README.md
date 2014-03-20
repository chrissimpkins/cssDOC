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

### 'Hover' Search vs. Selection Search

You have the option to either select the complete CSS element substring (including pseudoelement characters like ':', '::', and '@') or to locate the cursor within the element, at the beginning of the element, or at the end of the element ('hover' search) in order to launch documentation with cssDOC.  Then, use one of the following approaches to open the docs:

### Search with Right Click Menu

Use the `CSS Doc Search` menu item in the right click menu.

### Search with Keybinding

Use the following keybinding to perform the search:

##### CSS Documentation Search Keybinding

```
Ctrl-Alt-C
```

### Search with the Command Palette

Enter the keybinding to open the command palette (see description above in the Sublime Package Control section).  Type 'cssdoc' and then select `CSS Doc Search (cssDOC)`.

## Issues

Having a problem? Let's fix it.  Here are a few steps that will lead to the most rapid fix:

1. Make sure that you selected text in the editor before attempting to use cssDOC.  It's not that good (yet...).

2. Open the Sublime Text console with <code>Ctrl-`</code> or <code>View -> Show Console</code>, then run cssDOC again.  It generally provides helpful hints for problems and any exceptions that are raised will be displayed.

3. Submit the issue on [the GitHub repository](https://github.com/chrissimpkins/cssDOC/issues) with as much detail as you can provide.  Please paste the console ouptut for any exceptions that are raised.

## Changes

v.2.1.1 - added main menu item for access to documentation & keybinding settings

v2.1.0 - added 'hover' search - place cursor in/at beginning of/at end of CSS element and run cssDOC

v2.0.0 - changed the keybinding to `Ctrl-Alt-C` because, well, I suppose you may want to copy in a text editor, mea culpa...

v1.0.1 - added horizontal dividers to the context menu item

v1.0.0 - initial release

## License

[MIT License](https://github.com/chrissimpkins/cssDOC/blob/master/LICENSE)
