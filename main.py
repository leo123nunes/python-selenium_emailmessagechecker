from app import ChromeAuto

chrome = ChromeAuto()

try:

    chrome.open_browser()
    chrome.signin()

except Exception as e:
    print(e)
