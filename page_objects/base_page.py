
def go_to_homepage(selenium, base_url):
    selenium.get(base_url)


def do_click_account_icon(selenium):
    account_icon = selenium.find_element_by_id('path-1')
    account_icon.click()
