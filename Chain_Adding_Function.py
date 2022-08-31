# We want to create a function that will add numbers together when called in succession.
class add(int):
    def __call__(self, n):
        return add(self + n)
