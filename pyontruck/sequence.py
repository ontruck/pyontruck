def remove_duplicates(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]


def clean_nones(seq):
    return [x for x in seq if x is not None]
