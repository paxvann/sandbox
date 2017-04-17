

def decorate(functor):

    """

    :rtype: function
    """

    def wrapper():
        print("[decorator] Calling functor...")
        functor()
        print("... functor decorated!!")

    return wrapper

def hello_world():
    print("Hello, my name is world!")

"""
hello_world = decorate(hello_world)
hello_world()
"""

if __name__ == "__main__":
    decorate(hello_world)
