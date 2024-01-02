import json

from playwright.sync_api import Playwright, sync_playwright, expect
from loginModule import LoginModule
from chatModule import ChatModule
from sampleChatTest import SampleChatTest

login_module = LoginModule()
sample_chat_test = SampleChatTest()

with open("config.json", "r") as file:
        config = json.load(file)

username = config["username"]
password = config["password"]
oktaSignInCode = config["oktaSignInCode"]
accountName = config["accountName"]
buttonName = accountName + " " + username

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = context = browser.new_context()
    page = context.new_page() 
    page.goto("https://dev.ema.co/")
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("button", name="Auth Continue with Google").click()
    page.get_by_label("Email or phone").fill(username)
    page.get_by_role("button", name="Next").click()
    page.get_by_label("Username").fill(username)
    page.get_by_role("button", name="Next").click()
    page.get_by_label("Password").fill(password)
    page.get_by_role("button", name="Verify").click()
    page.get_by_role("link", name="Select").click()
    page.get_by_label("Enter code from Okta Verify").fill(oktaSignInCode)
    page.get_by_role("button", name="Verify").click()
    page.get_by_role("button", name="+ New Chat").click()
    storage = context.storage_state(path="state.json")

if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)