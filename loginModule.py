import json

with open("config.json", "r") as file:
        config = json.load(file)

username = config["username"]
password = config["password"]
oktaSignInCode = config["oktaSignInCode"]
accountName = config["accountName"]
buttonName = accountName + " " + username

class LoginModule:
    def login(self, context):
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
    
    def startNewChat(self, context):
        page = context.new_page() 
        page.goto("https://dev.ema.co/")
        page.get_by_role("button", name="Continue").click()
        page.get_by_role("button", name="Auth Continue with Google").click()
        page.wait_for_timeout(1000)
        page.get_by_role("link", name=buttonName).click()
        page.get_by_role("button", name="+ New Chat").click()
        page.wait_for_timeout(1000)
        return page