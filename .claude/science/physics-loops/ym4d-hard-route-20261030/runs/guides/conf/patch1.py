import sys
p=sys.argv[1]
s=open(p).read()
reps=[
("""gluing two boxes along a face transverse to the flux raises the odd-flux
weight by at most a constant factor. With C = 1 it reads x(2n) >= x(n)^2,
or Tr Lambda^2(T_-^n) <= Tr Lambda^2(T_+^n) (second exterior powers).
""",
"""gluing two boxes along a face transverse to the flux raises the odd-flux
weight by at most a constant factor. With C = 1 it reads x(2n) >= x(n)^2.
In terms of the normalized second exterior powers
l_+ = Tr Lambda^2(T_+^n)/(Tr T_+^n)^2 and l_- (the same for T_-), the
doubling defects are delta = -log(1 - 2 l), so C = 1 is l_- <= l_+.
"""),
("""V4 (the named line where the attempt stops). (VEXT) holds if and only if the
twisted sheet operator has no extra low-lying weight relative to the
periodic one, in this exact sense:

  Tr Lambda^2(T_-^n) <= Tr Lambda^2(T_+^n) + (eps/2) F_v(n) (Tr T_-^n)^2.

In words: the twisted cross-section must have no mode that the periodic one
lacks.""",
"""V4 (the named line where the attempt stops). By V1, (VEXT) with
M = 2 + eps is exactly

  log[(1 - 2 l_+)/(1 - 2 l_-)] <= eps F_v(n),

and l_- <= l_+ suffices (M = 2). To first order in small l this is
l_- <= l_+ + (eps/2) F_v(n). In words: the twisted cross-section must have
no low-lying two-state weight that the periodic one lacks."""),
("""One more use, flagged. Item F3 needs (TM)""",
"""Flag. The identity Z^- = Tr(T^n Theta) is the standard one (the flip at one
time step is the sign change of beta on the stack of plaquettes). It was
not matched line by line to the lane's (TM-c).

One more use, flagged. Item F3 needs (TM)"""),
]
for a,b in reps:
    assert s.count(a)==1, a[:40]
    s=s.replace(a,b)
open(p,'w').write(s)
print("patched")
