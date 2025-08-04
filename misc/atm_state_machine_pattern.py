"""Design an ATM using the State Machine Pattern"""

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

    atm.handle_event("TRANSACT")             # Denied
    atm.handle_event("AUTHENTICATE", "0000") # Wrong PIN
    atm.handle_event("AUTHENTICATE", "1234") # Correct PIN
    atm.handle_event("TRANSACT")             # Allowed
    atm.handle_event("LOGOUT")               # Logged out
    atm.handle_event("TRANSACT")             # Denied again
