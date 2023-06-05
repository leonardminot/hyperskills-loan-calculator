import unittest

from loan_calculator import get_months_to_repay, get_monthly_loan, get_last_loan, print_number_of_month_to_repay, \
    print_monthly_loan


class MyTestCase(unittest.TestCase):
    def test_when_loan_is_1000_and_monthly_payment_is_150_then_it_will_take_7_months_to_repay_the_loan(self):
        # Given
        loan_principal: int = 1000
        monthly_payment: int = 150

        # When
        months_to_repay: int = get_months_to_repay(loan_principal, monthly_payment)

        # Then
        self.assertEqual(months_to_repay, 7)

    def test_when_loan_is_1000_and_monthly_payment_is_1000_then_it_will_take_1_month_to_repay(self):
        # Given
        loan_principal: int = 1000
        monthly_payment: int = 1000

        # When
        months_to_repay: int = get_months_to_repay(loan_principal, monthly_payment)

        # Then
        self.assertEqual(months_to_repay, 1)

    def test_when_loan_is_1000_and_number_of_month_is_10_then_monthly_loan_is_100(self):
        # Given
        loan_principal: int = 1000
        number_of_repay_month: int = 10

        # When
        monthly_loan = get_monthly_loan(loan_principal, number_of_repay_month)

        # Then
        self.assertEqual(monthly_loan, 100)

    def test_when_loan_is_1000_and_number_of_month_is_9_then_monthly_loan_is_112(self):
        # Given
        loan_principal: int = 1000
        number_of_repay_month: int = 9

        # When
        monthly_loan = get_monthly_loan(loan_principal, number_of_repay_month)

        # Then
        self.assertEqual(monthly_loan, 112)

    def test_when_loan_is_1000_and_number_of_month_is_9_then_last_loan_is_104(self):
        # Given
        loan_principal: int = 1000
        number_of_repay_month: int = 9

        # When
        last_loan = get_last_loan(loan_principal, number_of_repay_month)

        # Then
        self.assertEqual(last_loan, 104)

    def test_given_monthly_payment_of_7_months_print_sentence(self):
        # Given
        number_of_repay_month = 7

        # When
        sentence_to_print = print_number_of_month_to_repay(number_of_repay_month)

        # Then
        self.assertEqual(sentence_to_print, "It will take 7 months to repay the loan")

    def test_given_monthly_payment_of_1_months_print_sentence(self):
        # Given
        number_of_repay_month = 1

        # When
        sentence_to_print = print_number_of_month_to_repay(number_of_repay_month)

        # Then
        self.assertEqual(sentence_to_print, "It will take 1 month to repay the loan")

    def test_given_monthly_payment_of_100_then_print_sentence(self):
        # Given
        monthly_loan = 100

        # When
        sentence_to_print = print_monthly_loan(monthly_loan)

        # Then
        self.assertEqual(sentence_to_print, "Your monthly payment = 100")

    def test_given_monthly_payment_of_112_and_last_payment_of_104_then_print_sentence(self):
        # Given
        monthly_loan = 112
        last_payment = 104

        # When
        sentence_to_print = print_monthly_loan(monthly_loan, last_payment)

        # Then
        self.assertEqual(sentence_to_print, "Your monthly payment = 112 and the last payment = 104.")


if __name__ == '__main__':
    unittest.main()
