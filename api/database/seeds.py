from sqlalchemy import Engine
from sqlmodel import Session

from api.public.transaction.models import Transaction
from api.public.user.models import User, UserRoles
from api.public.wallet.models import Wallet


# TODO: Refactor
userData = {
    "name": "Alex",
    "role": UserRoles.ADMIN,
}
walletData = {"total": 100}
transactionData = {
    "amount": 100,
    "type": "INCOME",
}


def seed_database(engine: Engine):
    with Session(engine) as session:
        database_is_seeded = session.get(User, "5c49ade2-e01d-4b6b-b57e-5a737d050404")

        # TODO: avoid needing this, use upsert instead
        if database_is_seeded:
            print("Database already seeded")
            return

        new_wallet = Wallet(**walletData)
        new_transaction = Transaction(**transactionData, wallet=new_wallet)

        new_user = User(**userData, wallet=new_wallet)
        session.add(new_user)
        session.add(new_transaction)

        session.commit()

        session.refresh(new_user)
        session.refresh(new_transaction)
