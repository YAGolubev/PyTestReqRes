# from main.sync_api import Playwright, sync_playwright, expect
from main.sync_api import sync_playwright


def test_endpoints():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://reqres.in/")
        # listOfElements = page.locator("//h3[@class='search-result__title']")
        # listOfElements = page.locator('li[data-key="endpoint"]')
        # print(listOfElements)
        # expect(listOfElements).to_have_count(15)
        page.locator("li").filter(has_text="List users").click()
        expect_request = page.locator('span[data-key="url"]')
        expect_response_code = page.locator('span[data-key="response-code"]')
        expect_output_response = page.locator('pre[data-key="output-response"]')
        context = playwright.request.new_context()
        response = context.get(f"https://reqres.in{expect_request}")
        assert response.status == expect_response_code
        assert response.json() == expect_output_response

        # reqres_api.reqres_single_user(user_id).status_code_should_be(200). \
        #         json_schema_should_be_valid('single_user_schema'). \
        #         objects_should_be(expected_data, reqres_api.deserialize_single_user())

        # page.locator("li").filter(has_text="Single user").first.click()
        # page.locator("li").filter(has_text="Single user not found").click()
        # page.locator("li").filter(has_text="List <resource>").click()
        # page.locator("li").filter(has_text="Single <resource>").first.click()
        # page.locator("li").filter(has_text="Single <resource> not found").click()
    # context.close()
    # browser.close()


def test_get(playwright: sync_playwright):
    context = playwright.request.new_context()
    response = context.get("https://reqres.in/")
    print(response)
    assert response.status == 200
    assert response.status_text == "OK"


# def run(playwright: Playwright) -> None:

#
#     # ---------------------

#
# with sync_playwright() as playwright:
#     run(playwright)
