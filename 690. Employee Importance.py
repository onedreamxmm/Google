'''
You are given a data structure of employee information, which includes the employee's unique id, their importance value and their direct subordinates' id.

For example, employee 1 is the leader of employee 2, and employee 2 is the leader of employee 3. They have importance value 15, 10 and 5, respectively. Then employee 1 has a data structure like [1, 15, [2]], and employee 2 has [2, 10, [3]], and employee 3 has [3, 5, []]. Note that although employee 3 is also a subordinate of employee 1, the relationship is not direct.

Now given the employee information of a company, and an employee id, you need to return the total importance value of this employee and all their subordinates.

Example 1:

Input: [[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
Output: 11
Explanation:
Employee 1 has importance value 5, and he has two direct subordinates: employee 2 and employee 3. They both have importance value 3. So the total importance value of employee 1 is 5 + 3 + 3 = 11.


Note:

One employee has at most one direct leader and may have several subordinates.
The maximum number of employees won't exceed 2000.

Time Complexity: O(N), where N is the number of employees. We might query each employee in dfs.

Space Complexity: O(N), the size of the implicit call stack when evaluating dfs.
'''

class Employee:
    def __init__(self, id, importance, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees, id):
        emp_dict = {e.id: e for e in employees}
        def dfs(id):
            if id not in emp_dict:
                print('employee ', id, ' not found')
                return 0
            emp = emp_dict[id]
            res = emp.importance + sum(dfs(s) for s in emp.subordinates)
            return res
        return dfs(id)

if __name__ == '__main__':
    e1 = Employee(1, 5, [2, 3])
    e2 = Employee(2, 3, [4, 6])
    e3 = Employee(3, 3, [])
    e4 = Employee(4, 1, [])
    e5 = Employee(5, 1, [])
    employees1 = [e1, e2, e3, e4, e5]
    employees2 = [e1, e2, e3]
    id1 = 1
    id2 = 4
    o = Solution()
    print(o.getImportance(employees1, id1))
    print(o.getImportance(employees2, id2))


