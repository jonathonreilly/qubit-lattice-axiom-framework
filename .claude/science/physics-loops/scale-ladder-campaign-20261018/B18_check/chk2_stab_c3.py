#!/usr/bin/env python3
"""B18 check 2/4: little groups of k* and k*+pi e_x under the gauge-dressed rotations (own momentum-shift
extraction), and the step-level c3 obstruction for H_link-type tastes T_x = (-1)^{x_1} diag(v_c), v built
here from the link-sign conditions v_{c'}/v_c = w (-1)^{a_x} (per corner plane; free plane amplitudes alpha_p).
c3 proof route: the conjugates by the three axis C2s preserve every corner plane, so alpha_p cancels in
tau = (R T_x R^-1) T_x^-1: these on-site symmetries are alpha-independent.  If the commutant at k* of
{rho(R)} + {alpha-independent taus} has no 2-dim block, c3 holds for ALL alpha (and both w)."""
import time
from chk_model import *
t0 = time.time(); PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)
KS = [np.array(t) * 2 * np.pi / L for t in TV]; BK = [Bloch(k) for k in KS]
def kid(k): return [i for i, q in enumerate(KS) if np.allclose(np.exp(1j * (q - k)), 1)][0]
def mom_map(Mop):
    out = {}
    for i in range(64):
        w = [np.linalg.norm(BK[j].conj().T @ Mop @ BK[i]) for j in range(64)]; j = int(np.argmax(w))
        assert abs(w[j] - np.sqrt(12)) < 1e-8; out[i] = j
    return out
rmaps = [mom_map(M) for M in Rm]
ik, ix = kid(kst), kid(kst + np.pi * np.eye(3)[0])
st0 = [r for r in range(24) if rmaps[r][ik] == ik]; stx = [r for r in range(24) if rmaps[r][ix] == ix]
stx_axes = sorted({tuple(np.abs(np.round(np.real(np.linalg.eig(ROTS[r].astype(float))[1][:, np.argmin(np.abs(np.linalg.eig(ROTS[r].astype(float))[0] - 1))]))).astype(int)) for r in stx if not np.array_equal(ROTS[r], np.eye(3))})
check("c1: |Stab(k*)| = 24, |Stab(k*+pi e_x)| = 8 (D4 about x) in the affine action of the 24 gauge-dressed rotations",
      len(st0) == 24 and len(stx) == 8, f"{len(st0)}, {len(stx)}; rotation axes in Stab(k*+pi e_x): {stx_axes}")
# orbit structure of all 64 momenta (sanity: only k*, -k* fixed)
fixed = [i for i in range(64) if all(rmaps[r][i] == i for r in range(24))]
check("only k* and -k* are fixed by all 24 lifted rotations", sorted(fixed) == sorted([ik, kid(-kst)]))

# ---- H_link-type tastes, built from link sign conditions
links = []   # (c, c', shift)
for sh, M in blL.items():
    for cp, c in np.argwhere(np.abs(M) > 1e-12): links.append((int(c), int(cp), np.array(sh)))
planes = {}
for c in CORN:
    planes.setdefault(tuple(sorted(np.nonzero(np.abs(np.add(*[np.array(d) for d in c])))[0])), []).append(CI[c])
pid = {c: p for p, cs in enumerate(planes.values()) for c in cs}
def taste_v(w, alpha):
    v = np.zeros(12, complex)
    for p, cs in enumerate(planes.values()):
        v[cs[0]] = alpha[p]; todo = [cs[0]]
        while todo:
            c = todo.pop()
            for a, b, sh in links:
                if a == c:
                    val = v[c] * w * (-1.0) ** sh[0]
                    if v[b] == 0: v[b] = val; todo.append(b)
                    elif not np.isclose(v[b], val): return None
    return v
xs = np.array([v[0] for v, c in VERTS]); cid = np.array([CI[c] for v, c in VERTS])
Hl = H0(0.0, 1.0)
def Treal(v): return np.diag((-1.0) ** xs[:, 0] * v[cid])
ok_t = []
for w in (1, -1):
    v = taste_v(w, (1, 1, 1)); T = Treal(v); ok_t.append(v is not None and np.allclose(T @ Hl @ np.linalg.inv(T), w * Hl))
