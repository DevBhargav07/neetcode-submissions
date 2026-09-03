"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        i = 0
        while i < len(intervals) - 1:
            j = i + 1
            if intervals[i].end > intervals[j].start:
                return False
            else:
                i += 1
        return True