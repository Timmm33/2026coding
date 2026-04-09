##week07-6.py
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque(list(senate))
        banR, banD = 0, 0 ##目前被消滅的次數都是0
        R, D = senate.count('R'), senate.count('D')
        while queue: ##只要還有人在排隊，就繼續進行「互相bsn對方」的遊戲
            now = queue.popleft() ##左邊吐出個字母要消滅敵對陣營
            if now == 'R':
                if banR>0: ##已經紀錄要消滅1個人
                    banR -= 1 ##用掉1個消滅的名額
                    R -= 1 ##馬上少掉1個人
                else: ##你沒有被削滅 可以反過來消滅對方
                    banD += 1
                    queue.append(now) ##再到最右邊排隊
            else:
                if banD > 0:
                    banD -= 1
                    D -= 1
                else:
                    banR += 1
                    queue.append(now)
            if R == 0: return 'Dire'
            if D == 0: return 'Radiant'

        queue = deque(list(senate))
        counter = Counter(senate)
        R, D = counter['R'], counter['D']
