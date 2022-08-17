from ast import Index
import brownie
from brownie import IndexComponents,Contract,accounts, network
import pytest

@pytest.fixture
def index_components_contract():
    if network.show_active() == "mainnet-fork":
        return accounts[0].deploy(IndexComponents)
    elif network.show_active() == "mainnet":
        return IndexComponents[-1]
    else:
        raise Exception("Wrong network for these tests")
    

@pytest.fixture
def get_components_function(index_components_contract):
    return index_components_contract.getComponents("0x632806bf5c8f062932dd121244c9fbe7becb8b48")

@pytest.fixture
def get_vtoken_array(index_components_contract):
    return index_components_contract.getVTokenArray("0x632806bf5c8f062932dd121244c9fbe7becb8b48")

def test_array_length(get_components_function, get_vtoken_array):
    pdi_contract = Contract.from_explorer("0x632806bf5c8f062932dd121244c9fbe7becb8b48")
    active_anatomy = [i for i in pdi_contract.anatomy()[0]]
    length = len(active_anatomy) + len(pdi_contract.inactiveAnatomy())
    assert len(get_components_function) == length
    assert len(get_vtoken_array) == length


