from mycroft import MycroftSkill, intent_file_handler


class HumanHelp(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('help.human.intent')
    def handle_help_human(self, message):
        self.speak_dialog('help.human')


def create_skill():
    return HumanHelp()

