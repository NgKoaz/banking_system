import asyncio
import datetime
import os
from captcha_solver.mbbank_solver import MbBankSolver
from mbbank import MBBankAsync


async def main():
    mb = MBBankAsync(username="USERNAME", password="PASSWORD", ocr_class=MbBankSolver())
    end_query_day = datetime.datetime.now()
    start_query_day = end_query_day - datetime.timedelta(days=30)
    print(await mb.getBalance())
    print(await mb.userinfo())
    print(await mb.getInterestRate())
    print(await mb.getAccountByPhone("USERNAME"))
    print(await mb.getBankList())
    print(await mb.getBalanceLoyalty())
    print(await mb.getLoanList())
    print(await mb.getSavingList())
    for i in ["TRANSFER", "PAYMENT"]:
        for a in ["MOST", "LATEST"]:
            await mb.getFavorBeneficiaryList(transactionType=i, searchType=a)
    card_list = await mb.getCardList()
    for i in card_list["cardList"]:
        await mb.getCardTransactionHistory(i["cardNo"], start_query_day, end_query_day)
    await mb.getTransactionAccountHistory(from_date=start_query_day, to_date=end_query_day)


asyncio.run(main())
