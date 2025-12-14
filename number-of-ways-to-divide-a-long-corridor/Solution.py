class Solution(object):
    def numberOfWays(self, c):
        """
        :type corridor: str
        :rtype: int
        """
        x = 0
        id = []
        m = []
        for i in range (len(c)) :
            if c[i] == 'S' :
                id.append(i)
                x += 1
        if x == 0 or x % 2 == 1 :
            return 0
        x = 1
        for i in range (1 , len(id) , 2) : # 2 spaces for taking (number of plants + 1) between every second seat and next seat
            a = id[i]
            if i < len(id) - 2 :
                b = id[i + 1]
                m.append(b - a) # could also directly multiply instead of using a list m as taken here
        for e in m :
            x *= e
        return x % 1000000007
