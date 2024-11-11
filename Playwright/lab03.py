import re
from playwright.sync_api import Page, expect


def test_webpage(page: Page):
    page.goto("https://google.co.in")
    # Create a locator.
    get_started = page.get_by_role("link", name="Get started")
    # Click it.
    get_started.click()


