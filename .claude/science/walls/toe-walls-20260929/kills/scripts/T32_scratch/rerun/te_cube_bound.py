"""T-E: how the repo's compact-cube all-coupling gap bound scales with volume.
Source formula (docs/GAUGE_WILSON_COMPACT_CUBE_ALL_COUPLING_GAP_BOUNDED_THEOREM_NOTE_2026-09-07.md:32,
proof sections 2-4): gap >= (16/a) (m0/M0)^2, m0/M0 >= (l/u) exp(-12 a v),
l = 2^-N_l, u = (3/2)^N_l  (per-link heat density in (1/2,3/2)), so l/u = 3^-N_l, and exp(-24 a v) = exp(-2 * 12 a v)
with 12 = 2 * (number of faces = 6) i.e. 2 a v per face.
Generalisation to a periodic L^3 spatial torus with the same technique (SUGGESTED, my scaling of the note's constants,
not a theorem): N_l = 3 L^3 links, N_f = 3 L^3 faces  =>  bound/(16/a) = 3^(-2 N_l) exp(-4 a v N_f).
Note the note's own line 131: "these deteriorate with volume".
"""
import math
def log10_bound(n_links, n_faces, av):
    return (-2*n_links*math.log(3) - 4*av*n_faces)/math.log(10)
print("cube of the note: N_l=12, N_f=6 :  log10(bound/(16/a)) at a v = 0  :", round(log10_bound(12,6,0.0),2), "  (3^-24 = %.3e)" % 3.0**-24)
print("torus L^3 (SUGGESTED scaling), a v = 0 and a v = 0.5")
for L in (2,3,4,6,8,12,16):
    nl=3*L**3; nf=3*L**3
    print("L=%2d  links=%6d  log10 bound = %10.1f  (a v=0)   %10.1f (a v=0.5)" % (L,nl,log10_bound(nl,nf,0.0),log10_bound(nl,nf,0.5)))
print("Compare: measured 0++ gap of the pure-glue beta=6 theory is ~0.8/a on every L>=8 (see analysis). The bound falls as 3^(-6 L^3).")
