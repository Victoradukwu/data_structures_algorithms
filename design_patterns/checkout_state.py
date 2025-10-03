"""_summary_
This is based on a Medium.com tutorial by Amir Lavasani:
https://medium.com/@amirm.lavasani/design-patterns-in-python-state-8916b2f65f69

"""

from abc import ABC, abstractmethod
from typing import Optional, Self

from design_patterns.work_flow_mgt_state_machine import current_state


class CheckoutState(ABC):
    @abstractmethod
    def add_item(self, item) -> Optional[Self]:
        pass

    @abstractmethod
    def review_cart(self)->Optional[Self]:
        pass

    @abstractmethod
    def enter_shipping_info(self, info) -> Optional[Self]:
        pass

    @abstractmethod
    def process_payment(self) -> Optional[Self]:
        pass

        """_summary_

        Below is an alternative implementation
        """
class EmptyCartState(CheckoutState):
    def add_item(self, item) -> CheckoutState:
        print("f{item} added to the cart.")
        return ItemAddedState()

    def review_cart(self) -> None:
        print("Cannot review an empty cart.")

    def enter_shipping_info(self, info):
        print("Cannot enter shipping info with an empty cart.")

    def process_payment(self):
        print("Cannot process payment with an empty cart.")


class ItemAddedState(CheckoutState):
    def add_item(self, item):
        print("Item added to the cart.")

    def review_cart(self):
        print("Reviewing cart contents.")
        return CartReviewedState()

    def enter_shipping_info(self, info):
        print("Cannot enter shipping info without reviewing the cart.")

    def process_payment(self):
        print("Cannot process payment without entering shipping info.")


class CartReviewedState(CheckoutState):
    def add_item(self, item):
        print("Cannot add items after reviewing the cart.")

    def review_cart(self):
        print("Cart already reviewed.")

    def enter_shipping_info(self, info):
        print("Entering shipping information.")
        return ShippingInfoEnteredState(info)

    def process_payment(self):
        print("Cannot process payment without entering shipping info.")


class ShippingInfoEnteredState(CheckoutState):
    def __init__(self, info):
        self.info = info
        
    def add_item(self, item):
        print("Cannot add items after entering shipping info.")

    def review_cart(self):
        print("Cannot review cart after entering shipping info.")

    def enter_shipping_info(self, info):
        print("Shipping information already entered.")

    def process_payment(self):
        print("Processing payment with the entered shipping info.")
        

class CheckoutContext:
    def __init__(self):
        self.current_state = EmptyCartState()

    def add_item(self, item):
        self.current_state = self.current_state.add_item(item) # type: ignore

    def review_cart(self):
        self.current_state = self.current_state.review_cart() # type: ignore

    def enter_shipping_info(self, info):
        self.current_state = self.current_state.enter_shipping_info(info) # type: ignore

    def process_payment(self):
        self.current_state.process_payment() # type: ignore
        
        
if __name__ == "__main__":
    cart = CheckoutContext()

    cart.add_item("Product 1")
    cart.review_cart()
    cart.enter_shipping_info("123 Main St, City")
    cart.process_payment()
    
    
    
    
class ShoppingCart:
    def __init__(self):
        self.current_state = EmptyCartState()
        self.cart = []
        
        # transition table
        self.transitions = {
            "EMPTY_CART": {
                "ADD_ITEM": self.add_item,
                "REVIEW_CART": self.cannot_review_empty_cart,
                "SHIPPING_INFO": self.cannot_add_shipping_info,
                "PROCESS_PAYMENT": self.cannot_process_payment,
            },
            "ITEM_ADDED": {
                "ADD_ITEM": self.item_alread_already_added,
                "REVIEW_CART": self.review_cart,
                "SHIPPING_INFO": self.cannot_add_shipping_info,
                "PROCESS_PAYMENT": self.cannot_process_payment,
            },
            "CART_REVIEWD": {
                "ADD_ITEM": self.item_alread_already_added,
                "REVIEW_CART": self.cart_already_reviewed,
                "SHIPPING_INFO": self.cannot_add_shipping_info,
                "PROCESS_PAYMENT": self.cannot_process_payment,
            },
            "SHIPPING_INFO_ENTERED": {
                "ADD_ITEM": self.item_alread_already_added,
                "REVIEW_CART": self.cart_already_reviewed,
                "SHIPPING_INFO": self.shipping_info_already_added,
                "PROCESS_PAYMENT": self.process_payment,
            },
            "PEYMENT_PROCESSED": {
                "ADD_ITEM": self.item_alread_already_added,
                "REVIEW_CART": self.cart_already_reviewed,
                "SHIPPING_INFO": self.shipping_info_already_added,
                "PROCESS_PAYMENT": self.payment_already_processed,
            },
        }
    
    def handle_event(self, event):
        if event in self.transitions.get(self.current_state): # type: ignore
            self.transitions.get(current_state).get(event)() # type: ignore
    
    def add_item(self, item):
        self.cart.append(item)
        print(f'{item} added to the cart')
    
    def item_alread_already_added(self, item):
        print(f"{item} already added to the cart")
    
    def cannot_review_empty_cart(self):
        print("Cannot review an empty cart")
    
    def review_cart(self):
        print("Cart content is being reviewed")
    
    def cart_already_reviewed(self):
        print("Cart content is already reviewed")
    
    def cannot_add_shipping_info(self):
        print("please review cart before adding shipping info")
    
    def enter_shipping_info(self, info):
        print('Shippinf info is being added')
    
    def shipping_info_already_added(self):
        print("Shippinf info is already added")
    
    def cannot_process_payment(self):
        print("please shipping info before processing payment")
    
    def process_payment(self):
        print("Payment is being processed")
    
    def payment_already_processed(self):
        print("Payment is alread processed")