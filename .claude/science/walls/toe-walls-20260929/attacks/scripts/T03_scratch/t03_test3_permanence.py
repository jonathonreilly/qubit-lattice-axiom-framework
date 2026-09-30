"""T03 Test 3: the count horn (escape 3: statistical permanence), Bell jump process on a unitary wave.

3a  atom + semi-infinite chain, one excitation (a special, stored-excitation initial state).
3b  translation-invariant formation term on a ring (no source): per-record destruction rate versus size.
Pre-registered in PREREGISTRATION.md.  Usage: python3 t03_test3_permanence.py [3a|3b]
"""
import math, sys, time
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import expm_multiply

rng = np.random.default_rng(20260929)
PASS = FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        print(f"[PASS] {name} {detail}", flush=True)
    else:
        FAIL += 1
        print(f"[FAIL] {name} {detail}", flush=True)


# ----------------------------------------------------------------------------- 3a
def chain_H(n, g):
    H = np.zeros((n + 1, n + 1))
    H[0, 1] = H[1, 0] = g
    for j in range(1, n):
        H[j, j + 1] = H[j + 1, j] = -1.0
    return H


def bell_chain(n, g, psi0, T, dt, M, label, checkpoints):
    H = chain_H(n, g)
    E, V = np.linalg.eigh(H)
    c0 = V.T @ psi0
    N1 = n + 1
    steps = int(round(T / dt))
    # initial positions sampled from |psi0|^2 (equivariance)
    p0 = np.abs(psi0) ** 2
    pos = rng.choice(N1, size=M, p=p0 / p0.sum())
    in_chain0 = pos >= 1
    fell = np.zeros(M, bool)
    nfalls = np.zeros(M, int)
    caps = 0
    Hlow = np.zeros(N1)   # H[j,j-1]   (left neighbour amplitude of j) -> H[j-1,j]
    Hup = np.zeros(N1)
    for j in range(N1 - 1):
        Hup[j] = H[j + 1, j]      # amplitude linking j to j+1
    for j in range(1, N1):
        Hlow[j] = H[j - 1, j]     # amplitude linking j to j-1
    results = {}
    chk = set(int(round(t / dt)) for t in checkpoints)
    rec = []
    for s in range(steps):
        t_mid = (s + 0.5) * dt
        psi = V @ (np.exp(-1j * E * t_mid) * c0)
        a = np.abs(psi) ** 2
        # inflow to k from j: f = 2 H[k,j] Im(conj(psi_k) psi_j)
        rr = np.zeros(N1)
        rl = np.zeros(N1)
        # right jump j -> j+1
        f = 2 * Hup[:-1] * np.imag(np.conj(psi[1:]) * psi[:-1])
        rr[:-1] = np.maximum(f, 0) / np.maximum(a[:-1], 1e-300)
        # left jump j -> j-1
        f2 = 2 * Hlow[1:] * np.imag(np.conj(psi[:-1]) * psi[1:])
        rl[1:] = np.maximum(f2, 0) / np.maximum(a[1:], 1e-300)
        tot = (rr + rl)[pos] * dt
        caps += int((tot > 1).sum())
        u = rng.random(M)
        pr = rr[pos] * dt
        pl = rl[pos] * dt
        right = u < pr
        left = (~right) & (u < pr + pl)
        newpos = pos + right.astype(int) - left.astype(int)
        fall = (pos == 1) & (newpos == 0)
        fell |= fall
        nfalls += fall
        pos = newpos
        if (s + 1) in chk:
            tt = (s + 1) * dt
            rec.append((tt, float((pos >= 1).mean()), float(fell.mean()), float(nfalls.mean()),
                        float((np.abs(V @ (np.exp(-1j * E * tt) * c0)) ** 2)[0]), float((pos == 0).mean())))
    print(f"--- {label}: n={n}, g={g}, M={M}, dt={dt}, steps where jump prob exceeded 1: {caps}", flush=True)
    print("   t     P(in chain)  P(ever fell)  mean #falls  |psi_atom|^2  P(bell at atom)", flush=True)
    for r in rec:
        print(f"{r[0]:6.0f}   {r[1]:9.4f}   {r[2]:10.4f}   {r[3]:9.4f}   {r[4]:10.4f}   {r[5]:9.4f}", flush=True)
    return rec, caps


