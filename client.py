'''
Module for the client class.

Please complete the Client class below, according to the specifications
in the docstrings.
'''

from tool import Tool


class Client:
    '''
    Class representing a client of the shop.

    Public attributes:
        client_id: The client's ID
        max_credits: The maximum number of credits the client can use
        tools: A set of tools the client has borrowed

    Public methods:
        get_credit_balance: Returns the number of credits the client 
            has available to borrow tools
        borrow_tool: Adds a tool to the client's set of borrowed tools.
        return_tool: Removes a tool from the client's set of borrowed tools.
    '''
    def __init__(self, client_id: str, max_credits: int) -> None:
        # TODO: Implement this method.
        self.client_id = client_id
        self.max_credits = max_credits
        self.__balance = max_credits
        self.tools = set()

    def get_credit_balance(self) -> int:
        '''
        Returns the number of credits the client has available to borrow tools

        Parameters:
            None

        Returns:
            The number of credits the client has available to borrow tools
        '''
        return self.__balance

    def borrow_tool(self, tool: 'Tool') -> bool:
        '''
        Adds a tool to the client's set of borrowed tools.

        Parameters:
            tool: The tool to add

        Returns:
            True if the tool was successfully added, False otherwise
        '''
        # TODO: Implement this method.
        if not tool.is_available():
            return False
        if self.__balance < tool.credits_needed():
            return False
        self.__balance -= tool.credits_needed()
        tool.borrow_tool(self)
        self.tools.add(tool)
        return True

    def return_tool(self, tool: 'Tool') -> bool:
        '''
        Removes a tool from the client's set of borrowed tools.

        Parameters:
            tool: The tool to remove

        Returns:
            True if the tool was successfully removed, False otherwise
        '''
        if tool not in self.tools:
            return False
        self.__balance += tool.credits_needed()
        self.tools.remove(tool)
        tool.return_tool()
        return True
