from loginModule import LoginModule
from chatModule import ChatModule

outputFilePath = "responseSampleChatTest.txt"

class SampleChatTest:
    def test(self, context):
        login_module = LoginModule()
        chat_module = ChatModule()
        page = login_module.startNewChat(context)
        inner_text = chat_module.askInChat(page, "Hey, Ema!")
        return inner_text

    def save_response(self, response):
        with open(outputFilePath, "w", encoding="utf-8") as file:
            file.write(response)