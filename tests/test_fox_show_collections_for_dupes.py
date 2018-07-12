import pytest
import conftest
import spreadsheet_utils
from page_objects import account
from page_objects import base_page
from page_objects import shows

OTHER_COLLECTIONS = ['FX', 'National Geographic', 'FOX Sports', 'All Shows']


@pytest.mark.nondestructive
def test_shows_for_dupes_with_existing_account(selenium, base_url):
    show_dupes_file = 'show_dupes.xlsx'

    base_page.go_to_homepage(selenium, base_url)
    base_page.do_click_account_icon(selenium)

    account.do_click_sign_in_button(selenium)
    account.do_sign_in(selenium, conftest.get_email(), conftest.get_password())

    shows.go_to_shows(selenium, base_url)

    shows.go_to_shows_collection(selenium, collection='FOX')
    fox_last_four_shows = shows.get_show_names(selenium)[-4:]
    fox_last_four_shows.sort()
    spreadsheet_utils.write_fox_shows(fox_last_four_shows, file=show_dupes_file)

    for collection in OTHER_COLLECTIONS:
        shows.go_to_shows_collection(selenium, collection=collection)
        other_shows = shows.get_show_names(selenium)
        spreadsheet_utils.write_collection_if_dupe(fox_last_four_shows, collection_shows=other_shows, collection=collection, file=show_dupes_file)


def test_shows_for_dupes_with_new_account(selenium, base_url):
    show_dupes_file = 'show_dupes_2.xlsx'

    base_page.go_to_homepage(selenium, base_url)
    base_page.do_click_account_icon(selenium)

    account.do_click_sign_up_button(selenium)
    account.do_sign_up(selenium)
    assert account.get_signup_confirmation_text(selenium) == 'Thanks for Signing Up!'

    shows.go_to_shows(selenium, base_url)

    shows.go_to_shows_collection(selenium, collection='FOX')
    fox_last_four_shows = shows.get_show_names(selenium)[-4:]
    fox_last_four_shows.sort()
    spreadsheet_utils.write_fox_shows(fox_last_four_shows, file=show_dupes_file)

    for collection in OTHER_COLLECTIONS:
        shows.go_to_shows_collection(selenium, collection=collection)
        other_shows = shows.get_show_names(selenium)
        spreadsheet_utils.write_collection_if_dupe(fox_last_four_shows, collection_shows=other_shows, collection=collection, file=show_dupes_file)
