"""TEST DATA PROJECT"""

# URLS
URL_LANDING = "https://thinking-tester-contact-list.herokuapp.com/"
URL_CONTACTS = "https://thinking-tester-contact-list.herokuapp.com/contactList"

# USER CREDENTIALS
EMAIL = "hello.world@gmail.com"
PASSWORD = "password_password"
USER_FIRST_NAME = "Robert"
USER_LAST_NAME = "Smith"

# INVALID CREDENTIALS
INVALID_EMAIL = "helloworldgmailcom"
WRONG_PASSWORD = "1234567890"
EMPTY_FIELD = ""

# CONTACT DATA
FIRST_NAME = "John"
LAST_NAME = "Doe"
BIRTHDATE = "2000-01-01"
EMAIL_ADDRESS = "john@doe.com"
PHONE = "1234567890"
STREET1 = "123 Main St"
STREET2 = "Apt 4B"
CITY = "Springfield"
STATE_PROVINCE = "IL"
POSTAL_CODE = "62704"
COUNTRY = "USA"

EDIT_FIRST_NAME = "RICARDO"
EDIT_LAST_NAME = "DIAZ"
EDIT_BIRTHDATE = "1999-12-12"
EDIT_EMAIL_ADDRESS = "HELLO@WORLD.COM"
EDIT_PHONE = "0987654321"
EDIT_STREET1 = "BOULEVARD OF BROKEN DREAMS"
EDIT_STREET2 = "80-180"
EDIT_CITY = "KYOTO"
EDIT_STATE_PROVINCE = "HAMPSHIRE"
EDIT_POSTAL_CODE = "200205"
EDIT_COUNTRY = "FRANCE"

# INVALID CHARACTERS IN CONTACT DATA
INVALID_CHARACTERS_BIRTHDATE = "not-a-date"
INVALID_CHARACTERS_EMAIL_ADDRESS = "invalid-email-template"
INVALID_CHARACTERS_PHONE = "non-digit"
INVALID_CHARACTERS_POSTAL_CODE = "non-digit"

# TOO LONG ENTRIES IN CONTACT DATA
LONG_FIRST_NAME = "Abcdefghijklmnopqrstu"  # 21/20
LONG_LAST_NAME = "Abcdefghijklmnopqrstu"  # 21/20
LONG_PHONE = "1234567890123456"  # 15/16
LONG_STREET1 = "AbcdefghijklmnopqrstuvwxyzAbcdefghijklmno"  # 41/40
LONG_STREET2 = "AbcdefghijklmnopqrstuvwxyzAbcdefghijklmno"  # 41/40
LONG_CITY = "AbcdefghijklmnopqrstuvwxyzAbcdefghijklmno"  # 41/40
LONG_STATE_PROVINCE = "Abcdefghijklmnopqrstu"  # 21/20
LONG_POSTAL_CODE = "12345678901"  # 11/10
LONG_COUNTRY = "AbcdefghijklmnopqrstuvwxyzAbcdefghijklmno"  # 41/40
