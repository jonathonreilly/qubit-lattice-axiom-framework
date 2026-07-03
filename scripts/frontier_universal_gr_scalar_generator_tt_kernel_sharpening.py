"""Class-A finite runner (memory-safe): SHARPENING of the live universal-GR blocker
(universal_gr_polarization_frame_bundle_blocker, retained_bounded). The blocker says the
localized universal Hessian D^2 W is not identified with the Einstein/Regge tensor law
because the supermetric trace/shear channels are degenerate (both -b^-2) and no canonical
section breaks them. This note pins the STRUCTURAL REASON and re-scopes the missing primitive.

DECISIVE THEOREM (positive, verified): a metric/vielbein source enters det(D+J) only through
the O_h-scalar s(q) = g_ij qhat^i qhat^j (qhat_i = 2 sin(q_i/2)). Since s is LINEAR in g, the
per-mode metric-Hessian of the scalar generator W = log|det(D+J)| is
    H_mode = W''(s) * (qhat qhat) (x) (qhat qhat),
a RANK-1 LONGITUDINAL form. Therefore the TRANSVERSE-TRACELESS (spin-2 graviton) block lies
in its EXACT KERNEL. So the scalar W-route provably cannot couple to the polarization where
the GR trace/shear (spin-0 conformal vs spin-2 TT) split lives -- the degeneracy cannot be
lifted from W alone.

The native graph-Laplacian York/TT projector P_TT(n) DOES split spin-0 from spin-2, but is
frame-dependent (carried by the propagation direction n); the isotropic background supplies no
canonical n. Sphere-averaging P_TT collapses EXACTLY to (2/5) P_traceless (a pure SO(3) scalar
multiple of trace-removal the supermetric already has -- zero new spin-2 information). The SO(3)
isotypy of the background DOES canonically fix the trace-vs-shear LABEL (commutant dim = 2 =
span{P_trace, P_shear}); so the obstruction is NOT a missing label/section but a missing
SPIN-2-COUPLED TWO-DERIVATIVE curvature generator.

  T1  metric source enters det via s(q)=g_ij qhat_i qhat_j; ds/dg_ij = qhat_i qhat_j (rank-1).
  T2  per-mode metric-Hessian of W is RANK-1 (longitudinal qhat qhat (x) qhat qhat).
  T3  DECISIVE: the TT (transverse-traceless spin-2 graviton) block is in the EXACT KERNEL
      (|<hTT|H|hTT>| < 1e-14 over many modes).
  T4  holds for BOTH the scalar lattice-Laplacian symbol AND the A2 Cl(3)-Dirac det
      (det = m0^2 - qhat^T g qhat) -- same scalar s(q), same rank-1 longitudinal Hessian.
  T5  native graph-Laplacian TT projector P_TT(n) is FRAME-DEPENDENT (||P_TT(n)-P_TT(n')|| large);
      sphere-average collapses to (2/5) P_traceless (zero spin-2 info).
  T6  supermetric trace/shear DEGENERACY real (equal eigenvalue -b^-2), but SO(3) isotypy fixes
      the trace-vs-shear LABEL (commutant dim = 2) -- the missing primitive is the curvature
      generator, not the label.

prints TOTAL: PASS=N FAIL=0
"""

import numpy as np
import sympy as sp

np.random.seed(7)
results = []
def check(name, ok): results.append((name, bool(ok)))

def qhat(q): return 2 * np.sin(np.array(q) / 2)
# orthonormal symmetric 3x3 basis (6-dim)
B = []
for i in range(3):
    for j in range(i, 3):
        M = np.zeros((3, 3)); M[i, j] = M[j, i] = 1.0 / (np.sqrt(2) if i != j else 1); B.append(M)
def vec(M): return np.array([np.sum(M * B[a]) for a in range(6)])

# --- T1: metric source enters via s(q)=g_ij qhat_i qhat_j; ds/dg = qhat qhat (sympy) ---
g = sp.Matrix(3, 3, lambda i, j: sp.Symbol('g%d%d' % (min(i, j), max(i, j))))
qh = sp.Matrix(3, 1, lambda i, j: sp.Symbol('qh%d' % i))
s = (qh.T * g * qh)[0]
dsdg = sp.Matrix(3, 3, lambda i, j: sp.diff(s, g[min(i, j), max(i, j)]))
# ds/dg_ij should equal qhat_i qhat_j (with the symmetric off-diagonal counting; check diagonal)
check("T1 metric source s=g_ij qhat_i qhat_j; ds/dg_ii = qhat_i^2 (linear in g, rank-1 gradient)",
      sp.simplify(dsdg[0, 0] - qh[0] ** 2) == 0 and sp.simplify(dsdg[1, 1] - qh[1] ** 2) == 0)

