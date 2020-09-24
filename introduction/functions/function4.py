# => Any number of argument
def any_number_of_argument(*args):
    for x in args:
        print(x)


# => Any number of argument (naming arguments)
def named_argument(**kwargs):
    print(kwargs)
    for i, j in kwargs.items():
        print("Responsible of {} is {}".format(i, j))
    print("Responsible of template is {}".format(kwargs.get("rm")))


# => Any number of argument (mixing of named and unnamed arguments)
def mix_of_args_and_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)


any_number_of_argument("Ilker")
any_number_of_argument("Ilker", 2, True, 3.14, None)
named_argument(rm="Ilker", lrm="Burak", cms="Erhan")
mix_of_args_and_kwargs(1, 2, 3, 4, rm="Ilker", lrm="Burak", cms="Erhan")