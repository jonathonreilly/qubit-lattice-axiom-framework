#!/usr/bin/env python3
"""C8 part 1: momentum-shifting (doubled-cell) phased-permutation letters.  Model: c8lib (b26lib/chklib/chk_model, read-only).
(a) D_Q covariance: G_g D_Q G_g^-1 = D_{R_g Q}; so a single-Q letter is O-covariant up to a character only if Q in {0, Pi},
    Pi = pi(1,1,1).  D_Pi commutes with every G_g, S^a, A0 and the on-site palette, anticommutes with R_L and Rt; k*+Pi = -k*.
    Hence single-Q letters = z D_Pi S^a, z D_Pi A0 S^a (B26 theorem applied to D_Pi X) and every translation-invariant word
    in them is +- an old (B26-palette) word; D_Pi W(k) D_Pi = W(k+Pi) = (-1)^{n_R} W(k): the known Pi-taste.
(b) Orbits and stabilisers of modes under O x 2Z^3 (doubled cell).
(c) Exhaustive range<=1 orbit-piece enumeration (group averages, both characters) vs the stabiliser prediction.
(d) Range-0 doubled-cell letters G0 (all 2 x 64 perm choices x 4^6 orbit phases): translation-invariant members; the
    translation-invariant symmetric conjugates P R_L P^-1, P Rt P^-1; their reduction to old letters and k* velocity."""
import sys, time
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
t0 = time.time()
from c8lib import *
PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)

# ---------------- (a) single-Q letters
Dq = {q: DQ(q) for q in SUBL}
ok = True
for (P, s), Rm_ in zip(rots, ROTS):
    for q in SUBL:
        rq = tuple(int(x) % 2 for x in np.abs(Rm_ @ np.array(q)))
        ok &= np.allclose(conj(Dq[q], P, s), Dq[rq])
check("G_g D_Q G_g^-1 = D_{R_g Q} for all 24 dressed rotations and 8 Q (gauge signs cancel)", ok)
orb = {}
for q in SUBL:
    o = frozenset(tuple(int(x) % 2 for x in np.abs(R @ np.array(q))) for R in ROTS); orb[o] = 1
sizes = sorted(len(o) for o in orb)
fixed = [q for q in SUBL if all(tuple(int(x) % 2 for x in np.abs(R @ np.array(q))) == q for R in ROTS)]
check("O-orbits of Q in pi{0,1}^3 are {0}, {Pi}, {pi e_i}, {pi(e_i+e_j)}; O-fixed Q are exactly 0 and Pi", sizes == [1, 1, 3, 3] and sorted(fixed) == [(0, 0, 0), (1, 1, 1)], f"sizes {sizes}")
Dpi = Dq[(1, 1, 1)]
A0r = onsite_real(A0)
onsite_ok = all(np.allclose(Dpi @ onsite_real(M) @ Dpi, onsite_real(M)) for M in [PC['H13'], PC['L123'], A0])
check("D_Pi commutes with S, A0 and on-site letters; anticommutes with R_L and Rt = A0 R_L A0^-1",
      np.allclose(Dpi @ Sr @ Dpi, Sr) and onsite_ok and np.allclose(Dpi @ RLr @ Dpi, -RLr) and np.allclose(Dpi @ (A0r @ RLr @ A0r.T) @ Dpi, -(A0r @ RLr @ A0r.T)))
check("k* + Pi = -k* (mod 2 pi)", np.allclose(wrap(kst + np.pi * np.ones(3)), wrap(-kst)))
rng = np.random.default_rng(11); ok = True
for _ in range(20):
    k = rng.uniform(-np.pi, np.pi, 3); w = ['S', 'R', PC['L132'], 'Si', 'Rt', PC['H21'], 'S2']
    ok &= np.allclose(Wb(w, (k + np.pi * np.ones(3))[None])[0], (-1) ** nR(w) * Wb(w, k[None])[0])
check("every old word obeys W(k+Pi) = (-1)^{n_R} W(k) (the D_Pi 'letter' is the known Pi-taste, B18/B20)", ok)

# ---------------- (b) doubled-cell orbits
G = G2_elements()
check("|O x 2Z^3| on L=4 = 192 and every element is a signed mode permutation", len(G) == 192 and all(len(set(P)) == nV for P, _, _ in G))
seen = -np.ones(nV, int); orbits = []
for a in range(nV):
    if seen[a] >= 0: continue
    o = sorted(set(int(P[a]) for P, _, _ in G)); orbits.append(o)
    for b in o: seen[b] = len(orbits) - 1
