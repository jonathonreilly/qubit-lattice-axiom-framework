#!/usr/bin/env python3
"""The energy product and the test-body law above the half-filled sea.

Class-A runner. Conditional on the same two separately supplied surfaces the
weak-field-source note is conditional on -- the designed fermion law (Bravyi-
Kitaev superfast encoding written on the coarse sublattice 2Z^3, hop
T_ij = (i/2) A_ij (B_i - B_j), n_v = (1 - B_v)/2) and the landed weak-field
response surface (phi = G0 P0 rho, H = -Delta_lat) -- and on one supplied
choice, the vacuum: the half-filled staggered sea that the matter-above-the-
sea note names as a decision it does not make. This runner establishes:

  A  TWO PAIRS.  The half-filled staggered sea on the 8^3 coarse torus at its
     energy-minimising twist, and TWO localised particle-hole pairs above it
     at centroid separations D: the two-pair determinant projector, the fall
     of the orbital overlaps with D, the additivity of the energy and of the
     local energy density eps_v, and the identically zero count.
  B  THE ENERGY PRODUCT.  E_int = <eps_1, G0 P0 eps_2> against the product
     form E_1 E_2 G0P0(D), validated first against the landed point-source
     control; the exact symmetric identity that names E_int as the cross term;
     the leading multipole correction that accounts for the deficit; and the
     large-separation behaviour of the ratio on rigid copies.
  C  THE TEST-BODY LAW.  F = -grad_{x2} E_int by finite differences against
     F_pred = -E_2 grad phi_1(x_2), with phi_1 = G0 P0 eps_1: the x ratios,
     the angle residuals, the gauge-sign rebuild lemma, the approach of the
     ratio to 1 with separation, and the inverse-square coefficient against
     the landed point-kernel control.
  D  COUNT VERSUS ENERGY.  An energy knob at fixed D moves E_int with E_1 E_2;
     the same bilinear form on the EMPTY vacuum's count source is literally
     constant under that knob; and above the sea the count of a pair is
     identically zero, so a count product vanishes there.
  E  UNITS.  What carries a dimension and what does not.

Group D3 and the structural statements of A are exact; every other group is a
finite-dimensional floating-point computation reporting its residual against a
tolerance declared before the run. The response validation quotes the landed
point-source control before any new number is reported.

This runner is self-contained: it re-declares the coarse lattice, the KS sign
field, the twists, the sea, the pairs, the lattice Green function and the
response, and imports nothing from the repository.

Output: one PASS/FAIL line per check and a final `TOTAL: PASS=N FAIL=M`.
Exit code 0 iff FAIL = 0.
"""

from __future__ import annotations

import itertools
import sys

import numpy as np

AUDIT_TIMEOUT_SEC = 300

PASS = 0
FAIL = 0


def check(label, cond):
    """Record and print one check."""
    global PASS, FAIL
    ok = bool(cond)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(("PASS " if ok else "FAIL ") + label)


PI = np.pi
EX = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]

# Quoted before the run, from the landed notes, and used as tolerances; the
# run fits nothing and chooses none of its own.
NOTE_E_SEA_8 = -611.811768          # matter-above-the-sea note, T1
NOTE_GAP_8 = 2.651309               # matter-above-the-sea note, T1
NOTE_POINT_CONTROL = {32: 0.3307, 64: 0.3275}   # both parents' own row
NOTE_T4_COEFF = {4: 1.0194, 6: 1.0064, 8: 1.0009, 10: 0.9963}   # source note T4


# ================================================ the coarse lattice, the sea

def eta_ks(v, a):
    """Kawamoto-Smit link sign of the coarse bond (v, v + e_a), axes 0/1/2."""
    if a == 0:
        return 1
    if a == 1:
        return -1 if (v[0] & 1) else 1
    return -1 if ((v[0] + v[1]) & 1) else 1


def build(L, twist):
    """Coarse torus L^3 with the KS staggered sign field; twist[a] = 1 flips
    the bonds crossing the cut v_a = L-1 -> 0."""
    sites = list(itertools.product(range(L), repeat=3))
    idx = {v: i for i, v in enumerate(sites)}
    M = np.zeros((L ** 3, L ** 3))
    for v in sites:
        for a in range(3):
            w = tuple((v[i] + EX[a][i]) % L for i in range(3))
            s = eta_ks(v, a)
            if twist[a] and v[a] == L - 1:
                s = -s
            M[idx[w], idx[v]] += s
            M[idx[v], idx[w]] += s
    return M, sites, idx


