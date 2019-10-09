from mycroft import MycroftSkill, intent_file_handler


class HumanHelp(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    def initialize(self):
        self.settings["phonenumber"] = self.settings.get('phonenumber', False)


    @intent_file_handler('help.human.intent')
    def handle_help_human(self, message):
        ambulance = self.ask_yesno('should_call_ambulance')
        if ambulance == "yes":
            self.speak_dialog('emergency_doctor')
        else:
            problem = ""
            self.speak_dialog('what_your_problem', expect_response=problem)
            ###### todoo some code
            self.speak_dialog('help.human')

    def heart_attack(self):
        self.log.info("Heart attack diagnosed")

    def unconsciousness(self):
        self.log.info("Stable side situation")

    def shock_situation(self):
        self.log.info("shock known")

    def poisoning(self):
        self.log.info("poisoning detected")


    @intent_file_handler('call_mum.intent')
    def handle_call_mum(self, message):
        self.speak_dialog('mum_is_coming')

def create_skill():
    return HumanHelp()

