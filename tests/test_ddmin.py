import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)+'/../'))

import ddmin as dd
def test_ddmin():
    def repro_func(lst_steps):
        """A Test function should return False if it reproduces
            In this case we're just looking for any combination of
            the letters e or f that is greater than 2
        """
        if ( (lst_steps.count('e') + lst_steps.count('f')) >= 2):
            return False
        else:
            return True

    # The circumstances is an iterable and separable list of steps or conditions
    circumstances = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

    debugger = dd.DDMin(circumstances, repro_func)
    assert debugger.execute() == ['e', 'f']
    # run it again, with an odd number of elements
    debugger = dd.DDMin(circumstances[:-1], repro_func)
    assert debugger.execute() == ['e', 'f']

