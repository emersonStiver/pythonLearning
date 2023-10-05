
class Solution(object):
    def lengthOfLastWord(self, s):
        arr = s.rsplit()
        return len(arr[-1]) if len(arr)>0 else 0

    def longestCommonPrefixRecursion2(self, strs):
        if len(strs) == 1:

            return
        mid = len(strs)//2
        left = self.lengthOfLastWord(strs[0:mid])
        right = self.longestCommonPrefix(strs[mid:])


    def longestCommonPrefix7(self, strs):
        if strs[0]=='' or len(strs)==0:
            return ''
        first = strs[0]
        result = ''
        for i in range(len(first)):
            for x in range(len(strs)):
                if not strs[x].startswith(first[i]):
                    return result
                strs[x] = strs[x][1:]
            result += first[i]
        return result
    """
    A: Absent
    L: Late
    P: present
    
    Elegibility:
    The student was absent ('A') for strictly fewer than 2 days total.
    The student was never late ('L') for 3 or more consecutive days.
                 
                 EXAMPLE: PPALLP
    """
    def checkRecord(self, s):
        counter, late, lower_case, my_dict = 0, False, s.lower(), {'a': 0, 'l':0, 'p':0}
        for x in lower_case:
            if x == 'l':
                counter +=1
                if counter ==3:
                    late = True
            else:
                counter = 0
            my_dict[x] = my_dict.get(x) + 1
        return True if late == False and my_dict['a']<2 else False

    def isIsomorphic(self, s,t):
        if len(s) != len(t):
            return False
        #From left to right
        myDict = {}
        for x in range(len(s)):
            if s[x] in myDict:
                if myDict[s[x]] != t[x]:
                    return False
            myDict[s[x]] = t[x]
        #From right to left
        size = len(s)-1
        myDict2 = {}
        while size >=0:
            if t[size] in myDict2:
                if myDict2[t[size]] != s[size]:
                    return False
            myDict2[t[size]] = s[size]
            size =size-1
        return True

    def isAnagram(self, s,t):
        if len(s)!=len(t):
            return False
        myDict, myDict2 = {}, {}
        for x in s:
            if x in myDict:
                myDict[x] = myDict[x] +1
            else:
                myDict[x] = 0
        for y in t:
            if y in myDict2:
                myDict2[y]= myDict2[y] +1
            else:
                myDict2[y] = 0
        return True if myDict == myDict2 else False

    def wordPattern(self, pattern, s):
        listWords = s.split()
        myDict ={}
        counter = 0
        for word in listWords:
            if word in myDict.values():
                if myDict[word] != pattern[counter]:#compare if the pattern in question is different to the pattern that is associeted with the word in questiom
                    return False
            if pattern[counter] in myDict:
                if myDict[pattern[counter]] != word:
                    return False
            else:
                myDict[pattern[counter]] = word
            counter +=1
        return True

a = 2
b = 4
print(a==4 and b>2)

#di ={'a':'dog'}
#print(di['dog'])
#sol = Solution()
#sol.wordPattern('abab', 'dog cat dog cat')


























