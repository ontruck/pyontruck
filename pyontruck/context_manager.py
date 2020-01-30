class MakeMutable:
    def __init__(self, unmutable):
        self.unmutable = unmutable

    def __enter__(self):
        self.unmutable._mutable = True

    def __exit__(self, *args, **kwargs):
        self.unmutable._mutable = False


def make_mutable(unmutable):
    return MakeMutable(unmutable)


class EditDict:
    def __init__(self, field, value, dictionary):
        self.field = field
        self.value = value
        self.dictionary = dictionary
        self.original_value = dictionary[self.field]

    def __enter__(self):
        self.dictionary[self.field] = self.value

    def __exit__(self, *args, **kwargs):
        self.dictionary[self.field] = self.original_value


def edit_dict(field, value, dictionary):
    return EditDict(field, value, dictionary)
