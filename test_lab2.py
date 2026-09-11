import ecommerce_form
import logging
import pytest 

logging.basicConfig(
    level= logging.DEBUG,
    filename= 'test.log',
    filemode='w'
)
@pytest.fixture
def system():
    return ecommerce_form.OnlinePurchase()

@pytest.mark.parametrize('quantity, expected',[
    (8,True),
    (0, False),
    (-1, False),
    (.8, False)
    ])
@pytest.mark.unit
def test_validate_quantity_component(system, quantity, expected):
    result=system.validate_quantity(quantity)
    assert result == expected

####

@pytest.mark.parametrize('coupon, expected',[
    ('DISCOUNT10',True),
    ('DISCOUNT20', True),
    ('DISCOUNT30', False),
    ('DISCOUNT40', False)
    ])
@pytest.mark.unit
def test_validate_coupon(system, coupon, expected):
    result=system.validate_coupon(coupon)
    assert result == expected
###

@pytest.mark.parametrize('address, expected',[
    ('av patria',True),
    ('dos', False),
    ('332222323', False)
    ])
@pytest.mark.wip
def test_validate_address(system, address, expected):
    result=system.validate_address(address)
    assert result == expected

@pytest.mark.system
def test_purchase_itemzero(system):
    logging.info('TestCase 1')
           
    #system = ecommerce_form.OnlinePurchase()
    cart ={
        'Laptop': 0,
        'Mouse': 2
    }
    coupon = 'DISCOUNT10' 
    address = 'Av Patria'
    result = system.process_purchase(cart, coupon, address)

    assert 'integer greater than 0' in result

    logging.info (f'Result:{result}')
    logging.info('TestCase FINISHED')

@pytest.mark.system
def test_coupon_invalid():
    logging.info('TestCase 2 (RF3)')
    system = ecommerce_form.OnlinePurchase()

    cart ={
        'Laptop': 1,
        'Mouse': 2
    }
    coupon = 'DISCOUNT30' 
    address = 'Av Patria'
    result = system.process_purchase(cart, coupon, address)
    assert 'code is not valid' in result
    logging.info('TestCase 2 FINISHED')

@pytest.mark.system
def test_coupon_valid():
    logging.info('TestCase 3 (RF9)')
    system = ecommerce_form.OnlinePurchase()

    cart ={
        'Laptop': 1,
        'Mouse': 2
    }
    coupon = 'DISCOUNT10' 
    address = 'Av Patria'
    result = system.process_purchase(cart, coupon, address)
    assert 'DISCOUNT10' in result
    assert '990' in result
    logging.info('TestCase 3 FINISHED')

if __name__ == '__main__':
    ola=0

    
