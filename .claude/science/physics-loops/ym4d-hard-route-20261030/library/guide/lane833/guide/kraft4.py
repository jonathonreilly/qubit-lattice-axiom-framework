# GUIDE: basic Kraft (Finner branching) at several beta; also degree-2-only class.
import math
from kraft3 import Ks, best
for b in [1/8, 1/7, 1/6, 0.17, 0.175, 0.18, 0.185]:
    s=math.sinh(b)/2;c=math.cosh(b);q=s*c**8
    R,arg=best(q,2*c**-6,5*c**-12,6)
    print(f"beta={b:.5f} s={s:.6f} c={c:.6f} q={q:.6f} R={R:.5f} R/q={R/q:.3f} P={arg[0]:.4f} y={arg[1]:.5f} Ks={[round(k,4) for k in Ks(arg[0],arg[1],2*c**-6,5*c**-12)]}")
print("degree-2 class 5q:")
for b in [0.2,2/9,0.25,0.27,0.28,7/25,0.285]:
    s=math.sinh(b)/2;c=math.cosh(b);q=s*c**8
    print(f"beta={b:.5f} 5q={5*q:.5f}")
