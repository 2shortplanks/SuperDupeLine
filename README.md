SuperDupeLine
=============

Sublime Text plugin to insert at the cursor the contents
of any other line in the current file (or in any open
file.)  Selection of the line to insert is triggered by
a key combination and then done via Sublime's fuzzy text
matching dialog.

![screencast](http://i.imgur.com/3mzU7BH.gif)

## Keymap

```javascript
[
    {
        "keys": ["super+k", "super+d"],
        "command": "super_dupeline"
    },
    {
        "keys": ["super+k", "super+f"],
        "command": "super_dupeline",
        "args": { "allTabs": true }
    }
]
```

## Author

Adapted from [Sublime Super Navigator](https://github.com/jugyo/SublimeSuperNavigator) by Mark Fowler mark@twoshortplanks.com