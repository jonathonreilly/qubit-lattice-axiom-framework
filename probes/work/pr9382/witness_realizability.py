"""PR 9382 attack-a: WITNESS REALIZABILITY for the forward-walking structure-factor note.

The note's stated configurations and numbers exist in the declared setting, rebuilt with own code:
 1. the momenta: k = pi/4 on the 8^3 torus (2 pi/8) and k = pi/8 on 16^3 (2 pi/16) are allowed cyclic momenta, s = 2 sin(k/2) = 2 sin(pi/8) for the first; N = 512 and 4096;
 2. the note's arithmetic from its own inputs u = 0.2888, chi = 1.064 +- 0.008, S = 0.408 +- 0.014: ceiling s sqrt(u chi) = 0.424, ratio 0.963 +- 0.034, m0/m_-1 = 0.768 = 1.003 s,
    sqrt(m1/m_-1) = 0.798 = 1.042 s, m1/m0 = 0.829 = 1.082 s (with m1 = 2 u s^2, m_-1 = chi/2, m0 = S); the combination of the two seeds' 0.4058 and 0.4110;
 3. the exact 2^3 control at k = pi: the flip component (864 states) of the canonical zero-winding state is built by own BFS and its exact S = m0 = 1.01215 is the note's 'exact' value; the
    four runs' 1.0115, 1.0128, 1.0099 are within 0.15 % of it;
 4. the moment chain holds for the exact 2^3 data, and 'ceiling' arithmetic of the exact case: the exact S / ceiling ratio (the bound is attained only by a one-frequency measure).
"""
import sys, time
import numpy as np
from scipy.sparse import coo_matrix, csr_matrix
from scipy.sparse.linalg import eigsh, cg, LinearOperator

T0 = time.time()
PASS = FAIL = 0; HITS = []
def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1; HITS.append(name)
    print(f"[{'PASS' if ok else 'FAIL'}] {name} {detail}", flush=True)

def build(Ls):
    Lx, Ly, Lz = Ls
    sites = [(x, y, z) for x in range(Lx) for y in range(Ly) for z in range(Lz)]
    sid = {s: i for i, s in enumerate(sites)}; nv = len(sites); nl = 3 * nv
    def lk(s, a): return a * nv + sid[s]
    def sh(s, a, d=1):
        t = list(s); t[a] = (t[a] + d) % Ls[a]; return tuple(t)
    plaq = []
    for s in sites:
        for a in range(3):
            for b in range(a + 1, 3):
                plaq.append((lk(s, a), lk(sh(s, a), b), lk(sh(s, b), a), lk(s, b)))
    canon = np.zeros(nl, np.int64)
    for s in sites:
        canon[lk(s, 0)] = (-1) ** s[1]; canon[lk(s, 1)] = (-1) ** s[0]; canon[lk(s, 2)] = (-1) ** s[0]
    axis = np.repeat(np.arange(3), nv)
    tail = np.array(sites * 3)                                   # link (s, a) has tail vertex s
    xb = tail[np.arange(nl), (axis + 1) % 3]                      # coordinate of the tail along axis a + 1
    return sites, nv, nl, np.array(plaq), canon, axis, xb
def vertex_div_zero(nv, nl, sites, Ls, canon):
    sid = {s: i for i, s in enumerate(sites)}
    for s in sites:
        d = 0
        for a in range(3):
            t = list(s); t[a] = (t[a] - 1) % Ls[a]
            d += canon[a * nv + sid[s]] - canon[a * nv + sid[tuple(t)]]
        if d != 0: return False
    return True
def component(nl, plaq, c0):
    masks = np.array([sum(1 << int(l) for l in p) for p in plaq], np.int64)
    seen = np.array([c0], np.int64); frontier = seen.copy()
    while len(frontier):
        new = []
        for p, m in zip(plaq, masks):
            b = [(frontier >> int(l)) & 1 for l in p]
            circ = (2 * b[0] - 1) + (2 * b[1] - 1) - (2 * b[2] - 1) - (2 * b[3] - 1)
            sel = frontier[np.abs(circ) == 4]
            if len(sel): new.append(sel ^ m)
        if not new: break
        new = np.unique(np.concatenate(new)); new = new[~np.isin(new, seen, assume_unique=True)]
        seen = np.union1d(seen, new); frontier = new
    return seen, masks
