class Solution(object):
    def countTrapezoids(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        freq = Counter(pt[1] for pt in points)
        sum , c2 = 0 , 0
        for f in freq.values() :
            if f <= 1 : 
                continue
            c = f * (f - 1) / 2  # number of choices for each y coordinate
            sum += c  # sum of number of choices for each y coordinate
            c2 += c * c  # sum of squares of number of choices for each y coordinate
        # Answer is in form of AB + BC + AC where A, B, C are c-values for different y coordinates (sum of pairwise products of frequencies).
        # We can write it in the form ((A + B + C) ^ 2 - (A^2 + B^2 + C^2)) / 2.
        no = (sum * sum - c2) / 2
        return no % 1000000007
