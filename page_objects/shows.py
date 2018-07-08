
def go_to_shows(selenium, base_url):
    selenium.get(base_url + '/shows')


def go_to_shows_collection(selenium, collection):
    collections = {'FOX' :1, 'FIFA': 2, 'FX': 3, 'National Geographic': 4, 'FOX Sports': 5, 'All Shows': 6}
    if collection not in collections:
        raise ValueError('Collection: {collection} not in {collections}!'.format(collection=collection, collections=collections))
    base_locator = 'a.PageHeaderBrowse_tab_19aN7:nth-child(%s)'
    collection_index = collections.get(collection)
    collection_tab = selenium.find_element_by_css_selector(base_locator % collection_index)
    collection_tab.click()
    print 'Collection: %s' % collection


def get_show_names(selenium):
    base_locator = 'div.Tile_tile_3qaLc:nth-child(%s) > div:nth-child(2)'
    show_names = []
    show_index = 1
    while _is_css_selector_present(selenium, base_locator % show_index):
        show = selenium.find_element_by_css_selector(base_locator % show_index)
        selenium.execute_script("arguments[0].scrollIntoView();", show)
        show_name = show.text.encode('utf-8').strip()
        print '#{show_index} Show: {show_name}'.format(show_index=show_index, show_name=show_name)
        show_names.append(show_name)
        show_index = show_index + 1
    return show_names


def _is_css_selector_present(selenium, css_selector):
    try:
        selenium.find_element_by_css_selector(css_selector)
        return True
    except:
        return False