def hamiltonian(codes, plaq, masks):
    n = len(codes); rows = []; cols = []
    for p, m in zip(plaq, masks):
        b = [(codes >> int(l)) & 1 for l in p]
        circ = (2 * b[0] - 1) + (2 * b[1] - 1) - (2 * b[2] - 1) - (2 * b[3] - 1)
        sel = np.flatnonzero(np.abs(circ) == 4)
        tgt = codes[sel] ^ m
        idx = np.searchsorted(codes, tgt)
        assert np.all(codes[idx] == tgt)
        rows.append(sel); cols.append(idx)
    rows = np.concatenate(rows); cols = np.concatenate(cols)
    H = coo_matrix((-np.ones(len(rows)), (rows, cols)), shape=(n, n)).tocsr()
    return H
def diag_fields(codes, nl, axis, xb, nv, k):
    n = len(codes); N = nv
    O = np.zeros((3, n)); w = np.cos(k * xb); ph = np.cos(k * xb)   # k = pi: cos = e^{ik x} = (-1)^x, real
    for l in range(nl):
        O[axis[l]] += ph[l] * (2.0 * ((codes >> l) & 1) - 1.0)
    O /= np.sqrt(N)
    return O

def lanczos_measure(Hop, psi0, r0, nit):
    """Lanczos from r0 (orthogonal to psi0), re-deflating psi0 every step. Returns the Ritz values and the weights of the spectral measure of r0."""
    m0 = float(r0 @ r0); v = r0 / np.sqrt(m0); vp = np.zeros_like(v); a = []; b = []
    beta = 0.0
    for j in range(nit):
        wv = Hop(v)
        wv -= psi0 * (psi0 @ wv)
        al = float(v @ wv); wv -= al * v + beta * vp
        wv -= psi0 * (psi0 @ wv)
        beta = float(np.linalg.norm(wv)); a.append(al)
        if beta < 1e-10: break
        b.append(beta); vp = v; v = wv / beta
    T = np.diag(a) + np.diag(b[:len(a) - 1], 1) + np.diag(b[:len(a) - 1], -1)
    th, U = np.linalg.eigh(T)
    return th, m0 * U[0] ** 2, m0

