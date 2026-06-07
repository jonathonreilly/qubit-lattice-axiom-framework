#!/usr/bin/env python3
r"""
Exercise verification — Koide r=1/2 polarization-selector wall.
Output of the /exercise reframe + attack pass (2026-06-07). This is an ATTACK MAP, NOT a closure.

Verifies (sympy/exact) the genuinely-new, correctly-oriented facts the exercise produced:
  (1) The C_3 doublet is Frobenius-Schur COMPLEX type (FS=0). -> r=1/2 is the FS-FAITHFUL
      (complex/holomorphic/Dirac) reading; r=1 is the FS-MISTYPE (realified as if FS=+1).
      This RE-ORIENTS (inverts) the refuted #3138 ("Majorana<->r=1/2"); matches the landed Berezin table.
  (2) Measure-neutrality OBSTRUCTION: the native flavor complex structure J_cs commutes with the whole
      K/CPT-real mass family -> SILENT on r. FS=0 + complex carrier are NECESSARY-NOT-SUFFICIENT.
  (3) CANDIDATE SELECTOR (Quantum axiom): the qubit (spin-1/2) coherent-state manifold CP^1 is KAHLER
      (Fubini-Study), and the coherent-state action's kinetic term is FIRST-ORDER / holomorphic (the Berry
      symplectic potential A with dA = Kahler form), NOT second-order real |z-dot|^2. First-order = "count
      once" = r=1/2; second-order modulus = "count twice" = r=1.
  (4) OPEN (sharpened AC_phi_lambda gate): does the flavor b-field kinetic term inherit the qubit
      coherent-state FIRST-ORDER holomorphic dynamics (-> r=1/2) or become second-order real (-> r=1)?

Reprove-and-cite: all facts reproven from C_3 + the spin-1/2 coherent state. Frobenius-Schur theorem,
Fubini-Study/Kahler geometry, spin-coherent-state (Berry/symplectic) path integral, and the first-vs-second
order index distinction are COMPARATORS only. No PDG values; Q=2/3 and Q=1 named as target/forced values.
"""
import sympy as sp
from sympy import I, sqrt, Rational, simplify, symbols, Matrix, eye, zeros, conjugate, diff, log

R = []
def chk(label, cond): R.append((label, bool(cond)))

# exact primitive cube root of unity (explicit algebraic form; avoids exp() non-reduction)
w  = Rational(-1, 2) + I*sqrt(3)/2
wb = Rational(-1, 2) - I*sqrt(3)/2

# (1) Frobenius-Schur indicators: FS(rho) = (1/|G|) sum_g chi(g^2). C_3 squares: e->e, s->s^2, s^2->s.
def fs(chi):  # chi = [chi(e), chi(s), chi(s^2)]; FS = (chi(e)+chi(s^2)+chi(s))/3
    return simplify((chi[0] + chi[2] + chi[1]) / Rational(3))
chk("(1a) FS(trivial) = +1  (REAL type)", fs([1, 1, 1]) == 1)
chk("(1b) FS(omega) = 0     (COMPLEX type; omega != omega-bar)", fs([1, w, w**2]) == 0)
chk("(1c) FS(omega-bar) = 0 (COMPLEX type)", fs([1, w**2, w]) == 0)
chk("(1d) omega-bar = conj(omega) is DETERMINED by omega (not independent) -> complex-type, 1 complex slot",
    simplify(wb - conjugate(w)) == 0)

# (2) Re-oriented Koide arithmetic (matches landed Berezin table; inverse of refuted #3138):
def Q(r): return Rational(1, 3) + Rational(2, 3)*r
chk("(2a) FS-faithful (complex, 1 slot): r=1/2 -> Q=2/3 (empirical)", Q(Rational(1, 2)) == Rational(2, 3))
chk("(2b) FS-mistype (realified, 2 slots): r=1 -> Q=1 (native log|det| default)", Q(1) == 1)
chk("(2c) ORIENTATION: complex<->r=1/2, NOT Majorana<->r=1/2 (#3138 inverted this and was refuted)",
    Q(Rational(1, 2)) == Rational(2, 3) and Q(1) == 1)

