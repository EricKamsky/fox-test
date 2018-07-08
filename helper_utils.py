import conftest
import string
import random
import datetime
import time


def get_random_string(length):
    stg = ''.join([random.choice(string.letters) for i in xrange(length)]).lower()
    return stg


def get_first_name():
    first_name = 'Just' + get_random_string(5)
    return first_name


def get_last_name():
    last_name = 'Me' + get_random_string(5)
    return last_name


def get_birth_date():
    year = random.randint(1950, 2000)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    birth_date = '{}{}{}'.format(month,day,year)
    return birth_date


def get_email():
    ts = time.time()
    time_stamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H-%M-%S')
    email = conftest.get_email()
    email_split = email.split('@')
    email_user_name = email_split[0]
    email_domain = email_split[1]
    email = '{user_name}+{time_stamp}@{email_domain}'.format(user_name=email_user_name, time_stamp=time_stamp,
                                                            email_domain=email_domain)
    return email


def get_password():
    password = "password"
    return password


