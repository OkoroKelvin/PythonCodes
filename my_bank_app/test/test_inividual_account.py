import unittest

from my_bank_app.models.information import UserInformation


class BankTest(unittest.TestCase):

    def test_individual_account_request(self):
        first_name = "John"
        last_name = "Doe"
        phone_number = "08097685743"
        bvn = "43454566763456"
        username = "everybees"
        password = "my#password"
        account_type = "individual_account"

        user_account_details = UserInformation(first_name, last_name, phone_number, password, bvn=bvn,
                                               username=username, account_type=account_type)
        self.assertEqual(user_account_details.account_type, "individual_account")
