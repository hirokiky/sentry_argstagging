from sentry.interfaces import Message
from sentry.plugins import register
from sentry.plugins.bases.tag import TagPlugin


class ArgsPlugin(TagPlugin):
    slug = 'args'
    title = 'Auto Tag: Args'
    author = "Hiroki KIYOHARA"
    tag = 'args'
    tag_label = 'Args'
    project_default_enabled = True

    def get_tag_values(self, event):
        tags_list = []

        d = event.interfaces
        for interface in d.values():
            if isinstance(interface, Message):
                tags_list.extend(interface.params)

        return tags_list

register(ArgsPlugin)