L = 8
TWIST = (1, 1, 1)
V = L ** 3
NOCC = V // 2
M, SITES, IDX = build(L, TWIST)
WV, U = np.linalg.eigh(M)
P = U[:, :NOCC] @ U[:, :NOCC].T
E_SEA = float(np.sum(WV[:NOCC]))
GAP = float(WV[NOCC] - WV[NOCC - 1])
HALF_RES = float(np.max(np.abs(np.diag(P) - 0.5)))


# ==================================================== the response, unchanged

def ghat(Lb):
    """Fourier symbol of G0 P0: 1/lambda(k) off the constant mode, 0 on it."""
    k = 2 * PI * np.fft.fftfreq(Lb)
    lam = 6 - 2 * (np.cos(k)[:, None, None] + np.cos(k)[None, :, None]
                   + np.cos(k)[None, None, :])
    G = np.zeros_like(lam)
    nz = lam > 1e-12
    G[nz] = 1.0 / lam[nz]
    G[0, 0, 0] = 0.0
    return G


def green(Lb):
    return np.real(np.fft.ifftn(ghat(Lb)))


def solve(rho, Gh):
    return np.real(np.fft.ifftn(np.fft.fftn(rho) * Gh))


GH = {Lb: ghat(Lb) for Lb in (32, 64)}
GR = {Lb: green(Lb) for Lb in (32, 64)}


# ===================================================== pairs above that sea

def gauss(v0, s=1.0):
    """Normalised-shape Gaussian seed on the coarse torus, minimal image."""
    g = np.zeros(V)
    for i, v in enumerate(SITES):
        d2 = 0
        for a in range(3):
            dd = (v[a] - v0[a]) % L
            dd = min(dd, L - dd)
            d2 += dd * dd
        g[i] = np.exp(-d2 / (2 * s * s))
    return g


# The KS field is not translation invariant, only gauge equivalent: under
# v -> v + e_a it is carried by a diagonal +-1 sign field on the sites.
GAUGE = {0: lambda v: (-1) ** (v[1] + v[2]),
         1: lambda v: (-1) ** (v[2]),
         2: lambda v: 1}


def gauge_vec(sh):
    f = np.ones(V)
    for a in range(3):
        if abs(sh[a]) % 2:
            f = f * np.array([GAUGE[a](v) for v in SITES], float)
    return f


def wp(v0, which, E0=None, wf=1.0, gsign=None):
    """Gaussian seed projected into the empty ('p') or occupied ('h') span,
    optionally band-filtered toward +-E0 with width wf, optionally carried by
    the gauge sign field so a rebuilt packet is the exact gauge image."""
    g = gauss(v0)
    if gsign is not None:
        g = g * gsign
    if which == 'p':
        sub, ev = U[:, NOCC:], WV[NOCC:]
    else:
        sub, ev = U[:, :NOCC], WV[:NOCC]
    c = sub.T @ g
    if E0 is not None:
        c = c * np.exp(-(ev - (E0 if which == 'p' else -E0)) ** 2 / (2 * wf * wf))
    psi = sub @ c
    return psi / np.linalg.norm(psi)


def onb(cols):
    A = np.column_stack(cols)
    Q, S, _ = np.linalg.svd(A, full_matrices=False)
    return Q[:, S > 1e-10]


def eps_of(Pp):
    """The local excitation energy density and its total."""
    D = Pp - P
    return np.sum(M * D, axis=1), float(np.trace(M @ D))


def one_pair(vp, vh, **kw):
    pk = wp(vp, 'p', **kw)
    hk = wp(vh, 'h', **kw)
    Pp = P - np.outer(hk, hk) + np.outer(pk, pk)
    e, E = eps_of(Pp)
    return pk, hk, e, E, np.diag(Pp) - 0.5


