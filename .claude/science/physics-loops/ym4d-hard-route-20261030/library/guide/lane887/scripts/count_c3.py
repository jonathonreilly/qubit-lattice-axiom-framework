# Arithmetic check of |Pi| in Lemma CH (counting only; GUIDE-level, proves nothing).
# Child index offsets inside a parent: 0..18 per coordinate. Same class = same parity in each coordinate.
# Witness pair: distinct, same class, offsets differ by at most 8 in each coordinate.
from itertools import product
def per_coord(par):
    vals=[u for u in range(19) if u%2==par]
    return sum(1 for a in vals for b in vals if abs(a-b)<=8), len(vals)
tot=0
for s in product((0,1),repeat=3):
    o=1; n=1
    for par in s:
        c,m=per_coord(par); o*=c; n*=m
    tot+=(o-n)//2
print("C_3 =",tot)
# all same-class pairs without the offset restriction
tot2=0
for s in product((0,1),repeat=3):
    n=1
    for par in s: n*= (10 if par==0 else 9)
    tot2+=n*(n-1)//2
print("all same-class pairs =",tot2)
# worst-case snake: 8 star-adjacent indices with distinct classes spanning 7
snake=[(0,0,0),(1,0,0),(2,1,0),(3,1,0),(4,1,1),(5,1,1),(6,2,1),(7,2,1)]
print("snake classes distinct:",len({tuple(c%2 for c in p) for p in snake})==8,
      "steps star-adjacent:",all(max(abs(a-b) for a,b in zip(p,q))==1 for p,q in zip(snake,snake[1:])))
print("1/C_3 =",1/tot, " 676^-8 =",676.0**-8, " (26e)^-8 =",(26*2.718281828459045)**-8)
