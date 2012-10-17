import sublime, sublime_plugin

# Author: Iulius Curt, April 2012

# Available commands
#   * save_back_there
#       Saves current position, overwriting eventual previously saved one
#   * go_back_there
#       Jumps to the latest saved position


# TODO: This class is mostly futile and should be replaced
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
# Keep track of the latest saved position: (position, view)
bt_latest = None


class SaveBackThereCommand(sublime_plugin.TextCommand):
    """ Puts the current location of the cursor in memory """
    def run(self, edit):
        global bt_memory
        global bt_latest

        buff_id = self.view.buffer_id()
        sels = self.view.sel()

        if not buff_id in bt_memory:
            # First time in current buffer
            bt_memory[buff_id] = BackThereMemory()
        bt_memory[buff_id].put(sels[0].begin())
        bt_latest = (sels[0].begin(), self.view)


class GoBackThereCommand(sublime_plugin.TextCommand):
    """ Moves the cursor to the position in memory """
    def run(self, edit):
        global bt_memory
        global bt_latest

        buff_id = self.view.buffer_id()
        switch_needed = False
        if buff_id in bt_memory and bt_memory[buff_id].valid:
            saved_region = sublime.Region(bt_memory[buff_id].get())
            current_view = self.view
            # Update the latest
            bt_latest = (bt_memory[buff_id].get(), current_view)
        elif bt_latest:
            # This is the case where no position is saved in the current view,
            # but there exists at least one position saved in some other view,
            # so, that one will be used
            saved_region = sublime.Region(bt_latest[0])
            current_view = bt_latest[1]
            switch_needed = True
        else:
            return

        # Check if the saved position is still inside the buffer limits
        buff_end = current_view.size()
        if saved_region.begin() > buff_end:
            saved_region = sublime.Region(buff_end, buff_end)

        # Move the cursor _back there_
        current_view.sel().clear()
        current_view.sel().add(saved_region)

        # Center the new cursor position in the viewport
        # (only if cursor is out of viewport)
        current_view.show(saved_region)

        # If it's the case, it will call switch_back_window to jump to the
        # wanted view
        if switch_needed:
            self.view.window().run_command('switch_back_window')


class SwitchBackWindowCommand(sublime_plugin.WindowCommand):
    """ Switches the view to where the last position was saved """
    def run(self):
        self.window.focus_view(bt_latest[1])