def run_3a():
    n = 400
    T = 700.0
    cps = [20, 40, 60, 100, 200, 300, 400, 500, 600, 700]
    psi0 = np.zeros(n + 1); psi0[0] = 1.0
    rec_w, caps_w = bell_chain(n, 0.2, psi0, T, 0.05, 3000, "3a weak coupling, atom excited", cps)
    d = {int(r[0]): r for r in rec_w}
    check("3a formed: P(excitation in chain at t=60) >= 0.95", d[60][1] >= 0.95, f"({d[60][1]:.4f})")
    check("3a permanent while the reservoir is far: P(ever fell by t=100) <= 0.05", d[100][2] <= 0.05, f"({d[100][2]:.4f})")
    check("3a recurrence recovers T1: P(ever fell by t=700) >= 0.3 (finite system)", d[700][2] >= 0.3, f"({d[700][2]:.4f})")
    check("3a equivariance sanity: Bell occupation of the atom tracks |psi_atom|^2 at t=20 (0.03)", abs(d[20][5] - d[20][4]) < 0.03, f"({d[20][5]:.4f} vs {d[20][4]:.4f})")
    # strong coupling contrast
    rec_s, _ = bell_chain(n, 1.0, psi0, 150.0, 0.05, 2000, "3a contrast: strong coupling g = 1", [20, 40, 60, 100, 150])
    ds = {int(r[0]): r for r in rec_s}
    print(f"   contrast: P(ever fell by t=100) weak = {d[100][2]:.4f}, strong = {ds[100][2]:.4f}", flush=True)
    # inbound control: gaussian packet arriving at the atom
    j = np.arange(1, n + 1)
    sig = 15.0; j0 = 150.0; k0 = -math.pi / 2
    packet = np.exp(-((j - j0) ** 2) / (4 * sig**2)) * np.exp(1j * k0 * j)
    psi_in = np.zeros(n + 1, complex); psi_in[1:] = packet
    psi_in /= np.linalg.norm(psi_in)

    # complex psi0: reuse routine with complex vector
    rec_i, _ = bell_chain_c(n, 0.5, psi_in, 260.0, 0.05, 2000, "3a control: inbound packet, g = 0.5", [50, 100, 150, 200, 260])
    di = {int(r[0]): r for r in rec_i}
    check("3a control: from an inbound state the count falls (P(ever fell by t=260) >= 0.5): monotone only for special psi", di[260][2] >= 0.5, f"({di[260][2]:.4f})")


def bell_chain_c(n, g, psi0, T, dt, M, label, checkpoints):
    # same as bell_chain, complex initial state
    return bell_chain(n, g, psi0.astype(complex), T, dt, M, label, checkpoints)


# ----------------------------------------------------------------------------- 3b
def ring_setup(L, gform):
    D = 1 << L
    rows, cols, vals = [], [], []
    nb = -np.ones((D, 2 * L), int)
    val = np.zeros((D, 2 * L))
    typ = np.zeros((D, 2 * L), int)  # 0 hop, 1 create, 2 destroy
    for c in range(D):
        for i in range(L):
            # hop between i and i+1
            j = (i + 1) % L
            bi = (c >> i) & 1; bj = (c >> j) & 1
            if bi != bj:
                c2 = c ^ (1 << i) ^ (1 << j)
                nb[c, i] = c2; val[c, i] = -1.0; typ[c, i] = 0
                rows.append(c2); cols.append(c); vals.append(-1.0)
            # formation flip at i
            c3 = c ^ (1 << i)
            nb[c, L + i] = c3; val[c, L + i] = gform
            typ[c, L + i] = 1 if bi == 0 else 2
            rows.append(c3); cols.append(c); vals.append(gform)
    H = sp.csr_matrix((vals, (rows, cols)), shape=(D, D), dtype=float)
    return H, nb, val, typ


