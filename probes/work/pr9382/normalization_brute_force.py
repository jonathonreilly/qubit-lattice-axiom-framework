"""PR 9382 attack-f: NORMALIZATION factors of the moment identities and of the curvature estimator, recomputed by brute force on the exactly solvable 2^3 torus (k = pi, 864-state flip component).

Note/parents: O_a = N^{-1/2} sum_(a-links) e^{ik x_(a+1)} sigma (real at k = pi); u = -E0/(3N); s^2 = 2 - 2 cos k; m1 = 2 u s^2 (f-sum), chi = 2 m_-1, S = m0; the chain
omega_min <= m0/m_-1 <= sqrt(m1/m_-1) <= m1/m0 and the ceiling S <= s sqrt(u chi); the probe field F = sum_links cos(k x_b) sigma = sqrt(N) (O_0 + O_1 + O_2) with the three-field stencil
chi_fit = 4 (15 E0 - 16 E(h) + E(2h))/(12 h^2)/(3 pref N), pref = 2 at 2k = 0 mod 2 pi (1 otherwise).
Each convention is varied in turn (N^-1/2 -> N^-1, u -> -E0/N, chi -> m_-1, pref -> 1, F -> the single mode) and the exact numbers show which choice reproduces the identities to rounding.
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


o = analyse((2, 2, 2), label="2^3")
N = o["N"]; s = o["s"]; u = o["u"]; E0 = o["E0"]
m0, m1, mm1 = o["m0"], o["m1"], o["mm1"]
print(f"exact 2^3 (k = pi): N = {N}, E0 = {E0:.9f}, u = -E0/(3N) = {u:.9f}, s^2 = {s**2:.6f}; m0 per mode {m0}; m1 per mode {m1}; m_-1 per mode {mm1}")
# (i) O normalisation
check("the exact S = m0 = 1.01215 needs O_a = N^{-1/2} sum ...: with N^{-1} the structure factor would be m0/N = 0.12652, with (N/3)^{-1/2} it would be 3 m0",
      abs(m0.mean() - 1.012148) < 5e-6 and abs(m0.mean() / N - 0.12652) < 1e-4, f"m0 = {m0.mean():.9f}; m0/N = {m0.mean()/N:.6f}; 3 m0 = {3*m0.mean():.6f}")
# (ii) f-sum with u = -E0/(3N)
m1a = float(m1.mean())
alts = {"u = -E0/(3N) (note)": 2 * u * s ** 2, "u = -E0/N": 2 * (-E0 / N) * s ** 2, "u = -E0/(3N), m1 = u s^2": u * s ** 2, "u = -E0/(3N), s^2 = 4 sin^2(k) ": 2 * u * (4 * np.sin(np.pi) ** 2)}
for nm, val in alts.items(): print(f"   f-sum candidates: {nm:40s} -> m1 = {val:.9f} (exact {m1a:.9f})")
check("m1 = 2 u s^2 with u = -E0/(3N) and s^2 = 2 - 2 cos k reproduces the exact mode-averaged first moment to 1e-9 and the alternatives do not", abs(alts["u = -E0/(3N) (note)"] - m1a) < 1e-9 * m1a and all(abs(v - m1a) > 1e-3 * m1a for k_, v in alts.items() if k_ != "u = -E0/(3N) (note)"), f"{m1a:.10f} vs {alts['u = -E0/(3N) (note)']:.10f}")
# (iii) chi and the second-order coefficient
mm1a = float(mm1.mean()); chi = 2 * mm1a
a2 = N * float(o["cross"].sum()); cross_off = N * (float(o["cross"].sum()) - float(np.trace(o["cross"])))
print(f"   second-order coefficient a2 = N sum_ab <O_a R O_b> = {a2:.9f} (diagonal part {N*np.trace(o['cross']):.9f}, cross terms {cross_off:.2e}); 3 N m_-1 = {3*N*mm1a:.9f}; 3 pref N chi / 4 = {3*2*N*chi/4:.9f} (pref 2), {3*1*N*chi/4:.9f} (pref 1)")
check("with the cyclic triple probe F = sqrt(N) (O_0 + O_1 + O_2): a2 = 3 N m_-1 = 3 pref N chi/4 with pref = 2 and chi = 2 m_-1 exactly (cross terms vanish); pref = 1 or chi = m_-1 would break it by a factor 2",
      abs(a2 - 3 * N * mm1a) < 1e-9 * a2 and abs(a2 - 3 * 2 * N * chi / 4) < 1e-9 * a2 and abs(a2 - 3 * 1 * N * chi / 4) > 0.4 * a2 and abs(cross_off) < 1e-9 * a2, f"{a2:.9f}")
# (iv) finite-difference stencil with h = 0.15
E1, E2 = o["Eh"][0.15], o["Eh"][0.30]; h = 0.15
a_fd = (15 * E0 - 16 * E1 + E2) / (12 * h ** 2); chi_fit = 4 * a_fd / (3 * 2 * N)
print(f"   stencil at h = 0.15: a_fd = {a_fd:.9f} (exact a2 {a2:.9f}, ratio {a_fd/a2:.6f}); chi_fit = {chi_fit:.8f} vs chi = {chi:.8f} (ratio {chi_fit/chi:.6f}); with pref = 1: chi_fit = {4*a_fd/(3*1*N):.8f}")
check("chi_fit = 4 a_fd / (3 pref N) with pref = 2 lands within 3 % of the exact chi = 2 m_-1 on 2^3 at h = 0.15 (the residual is the h^4 bias); pref = 1 is off by a factor 2", abs(chi_fit / chi - 1) < 0.03 and abs(4 * a_fd / (3 * 1 * N) / chi - 2) < 0.06, f"{chi_fit/chi - 1:+.5f}")
# (v) ceiling algebra
b1 = 2 * s * np.sqrt(u / chi); b2 = s * np.sqrt(u * chi)
alg = np.sqrt(m1a * mm1a)
check("ceiling algebra: sqrt(m1 m_-1) = s sqrt(u chi) and sqrt(m1/m_-1) = 2 s sqrt(u/chi) exactly for m1 = 2 u s^2, m_-1 = chi/2", abs(alg - b2) < 1e-9 * b2 and abs(np.sqrt(m1a / mm1a) - b1) < 1e-9 * b1, f"{alg:.9f} vs {b2:.9f}; {np.sqrt(m1a/mm1a):.9f} vs {b1:.9f}")
# (vi) single-mode probe vs triple
print(f"   single-mode probe F = sqrt(N) O_0 would give a2_single = N <O_0 R O_0> = {N*float(o['cross'][0,0]):.9f} = a2/3 (pref of the single probe is 2 x (1/3)) ")
check("a single-mode probe has second-order coefficient a2/3 (so its estimator needs A = pref N chi/4, not 3 pref N chi/4)", abs(N * float(o["cross"][0, 0]) - a2 / 3) < 1e-9 * a2)

print()
for h_ in HITS: print("HIT:", h_)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print(f"SUMMARY: attack-f normalization on PR 9382 (exact 2^3, k = pi): O_a = N^-1/2 gives S = {m0.mean():.5f}; m1 = 2 u s^2 with u = -E0/(3N) matches the exact first moment ({m1a:.6f}) and the tried alternatives do not; a2 = 3 N m_-1 = 3 pref N chi/4 with pref = 2, chi = 2 m_-1 (cross terms {cross_off:.0e}); stencil chi_fit/chi = {chi_fit/chi:.4f} at h = 0.15; ceiling algebra exact; single-mode probe is a2/3; PASS={PASS} FAIL={FAIL}; no defect in the note's normalizations")
sys.exit(1 if FAIL else 0)
