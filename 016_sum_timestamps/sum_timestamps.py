from datetime import timedelta


def _extract_td(timestamp):
    if timestamp.count(":") < 2:
        timestamp = "0:" + timestamp

    ts = timestamp.split(":")

    return timedelta(hours=int(ts[0]),
                     minutes=int(ts[1]),
                     seconds=int(ts[2]))


def _get_hms(td):
    hours = td.seconds // 3600
    td -= timedelta(hours=hours)
    # ex. timedelta with days: datetime.timedelta(days=1, seconds=61386)
    hours += td.days * 24
    td -= timedelta(days=td.days)
    minutes = td.seconds // 60
    td -= timedelta(minutes=minutes)
    seconds = td.seconds

    return hours, minutes, seconds


def sum_timestamps(timestamps):
    td = timedelta()
    for timestamp in timestamps:
        td += _extract_td(timestamp)

    hours, minutes, seconds = _get_hms(td)

    result = (f"{hours}:" if hours > 0 else "") + f"{minutes:02}:{seconds:02}"
    # according to requirements: "05:55" -> "5:55"
    if result.startswith("0"):
        result = result[1:]

    return result
