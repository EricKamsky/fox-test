import helper_utils


def do_click_sign_up_button(selenium):
    sign_up_button = selenium.find_element_by_css_selector('button.Account_signUp_3SpTs')
    sign_up_button.click()


def do_click_sign_in_button(selenium):
    sign_in_button = selenium.find_element_by_css_selector('button.Account_signIn_Q0B7n')
    sign_in_button.click()


def do_fill_sign_up_field(selenium, field, text):
    # maybe consolidate these besides birthday locator, pass in locator instead, and just validate that it's in list.
    fields = {'FirstName', 'LastName', 'Email', 'Password', 'Birthday'}
    if field not in fields:
        raise ValueError('Field: {field} not in {fields}!'.format(field=field, fields=fields))
    if field is 'Birthday':
        selenium.find_element_by_css_selector('div.Account_signupBirthdayGenderContainer_1n0m8 > div.Account_signupColumnSplit_YtgPc > input.Account_signupField_21Jct').send_keys(text)
    else:
        selenium.find_element_by_name('signup%s' % field).send_keys(text)


def do_select_gender(selenium, gender=None):
    drill_down_select = selenium.find_element_by_css_selector('a.Dropdown_selectedText_3xUOl.AccountSignupDropdown_selectedText_1SbK3')
    drill_down_select.click()
    if gender is 'Male':
        selenium.find_element_by_xpath("//a[contains(text(),'Male')]").click()
    elif gender is 'Female':
        selenium.find_element_by_xpath("//a[contains(text(),'Female')]").click()
    else:
        selenium.find_element_by_xpath('//a[3]/div').click()


def do_click_create_profile_button(selenium):
    create_profile_button = selenium.find_element_by_css_selector('div.Account_signupButtonDesktop_1PCXs > button')
    create_profile_button.click()


def do_sign_up(selenium, first_name=helper_utils.get_first_name(), last_name=helper_utils.get_last_name(), email=helper_utils.get_email(),
               password=helper_utils.get_password(), birth_day=helper_utils.get_birth_date()):
    do_fill_sign_up_field(selenium, field='FirstName', text=first_name)
    do_fill_sign_up_field(selenium, field='LastName', text=last_name)
    do_fill_sign_up_field(selenium, field='Email', text=email)
    do_fill_sign_up_field(selenium, field='Password', text=password)
    do_fill_sign_up_field(selenium, field='Birthday', text=birth_day)
    do_select_gender(selenium)
    do_click_create_profile_button(selenium)


def get_signup_confirmation_text(selenium):
    return selenium.find_element_by_css_selector('div.Account_signupSuccessHeaderText_3N7UQ').text


def do_click_account_created_done_button(selenium):
    done_button = selenium.find_element_by_css_selector('button')
    done_button.click()


def do_sign_in(selenium, email, password):
    email_field = selenium.find_element_by_name('signinEmail')
    email_field.send_keys(email)
    password_field = selenium.find_element_by_name('signinPassword')
    password_field.send_keys(password)
    sign_in_button = selenium.find_element_by_css_selector('div.Account_signinButtonDesktop_2SO1g > button')
    sign_in_button.click()

