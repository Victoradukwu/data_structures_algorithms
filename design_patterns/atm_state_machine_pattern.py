"""Design an ATM using the State Machine Pattern"""

from abc import ABC, abstractmethod
from typing import Optional, Self


class ATM:
    def __init__(self):
        self.state = "UNAUTHORIZED"
        self.pin_code = "1234"

        # Transition table:
        self.transitions = {
            "UNAUTHORIZED": {
                "AUTHENTICATE": self._authenticate,
                "TRANSACT": self._deny_transaction,
                "LOGOUT": self._no_session
            },
            "AUTHORIZED": {
                "AUTHENTICATE": self._already_authenticated,
                "TRANSACT": self._perform_transaction,
                "LOGOUT": self._logout
            }
        }

    def handle_event(self, event, data=None):
        if event in self.transitions[self.state]:
            self.transitions[self.state][event](data)
        else:
            print(f"Invalid event '{event}' in state '{self.state}'.")

    # --- State transition methods ---
    def _authenticate(self, pin):
        if pin == self.pin_code:
            print("Authentication successful.")
            self.state = "AUTHORIZED"
        else:
            print("Invalid PIN.")

    def _perform_transaction(self, _):
        print("Transaction performed.")

    def _logout(self, _):
        print("Logged out.")
        self.state = "UNAUTHORIZED"

    def _deny_transaction(self, _):
        print("Access denied. Please authenticate first.")

    def _already_authenticated(self, _):
        print("Already authenticated.")

    def _no_session(self, _):
        print("No active session to logout from.")

# --- Example Usage ---
if __name__ == "__main__":
    atm = ATM()

    atm.handle_event("TRANSACT")  # Denied
    atm.handle_event("AUTHENTICATE", "0000")  # Wrong PIN
    atm.handle_event("AUTHENTICATE", "1234")  # Correct PIN
    atm.handle_event("TRANSACT")  # Allowed
    atm.handle_event("LOGOUT")  # Logged out
    atm.handle_event("TRANSACT")  # Denied again


"""
Alternative Implementation, à là workflow_mgt_state_machine.py
"""


class Event(ABC):
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name


class EventAuthenticate(Event):
    def __init__(self, pin):
        super().__init__("authenticate")
        self.pin = pin


class EventTransact(Event):
    def __init__(self):
        super().__init__("transact")


class EventLogout(Event):
    def __init__(self):
        super().__init__("logout")


class State(ABC):
    def __init__(self) -> None:
        self.pin_code = "1234"

    @abstractmethod
    def handle_event(self, event: Event) -> Optional[Self]:
        pass

    def __eq__(self, other) -> bool:
        return self.__class__ == other.__class__


class UnAuthorizedState(State):
    def handle_event(self, event: Event):
        if isinstance(event, EventAuthenticate):
            if event.pin == self.pin_code:
                print("Authentication successful.")
                return AuthorizedState()
        else:
            print("Your logged out. Log in to continue")


class AuthorizedState(State):
    def handle_event(self, event: Event) -> Optional[State]:
        if isinstance(event, EventAuthenticate):
            print("Already authorised.")
        elif isinstance(event, EventTransact):
            print("Transaction successful")
        else:
            print("Successfully logged out")
            return UnAuthorizedState()


class Transition:
    """Base class for all types of Transitions"""

    def __init__(self, event, from_state, to_state):
        self.event = event
        self.from_state = from_state
        self.to_state = to_state


class TransitionManager:
    def __init__(self):
        self.transitions = []

    def add_transition(self, transition):
        self.transitions.append(transition)

    def handle_event(self, current_state, event):
        """Handle a sequence of transitions"""
        for transition in self.transitions:
            if transition.from_state == current_state and transition.event == event:
                return current_state.handle_event(transition.event)
        return current_state