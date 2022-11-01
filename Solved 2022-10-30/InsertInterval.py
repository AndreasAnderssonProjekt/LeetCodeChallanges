"""Intervals is an array of non-overlapping intervals, sorted in ascending order
by their start times. Insert newInterval if it is non-overlapping such that intervals
is still sorted in ascending order by their start times. Merge overlapping
intervals if necessary."""
def insertInterval(intervals, newInterval):
    left_intervals = []
    right_intervals = []
    start = newInterval[0]
    end = newInterval[1]

    for interval in intervals:
        if interval[1] < newInterval[0]:
            left_intervals.append(interval)

        if interval[0] > newInterval[1]:
            right_intervals.append(interval)

    if left_intervals + right_intervals != intervals:
        start = min(newInterval[0], intervals[len(left_intervals)][0])
        end = max(newInterval[1], intervals[-len(right_intervals) - 1][1])

    return left_intervals + [[start,end]] + right_intervals
