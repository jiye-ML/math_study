my_p = list(map(int, input().strip().split()))
my_q = list(map(int, input().strip().split()))

from collections import Counter
from math import log2

counter_p = Counter(my_p)
counter_q = Counter(my_q)

count_p = 0
count_q = 0
for item in counter_p.items():
    count_p += item[1]
    count_q += counter_q.get(item[0])

prob_p = {}
prob_q = {}
for item in counter_p.items():
    prob_p[item[0]] = item[1] / count_p
    prob_q[item[0]] = counter_q.get(item[0]) / count_q

for item in counter_p.items():
    prob_p[item[0]] = item[1] / float(count_p)
    prob_q[item[0]] = counter_q.get(item[0]) / float(count_q)

ans = 0
for item in counter_p.items():
    ans += prob_p[item[0]] * log2(prob_p[item[0]] / prob_q[item[0]])

print("{:.2f}".format(ans))