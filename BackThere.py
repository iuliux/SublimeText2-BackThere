import sublime, sublime_plugin

# Author: Iulius Curt, April 2012

# Available commands
#   * save_back_there
#       Saves current position, overwriting eventual previously saved one
#   * go_back_there
#       Jumps to the latest saved position


class BackThereMemory:
    """ Utility class to remember position """
    def __init__(self):
        self._location_ = 0
        self.valid = False

    def put(self, location):
        self._location_ = location
        self.valid = True

    def get(self):
        return self._location_


# One memory bank for each buffer
bt_memory = {}


class SaveBackThereCommand(sublime_plugin.TextCommand):
    """ Puts the current location of the cursor in memory """
    def run(self, edit):
        buff_id = self.view.buffer_id()
        sels = self.view.sel()

        if not buff_id in bt_memory:
            # First time in current buffer
            bt_memory[buff_id] = BackThereMemory()
        bt_memory[buff_id].put(sels[0].begin())


class GoBackThereCommand(sublime_plugin.TextCommand):
    """ Moves the cursor to the position in memory """
    def run(self, edit):
        buff_id = self.view.buffer_id()
        if buff_id in bt_memory and bt_memory[buff_id].valid:
            saved_region = sublime.Region(bt_memory[buff_id].get())

            # Check if the saved position is still inside the buffer limits
            buff_end = self.view.size()
            if saved_region.begin() > buff_end:
                saved_region = sublime.Region(buff_end, buff_end)

            # Move the cursor _back there_
            self.view.sel().clear()
            self.view.sel().add(saved_region)

            # Center the new cursor position in the viewport
            # (only if cursor is out of viewport)
            self.view.show(saved_region)
