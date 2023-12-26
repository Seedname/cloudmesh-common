import datetime as TIME
import humanize as HUMANIZE
from dateutil import parser
from zoneinfo import ZoneInfo
import tzlocal


class DateTime(object):
    """This class provides some simple date time functions so we can use all the
    same format. Here is a simple example

        start = DateTime.now()
        stop = DateTime.now() + DateTime.delta(1)

        print ("START", start)
        print ("STOP", stop)
        print("HUMANIZE STOP", DateTime.humanize(stop - start))
        print ("LOCAL", DateTime.local(start))
        print("UTC", DateTime.utc(start))
        print("NATURAL", DateTime.natural(start))
        print("WORDS", DateTime.words(start))
        print("TIMEZONE", DateTime.timezone)

    This will result in

        START 2019-08-03 21:34:14.019147
        STOP 2019-08-03 21:34:15.019150
        HUMANIZE STOP a second ago
        LOCAL 2019-08-03 17:34:14 EST
        UTC 2019-08-03 21:34:14.019147 UTC
        NATURAL 2019-08-03 21:34:14.019147 UTC
        WORDS Sat 6 Aug 2019, 21:34:14 UTC
        TIMEZONE EST

    """

    timezone = TIME.datetime.now().astimezone().tzinfo

    @staticmethod
    def now():
        return str(TIME.datetime.now())

    @staticmethod
    def utc_now():
        return str(TIME.datetime.now(datetime.UTC))
        
    @staticmethod
    def natural(time):
        if type(time) == TIME.datetime:
            time = str(time)
        return str(parser.parse(time)) + " UTC"

    @staticmethod
    def words(time):
        return TIME.datetime.strftime(time, "%a %w %b %Y, %H:%M:%S UTC")

    @staticmethod
    def datetime(time):
        if type(time) == TIME:
            return time
        else:
            return DateTime.humanize(time)

    @staticmethod
    def humanize(time):
        return HUMANIZE.naturaltime(time)

    @staticmethod
    def string(time):
        # deprecated use get
        if type(time) == str:
            d = parser.parse(time)
        else:
            d = time
        return d

    @staticmethod
    def get(str):
        return parser

    @staticmethod
    def delta(n):
        return str(TIME.timedelta(seconds=n))

    @staticmethod
    def utc(time):
        return str(time) + " UTC"

    @staticmethod
    def local(time):
        return DateTime.utc_to_local(time)

    @staticmethod
    def utc_to_local(time):
        if "." in str(time):
            TIME_FORMAT = "%Y-%m-%d %H:%M:%S.%f"
        else:
            TIME_FORMAT = "%Y-%m-%d %H:%M:%S"

        utc = TIME.datetime.strptime(str(time), TIME_FORMAT)
        local_dt = utc.replace(tzinfo=ZoneInfo("UTC")).astimezone(
            tzlocal.get_localzone()
        )
        return local_dt.strftime(TIME_FORMAT) + " " + str(DateTime.timezone)

    def datetime(str):
        d = parser.parse(str)

    @staticmethod
    def add(one, two):
        return DateTime.datetime(one) + DateTime.datetime(two)    
    
if __name__ == "__main__":
    start = DateTime.now()
    stop = DateTime.add(DateTime.now(), DateTime.delta(1))

    stop2 = DateTime.datetime(DateTime.now()), DateTime.datetime(DateTime.delta(2))

    print("START", start)
    print("STOP", stop, stop2)
    print("HUMANIZE STOP", DateTime.humanize(stop - start))
    print("LOCAL", DateTime.local(start))
    print("UTC", DateTime.utc(start))
    print("NATURAL", DateTime.natural(start))
    print("WORDS", DateTime.words(start))
    print("TIMEZONE", DateTime.timezone)

    # print("CONVERT", DateTime.local("2019-08-03 20:48:27.205442 UTC"))
    """
    START 2019-08-03 21:34:14.019147
    STOP 2019-08-03 21:34:15.019150
    HUMANIZE STOP a second ago
    LOCAL 2019-08-03 17:34:14 EST
    UTC 2019-08-03 21:34:14.019147 UTC
    NATURAL 2019-08-03 21:34:14.019147 UTC
    WORDS Sat 6 Aug 2019, 21:34:14 UTC
    TIMEZONE EST
    """
