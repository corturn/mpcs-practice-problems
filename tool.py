'''
Module representing a tool in the shop. Provides the Tool class.

Please write your solution in the client.py file.
'''

class Tool:
    '''
    Class representing a tool in the shop.
    
    Public attributes: 
        tool_id - a unique identifier for the tool
        type - the type of tool

    Public methods:
        credits_needed: returns the number of creditsNeeded to
        borrow the tool

        is_available: is the tool currently available to be 
        borrowed?

        borrow_tool: record a Client as borrowing the tool.

        return_tool: record that a Client returned the tool.
    '''
    def __init__(self, tool_id: str, credits: int, tool_type: str) -> None:
        '''
        Initialize a Tool object.

        Arguments:
            tool_id: a unique identifier for the tool
            credits: the number of credits needed to borrow the tool
            tool_type: the type of tool
        '''
        self.tool_id = tool_id
        self.__credits = credits
        self.__client = None
        self.type = tool_type

    def credits_needed(self) -> int:
        '''
        Return the number of credits needed to borrow the tool.

        Arguments:
            None
        
        Returns:
            The number of credits needed to borrow the tool.
        '''
        return self.__credits    
    
    def is_available(self) -> bool:
        '''
        Return True iff the tool is available to be borrowed.

        Arguments:
            None
        
        Returns:
            True iff the tool is available to be borrowed.
        '''
        return self.__client is None
    
    def borrow_tool(self, client) -> None:
        '''
        Record that a Client is borrowing the tool.

        Arguments:
            client: the Client borrowing the tool 

        Returns:
            None
        '''
        self.__client = client

    def return_tool(self) -> None:
        '''
        Record that a Client has returned the tool.

        Arguments:
            None

        Returns:
            None
        '''
        self.__client = None
