from .base import Module

class Groups(Module):
    DESCRIPTION = "Get links to other admit groups!"
    links = {
        "University of Michigan": "46781389/hZehS1",
    }
    def response(self, query):
        return '\n'.join(["%s -> https://groupme.com/join_group/%s" % (name, self.links[name]) for name in self.links])
