class Solution(object):
    def toggleLightBulbs(self, bulbs):
        """
        :type bulbs: List[int]
        :rtype: List[int]
        """
        result ={}
        for a in bulbs :
            result[a] = result.get(a,0) + 1
        
        for key in result:
                if result[key]%2 == 0 :
                    result[key] = 0

                else:
                    result[key] = 1 
        main = ([k for k , v in result.items() if v == 1])
        main.sort()
        return(main)