import sys, pickle, math, numpy as np, scipy.linalg as sl
sys.path.insert(0, '.'); sys.path.insert(0, '/Users/jonreilly/Projects/Physics/.claude/worktrees/peaceful-heisenberg-e2d2a0/scripts')
import regge_generic as RG, whitney as WF
from rp import rp_matrix
import scale_ladder_gravity_regge_metric_universality_common_cone_2026_10_18 as R1
C = pickle.load(open('canon_1.pkl', 'rb'))
print("vertex types:", sorted(set(tuple(np.round(o, 3)) for o in C.OFF)))
# (a) leading symbol: Schur over the complement of im M + im G
A0 = np.hstack([C.line_map(np.zeros(4)), C.gauge(np.zeros(4))]).real; u, s, _ = np.linalg.svd(A0); Cc = u[:, int((s > 1e-9*s[0]).sum()):]
def seff(k):
    Q = C.Q(k); Mp, Mm = C.line_map(k), C.line_map(-k)
    return Mm.T @ Q @ Mp - (Mm.T @ Q @ Cc) @ np.linalg.solve(Cc.T @ Q @ Cc, Cc.T @ Q @ Mp)
B, *_ = R1.census(2, 2, R1.GROUPS['B4'])
def FS(x, h, k):
    a = [seff(e*k)/e**2 for e in (2e-2, 1e-2)]; S2 = (4*a[1]-a[0])/3; return float(np.real(x @ (0.5*(S2+S2.T)) @ x))
cS, _ = R1.fit(FS, B, nsamp=700); cE, _ = R1.fit(lambda x, h, k: R1.EH(h, k, np.eye(4)), B, nsamp=700)
lam = (cS@cE)/(cE@cE); print(f"(a) full form O(k^2) = {lam:+.6f} EH, misfit {np.linalg.norm(cS-lam*cE)/np.linalg.norm(cS):.1e}")
# (b) Whitney forms: Hodge massless counts and on-shell k^4
F = WF.Forms(C); print("(b) form classes:", F.n, " d^2:", max(np.abs(F.d(j+1, np.array([0.3,0.1,-0.2,0.4])) @ F.d(j, np.array([0.3,0.1,-0.2,0.4]))).max() for j in range(3)))
kd = np.array([0.3, -0.5, 0.6, 0.55]); kd /= np.linalg.norm(kd)
cnt = []
for j in range(5):
    K, M = F.hodge(j, 0.01*kd); w = np.sort(np.real(sl.eigvals(K, M))); cnt.append(int((np.abs(w) < 1e-2).sum()))
print("    Hodge massless counts per degree:", cnt)
worst = 0
for n in [(1,0,0), (3,1,2)]:
    n = np.array(n, float); n /= np.linalg.norm(n); km = 0.05
    for j in range(5):
        K, M = F.hodge(j, np.array([*(km*n), 1j*km])); w = np.sort(np.abs(sl.eigvals(K, M)))
        worst = max(worst, w[math.comb(4, j)-1]/km**2)
print(f"    on omega = k: max |lambda|/k^2 over the 16 = {worst:.1e} (O(k^4) term would be ~1e-4)")
# (c) graviton shells near the cone
def svn(k):
    s_ = np.sort(np.linalg.svd(C.Q(k), compute_uv=False)); return s_/s_[-1]
ng = 4*len(C.types)
for name, n in {'axis': (1,0,0), 'face': (1,1,0), 'body': (1,1,1)}.items():
    n = np.array(n, float); n /= np.linalg.norm(n); km = 0.05; ks = km*n
    oms = km*np.linspace(0.995, 1.005, 201); f = np.array([svn(np.array([*ks, 1j*o]))[ng] for o in oms])
    mins = [oms[i] for i in range(1, 200) if f[i] < f[i-1] and f[i] < f[i+1] and f[i] < 1e-6]
    print(f"(c) graviton {name}: on-shell alphas {[round((w*w/km**2-1)/km**2, 4) for w in mins]}")
# (d) RP of the P1 scalar with lumped mass
tix = {t: i for i, t in enumerate(C.types)}; wv = np.zeros(len(C.types))
for vs in C.simp:
    P = np.array([C.pos(v) for v in vs]); vol = abs(np.linalg.det(P[1:]-P[0]))/24
    for v in vs: wv[tix[v[1]]] += vol/5
offs_t = [float(o[3]) for o in C.OFF]
mn = min(np.linalg.eigvalsh(0.5*(R+R.conj().T)).min()/abs(np.linalg.eigvalsh(0.5*(R+R.conj().T))).max()
         for ks in [np.zeros(3), np.array([0.7, -0.3, 0.2])] for t0 in (0.0, 0.5)
         for R in [rp_matrix(lambda k: RG.p1_scalar(C, k) + 0.3*np.diag(wv), offs_t, ks, 6, t0)[0]])
print(f"(d) P1 scalar lumped-mass RP: min/max eigenvalue {mn:+.1e}")
