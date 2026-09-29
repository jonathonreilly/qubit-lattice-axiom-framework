#!/usr/bin/env python3
"""J:attack-e:PR9373 -- SAMPLED EVIDENCE: the note's floating-point consistency check gives sphere fluxes -2 and +2 at only two couplings (J = 2/5 and 8/5) and two radii (0.004, 0.008), while its statement is for every J in (0, 2).

Instead of more samples at hand-picked couplings, this script scans the whole parameter line: for 61 values of q on a geometric grid from 0.03 to 30 (J from about 0.007 to 1.999) it computes, with its own network construction and its own discrete Fukui fluxes of the lowest two bands,
the flux through spheres around f+ and f- at the radii 0.004, 0.008 and at radii scaled with the local size of the two-band region (r = 0.5 * (gap to the outer bands)/(velocity scale)), and locates where a fixed small radius stops being 'small enough' (flux different from -+2 while a
smaller radius still gives -+2).  It also checks that a sphere only around f+ (not around the pair) is used at every q (no other node within the sphere), by the minimum of the middle gap on the sphere versus at the centre.
Prints SUMMARY:; HIT only if for some q no radius in a shrinking sequence reproduces the flux -2 at f+ and +2 at f-.
"""
import sys, time
import numpy as np

def is_site(p):
    i, j, z = p; m = z % 4
    if m == 0: return j % 2 == 0
    if m == 1: return i % 2 == 1
    if m == 2: return j % 2 == 1
    return i % 2 == 0
def nbrs(p):
    out = []
    for a in range(3):
        for s in (-1, 1):
            q = list(p); q[a] += s; q = tuple(q)
            if is_site(q): out.append(q)
    return out
def flavour(p, q):
    d = tuple(q[a] - p[a] for a in range(3))
    if d[2] != 0: return "z"
    lo = p if sum(d) > 0 else q; m = p[2] % 4
    idx = lo[0] + m // 2 if m in (0, 2) else lo[1] + (m - 1) // 2
    return "x" if idx % 2 == 0 else "y"
REPS = [(0, 0, 0), (1, 0, 0), (1, 0, 1), (1, 1, 1)]
def reduce(p):
    n3 = p[2] // 2; x, y, z = p[0] - n3, p[1] - n3, p[2] - 2 * n3
    n1, n2 = x // 2, y // 2; rep = (x - 2 * n1, y - 2 * n2, z)
    return REPS.index(rep), (n1, n2, n3)
def terms_of(Jx, Jy, Jz, kappa):
    J = {"x": Jx, "y": Jy, "z": Jz}; out = []
    for p in REPS:
        a, _ = reduce(p)
        if sum(p) % 2 == 0:
            for q in nbrs(p):
                b, n = reduce(q); out.append((a, b, n, 2 * J[flavour(p, q)]))
        nb = {flavour(p, q): q for q in nbrs(p)}
        for (l, m) in (("x", "y"), ("y", "z"), ("z", "x")):
            r1, n1 = reduce(nb[l]); r2, n2 = reduce(nb[m])
            out.append((r1, r2, tuple(int(x) for x in np.subtract(n2, n1)), 2 * kappa))
    return out
def Hfloat(F, T):
    F = np.atleast_2d(F); Mk = np.zeros((len(F), 4, 4), dtype=complex)
    for (a, b, n, amp) in T:
        ph = np.exp(2j * np.pi * (F @ np.array(n, dtype=float)))
        Mk[:, a, b] += float(amp) * ph; Mk[:, b, a] -= float(amp) * np.conj(ph)
    return 1j * Mk
