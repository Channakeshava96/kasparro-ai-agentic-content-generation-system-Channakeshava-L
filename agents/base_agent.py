from abc import ABC, abstractmethod

class BaseAgent(ABC):
    """
    Base interface for all agents in the system.
    Enforces clear input/output and single responsibility.
    """

    @abstractmethod
    def run(self, input_data):
        """
        Execute agent logic.

        Args:
            input_data: structured input data

        Returns:
            structured output data
        """
        pass
