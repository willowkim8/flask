def document_it(func):
    def new_function(*args):
        print('Running function:', func.__name__)
        print('Arguments:', args)
        result = func(*args)
        print('This is result:', result)
        return result
    return new_function

def give_me_soju(a):
    return 'I need {} more soju!!'.format(a)

give_me_soju(3)