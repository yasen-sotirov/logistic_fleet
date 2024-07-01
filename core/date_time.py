from datetime import datetime, timedelta


class DateTime:

    CURRENT_DATE_TIME = datetime.now().strftime('%d/%m/%Y %H:%M')

    @staticmethod
    def diff_between_dt(first_date, second_date):
        dt1 = datetime.strptime(first_date, "%d/%m/%Y %H:%M")
        dt2 = datetime.strptime(second_date, "%d/%m/%Y %H:%M")
        return (dt2 - dt1).total_seconds()
    

    @staticmethod
    def set_current_td(current_td):
        DateTime.CURRENT_DATE_TIME = current_td

    @staticmethod
    def add_days_to_now(days_to_add: int):
        dt1 = datetime.strptime(DateTime.CURRENT_DATE_TIME, "%d/%m/%Y %H:%M")
        result = dt1 + timedelta(days=days_to_add)

        DateTime.CURRENT_DATE_TIME = result.strftime("%d/%m/%Y %H:%M")


