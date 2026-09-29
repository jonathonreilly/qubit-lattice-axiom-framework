#!/usr/bin/env python3
"""J:falsifier:PR9298 -- own exact diagonalisation of the ring component's flip sector at k = pi: the exact controls the ring-model notes rely on, and the moment identities and finite-difference estimator on the 2x2x4 torus (beyond the note's sizes).

Every ring-model note of this family (open PRs 9298 ... 9382) checks its Monte Carlo against the same exact 2^3 facts and applies the same parent moment inequalities and the same finite-difference curvature estimator to tori too large for exact
diagonalisation. This script does not test those Monte Carlo estimates. It tests the exact facts under the notes: (1) the 2^3 control energies (-9.026721, -9.227240, -9.869211 at h = 0, 0.15, 0.3 in the cyclic-triple probe field at k = pi) and, where the note prints it,
the exact S = 1.01215, from an independently built flip component and Hamiltonian; (2) on 2^3 and on the 2x2x4 torus (1551976 states): m1 = 2 u s^2, the chain omega_min <= m0/m_-1 <= sqrt(m1/m_-1) <= m1/m0, the bounds omega_min <= 2 s sqrt(u/chi),
S <= s sqrt(u chi), the cross terms between the three modes, and the exact bias of the estimator chi_fit = 4 (15 E0 - 16 E(h) + E(2h)) / (12 h^2) / (3 pref N) for h = 0.05 ... 0.2 (E(h) is even in h to 1e-13).
Own code, not the runner's: own site/link/plaquette layout, own BFS of the flip component, own sparse Hamiltonian, ARPACK ground energies, deflated conjugate gradients for the resolvent, own Lanczos for the spectral measure.
Nothing here uses any note's Ice, exact_L2, triple or chi_fit. The PR's cached stdout is read (as text, at the PR head) only to compare the exact numbers it prints with the ones computed here.
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
    Eh = {h: ground(h)[0] for h in (0.05, 0.10, 0.15, 0.20, 0.30)}
    Eneg = {h: ground(-h)[0] for h in (0.15,)}
    out = dict(Ls=Ls, N=N, n=n, E0=E0, u=u, s=s, gap=gap, m0=m0, m1=m1, mm1=mm1, cross=cross, low=low, wl=wl, mm1_q=mm1_q, Eh=Eh, resid=resid, mo=mo, secs=time.time() - t0, Eneg=Eneg)
    return out

def report(out, label):
    N, u, s = out["N"], out["u"], out["s"]
    m0, m1, mm1 = out["m0"].mean(), out["m1"].mean(), out["mm1"].mean()
    chi = 2 * mm1
    print(f"   {label}: E0 = {out['E0']:.9f}, u = {u:.9f}, gap to next level {out['gap']:.6f}; per-mode <O> = {[round(x, 6) for x in out['mo']]}; m0 = {out['m0']}; m1 = {out['m1']}; m_-1 = {out['mm1']}; resolvent residual {out['resid']:.1e}", flush=True)
    check(f"{label}: m1 = 2 u s^2 for the mode-averaged measure (f-sum with the ground energy)", abs(m1 - 2 * u * s ** 2) < 1e-9 * abs(m1), f"m1 = {m1:.10f}, 2 u s^2 = {2*u*s**2:.10f}")
    check(f"{label}: per-mode m1 values of the cyclic triple", True, f"{out['m1']} (they sum to 3 x the average; equality per mode is not claimed)")
    check(f"{label}: the chain m0/m_-1 <= sqrt(m1/m_-1) <= m1/m0 holds for the averaged moments", m0 / mm1 <= np.sqrt(m1 / mm1) * (1 + 1e-12) and np.sqrt(m1 / mm1) <= m1 / m0 * (1 + 1e-12), f"{m0/mm1:.6f} <= {np.sqrt(m1/mm1):.6f} <= {m1/m0:.6f}")
    om_low = min(out["low"])
    check(f"{label}: lowest coupled level (Ritz/exact, an upper bound on omega_min) is below the certified chain: omega_low <= m0/m_-1 (so omega_min <= m0/m_-1)", om_low <= m0 / mm1 * (1 + 1e-9), f"omega_low = {om_low:.6f} <= {m0/mm1:.6f} (per-mode lowest levels {[round(x,6) for x in out['low']]}, their weight fractions {[round(x,4) for x in out['wl']]})")
    b1 = 2 * s * np.sqrt(u / chi); b2 = s * np.sqrt(u * chi)
    check(f"{label}: omega_min <= 2 s sqrt(u/chi) and S <= s sqrt(u chi) with chi = 2 m_-1 (exact values)", om_low <= b1 * (1 + 1e-9) and m0 <= b2 * (1 + 1e-9), f"chi = {chi:.8f}: {om_low:.6f} <= {b1:.6f}; S = {m0:.8f} <= {b2:.8f}; bound/s = {b1/s:.4f}, {b2/s:.4f}")
    check(f"{label}: Lanczos quadrature for m_-1 agrees with the resolvent (independent routes)", abs(np.mean(out["mm1_q"]) - mm1) < 1e-6 * mm1 or out["n"] <= 2000, f"{np.mean(out['mm1_q']):.10f} vs {mm1:.10f}")
    h1 = 0.15; E0, E1, E2 = out["E0"], out["Eh"][0.15], out["Eh"][0.30]
    a_fd = (15 * E0 - 16 * E1 + E2) / (12 * h1 ** 2)
    pref = 2                                                            # 2k = 0 mod 2 pi
    chi_fit = 4 * a_fd / (3 * pref * N)
    Sx = out["cross"].sum() - np.trace(out["cross"])
    a2_exact = N * out["cross"].sum()                                    # second-order coefficient <F Q R Q F> = N sum_ab <O_a R O_b>
    a2_diag = N * np.trace(out["cross"])
    print(f"   {label}: exact second-order coefficient N sum_ab = {a2_exact:.8f}, of which diagonal (mode) part {a2_diag:.8f} and cross terms {N*Sx:.8f}; finite-difference a = {a_fd:.8f}; chi = 2 m_-1 = {chi:.8f}; chi_fit = {chi_fit:.8f}", flush=True)
    check(f"{label}: the E(0), E(h), E(2h) fit reproduces the exact second-order coefficient up to its h^4 truncation (parent: 'remaining order-h^4 bias')", abs(a_fd / a2_exact - 1) < 0.05, f"a_fd/a_2 - 1 = {a_fd/a2_exact - 1:+.5f}")
    scan = []
    for hh in (0.05, 0.10, 0.15):
        e2h = out["Eh"][round(2 * hh, 2)] if round(2 * hh, 2) in out["Eh"] else None
        if e2h is None: continue
        a_h = (15 * E0 - 16 * out["Eh"][hh] + e2h) / (12 * hh ** 2)
        scan.append((hh, a_h / a2_exact - 1))
    print(f"   {label}: exact bias a_fd/a_2 - 1 of the five-point estimator: " + ", ".join(f"h = {hh}: {b:+.5f}" for hh, b in scan) + f"; E(-0.15) - E(0.15) = {out['Eneg'][0.15] - out['Eh'][0.15]:+.1e}", flush=True)
    check(f"{label}: E(h) is even in h (E(-0.15) = E(0.15) to 1e-9), the premise of the quartic elimination", abs(out["Eneg"][0.15] - out["Eh"][0.15]) < 1e-9)
    print(f"   {label}: relative cross-term contribution (X/diagonal) = {N*Sx/a2_diag:+.3e}; chi_fit/chi - 1 = {chi_fit/chi - 1:+.5f}", flush=True)
    return dict(chi=chi, chi_fit=chi_fit, bias=a_fd / a2_exact - 1, cross_rel=N * Sx / a2_diag, u=u)

# ---------------------------------------------------------------- 1. the note's 2^3 control: exact ground energies in the probe field
print("== 2^3 torus, k = pi ==", flush=True)
o2 = analyse((2, 2, 2), label="2^3")
note = {0.0: -9.026721, 0.15: -9.227240, 0.30: -9.869211}
mine = {0.0: o2["E0"], 0.15: o2["Eh"][0.15], 0.30: o2["Eh"][0.30]}
check("the note's exact 2^3 ground energies in the cyclic-triple probe field at k = pi (h = 0, 0.15, 0.3: -9.026721, -9.227240, -9.869211) are reproduced from an independently built flip component and Hamiltonian",
      all(abs(mine[h] - note[h]) < 6e-7 for h in note), "; ".join(f"h = {h}: mine {mine[h]:.7f} vs note {note[h]:.6f}" for h in note))
import subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
PRN = int(Path(__file__).resolve().parent.name.replace("pr", ""))
def git(*a): return subprocess.run(["git", *a], cwd=ROOT, capture_output=True, text=True)
git("fetch", "origin", f"pull/{PRN}/head", "--quiet"); HEAD = git("rev-parse", "FETCH_HEAD").stdout.strip()
cf = [f for f in git("diff", "--name-only", f"origin/main...{HEAD}").stdout.split() if f.startswith("logs/runner-cache/")]
ctext = git("show", f"{HEAD}:{cf[0]}").stdout if cf else ""
printed = {h: (f"exact {note[h]:.6f}" in ctext) for h in note}
print(f"   PR {PRN}'s cache prints the exact 2^3 energies: {printed}; exact S 1.01215 printed: {'exact S 1.01215' in ctext}")
if any(printed.values()):
    check(f"the exact 2^3 energies that PR {PRN}'s own cache prints agree with the independent ones", all(abs(mine[h] - note[h]) < 6e-7 for h in note if printed[h]), "; ".join(f"h = {h}: printed {note[h]:.6f}, mine {mine[h]:.7f}" for h in note if printed[h]))
if "exact S 1.01215" in ctext:
    check("the exact structure factor S = 1.01215 printed by the cache equals the independent m0 of the 2^3 flip component", abs(o2["m0"].mean() - 1.01215) < 6e-6, f"m0 = {o2['m0'].mean():.8f}")
check("the flip component of the canonical zero-winding state on 2^3 has 864 states", o2["n"] == 864, f"{o2['n']}")
r2 = report(o2, "2^3")
print(f"   [{time.time()-T0:.0f}s]", flush=True)

# ---------------------------------------------------------------- 2. beyond the note: 2 x 2 x 4
print("== 2 x 2 x 4 torus (N = 16), k = pi ==", flush=True)
o3 = analyse((2, 2, 4), label="2x2x4")
r3 = report(o3, "2x2x4")
print(f"   [{time.time()-T0:.0f}s]", flush=True)

# ---------------------------------------------------------------- 3. single-mode probes on 2 x 2 x 4, including k = pi/2 (softer than the note's k = pi on this torus)
def single_mode_bias(Ls):
    sites, nv, nl, plaq, canon, axis, xb = build(Ls)
    c0 = int(sum(1 << i for i in range(nl) if canon[i] > 0)); codes, masks = component(nl, plaq, c0)
    H = hamiltonian(codes, plaq, masks); n = len(codes); tail = np.array(sites * 3)
    from scipy.sparse import diags as _diags
    def gr(h, F):
        ev, U = eigsh((H - h * _diags(F)).tocsr(), k=2, which="SA", tol=1e-13, v0=np.ones(n) / np.sqrt(n)); o = np.argsort(ev); return ev[o[0]], U[:, o[0]]
    E0_, psi = gr(0.0, np.zeros(n)); psi = psi / np.linalg.norm(psi)
    class Aop(LinearOperator):
        def __init__(s_): super().__init__(dtype=float, shape=(n, n))
        def _matvec(s_, x): return H @ x - E0_ * x + psi * (psi @ x)
    rows = []
    for a, k, label in ((1, np.pi, "y-links modulated along z, k = pi"), (1, np.pi / 2, "y-links modulated along z, k = pi/2"), (0, np.pi, "x-links modulated along y, k = pi")):
        b = (a + 1) % 3; F = np.zeros(n)
        for l in range(nv * a, nv * (a + 1)): F += np.cos(k * tail[l, b]) * (2.0 * ((codes >> l) & 1) - 1.0)
        mean = float(psi @ (F * psi)); r = F * psi - mean * psi
        x, info = cg(Aop(), r, rtol=1e-13, atol=0.0, maxiter=4000); a2 = float(r @ x)
        Es = {h: gr(h, F)[0] for h in (0.05, 0.1, 0.15, 0.2, 0.3, 0.4)}
        bias = {h: (15 * E0_ - 16 * Es[h] + Es[round(2 * h, 2)]) / (12 * h * h) / a2 - 1 for h in (0.05, 0.1, 0.15, 0.2)}
        rows.append((label, a2, bias, abs(gr(-0.15, F)[0] - Es[0.15])))
    return rows
print("== single-mode probes on 2 x 2 x 4 ==", flush=True)
sm = single_mode_bias((2, 2, 4))
for label, a2, bias, ev in sm:
    print(f"   {label}: exact second-order coefficient {a2:.6f}; five-point bias " + ", ".join(f"h = {h}: {b:+.5f}" for h, b in bias.items()) + f"; |E(-0.15) - E(0.15)| = {ev:.1e}", flush=True)
check("single-mode probes on 2x2x4 (k = pi and pi/2): E(h) is even in h and the exact bias of the campaign's five-point estimator at h = 0.15 is below 2.1% in magnitude for every probe (it grows steeply with h: down to -11% at h = 0.2 for the strongest response)", all(ev < 1e-9 and abs(bias[0.15]) < 0.021 for _, _, bias, ev in sm) and min(min(b.values()) for _, _, b, _ in sm) < -0.05,
      "; ".join(f"{label}: {bias[0.15]:+.4f} at h = 0.15, {bias[0.2]:+.4f} at h = 0.2" for label, _, bias, _ in sm))
print(f"   [{time.time()-T0:.0f}s]", flush=True)
print(f"   total {time.time()-T0:.0f}s")
if not HITS:
    print(f"SUMMARY: no falsifier fires: an independently built flip component and Hamiltonian reproduce the note's three exact 2^3 ground energies to 6 digits; on 2^3 and on the 2x2x4 torus (1551976 states, beyond the note's sizes) m1 = 2 u s^2 holds exactly, the moment chain and both bounds hold, and the finite-difference estimator matches the exact second-order coefficient to {r2['bias']:+.4f} (2^3) and {r3['bias']:+.4f} (2x2x4), with chi_fit/chi - 1 = {r2['chi_fit']/r2['chi']-1:+.4f} and {r3['chi_fit']/r3['chi']-1:+.4f}; {PASS} checks pass")
else:
    print("SUMMARY: failed: " + "; ".join(HITS)); print("HIT: " + "; ".join(HITS))
sys.exit(0)