def desc(a):
    v, c = VERTS[a]; return (tuple(int(x) % 2 for x in v), tuple(sorted(c)))
orbinfo = []
for o in orbits:
    a = o[0]; stab = sum(1 for P, _, _ in G if P[a] == a); v, c = VERTS[a]
    s = tuple(int(x) % 2 for x in v); cls = sum(s)
    # for s with one or two odd coords: is the corner "parallel" (contains the special axis) or "perpendicular"?
    axis = None
    if cls == 1: axis = [i for i in range(3) if s[i] == 1][0]
    if cls == 2: axis = [i for i in range(3) if s[i] == 0][0]
    par = None if axis is None else any(abs(d[axis]) == 1 for d in c)
    orbinfo.append((cls, par, len(o) // 8, stab))
    print(f"  orbit: sublattice class |s|={cls}, corner contains special axis={par}: {len(o) // 8} modes per doubled cell, stabiliser order {stab}")
exp = sorted([(0, None, 12, 2), (3, None, 12, 2), (1, False, 12, 2), (1, True, 24, 1), (2, False, 12, 2), (2, True, 24, 1)], key=str)
check("6 mode orbits per doubled cell: 000, 111, 100-perp, 110-perp (12 modes, stabiliser C2') and 100-par, 110-par (24 modes, free)",
      sorted(orbinfo, key=str) == exp)

# ---------------- (c) range<=1 orbit pieces
reps = [o[0] for o in orbits]; free = {i for i, x in enumerate(orbinfo) if x[3] == 1}
DISP1 = list(itertools.product((-1, 0, 1), repeat=3))
cnt = collections.Counter(); pieces0 = {}; mism = 0
for oi, m0 in enumerate(reps):
    v0, c0 = VERTS[m0]
    for d in DISP1:
        for cc in CORN:
            t = vid(np.add(v0, d), cc)
            for twist in (False, True):
                X = gavg(m0, t, twist, G)
                ok = is_partial_phased_perm(X) if X else False
                if ok:
                    # bijective onto an orbit of the same size?
                    imgs = {k[0] for k in X}; srcs = {k[1] for k in X}
                    ok = len(imgs) == len(srcs) == len(orbits[oi])
                cnt[(oi, ok)] += 1
                # stabiliser prediction: free source orbit -> valid iff target lies in a free orbit
                if oi in free:
                    pred = seen[t] in free
                    if pred != ok: mism += 1
                if ok and d == (0, 0, 0): pieces0.setdefault(oi, []).append((twist, cc, X))
for oi in range(len(orbits)):
    print(f"  orbit {oi} {orbinfo[oi]}: range<=1 targets x 2 characters = {cnt[(oi, True)] + cnt[(oi, False)]}, valid pieces {cnt[(oi, True)]}")
check("free-orbit sources: a range<=1 target gives a (bijective) piece iff the target lies in a free orbit, for both characters (stabiliser argument)", mism == 0, f"mismatches {mism}")
stabok = True
for oi in range(len(orbits)):
    if oi in free: continue
    # C2'-stabiliser orbits: valid targets have exactly one admissible character each
    tw = collections.Counter()
    m0 = reps[oi]; v0, c0 = VERTS[m0]
    for d in DISP1:
        for cc in CORN:
            t = vid(np.add(v0, d), cc); vs_ = [twist for twist in (False, True) if (lambda X: X and is_partial_phased_perm(X) and len({k[0] for k in X}) == len(orbits[oi]))(gavg(m0, t, twist, G))]
            tw[len(vs_)] += 1
    stabok &= tw[2] == 0
print(f"  range-0 pieces per orbit (twist, target corner): " + str({oi: [(tw, tuple(sorted(cc))) for tw, cc, _ in v] for oi, v in pieces0.items() if oi not in free}))
check("C2'-stabiliser orbits: no target admits both characters (the stabiliser sign fixes chi)", stabok)
n0 = {oi: collections.Counter(tw for tw, _, _ in v) for oi, v in pieces0.items()}
check("range 0: each C2'-orbit has exactly one piece per character (identity for chi=1, antipodal for chi=A2); each free orbit 8 per character",
      all(n0[oi][False] == (8 if oi in free else 1) and n0[oi][True] == (8 if oi in free else 1) for oi in range(6)), str({oi: dict(c) for oi, c in n0.items()}))

# ---------------- (d) range-0 doubled-cell letters, conjugates of R_L / Rt
def sub_blocks(X):
    """X: dict (row,col)->val, range 0: returns p[s] (12x12) for s in SUBL"""
    p = np.zeros((8, 12, 12), complex)
    for (a, b), val in X.items():
        va, ca = VERTS[a]; vb, cb = VERTS[b]
        if any(x >= 2 for x in vb): continue
        si = SUBL.index(tuple(vb)); assert tuple(va) == tuple(vb)
        p[si, CI[ca], CI[cb]] += val
    return p
ORB = np.zeros((8, 12), int)
for si, s in enumerate(SUBL):
    for c in CORN: ORB[si, CI[c]] = seen[vid(s, c)]
pieceblk = {oi: [(tw, cc, sub_blocks(X)) for tw, cc, X in v] for oi, v in pieces0.items()}
for oi in pieceblk:
    pieceblk[oi] = [(tw, cc, b / np.abs(b).max()) for tw, cc, b in pieceblk[oi]]
def letters_G0(twist):
    lists = [[b for tw, cc, b in pieceblk[oi] if tw == twist] for oi in range(6)]
    for choice in itertools.product(*[range(len(x)) for x in lists]):
        yield choice, sum(lists[oi][ci] for oi, ci in enumerate(choice))
# translation-invariant members of G0 (any phases): p_s independent of s up to the orbit phases
ti_members = 0; total = 0; old_ok = True
PH4 = np.array([1, 1j, -1, -1j])
PHV = np.array(list(itertools.product(range(4), repeat=6)))           # 4096 orbit-phase vectors
Zs = PH4[PHV]                                                          # (4096, 6)
for twist in (False, True):
    for choice, p in letters_G0(twist):
        # phases applied per orbit (source orbit = target orbit at range 0): p_s -> diag(z_{ORB[s]}) p_s
        zz = Zs[:, ORB]                                                    # (4096, 8, 12)
        ps = zz[:, :, :, None] * p[None]                                   # (4096, 8, 12, 12)
        eq = np.all(np.abs(ps - ps[:, :1]) < 1e-9, axis=(1, 2, 3))
        total += len(Zs); ti_members += int(eq.sum())
        for j in np.nonzero(eq)[0][:4]:
            q = ps[j, 0]; z = q[np.nonzero(np.abs(q) > 1e-9)][0]
            old_ok &= np.allclose(q / z, np.eye(12)) or np.allclose(q / z, A0) or np.allclose(q / z, -A0)
print(f"  G0: {total} letters (2 characters x 64 perm choices x 4^6 phases); translation-invariant: {ti_members}")
check("translation-invariant members of G0 are exactly z*1 (chi=1) and z*A0 (chi=A2): 4+4 (pure-permutation reduction, range 0)", ti_members == 8 and old_ok)

# conjugates  P M P^-1, M in {R_L, Rt}: blocks y_s(d) = p_{s+d} m(d) p_s^-1 (dmod displacements)
MB = {'R': blL, 'Rt': {d: A0 @ M @ A0i for d, M in blL.items()}}
def conj_blocks(p, mb):
    out = {}
    for d, M in mb.items():
        ys = []
        for si, s in enumerate(SUBL):
            t = tuple((a + b) % 2 for a, b in zip(s, d)); ti = SUBL.index(t)
            ys.append(p[ti] @ M @ p[si].conj().T)
        out[d] = np.array(ys)
    return out
results = {}
t1 = time.time()
for Mname, mb in MB.items():
    for twist in (False, True):
        for choice, p in letters_G0(twist):
            yb = conj_blocks(p, mb)
            # phases: y_s(d)[c',c] -> z_{ORB[s+d,c']} conj z_{ORB[s,c]} y_s(d)[c',c]; translation invariance: equal over s
            okz = np.ones(len(Zs), bool)
            for d, ys in yb.items():
                tsi = [SUBL.index(tuple((a + b) % 2 for a, b in zip(s, d))) for s in SUBL]
                nz = np.abs(ys) > 1e-9
                if not np.all(nz == nz[:1]): okz[:] = False; break
                ii, jj = np.nonzero(nz[0])
                vals = ys[:, ii, jj]                                           # (8, n)
                zt = Zs[:, ORB[tsi][:, ii]]; zsrc = np.conj(Zs[:, ORB[:, jj]])   # (4096, 8, n)
                v = vals[None] * zt * zsrc
                okz &= np.all(np.abs(v - v[:, :1]) < 1e-9, axis=(1, 2))
                if not okz.any(): break
            for j in np.nonzero(okz)[0]:
                z = Zs[j]; y0 = {d: (np.diag(z[ORB[SUBL.index(tuple(x % 2 for x in d))]]) @ ys[0] @ np.diag(np.conj(z[ORB[0]])))
                                 for d, ys in yb.items()}
                key = (Mname, tuple(np.round(np.concatenate([y0[d].ravel() for d in sorted(y0)]), 6)))
                results.setdefault(key, (Mname, twist, choice, y0))
print(f"  conjugate scan done in {time.time() - t1:.0f}s; distinct translation-invariant conjugates: {len(results)}")
# analyse distinct conjugates
def letter_from_blocks(y0):
    sh = np.array(sorted(y0), float); M = np.array([y0[d] for d in sorted(y0)])
    return sh, M
def bloch_of(sh, M, k): return np.einsum('t,tij->ij', np.exp(1j * sh @ k), M)
basis_u = list(ONSITE_BASIS) + [A0 @ B for B in ONSITE_BASIS]
KS = np.random.default_rng(5).uniform(-np.pi, np.pi, (4, 3))
def reducible(sh, M):
    """X = u R u^-1 or u Rt u^-1 with u in span(onsite sym algebra + A0*algebra), u invertible (solve X u = u M0)"""
    for M0 in ('R', 'Rt'):
        rows = []
        for k in KS:
            X = bloch_of(sh, M, k); R0 = RLk(k) if M0 == 'R' else RLt(k)
            rows.append(np.array([(X @ B - B @ R0).ravel() for B in basis_u]).T)
        A = np.vstack(rows); _, sv, Vh = np.linalg.svd(A)
        null = Vh[np.sum(sv > 1e-8):].conj()
        cands = list(null) + ([np.random.default_rng(1).normal(size=len(null)) @ null] if len(null) > 1 else [])
        for vec in cands:
            u = sum(c * B for c, B in zip(vec, basis_u)); sv_u = np.linalg.svd(u, compute_uv=False)
            if sv_u.min() > 1e-6 * sv_u.max(): return (M0, len(null))
    return None
def which_old(sh, M):
    for nm, f in (('R_L', RLk), ('Rt', RLt)):
        for z in (1, -1):
            if all(np.allclose(bloch_of(sh, M, k), z * f(k)) for k in KS): return ('+' if z > 0 else '-') + nm
    return None
nonred = []; vel = []; symok = True
for key, (Mname, twist, choice, y0) in results.items():
    sh, M = letter_from_blocks(y0)
    # O-symmetry in real space
    Xr = np.zeros((nV, nV), complex)
    for a, (v, c) in enumerate(VERTS):
        for d, B in y0.items():
            for ci in range(12):
                if abs(B[ci, CI[c]]) > 1e-12: Xr[vid(np.add(v, d), CORN[ci]), a] += B[ci, CI[c]]
    symok &= all(np.allclose(conj(Xr, P, s), Xr) for P, s in rots) and all(np.allclose(conj(Xr, P, s), Xr) for P, s in trans)
    red = reducible(sh, M)
    if which_old(sh, M) is None: nonred.append(key)
    print(f"   conjugate of {Mname} by G0 letter chi={'A2' if twist else '1'} perm-choice={choice}: reduces to u {red[0] if red else None} u^-1 (solution-space dim {red[1] if red else 0})"
          f"; X in {{+-R_L, +-Rt}}: {which_old(sh, M)}")
    fg = lambda k, sh=sh, M=M: (bloch_of(sh, M, k), [bloch_of(sh, M * 1, k) * 0 + np.einsum('t,tij->ij', 1j * sh[:, j] * np.exp(1j * sh @ k), M) for j in range(3)])
    for kk in (kst, -kst):
        for D in (Dp, Dm):
            isc, sc, h = compressed_velocity(fg, kk, D); iso, v = iso_speed(h); vel.append((isc, iso, v))
check("every translation-invariant conjugate P M P^-1 is O-symmetric and translation invariant in real space (L=4)", symok, f"{len(results)} distinct")
check("every translation-invariant conjugate P R_L P^-1 / P Rt P^-1 (range-0 P in G0, all 524288) is one of +-R_L, +-Rt (old letters)",
      len(nonred) == 0, f"non-reducible: {len(nonred)}")
check("every such conjugate is scalar on D+ and D- at +-k* with zero compressed derivative (no new velocity source)",
      all(isc and v < 1e-9 for isc, iso, v in vel), f"max speed {max(v for _, _, v in vel):.1e}")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}   [{time.time() - t0:.0f}s]")
