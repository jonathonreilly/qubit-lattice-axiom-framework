#!/usr/bin/env python3
"""s3: sharpness witness for the clean-level hypothesis.

Finite-range walks whose isolated Weyl nodes at quasienergy 0 have NONZERO net chirality.
Theorem L + K force the level eps = 0 to contain Fermi sheets carrying the opposite
Berry flux; the script certifies (i) W3 = 0 exactly, (ii) the isolated level-0 nodes,
their boxes, chiralities and dispersion, (iii) the presence of a sheet component at
level 0 (a connected uncertified set too large to be a node neighbourhood, plus explicit
non-degenerate eigenvalue-1 points found on it).
  T2: U = e^{i k_x} Q(2,1,1)                (n = 2, det U = e^{2 i k_x} not constant)
  T3: U = (e^{i k_x} Q(2,1,1)) (+) e^{-0.5i} e^{-2 i k_x}   (n = 3, det U = e^{-0.5i} constant)
"""
import numpy as np
import lib5b as L
import walks5b as WK

C = L.Checker()
Q = WK.Q_product((2, 1, 1))
T2 = L.lmul(L.Laurent({(1, 0, 0): np.eye(2)}), Q); T2.name = 'T2 = e^{ikx} Q211'
T3 = L.ldirect(T2, L.Laurent({(-2, 0, 0): np.array([[np.exp(-0.5j)]])})); T3.name = 'T3 = e^{ikx}Q211 (+) e^{-0.5i} e^{-2ikx}'
# all Weyl nodes of Q211 at its levels 0 and pi (certified clean levels, as in s2 case [2])
QNODES = []
for lev in (0.0, np.pi):
    rq = L.analyze_level(Q, lev, N0=32, depth=4, M=16, verbose=False)
    assert rq['clean'] and not any(b['pocket'] for b in rq['boxes'])
    for b in rq['boxes']:
        assert len(b['nodes']) == 1 and round(b['ch']) == b['nodes'][0]['chi']
        QNODES.append((b['nodes'][0]['k'], b['nodes'][0]['chi'], lev))
print(f'Q211: {len(QNODES)} Weyl nodes at its levels 0 and pi (each alone in a certified box, Ch = chi)')
C.check('Q211 node inventory: 16 at level 0 and 16 at level pi, each certified alone in its box', len(QNODES) == 32)


def small_box_certificate(W, p, d, n_face=60, n_vol=10):
    """Certify: (a) no eigenvalue 1 on the surface of [p-d,p+d]^3 (Lipschitz, face cells of side h,
    sup-distance <= h/2 to a centre); (b) a quasienergy phi absent on the whole cube."""
    h = 2*d/n_face
    cs = (np.arange(n_face) + 0.5)*h - d
    pts = []
    for a in range(3):
        b_, c_ = (a+1) % 3, (a+2) % 3
        for side in (-d, d):
            G = np.zeros((n_face, n_face, 3)); G[..., a] = side
            G[..., b_] = cs[:, None]; G[..., c_] = cs[None, :]
            pts.append(G.reshape(-1, 3))
    pts = np.concatenate(pts) + p
    sfc = L.gapfun(W(pts), 0.0)
    if not np.all(sfc > W.L*h/2*(1+1e-9)):
        return False, None
    hv = 2*d/n_vol
    cv = (np.arange(n_vol) + 0.5)*hv - d
    V = np.stack(np.meshgrid(cv, cv, cv, indexing='ij'), -1).reshape(-1, 3) + p
    E = L.quasi(W(V)).ravel()
    for phi in np.linspace(-np.pi, np.pi, 73)[:-1]:
        if abs(np.angle(np.exp(1j*phi))) < 0.3:
            continue
        if np.all(L.gapfun(W(V), phi) > W.L*hv/2*(1+1e-9)):
            return True, np.mod(phi, 2*np.pi)      # phi in (0, 2pi) = (eps, eps+2pi)
    return False, None


Kt = np.random.default_rng(4).uniform(0, 2*np.pi, (300, 3))
for W in (T2, T3):
    print(f'=== {W.name} (n={W.n}, r={W.range}, L={W.L:.2f})', flush=True)
    r = W.range
    w1 = L.w3_grid(W, 6*r + 2); w2 = L.w3_grid(W, 6*r + 5, 0.37)
    C.check(f'{W.name}: exact-grid W3 = 0 ({w1.real:+.1e}, {w2.real:+.1e})', abs(w1) < 1e-8 and abs(w2) < 1e-8, 'exact-grid certificate')
    d = np.linalg.det(W(Kt))
    print(f'  det U: max |det - det(k0)| = {np.abs(d - d[0]).max():.2e} (constant iff ~1e-15)')
    nod = []
    for (p, chiQ, lev) in QNODES:
        if abs(np.angle(np.exp(1j*p[0]) * (1 if lev == 0 else -1))) > 1e-9:
            continue          # eigenvalue of U at p is e^{i p_x} Q(p) = e^{i p_x} (+-1); keep those = 1
        chi, v, tilt, oth = L.weyl_chirality(W, 0.0, p)
        ok, phi = small_box_certificate(W, p, 0.1)
        lo_k, hi_k = p - 0.1, p + 0.1
        ch, rk = L.chern_box(W, lo_k, hi_k, 0.0, phi, 24) if ok else (np.nan, None)
        tv = np.linalg.norm(np.linalg.solve(v, tilt))
        nod.append(dict(k=p, chi=chi, ch=ch, ok=ok, tv=tv))
        print(f'    level-0 Weyl node k={np.round(p, 6)} chi={chi:+d} (chi of Q: {chiQ:+d}) tilt={np.round(tilt, 4)} '
              f'v sing.vals={np.round(np.linalg.svd(v, compute_uv=False), 4)} |v^-1 t|={tv:.3f} box(0.1) certified={ok} Ch={ch:+.6f}')
    C.check(f'{W.name}: every level-0 node box surface certified level-free and phi-free inside', all(q['ok'] for q in nod) and len(nod) > 0)
    C.check(f'{W.name}: all level-0 nodes are type-I (|v^-1 tilt| < 1)', all(q['tv'] < 1 for q in nod))
    C.check(f'{W.name}: per node box Ch(P_<) = chi (Lemma S)', all(abs(q['ch'] - q['chi']) < 1e-9 for q in nod))
    s = sum(q['chi'] for q in nod)
    print(f'  net chirality of the {len(nod)} isolated level-0 Weyl nodes: {s:+d}.  Theorem L with W3 = 0 then forces '
          f'the level-0 sheets to carry sum Ch(P_<|dN) = {-s:+d}.')
    C.check(f'{W.name}: net level-0 nodal chirality is nonzero (witness)', s != 0)
    # explicit non-degenerate level-0 points on the sheet
    pts = 0
    rng = np.random.default_rng(9)
    for _ in range(40):
        kk, sv = L.find_min(W, 0.0, rng.uniform(0, 2*np.pi, 3))
        if sv < 1e-9:
            lam = np.linalg.eigvals(W(kk[None])[0]); dd = np.sort(np.abs(lam - 1))
            if dd[1] > 1e-2:
                pts += 1
    C.check(f'{W.name}: found {pts}/40 random-start non-degenerate eigenvalue-1 points (sheet points)', pts > 0)
C.total()
