from loginModule import LoginModule

class XlsxRetrievalTest:
    def driveTest(self, context, file_name, text):
        login_module = LoginModule()
        page = login_module.startNewChat(context)
        
