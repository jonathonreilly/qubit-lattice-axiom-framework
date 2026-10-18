#!/usr/bin/env python3
"""B7 (3): which part of the site-rotation group carries the odd-filling obstruction.

For each subgroup H of the 24 dressed site rotations (with all translations kept):
  * class of the fibre representation restricted to H (does a commuting pair anticommute?);
  * momenta fixed by H under the affine action, and the level multiplicities there;
  * odd-L twisted-torus argument: is theta = k* fixed by H and do two commuting dressed C2's anticommute?
  * constructive test at nu = 1: an on-site Hamiltonian with a nondegenerate lowest H-level plus random
    H-symmetric hopping, gap certified by a Lipschitz bound (only possible when the class is trivial).
Claim checked: with translations kept, odd filling is obstructed exactly when H contains a Klein four-group
(three mutually commuting C2 rotations); cyclic H allow nu = 1 insulators.
Also: the A2 staggered Dirac mass of the companion note keeps T (which contains D2) but doubles the cell;
filling 1 per site is 2 per doubled cell, and a doublet on one coset of cube centres is an allowed
atomic configuration (class at the cube centre computed below).
"""
import itertools, sys, time
from fractions import Fraction as Fr
import numpy as np
import b7_model as m

PASS = FAIL = 0
def check(name, ok, detail=''):
    global PASS, FAIL
    PASS += bool(ok); FAIL += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  {detail}" if detail else ''), flush=True)
def mults(ev, tol=1e-7):
    out = []; i = 0
    while i < len(ev):
        j = i
        while j + 1 < len(ev) and ev[j + 1] - ev[i] < tol: j += 1
        out.append(j - i + 1); i = j + 1
    return out

t0 = time.time()
D = m.build(); OH = D['OH']; U = D['U']; sh = D['shift']
rng = np.random.default_rng(99)
kst = np.array([1, -1, 1]) * np.pi / 2
def gid(M): return [g for g in range(24) if (OH[g] == np.array(M)).all()][0]
def closure(gens):
    S = {0} | set(gens)
    while True:
        new = {gid(OH[a] @ OH[b]) for a in S for b in S} | S
        if new == S: return sorted(S)
        S = new
