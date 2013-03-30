import sublime, sublime_plugin

class SwapperCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for pos in self.view.sel():
            if pos.begin()-2 >= 0 :
                region = sublime.Region(pos.begin()-2, pos.begin())
                str = self.view.substr(region)[::-1]
                self.view.erase(edit, region)
                self.view.insert(edit, pos.begin()-2, str)