import sublime, sublime_plugin

# Author: Iulius Curt, April 2012

# available commands
#   save_back_there
#   go_back_there


class BackThereMemory:
    """ Utility class to remember position """
    def __init__(self):
        self.location = 0
        self.valid = False

    def put(self, location):
        self.location = location
        self.valid = True

    def get(self):
        return self.location

    def isValid(self):
        return self.valid

bt_memory = BackThereMemory()

class SaveBackThereCommand(sublime_plugin.TextCommand):
    """ Puts the current location of the cursor in memory """
    def run(self, edit):
        sels = self.view.sel()
        bt_memory.put(sels[0].begin())


class GoBackThereCommand(sublime_plugin.TextCommand):
    """ Replaces the cursor to the position in memory """
    def run(self, edit):
        if bt_memory.isValid():
            self.view.sel().clear()
            self.view.sel().add( \
                    sublime.Region(bt_memory.get()))
