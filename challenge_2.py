# Challenge 2
# Given a timestamp in 12-hour AM/PM format, convert it into 24-hour time in UTC with UTC date time
# format.

# Simple function to convert a 12-hour timestamp to 24-hour UTC timestamp using string manipulation
# In a real case, may be solved more easily using the datetime module
def to_utc(timestamp):
    """
    Converts a timestamp to UTC format.

    Args:
        timestamp (str): The timestamp to be converted.

    Returns:
        str: The converted timestamp in UTC format.
    """

    date, time = timestamp.split(' ')
    day, month, year = date.split('/')
    hour, minute = time[:-2].split(':')
    meridiem = time[-2:]

    # NOTE: Reference for conversion taken from https://en.wikipedia.org/wiki/12-hour_clock
    if meridiem == 'AM' and hour == '12':
        hour = '0'

    if meridiem == 'PM' and hour != '12':
        hour = str(int(hour) + 12)

    return f'{year}-{month}-{day}T{hour.zfill(2)}:{minute}:00Z'

assert to_utc('05/05/2024 8:30AM') == '2024-05-05T08:30:00Z'
assert to_utc('20/07/1969 8:17PM') == '1969-07-20T20:17:00Z'
assert to_utc('01/01/2000 12:01AM') == '2000-01-01T00:01:00Z'
assert to_utc('14/04/1961 11:11PM') == '1961-04-14T23:11:00Z'

print('All tests passed')