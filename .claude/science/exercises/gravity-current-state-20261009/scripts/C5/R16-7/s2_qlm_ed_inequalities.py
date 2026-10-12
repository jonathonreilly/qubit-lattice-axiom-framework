"""R16-7 s2 (written before running): ED sanity check of the inequality machinery (M1-M4) on a
2D U(1) quantum link model (spin-1/2 links = qubits, exact integer Gauss law div E = 0), L x L torus.
H = -K sum_p (U_p + U_p^dag) + V sum_p (U_p U_p^dag + U_p^dag U_p),  U_p = S+_b S+_r S-_t S-_l.
Checks (pre-registered):
 (a) f-sum identity: m1(k) = <[C^dag,[H,C]]> equals K sum_p |mu_p(k)|^2 <U_p+U_p^dag> (pattern symbol |mu|^2 = qhat^2)
 (b) Bogoliubov: chi_AA * m1 >= |<[C,A]>|^2  (A = magnetic sine at -k)
 (c) softness bound: omega_min(k)^2 <= m1/chi_CC
 (d) diamagnetic: E0(random plaquette twists) >= E0(0)  (H stoquastic in the E basis for K > 0)
This tests factors/signs of the general theorems; it is not a thermodynamic-limit photon measurement
(2D compact U(1) is confining).
"""
import numpy as np, itertools, sys
L = int(sys.argv[1]) if len(sys.argv) > 1 else 4
K, Vrk = 1.0, float(sys.argv[2]) if len(sys.argv) > 2 else 0.0
def lid(x, y, d): return 2*((x % L) + L*(y % L)) + d
nl = 2*L*L
site_links = []
for y in range(L):
    for x in range(L):
        site_links.append([(lid(x, y, 0), +1), (lid(x, y, 1), +1), (lid(x-1, y, 0), -1), (lid(x, y-1, 1), -1)])
complete_at = {}
for s, lk in enumerate(site_links):
    complete_at.setdefault(max(l for l, _ in lk), []).append(s)
states = []
cfg = np.zeros(nl, int)   # E = cfg - 1/2 -> use e = 2E = +-1
def dfs(l):
    if l == nl:
        states.append(cfg.copy()); return
    for v in (1, -1):
        cfg[l] = v; ok = True
        for s in complete_at.get(l, []):
            if sum(sg*cfg[ll] for ll, sg in site_links[s]) != 0: ok = False; break
        if ok: dfs(l+1)
    cfg[l] = 0
dfs(0)
states = np.array(states); D = len(states)
index = {tuple(s): i for i, s in enumerate(states)}
# plaquettes: b=(x,y,0) +, r=(x+1,y,1) +, t=(x,y+1,0) -, l=(x,y,1) -
plaqs = []
for y in range(L):
    for x in range(L):
        plaqs.append(((lid(x, y, 0), +1), (lid(x+1, y, 1), +1), (lid(x, y+1, 0), -1), (lid(x, y, 1), -1), (x+0.5, y+0.5)))
def apply_U(st, p, dag=False):
    # U raises e on + links (e: -1 -> +1) and lowers on - links; U^dag the reverse
    new = st.copy()
    for (l, sg) in p[:4]:
        want_from = -sg if not dag else sg
        if st[l] != want_from: return None
        new[l] = -want_from
    return new
Uops = []
for p in plaqs:
    M = np.zeros((D, D))
    for i, st in enumerate(states):
        n = apply_U(st, p)
        if n is not None: M[index[tuple(n)], i] = 1.0
    Uops.append(M)
# winding sectors
Wx = np.array([sum(st[lid(0, y, 0)] for y in range(L)) for st in states])
Wy = np.array([sum(st[lid(x, 0, 1)] for x in range(L)) for st in states])
def H_of(theta=None):
    H = np.zeros((D, D), complex)
    for j, U in enumerate(Uops):
        ph = 1.0 if theta is None else np.exp(1j*theta[j])
        H += -K*(ph*U + np.conj(ph)*U.T) + Vrk*(U@U.T + U.T@U)
    return H
