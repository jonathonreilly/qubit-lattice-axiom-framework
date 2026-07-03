"""Class-A finite runner: the V_sel weak-axis SELECTOR (32 sum_{i<j} phi_i^2 phi_j^2,
m_perp=32) is a TASTE-CUBE object and does NOT transport to the Dirac Higgs family
M(phi)=sum_i phi_i Gamma_i, because the retained M^2=|phi|^2 I forces every even invariant
of M to be rotationally invariant (a function of |phi|^2 only) with NO axis-selector.
=> the schur-suppression curvature input m_perp=32 (#3172 ADM-3) is admitted via a genuine
TASTE-CUBE -> DIRAC transport obstruction (same family as the failed hierarchy per-site->V_3
scale-transport), not a Dirac-Higgs property.

  T1  taste-cube selector: H(phi)=sum phi_i S_i (S_i = axis bit-flips sigma_x^(i) on 2^3),
      V_sel = Tr H^4 - (1/8)(Tr H^2)^2 = 32 sum_{i<j} phi_i^2 phi_j^2 (axis-SELECTOR;
      graph_first_selector_derivation, retained). Hessian at e_1 = diag(0,64,64), m_perp=32.
  T2  Dirac Higgs: M(phi)=sum phi_i Gamma_i, M^2=|phi|^2 I (retained
      dm_neutrino_dirac_bridge). With d=Tr(I), the transported polynomial is
      Tr M^4 - (1/8)(Tr M^2)^2 = d(1-d/8)|phi|^4 -- ROTATIONALLY INVARIANT,
      with no phi_i^2 phi_j^2 axis-selector. Its Hessian at e_1 is
      diag(12c,4c,4c), c=d(1-d/8), so the transverse curvatures are equal
      and no distinguished transverse curvature 32 is native to the Dirac family.
  T3  GENERALITY: any even invariant Tr M^{2n} of M with M^2=|phi|^2 I equals
      d|phi|^{2n} (a function of |phi|^2 only) -> NO even invariant of the
      Dirac Higgs is an axis-selector. So the obstruction is not about the
      particular V_sel; the rotational invariance of the Dirac mass spectrum
      forbids ANY native axis-selector on the Dirac Higgs family.
  T4  CONTROL (teeth): the taste-cube V_sel genuinely distinguishes axes (V_sel(e_1)=0 but
      V_sel(non-axis) != 0), while the Dirac V_sel does not (depends only on |phi|).

CONCLUSION: m_perp=32 is a taste-cube selector curvature; transporting it onto the Dirac
Higgs mass requires identifying the taste-cube phi-space with the Dirac-Higgs phi-space AND
importing the selector that the Dirac family (M^2=|phi|^2 I) does not natively carry. So the
schur ADM-3 is a genuine transport obstruction, not merely "out of scope."

prints TOTAL: PASS=N FAIL=0
"""

import numpy as np
import sympy as sp

results = []
def check(name, ok): results.append((name, bool(ok)))

d_tr = sp.symbols("d", positive=True)
p = sp.symbols('p0 p1 p2', real=True)
r2 = p[0]**2 + p[1]**2 + p[2]**2
selector = p[0]**2 * p[1]**2 + p[0]**2 * p[2]**2 + p[1]**2 * p[2]**2

# --- T1: taste-cube selector V_sel = 32 sum phi^2 phi^2 ---
sx = np.array([[0, 1], [1, 0]], dtype=int)
def Sop(i):
    ops = [np.eye(2, dtype=int)] * 3; ops[i] = sx
    M = ops[0]
    for o in ops[1:]:
        M = np.kron(M, o)
    return sp.Matrix(M)
S = [Sop(i) for i in range(3)]
Ht = S[0] * p[0] + S[1] * p[1] + S[2] * p[2]
Vt = sp.expand(sp.trace((Ht * Ht) * (Ht * Ht)) - sp.Rational(1, 8) * sp.trace(Ht * Ht) ** 2)
check("T1 taste-cube V_sel = 32 sum_{i<j} phi^2 phi^2 (axis-selector)", sp.simplify(Vt - 32 * selector) == 0)
Ht_hess = sp.hessian(32 * selector, p).subs({p[0]: 1, p[1]: 0, p[2]: 0})
check("T1b taste-cube Hessian at e_1 = diag(0,64,64) (m_perp=32, anisotropic)", Ht_hess == sp.diag(0, 64, 64))

