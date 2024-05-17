class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def addTime(t1, t2):
        total_minutes = t1.hours * 60 + t1.minutes + t2.hours * 60 + t2.minutes
        return Time(total_minutes // 60, total_minutes % 60)

    def displayTime(self):
        print(f"{self.hours} hour(s) and {self.minutes} min")

    def displayMinute(self):
        total_minutes = self.hours * 60 + self.minutes
        print(f"{total_minutes} minutes")


time1 = Time(2, 50)
time2 = Time(1, 20)
added_time = Time.addTime(time1, time2)
added_time.displayTime()
added_time.displayMinute()