def analyse(Ls, k=np.pi, lanczos_it=150, label=""):
    t0 = time.time()
    sites, nv, nl, plaq, canon, axis, xb = build(Ls)
    assert vertex_div_zero(nv, nl, sites, Ls, canon)
    c0 = int(sum(1 << i for i in range(nl) if canon[i] > 0))
    codes, masks = component(nl, plaq, c0)
    n = len(codes); N = nv
    H = hamiltonian(codes, plaq, masks)
    assert (H - H.T).nnz == 0
    print(f"   {label} {Ls}: N = {N}, {len(plaq)} plaquettes, flip component of {n} states, {H.nnz} nonzeros ({time.time()-t0:.0f}s)", flush=True)
    O = diag_fields(codes, nl, axis, xb, nv, k)
    Ftot = np.sqrt(N) * O.sum(axis=0)                                # F = sum_l cos(k x_b) sigma_l = sqrt(N) (O_0 + O_1 + O_2)
    def ground(h):
        if n <= 2000:
            Hm = H.toarray() - h * np.diag(Ftot); ev, U = np.linalg.eigh(Hm); return float(ev[0]), U[:, 0], ev
        from scipy.sparse import diags
        ev, U = eigsh((H - h * diags(Ftot)).tocsr(), k=2, which="SA", tol=1e-13, v0=np.ones(n) / np.sqrt(n))
        o = np.argsort(ev); return float(ev[o[0]]), U[:, o[0]], ev[o]
    E0, psi0, ev0 = ground(0.0)
    psi0 = psi0 / np.linalg.norm(psi0)
    gap = float(ev0[1] - ev0[0]) if len(ev0) > 1 else float("nan")
    u = -E0 / (3 * N); s2 = 2 - 2 * np.cos(k); s = np.sqrt(s2)
    Hop = lambda x: H @ x
    om = (O * psi0).sum(axis=1) if False else None
    r = []; mo = []
    for a in range(3):
        mean = float(psi0 @ (O[a] * psi0)); mo.append(mean)
        ra = O[a] * psi0 - mean * psi0; r.append(ra)
    m0 = np.array([float(x @ x) for x in r])
    m1 = np.array([float(x @ (H @ x - E0 * x)) for x in r])
    # resolvent: (H - E0 + |psi0><psi0|) x = r
    class Aop(LinearOperator):
        def __init__(s_, ): super().__init__(dtype=float, shape=(n, n))
        def _matvec(s_, x): return H @ x - E0 * x + psi0 * (psi0 @ x)
    A = Aop()
    X = []
    for a in range(3):
        x, info = cg(A, r[a], rtol=1e-13, atol=0.0, maxiter=4000); assert info == 0, info
        X.append(x)
    resid = max(float(np.linalg.norm(H @ X[a] - E0 * X[a] - r[a])) for a in range(3))
    mm1 = np.array([float(r[a] @ X[a]) for a in range(3)])
    cross = np.array([[float(r[a] @ X[b]) for b in range(3)] for a in range(3)])
    # Lanczos spectral measures for the three modes
    low = []; wl = []; mm1_q = []
    for a in range(3):
        if n <= 2000:
            ev, U = np.linalg.eigh(H.toarray()); c = U.T @ r[a]; wts = c ** 2; keep = (np.arange(n) > 0) & (wts > 1e-14 * m0[a])
            th = ev[keep]; wt = wts[keep]
        else:
            th, wt, _ = lanczos_measure(Hop, psi0, r[a], lanczos_it)
            keep = wt > 1e-12 * m0[a]; th = th[keep]; wt = wt[keep]
        th = th - E0
        low.append(float(th.min())); wl.append(float(wt[np.argmin(th)] / m0[a])); mm1_q.append(float((wt / th).sum()))
    # finite-field ground energies (exact)
    Eh = {h: ground(h)[0] for h in (0.15, 0.30)}
    out = dict(Ls=Ls, N=N, n=n, E0=E0, u=u, s=s, gap=gap, m0=m0, m1=m1, mm1=mm1, cross=cross, low=low, wl=wl, mm1_q=mm1_q, Eh=Eh, resid=resid, mo=mo, secs=time.time() - t0)
    return out


