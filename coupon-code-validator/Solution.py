class Solution(object):
    def validateCoupons(self, c, b, a):
        """
        :type code: List[str]
        :type businessLine: List[str]
        :type isActive: List[bool]
        :rtype: List[str]
        """
        cp = r'^[A-Za-z0-9_]{1,}$'
        e = []
        g = []
        p = []
        r = []
        for i in range (len(c)):
            if a[i] == False :
                continue
            match = re.match(cp, c[i])
            if match :
                if b[i] == "electronics" :
                    e.append(c[i])
                elif b[i] == "grocery" :
                    g.append(c[i])
                elif b[i] == "pharmacy" :
                    p.append(c[i])
                elif b[i] == "restaurant" :
                    r.append(c[i])
        e.sort()
        g.sort()
        p.sort()
        r.sort()
        return e + g + p + r
