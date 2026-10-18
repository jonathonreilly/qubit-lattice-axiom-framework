

# ------------------------------------------------------------------ helpers for the census
B4 = []
for _p in itertools.permutations(range(4)):
    for _s in itertools.product([1, -1], repeat=4):
        _M = np.zeros((4, 4))
        for _i in range(4): _M[_p[_i], _i] = _s[_i]
        B4.append(_M)


def b4_symmetric(C):
    def canon_pts(P):
        P2 = np.array(sorted(tuple(np.round(840 * p).astype(int)) for p in P)); sh = np.floor_divide(P2.min(axis=0), 840) * 840
        return tuple(map(tuple, P2 - sh))
    base = {canon_pts([C.pos(v) for v in s]) for s in C.simp}
    return all(canon_pts([g @ C.pos(v) for v in s]) in base for g in B4 for s in C.simp)


def profile(C, ngauge=None):
    """(nullity, gauge rank, massless non-gauge count) of the Regge edge form."""
    q = np.array([0.31, -0.22, 0.17, 0.4]); s = np.sort(np.linalg.svd(C.Q(q), compute_uv=False)); s = s / s[-1]
    nul = int((s < 1e-8).sum()); grk = np.linalg.matrix_rank(C.gauge(q), tol=1e-9)
    kd = np.array([0.3, -0.5, 0.6, 0.55]); kd /= np.linalg.norm(kd); ev = []
    for x in (0.02, 0.01):
        Q = C.Q(x * kd); w = np.linalg.eigvalsh(0.5 * (Q + Q.conj().T)); ev.append(np.sort(np.abs(w)))
    soft = int(sum(1 for i in range(nul, min(nul + 40, C.E)) if abs(ev[0][i] / ev[1][i] - 4) < 0.1 and ev[1][i] < 1e-2))
    return nul, grk, soft


def k4_form_residue(C):
    """max over degrees and two directions of |lambda(omega = k)|/k^4 for the C(4,k) lowest Hodge eigenvalues at |k| = 0.025."""
    F = Forms(C); worst = 0.0
    for n in [(1, 0, 0), (3, 1, 2)]:
        n = np.array(n, float); n /= np.linalg.norm(n); km = 0.025
        for j in range(5):
            K, M = F.hodge(j, np.array([*(km * n), 1j * km])); w = np.sort(np.abs(sl.eigvals(K, M)))
            worst = max(worst, w[math.comb(4, j) - 1] / km ** 4)
    return worst


def comp_inv(Q, G, J):
    Pq, _ = np.linalg.qr(G); n = Q.shape[0]
    Pc = np.linalg.svd(np.eye(n) - Pq @ Pq.conj().T)[0][:, :n - G.shape[1]]
    return Pc @ np.linalg.solve(Pc.conj().T @ Q @ Pc, Pc.conj().T @ J)