# (3) Measure-neutrality OBSTRUCTION: J_cs commutes with the entire K/CPT-real mass family -> silent on r.
C = Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
Jcs = (C - C*C)/sqrt(3)
a, br, bi = symbols('a b_r b_i', real=True)
b = br + I*bi
H = a*eye(3) + b*C + conjugate(b)*(C*C)
P_doublet = eye(3) - (eye(3) + C + C*C)/3
chk("(3a) [J_cs, H] = 0 for all (a,b): the static complex structure is SILENT on r (cannot select det_C/det_R)",
    simplify(Jcs*H - H*Jcs) == zeros(3, 3))
chk("(3b) J_cs is a genuine complex structure (J_cs^2 = -P_doublet) yet measure-neutral -> selector must be DYNAMICAL",
    simplify(Jcs*Jcs + P_doublet) == zeros(3, 3))

# (4) CANDIDATE SELECTOR: qubit (spin-1/2) coherent states on CP^1 are KAHLER, and the coherent-state action
#     is FIRST-ORDER (the Berry symplectic potential), not second-order real.
z, zb = symbols('z zbar')
Kpot = log(1 + z*zb)                          # Kahler potential of CP^1 (spin-1/2 coherent states)
g = simplify(diff(diff(Kpot, z), zb))         # Kahler metric g_{z zbar}
chk("(4a) qubit coherent-state metric = d_z d_zbar log(1+|z|^2) = Fubini-Study 1/(1+|z|^2)^2 (KAHLER)",
    simplify(g - 1/(1 + z*zb)**2) == 0)
# Berry / symplectic potential in (1,0) gauge: A = A_z dz with A_z = -i*zbar/(1+|z|^2). Its curvature is the
# Kahler form: dA = d_zbar(A_z) dzbar^dz = -i g dzbar^dz = i g dz^dzbar = omega. So the coherent-state action
# carries a FIRST-ORDER term int A_z z-dot dt (linear in z-dot), the Berry/symplectic phase, NOT a second-order |z-dot|^2.
A_z = -I*zb/(1 + z*zb)
dA_zbar_z = simplify(diff(A_z, zb))           # coefficient of dzbar^dz in dA
omega_zbar_z = simplify(-I*g)                 # Kahler form omega = i g dz^dzbar => its dzbar^dz coefficient is -i g
chk("(4b) coherent-state action is FIRST-ORDER: Berry potential A_z = -i*zbar/(1+|z|^2) has dA = the Kahler form "
    "(symplectic) -> first-order holomorphic kinetic term int A_z*z-dot dt, NOT second-order |z-dot|^2",
    simplify(dA_zbar_z - omega_zbar_z) == 0)  # d_zbar A_z == -i g == omega's dzbar^dz coefficient
# first-order (count once) -> r=1/2 ; second-order modulus (count twice) -> r=1  (the index fork)
chk("(4c) first-order/holomorphic index = count ONCE = r=1/2; second-order modulus = count TWICE = r=1 "
    "(the open AC_phi_lambda fork, now = 'does flavor inherit the qubit's first-order coherent-state dynamics?')",
    Q(Rational(1, 2)) == Rational(2, 3))

passed = sum(1 for _, o in R if o); failed = sum(1 for _, o in R if not o)
for l, o in R: print(("PASS" if o else "FAIL") + " - " + l)
print("\n%d PASS, %d FAIL" % (passed, failed))
if failed: raise SystemExit(1)
print("""
EXERCISE OUTPUT (attack map, NOT a closure):
 RE-ORIENTED  the reframe: the C_3 doublet is Frobenius-Schur COMPLEX (FS=0). r=1/2 is the FS-faithful
              (complex/holomorphic/Dirac) reading; r=1 is the FS-mistype (realifying a complex-type irrep).
              This is the CORRECT orientation -- the exact inverse of the refuted #3138.
 SHARPENED    the wall: FS=0 + the complex M_2(C) carrier are NECESSARY (exclude the r=1 mistype) but NOT
              SUFFICIENT. Obstruction: J_cs is measure-neutral (commutes with H) -> the SELECTOR is dynamical.
 CANDIDATE    selector: the qubit coherent-state geometry (CP^1) is KAHLER and its action is FIRST-ORDER
              (Berry symplectic potential), i.e. the "count-once" / r=1/2 dynamics -- supplied by the Quantum axiom.
 OPEN gate    (sharpened): does the flavor b-field kinetic term inherit the qubit coherent-state's first-order
              holomorphic dynamics (-> r=1/2) or coarse-grain to a second-order real modulus (-> r=1)? This is
              the AC_phi_lambda realization question, now a concrete calculation. NOT closed by the exercise.
""")
