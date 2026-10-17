"""Structural facts behind dressing-independence (BKSF) vs dependence (c12)."""
from mpd_core import *
from bksf_core import BKSF
b = BKSF(4, range(6))
P = (0, 0, 0)
for v in b.sites():
    P = mul(P, b.B(v))
print("BKSF: product of all B_v is the identity operator:", P == (0, 0, 0))
# any single-qubit Pauli flips an even number of B's
ok = all(sum(anticommute(Q, b.B(v)) for v in b.sites()) % 2 == 0
         for q in range(b.n) for Q in [(1 << q, 0, 0), (1 << q, 1 << q, 1), (0, 1 << q, 0)])
print("BKSF: every single-qubit Pauli flips an even number of B's (so no local odd-charge operator):", ok)
lat = Lattice(4)
g = lat.gamma((0, 0, 0), 0)
nB = sum(anticommute(g, lat.to_pauli(lat.B_mono(v))) for v in lat.all_sites())
nS = sum(anticommute(g, lat.to_pauli(lat.plaq_mono(v, a, c))) for v in lat.all_sites() for (a, c) in ORIENTS)
print("c12: single local Majorana gamma_{0,+x} (a 1-qubit Pauli X1) flips %d B and %d plaquettes" % (nB, nS))