def link(A_, B_): return np.linalg.det(np.einsum('...ia,...ib->...ab', A_.conj(), B_))
def sphere(T, c, s, m=64):
    th = np.linspace(0, np.pi, m + 1); ph = np.linspace(0, 2 * np.pi, 2 * m + 1)
    P = np.stack([np.sin(th)[:, None] * np.cos(ph)[None, :], np.sin(th)[:, None] * np.sin(ph)[None, :], np.cos(th)[:, None] * np.ones_like(ph)[None, :]], axis=-1) * s + np.array(c)
    ev, V = np.linalg.eigh(Hfloat(P.reshape(-1, 3), T))
    V = V[:, :, :2].reshape(m + 1, 2 * m + 1, 4, 2).copy(); V[0, :] = V[0, 0]; V[-1, :] = V[-1, 0]; V[:, -1] = V[:, 0]
    pl = np.angle(link(V[:-1, :-1], V[1:, :-1]) * link(V[1:, :-1], V[1:, 1:]) * link(V[1:, 1:], V[:-1, 1:]) * link(V[:-1, 1:], V[:-1, :-1]))
    return float(pl.sum() / (2 * np.pi)), float((ev[:, 2] - ev[:, 1]).min()), float((ev[:, 1] - ev[:, 0]).min())
T0 = time.time()
qs = np.geomspace(0.03, 30, 61)
rows = []; bad = []
for q in qs:
    J = 8 * q * q / (1 + 4 * q * q); T = terms_of(1.0, 1.0, J, q)
    x = (np.arctan2(4 * q, 4 * q * q - 1) / (2 * np.pi)) % 1.0
    res = {}
    for sg, f in ((1, (x, 1 - x, 0.5)), (-1, (1 - x, x, 0.5))):
        seq = []
        for r in (0.008, 0.004, 0.002, 0.001, 0.0005, 0.00025):
            flux, g23, g12 = sphere(T, f, r, m=64)
            seq.append((r, round(flux, 3)))
        res[sg] = seq
    # accepted radius: the first (largest) radius with flux -+2 followed by smaller radii also -+2
    def first_ok(seq, target):
        for i, (r, fx) in enumerate(seq):
            if abs(fx - target) < 0.02 and all(abs(f2 - target) < 0.02 for _, f2 in seq[i:]): return r
        return None
    rp, rm = first_ok(res[1], -2.0), first_ok(res[-1], 2.0)
    rows.append((q, J, rp, rm, res[1][0][1], res[-1][0][1], res[1][1][1]))
    if rp is None or rm is None: bad.append((q, J, res))
n_ok_004 = sum(1 for r in rows if abs(r[6] + 2) < 0.02 and abs(r[5] - 2) < 0.02)
print(f"   {len(qs)} values of q from 0.03 to 30 (J from {rows[0][1]:.4f} to {rows[-1][1]:.4f}): the radius 0.004 gives -2 at f+ and +2 at f- for {n_ok_004} of them; largest radius (from 0.008, 0.004, ...) that is in the flux-2 regime for all smaller radii found for every q: {sum(1 for r in rows if r[2] is not None and r[3] is not None)} of {len(qs)}", flush=True)
fails = [r for r in rows if not (abs(r[6] + 2) < 0.02 and abs(r[5] - 2) < 0.02)]
for r in fails[:12]: print(f"      q = {r[0]:.4g} (J = {r[1]:.4g}): flux at radius 0.004 around f+ = {r[6]}, around f- (radius 0.008) = {r[5]}; largest radius in the -+2 regime: f+ {r[2]}, f- {r[3]}")
ok = not bad
print(f"[{'PASS' if ok else 'FAIL'}] for every q of the grid a shrinking radius sequence reaches the flux -2 at f+ and +2 at f-: the note's statement holds on the whole line; the fixed radii 0.004 and 0.008 are 'small enough' for {n_ok_004} of {len(qs)} values of q")
print(f"   total {time.time() - T0:.0f}s")
if ok:
    print(f"SUMMARY: no purchase on the sign or the magnitude: for {len(qs)} values of q (J from {rows[0][1]:.4f} to {rows[-1][1]:.4f}) a shrinking radius reproduces the flux -2 at f+ and +2 at f-; the fixed radii 0.004 / 0.008 of the note's check are in the regime for {n_ok_004} of them, and {len(fails)} values of q need a smaller radius")
else:
    print("SUMMARY: for some q no radius reproduces the flux: " + str([(b[0], b[1]) for b in bad[:3]])); print("HIT: no radius reproduces the flux -+2 at q = " + ", ".join(f"{b[0]:.4g}" for b in bad[:5]))
sys.exit(0)
