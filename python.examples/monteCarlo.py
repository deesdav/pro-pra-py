"""
import random
 
count =  20000000
inn = 0
for i in range(count):
    x = random.uniform(-0.5,0.5)
    y = random.uniform(-0.5,0.5)
 
    if x*x + y*y < 0.25:
        inn= inn+1
P = (inn/count)
result = P*4
print(result)
"""
import random

TOTAL_COUNT = 2_000_000
TOTAL_IN = 0
def generate_random_position():
    return(random.random( )-0.5 , random.random() -0.5)

for i in range(TOTAL_COUNT):
    x, y = generate_random_position()
    if x ** 2 +  y ** 2 < 0.25:
        TOTAL_IN = TOTAL_IN+1

P = TOTAL_IN/TOTAL_COUNT
print(P*4)
