import gradio as gr

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

from dotenv import load_dotenv
import os


def initialize_driver(chromedriver_path: str):
    """Initializes and returns a WebDriver instance."""
    chrome_options = ChromeOptions()
    # chrome_options.add_argument("--headless")  # Run in headless mode (no GUI). Comment out to see what's going on.
    chrome_service = ChromeService(chromedriver_path)
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    return driver


def main():
    load_dotenv()
    chromedriver_path = os.getenv("CHROMEDRIVER_PATH")

    chatgpt_url = "https://chat.openai.com/?model=text-davinci-002-render-sha"
    bard_url = "https://bard.google.com/chat?utm_source=sem&utm_medium=paid-media&utm_campaign=q4enUS_sem7"
    claude_url = "https://claude.ai/chats"
    urls_list = [chatgpt_url, bard_url, claude_url]

    driver = initialize_driver(chromedriver_path)
    for url in urls_list:
        driver.get(url)

    # Initialize WebDriver
    driver.quit()


if __name__ == "__main__":
    main()
