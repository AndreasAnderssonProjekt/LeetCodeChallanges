"""
Given an array of intervals where intervals[i] = [start_i, end_i], 
merge all overlapping intervals, and return an array of the non-overlapping intervals that 
cover all the intervals in the input.
"""
def mergeIntervals(intervals):
    intervals.sort(key = lambda x : x[0])
    current_start = intervals[0][0]
    current_end = intervals[0][1]
    result = []
    for i in range(len(intervals)):
        # If overlapping, extend the current interval.
        if current_end >= intervals[i][0]:
            current_end = max(current_end, intervals[i][1])
            if i == len(intervals) - 1:
                result.append([current_start, current_end])

        else:
            result.append([current_start, current_end])
            current_start = intervals[i][0]
            current_end = intervals[i][1]
            if i == len(intervals) - 1:
                result.append([current_start, current_end])

    return result
