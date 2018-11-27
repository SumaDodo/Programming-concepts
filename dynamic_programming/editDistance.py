class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n = len(word1)
        m = len(word2)
        
        if n*m == 0:
            return n+m
        
        dp = [[0]*(m+1) for _ in range(n+1)]
        
        for i in range(n+1):
            dp[i][0] = i
            
        for j in range(m+1):
            dp[0][j] = j
            
        for i in range(1, n+1):
            for j in range(1, m+1):
                go_left = dp[i-1][j] + 1
                go_down = dp[i][j-1] + 1
                go_left_down = dp[i-1][j-1]
                if word1[i-1] != word2[j-1]:
                    go_left_down +=1
                dp[i][j] = min(go_left,go_down,go_left_down)
                
        return dp[n][m]