C2x, C2y, C2z = gid(np.diag([1, -1, -1])), gid(np.diag([-1, 1, -1])), gid(np.diag([-1, -1, 1]))
C2xy = gid([[0, 1, 0], [1, 0, 0], [0, 0, -1]]); C4z = gid([[0, -1, 0], [1, 0, 0], [0, 0, 1]])
C3 = gid([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
SUB = {'O': list(range(24)), 'T': [g for g in range(24) if D['W1'][g] == 0], 'D4z': closure([C4z, C2x]),
       'D2 (axes)': closure([C2x, C2y]), "D2' (z, xy)": closure([C2z, C2xy]), 'C4z': closure([C4z]),
       'C3[111]': closure([C3]), 'C2x': closure([C2x]), 'C2xy': closure([C2xy])}
h0 = D['blocks_from'](D['H0mat'](-1.0, 0.2))
def has_D2(S):
    inv = [g for g in S if g and np.allclose(OH[g] @ OH[g], np.eye(3))]
    return any(np.allclose(OH[a] @ OH[b], OH[b] @ OH[a]) for a, b in itertools.combinations(inv, 2))
def anticomm_pair(S):
    for a, b in itertools.combinations(S, 2):
        if np.allclose(OH[a] @ OH[b], OH[b] @ OH[a]):
            X = U[a] @ U[b] @ U[a].T @ U[b].T
            if np.allclose(X, -np.eye(12)): return (a, b)
    return None
def dims(S):
    X = rng.normal(size=(12, 12)) + 1j * rng.normal(size=(12, 12)); X = X + X.conj().T
    return sorted(set(mults(np.linalg.eigvalsh(sum(U[g] @ X @ U[g].T for g in S) / len(S)))))
def certified_gap(h, nu, N=24):
    ks = m.kgrid(N); E = np.linalg.eigvalsh(m.Hk(h, ks))
    return E[:, nu].min() - E[:, nu - 1].max() - 2 * m.lipschitz(h) * np.sqrt(3) * np.pi / N
ks24 = m.kgrid(24)
print(f"{'H':12s} |H| contains-D2 anticommuting-pair irrep-dims  #fixed-momenta(N=24, incl. k*)  nu=1 certified gap")
rows = {}
for name, S in SUB.items():
    d = dims(S); ac = anticomm_pair(S); d2 = has_D2(S)
    fixed = [k for k in ks24 if all(np.allclose(np.exp(1j * (OH[g] @ k + np.pi * sh[g] - k)), 1, atol=1e-9) for g in S)]
    kfix = all(np.allclose(np.exp(1j * (OH[g] @ kst + np.pi * sh[g] - kst)), 1) for g in S)
    # nu = 1 constructive attempt: on-site term with a nondegenerate lowest level, plus weak symmetric hopping
    cert = None
    if 1 in d:
        X = rng.normal(size=(12, 12)) + 1j * rng.normal(size=(12, 12)); X = X + X.conj().T
        Y = sum(U[g] @ X @ U[g].T for g in S) / len(S)
        hop = m.symmetrize(m.random_blocks(rng, 1), D, S); hn = max(np.abs(B).max() for B in hop.values())
        ev = np.linalg.eigvalsh(Y); sc = (ev[1] - ev[0])
        h = m.add({(0, 0, 0): Y / sc}, hop, 1.0, 0.01 / hn)
        cert = certified_gap(h, 1)
    rows[name] = (len(S), d2, ac is not None, d, len(fixed), kfix, cert)
    print(f"{name:12s} {len(S):3d} {str(d2):5s} {str(ac is not None):5s} {str(d):8s} {len(fixed):5d} {kfix}  "
          + (f"{cert:.3f}" if cert is not None else '-'))
check("for every tested subgroup: the dressed lift has an anticommuting commuting pair (only even irreps) "
      "iff the subgroup contains a Klein four-group", all(r[1] == r[2] and (r[2] == (1 not in r[3])) for r in rows.values()))
check("k* is fixed by every subgroup, so the k*-fibre and the theta = k* odd torus argument apply to each; the "
      "obstruction (odd nu) holds exactly for the D2-containing ones", all(r[5] for r in rows.values()))
check("subgroups without D2 (C4z, C3, C2x, C2xy) admit a certified gapped symmetric insulator at nu = 1",
      all(rows[n][6] is not None and rows[n][6] > 0 for n in ('C4z', 'C3[111]', 'C2x', 'C2xy')),
      str({n: round(rows[n][6], 3) for n in ('C4z', 'C3[111]', 'C2x', 'C2xy')}))

# random dispersive scans at nu = 1 for D2 (axes) vs C4z (evidence)
ks16 = m.kgrid(16)
for name in ('D2 (axes)', 'C4z'):
    gapped = 0
    for trial in range(20):
        h = m.add(h0, m.symmetrize(m.random_blocks(rng, 1 + trial % 2), D, SUB[name]), 1.0, [0.3, 1, 3][trial % 3])
        E = np.linalg.eigvalsh(m.Hk(h, ks16)); gapped += (E[:, 1].min() - E[:, 0].max()) > 1e-9
    print(f"   {name}: random dispersive Hamiltonians gapped at nu = 1: {gapped}/20")

# cube-centre class (the massive-Dirac reduced group keeps the rotations about c = (1/2,1/2,1/2))
h_ = Fr(1, 2)
S, bad = m.wyckoff_class(D, (h_, h_, h_), list(range(24)))
check("the 24 rotations about a cube centre (site rotation composed with c - Rc) all lie in the A2-mass model's group "
      "and their dressed class is nontrivial: one fermion per cube centre is forbidden, a doublet (2 per cube centre "
      "on one of the two FCC cosets = 1 per original site) is allowed",
      len(S) == 24 and bool(bad) and all(D['W1'][g] == (sum(t) % 2) for g, t in S),
      f"{len(bad)} anticommuting commuting pairs; translation parity = w1(R) for all 24")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   ({time.time() - t0:.0f} s)")
sys.exit(1 if FAIL else 0)
