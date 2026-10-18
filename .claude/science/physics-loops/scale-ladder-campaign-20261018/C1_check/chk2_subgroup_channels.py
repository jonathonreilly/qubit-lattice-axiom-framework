#!/usr/bin/env python3
"""C1 check, adversarial part of claim 2: pairing channels that keep only a SUBGROUP H of O (a multi-dim pair irrep with
one component chosen, U(1)-dressed).  For every subgroup H of O and every 1-dim character chi of H, the on-site Q = R channel
{A antisym: U_g A U_g^T = chi(g) A, g in H} and the pattern of node singlets that H forces to vanish.
Then a Floquet-BdG test of the selective channel(s) found (T with complex chi = omega), on-site and range-1."""
import time, cmath
from cklib import *
t0 = time.time(); PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)
rng = np.random.default_rng(77)
MUL = {}
for a in PROPER:
    for b in PROPER: MUL[(a, b)] = find_el(OH[a] @ OH[b])
E0 = find_el(np.eye(3, dtype=int))
def closure(gens):
    S = {E0} | set(gens); ch = True
    while ch:
        ch = False
        for a in list(S):
            for b in list(S):
                c = MUL[(a, b)]
                if c not in S: S.add(c); ch = True
    return frozenset(S)
subs = set()
for a in PROPER:
    for b in PROPER: subs.add(closure([a, b]))
subs = sorted(subs, key=len)
print(f"subgroups of O found: {len(subs)} (orders {sorted(set(len(s) for s in subs))})")
def characters(H):
    H = sorted(H); gens = []
    cur = frozenset([E0])
    for h in H:
        if h not in cur: gens.append(h); cur = closure(gens)
    roots = [cmath.exp(2j * np.pi * m / 12) for m in range(12)]
    out = []
    for vals in itertools.product(roots, repeat=len(gens)):
        chi = {E0: 1.0}; frontier = [E0]; ok = True
        while frontier and ok:
            new = []
            for x in frontier:
                for gi, gv in zip(gens, vals):
                    y = MUL[(x, gi)]; v = chi[x] * gv
                    if y in chi:
                        if abs(chi[y] - v) > 1e-9: ok = False; break
                    else: chi[y] = v; new.append(y)
                if not ok: break
            frontier = new
        if ok and all(abs(chi[MUL[(a, b)]] - chi[a] * chi[b]) < 1e-9 for a in H for b in H):
            if not any(all(abs(c[g] - chi[g]) < 1e-9 for g in H) for c in out): out.append(chi)
    return out
DQ = {n: node_doublet(n) for n in NODES}
def pattern(H, chi):
    V = onsite_channel(chi, idx=sorted(H))
    if not V: return None, 0
    allowed = {}
    for n in NODES:
        allowed[n] = max(abs(singlet(DQ[n], 2 * X)) for X in V) > 1e-9
    return allowed, len(V)
def is_T(H): return len(H) == 12
selective = []; table = []
for H in subs:
    cls_counts = {}
    for g in H: cls_counts[cls(OH[g])] = cls_counts.get(cls(OH[g]), 0) + 1
    for chi in characters(H):
        al, dim = pattern(H, chi)
        if al is None: continue
        ks = al[(0, 0, 0)] or al[(1, 1, 1)]; nd = sum(al[n] for n in DOUB)
        table.append((len(H), cls_counts, ks, nd))
        if not ks and nd > 0:
            selective.append((len(H), dict(cls_counts), {g: chi[g] for g in H}, nd, dim, H, chi))
print(f"(H, chi) pairs with a non-empty on-site channel: {len(table)}")
summary = {}
for s in selective:
    key = (s[0], tuple(sorted(s[1].items())), s[3]); summary[key] = summary.get(key, 0) + 1
for key, c in sorted(summary.items()):
    print(f"   SELECTIVE (+-k* forbidden, {key[2]} doublers allowed): |H|={key[0]} classes={dict(key[1])}  x{c}")
fullT = [s for s in selective if s[0] == 12 and s[3] == 6]
check("X1 (adversarial) selective symmetric-subgroup channels EXIST: with O broken to T (C4, C2' broken; C3 U(1)-dressed, chi(C3) = omega), "
      "the Q = R on-site singlet is forbidden at +-k* and allowed at all six doublers", len(fullT) >= 1,
      f"{len(fullT)} (T, chi) channels; complex chi: {[np.round([c for g, c in s[2].items() if cls(OH[g]) == 'C3'][:1], 3).tolist() for s in fullT]}")
no_O = all(s[0] != 24 for s in selective)
check("X1b no selective channel with H = O (C1's PSG-symmetric statement confirmed); selective channels need |H| <= 12", no_O)

