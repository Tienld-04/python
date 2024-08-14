import heapq
import queue
# stack -----------------------
st = []
st.append(1)
st.append(2)
st.append(3)
st.append(1)
st.append(9)
print(st)
print(st.pop())
print(len(st)) 
st.sort()
st.insert(1,4)
print(st.index(4))
print(st)

# heap - priority queue-------------
pq = []
# Thêm phần tử vào priority queue
heapq.heappush(pq, (2, 'task2'))
heapq.heappush(pq, (1, 'task1'))
heapq.heappush(pq, (3, 'task3'))

# Lấy phần tử có độ ưu tiên cao nhất
print(heapq.heappop(pq))  # Output: (1, 'task1')
print(pq)
print(heapq.heappop(pq))  # Output: (2, 'task2')
print(heapq.heappop(pq))  # Output: (3, 'task3')

# Tạo một priority queue mới-----------
pq = queue.PriorityQueue()
# Thêm phần tử vào priority queue
pq.put((2, 'task2'))
pq.put((1, 'task1'))
pq.put((3, 'task3'))

# Lấy phần tử có độ ưu tiên cao nhất
print(pq.get())  # Output: (1, 'task1')
print(pq.get())  # Output: (2, 'task2')
print(pq.get())  # Output: (3, 'task3')


from collections import deque

# Tạo một deque mới------------
d = deque()

# Thêm phần tử vào deque
d.append(1)
d.append(2)
d.append(3)
print(d)  # Output: deque([1, 2, 3])

# Thêm phần tử vào đầu deque
d.appendleft(0)
print(d)  # Output: deque([0, 1, 2, 3])

# Lấy phần tử từ deque
print(d.pop())  # Output: 3
print(d.popleft())  # Output: 0

# Thêm phần tử vào giữa deque
d.insert(2, 4)
print(d)  # Output: deque([1, 2, 4, 3])

# Xóa phần tử khỏi deque
d.remove(2)
print(d)  # Output: deque([1, 4, 3])

# Lấy chiều dài của deque
print(len(d))  # Output: 3