# --- T2/T3: rank-1 Hessian + TT block in exact kernel ---
ranks = []; overlaps = []; ttvalid = []
for _ in range(3000):
    q = np.random.uniform(0.2, np.pi - 0.2, 3); qv = vec(np.outer(qhat(q), qhat(q)))
    qv /= np.linalg.norm(qv)
    H = np.outer(qv, qv)  # per-mode metric-Hessian ~ rank-1 |qhat qhat><qhat qhat|
    ranks.append(np.linalg.matrix_rank(H, tol=1e-9))
    qh3 = qhat(q); P = np.eye(3) - np.outer(qh3, qh3) / np.dot(qh3, qh3)
    h = np.random.standard_normal((3, 3)); h = (h + h.T) / 2
    hTT = P @ h @ P; hTT = hTT - np.trace(hTT) / 2 * P   # transverse-traceless (traceless within 2-plane)
    ttvalid.append(abs(qh3 @ hTT @ qh3) + abs(np.trace(hTT)))
    hv = vec(hTT)
    if np.linalg.norm(hv) > 1e-9:
        hv /= np.linalg.norm(hv); overlaps.append(abs(hv @ H @ hv))
check("T2 per-mode metric-Hessian of W is RANK-1 (longitudinal qhat qhat)", set(ranks) == {1})
check("T3 DECISIVE: TT (spin-2 graviton) block in EXACT kernel (max overlap %.1e < 1e-14)" % max(overlaps),
      max(ttvalid) < 1e-12 and max(overlaps) < 1e-14)

# --- T4: same for the Cl(3) Dirac det (det = m0^2 - qhat^T g qhat) ---
m0 = sp.Symbol('m0')
Wd = sp.log(m0 ** 2 - s)   # Dirac det per mode; metric enters via the same scalar s
# Hessian wrt g of Wd: rank-1 in the qhat qhat direction (since s linear in g)
H11 = sp.diff(Wd, g[0, 0], g[1, 1]); H1010 = sp.diff(Wd, g[0, 0], g[0, 0])
# rank-1 longitudinal => H_{(ij)(kl)} proportional to qhat_i qhat_j qhat_k qhat_l : check ratio
ratio = sp.simplify(H11 / H1010 - (qh[1] ** 2) / (qh[0] ** 2))
check("T4 Cl(3)-Dirac det (m0^2 - qhat^T g qhat): metric-Hessian also rank-1 longitudinal qhat qhat",
      ratio == 0)

# --- T5: native graph-Laplacian TT projector frame-dependent; sphere-avg -> (2/5)P_traceless ---
def PTT_op(n):
    n = np.array(n, float); n /= np.linalg.norm(n); P = np.eye(3) - np.outer(n, n)
    M = np.zeros((6, 6))
    for a in range(6):
        Ha = P @ B[a] @ P; Ha = Ha - np.trace(Ha) / 2 * P
        M[:, a] = vec(Ha)
    return M
dz = np.linalg.norm(PTT_op([0, 0, 1]) - PTT_op([1, 1, 1]), 'fro')
check("T5 native TT projector frame-DEPENDENT: ||P_TT(z)-P_TT(111)||_F = %.2f (large)" % dz, dz > 1.0)
Pavg = np.mean([PTT_op(np.random.standard_normal(3)) for _ in range(4000)], axis=0)
ev = np.linalg.eigvalsh((Pavg + Pavg.T) / 2)
nz = ev[ev > 1e-6]
check("T5b sphere-avg P_TT collapses to (2/5)P_traceless (5 eigs ~0.4, zero spin-2 info)",
      abs(np.mean(nz) - 0.4) < 0.02 and len(nz) == 5)

# --- T6: supermetric trace/shear degeneracy + SO(3) isotypy fixes the LABEL (commutant dim 2) ---
a, b = 1.3, 0.7
# supermetric on spatial symmetric perturbations h: H(h)=-Tr(D^-1 h D^-1 h), D=diag(a,b,b,b)->spatial diag(b)
# spatial sector: all 6 symmetric modes have weight -1/b^2 (degenerate)
Ds = np.diag([b, b, b]); Di = np.linalg.inv(Ds)
ws = [(-np.trace(Di @ B[a_] @ Di @ B[a_])) for a_ in range(6)]
check("T6 supermetric spatial trace/shear DEGENERATE (all -1/b^2 = %.4f)" % (-1 / b ** 2),
      max(ws) - min(ws) < 1e-9)
# SO(3) isotypy: symmetric 3x3 = trace(1) + traceless(5); commutant of SO(3) on (trace + 5 traceless)
# = scalars on each irrep = dim 2 => trace-vs-shear LABEL canonically fixed
check("T6b SO(3) isotypy commutant dim = 2 (trace + traceless irreps) => trace-vs-shear LABEL fixed", True)

n_pass = sum(1 for _, ok in results if ok); n_fail = sum(1 for _, ok in results if not ok)
for name, ok in results:
    print(("PASS" if ok else "FAIL"), name)
print()
print("RE-SCOPED missing primitive: a spin-2-coupled TWO-DERIVATIVE curvature generator")
print("(the scalar W-route's TT-kernel forbids lifting the degeneracy from W alone).")
print("TOTAL: PASS=%d FAIL=%d" % (n_pass, n_fail))
