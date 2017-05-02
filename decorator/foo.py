#
import decorator

def inc(bar):
    return bar + 1

def call_foo_with_arg(functor, arg):
    return functor(arg)


@decorator.decorate
def print_func():
    """
    :return: 
    """
    print("<print_func> ENTERING...")

    def nested_func_first():
        return '[nested_func_first] TRACE'

    def nested_func_second():
        return '[nested_func_second] TRACE'

    print(nested_func_first());
    print(nested_func_second());

    a = 0
    if a:
        b = True
    else:
        c = False

    print('<print_func> EXITING...b=={}'.format(b))

if __name__ == "__main__":
    print('inc(2)==3 -> {}'.format(inc(2) == 3))
    print('inc=', inc)
    print('inc(2)=', inc(2))
    print('type(inc)=', type(inc))

    print('call_foo_with_arg(inc, x)=', call_foo_with_arg(inc, 3))

    print_func()

    print('-------------------------------')
