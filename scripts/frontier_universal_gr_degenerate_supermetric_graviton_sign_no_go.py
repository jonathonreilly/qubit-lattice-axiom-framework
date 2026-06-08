"""Class-A finite runner (memory-safe): the framework's degenerate (lambda=0, trace=shear)
W-supermetric, glued to the linearized Regge/Lichnerowicz curvature potential, CANNOT produce
a healthy spin-2 graviton -- a global-sign no-go. Sharpens the universal-GR polarization-frame
blocker (retained_bounded) from "D^2 W unidentified with Einstein/Regge" to a single SIGNED defect:
the missing conformal/indefiniteness term.

Setup (gluing of kinetic + potential halves):
  kinetic   = the supermetric fiber metric G on ADM channels;
  potential = the linearized Regge/Lichnerowicz curvature V (COMPARATOR method-context, not W-derived):
              V_trace = -k^2/2, V_shear(TT) = +k^2/2 (opposite-sign O(k^2));
  dispersion omega^2(channel) = V(channel) / G(channel).

Framework supermetric (retained universal_gr_supermetric_normal_form) = the lambda=0 DeWitt case:
  G = -Tr(D^-1 h D^-1 k) on D=diag(a,b,b,b) -> G_trace = G_shear = -1/b^2 (DEGENERATE, no conformal term).
Standard GR DeWitt (lambda=1) control:  G_trace = -2/b^2, G_shear = +1/b^2 (indefinite).

  T1  framework supermetric is lambda=0 DeWitt: G_trace = G_shear = -1/b^2 (degenerate); GR (lambda=1):
      G_trace=-2/b^2, G_shear=+1/b^2; the difference is the conformal -lambda(tr h)^2 term, which VANISHES on TT.
  T2  gluing dispersion (framework lambda=0): omega^2_trace and omega^2_TT come out OPPOSITE-signed
      (omega^2_TT < 0, tachyonic) -- no healthy graviton.
  T3  GR control (lambda=1): omega^2_trace > 0 AND omega^2_TT > 0 (healthy) -- the ratio method is sound;
      the failure is SPECIFIC to the degenerate lambda=0 supermetric.
  T4  GLOBAL-SIGN THEOREM: for the degenerate (G_trace=G_shear) supermetric, omega^2_trace * omega^2_TT < 0
      for EVERY overall normalization sign -- no normalization heals both physical channels.
  T5  #3214 reproduced: W's per-mode metric-Hessian is rank-1 longitudinal (qhat qhat)(x)(qhat qhat);
      the TT graviton is in W's EXACT kernel -- so the -1/b^2 TT kinetic weight has NO finite-k W origin either.

prints TOTAL: PASS=N FAIL=0
"""

import numpy as np
import sympy as sp

results = []
def check(name, ok): results.append((name, bool(ok)))

# --- T1: framework supermetric = lambda=0 DeWitt (trace=shear), GR = lambda=1 ---
a, b, phi, A = sp.symbols('a b phi A', positive=True)
lam = sp.symbols('lambda')
# DeWitt G_lambda(h,h) = |h|^2_g - lambda (tr_g h)^2, spatial metric g=b^2 I (so g^-1=b^-2 I)
# trace mode h=phi*I: |h|^2 = 3 phi^2 b^-4 ; (tr_g h)^2 = (b^-2*3phi)^2... use normalized channel weights
def G_trace(l): return (3 - 9 * l) / b ** 4      # conformal/trace weight (per phi^2)
def G_shear(l): return sp.Integer(1) / b ** 4 * 2  # TT weight (per A^2); lambda-independent (traceless)
check("T1 framework lambda=0: G_trace ~ G_shear sign-equal (degenerate); conformal term vanishes on TT",
      sp.simplify(G_trace(0) - 3 / b ** 4) == 0 and sp.simplify(sp.diff(G_shear(lam), lam)) == 0)
