class Solution:

    def can_solve(self, M, D, mid):
        remove = 0; _next = 0; now = 0; N = len(D)
        while _next < N - 1:
            _next += 1
            if D[_next] - D[now] < mid: remove += 1
            else: now = _next
        if remove > M: return False
        else: return True

    def binary_search(self, L, M, N, D):
        l = 0
        r = L
        ans = mid = 0
        while l <= r:
            mid = (l + r) // 2
            if self.can_solve(M, D, mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans

RUN_TEST = False
input_data = '''25 5 2
                2
                11
                14
                17
                21'''

def main(input_data):
    input_data_list = list(map(int, input_data.split()))    #
    L = input_data_list[0]                                  #
    N = input_data_list[1]                                  #
    M = input_data_list[2]                                  #
    D = input_data_list[3:]                                 #
    sol = Solution()                                        #

    D.insert(0, 0)
    D.append(L)
    ans = sol.binary_search(L, M, N, D)

    if not RUN_TEST: print(ans)                             #
    return ans                                              #

# Do not Change The following code
if __name__ == "__main__":
    from time import time
    from math import floor
    if not RUN_TEST: main(input_data)
    else:
        earning = 0
        testcases = 10
        for i in range(1, 1 + testcases):
            start = time()
            _in = open('./test_data/stone/stone%d.in' % i, 'r')
            key = open('./test_data/stone/stone%d.ans' % i, 'r')
            input_data = _in.read()
            ans = main(input_data)
            end = time()
            delta = floor((end - start) * 1000)
            if delta > 1000: print('Time Exceeded Limit.')
            elif ans - int(key.read()) == 0: 
                print('Test Point %d Accepted in %d ms.' % (i, delta))
                earning += 1
            else: print('Test Point %d Wrong Answer.' % i)
            _in.close(); key.close()
        print('Point (%d/%d)' % (earning, testcases))