H = H_of()
print("L=%d  Gauss-law states D=%d  V=%.2f  K=%.1f" % (L, D, Vrk, K))
secs = sorted(set(zip(Wx, Wy)))
best = None
for sec in secs:
    idx = np.where((Wx == sec[0]) & (Wy == sec[1]))[0]
    e0 = np.linalg.eigvalsh(H[np.ix_(idx, idx)].real)[0]
    if best is None or e0 < best[0] - 1e-12: best = (e0, sec, idx)
E0, sec, idx = best
print("ground-state winding sector", sec, " dim", len(idx), " E0 = %.8f" % E0)
Hs = H[np.ix_(idx, idx)]
w, v = np.linalg.eigh(Hs); g0 = v[:, 0]
print("gap to first excitation in sector: %.6f ; GS min component (Perron-Frobenius positivity): %.3e" % (w[1]-w[0], (g0*np.sign(g0.sum())).real.min()))
Esub = lambda M: M[np.ix_(idx, idx)]
for n in range(1, L//2 + 1):
    k = 2*np.pi*n/L
    # C = sum over y-links e^{i k x} e_l / 2 (E = e/2), transverse to k || x
    Cd = np.zeros(D, complex)
    for i, st in enumerate(states):
        Cd[i] = sum(np.exp(1j*k*x)*st[lid(x, y, 1)]/2 for x in range(L) for y in range(L))
    C = np.diag(Cd)
    A = np.zeros((D, D), complex)
    for (p, U) in zip(plaqs, Uops):
        A += np.exp(-1j*k*p[4][0])*(U - U.T)/(2j)
    C, A = Esub(C), Esub(A)
    comm = lambda X, Y: X@Y - Y@X
    m1 = (g0.conj()@comm(C.conj().T, comm(Hs, C))@g0).real
    mu2 = abs(np.exp(1j*k) - 1)**2
    hop = sum((g0.conj()@Esub(U + U.T)@g0).real for U in Uops)
    m1_formula = K*mu2*hop
    lhs_comm = abs(g0.conj()@comm(C, A)@g0)**2
    def chi(X):
        Xn = v.conj().T@X@g0; Xdn = v.conj().T@X.conj().T@g0
        return sum((abs(Xn[j])**2 + abs(Xdn[j])**2)/(w[j]-w[0]) for j in range(1, len(w)))
    chiA, chiC = chi(A), chi(C)
    Cn = v.conj().T@C@g0; Cdn = v.conj().T@C.conj().T@g0
    conn = [j for j in range(1, len(w)) if abs(Cn[j])**2 + abs(Cdn[j])**2 > 1e-12]
    wmin = w[conn[0]] - w[0] if conn else np.nan
    print("k=%.4f qhat^2=%.4f | (a) m1=%.6f formula K|mu|^2<U+U^dag>=%.6f | (b) chi_AA*m1=%.6f >= |<[C,A]>|^2=%.6f : %s | (c) wmin^2=%.6f <= m1/chi_CC=%.6f : %s" % (
        k, mu2, m1, m1_formula, chiA*m1, lhs_comm, chiA*m1 >= lhs_comm - 1e-10, wmin**2, m1/chiC, wmin**2 <= m1/chiC + 1e-10))
rng = np.random.default_rng(3); viol = 0; mins = []
for trial in range(20):
    th = rng.uniform(0, 2*np.pi, len(plaqs))
    Ht = H_of(th)
    e = min(np.linalg.eigvalsh(Ht[np.ix_(np.where((Wx==s[0])&(Wy==s[1]))[0], np.where((Wx==s[0])&(Wy==s[1]))[0])])[0] for s in secs)
    mins.append(e - E0); viol += e < E0 - 1e-10
print("(d) diamagnetic: 20 random twists, min(E0(theta)-E0(0)) = %.6f, violations = %d" % (min(mins), viol))
