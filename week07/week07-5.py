##week07-5.py
class RecentCounter:

    def __init__(self): ##一開始物件的「建構子constructor」只呼叫一次
        ##使用Queue得資料結構，但Python有collections.deque
        ##Double End Queue 簡稱 deque() 在LeetCode 可直接用他
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] < t- 3000:
            self.queue.popleft()
        return len(self.queue)


## Your RecentCounter object will be instantiated and called as such:
## obj = RecentCounter()
## param_1 = obj.ping(t)

