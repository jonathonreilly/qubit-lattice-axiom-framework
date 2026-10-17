import random, pickle
from orbits import *
random.seed(5)
for mode,fn in ((0,'fixed.txt'),(1,'sold.txt')):
    S=set(tuple((int(n)>>(4*r))&15 for r in range(7)) for n in open(D+fn))
    ok=lambda s: all(commute_all_translates(s,act(M,s,mode)) for M in G)
    found=random.sample(sorted(S),300)
    assert all(ok(s) for s in found)
    # random non-members, and near-members (one site changed)
    neg=0
    for _ in range(3000):
        s=tuple(random.randrange(16) for _ in range(7))
        if s in S or s==(0,)*7: continue
        assert not ok(s); neg+=1
    for s in random.sample(sorted(S),300):
        s2=list(s); r=random.randrange(7); s2[r]=random.randrange(16); s2=tuple(s2)
        if s2 not in S and s2!=(0,)*7: assert not ok(s2); neg+=1
    print(mode,'pos ok, neg ok',neg)
