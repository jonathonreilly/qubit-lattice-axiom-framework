"""A49 ed16: exact covariance matrices on the 16-site cubic cluster (Z^3 mod <(2,2,0),(2,0,2),(0,2,2)>, all 24 turns).
States (dual frame): projected parton lam' = 0, 0.1, 0.2; weakly ordered projected Neel / collinear references with
the order field along dual z and along dual (111); compass-staggered product state; controls: exact ground states of
the soldered Heisenberg rule J1 and of its Klein dual (-J1 + 2K1 in A44 units), polarized product state.
Saves C, G, <h> per state to ed16_C.npz; prints lowest relative variances per operator set."""
import sys, signal, time, numpy as np, scipy.sparse.linalg as sla
signal.alarm(285)
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from a49lib import *
t0 = time.time()
cl = Cluster([[2, 2, 0], [2, 0, 2], [0, 2, 2]]); N = cl.N
ops = [(nm, cls, "b", op) for nm, cls, op in bilinear_basis()] + [(nm, cls, "4", d4) for nm, cls, d4, sold in four_basis()]
T = Tables(cl, ops); names = T.names; n = len(names)
strs = [T.cluster_strings(k) for k in range(n)]
G = T.gram(strs)
print(f"16-site cluster: {T.np_} pairs, {T.ns} four-sets; Gram rank {np.linalg.matrix_rank(G, tol=1e-9)} of {n}")
print("Gram diagonal: " + " ".join(f"{nm}:{G[k,k]:.2f}" for k, nm in enumerate(names)))
Z = zarrays(N); bits = bits_table(N)
SETS = {"NN": ["J1", "K1", "D1"], "S1b": ["J1", "K1", "D1", "J2", "Kn2", "Kd2", "D2", "J3", "K3", "D3"],
        "S1": [x for x, c in zip(names, T.cls) if c == "S1"], "S1uS2": list(names)}
# twisted Casimir S_tw^2 (dual-frame total spin squared) on this cluster, expressed in the basis
cas = {}
for i in range(N):
    for j in range(i + 1, N):
        for a in range(3):
            add(cas, ((i, a), (j, a)), 1.)
bcas = np.array([hs(s, cas) / N for s in strs]); ccas = np.linalg.lstsq(G, bcas, rcond=None)[0]
res_cas = hs(cas, cas) / N - bcas @ ccas
print(f"twisted Casimir in span(S1uS2) on this cluster: residual {res_cas:.2e} (coefficients " + " ".join(f"{nm}:{c:+.3f}" for nm, c in zip(names, ccas) if abs(c) > 1e-9) + ")")

def report(tag, C, ex):
    out = {}
    for sname, sl in SETS.items():
        ix = [names.index(x) for x in sl]
        lam, V = releig(C[np.ix_(ix, ix)], G[np.ix_(ix, ix)])
        v = V[:, 0]; v = v / np.abs(v).max()
        top = sorted(range(len(ix)), key=lambda q: -abs(v[q]))[:4]
        cs = ""
        if sname == "S1uS2":   # overlap of lowest vector with the Casimir direction (G metric)
            cc = ccas[ix]; cs = f" | cos(low vec, Casimir) = {abs(V[:,0] @ G[np.ix_(ix,ix)] @ cc)/np.sqrt(cc @ G[np.ix_(ix,ix)] @ cc):.3f}"
            # lowest in the G-orthogonal complement of the Casimir
            g = G[np.ix_(ix, ix)] @ cc; Zc = np.linalg.svd(g[None, :])[2][1:].T
            lam_c = releig(Zc.T @ C[np.ix_(ix, ix)] @ Zc, Zc.T @ G[np.ix_(ix, ix)] @ Zc)[0]
            cs += f"; complement: {lam_c[0]:.4g}, {lam_c[1]:.4g}"
        print(f"  {tag:14s} {sname:6s} n={len(ix):2d}: lam = {lam[0]:.4g}, {lam[1]:.4g}, {lam[2]:.4g}; low vec " +
              " ".join(f"{sl[q]}:{v[q]:+.2f}" for q in top) + cs, flush=True)
        out[sname] = lam
    return out

