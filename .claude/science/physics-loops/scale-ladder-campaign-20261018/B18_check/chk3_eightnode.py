#!/usr/bin/env python3
"""B18 check 3: the eight-node step Ws = S.R_L.U_H.U_L has no taste carrying the k* node to a doubler.
Own route: exact first-order degenerate perturbation theory (analytic dW/dk from the Fourier blocks),
for EVERY 2-fold level at the four momenta k*, -k*, k*+pi e_x, -k*+pi e_x (all quasi-energies), giving the
2x2 Weyl velocity matrix B_jb, tilt a_j, |det B| and chirality sign(det B).
Invariant: for T translation-covariant (anti)unitary with momentum map k -> Mk+theta, M in GL(3,Z) (unitarity
forces |det M| = 1: a map with |det M| = n > 1 multiplies the spectral multiplicity by n), and
T W T^-1 = w W^{+-1}, a Weyl level at k0 maps to a Weyl level at Mk0+theta with B' = (+-) M^{-T} B O (O in O(3) from
the 2x2 frame change / conjugation), so |det B| is invariant.  Also the direct spectral test over all 48 x 8 maps
k -> Mk + pi e with M in O_h, E -> +-E + phi."""
import time
from chk_model import *
t0 = time.time(); PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)
def dHk(bl, k, j):
    H = np.zeros((12, 12), complex)
    for sh, M in bl.items(): H += 1j * sh[j] * M * np.exp(1j * np.dot(k, sh))
    return H
UU = UH @ UL
def W(k): return SKc(k) @ RLk(k) @ UU
def dW(k, j): return (dHk(blS, k, j) @ RLk(k) + SKc(k) @ dHk(blL, k, j)) @ UU
PAU = [np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]])]
def levels_at(k, tol=1e-8):
    e, V = np.linalg.eig(W(k)); ph = np.angle(e); out = []; used = np.zeros(12, bool)
    for i in np.argsort(ph):
        if used[i]: continue
        grp = [j for j in range(12) if not used[j] and abs(wrap(ph[j] - ph[i])) < tol]; used[grp] = True
        Q, _ = np.linalg.qr(V[:, grp]); out.append((ph[i], len(grp), Q))
    return out
def weyl(k, E, Q):
    Wk = W(k); A = [-1j * Q.conj().T @ Wk.conj().T @ dW(k, j) @ Q for j in range(3)]
    herm = max(np.abs(a - a.conj().T).max() for a in A)
    a = np.array([np.trace(x).real / 2 for x in A]); B = np.array([[np.trace(A[j] @ PAU[b]).real / 2 for b in range(3)] for j in range(3)])
    return a, B, herm
targets = {"k*": kst, "-k*": -kst, "k*+pi ex": kst + np.pi * np.eye(3)[0], "-k*+pi ex": -kst + np.pi * np.eye(3)[0]}
vs = np.sqrt(2) / 3
table = {}
for nm, k0 in targets.items():
    for E, m, Q in levels_at(k0):
        row = dict(E=E, m=m)
        if m == 2:
            a, B, herm = weyl(k0, E, Q); sv = np.linalg.svd(B, compute_uv=False)
            row.update(tilt=np.linalg.norm(a), sv=sv, det=np.linalg.det(B), herm=herm)
        table.setdefault(nm, []).append(row)
for nm, rows in table.items():
    print(nm)
    for r in rows:
        if r['m'] == 2: print(f"   E={r['E']:+.6f} m=2  speeds {np.round(r['sv'], 7)}  |det|={abs(r['det']):.6f} chir={int(np.sign(r['det'])):+d} tilt={r['tilt']:.1e}")
        else: print(f"   E={r['E']:+.6f} m={r['m']}")
# finite-difference cross-check of the perturbation theory at k* (pi/2 level) and at k*+pi ex
def fd_speeds(k0, E, d, q=1e-4):
    e = wrap(np.angle(np.linalg.eigvals(W(k0 + q * d))) - E); e = np.sort(e[np.abs(e) < 10 * q]); return (e[-1] - e[0]) / (2 * q)
Enode = [r['E'] for r in table['k*'] if r['m'] == 2 and abs(r['E'] - np.pi / 2) < 1e-6][0]
fd = [fd_speeds(kst, Enode, d) for d in np.eye(3)] + [fd_speeds(targets["k*+pi ex"], Enode, d) for d in np.eye(3)]
pt_ks = [r for r in table['k*'] if r['m'] == 2 and abs(r['E'] - Enode) < 1e-6][0]['sv']
pt_dx = [r for r in table['k*+pi ex'] if r['m'] == 2 and abs(r['E'] - Enode) < 1e-6][0]['sv']
check("perturbation-theory velocities agree with finite differences (k* and k*+pi e_x at the +pi/2 node)",
      np.allclose(sorted(fd[:3]), sorted(pt_ks), atol=1e-6) and np.allclose(sorted(fd[3:]), sorted(pt_dx), atol=1e-6),
      f"fd {np.round(fd, 7)}")
allrows = [(nm, r) for nm, rows in table.items() for r in rows if r['m'] == 2]
ks_rows = [r for nm, r in allrows if nm in ("k*", "-k*")]; dbl_rows = [r for nm, r in allrows if nm not in ("k*", "-k*")]
iso = [r for r in ks_rows if np.allclose(r['sv'], vs, atol=1e-8)]
check("k*, -k*: the 2-fold levels at +-pi/2 are isotropic Weyl nodes at sqrt2/3 (|det| = (sqrt2/3)^3 = 0.104757), untilted",
      len(iso) == 4 and all(r['tilt'] < 1e-9 for r in iso) and all(abs(abs(r['det']) - vs ** 3) < 1e-9 for r in iso),
      f"{len(iso)} such levels; v*^3 = {vs**3:.6f}")
