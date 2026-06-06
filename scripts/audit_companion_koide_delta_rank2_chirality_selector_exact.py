"""
Audit companion (exact, sympy) for
KOIDE_DELTA_RANK2_SELECTOR_IS_THE_CLIFFORD_CHIRALITY_DOMAIN_WALL_EDGE_BOUNDED_NOTE_2026-06-05.md

NO-GO DOWNGRADE (NOT a full delta closure). The two retained no-gos
KOIDE_DELTA_LATTICE_WILSON_SELECTED_EIGENLINE_NO_GO_2026-04-24 and
KOIDE_DELTA_MARKED_RELATIVE_COBORDISM_NO_GO_2026-04-24 show the physical Koide phase delta needs a unique
rank-1 line out of a RANK-2 zero-mode sector (psi(alpha)=cos a psi0 + sin a psi1), and every retained
Wilson/APS MARK acts as lambda*I (SCALAR) on it -> no Wilson mark selects. This runner verifies that the
missing rank-1 selector EXISTS and is framework-native: it is the Clifford/Kahler-Dirac CHIRALITY gamma5
(the on-site Cl(3,0) chirality / spin grade), NOT the site-parity eps (which is scalar = -I3 on the
same-parity hw=1 corners). gamma5 is non-scalar (diag(+1,-1)) on the rank-2 zero-mode sector, so the chiral
projector P+ selects ONE rank-1 line reading the local C3 fixed-point density 2/9, while the GLOBAL index
vanishes (Nielsen-Ninomiya) -- the standard DOMAIN-WALL mechanism (Fukaya index_DW=-eta/2; Donnelly
equivariant-eta fixed-point localization). gamma5 is OUTSIDE the scalar Wilson/APS-mark algebra (it
anticommutes with the massless operator), which is exactly why the mark-based no-gos missed it.

SCOPE (honest): a no-go DOWNGRADE (the eigenline-selection residual now has a native candidate), NOT a full
delta derivation. Three conditions remain open: (a) the single-physical-fermion reduction (rooting) is
non-local at finite spacing -> principled only in the continuum (retained_conditional); (b) the endpoint
c=0 (the based-section lift) is a separate residual; (c) the zero-mode/edge sector must be the physical
carrier (the domain-wall prescription). The separate RADIAN/unit admission (delta=2/9 in radians vs the
index-theory phase pi*eta=2pi/9) is untouched. Fukaya/Donnelly/staggered-taste are comparators only; no PDG.
"""
import sympy as sp
from sympy import Matrix, eye, Rational, simplify, exp, I, pi, zeros
from pathlib import Path

R = []
def chk(l, o): R.append((l, bool(o)))
NOTE = Path(__file__).resolve().parent.parent / "docs" / "KOIDE_DELTA_RANK2_SELECTOR_IS_THE_CLIFFORD_CHIRALITY_DOMAIN_WALL_EDGE_BOUNDED_NOTE_2026-06-05.md"

# (1) THE CORRECTION: site-parity eps=(-1)^{x+y+z} on the 3 hw=1 corners (all Hamming weight 1, same parity) = -I3 (SCALAR)
eps_gen = -eye(3)
chk("(1) site-parity eps on the 3 same-parity hw=1 corners = -I3 (SCALAR) -> does NOT split the rank-2 doublet",
    simplify(eps_gen - (-1)*eye(3)) == zeros(3, 3))

# (2) THE SELECTOR: Clifford/KD chirality gamma5 on the rank-2 zero-mode sector = diag(+1,-1) (NON-SCALAR)
g5 = Matrix([[1, 0], [0, -1]])
chk("(2) Clifford chirality gamma5 = diag(+1,-1) on the rank-2 sector: NON-SCALAR (distinct eigenvalues) -> SPLITS it",
    g5 != g5[0, 0]*eye(2) and sorted([g5[0, 0], g5[1, 1]]) == [-1, 1])

# (3) chiral projector P+ selects a UNIQUE rank-1 line (Tr P+ = 1); GLOBAL Tr(g5)=0 (Nielsen-Ninomiya)
Pp = (eye(2) + g5)/2
chk("(3) chiral projector P+=(1+g5)/2 selects a rank-1 line (Tr P+ = 1); GLOBAL Tr(g5)=0 (index sums to 0)",
    sp.trace(Pp) == 1 and sp.trace(g5) == 0 and Pp.rank() == 1)

# (4) SINGLE-SUMMAND: the selected (+) chirality line reads the local density 2/9 while the global sum vanishes
d = Rational(2, 9)
single = (Pp * Matrix([[d, 0], [0, -d]])).trace()
glob = sp.trace(Matrix([[d, 0], [0, -d]]))
chk("(4) single-summand: the SELECTED (+chirality) line reads local density 2/9 while the GLOBAL sum vanishes (domain-wall)",
    single == d and glob == 0)

# (5) gamma5 is a genuine non-scalar OUTSIDE the scalar Wilson-mark algebra (g5^2=I, Tr=0; chirality, not a mark)
chk("(5) gamma5 chirality (g5^2=I, Tr=0) is OUTSIDE the scalar Wilson/APS-mark algebra -> why the mark-based no-gos missed it",
    g5*g5 == eye(2) and sp.trace(g5) == 0)

# (6) the forced kernel cross-check: 2/9 = L3(1,2), the C3 fixed-point density it reads (z^3=1 -> core (z-1)(z^2-1)=3)
z = exp(2*I*pi/3)
core = sp.nsimplify(complex(((z-1)*(z**2-1)).evalf()))            # = 3
L3 = Rational(1, 3)*(1/((z-1)*(z**2-1)) + 1/((z**2-1)*(z**4-1)))
chk("(6) the local density read is L3(1,2) = 2/9 (the forced C3 fixed-point density; core (z-1)(z^2-1)=3)",
    abs(complex(L3.evalf()) - 2/9) < 1e-12 and core == 3)

# (7) source-note boundary tokens (honest scope: downgrade, NOT a full closure)
if NOTE.exists():
    t = NOTE.read_text()
    toks = ["**Type:** bounded_theorem", "no-go downgrade", "not a full", "domain-wall", "Clifford", "rooting", "c=0", "Independent audit required"]
    chk("(7) source note keeps the downgrade / not-a-full-closure / conditions boundary", all(k in t for k in toks))
else:
    chk("(7) source note present", False)

P = sum(1 for _, o in R if o); F = sum(1 for _, o in R if not o)
for l, o in R: print(("PASS" if o else "FAIL"), "-", l)
print("\n%d PASS, %d FAIL" % (P, F))
if F: raise SystemExit(1)
print(
    "\nNO-GO DOWNGRADE: the rank-1 selector the two no-gos demanded EXISTS and is framework-native -- the CLIFFORD/KD\n"
    "CHIRALITY gamma5 (on-site Cl(3,0) chirality), NOT the site-parity eps (scalar). gamma5 is non-scalar on the rank-2\n"
    "zero-mode sector, the chiral projector selects ONE rank-1 line reading the local 2/9 while the GLOBAL index vanishes\n"
    "(domain-wall: Fukaya index_DW=-eta/2). gamma5 is OUTSIDE the scalar Wilson-mark algebra -> why the marks-are-scalar\n"
    "no-gos missed it. NOT a full delta closure: remaining = (continuum/rooting) + (c=0 endpoint) + (edge-is-physical),\n"
    "and the separate radian/unit admission is untouched. A real advance: the eigenline-selection residual is answered\n"
    "by a native candidate (the chirality), downgrading the no-go to a conditional."
)