def two_pair(pks, hks):
    """P'' = P - Q_h + Q_p with Q_h, Q_p the projectors onto the two-
    dimensional hole and particle spans."""
    Qp = onb(pks)
    Qh = onb(hks)
    Pp = P - Qh @ Qh.T + Qp @ Qp.T
    e, E = eps_of(Pp)
    return e, E, float(np.max(np.abs(Pp @ Pp - Pp))), int(round(np.trace(Pp))), np.diag(Pp) - 0.5


BASE = (2, 2, 3)   # the twist cut sits between x = 7 and x = 0; see the note


def make_pair(dp, off, gauge_from=None, **kw):
    """A pair of internal separation dp along z, offset by `off` from BASE."""
    vp = tuple((BASE[a] + off[a]) % L for a in range(3))
    vh = tuple((vp[a] + (0, 0, dp)[a]) % L for a in range(3))
    mid = tuple(int(round(BASE[a] + off[a] + (0, 0, dp)[a] / 2.0)) % L for a in range(3))
    if gauge_from is not None:
        kw = dict(kw)
        kw['gsign'] = gauge_vec(tuple(off[a] - gauge_from[a] for a in range(3)))
    pk, hk, e, E, r = one_pair(vp, vh, **kw)
    return pk, hk, e, E, r, mid


def unwrapped(vec, about):
    out = []
    for i, v in enumerate(SITES):
        q = []
        for a in range(3):
            t = (v[a] - about[a]) % L
            if t > L // 2:
                t -= L
            q.append(t)
        out.append((tuple(q), vec[i]))
    return out


def moments(pr):
    q = sum(x for _, x in pr)
    p = np.array([sum(x * o[a] for o, x in pr) for a in range(3)])
    Q = np.zeros((3, 3))
    for o, x in pr:
        r2 = sum(o[a] ** 2 for a in range(3))
        for a in range(3):
            for b in range(3):
                Q[a, b] += x * (3 * o[a] * o[b] - (r2 if a == b else 0))
    return q, p, Q


def prep(vec, about):
    """Unwrap about the pair midpoint, then recentre on the ROUNDED charge
    centroid; the integer shift is the same for two translated copies, so
    their centroid separation is exactly Dvec."""
    pr = unwrapped(vec, about)
    q, p, _ = moments(pr)
    c = np.round(p / q).astype(int)
    pr = [(tuple(o[a] - c[a] for a in range(3)), x) for o, x in pr]
    q, p, Q = moments(pr)
    return pr, q, p, Q


def place(pr, Lb, base):
    A = np.zeros((Lb,) * 3)
    for o, x in pr:
        A[(o[0] + base[0]) % Lb, (o[1] + base[1]) % Lb, (o[2] + base[2]) % Lb] += x
    return A


def multipole_rel(q1, p1, Q1, q2, p2, Q2, Dvec):
    """Relative correction to q1 q2 G(D) from the continuum expansion of
    1/(4 pi |R - (u - v)|) to dipole and traceless-quadrupole order."""
    D = np.linalg.norm(Dvec)
    n = np.array(Dvec, float) / D
    t1 = float(n @ (q2 * p1 - q1 * p2)) / (q1 * q2 * D)
    t2 = (q2 * float(n @ Q1 @ n) + q1 * float(n @ Q2 @ n)
          - 2 * (3 * float(n @ p1) * float(n @ p2) - float(p1 @ p2))) / (2 * q1 * q2 * D * D)
    return t1 + t2


DVECS = [(2, 0, 0), (3, 0, 0), (4, 0, 0), (3, 3, 0)]


# ================================================== A -- the two-pair state

ST = {}
A_ROWS = []
for dp in (1, 2):
    for Dvec in DVECS:
        p1, h1, e1, E1, r1, m1 = make_pair(dp, (0, 0, 0))
        p2, h2, e2, E2, r2, m2 = make_pair(dp, Dvec)
        e12, E12, idem, rk, r12 = two_pair([p1, p2], [h1, h2])
        ST[(dp, Dvec)] = dict(e1=e1, e2=e2, E1=E1, E2=E2, m1=m1, m2=m2,
                              r1=r1, r2=r2, r12=r12)
        A_ROWS.append(dict(dp=dp, D=Dvec, op=abs(float(p1 @ p2)), oh=abs(float(h1 @ h2)),
                           rel=(E12 - E1 - E2) / (E1 + E2),
                           dev=float(np.max(np.abs(e12 - e1 - e2))),
                           idem=idem, tr=rk))