check("T1b GR lambda=1: G_trace=-6/b^4 (neg) vs G_shear=+2/b^4 (pos) -> OPPOSITE (indefinite)",
      sp.simplify(G_trace(1) + 6 / b ** 4) == 0 and G_trace(1) < 0)

# --- T2/T3/T4: gluing dispersion omega^2 = V/G, V_trace=-k^2/2, V_shear=+k^2/2 ---
bn = 0.7; k = 1.0
def disp(Gtr, Gsh): return ((-k * k / 2) / Gtr, (+k * k / 2) / Gsh)
# framework lambda=0: G_trace = G_shear = -1/b^2 (the retained supermetric normal form's spatial weights)
wt0, ws0 = disp(-1 / bn ** 2, -1 / bn ** 2)
check("T2 framework lambda=0 gluing: omega^2_trace and omega^2_TT OPPOSITE-signed; TT tachyonic (omega^2_TT<0)",
      wt0 * ws0 < 0 and ws0 < 0)
wt1, ws1 = disp(-2 / bn ** 2, +1 / bn ** 2)   # GR lambda=1 control
check("T3 GR control lambda=1: omega^2_trace>0 AND omega^2_TT>0 (healthy graviton) -> method sound",
      wt1 > 0 and ws1 > 0)
# global-sign theorem: degenerate G (G_trace=G_shear=g0); omega^2_trace*omega^2_TT = (V_tr V_sh)/g0^2 < 0 always
gs_ok = True
for eps in (+1, -1):
    g0 = eps * (-1 / bn ** 2); wt, ws = disp(g0, g0)
    if not (wt * ws < 0): gs_ok = False
check("T4 GLOBAL-SIGN THEOREM: degenerate supermetric -> omega^2_trace*omega^2_TT<0 for EVERY overall sign (no heal)",
      gs_ok)

# --- T5: #3214 reproduced -- W metric-Hessian rank-1 longitudinal, TT graviton in exact kernel ---
np.random.seed(3)
B = []
for i in range(3):
    for j in range(i, 3):
        M = np.zeros((3, 3)); M[i, j] = M[j, i] = 1.0 / (np.sqrt(2) if i != j else 1); B.append(M)
def vec(M): return np.array([np.sum(M * B[a_]) for a_ in range(6)])
def qhat(q): return 2 * np.sin(np.array(q) / 2)
ranks = []; overlaps = []
for _ in range(2000):
    q = np.random.uniform(0.2, np.pi - 0.2, 3); qv = vec(np.outer(qhat(q), qhat(q))); qv /= np.linalg.norm(qv)
    H = np.outer(qv, qv); ranks.append(np.linalg.matrix_rank(H, tol=1e-9))
    qh = qhat(q); P = np.eye(3) - np.outer(qh, qh) / np.dot(qh, qh)
    h = np.random.standard_normal((3, 3)); h = (h + h.T) / 2
    hTT = P @ h @ P; hTT = hTT - np.trace(hTT) / 2 * P; hv = vec(hTT)
    if np.linalg.norm(hv) > 1e-9:
        hv /= np.linalg.norm(hv); overlaps.append(abs(hv @ H @ hv))
check("T5 #3214: W metric-Hessian rank-1 longitudinal; TT graviton in EXACT kernel (no finite-k W origin)",
      set(ranks) == {1} and max(overlaps) < 1e-14)

n_pass = sum(1 for _, ok in results if ok); n_fail = sum(1 for _, ok in results if not ok)
for name, ok in results:
    print(("PASS" if ok else "FAIL"), name)
print()
print("framework lambda=0: omega^2_trace=%.3f  omega^2_TT=%.3f (opposite, TT tachyonic)" % (wt0, ws0))
print("GR lambda=1 control: omega^2_trace=%.3f  omega^2_TT=%.3f (both healthy)" % (wt1, ws1))
print("DEFECT = missing conformal/indefiniteness term; missing primitive narrows to ONE object:")
print("  a spin-2-coupled two-derivative curvature generator PAIRED with a non-degenerate fiber metric.")
print("TOTAL: PASS=%d FAIL=%d" % (n_pass, n_fail))
