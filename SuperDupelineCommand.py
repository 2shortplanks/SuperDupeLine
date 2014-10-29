import sublime, sublime_plugin
import os

class SuperDupelineCommand(sublime_plugin.TextCommand):
    def run(self, edit, allTabs=False):

        # remmeber the edit we're going to need it later
        self.daedit = edit;

        if allTabs:
            self.navigate(self.view.window().views(), showFileName=True)
        else:
            self.navigate([self.view])

    def navigate(self, views, showFileName=False):
        if len(self.view.sel()) == 1 and self.view.sel()[0].size() > 0:
            pattern = ".*%s.*" % self.view.substr(self.view.sel()[0])
        else:
            pattern = ".+"

        items = []
        view_and_regions = []

        for view in views:
            regions = view.find_all(pattern)
            if showFileName:
                if view.file_name():
                    name = os.path.basename(view.file_name())
                elif len(view.name()) > 0:
                    name = view.name()
                else:
                    name = 'untitled'
                items += [["%s: %s" % (name, view.substr(view.line(_)))] for _ in regions]
            else:
                items += [view.substr(view.line(_)) for _ in regions]
            view_and_regions += [[view, _] for _ in regions]

        def on_done(index):
            if index >= 0:
				self.view.insert(self.daedit, self.view.sel()[0].begin(), items[index].lstrip())

        if int(sublime.version()) > 3000:
            self.view.window().show_quick_panel(items, on_done, sublime.MONOSPACE_FONT, -1, on_done)
        else:
            self.view.window().show_quick_panel(items, on_done)
