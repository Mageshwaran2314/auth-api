import datetime
import time


def n_days_to_int(date, days) -> int:

    get_datetime = datetime.datetime.fromtimestamp(date)
    datetime_n_days = get_datetime + datetime.timedelta(days=days)
    return int(datetime_n_days)


def password_expiry_90_Days(user):

    current_time_in_seconds = int(time.time())
    new_datetime = n_days_to_int(user['password_updated_at'], 90)
    return current_time_in_seconds > new_datetime


def block_account_3_attempts(user):
    current_time_in_seconds = int(time.time())
    new_datetime = n_days_to_int(user['accessed_failed_at'], 1)
    if (current_time_in_seconds < new_datetime and user['access_failed_count'] < 3 and not user['locked']):
        if (user['access_failed_count'] == 2):
            user['locked'] = True
        user['accessed_failed_at'] = current_time_in_seconds
        user['access_failed_count'] += 1
    return user


def block_account_6_attempts(user):
    if (user['access_failed_count'] >= 3 and not user['blocked']):
        if (user['access_failed_count'] == 5):
            user['blocked'] = True
        user['accessed_failed_at'] = int(time.time())
        user['access_failed_count'] += 1
    return user


def block_or_lock_account(user):
    if (user['access_failed_count'] < 3):
        user = block_account_3_attempts(user)
    else:
        user = block_account_6_attempts(user)