def rp_vertex(Qfun, offs_t, ks, Nt, t0):
    kts = 2 * np.pi * np.arange(Nt) / Nt
    inv = [np.linalg.inv(Qfun(np.array([*ks, kt]))) for kt in kts]
    G = lambda dbt: sum(Ki * np.exp(1j * kt * dbt) for Ki, kt in zip(inv, kts)) / Nt
    half = [(bt, tau, bt + ot) for bt in range(-1, Nt // 2 + 1) for tau, ot in enumerate(offs_t)
            if t0 - 1e-9 <= bt + ot <= t0 + Nt / 2 + 1e-9]
    R = np.zeros((len(half),) * 2, complex)
    for a, (bt1, ta, _) in enumerate(half):
        for b, (bt2, tb, t2) in enumerate(half):
            R[a, b] = G(bt1 - int(round(2 * t0 - t2 - offs_t[tb])))[ta, tb]
    return R


def main():
    built = {}
    def get(which):
        if which not in built:
            OFF, base, vol, ncell, sizes = build(which); built[which] = (Complex(OFF, base), vol, len(base))
        return built[which]
    # ---------------- K1 the builder reproduces the D4 cone
    C4, vol4, n4 = get((4,))
    check("K1 canonical builder (Delaunay cells, every non-simplicial face coned from its circumcentre) on Z^4 + {hypercube centres} = the D4 cone",
          n4 == 96 and len(C4.types) == 8 and abs(vol4 - 1) < 1e-9 and C4.E == 72, f"{n4} simplices, {len(C4.types)} vertex types, {C4.E} edges, volume {vol4:.6f}")
    # ---------------- K2 profiles of five carriers
    expect = {(): (1, 0), (1,): (0, 0), (2,): (0, 2), (3,): (0, 0), (4,): (0, 2)}
    rows, ok2 = [], True
    for which, (eh, ep) in expect.items():
        C, vol, n = get(which); nul, grk, soft = profile(C); sym = b4_symmetric(C)
        hid, par = nul - grk, soft - 6; ok2 &= (hid == eh and par == ep and sym and abs(vol - 1) < 1e-9)
        rows.append(f"{set(which) or '{}'}: hidden {hid}, partners {par}, B4 {sym}")
    check("K2 hidden-curvature and partner counts: Z^4 alone 1/0; + link midpoints 0/0; + face centres 0/2; + cube centres 0/0; + hypercube centres 0/2",
          ok2, "; ".join(rows))
    # ---------------- K3 O(k^4) residue of the matter (Whitney Hodge) cone
    res = {w: k4_form_residue(get(w)[0]) for w in [(4,), (2,), (1,), (3,)]}
    check("K3 on omega = k, |lambda|/k^4 of all 16 Hodge modes: < 1e-4 for the even sets {4}, {2} (no O(k^4) term); > 1e-3 for {1}, {3} (splitting)",
          res[(4,)] < 1e-4 and res[(2,)] < 1e-4 and res[(1,)] > 1e-3 and res[(3,)] > 1e-3, "; ".join(f"{set(w)}: {v:.1e}" for w, v in res.items()))
    # ---------------- K4 the link-midpoint carrier: linearised GR for any consistent reading, no extra term
    C1 = get((1,))[0]; site = [i for i, o in enumerate(C1.OFF) if np.allclose(o, 0)][0]
    def Gns(k):
        G = C1.gauge(k); return np.hstack([G[:, 4 * t:4 * t + 4] for t in range(len(C1.types)) if t != site])
    def reading(k, W):
        A = np.hstack([C1.line_map(k), Gns(k)]); return np.linalg.solve(A.conj().T @ W @ A, A.conj().T @ W)[:10]
    rng = np.random.default_rng(0); Ws = [np.eye(C1.E), np.diag(rng.uniform(0.2, 5, C1.E))]
    itt, ixx = 3, 0; out = []
    for kk in [np.array([0, 0.02, 0, 0.0]), np.array([0, 0.012, 0.009, 0.0])]:
        for W in Ws:
            L = reading(kk, W); T = np.zeros(10); T[itt] = 1.0
            h = L @ comp_inv(C1.Q(kk), C1.gauge(kk), L.conj().T @ T); out.append((h[itt].real * (kk @ kk), (h[ixx] / h[itt]).real))
    check("K4 Z^4 + link midpoints: a static T_tt source through two different consistent site readings gives h_tt k^2 = -2 and h_xx/h_tt = -1 (no curvature-squared term)",
          all(abs(a + 2) < 1e-3 and abs(b + 1) < 1e-3 for a, b in out), "; ".join(f"{a:+.4f}/{b:+.4f}" for a, b in out))
    # ---------------- K5 its P1 scalar is reflection positive with lumped mass
    tix = {t: i for i, t in enumerate(C1.types)}; wv = np.zeros(len(C1.types))
    for vs in C1.simp:
        P = np.array([C1.pos(v) for v in vs]); vol = abs(np.linalg.det(P[1:] - P[0])) / 24
        for v in vs: wv[tix[v[1]]] += vol / 5
    offs_t = [float(o[3]) for o in C1.OFF]; mn = 1.0
    for ks in [np.zeros(3), np.array([0.7, -0.3, 0.2])]:
        for t0 in (0.0, 0.5):
            R = rp_vertex(lambda k: p1_scalar(C1, k) + 0.3 * np.diag(wv), offs_t, ks, 6, t0)
            w = np.linalg.eigvalsh(0.5 * (R + R.conj().T)); mn = min(mn, w.min() / abs(w).max())
    check("K5 Z^4 + link midpoints: P1 scalar with lumped mass is reflection positive at both tick planes", mn > -1e-12, f"min/max eigenvalue {mn:+.1e}")
    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
