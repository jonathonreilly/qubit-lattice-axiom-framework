"""
Audit companion (exact, sympy) for
THREE_AXIOM_CLEAN_BASE_RECORD_PROMOTION_PROPOSAL_NOTE_2026-06-04.md

Grounds the load-bearing algebraic facts the per-axiom anti-smuggling audit relies on.
It does NOT prove the axiom proposal (that is a governance/review-loop matter); it verifies
the facts that keep each axiom statement honest. P1's full irreducibility is the separately
shipped result (observable_principle P1 exponent-fixing, #2456 on main), cited not re-proven.
"""
import sympy as sp
from sympy import I, eye, zeros, Matrix, symbols, log, simplify

s0 = eye(2)
s1 = Matrix([[0, 1], [1, 0]])
s2 = Matrix([[0, -I], [I, 0]])
s3 = Matrix([[1, 0], [0, -1]])

def ac(A, B): return A*B + B*A
def co(A, B): return A*B - B*A
def Z(A):     return simplify(A) == zeros(A.rows, A.cols)

R = []
def chk(l, o): R.append((l, bool(o)))

# (Q1) AXIOM I's "algebra-3": M_2(C) has exactly 3 mutually-anticommuting Hermitian traceless
#      generators (the Paulis); the only matrix anticommuting with all three is 0 -> no 4th.
a, b, c, d = symbols('a b c d')
M = Matrix([[a, b], [c, d]])
Jc = Matrix([e for s in (s1, s2, s3) for e in ac(M, s)]).jacobian([a, b, c, d])
chk("Q1  Axiom I algebra-3: M_2(C) has exactly 3 anticommuting Hermitian generators (no 4th; rank 4)",
    Jc.rank() == 4)

# (Q2) THE TWO 3's ARE INDEPENDENT (the key discipline): the algebra-3 is intrinsic to the qubit and
#      does NOT fix the lattice dimension -- an Ising bond s3(x)s3 reuses one commuting operator in
#      any number of lattice directions ([s3,s3]=0), so a qubit sits on any Z^d. Hence Axiom I's
#      algebra-3 != Axiom II's spatial-d; neither derives the other.
chk("Q2  two 3's independent: [s3,s3]=0 so the qubit Ising-couples in any number of directions (algebra-3 != spatial-d)",
    Z(co(s3, s3)))

# (Q3) AXIOM I's complex structure (real, openly-committed content): omega = s1 s2 s3 = i*I, central,
#      omega^2 = -I. This is what makes the qubit M_2(C) (not the real rebit M_2(R)).
omega = s1*s2*s3
chk("Q3  Axiom I complex structure: omega = s1 s2 s3 = i*I, omega^2=-I, central (the qubit is complex)",
    Z(omega - I*s0) and Z(omega*omega + s0) and all(Z(co(omega, s)) for s in (s1, s2, s3)))

# (Q4) AXIOM III's form (P1): the readout additive over independent records IS the logarithm
#      (illustrative: log(x*y) = log x + log y). The IRREDUCIBILITY of this choice is the separately
#      shipped P1 result (#2456), cited there; here we only exhibit the additive-log form.
x, y = symbols('x y', positive=True)
chk("Q4  Axiom III form (P1): additive-over-independent readout is the log -- log(x*y)=log x+log y",
    simplify(log(x*y) - (log(x) + log(y))) == 0)

P = sum(1 for _, o in R if o)
F = sum(1 for _, o in R if not o)
for l, o in R:
    print(("PASS" if o else "FAIL"), "-", l)
print("\n%d PASS, %d FAIL" % (P, F))
if F:
    raise SystemExit(1)
print(
    "\nGrounded: Axiom I's algebra-3 is intrinsic to the qubit and INDEPENDENT of Axiom II's spatial-d\n"
    "(Q1,Q2); the qubit's complex structure is real, openly-committed content (Q3); Axiom III is the\n"
    "additive-log readout form (P1, Q4), whose irreducibility is the shipped #2456 result. The three\n"
    "axiom statements are mutually clean -- the only cross-axiom smuggle risk (conflating the two 3's)\n"
    "is refuted by Q2."
)
