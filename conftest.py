import pytest

# Use existing user
EMAIL = 'erickamsky@gmail.com'
PASSWORD = 'password'

@pytest.fixture(scope="session")
def get_email():
    return EMAIL


@pytest.fixture(scope="session")
def get_password():
    return PASSWORD


@pytest.fixture
def selenium(selenium):
    selenium.implicitly_wait(10)
    #selenium.maximize_window()
    return selenium