from abc import ABC, abstractmethod
from typing import Optional, Self


class Event:
    """Base class for all types of Events"""

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

class State(ABC):
    """Base class for all types of States"""

    @abstractmethod
    def handle_event(self, event: Event)->Optional[Self]:
        pass

    def __eq__(self, other):
        return self.__class__ == other.__class__


class Transition:
    """Base class for all types of Transitions"""
    def __init__(self, event, from_state, to_state):
        self.event = event
        self.from_state = from_state
        self.to_state = to_state 


#Concrete Implementations of Event
class EventSubmitForApproval(Event):
    def __init__(self):
        super().__init__("submit_for_approval")

class EventApprove(Event):
    def __init__(self):
        super().__init__("approve")

class EventCancel(Event):
    def __init__(self):
        super().__init__("cancel")


# Concrete implementations of State
class PendingApprovalState(State):
    """The only transition allowed in this state is `PendingApprovalState`--->`InProgressState`,
    triggered by `EventSubmitForApproval` event
    """
    def handle_event(self, event):
        if isinstance(event, EventSubmitForApproval):
            print("Workflow submitted for approval.")
            return InProgressState()
        else:
            print(f"Invalid event '{event.name}' for the Pending Approval state.")
            return self


class InProgressState(State):
    """The only transitions allowed in this state are:
    1. `InProgressState`--->`CompletedState`, triggered by `EventApprove` event
    2. `InProgressState`--->`CancelledState`, triggered by `EventCancel` event
    """
    def handle_event(self, event):
        if isinstance(event, EventApprove):
            print("Workflow approved.")
            return CompletedState()
        elif isinstance(event, EventCancel):
            print("Workflow canceled.")
            return CanceledState()
        else:
            print(f"Invalid event '{event.name}' for the In Progress state.")
            return self


class CompletedState(State):
    """No transition from this state to any other; it's a terminal state"""
    def handle_event(self, event):
        print(f"Invalid event '{event.name}' for the Completed state.")
        return self


class CanceledState(State):
    """No transition from this state to any other; it's a terminal state"""
    def handle_event(self, event):
        print(f"Invalid event '{event.name}' for the Canceled state.")
        return self
    
    
class TransitionManager:
    def __init__(self):
        self.transitions = []

    def add_transition(self, transition):
        self.transitions.append(transition)

    def handle_event(self, current_state, event):
        """Handle a sequence of transitions"""
        for transition in self.transitions:
            # current_state.handle_event(transition.event)
            if transition.from_state == current_state and transition.event == event:
                return current_state.handle_event(transition.event)
        return current_state
    
    
# Testing the implementation
workflow = TransitionManager()
workflow.add_transition(Transition(EventSubmitForApproval(), PendingApprovalState(), InProgressState()))
workflow.add_transition(Transition(EventApprove(), InProgressState(), CompletedState()))
workflow.add_transition(Transition(EventCancel(), InProgressState(), CanceledState()))

current_state = PendingApprovalState()
# print('KKKKKK', current_state.__class__.__name__)
current_state = workflow.handle_event(current_state, EventSubmitForApproval())
# print('KKKKKK', current_state.__class__.__name__)
current_state = workflow.handle_event(current_state, EventApprove())
# print("KKKKKK", current_state.__class__.__name__)
current_state = workflow.handle_event(current_state, EventCancel())
# print("KKKKKK", current_state.__class__.__name__)
current_state = workflow.handle_event(current_state, EventApprove())
# print("KKKKKK", current_state.__class__.__name__)