"""Finite-size remark: sector consistency and log2 dim on odd and even L."""
from mpd_core import *
for L in [2, 3, 4, 5, 6, 7, 8]:
    lat = Lattice(L); row = []
    for sec in all_sectors():
        T = Tableau(lat.n)
        for m in lat.generators(sec): T.insert(lat.to_pauli(m))
        lab = "".join("+" if sec[o] > 0 else "-" for o in ORIENTS)
        row.append("%s:%s" % (lab, (lat.n - T.rank()) if T.consistent else "-I"))
    print("L=%d " % L + "  ".join(row))
