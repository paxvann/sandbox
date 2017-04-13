#
import decorator

def inc(bar):
    return bar + 1

def call_foo_with_arg(functor, arg):
    return functor(arg)


@decorator.decorate
def print_func():
    print("Printing from parent() function!")

    def first_child():
        print("Printing from first_child() function!")
    def second_child():
        print("Printing from second_child() function!")

    print(first_child());
    print(second_child());

if __name__ == "__main__":
    print('inc(2)==3 -> {}'.format(inc(2) == 3))
    print('inc=', inc)
    print('inc(2)=', inc(2))
    print('type(inc)=', type(inc))

    print('call_foo_with_arg(inc, x)=', call_foo_with_arg(inc, 3))

    print_func()
