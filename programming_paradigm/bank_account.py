#!/usr/bin/env python3
"""
BankAccount class module that encapsulates banking operations.
"""


class BankAccount:
    """
    A class representing a simple bank account with basic operations.
    """

    def __init__(self, initial_balance=0):
        """
        Initialize the bank account with an optional initial balance.

        Args:
            initial_balance: The starting balance (default 0)
        """
        self.account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposit money into the account.

        Args:
            amount: The amount to deposit
        """
        self.account_balance += amount

    def withdraw(self, amount):
        """
        Withdraw money from the account if sufficient funds are available.

        Args:
            amount: The amount to withdraw

        Returns:
            bool: True if withdrawal was successful, False otherwise
        """
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """
        Display the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.account_balance}")