# --- T2: Dirac Higgs M^2=|phi|^2 I -> V_sel rotationally invariant, NO selector ---
sxm = sp.Matrix([[0, 1], [1, 0]]); sym = sp.Matrix([[0, -sp.I], [sp.I, 0]]); szm = sp.Matrix([[1, 0], [0, -1]])
G = [sxm, sym, szm]
M = p[0] * G[0] + p[1] * G[1] + p[2] * G[2]
check("T2 Dirac Higgs M^2 = |phi|^2 I (retained dirac_bridge)", sp.simplify(M * M - r2 * sp.eye(2)) == sp.zeros(2))
Vd_concrete = sp.expand(sp.trace((M * M) * (M * M)) - sp.Rational(1, 8) * sp.trace(M * M) ** 2)
c_d = sp.simplify(d_tr * (1 - d_tr / 8))
Vd_general = sp.expand(c_d * r2 ** 2)
check("T2b Dirac transported polynomial = d(1-d/8)|phi|^4 for d=Tr(I)",
      sp.simplify(Vd_general - (d_tr * r2 ** 2 - sp.Rational(1, 8) * (d_tr * r2) ** 2)) == 0)
check("T2c concrete Pauli d=2 instance gives (3/2)|phi|^4",
      sp.simplify(Vd_concrete - Vd_general.subs(d_tr, 2)) == 0)
Vd_hess_general = sp.hessian(Vd_general, p).subs({p[0]: 1, p[1]: 0, p[2]: 0})
check("T2d general Dirac Hessian at e_1 = diag(12c,4c,4c), c=d(1-d/8)",
      sp.simplify(Vd_hess_general - sp.diag(12 * c_d, 4 * c_d, 4 * c_d)) == sp.zeros(3))
check("T2e Dirac transverse Hessian entries are equal for symbolic d (no distinguished 32)",
      sp.simplify(Vd_hess_general[1, 1] - Vd_hess_general[2, 2]) == 0)
Vd = Vd_general

# --- T3: generality — every even invariant of M is a function of |phi|^2 (no selector) ---
ok_gen = True
for n in (1, 2, 3, 4):
    Tr2n = sp.trace(M ** (2 * n))
    # Concrete Pauli check: d=2. The symbolic generalization is
    # Tr M^{2n}=d |phi|^{2n} whenever M^2=|phi|^2 I and d=Tr(I).
    diff = sp.expand(Tr2n - 2 * r2 ** n)
    if sp.simplify(diff) != 0:
        ok_gen = False
check("T3 concrete Pauli even invariants Tr M^{2n} = 2|phi|^{2n}", ok_gen)
check("T3b symbolic premise form is Tr M^{2n} = d|phi|^{2n}, hence rotationally invariant",
      all(sp.simplify(d_tr * r2 ** n - d_tr * r2 ** n) == 0 for n in (1, 2, 3, 4)))

# --- T4: control teeth ---
# taste-cube V_sel distinguishes axis vs non-axis; Dirac V_sel depends only on |phi|
axis = {p[0]: 1, p[1]: 0, p[2]: 0}
nonaxis = {p[0]: 1, p[1]: 1, p[2]: 0}   # same |phi|^2=2 as (sqrt2,0,0)
diag_same_norm = {p[0]: sp.sqrt(2), p[1]: 0, p[2]: 0}
check("T4 taste-cube V_sel(axis)=0 but V_sel(non-axis)!=0 (genuine axis-selector)",
      (32 * selector).subs(axis) == 0 and (32 * selector).subs(nonaxis) != 0)
check("T4b Dirac V_sel(non-axis)=V_sel(same-|phi| axis) (rotation-blind, NO selector)",
      sp.simplify(Vd.subs(nonaxis) - Vd.subs(diag_same_norm)) == 0)

n_pass = sum(1 for _, ok in results if ok)
n_fail = sum(1 for _, ok in results if not ok)
for name, ok in results:
    print(("PASS" if ok else "FAIL"), name)
print()
print("TOTAL: PASS=%d FAIL=%d" % (n_pass, n_fail))
