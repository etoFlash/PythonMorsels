def deep_add(num_or_iter, start=None):
    result = start

    for item in num_or_iter:
        if isinstance(item, (list, tuple, set)):
            value = deep_add(item)
        else:
            value = item

        if result:
            result = result + value
        else:
            result = value

    return result or 0
