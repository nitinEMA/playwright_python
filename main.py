from playwright.sync_api import Playwright, sync_playwright, expect
from loginModule import LoginModule
from chatModule import ChatModule
from sampleChatTest import SampleChatTest

login_module = LoginModule()
chat_module = ChatModule()
sample_chat_test = SampleChatTest()

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    login_module.login(context)

    # Run Sample Chat Test
    response = sample_chat_test.test(context=context)
    sample_chat_test.save_response(response=response)

    # Run as many tests as you wish





    ##############################

if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)