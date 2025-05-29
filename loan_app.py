from datetime import date

class LoanArrearsCalculator:
    def __init__(self, serial, principal, rate, period, issue_date, principal_balance, interest_balance):
        self.serial = serial
        self.principal = principal
        self.rate = rate
        self.period = period
        self.issue_date = issue_date # should be a date object
        self.principal_balance = principal_balance
        self.interest_balance = interest_balance
        self.serviced_period = self._months_difference(issue_date)

    @staticmethod
    def _months_difference(issued_date):
        today = date.today()
        month_difference = (today.year - issued_date.year) * 12 + today.month - issued_date.month
        if today.day < issued_date.day:
            month_difference -= 1
        return month_difference
    def _principal_arrears(self):
        principal_payment = self.principal / self.period
        principal_to_pay = principal_payment * self.serviced_period
        arrears = (principal_to_pay - self.principal) + self.principal_balance
        return  arrears
    def _total_interest_reducing(self):
        principal_payment = self.principal / self.period
        principal = self.principal
        cumulative_interest = 0
        for _ in range(1, self.serviced_period + 1):
            interest_for_month = (self.rate / 100) * principal
            principal -= principal_payment
            cumulative_interest += interest_for_month
        return cumulative_interest
    def _average_interest(self):
        principal_payment = self.principal / self.period
        av_int = (principal_payment * self.rate * (self.period + 1)) / 200
        total_interest_to_pay= av_int * self.serviced_period
        return total_interest_to_pay
    def calculate_arrears(self):
        principal_arrears = self._principal_arrears()
        interest_to_be_paid = self._average_interest()
        total_period_interest = self._total_interest_reducing()
        paid_interest = total_period_interest - self.interest_balance
        interest_arrears = interest_to_be_paid - paid_interest
        return f"Principal Arrears: {principal_arrears:.2f}. Interest Arrears: {interest_arrears:.2f}"