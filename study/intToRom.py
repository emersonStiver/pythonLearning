class Solution(object):
    def reverseString(self, s):
        def helper(f, e, limit, s):
            while f <= limit:
                store = s[f]
                s[f], s[e] = s[e], store
                f += 1
                e -= 1
            return s

        f, e = 0, (len(s) - 1)

        if len(s) % 2 == 0:
            limit = (len(s) // 2) - 1
            return helper(f, e, limit, s)
        else:
            limit = (len(s) // 2)
            return helper(f, e, limit, s)

    def judgeCircle(self, moves):
        r = moves.count('R')
        l = moves.count('L')
        u = moves.count('U')
        d = moves.count('D')
        return True if r - l == 0 and u - d == 0 else False

    def thousandSeparator(self, n):
        if n <= 3:
            return n
        my_list = [x for x in str(n)]
        my_list.reverse()

        for x in range(3, len(my_list), 4):
            my_list.insert(x, '.')
        my_list.reverse()
        return ''.join(my_list)

    def thousandSeparator2(self, n):
        if n <= 3:
            return n
        my_list, flag = [], True
        while flag:
            my_list.append(str(n % 10))
            n = n // 10
            if n == 0:
                flag = False
        counter = 3

        while counter < len(my_list):
            my_list.insert(counter, '.')
            counter = counter + 4
            if counter > len(my_list):
                my_list.reverse()
                return ''.join(my_list)
        my_list.reverse()
        return ''.join(my_list)


sol = Solution()
print(sol.thousandSeparator2(0))

# print(sol.thousandSeparator(1234232249))
