class Solution(object):
    def numberOfWays(self, c):
        """
        :type corridor: str
        :rtype: int
        """
        x = 0
        id = []
        for i in range (len(c)) :
            if c[i] == 'S' :
                id.append(i)
                x += 1
        if x == 0 or x % 2 == 1 :
            return 0
        x = 1
        for i in range (1 , len(id) , 2) :
            if i < len(id) - 2 :
                x *= (id[i + 1] - id[i])
        return x % 1000000007
