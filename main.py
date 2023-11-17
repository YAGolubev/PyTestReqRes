from playwright.sync_api import Playwright, expect, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://reqres.in/", wait_until="domcontentloaded")
    list_endpoints = page.locator("li[data-key='endpoint']")
    print(list_endpoints)
    # eleText = list_endpoints.all_text_contents()
    # print(eleText)
    # eleText = list_endpoints.all_inner_text()
    # print(eleText)
    print(list_endpoints.count())
    expect(list_endpoints).to_have_count(15)
    # page.locator("li").filter(has_text="List users").click()
    # page.get_by_role("link", name="/api/users?page=2").click()
    # page.goto("https://reqres.in/")
    # page.get_by_text("200", exact=True).click()
    # page.get_by_text("{ \"page\": 2, \"per_page\": 6, \"total\": 12,
    # \"total_pages\": 2, \"data\": [ { \"id\": 7, ").click()

    # page.locator("li").filter(has_text="List users").click()
    # expect_request = page.locator('span[data-key="url"]')
    # expect_response_code = page.locator('span[data-key="response-code"]')
    # expect_output_response = page.locator('pre[data-key="output-response"]')
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
