BackThere (Sublime Text 2 plugin)
======


## It does...

Saves one position for you to return to it as many times you need.

It is composed of two commands:

1.  `save_back_there` - Saves the current position of the text cursor in the current window

2.  `go_back_there` - Places the cursor _back_ _there_, where it was last saved


## Default key bingings

1.  Save command: 

    `Ctrl` + `Shift` + `q`

2.  Go command:

    `Ctrl` + `q`

For OSX, replace `Ctrl` with `Command`

To use your custom (and probably better) key bindings, you should either add them in `Preferences -> Key bindings - User` like in the example below, either edit the `Default (<operating-system>).sublime-keymap` file in the plugin's folder.

    { "keys": ["shift+ctrl+q"], "command": "save_back_there" },
    { "keys": ["ctrl+q"], "command": "go_back_there" }

## Installing (with PackageControl)
TODO

## Installing (without PackageControl)

If you don't have `git` installed, you can just download as Zip, and unpack it.

### OSX

    $ cd ~/Library/Application\ Support/Sublime\ Text\ 2/Packages/
    $ git clone git://github.com/iuliux/SublimeText2-BackThere.git BackThere

### Linux (Ubuntu like distros)

    $ cd ~/.config/sublime-text-2/Packages/
    $ git clone git://github.com/iuliux/SublimeText2-BackThere.git BackThere

### Windows 7:

Copy the directory to: `C:\Users\<username>\AppData\Roaming\Sublime Text 2\Packages`  
or using GitHub for Windows

### Windows XP:

Copy the directory to: `C:\Documents and Settings\<username>\Application Data\Sublime Text 2\Packages`  
or using GitHub for Windows


## License
MIT License, see http://opensource.org/licenses/MIT