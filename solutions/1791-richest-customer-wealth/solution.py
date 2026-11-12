class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        # iterate through each customer
            # iterate through each customer's bank accounts
                # add current bank account's balance to a sum
        # return the max amount
        wealth = [0 for _ in accounts]
        for idx, guest in enumerate(accounts):
            for bal in guest:
                wealth[idx] += bal
        return max(wealth)

