def compact(iter_object):
    for index, item in enumerate(iter_object):
        if not index:
            last_value = item
            yield last_value

        if item == last_value:
            continue

        last_value = item
        yield item
