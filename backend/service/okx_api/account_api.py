# account_api_wrapper.py

import okx.Account as Account
from typing import Dict
from backend.service.decorator import add_docstring


class AccountAPIWrapper:
    def __init__(self, apikey, secretkey, passphrase, flag):
        self.accountAPI = Account.AccountAPI(apikey, secretkey, passphrase, False, flag)

    @add_docstring("获取账户余额")
    def get_account_balance(self) -> Dict:
        return self.accountAPI.get_account_balance()

    @add_docstring("账户持仓信息 - 期货交易")
    def get_positions(self) -> Dict:
        return self.accountAPI.get_positions()

    @add_docstring("账户历史持仓信息")
    def get_positions_history(self) -> Dict:
        return self.accountAPI.get_positions_history()

    @add_docstring("账户账单流水")
    def get_account_bills_archive(self) -> Dict:
        return self.accountAPI.get_account_bills_archive()
