class SolutionMissingError(Exception):
    def __init__(self):
        Exception.__init__(self, "You tried to call code that has not been completed!")

def TBC(ignoredArg=None):
    raise SolutionMissingError

TBC_above = TBC
