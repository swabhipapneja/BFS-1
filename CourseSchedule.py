# Time Complexity : O(v + e), v is the number of courses and e is number of elements in given prereq list
# Space Complexity : O(v + e), because we are using an indegrees array that has length = v (numCourses) and a map that stores all edges
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : NA 

from collections import deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if numCourses == 0:
            return True

        # we need to find a sequence in which we can attempt all these courses - Topological Sort
        # we need to start with a course that is not dependent on any other course
        # it means a course that does not occur at index 0 of any list in prereq

        # given prereq are the edges
        # numCourses are the vertices

        # to store number of courses dependent on a course (at that index)
        indegrees = [0] * numCourses 
        # hashmap to store what courses are dependent on what course
        map = {}
        # queue for bfs
        q = deque()
        # to keep count of courses going in q
        count = 0
        # traverse all the lists in prereq
        # if a course has any dependency (comes at index 0)
        # go to indegrees at that index, and increment dependency count by 1
        for prereq in prerequisites:
            to = prereq[0] # dependent
            fromm = prereq[1] # independent
            indegrees[to] += 1
            if fromm not in map:
                map[fromm] = [] # create new list at that key
            # add the courses dependent on 'from' to the value list 
            map[fromm].append(to)

        # now we look for the index, where the dependency count is 0
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)
                count += 1
        
        # take a queue, and add all courses that are currently accessible
        while q:
            # remove an element
            curr = q.popleft()
            # we go to those courses in indegree, and reduce dependency count by 1
            for course in map.get(curr, []):
                indegrees[course] -= 1
                # if the dependency count has reduced to 0
                # we add them to the queue now
                if indegrees[course] == 0:
                    q.append(course)
                    count += 1
                
        # because if all courses went in queue, it means schedule is possible
        if count == numCourses:
            return True
        else:
            return False

        # OR (but this O(n) operation)      
        # at last if all elements in indegrees have become 0
        # then we know that this schedule is possible
        # for i in range(numCourses):
        #     if indegrees[i] != 0:
        #         return False
        
        # return True

