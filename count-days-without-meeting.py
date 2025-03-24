class Solution:
    def approach1(self, days, meetings):
        meetings.append([0,0])
        meetings.append([days+1,days+1])
        meetings.sort()
        f = 0
        latest = 0
        for i in range(len(meetings)):
            if meetings[i][0] > latest:
                f += meetings[i][0]-latest-1
            latest = max(latest, meetings[i][1])
        return f
        

    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        return self.approach1(days, meetings)
        
