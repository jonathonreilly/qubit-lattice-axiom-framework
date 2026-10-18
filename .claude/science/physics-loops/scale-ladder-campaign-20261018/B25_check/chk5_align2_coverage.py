#!/usr/bin/env python3
"""B25_check part 5: does B25's explicit ALIGN2 mechanism (P' = PL(-phi), cyclic rotation) cover all 28 census words with a
k-dependent taste?  Independent build (corelib).  For each census ALIGN2 word W = S^a P S^a G S^a P' S^a G with kdep > 0:
  (A) rotation mechanism (B25 kdep_mechanism.py):  W(k+t_Y) = V W_rot(k) V^-1, W_rot = S^a P' S^a G S^a P S^a G, constant V;
  (B) transpose-cyclic mechanism (found here):    W(k+t_Y) = V W'(k) V^-1, W' = S^a P^T S^a G S^a P'^T S^a G, constant V, and
      W'(k)^T = G^T S^a P' S^a G^T S^a P S^a  (P^T^T = P), which for G^T = +-G is +- a cyclic rotation of W(k): spec W' = spec W.
Prints PASS/FAIL, TOTAL."""
import sys, os, pickle, collections
import numpy as np
import corelib as cl
PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)
W1 = lambda w, k: cl.Wc(w, np.asarray(k, float)[None])[0]
ks = np.random.default_rng(55).uniform(-np.pi, np.pi, (5, 3)); kv = np.random.default_rng(56).uniform(-np.pi, np.pi, (4, 3))
def const_inter(Af, Bf):
    rows = [np.kron(Af(k), np.eye(12)) - np.kron(np.eye(12), Bf(k).T) for k in ks]
    _, s, vh = np.linalg.svd(np.vstack(rows)); null = vh[np.sum(s > 1e-9 * s[0]):].conj()
    if not len(null): return None
    V = ((np.random.default_rng(1).normal(size=len(null)) + 1j * np.random.default_rng(2).normal(size=len(null))) @ null).reshape(12, 12)
    if np.linalg.svd(V, compute_uv=False)[-1] < 1e-6 * np.linalg.norm(V, 2): return None
    return V if all(np.allclose(Af(k) @ V, V @ Bf(k), atol=1e-8) for k in kv) else None
def plane_phase(n):
    M = cl.letter_const(n)
    for m in range(12):
        if np.allclose(M, cl.PL(np.pi * m / 6)): return m
    return None
R = pickle.load(open(os.path.join(cl.HERE, '..', 'B25_spectral_tastes', 'census.pkl'), 'rb'))['R']
kd = [(j, r) for j, r in R if r and r.get('Lu') and r['kdep'] > 0 and j[0] == 'ALIGN2']
print(f"   census ALIGN2 words with a k-dependent coset: {len(kd)}")
stat = collections.Counter(); allok = True
for j, r in kd:
    sk, nm = j[1], j[2]; a = sk[0]; P, G, Pp = nm[0], nm[1], nm[2]
    mP, mPp = plane_phase(P), plane_phase(Pp); Gm = cl.letter_const(G)
    asum0 = (mP + mPp) % 12 == 0
    Gsym = np.allclose(Gm.T, Gm) or np.allclose(Gm.T, -Gm)
    pw = cl.POW[a]; t = np.pi / (2 * abs(pw)) * np.ones(3)
    w = cl.build(sk, nm)
    Pm, Ppm = cl.letter_const(P), cl.letter_const(Pp)
    wrot = [a, Ppm, a, Gm, a, Pm, a, Gm]; wpr = [a, Pm.T, a, Gm, a, Ppm.T, a, Gm]
    VA = const_inter(lambda k: W1(w, k + t), lambda k: W1(wrot, k))
    VB = const_inter(lambda k: W1(w, k + t), lambda k: W1(wpr, k))
    # W'^T vs cyclic rotation of W (exact identity check at random k): W'^T = G^T a P' a G^T a P a
    rotW = [a, Ppm, a, Gm, a, Pm, a, Gm]                # S P' S G S P S G  ~ cyclic rotation of W
    ident = Gsym and all(np.allclose(W1(wpr, k).T, (1 if np.allclose(Gm.T, Gm) else 1) * W1([Gm.T, a, Ppm, a, Gm.T, a, Pm, a], k)) for k in ks)
    specB = all(np.allclose(np.sort_complex(np.round(np.linalg.eigvals(W1(wpr, k)), 9)), np.sort_complex(np.round(np.linalg.eigvals(W1(w, k)), 9))) for k in ks)
    mech = ('A' if VA is not None else '') + ('B' if VB is not None and ident else '')
    stat[(asum0, Gsym, mech)] += 1
    allok &= bool(mech)
    print(f"   {'.'.join(sk)} {nm}: phi+phi' = 0 mod 2pi {asum0}; G^T=+-G {Gsym}; mechanism {mech or 'NONE'}; spec W' = spec W {specB}")
print("   (phi'=-phi, G symmetric, mechanisms) ->", dict(stat))
check("every census k-dependent ALIGN2 word is explained by mechanism A or B (constant V, verified out-of-sample)", allok and len(kd) == 28, f"{len(kd)} words")
nA = sum(v for (s0, gs, m), v in stat.items() if 'A' in m)
check("B25's explicit mechanism (A: P' = PL(-phi)) covers only part of them; the rest need the transpose-cyclic mechanism B (G^T = +-G)",
      0 < nA < len(kd), f"A covers {nA}/{len(kd)}")
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
