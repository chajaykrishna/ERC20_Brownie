from brownie import OurToken
from toolz.itertoolz import get
from scripts.helpful_scripts import get_account
from web3 import Web3

initial_supply = Web3.toWei(1000, "ether")
def main():
    our_token = OurToken.deploy(initial_supply,{"from": get_account()})
    print (our_token.name(), our_token.symbol())