store = {"names": np.array(names), "G": G, "ccas": ccas}
def run_state(tag, psi):
    psi = psi / np.linalg.norm(psi)
    C, ex, _ = exact_C(strs, psi, Z, N)
    store[f"C_{tag}"] = C; store[f"ex_{tag}"] = ex
    print(f" {tag}: <h> per site " + " ".join(f"{nm}:{e:+.3f}" for nm, e in zip(names, ex) if abs(e) > 5e-4), flush=True)
    report(tag, C, ex)
    return psi

print("== parton states ==")
psis = {}
for lp in (0.0, 0.1, 0.2):
    Phi, gap = mf_state(cl, lam2=lp); print(f" lam'={lp}: MF gap {gap:.3f}")
    psis[lp] = run_state(f"lp{lp}", projected_vector(Phi, bits))
    v = psis[lp]; nup = N - bits.sum(1); W = np.bincount(nup, weights=np.abs(v) ** 2, minlength=N + 1)
    print(f"   sector weights W(n_up = 8, 9, 10, 7, 6) = " + ", ".join(f"{W[k]:.2e}" for k in (8, 9, 10, 7, 6)))
print("== ordered references ==")
for pat, ms in (("neel", (0.05, 0.1, 0.3)), ("collinear", (0.1, 0.4))):
    for ax, axn in (((0, 0, 1), "z"), ((1, 1, 1), "111")):
        for m in ms:
            Phi, gap = mf_state(cl, m=m, pattern=pat, axis=ax)
            if gap < 1e-8: print(f" {pat} {axn} m={m}: open shell"); continue
            run_state(f"{pat[:3]}{axn}_{m}", projected_vector(Phi, bits))
blochs = [(-1) ** int(sum(x)) * np.ones(3) / np.sqrt(3) for x in cl.sites]
run_state("cs_product", projected_vector(product_state(blochs), bits))   # dual Neel along 111 = soldered compass-staggered
print("== controls ==")
def ground(c):
    H = {}
    for k, ck in enumerate(c):
        for key, v in strs[k].items(): add(H, key, ck * v)
    H = clean(H)
    op = sla.LinearOperator((2 ** N, 2 ** N), matvec=lambda x: apply_strings(H, x.astype(complex), Z), dtype=complex)
    vals, vecs = sla.eigsh(op, k=3, which='SA', tol=1e-13)
    o = np.argsort(vals); return vals[o], vecs[:, o], H
cJ = np.zeros(n); cJ[names.index("J1")] = 1.
vals, vecs, H = ground(cJ)
print(f" soldered Heisenberg J1: E0/N = {vals[0]/N:+.6f}, gap/N {(vals[1]-vals[0])/N:.4f}; residual {np.linalg.norm(apply_strings(H, vecs[:,0], Z) - vals[0]*vecs[:,0]):.1e}")
run_state("gs_J1", vecs[:, 0])
cD = np.zeros(n); cD[names.index("J1")] = -1.; cD[names.index("K1")] = 2 / np.sqrt(3)
vals, vecs, H = ground(cD)
print(f" Klein-dual Heisenberg (-J1 + 1.1547 K1): E0/N = {vals[0]/N:+.6f}, gap/N {(vals[1]-vals[0])/N:.4f}")
run_state("gs_dualJ1", vecs[:, 0])
nh = np.array([1., 2., 3.]) / np.sqrt(14.)
pol = [np.array([kR(x, b) * nh[b] for b in range(3)]) for x in cl.sites]     # soldered uniform n -> dual R_x n
run_state("polarized", projected_vector(product_state(pol), bits))
np.savez("ed16_C.npz", **store)
print(f"done in {time.time()-t0:.0f}s")
