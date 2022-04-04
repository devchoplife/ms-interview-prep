"""
Description
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],…] (si < ei), find the minimum number of conference rooms required.

Sample I/O

Example 1
Input: [[0, 30],[5, 10],[15, 20]]
Output: 2

Example 2
Input: [[7,10],[2,4]]
Output: 1
"""
from typing import List


def minMeetingRooms(intervals) -> int:
    # type intervals List[List[int]]
    startTimes = [i[0] for i in intervals]
    endTimes = [i[1] for i in intervals]

    startTimes = sorted(startTimes)
    endTimes = sorted(endTimes)
    rooms = 0

    while len(startTimes) > 0:
        startTime = startTimes.pop(0)
        # now a meeting is going to start, is there a meeting ending/is a meeting room released
        endTime = endTimes[0]
        if endTime <= startTime:
            endTimes.pop(0)
        else:
            """need to ask for a new room"""
            rooms += 1

    return rooms


print(minMeetingRooms([[1, 3], [9, 18], [3, 7], [6, 12], [4, 9]]))