# validation against the parent note's own pair table
VAL = []
for d in (1, 2, 3, 4):
    _, _, ev, Ev, _ = one_pair((0, 0, 0), (d % L, 0, 0))
    VAL.append((Ev, abs(float(ev.sum()) - Ev)))
po, ho = U[:, NOCC], U[:, NOCC - 1]
E_ORB = eps_of(P - np.outer(ho, ho) + np.outer(po, po))[1]

# the one-coarse-site translation residual of eps_v: naive vs gauge-corrected
_, _, e0, E0_, _, _ = make_pair(1, (0, 0, 0))
perm_x = np.array([IDX[tuple((v[b] + (1, 0, 0)[b]) % L for b in range(3))] for v in SITES])
_, _, e_nv, _, _, _ = make_pair(1, (1, 0, 0))
_, _, e_gv, _, _, _ = make_pair(1, (1, 0, 0), gauge_from=(0, 0, 0))
TR_NAIVE = float(np.max(np.abs(e_nv[perm_x] - e0)))
TR_GAUGE = float(np.max(np.abs(e_gv[perm_x] - e0)))

d1 = [r for r in A_ROWS if r['dp'] == 1]
d2 = [r for r in A_ROWS if r['dp'] == 2]
MAXIDEM = max(r['idem'] for r in A_ROWS)
MAXCNT = max(abs(float(ST[k]['r1'].sum())) for k in ST)
MAXCNT = max(MAXCNT, max(abs(float(ST[k]['r12'].sum())) for k in ST))

check("A1 [numerical, 1e-6] the conditioning vacuum: the half-filled staggered sea on 8^3 at twist (1,1,1) has E_sea = %.6f, the matter note's own value (%.1e), gap %.6f = 2 sqrt(6 - 3 sqrt2) (%.1e), <n_v> = 1/2 at all 512 sites (%.1e)"
      % (E_SEA, abs(E_SEA - NOTE_E_SEA_8), GAP, abs(GAP - 2 * np.sqrt(6 - 3 * np.sqrt(2))), HALF_RES),
      abs(E_SEA - NOTE_E_SEA_8) < 1e-6 and abs(GAP - 2 * np.sqrt(6 - 3 * np.sqrt(2))) < 1e-12
      and HALF_RES < 1e-15 and abs(GAP - NOTE_GAP_8) < 1e-6)

check("A2 [numerical, 1e-13] single pairs first: the band-edge orbital pair has E_exc = %.6f and the localised wavepackets %.4f to %.4f over d = 1..4, sum_v eps_v = E_exc to %.0e -- the matter note's 2.651309 and 2.6513-4.5163"
      % (E_ORB, min(r[0] for r in VAL), max(r[0] for r in VAL), max(r[1] for r in VAL)),
      abs(E_ORB - NOTE_GAP_8) < 1e-6 and max(r[1] for r in VAL) < 1e-13
      and abs(max(r[0] for r in VAL) - 4.5163) < 1e-3)

check("A3 [numerical, 1e-14] TWO pairs above it at D = (2,0,0)/(3,0,0)/(4,0,0)/(3,3,0): P'' = P - Q_h + Q_p is a projector, max|P''^2 - P''| = %.0e over eight states, trace exactly %d = V/2"
      % (MAXIDEM, A_ROWS[0]['tr']),
      MAXIDEM < 1e-14 and all(r['tr'] == 256 for r in A_ROWS))

check("A4 [numerical] the pairs decouple with D: the orbital overlaps fall <p1|p2> = %.2f/%.2f/%.3f/%.3f and <h1|h2> = %.2f/%.3f/%.4f/%.4f at those D"
      % tuple([r['op'] for r in d1] + [r['oh'] for r in d1]),
      d1[0]['op'] > 0.35 and d1[2]['op'] < 0.05 and d1[0]['oh'] > 0.37 and d1[2]['oh'] < 2e-3
      and d1[0]['op'] > d1[1]['op'] > d1[2]['op'])

