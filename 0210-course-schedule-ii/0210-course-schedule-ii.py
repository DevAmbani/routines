from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        0 -> Unvisited
        1 -> Visiting
        2 -> Checked
        """
        state = [0] * numCourses
        courseSchedule = defaultdict(list)
        visited = []

        for course, dependency in prerequisites:
            courseSchedule[course].append(dependency)

        def dfs(course):
            if state[course] == 2:
                return True
            if state[course] == 1:
                return False
            
            state[course] = 1

            for dependency in courseSchedule[course]:
                if dfs(dependency) is False:
                    return False
            
            visited.append(course)
            state[course] = 2
        
        for course in range(numCourses):
            if dfs(course) is False:
                return []
        
        return visited