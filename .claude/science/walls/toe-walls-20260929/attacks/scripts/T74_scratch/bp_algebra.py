"""Exact check of the BP bookkeeping: c_cell = b*d/2^d (rank-d Hamming-weight-one projector on C^(2^d),
unit response b), G_lat = 1/(4 c_cell) from the retained narrow theorem 4 G c = 1.
Claim: G_lat*b is invariant under b -> lambda*b; G_lat = 1 only on the curve b*d/2^d = 1/4."""
from fractions import Fraction as F
import itertools
def c_cell(d,b): return F(b)*F(d, 2**d)
def G(d,b): return 1/(4*c_cell(d,b))
print("d  b   c_cell   G_lat=1/(4c)   G*b")
for d in range(2,8):
    for b in (F(1),F(2),F(1,2)):
        print(d, b, c_cell(d,b), G(d,b), G(d,b)*b)
# where is G=1 exactly? b = 2^d/(4d)
for d in range(2,8):
    print("d=%d: G_lat=1 iff b = %s" % (d, F(2**d, 4*d)))
# invariance check
for d in range(2,8):
    for b in (F(1),F(3,7),F(5,2)):
        for lam in (F(2),F(1,3)):
            assert G(d,lam*b)*lam*b == G(d,b)*b
print("G*b invariant under b->lambda b: OK (exact rational arithmetic)")
# Baker/W3(3): irrelevant to this bookkeeping; not tested here.
