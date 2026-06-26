from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        UNVISITED (0) → never been here
        VISITING  (1) → currently in our DFS path (on the call stack)
        VISITED   (2) → fully explored, confirmed no cycle below it
        """
        state = [0] * numCourses
        courseSelection = defaultdict(list)

        for course, depedency in prerequisites:
            courseSelection[course].append(depedency)

        def dfs(course):
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True

            state[course] = 1

            for depedency in courseSelection[course]:
                if dfs(depedency) is False:
                    return False
            
            state[course] = 2
            return True
        
        for course in range(numCourses):
            if dfs(course) is False:
                return False
        
        return True