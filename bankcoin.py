from ecdsa import SigningKey, SECP256k1
from utils import serialize

def transfer_message(previous_signature, public_key):
    return serialize({
        "previous_signature": previous_ssignature,
        "next_owner_public_key": public_key,
    })


class Transfer:
    
    def __init__(self, signature, public_key):
        self.signature = signature
        self.public_key = public_key


class BankCoin:
    
    def __init__(self, transfers):
        self.transfers = transfers

    def validate(self):
        # Check the subsequent transfers
        previous_transfer = self.transfers[0]
        for transfer in self.transfers[1:]:
            # Check previous owner signed this transfer using their private key
            assert previous_transfer.public_key.verify(
                transfer.signature,
                transfer_message(previous_transfer.signature, transfer.public_key),

            )
            previous_transfer = transfer


def issue(public_key):
    transfer = Transfer(
        signature=None,
        public_key=public_key,
    )
    
    # Create and return the coin with just the issuing transfer
    coin = ECDSACoin(transfers=[transfer])
    return coin

class Bank:
    def __init__(self):
        # coin.id -> coin
        self.coins = {}
        