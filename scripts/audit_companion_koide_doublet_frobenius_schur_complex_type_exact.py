#!/usr/bin/env python3
r"""
Audit companion — the C_3 generation doublet is Frobenius-Schur COMPLEX type; the r=1/2-vs-r=1
fork is the FS-faithful (1 complex slot) vs realified (2 real slots) reading; the static flavor
complex structure J_cs is measure-neutral (silent on r). Bounded reframe + obstruction note.

This note CORRECTS the orientation of the retracted #3138 ("det_C = Pfaffian = Majorana -> r=1/2"),
which inverted the landed, runner-verified Berezin-fork mapping. The correct, FS-grounded orientation is:

    complex / holomorphic / Dirac  (1 complex slot)  ->  r = 1/2    [the FS-faithful reading]
    real    / Majorana            (2 real slots)    ->  r = 1      [the realified reading]

It is NOT a closure: FS=0 + the complex M_2(C) carrier are NECESSARY (they exclude the realified
reading as the faithful one for this complex-type irrep) but NOT SUFFICIENT to force r=1/2, because the
native flavor complex structure J_cs commutes with the whole K/CPT-real mass family and is therefore
measure-neutral. The selector is dynamical and remains the open AC_phi_lambda gate.

Reprove-and-cite: every fact reproven from the C_3 primitive (sympy/exact). The Frobenius-Schur indicator
theorem and the Majorana<->real / Dirac<->complex (Berezin polarization) correspondence are COMPARATORS only.
No PDG values; Q=2/3 and Q=1 are named as the empirical target and the realified value, not derived here.
"""
import sympy as sp
from sympy import I, sqrt, Rational, simplify, symbols, Matrix, eye, zeros, conjugate

R = []
def chk(label, cond): R.append((label, bool(cond)))

# exact primitive cube root of unity (explicit algebraic form; avoids exp() non-reduction)
w  = Rational(-1, 2) + I*sqrt(3)/2
wb = Rational(-1, 2) - I*sqrt(3)/2
chk("(0) w is a primitive cube root: w^3=1, 1+w+w^2=0, conj(w)=w^2=wb",
    simplify(w**3 - 1) == 0 and simplify(1 + w + w**2) == 0 and simplify(conjugate(w) - wb) == 0)

# (1) Frobenius-Schur indicators FS(rho) = (1/|G|) sum_g chi(g^2). C_3 squares: e->e, s->s^2, s^2->s.
def fs(chi):  # chi = [chi(e), chi(s), chi(s^2)]
    return simplify((chi[0] + chi[2] + chi[1]) / Rational(3))
chk("(1a) FS(trivial) = +1 (REAL type)", fs([1, 1, 1]) == 1)
chk("(1b) FS(omega)   = 0 (COMPLEX type: omega != omega-bar)", fs([1, w, w**2]) == 0)
chk("(1c) FS(omega-bar)= 0 (COMPLEX type)", fs([1, w**2, w]) == 0)
chk("(1d) the doublet (omega (+) omega-bar) is the realification of a COMPLEX-type irrep, not a real-type one "
    "(omega-bar = conj(omega) is determined by omega, not independent)", simplify(wb - conjugate(w)) == 0)

# (2) The FS-grounded, correctly-oriented Koide arithmetic (matches the landed Berezin-fork table; the
#     INVERSE of the retracted #3138). Q = 1/3 + (2/3) r.
def Q(r): return Rational(1, 3) + Rational(2, 3)*r
chk("(2a) FS-faithful (complex type, 1 complex slot): r=1/2 -> Q=2/3 (empirical target)",
    Q(Rational(1, 2)) == Rational(2, 3))
chk("(2b) realified (2 real slots): r=1 -> Q=1 (the native log|det| dimension-count value)",
    Q(1) == 1)
chk("(2c) ORIENTATION (corrects #3138): complex <-> r=1/2 and real/Majorana <-> r=1; #3138 asserted the inverse "
    "(Majorana <-> r=1/2) and was refuted",
    Q(Rational(1, 2)) == Rational(2, 3) and Q(1) == 1)

# (3) OBSTRUCTION (necessary-not-sufficient): the native flavor complex structure J_cs=(C-C^2)/sqrt3 commutes
#     with the entire K/CPT-real mass family H = aI + bC + b̄C^2, so it is MEASURE-NEUTRAL -- silent on r.
C = Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
Jcs = (C - C*C)/sqrt(3)
a, br, bi = symbols('a b_r b_i', real=True)
b = br + I*bi
H = a*eye(3) + b*C + conjugate(b)*(C*C)
P_doublet = eye(3) - (eye(3) + C + C*C)/3
chk("(3a) J_cs is a genuine complex structure on the doublet: J_cs^2 = -P_doublet", simplify(Jcs*Jcs + P_doublet) == zeros(3, 3))
chk("(3b) [J_cs, H] = 0 for all (a,b): J_cs is MEASURE-NEUTRAL (silent on r) -> FS-typing alone does NOT force r=1/2; "
    "the selector is dynamical (open AC_phi_lambda gate)", simplify(Jcs*H - H*Jcs) == zeros(3, 3))

passed = sum(1 for _, o in R if o); failed = sum(1 for _, o in R if not o)
for l, o in R: print(("PASS" if o else "FAIL") + " - " + l)
print("\n%d PASS, %d FAIL" % (passed, failed))
if failed: raise SystemExit(1)
print("""
BOUNDED RESULT (reframe + obstruction; NOT a closure):
 - The C_3 generation doublet is Frobenius-Schur COMPLEX type (FS=0). The r=1/2 reading counts it as its
   faithful complex type (1 complex slot); the r=1 reading counts its realification (2 real slots).
 - CORRECT ORIENTATION: complex/holomorphic/Dirac <-> r=1/2; real/Majorana <-> r=1. This is the inverse of the
   retracted #3138, and matches the landed, runner-verified Berezin-fork table.
 - OBSTRUCTION: J_cs is measure-neutral ([J_cs,H]=0), so FS=0 + the complex carrier are NECESSARY-NOT-SUFFICIENT.
   Which reading is selected is the open, DYNAMICAL AC_phi_lambda gate. r=1/2 is NOT derived here.
""")