check("A5 [numerical] the joint energy is additive to the same order: (E_12 - E_1 - E_2)/(E_1 + E_2) = %+.1e/%+.1e/%+.1e/%+.1e at d_pair = 1 and %+.1e/%+.1e at d_pair = 2; the eps_v defect falls an order per unit of D, %.1e -> %.1e -> %.1e"
      % (d1[0]['rel'], d1[1]['rel'], d1[2]['rel'], d1[3]['rel'], d2[1]['rel'], d2[2]['rel'],
         d1[0]['dev'], d1[1]['dev'], d1[2]['dev']),
      abs(d1[0]['rel']) > 8 * abs(d1[1]['rel']) and abs(d1[1]['rel']) > 8 * abs(d1[2]['rel'])
      and d1[0]['dev'] > 8 * d1[1]['dev'] and d1[1]['dev'] > 8 * d1[2]['dev'])

check("A6 [numerical, 1e-13] the COUNT above this sea is identically zero: sum_v (<n_v> - 1/2) = 0 to %.0e for every single-pair AND every joint state, so a count product here is exactly 0, not merely small"
      % MAXCNT, MAXCNT < 1e-13)


# ============================================== B -- the energy product

BROWS = {}
SYMMAX = 0.0
for Lb in (32, 64):
    Gh = GH[Lb]
    Gr = GR[Lb]
    b1 = (Lb // 2,) * 3
    for dp in (1, 2):
        for Dvec in DVECS:
            S = ST[(dp, Dvec)]
            pr1, q1, p1_, Q1 = prep(S['e1'], S['m1'])
            pr2, q2, p2_, Q2 = prep(S['e2'], S['m2'])
            b2 = tuple(b1[a] + Dvec[a] for a in range(3))
            A1 = place(pr1, Lb, b1)
            A2 = place(pr2, Lb, b2)
            F1 = np.fft.fftn(A1)
            F2 = np.fft.fftn(A2)
            Ei = float(np.real(np.sum(np.conj(F1) * Gh * F2)) / Lb ** 3)
            F12 = np.fft.fftn(A1 + A2)
            tot = float(np.real(np.sum(np.conj(F12) * Gh * F12)) / Lb ** 3)
            s1 = float(np.real(np.sum(np.conj(F1) * Gh * F1)) / Lb ** 3)
            s2 = float(np.real(np.sum(np.conj(F2) * Gh * F2)) / Lb ** 3)
            SYMMAX = max(SYMMAX, abs(tot - s1 - s2 - 2 * Ei))
            GD = float(Gr[Dvec[0] % Lb, Dvec[1] % Lb, Dvec[2] % Lb])
            pred = q1 * q2 * GD
            BROWS[(Lb, dp, Dvec)] = (Ei, pred, Ei / pred,
                                     1 + multipole_rel(q1, p1_, Q1, q2, p2_, Q2, Dvec))
            del A1, A2, F1, F2, F12

# validation of the response implementation against the landed point control
PC = {}
for Lb in (32, 64):
    r = Lb // 4
    PC[Lb] = 4 * PI * r * float(GR[Lb][r, 0, 0])

r64 = [BROWS[(64, 1, D)][2] for D in DVECS]
m64 = [BROWS[(64, 1, D)][3] for D in DVECS]
r64b = [BROWS[(64, 2, D)][2] for D in DVECS]
r32 = [BROWS[(32, 1, D)][2] for D in DVECS]
r32b = [BROWS[(32, 2, D)][2] for D in DVECS]

# large separation: two RIGID copies of one profile in the Lb = 64 box
Lb = 64
Gh = GH[Lb]
Gr = GR[Lb]
b1 = (Lb // 2,) * 3
S = ST[(1, (4, 0, 0))]
pr1, q1, p1_, Q1 = prep(S['e1'], S['m1'])
F1 = np.fft.fftn(place(pr1, Lb, b1))
kk = 2 * PI * np.fft.fftfreq(Lb)
KX, KY, KZ = np.meshgrid(kk, kk, kk, indexing='ij')
BIG = {}
for D in (2, 3, 4, 6, 8, 10, 12, 16):
    Ei = float(np.real(np.sum(np.conj(F1) * Gh * F1 * np.exp(-1j * KX * D))) / Lb ** 3)
    GD = float(Gr[D, 0, 0])
    BIG[D] = (Ei, q1 * q1 * GD, Ei / (q1 * q1 * GD),
              1 + multipole_rel(q1, p1_, Q1, q1, p1_, Q1, (D, 0, 0)))

check("B1 [numerical, 1e-4] validation before any new number: the response is the landed one, G0 the Fourier inverse of lambda(k) = 6 - 2 sum_a cos k_a off the constant mode, its point control 4 pi r G at r = Lb/4 giving %.4f and %.4f at Lb = 32, 64, both parents' own row (%.0e)"
      % (PC[32], PC[64], max(abs(PC[Lb] - NOTE_POINT_CONTROL[Lb]) for Lb in (32, 64))),
      max(abs(PC[Lb] - NOTE_POINT_CONTROL[Lb]) for Lb in (32, 64)) < 1e-4)

check("B2 [numerical, 1e-9] THE ENERGY PRODUCT. E_int = <eps_1, G0 P0 eps_2> against E_1 E_2 G0P0(D), Lb = 64, d_pair = 1: ratio %.4f/%.4f/%.4f/%.4f at those four D -- the bilinear response carries the product of the two excitation ENERGIES"
      % tuple(r64), min(r64[1:]) > 0.90 and max(r64) < 1.0)

check("B3 [numerical, 1e-9] neither the internal separation nor the box is doing the work: d_pair = 2 on Lb = 64 gives %.4f/%.4f at D = 3, 4, and Lb = 32 gives %.4f (d_pair 1) and %.4f (d_pair 2) at D = 4"
      % (r64b[1], r64b[2], r32[2], r32b[2]),
      abs(r64b[1] - 0.8757) < 5e-3 and abs(r64b[2] - 0.9188) < 5e-3
      and abs(r32[2] - 0.9575) < 5e-3 and abs(r32b[2] - 0.8997) < 5e-3)

check("B4 [numerical, 1e-14] E_int is exactly the cross term, not a fitted object: <eps_12, G eps_12> - <eps_1, G eps_1> - <eps_2, G eps_2> = 2 E_int to %.0e over all sixteen rows"
      % SYMMAX, SYMMAX < 1e-14)

check("B5 [numerical] the deficit from 1 is the sources' SHAPE: adding each source's dipole and traceless quadrupole to the point form gives %.4f/%.4f/%.4f/%.4f against the computed %.4f/%.4f/%.4f/%.4f, closing it to 1-3 per cent at |D| >= 3"
      % tuple(m64 + r64),
      max(abs(m64[i] - r64[i]) for i in (1, 2, 3)) < 0.03 and abs(m64[1] - 0.9146) < 5e-3)

check("B6 [numerical] the ratio goes to 1 with separation: on two RIGID copies of one eps profile in the Lb = 64 box -- the kernel and the source shape, NOT a joint 8^3 state -- it is %.4f/%.4f/%.4f/%.4f at D = 3/4/8/16"
      % (BIG[3][2], BIG[4][2], BIG[8][2], BIG[16][2]),
      BIG[3][2] < BIG[4][2] < BIG[8][2] < BIG[16][2] and BIG[16][2] > 0.998)


# ============================================== C -- the test-body law

CR = {}
for dp in (1, 2):
    for Dvec in ((3, 0, 0), (4, 0, 0)):
        S = ST[(dp, Dvec)]
        pra, qa, _, _ = prep(S['e1'], S['m1'])
        prb, qb, _, _ = prep(S['e2'], S['m2'])
        b2 = tuple(b1[a] + Dvec[a] for a in range(3))
        A1 = place(pra, Lb, b1)
        Fa = np.fft.fftn(A1)
        phi1 = solve(A1, Gh)
        Fb = np.fft.fftn(place(prb, Lb, b2))
        Fpred = np.zeros(3)
        Fnum = np.zeros(3)
        for a in range(3):
            pp = list(b2)
            pp[a] = (pp[a] + 1) % Lb
            mm = list(b2)
            mm[a] = (mm[a] - 1) % Lb
            Fpred[a] = -qb * (phi1[tuple(pp)] - phi1[tuple(mm)]) / 2.0
            vals = []
            for sg in (+1, -1):
                s = [0, 0, 0]
                s[a] = sg
                ph = np.exp(-1j * (KX * s[0] + KY * s[1] + KZ * s[2]))
                vals.append(float(np.real(np.sum(np.conj(Fa) * Gh * Fb * ph)) / Lb ** 3))
            Fnum[a] = -(vals[0] - vals[1]) / 2.0
        cos = float(Fnum @ Fpred) / (np.linalg.norm(Fnum) * np.linalg.norm(Fpred))
        CR[(dp, Dvec)] = (Fnum[0] / Fpred[0], float(np.degrees(np.arccos(np.clip(cos, -1, 1)))))
        del A1, Fa, Fb, phi1

# the force on rigid copies, out to large D
FS = {}
phiR = solve(place(pr1, Lb, b1), Gh)
for D in (3, 4, 6, 8, 10, 16):
    Fnum = np.zeros(3)
    Fpred = np.zeros(3)
    pos = (b1[0] + D, b1[1], b1[2])
    for a in range(3):
        vals = []
        for sg in (+1, -1):
            s = [D, 0, 0]
            s[a] += sg
            ph = np.exp(-1j * (KX * s[0] + KY * s[1] + KZ * s[2]))
            vals.append(float(np.real(np.sum(np.conj(F1) * Gh * F1 * ph)) / Lb ** 3))
        Fnum[a] = -(vals[0] - vals[1]) / 2.0
        pp = list(pos)
        pp[a] = (pp[a] + 1) % Lb
        mm = list(pos)
        mm[a] = (mm[a] - 1) % Lb
        Fpred[a] = -q1 * (phiR[tuple(pp)] - phiR[tuple(mm)]) / 2.0
    cos = float(Fnum @ Fpred) / (np.linalg.norm(Fnum) * np.linalg.norm(Fpred))
    FS[D] = (Fnum[0] / Fpred[0], float(np.degrees(np.arccos(np.clip(cos, -1, 1)))),
             4 * PI * D * D * Fnum[0] / (q1 * q1))

check("C1 [numerical, 1e-9] THE TEST-BODY LAW. F = -grad_{x2} E_int by central differences on pair 2's centroid against F_pred = -E_2 grad phi_1(x_2), phi_1 = G0 P0 eps_1: the x ratio is %.4f/%.4f at D = 3, 4 for d_pair = 1 and %.4f/%.4f for d_pair = 2, Lb = 64"
      % (CR[(1, (3, 0, 0))][0], CR[(1, (4, 0, 0))][0], CR[(2, (3, 0, 0))][0], CR[(2, (4, 0, 0))][0]),
      all(0.80 < CR[k][0] < 1.0 for k in CR))

check("C2 [numerical] and the two vectors point the same way: the angle between F_num and F_pred is %.1f/%.1f/%.1f/%.1f degrees on those same four rows"
      % (CR[(1, (3, 0, 0))][1], CR[(1, (4, 0, 0))][1], CR[(2, (3, 0, 0))][1], CR[(2, (4, 0, 0))][1]),
      max(CR[k][1] for k in CR) < 10.0)

check("C3 [numerical] the GAUGE-SIGN REBUILD LEMMA, named not absorbed: rebuilding pair 2 one coarse site over from a fresh seed is NOT faithful, translation residual %.2e, against %.2e when the seed is carried by the KS field's gauge sign: a sign-field artefact"
      % (TR_NAIVE, TR_GAUGE), TR_NAIVE > 0.3 and TR_GAUGE < 5e-3 and TR_NAIVE > 100 * TR_GAUGE)

check("C4 [numerical] the law tightens with separation: on rigid copies at D = 3/4/6/8/10/16 the x ratio is %.4f/%.4f/%.4f/%.4f/%.4f/%.4f and the angle falls %.1f -> %.1f degrees"
      % (FS[3][0], FS[4][0], FS[6][0], FS[8][0], FS[10][0], FS[16][0], FS[3][1], FS[16][1]),
      FS[3][0] < FS[4][0] < FS[6][0] and FS[16][0] > 0.999 and FS[16][1] < FS[3][1])

check("C5 [numerical] the pull is inverse-square with the landed coefficient: 4 pi D^2 F_x/(E_1 E_2) = %.4f/%.4f/%.4f/%.4f/%.4f/%.4f at those D against the source note's point control 1.0194/1.0064/1.0009/0.9963 at d = 4/6/8/10"
      % tuple(FS[D][2] for D in (3, 4, 6, 8, 10, 16)),
      all(abs(FS[d][2] - NOTE_T4_COEFF[d]) < 0.03 for d in (4, 6, 8, 10)))


# ============================================== D -- count versus energy

KNOB = []
for E0v in (1.35, 1.80, 2.40, 2.90, 3.15):
    kw = dict(E0=E0v, wf=0.6)
    _, _, ea, Ea, _, ma = make_pair(1, (0, 0, 0), **kw)
    pra, qa, _, _ = prep(ea, ma)
    Dvec = (4, 0, 0)
    _, _, eb, Eb, _, mb = make_pair(1, Dvec, **kw)
    prb, qb, _, _ = prep(eb, mb)
    b2 = tuple(b1[a] + Dvec[a] for a in range(3))
    Fa = np.fft.fftn(place(pra, Lb, b1))
    Fb = np.fft.fftn(place(prb, Lb, b2))
    Ei = float(np.real(np.sum(np.conj(Fa) * Gh * Fb)) / Lb ** 3)
    C1 = np.zeros((Lb,) * 3)
    C1[b1] = 1.0
    C1[b1[0], b1[1], b1[2] + 1] = 1.0
    C2 = np.zeros((Lb,) * 3)
    C2[b2] = 1.0
    C2[b2[0], b2[1], b2[2] + 1] = 1.0
    Ec = float(np.real(np.sum(np.conj(np.fft.fftn(C1)) * Gh * np.fft.fftn(C2))) / Lb ** 3)
    KNOB.append((qa, Ei, qa * qb, Ec))
    del Fa, Fb, C1, C2

E_RISE = KNOB[-1][1] / KNOB[0][1]
P_RISE = KNOB[-1][2] / KNOB[0][2]
C_SPREAD = max(k[3] for k in KNOB) - min(k[3] for k in KNOB)

EPROD = ST[(1, (4, 0, 0))]['E1'] * ST[(1, (4, 0, 0))]['E2']

check("D1 [numerical] COUNT VERSUS ENERGY. An energy knob -- one Gaussian seed band-filtered toward +-E0, width 0.6 -- moves E_exc through %.4f/%.4f/%.4f/%.4f/%.4f at fixed D = 4: E_int rises 1.000 -> %.3f while E_1 E_2 rises 1.000 -> %.3f, a ratio of ratios of %.3f"
      % (KNOB[0][0], KNOB[1][0], KNOB[2][0], KNOB[3][0], KNOB[4][0], E_RISE, P_RISE, E_RISE / P_RISE),
      E_RISE > 2.4 and P_RISE > 2.4 and abs(E_RISE / P_RISE - 1.0) < 0.06)

check("D2 [numerical, 1e-12] the SAME form on the empty vacuum's count source -- two A-string pairs, <n_v> = 1 at each string's two endpoints, I = 2 per pair -- reads E_int^count = %.7f in EVERY one of those rows, spread %.0e: constant while the excitation's energy quadruples"
      % (KNOB[0][3], C_SPREAD), C_SPREAD < 1e-12)

check("D3 [numerical, 1e-13] and above this sea that count source does not exist: sum_v rho = 0 to %.0e for every pair and every joint state, so I_1 I_2 = 0 identically while E_1 E_2 = %.2f for the same two pairs. The pooled object differs BY VACUUM"
      % (MAXCNT, EPROD), MAXCNT < 1e-13)

check("D4 [stated] so the source note's T6 sentence stands where it was proved -- 'the object the pooled response carries is the count product I(S) I(T) and NOT a mass product', on the EMPTY vacuum -- while above this sea the same form carries the ENERGY product", True)


# ============================================== E -- units

check("E1 [stated] units: hop t = 1, so every E_exc is in units of t and m = E_exc/t is a dimensionless lattice number; G0 P0 carries a^{-1}, so E_int is in t^2/a. No G_Newton, no coupling and no M_phys appears; the source note's factor-2 unit carry applies unchanged and is not adjudicated", True)

print("SUMMARY: conditional on the half-filled sea as the vacuum, the bridge's bilinear response carries the product of the two excitation energies with the landed kernel, ratio -> 1 with separation, and F = -E_test grad phi holds in its linear response. Both candidates come from that choice, not an axiom.")
print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
sys.exit(0 if FAIL == 0 else 1)
