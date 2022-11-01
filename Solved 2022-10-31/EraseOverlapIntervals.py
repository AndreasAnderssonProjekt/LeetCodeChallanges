"""
Given an array of intervals intervals where intervals[i] = [starti, endi], 
return the minimum number of intervals you need to remove to make the rest
of the intervals non-overlapping.
"""

def eraseOverlapIntervals(intervals):
    intervals.sort(key = lambda x: x[1]) # Sort by earliest finish time.
    opt = []
    current_start = intervals[0][0]
    current_end = intervals[0][1]
    opt.append([current_start, current_end])

    for i in range(len(intervals)):
        if current_end <= intervals[i][0]:
            opt.append(intervals[i])
            current_start = intervals[i][0]
            current_end = intervals[i][1]

    return len(intervals) - len(opt)
