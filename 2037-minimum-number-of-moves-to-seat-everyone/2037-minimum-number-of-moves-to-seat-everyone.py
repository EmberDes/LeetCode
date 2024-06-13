class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        ans = 0
        list.sort(seats)
        list.sort(students)
        for i in range(0,len(seats)):
            ans += abs(seats[i]-students[i])
        
        return ans
            
        