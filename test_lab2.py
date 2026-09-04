import ecommerce_form
import logging

logging.basicConfig(
    level= logging.DEBUG,
    filename= 'test.log',
    filemode='w'
)

def test_purchase_itemzero():
    logging.info('TestCase 1')
           
    system = ecommerce_form.OnlinePurchase()

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

    