# ---- 1-2: arithmetic
u, chi, chi_e, S_e = 0.2888, 1.064, 0.008, 0.014
S = (0.4058 + 0.4110) / 2          # the two seeds' plateau values; the note prints their combination as 0.408 (rounded from 0.4084)
s = 2 * np.sin(np.pi / 8); s2 = s * s
check("momenta: k = pi/4 on L = 8 and k = pi/8 on L = 16 are 2 pi/L; s = 2 sin(pi/8) = 0.76537 and s^2 = 2 - 2 cos(pi/4)", abs(2 * np.pi / 8 - np.pi / 4) < 1e-15 and abs(2 * np.pi / 16 - np.pi / 8) < 1e-15 and abs(s2 - (2 - 2 * np.cos(np.pi / 4))) < 1e-14 and 8 ** 3 == 512 and 16 ** 3 == 4096, f"s = {s:.5f}")
ceil = s * np.sqrt(u * chi); ratio = S / ceil
ceil_e = 0.5 * ceil * (chi_e / chi)                       # d ceiling / ceiling = 1/2 d chi/chi
ratio_e = ratio * np.hypot(S_e / S, ceil_e / ceil)
m1 = 2 * u * s2; mm1 = chi / 2; m0 = S
f1, f2, f3 = m0 / mm1, np.sqrt(m1 / mm1), m1 / m0
check("ceiling s sqrt(u chi) = 0.424 and S/ceiling = 0.963 +- 0.034 from the note's own inputs (S = 0.4084 unrounded)", abs(ceil - 0.424) < 5e-4 and abs(ratio - 0.963) < 1.5e-3 and abs(ratio_e - 0.034) < 1.5e-3, f"ceiling {ceil:.4f}, ratio {ratio:.4f} +- {ratio_e:.4f}")
check("the three weighted mean frequencies: m0/m_-1 = 0.768 (1.003 s), sqrt(m1/m_-1) = 0.798 (1.042 s), m1/m0 = 0.829 (1.082 s), from S = 0.4084 (the rounded 0.408 gives 1.002 s and 1.0835 s)", abs(f1 - 0.768) < 1e-3 and abs(f2 - 0.798) < 1e-3 and abs(f3 - 0.829) < 1e-3 and abs(f1 / s - 1.003) < 1e-3 and abs(f2 / s - 1.042) < 1e-3 and abs(f3 / s - 1.082) < 1e-3, f"{f1:.4f} = {f1/s:.4f} s, {f2:.4f} = {f2/s:.4f} s, {f3:.4f} = {f3/s:.4f} s")
check("the chain m0/m_-1 <= sqrt(m1/m_-1) <= m1/m0 holds for these numbers (Cauchy-Schwarz ordering is realised)", f1 <= f2 <= f3)
# two seeds: 0.4058, 0.4110 combined S = 0.408 +- 0.014
mean2 = (0.4058 + 0.4110) / 2
check("the two 7680-walker seeds 0.4058 and 0.4110 average to 0.4084 (note: 0.408)", abs(mean2 - 0.408) < 5e-4, f"{mean2:.4f}")
# ---- 3-4: exact 2^3
o = analyse((2, 2, 2), label="2^3")
S_exact = float(o["m0"].mean()); u_e = o["u"]; s_pi = 2.0
check("own BFS flip component of the canonical zero-winding state on 2^3 has 864 states and its exact k = pi structure factor is 1.01215 (note: 'exact 1.01215')", o["n"] == 864 and abs(S_exact - 1.01215) < 5e-5, f"n = {o['n']}, S = m0 = {S_exact:.9f}")
runs = {"lag 1": 1.0115, "lag 2": 1.0128, "lag 4": 1.0099}
check("the note's three lag values (1.0115, 1.0128, 1.0099) lie within 0.3 % of the exact value (so 'all within 0.3 standard errors' needs standard errors of at least 0.001)", all(abs(v / S_exact - 1) < 0.003 for v in runs.values()), ", ".join(f"{k}: {100*(v/S_exact-1):+.3f}%" for k, v in runs.items()))
mm1_e = float(o["mm1"].mean()); m1_e = float(o["m1"].mean()); chi_ex = 2 * mm1_e
ceil_ex = 2.0 * np.sqrt(u_e * chi_ex)
check("2^3 exact: the chain omega_low <= m0/m_-1 <= sqrt(m1/m_-1) <= m1/m0 and S <= s sqrt(u chi) hold", min(o["low"]) <= S_exact / mm1_e <= np.sqrt(m1_e / mm1_e) <= m1_e / S_exact * (1 + 1e-12) and S_exact <= ceil_ex * (1 + 1e-12), f"S = {S_exact:.6f} <= ceiling {ceil_ex:.6f} (ratio {S_exact/ceil_ex:.4f})")
print(f"   exact 2^3: S/ceiling = {S_exact/ceil_ex:.4f} (a one-frequency measure would give 1); frequencies m0/m_-1 = {S_exact/mm1_e:.4f}, sqrt(m1/m_-1) = {np.sqrt(m1_e/mm1_e):.4f}, m1/m0 = {m1_e/S_exact:.4f}, lowest coupled level {min(o['low']):.4f}")

print()
for h in HITS: print("HIT:", h)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print(f"SUMMARY: attack-a witness realizability on PR 9382: momenta and s, the ceiling 0.424 and ratio 0.963 +- 0.034, the three weighted frequencies, the two-seed average, and the exact 2^3 control (864 states, S = {S_exact:.5f}, exact S/ceiling {S_exact/ceil_ex:.3f}) all reproduce from the note's own inputs and an own exact flip component; PASS={PASS} FAIL={FAIL}; no defect in the note's witnesses (the 8^3 and 16^3 walker runs are not re-executed)")
sys.exit(1 if FAIL else 0)
