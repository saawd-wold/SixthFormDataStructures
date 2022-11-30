from . import ADT

AbstractStack = ADT.AbstractStack

from . import stacks

S = None
error = False
try:
    S = stacks.Stack(100)
except TypeError as e:
    error = True
    print("Warning: Encountered error when attempting to instantiate Stack class from Stacks.stack")
    warnmsg = """
This is most likely because the implementation of the Stack class in Stacks/stacks.py does not yet implement each of the four methods that are necessary for stacks:
* isFull
* push
* pop
* isEmpty

The abstract base class for stacks is danielsdatastructures.Stacks.AbstractStack.
You may extend this class (implementing the four methods above) yourself.
    """
    print(warnmsg)

if not error:
    test = lambda t : Exception(t[1]) if not t[0] else None
    def initialemptiness(s):
        if s.isEmpty():
            return True, "Success"
        else:
            return False, "Failed test: Newly created stack returned isEmpty == False."
    def initialfullness(s):
        if not s.isFull():
            return True, "Success"
        else:
            return False, "Failed test: Newly created stack returned isFull == True."
    def proceduralfullness(s):
        for i in range(100):
            if not s.isFull():
                s.push(i)
            else:
                return False, f"Failed test: stack became full after {i} pushes despite being initialised with maxsize=100"
        if s.isFull():
            return True, "Success"
        else:
            return False, "Failed test: stack was not full after maxsize=100 pushes."
    def fifo(s):
        n = 99
        if s.pop() == n:
            return True, "Success"
        else:
            return False, "Failed test: stack did not pop from top (first pop did not return last element added :/)."
    def proceduralemptiness(s):
        for i in range(99):
            if s.isEmpty():
                return False, f"Failed test: stack was empty after only {i+1} pops and 100 pushes."
            else:
                s.pop()
        if s.isEmpty():
            return True, "Success"
        else:
            return False, "Failed test: stack was still not empty after 100 pops following 100 pushes."

    try:
        print("Testing Stack invariants.")
        test ( initialemptiness(S) )
        test ( initialfullness(S) )
        test ( proceduralfullness(S) )
        test ( fifo(S) )
        test ( proceduralemptiness(S) )
        print("All tests succeeded. Enjoy your stacks!")
    except Exception as e:
        print(e)
        print("You can use the stack implementation as provided but we make no guarantees that it'll behave!")
