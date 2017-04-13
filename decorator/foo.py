#

def foo(bar):
    return bar + 1

def call_foo_with_arg(functor, arg):
    return functor(arg)

if __name__ == "__main__":
    print('foo(2)==3 -> {}'.format(foo(2) == 3))
    print('foo=', foo)
    print('foo(2)=', foo(2))
    print('type(foo)=', type(foo))

    print('call_foo_with_arg(foo, x)=', call_foo_with_arg(foo, 3))

