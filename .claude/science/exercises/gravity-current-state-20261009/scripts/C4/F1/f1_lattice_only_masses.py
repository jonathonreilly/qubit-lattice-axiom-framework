"""F1 (lane RF), case B: keep only the lattice's discrete symmetries plus the preferred slicing
(spatial diffeos NOT a gauge redundancy). Static Newtonian sector with every O(k^0) mass term that
proper cubic symmetry allows in the (h_ij, n) sector, plus generic gauge-breaking O(k^2) gradient
terms for the now-physical longitudinal parts of h.
  cubic O(k^0) invariants: h-block 3 (mu_A1 trace, mu_E, mu_T2); n^2 (mu_n); n tr h (m4);
  shift n_i n_i (mu_1); no shift-h or shift-n mixing (T1 x {A1,E,T2} has no A1).  (checked below by
  a group average.)
Static energy (GR normalisation g=1/2, g_n=1, khronometric alpha=a):
  E = (g/2) h.R.h + (b/2)|q.h|^2 + (b2/2)(q.h.q)^2 + 1/2 h.Mh.h + g_n n S.h + 1/2(-2 a q^2 + mu_n) n^2 + m4 n tr h + n rho
Readout as k -> 0: n k^2 (Newtonian needs a finite negative limit) and gamma = Psi/Phi
(Psi from the transverse trace part; Phi = n).
"""
import numpy as np, itertools
exec(open(__file__.replace('f1_lattice_only_masses.py', 'f1_symbol_lib.py')).read())

# --- group average: count O(k^0) cubic-invariant quadratic forms on (h6, n, n_i3)
def cubic_group():
    mats = []
    for perm in itertools.permutations(range(3)):
        P = np.zeros((3, 3))
        for i, p in enumerate(perm): P[i, p] = 1
        for signs in itertools.product([1, -1], repeat=3):
            Rm = P * np.array(signs)[:, None]
            if np.linalg.det(Rm) > 0: mats.append(Rm)
    return mats
G = cubic_group()
def rep(Rm):
    # action on (h(6), n(1), N_i(3)) as 10x10
    Hh = np.zeros((6, 6))
    for b in range(6):
        Hh[:, b] = vec(Rm @ BAS[b] @ Rm.T)
    out = np.zeros((10, 10)); out[:6, :6] = Hh; out[6, 6] = 1; out[7:, 7:] = Rm
    return out
# dimension of invariant symmetric bilinear forms = dim of invariant subspace of Sym^2(V)
dimV = 10
basis_forms = []
for i in range(dimV):
    for j in range(i, dimV):
        F = np.zeros((dimV, dimV)); F[i, j] = F[j, i] = 1; basis_forms.append(F)
Proj = np.zeros((len(basis_forms), len(basis_forms)))
Bv = np.array([F[np.triu_indices(dimV)] for F in basis_forms]).T
for Rm in G:
    Rr = rep(Rm)
    img = np.array([(Rr.T @ F @ Rr)[np.triu_indices(dimV)] for F in basis_forms]).T
    Proj += np.linalg.lstsq(Bv, img, rcond=None)[0]
Proj /= len(G)
print(f"cubic-invariant O(k^0) quadratic forms on (h_ij, n, n_i): {int(round(np.trace(Proj)))}  (expect 6: muA1, muE, muT2, mu_n, m4, mu_1)")

def static_B(kmag, mu=dict(), a=0.1, g=0.5, g_n=1.0, b=1.0, b2=0.7, d=np.array([0.36, 0.48, 0.8])):
    k = kmag * d / np.linalg.norm(d)
    q = 2 * np.sin(k / 2); qq = q @ q
    R = R_op(q); s = S_vec(q)
    Qv = np.zeros((3, 6));
    for bb in range(6): Qv[:, bb] = BAS[bb] @ q
    qhq = np.array([q @ BAS[bb] @ q for bb in range(6)])
    tr = np.array([1, 1, 1, 0, 0, 0.])
    PA1 = np.outer(tr, tr) / 3; PE = np.diag([1, 1, 1, 0, 0, 0.]) - PA1; PT2 = np.diag([0, 0, 0, 1, 1, 1.])
    Mh = mu.get('A1', 0) * PA1 + mu.get('E', 0) * PE + mu.get('T2', 0) * PT2
    M = np.zeros((7, 7))
    M[:6, :6] = g * R + b * Qv.T @ Qv + b2 * np.outer(qhq, qhq) + Mh
    M[:6, 6] = M[6, :6] = g_n * s + mu.get('m4', 0) * tr
    M[6, 6] = -2 * a * qq + mu.get('n', 0)
    rhs = np.zeros(7); rhs[6] = 1.0
    x = -np.linalg.solve(M, rhs)
    h = mat(x[:6]); n = x[6]
    # transverse-trace part: sigma = (tr h - khat.h.khat)/2
    kh = q / np.sqrt(qq)
    sigma = (np.trace(h) - kh @ h @ kh) / 2
    return n * qq, (-sigma / 2) / n

cases = [("none (gauge-breaking gradients only)", {}),
         ("mu_E = 1e-3 (TT-only mass)", {'E': 1e-3}),
         ("mu_A1 = 1e-3", {'A1': 1e-3}),
         ("mu_n = 1e-3", {'n': 1e-3}),
         ("m4 = 1e-3", {'m4': 1e-3}),
         ("mu_A1=1e-3, m4 tuned to det=0 direction?", {'A1': 1e-3, 'm4': 1e-3, 'n': 1e-3})]
for name, mu in cases:
    rows = []
    for km in [1e-1, 1e-2, 1e-3, 1e-4]:
        nk2, gam = static_B(km, mu)
        rows.append(f"k={km:.0e}: nk2={nk2:+.4f}, gamma={gam:+.4f}")
    print(f"  {name}: " + " | ".join(rows))
print("  GR target: n k^2 -> -1/(2(2-a)) = %.4f, gamma -> 1" % (-1 / (2 * (2 - 0.1))))
