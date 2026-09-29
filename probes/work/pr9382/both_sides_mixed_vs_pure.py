"""PR 9382 attack-b: SAME TEST, BOTH SIDES for the note's separation 'mixed estimate above the moment ceiling, pure (forward-walking) estimate within it'.

The note's claim: on 8^3 (k = pi/4) the landed 120-walker values (0.57, at the level of the mixed estimate, lag 0) exceed the ceiling s sqrt(u chi) = 0.424, while the pure value 0.408 lies within it (ratio 0.963).
The identical test -- 'is the estimate above the Cauchy-Schwarz ceiling?' -- is applied here to BOTH estimators on the exactly solvable 2^3 torus at k = pi (own BFS flip component, exact ground state):
  pure  S = <phi0| O^2 |phi0>  (= m0, the exact value the note quotes as 1.01215),
  mixed <g| O^2 |phi0> / <g|phi0>  with the guide g = exp(lambda N_flip), N_flip = number of flippable plaquettes, lambda = 0, 0.1, 0.2 (the note's), 0.4, 0.8, 1.6,
in every representation the note uses: raw O_a^2 and connected (O_a - <O_a>)^2, per mode and averaged over the cyclic triple, and against the ceiling s sqrt(u chi) computed from the exact u and chi = 2 m_-1.
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


Ls = (2, 2, 2); k = np.pi
sites, nv, nl, plaq, canon, axis, xb = build(Ls)
c0 = int(sum(1 << i for i in range(nl) if canon[i] > 0))
codes, masks = component(nl, plaq, c0); n = len(codes); N = nv
H = hamiltonian(codes, plaq, masks).toarray()
ev, U = np.linalg.eigh(H); E0 = float(ev[0]); phi = U[:, 0] * np.sign(U[:, 0].sum())
O = diag_fields(codes, nl, axis, xb, nv, k)                 # (3, n), diagonal in the sigma basis
# flippable plaquettes per state
nflip = np.zeros(n)
for p in plaq:
    b = [(codes >> int(l)) & 1 for l in p]
    circ = (2 * b[0] - 1) + (2 * b[1] - 1) - (2 * b[2] - 1) - (2 * b[3] - 1)
    nflip += (np.abs(circ) == 4)
mean_pure = np.array([float((phi * phi) @ O[a]) for a in range(3)])
raw_pure = np.array([float((phi * phi) @ (O[a] ** 2)) for a in range(3)])
conn_pure = raw_pure - mean_pure ** 2
u = -E0 / (3 * N); s = 2.0
# chi = 2 m_-1 exactly
r = [O[a] * phi - mean_pure[a] * phi for a in range(3)]
Xs = []
for a in range(3):
    A = H - E0 * np.eye(n) + np.outer(phi, phi); Xs.append(np.linalg.solve(A, r[a]))
mm1 = float(np.mean([r[a] @ Xs[a] for a in range(3)])); chi = 2 * mm1
ceil = s * np.sqrt(u * chi)
print(f"exact 2^3: N_flip range {nflip.min():.0f}..{nflip.max():.0f}; <O_a> = {np.round(mean_pure, 12)}; pure S per mode {np.round(conn_pure, 6)}, mean {conn_pure.mean():.9f}; u = {u:.6f}; chi = {chi:.6f}; ceiling s sqrt(u chi) = {ceil:.6f}")
check("pure: the exact S = m0 is 1.012148 (the note's exact control) and lies below the ceiling (ratio < 1)", abs(conn_pure.mean() - 1.012148) < 5e-6 and conn_pure.mean() < ceil, f"S/ceiling = {conn_pure.mean()/ceil:.4f}")
rows = []
print("   lambda   mixed raw (mean of 3)   mixed connected   mixed/pure   mixed/ceiling")
for lam in (0.0, 0.1, 0.2, 0.4, 0.8, 1.6):
    g = np.exp(lam * nflip); w = g * phi; Z = w.sum()
    raw = np.array([float(w @ (O[a] ** 2)) / Z for a in range(3)])
    mean = np.array([float(w @ O[a]) / Z for a in range(3)])
    conn = raw - mean ** 2
    rows.append((lam, raw.mean(), conn.mean()))
    print(f"   {lam:5.1f}    {raw.mean():14.6f}      {conn.mean():14.6f}   {conn.mean()/conn_pure.mean():9.4f}   {conn.mean()/ceil:9.4f}")
lam2 = [r for r in rows if r[0] == 0.2][0]
above = [r for r in rows if r[2] > ceil * (1 + 1e-12)]
check("the same test on the exact 2^3 torus: the mixed estimate with the note's guide (lambda = 0.2) is within 10 % of the pure value and below the ceiling (it does not exceed the moment bound there)", abs(lam2[2] / conn_pure.mean() - 1) < 0.10 and lam2[2] < ceil, f"mixed {lam2[2]:.5f}, pure {conn_pure.mean():.5f}, ceiling {ceil:.5f}")
print(f"   guides for which the mixed estimate exceeds the exact ceiling on 2^3: {[r[0] for r in above] if above else 'none'}")
# the mixed-minus-pure difference and its sign as a function of lambda
diffs = [(r[0], r[2] - conn_pure.mean()) for r in rows]
print("   mixed - pure by guide strength:", ", ".join(f"lambda {l}: {d:+.5f}" for l, d in diffs))
# the same test on the mixed estimate of the ENERGY (a quantity where mixed and pure are both known): mixed energy and the ground energy
g = np.exp(0.2 * nflip); Emixed = float((g * phi) @ (H @ np.ones(n)) / ((g * phi).sum()))
print(f"   for scale: 'mixed' energy with the same guide, sum_x H(x, .) contracted as <g|H|phi0>/<g|phi0> = {float(g @ (H @ phi) / (g @ phi)):.6f} = E0 = {E0:.6f} (exact for an eigenvector: the mixed estimator is exact for observables that commute with H)")
check("the mixed estimator is exact for the Hamiltonian itself (<g|H|phi0>/<g|phi0> = E0), so the mixed/pure split is specific to observables that do not commute with H such as O_a^2", abs(float(g @ (H @ phi) / (g @ phi)) - E0) < 1e-10)
print()
for h in HITS: print("HIT:", h)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print(f"SUMMARY: attack-b same test both sides on PR 9382: on the exact 2^3 torus (k = pi) the pure S = {conn_pure.mean():.5f} lies at {conn_pure.mean()/ceil:.3f} of the ceiling {ceil:.4f}; the mixed estimate with the note's guide (lambda 0.2) is {lam2[2]:.5f} ({lam2[2]/conn_pure.mean():.3f} x pure, {lam2[2]/ceil:.3f} x ceiling) and exceeds the ceiling for lambda in {[r[0] for r in above] if above else 'none'}; the note's 8^3 statement (mixed 0.565-0.574 above the 0.424 ceiling, pure 0.408 within) is therefore size-specific rather than a general property of the mixed estimator; PASS={PASS} FAIL={FAIL}; no defect (the note claims it for 8^3 only)")
sys.exit(1 if FAIL else 0)
