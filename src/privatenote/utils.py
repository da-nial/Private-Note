import uuid
from datetime import datetime, timedelta


def generate_unique_url():
    return str(uuid.uuid4())


def get_expiration_date(day):
    ini_time_for_now = datetime.now()
    future_date_after_n_days = ini_time_for_now + timedelta(days=day)
    return future_date_after_n_days
