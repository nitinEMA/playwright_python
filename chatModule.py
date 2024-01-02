class ChatModule:
    def askInChat(self, page, text):
        page.get_by_placeholder("Ask Ema anything...").click()
        page.get_by_placeholder("Ask Ema anything...").fill(text)
        page.locator("div:nth-child(5) > .w-4\\/6 > div:nth-child(3)").click()
        page.wait_for_timeout(10000)
        
        element = page.locator('body > div.w-full.h-full.bg-onboarding > div > div.chat-header.w-4\\/6.\\32 xl\\:w-3\\/4.z-10.bg-white.shadow-\\[-5px_0px_11px_rgba\\(0\\,0\\,0\\,0\\.08\\)\\]')
        inner_text = element.inner_text()
        return inner_text
