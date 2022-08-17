import brownie
from brownie import IndexComponents,Contract
import pytest

@pytest.fixture
def index_components_contract():
    return IndexComponents[1]

@pytest.fixture
def get_components_function(index_components_contract):
    return index_components_contract.getComponents("0x632806bf5c8f062932dd121244c9fbe7becb8b48")

def test_array_length(get_components_function):
    pdi_contract = Contract.from_explorer("0x632806bf5c8f062932dd121244c9fbe7becb8b48")
    active_anatomy = [i for i in pdi_contract.anatomy()[0]]
    length = len(active_anatomy) + len(pdi_contract.inactiveAnatomy())
    assert len(get_components_function) == length