dets_d = sorted({round(abs(r['det']), 6) for r in dbl_rows})
check("EVERY 2-fold level at the doubler momenta k*+pi e_x, -k*+pi e_x (all quasi-energies, both node sets) has |det B| != v*^3, "
      "so no translation-covariant (anti)unitary with M in GL(3,Z), any theta, any E -> +-E + phi, carries a k* Weyl node there",
      all(abs(abs(r['det']) - vs ** 3) > 1e-3 for r in dbl_rows), f"doubler-momentum |det| values {dets_d}; levels {[(round(r['E'],4), round(abs(r['det']),6)) for r in dbl_rows]}")
nd = [r for r in dbl_rows if abs(abs(r['E']) - np.pi / 2) < 1e-6]
check("the doubler cones at +pi/2 and -pi/2 are identical uniaxial cones (0.2467203, 0.5837466 x2), |det| = 0.084072, opposite chirality to the same-momentum partner set",
      len(nd) == 4 and all(np.allclose(sorted(r['sv']), [0.2467203, 0.5837466, 0.5837466], atol=2e-7) for r in nd),
      f"{[(round(r['E'],4), int(np.sign(r['det']))) for r in nd]}")
# chirality bookkeeping at the +pi/2 set
ch = {nm: int(np.sign(r['det'])) for nm, rows in table.items() for r in rows if r['m'] == 2 and abs(r['E'] - Enode) < 1e-6}
print("chiralities at +pi/2 (sign det B):", ch)
# the ratio claims
r_ = pt_dx; print(f"ratio v_ax/v_tr = {min(r_)/max(r_):.12f} vs 1-1/sqrt3 = {1-1/np.sqrt(3):.12f}")

# direct spectral test over all M in O_h and e in {0,1}^3, E -> +-E + phi
OH = [np.array(P) * np.array(s)[:, None] for P in [np.eye(3, dtype=int)[list(p)] for p in itertools.permutations(range(3))] for s in itertools.product((1, -1), repeat=3)]
rng = np.random.default_rng(11); KR = rng.uniform(-np.pi, np.pi, (5, 3))
def spec(k): return np.sort(np.mod(np.angle(np.linalg.eigvals(W(k))), 2 * np.pi))
SP = {}
def specc(k):
    key = tuple(np.round(np.mod(k, 2 * np.pi), 10))
    if key not in SP: SP[key] = spec(k)
    return SP[key]
def mismatch(a, b):
    best = np.inf
    for j in range(12):
        c = np.sort(np.mod(a + (b[0] - a[j]), 2 * np.pi))
        d = [np.max(np.abs(wrap(np.roll(c, s) - b))) for s in range(12)]; best = min(best, min(d))
    return best
res = {}
for M in OH:
    for e in itertools.product((0, 1), repeat=3):
        th = np.pi * np.array(e)
        for sg in (1, -1):
            res[(tuple(M.ravel()), e, sg)] = max(mismatch(sg * specc(k), specc(M @ k + th)) for k in KR)
good = [key for key, v in res.items() if v < 1e-8]
def maps_to(key):
    M = np.array(key[0]).reshape(3, 3); th = np.pi * np.array(key[1]); k = wrap(M @ kst + th)
    return "k*" if np.allclose(np.exp(1j * (k - kst)), 1) else ("-k*" if np.allclose(np.exp(1j * (k + kst)), 1) else "doubler/other")
dest = sorted({maps_to(k) for k in good})
nprop = sum(1 for k in good if round(np.linalg.det(np.array(k[0]).reshape(3, 3))) == 1)
check("direct spectral test, all 48 x 8 x 2 maps k -> Mk + pi e (M in O_h), E -> +-E + phi: every map whose spectra match sends k* to +-k*; "
      "no spectrally allowed map sends k* to a doubler",
      dest and set(dest) <= {"k*", "-k*"}, f"{len(good)} of {len(res)} maps pass the spectral test ({nprop} with det M = +1); destinations {dest}; "
      f"min mismatch among doubler-sending maps {min(v for k_, v in res.items() if maps_to(k_) == 'doubler/other'):.3f}")
# genuine operator for k -> k + Q ?
Q3 = np.pi * np.ones(3)
I = np.eye(12); ks2 = rng.uniform(-np.pi, np.pi, (4, 3))
found = []
for om in (1, -1, 1j, -1j):
    A = np.vstack([np.kron(W(k).T, I) - om * np.kron(I, W(k + Q3)) for k in ks2]); _, s, Vh = np.linalg.svd(A)
    s = np.concatenate([s, np.zeros(Vh.shape[0] - len(s))]); nb = Vh[s < 1e-9]
    if len(nb):
        Vq = sum((rng.normal() + 1j * rng.normal()) * v.conj().reshape(12, 12, order='F') for v in nb)
        if np.linalg.svd(Vq, compute_uv=False).min() > 1e-6 and all(np.allclose(Vq @ W(k), om * W(k + Q3) @ Vq) for k in rng.uniform(-np.pi, np.pi, (3, 3))):
            found.append((om, len(nb)))
check("k -> k + pi(1,1,1) is realised by a genuine on-site operator, V W(k) V^-1 = w W(k+Q) (a Q-type taste mapping k* <-> -k* only)",
      bool(found), f"(w, null-space dim): {found}")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time()-t0:.0f}s]")
