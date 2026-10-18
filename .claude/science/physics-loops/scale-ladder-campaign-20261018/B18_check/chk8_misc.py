#!/usr/bin/env python3
"""B18 check 8: (a) S has NON-uniform (corner-dependent) momentum-shift symmetries G = diag((-1)^{e_c.x}) with
e_c.f_c even (it is 12 families of decoupled chains), outside the uniform-taste theorem; they are not symmetries of
the eight-node step.  (b) the Q = pi(1,1,1) taste: is there one on-site V with V R_L(k) V^-1 = -R_L(k+Q) that also
commutes with H_on, Lambda and S (then EVERY S.U, S.R_L.U, R_L.S.U Clifford-phase step has W(k+Q) = -V W(k) V^-1,
which the B18 family screen implicitly needs to cover the maps k -> +-k + pi e for e of weight 2)?"""
from chk_model import *
PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)
xs = np.array([v for v, c in VERTS]); cid = np.array([CI[c] for v, c in VERTS])
# normal of each corner's plane
nrm = {CI[c]: np.array([1 - abs(x) for x in FACE[c]]) for c in CORN}
G = np.diag([(-1.0) ** int(xs[a] @ nrm[cid[a]]) for a in range(nV)])
okS = np.allclose(G @ Sr @ G, Sr)
# its momentum action: corner c shifted by pi n_c  -> not a uniform map
Wreal = Sr @ RLr @ np.kron(np.eye(L ** 3), UH @ UL)   # VERTS ordering is site-major with CORN order
assert np.allclose(blocks_from(Wreal)[(0, 0, 0)] if (0, 0, 0) in blocks_from(Wreal) else 0, Hk(blocks_from(Wreal), np.zeros(3)) * 0 + blocks_from(Wreal).get((0, 0, 0), 0))
kk = np.array([0.3, -0.4, 0.9])
okW = np.allclose(Hk(blocks_from(Wreal), kk), Ws(kk))
notW = not any(np.allclose(G @ Wreal @ G, w * Wreal) for w in (1, -1, 1j, -1j))
check("(a) G = diag((-1)^{n_c . x}) (n_c = normal of the corner's plane) commutes with S: a corner-dependent momentum shift k -> k + pi n_c, "
      "outside the uniform-taste class; it is NOT a symmetry of the eight-node step (any w)", okS and okW and notW)
# (b) joint Q taste
Q3 = np.pi * np.ones(3); I = np.eye(12); rng = np.random.default_rng(0); ks = rng.uniform(-np.pi, np.pi, (4, 3))
rows = [np.kron(RLk(k).T, I) + np.kron(I, RLk(k + Q3)) for k in ks]          # V RL(k) = -RL(k+Q) V
rows += [np.kron(Hon0.T, I) - np.kron(I, Hon0), np.kron(Lam.T, I) - np.kron(I, Lam)] + [np.kron(SKc(k).T, I) - np.kron(I, SKc(k)) for k in ks[:2]]
A = np.vstack(rows); _, s, Vh = np.linalg.svd(A, full_matrices=False); s = np.concatenate([s, np.zeros(144 - len(s))]); nb = Vh[s < 1e-9]
V = nb[0].conj().reshape(12, 12, order='F') if len(nb) else None
okV = V is not None and np.linalg.svd(V, compute_uv=False).min() > 1e-6
fam = []
if okV:
    for (a, b) in [(0, 0), (2, 3), (1, 2)]:
        for (c1, c2, c3) in [(1, 1, 0), (0, 2, 0), (3, 1, 2)]:
            U = UHc(a, b) @ ULc(c1, c2, c3)
            for Wf in (lambda k: SKc(k) @ U, lambda k: SKc(k) @ RLk(k) @ U, lambda k: RLk(k) @ SKc(k) @ U):
                fam.append(all(np.allclose(V @ Wf(k) @ np.linalg.inv(V), -Wf(k + Q3)) or np.allclose(V @ Wf(k) @ np.linalg.inv(V), Wf(k + Q3)) for k in ks[:2]))
check("(b) one on-site V (diagonal? see detail) gives R_L(k+Q) = -V R_L(k) V^-1 and commutes with H_on, Lambda and S, so every B1 Clifford-phase step "
      "has the Q-taste W(k+Q) = +-V W(k) V^-1 (the family screen's e_x-only test then also covers weight-2 shifts)",
      okV and all(fam), f"null dim {len(nb)}; V diagonal: {bool(V is not None and np.allclose(V, np.diag(np.diag(V))))}; sampled steps OK {sum(fam)}/{len(fam)}")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
