"""T95 - DOES ANYTHING SELECT FOUR DIMENSIONS?
Every structural result in this campaign has been dimension-general: Result 1's
uniform-weight theorem, Result 16's master identity, the complex arena, the Regge
action.  A theory of everything has to say something about WHY four, so: is there
anything in the framework that singles it out?

There is a candidate, and it fell out of building the Regge machinery.  Curvature
in a d-complex lives on HINGES -- codimension-2 cells, degree d-2 (Result 31).
The Hodge star maps degree k to degree d-k, so the SELF-DUAL degree is d/2.
Those coincide when

        d - 2  =  d / 2      <==>      d = 4

**Only in four dimensions does curvature live on the self-dual middle degree.**
If that is more than arithmetic, it should have consequences the framework can
feel.  Checked here:
 (C1) the arithmetic itself, across dimensions;
 (C2) does the Hodge star map hinges to hinges?  (only if d=4)
 (C3) the flavour count 2^(d/2) is an integer only for even d, and the fibre
      1,4,6,4,1 is symmetric only because of the same duality;
 (C4) in d=4 the hinge degree is 2, so the curvature two-form and the gauge
      field strength of Result 40 live on THE SAME CELLS -- gravity and gauge
      curvature share a home only in four dimensions."""
import numpy as np, itertools
from math import comb
print("T95 (C1)  hinge degree vs self-dual degree")
print(f"   {'d':>3} {'hinge deg (d-2)':>16} {'self-dual deg (d/2)':>21} {'coincide?':>11} "
      f"{'flavours 2^(d/2)':>18}")
for d in range(2,9):
    hd=d-2; sd=d/2
    fl=2**(d/2) if d%2==0 else None
    print(f"   {d:3d} {hd:16d} {sd:21.1f} {str(abs(hd-sd)<1e-12):>11} "
          f"{(str(int(fl)) if fl else 'not integer'):>18}")
print()
print("T95 (C2)  does the Hodge star map hinges to hinges?")
for d in range(2,9):
    hd=d-2
    print(f"   d={d}: star maps degree {hd} -> degree {d-hd} = {d-hd}"
          f"   {'HINGES TO HINGES' if d-hd==hd else ''}")
print()
print("T95 (C3)  the fibre C(d,k), and where the hinge sits in it")
for d in (2,3,4,5,6):
    row=[comb(d,k) for k in range(d+1)]
    hd=d-2
    print(f"   d={d}: fibre {row} (total {2**d}); hinge degree {hd} has {comb(d,hd)} cells per site"
          f"{'  <-- the LARGEST block' if comb(d,hd)==max(row) else ''}")
print()
print("T95 (C4)  in d=4 gravity and gauge curvature share the same cells")
d=4
print(f"   Regge curvature lives on hinges: degree {d-2} cells (Result 31)")
print(f"   U(1) field strength F = dA lives on plaquettes: degree 2 cells (Result 40)")
print(f"   equal in d=4: {d-2==2}")
for dd in (3,5,6):
    print(f"   in d={dd}: hinges are degree {dd-2}, plaquettes degree 2 -> "
          f"{'same' if dd-2==2 else 'DIFFERENT cells'}")
print()
print("   So four dimensions is the unique case where (i) curvature sits on the")
print("   self-dual middle degree, (ii) the Hodge star maps hinges to hinges, and")
print("   (iii) gravitational and gauge curvature live on the same cells.")
print("   That is arithmetic, not yet a selection principle -- nothing here says the")
print("   framework CANNOT be built in other dimensions.  What it says is that d=4")
print("   is the only dimension in which its two curvatures are the same kind of")
print("   object, which is the sort of coincidence a selection principle would need.")