links_in_plane = all(pid[a] == pid[b] for a, b, sh in links)
check("H_link keeps each corner in its plane; the link-sign conditions are consistent for w = +1 and w = -1, giving the diagonal "
      "tastes T_x = (-1)^{x_1} diag(v_c) with one free amplitude per plane (verified in real space on the L=4 torus)", links_in_plane and all(ok_t))
Bst = Bloch(kst); rho = [Bst.conj().T @ M @ Bst for M in Rm]
sites = np.array([v for v, c in VERTS])
def taus(v, subset):
    T = Treal(v); Ti = np.linalg.inv(T); out = []; conjs = {}
    for r in subset:
        D = Rm[r] @ T @ Rm[r].T; d = np.diag(D); assert np.allclose(D, np.diag(d))
        tau = d[loc0]; e = [e for e in itertools.product((0, 1), repeat=3) if np.allclose(d, (-1.0) ** (sites @ np.array(e)) * tau[cid])]
        assert len(e) == 1; conjs.setdefault(e[0], []).append(tau)
    for ts in conjs.values():
        for a in ts:
            for b in ts: out.append(a / b); out.append(a * b)
    return out, conjs
def commutant_mults(gens):
    I = np.eye(12); A = np.vstack([np.kron(g.T, I) - np.kron(I, g) for g in gens]); w_, U_ = np.linalg.eigh(A.conj().T @ A)
    cb = [U_[:, j].reshape(12, 12, order='F') for j in range(144) if w_[j] < 1e-9]
    r_ = np.random.default_rng(0); X = sum((r_.normal() + 1j * r_.normal()) * b for b in cb); X = X + X.conj().T
    ev = np.linalg.eigvalsh(X); out = []
    for x in ev:
        if out and abs(x - out[-1][0]) < 1e-8: out[-1][1] += 1
        else: out.append([x, 1])
    return len(cb), [m for _, m in out]
print("commutant of rho alone at k*:", commutant_mults(rho))
axisC2 = [r for r in range(24) if np.allclose(ROTS[r], np.diag(np.diag(ROTS[r]))) ]   # identity + 3 axis C2s
res_ind = []
for w in (1, -1):
    v = taste_v(w, (1, 1, 1)); tl, cj = taus(v, axisC2)
    # alpha-independence: same taus for random plane amplitudes
    va = taste_v(w, tuple(np.exp(2j * np.pi * np.random.default_rng(w + 5).uniform(size=3)) * np.random.default_rng(9).uniform(0.5, 2, 3)))
    tl2, _ = taus(va, axisC2)
    same = all(any(np.allclose(a, b) for b in tl) for a in tl2[0::2])   # ratio taus coincide
    res_ind.append((w, same, commutant_mults(rho + [np.diag(t) for t in tl[0::2]])))
print("alpha-independent (axis-C2) taus, per w: (w, alpha-independent?, (commutant dim, multiplicities))", res_ind)
check("c3 for ALL alpha: the axis-C2 conjugates alone (alpha-independent ratio taus) already cut the k* commutant to blocks with no "
      "2-fold level, for w = +1 and w = -1", all(s and 2 not in m[1] for w, s, m in res_ind), f"{[(w, m) for w, s, m in res_ind]}")
r7 = np.random.default_rng(5); full = []
for w in (1, -1):
    for al in [(1, 1, 1), (1, 1, -1), (1, -1, 1), (1, 1j, 1), (2, 1, 0.5)] + [tuple(np.exp(2j * np.pi * r7.uniform(size=3))) for _ in range(3)]:
        v = taste_v(w, al); tl, _ = taus(v, range(24))
        full.append(commutant_mults(rho + [np.diag(t) for t in tl]))
check("c3 with all 24 conjugates (16 alpha choices incl. non-unimodular): commutant at k* has no 2-fold level", all(2 not in m for d, m in full),
      f"{sorted(set((d, tuple(m)) for d, m in full))}")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time()-t0:.0f}s]")
