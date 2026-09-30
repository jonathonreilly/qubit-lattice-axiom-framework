from cov_rect import counts
from covariant2d import NAMES
R=[NAMES.index(x) for x in "0,1,2adj,3,4".split(",")]
fib=[0,1]
for i in range(30): fib.append(fib[-1]+fib[-2])
ok=True
for H in range(2,9):
    for W in range(H,10):
        f,n=counts(H,W,R,0)
        pred=fib[H]+fib[W]-1
        print(H,W,"frozen",f,"reach",n,"F_H+F_W-1 =",pred,"match" if (f==pred==n) else "MISMATCH")
