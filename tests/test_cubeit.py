from playwright.sync_api import Page, expect

BASE_URL = "http://localhost:8000"

def test_cube(page: Page) -> None:
    page.goto(BASE_URL)
    input = page.get_by_placeholder("enter number...")
    input.fill("5")

    page.get_by_role(
        "button", name="Cube"
    ).click()

    result = page.locator("p#result") # If we inspect, we see that is a paragraph <p> with the id="result"
    expect(result).to_contain_text("125")


#Another test case whe the input field is empty
def test_empty_input(page: Page):
    page.goto(BASE_URL)
    input = page.get_by_placeholder("enter number...")
    input.fill("")

    page.get_by_role(
        "button", name="Cube"
    ).click()

    result = page.locator("p#result")
    expect(result).to_contain_text(
        "Enter something!"
    )