# ---------------- BdG test of the T-omega channel ----------------
Hs, chiT = fullT[0][5], fullT[0][6]
VT = onsite_channel(chiT, idx=sorted(Hs)); print(f"   T-omega on-site channel dim {len(VT)}")
A = sum((rng.normal() + 1j * rng.normal()) * X for X in VT); A /= np.linalg.norm(A)
assert all(np.allclose(UF[g] @ A @ UF[g].T, chiT[g] * A) for g in Hs)
broken = [g for g in PROPER if g not in Hs]
print("   broken check: max over C4/C2' of min_c ||U A U^T - c A|| / ||A|| :", f"{min(np.linalg.norm(UF[g] @ A @ UF[g].T - c * A) for g in broken[:1] for c in [1, -1, 1j, -1j, chiT[MUL[(broken[0], broken[0])]] ** 0.5]):.3f}")
Don = lambda ks: np.broadcast_to(A, (len(np.atleast_2d(ks)), 12, 12)).copy()
tau = 0.5
mK = {n: abs(singlet(DQ[n], 2 * A)) for n in NODES}
print("   first-order node singlets |m_K|:", ", ".join(f"{NAME[n]}:{v:.3e}" for n, v in mK.items()))
gK = {n: gap0(NODES[n], Don, tau, QR)[0] for n in NODES}
print("   BdG |eps|_min at the nodes:", ", ".join(f"{NAME[n]}:{v:.3e}" for n, v in gK.items()))
# near +-k*: radial scan of the quasi-energy-0 gap along many directions
def radial(n, Dfun, tau, rs=np.linspace(0, 0.3, 61), ndir=30):
    dirs = rng.normal(size=(ndir, 3)); dirs /= np.linalg.norm(dirs, axis=1)[:, None]
    ks = np.array([NODES[n] + r * d for d in dirs for r in rs])
    g = gap0(ks, Dfun, tau, QR).reshape(ndir, len(rs)); return rs, g
for n in ((0, 0, 0), (1, 1, 1)):
    rs, g = radial(n, Don, tau)
    zero_r = [rs[np.argmin(row)] for row in g]
    print(f"   {NAME[n]}: per-direction minimum of |eps| over r<=0.3: max {g.min(axis=1).max():.2e}, at r in [{min(zero_r):.3f}, {max(zero_r):.3f}]")
dbl = min(gK[n] for n in DOUB)
check("X2 T-omega on-site pairing (tau=0.5): first-order singlet exactly zero at +-k*, nonzero at the six doublers; the six doublers are gapped",
      max(mK[(0, 0, 0)], mK[(1, 1, 1)]) < 1e-12 and min(mK[n] for n in DOUB) > 1e-3 and dbl > 1e-2, f"min doubler gap {dbl:.4f}")
z_k = gK[(0, 0, 0)] < 1e-9 and gK[(1, 1, 1)] < 1e-9
print("   exact BdG zero at +-k*:", z_k)
# cone test at +-k* (small q) and Bogoliubov-Fermi-surface test
cone = []
for n in ((0, 0, 0), (1, 1, 1)):
    for _ in range(12):
        d = rng.normal(size=3); d /= np.linalg.norm(d); q = 1e-4
        ev = np.sort(np.abs(bdg_eps(NODES[n] + q * d, Don, tau, QR)[0]))[:4]; cone.append(ev / q)
cone = np.array(cone)
print(f"   +-k* small-q |eps|/q (4 lowest BdG bands): range [{cone.min():.6f}, {cone.max():.6f}]   (sqrt2/3 = {np.sqrt(2)/3:.6f})")
for tt in (0.1, 0.3, 0.5, 1.0):
    print(f"   tau={tt}: |eps|(+-k*) = {gap0(NODES[(0,0,0)], Don, tt, QR)[0]:.2e}, {gap0(NODES[(1,1,1)], Don, tt, QR)[0]:.2e}; doubler gap {min(gap0(NODES[n], Don, tt, QR)[0] for n in DOUB):.4f}")
check("X3 T-omega on-site: +-k* remain EXACT BdG zeros for all tau tested (protected by the residual T, no tuning)", z_k and
      all(gap0(NODES[n], Don, tt, QR)[0] < 1e-9 for n in ((0, 0, 0), (1, 1, 1)) for tt in (0.1, 0.3, 1.0)))
iso = np.allclose(cone, np.sqrt(2) / 3, atol=5e-4)
print("   isotropic cone at sqrt2/3:", iso)
(b0, k0), (bp, kp) = grid_min(Don, tau, QR, N=20, exclude=(KST, -KST), r_ex=0.35)
print(f"   global scan outside 0.35-balls of +-k* (N=20): min 0-gap {b0:.4f}, min pi-gap {bp:.4f}")
check("X4 T-omega on-site: small-q BdG spectrum at +-k* is an isotropic 4-band cone at sqrt2/3 (pairing enters only at O(q^2)) and no "
      "other quasi-energy-0/pi zero outside the balls (grid N=20; numerical, uncertified)", iso and b0 > 1e-3 and bp > 1e-3)
# range-1 T-omega pairing
blT = sym_pair(rand_blocks(rng, 1), chiT, QR, idx=sorted(Hs))
assert check_sym(blT, chiT, QR, idx=sorted(Hs), rng=rng)
nrm = np.linalg.norm(Delta(blT, QR, KST)[0]) + 1e-12
Dr = lambda ks: Delta(blT, QR, ks) / nrm
gr = {n: gap0(NODES[n], Dr, 0.3, QR)[0] for n in NODES}
print("   range-1 T-omega: BdG |eps| at nodes:", ", ".join(f"{NAME[n]}:{v:.2e}" for n, v in gr.items()))
for n in ((0, 0, 0), (1, 1, 1)):
    rs, g = radial(n, Dr, 0.3, rs=np.linspace(0, 0.2, 41), ndir=20)
    print(f"   range-1 {NAME[n]}: min over directions of max_r... per-direction min |eps| (r<=0.2): {g.min(axis=1).max():.2e}")
check("X5 range-1 T-omega pairing: +-k* exact BdG zeros, six doublers gapped", max(gr[(0, 0, 0)], gr[(1, 1, 1)]) < 1e-9 and min(gr[n] for n in DOUB) > 1e-3)
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time()-t0:.0f}s]")