def run_ring(L, gform, T, dt, M, groups=4):
    H, nb, val, typ = ring_setup(L, gform)
    D = 1 << L
    psi0 = np.zeros(D, complex); psi0[0] = 1.0
    steps = int(round(T / dt))
    A = -1j * H
    # psi at mid steps
    psis = expm_multiply(A, psi0, start=dt / 2, stop=dt / 2 + (steps - 1) * dt, num=steps, endpoint=True)
    cur = np.zeros(M, int)
    popc = np.array([bin(i).count("1") for i in range(D)])
    t_lo, t_hi = 30.0, T
    rec_time = np.zeros(groups); emp_time = np.zeros(groups); ndes = np.zeros(groups); ncre = np.zeros(groups)
    gid = np.arange(M) % groups
    Nmean = []
    caps = 0
    for s in range(steps):
        psi = psis[s]
        a = np.abs(psi) ** 2
        nbc = nb[cur]               # (M, 2L)
        valid = nbc >= 0
        nbi = np.where(valid, nbc, 0)
        f = 2 * val[cur] * np.imag(np.conj(psi[nbi]) * psi[cur][:, None])
        rate = np.where(valid, np.maximum(f, 0), 0.0) / np.maximum(a[cur], 1e-300)[:, None]
        cum = np.cumsum(rate, axis=1) * dt
        tot = cum[:, -1]
        caps += int((tot > 1).sum())
        u = rng.random(M)
        jump = u < tot
        k = np.argmax(cum >= u[:, None], axis=1)
        tt = (s + 0.5) * dt
        Nc = popc[cur]
        if tt >= t_lo:
            rec_time += np.bincount(gid, weights=Nc * dt, minlength=groups)
            emp_time += np.bincount(gid, weights=(L - Nc) * dt, minlength=groups)
            Nmean.append(Nc.mean())
            js = np.where(jump)[0]
            tk = typ[cur[js], k[js]]
            ndes += np.bincount(gid[js][tk == 2], minlength=groups)
            ncre += np.bincount(gid[js][tk == 1], minlength=groups)
        newc = np.where(jump, nb[cur, k], cur)
        cur = newc
    rho = np.mean(Nmean) / L
    rd_g = ndes / rec_time
    rc_g = ncre / emp_time
    rd = ndes.sum() / rec_time.sum()
    rc = ncre.sum() / emp_time.sum()
    return rho, rd, rc, caps, rd_g.std(ddof=1) / math.sqrt(groups), rc_g.std(ddof=1) / math.sqrt(groups)


def run_3b():
    gform = 0.4
    out = []
    for L, M in ((6, 6000), (8, 6000), (10, 6000), (12, 6000), (14, 4000)):
        t0 = time.time()
        rho, rd, rc, caps, erd, erc = run_ring(L, gform, 120.0, 0.05, M)
        out.append((L, rho, rd, rc))
        pred = rho / (1 - rho)
        print(f"L={L:2d}  M={M}  density={rho:.4f}  r_destroy per record={rd:.4f}+-{erd:.4f}  r_create per empty site={rc:.4f}+-{erc:.4f}  "
              f"r_c/r_d={rc/rd:.3f}  (rho/(1-rho)={pred:.3f})  capped steps={caps}  [{time.time()-t0:.0f}s]", flush=True)
    rd6, rd12 = out[0][2], out[-2][2]
    ratio = rd12 / rd6
    check("3b bulk destruction rate is intensive: r_d(L=12)/r_d(L=6) within [0.7, 1.3]  (FAIL of permanence)", 0.7 <= ratio <= 1.3, f"(ratio {ratio:.3f})")
    print("   r_d(L=14)/r_d(L=6) = %.3f" % (out[-1][2] / rd6), flush=True)
    check("3b no statistical permanence: r_d does NOT fall by 2x from L=6 to L=12", ratio > 0.5)
    ok = all(abs((o[3] / o[2]) / (o[1] / (1 - o[1])) - 1) < 0.35 for o in out)
    check("3b detailed balance: r_c/r_d within 35% of rho/(1-rho) at every L", ok,
          " ".join(f"{(o[3]/o[2])/(o[1]/(1-o[1])):.2f}" for o in out))
    print("mean lifetime of a record 1/r_d (hop units): " + ", ".join(f"L={o[0]}: {1/o[2]:.1f}" for o in out), flush=True)


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which in ("3a", "all"):
        run_3a()
    if which in ("3b", "all"):
        run_3b()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
