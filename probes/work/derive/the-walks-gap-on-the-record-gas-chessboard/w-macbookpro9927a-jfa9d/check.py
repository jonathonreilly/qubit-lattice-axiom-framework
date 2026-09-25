#!/usr/bin/env python3
"""check.py for J:derive:the-walks-gap-on-the-record-gas-chessboard:a2 (worker w-macbookpro9927a-jfa9d, claude-opus-5-5).

The walk K = H0 + m eps S (offset c/2 removed, m = c/2): H0 = sum_j sigma_j D_j, D_j = (i/2)(T_j - T_j^dag) (block 54),
eps_x = (-1)^(x+y+z), S_x = +1 in step with the A-chessboard and -1 out of step (n_x = (1 + eps_x S_x)/2).
Clocking choice: c n added to the unclocked walk (block 79 T1's 'c n AFTER clocking only the kinetic operator', which
for the chessboard clock phi = r^eps gives phi H phi + c n = H + c n). Exact arithmetic throughout except family N.

Families
  Q  pinned sources (blocks 79, 81 on main; block 117 on its branch; the task)
  S  the square identity K^2 = H0^2 + m^2 + m eps [S, H0] for an arbitrary pattern S (exact on the 4^3 torus)
  P  a single out-of-step site: the site block of (K0 - E)^-1 is (E + m eps_x0) F(E) I (exact on the 4^3 torus by plugging
     in the Fourier candidate); the secular function 2m(m + eps E)F(E) is increasing on the gap; the substitution q = 2k
     gives int dk/(2pi)^3 / sum sin^2 k = 2 W3 exactly on the 8^3 grid versus the 4^3 grid of (3 - sum cos)
  W  a planar wall: the exact decaying eigenvector at E = -(sqrt(1+c^2) - 1)/2 (c = 3/4, 4/3, 12/5); the transverse terms
     anticommute with the rest, so the wall band is E^2 = E_b^2 + sin^2 kx + sin^2 ky; exact inertia counts on 4x4xLz slabs
  G  the gas at zeta = g^-3 is the ferromagnetic Ising model g^(#unlike/2) in S (so FKG); a flip with in-step neighbours
     has conditional probability g^3/(1+g^3); FKG lower bounds for isolated flips and for large out-of-step domains
  N  [float] Watson's closed form for W3 and c* = 1/sqrt(2 W3); the secular crossing; the level reaching the offset
"""
import hashlib
import json
import os
import random
import subprocess
import sys
import time
from fractions import Fraction as F
from math import comb

import numpy as np
import sympy as sp

T0 = time.time()
REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), *([os.pardir] * 5)))
FAILS = []


def rep(fam, ok, msg):
    if not ok:
        FAILS.append(fam)
    print(f"[{fam}] {'PASS' if ok else 'FAIL'} {msg}")
    sys.stdout.flush()


# ------------------------------------------------------------------ Q
SRC = [("block79", "7445cc7a50e2c7631d70dc8d9a065d0653ffa6ef",
        "docs/ADMISSIBILITY_RULE_A_CHESSBOARD_RECORD_BACKGROUND_IS_FELT_ONLY_AS_A_REST_MASS_AND_A_WALL_BETWEEN_OUT_OF_STEP_DOMAINS"
        "_BINDS_EXACT_ZERO_MODES_WHEN_ODD_BOUNDED_THEOREM_NOTE_2026-09-22.md",
        "a2631066f02143815c8dab971ebabf3d48c0250e52223fe5a216b7b4876df999",
        ["The algebraic identity `c n=(c/2)I+(c/2)eps` gives an offset and a staggered term. For the uniform free walk without "
         "scalar hopping the latter has gap |c|/2 relative to the offset, by the odd-displacement square identity.",
         "Adding c n AFTER clocking only the kinetic operator defines a different supplied model, phi H phi+c n=H+c n.",
         "Exact nullities of these 48-by-48 matrices are respectively 0,4,0,4."], None),
       ("block81", "fbe9f0f0154402d8afa07a8d12c920df2d9d0848",
        "docs/ADMISSIBILITY_RULE_THE_RECORD_GAS_NEVER_MAKES_THE_CHESSBOARD_A_REST_MASS_NEEDS_BINDING_GROWS_ONLY_AROUND_LOOPS_CONTENT"
        "_ORDER_GIVES_THE_WALK_NO_GAP_BOUNDED_THEOREM_NOTE_2026-09-22.md",
        "b5a271afed1eb32e16a3fcb714de896cb690bc490cd1d4ed632cf8298e6b6bbe",
        ["At bond scale g and site activity z the unnormalized weight is z^|V| 6^|V| g^|E| Q(G)."], None),
       ("block117", "24cc9059fba92e8bfbeec3f61f8d056241784ec4",
        "docs/ADMISSIBILITY_RULE_THE_RECORD_GAS_DOES_MAKE_THE_CHESSBOARD_WHEN_A_RECORDED_BOND_COSTS_A_FACTOR_BELOW_NINE_OVER_62500"
        "_AND_THE_TWO_FRAMED_STATES_DIFFER_AT_EVERY_SITE_BOUNDED_THEOREM_NOTE_2026-09-24.md",
        "cc2727f554303be434b0ec91409b4ba4573ca508c717c0cddb25ffa4b6659a2f",
        ["- For `x ≤ 3/250`, every site of every framed box has `P(σ_x = −1) ≤ 0.0897`.",
         "- At `ζ = g⁻³` this holds for `g ≤ 9/62500` without contents and for `g ≤ 10⁻⁵` at `(3,1,2)`."],
        "physics-loop/admissibility-induced-law-block117-the-record-gas-does-make-the-chessboard-when-bonds-are-expensive-20260924")]
TASKQ = ("363799d6c61f3c79b9e6261370e943f2711b2ad1", "J:derive:the-walks-gap-on-the-record-gas-chessboard:a2",
         ["TASK: on the gas's typical arrangements, is the walk's spectrum still gapped around the offset?",
          "State which clocking choice you use.",
          "HIT: an explicit gap bound, or an explicit mechanism that closes it, with exact checks on finite boxes."])


def git_show(spec, branch=None):
    r = subprocess.run(["git", "show", spec], cwd=REPO, capture_output=True)
    if r.returncode != 0:
        subprocess.run(["git", "fetch", "--quiet", "origin", branch or spec.split(":")[0]], cwd=REPO, capture_output=True)
        r = subprocess.run(["git", "show", spec], cwd=REPO, capture_output=True)
    return r.stdout if r.returncode == 0 else None


def fam_Q():
    ok, msg = True, []
    for tag, c, p, h, quotes, br in SRC:
        b = git_show(f"{c}:{p}", br)
        if b is None:
            rep("Q", False, f"{tag} unreadable")
            return
        good = hashlib.sha256(b).hexdigest() == h
        n = sum(q in b.decode() for q in quotes)
        ok &= good and n == len(quotes)
        msg.append(f"{tag}@{c[:8]} {'sha ok' if good else 'SHA MISMATCH'} {n}/{len(quotes)}")
    b = git_show(f"{TASKQ[0]}:probes/TASKS.json")
    what = next((t["what"] for t in json.loads(b.decode()) if t["id"] == TASKQ[1]), "") if b else ""
    n = sum(q in what for q in TASKQ[2])
    ok &= n == len(TASKQ[2])
    msg.append(f"task@{TASKQ[0][:8]} {n}/{len(TASKQ[2])}")
    rep("Q", ok, "; ".join(msg))


# ------------------------------------------------------------------ torus machinery (Gaussian integers after scaling)
SIG = [np.array([[0, 1], [1, 0]], dtype=complex), np.array([[0, -1j], [1j, 0]], dtype=complex),
       np.array([[1, 0], [0, -1]], dtype=complex)]
L = 4
SITES = [(x, y, z) for x in range(L) for y in range(L) for z in range(L)]
SIDX = {s: i for i, s in enumerate(SITES)}
EPS = np.array([(-1) ** (sum(s)) for s in SITES])


def H0x2():
    """2 H0 on the 4^3 torus (Gaussian-integer entries): <x|D_j|x - e_j> = i/2, <x|D_j|x + e_j> = -i/2."""
    n = 2 * len(SITES)
    M = np.zeros((n, n), dtype=complex)
    for i, s in enumerate(SITES):
        for j in range(3):
            for sg, amp in ((-1, 1j), (1, -1j)):
                t = list(s)
                t[j] = (t[j] + sg) % L
                k = SIDX[tuple(t)]
                M[2 * i:2 * i + 2, 2 * k:2 * k + 2] += amp * SIG[j]
    return M


def fam_S():
    ok = True
    B0 = H0x2()
    rnd = random.Random(7)
    for trial in range(3):
        Sv = np.array([rnd.choice((1, -1)) for _ in SITES])
        p, q = (3, 8) if trial != 1 else (5, 3)
        diag = np.repeat(EPS * Sv, 2)
        A = q * B0 + 2 * p * np.diag(diag)            # A = 2 q K with m = p/q
        Sd = np.diag(np.repeat(Sv, 2))
        comm = Sd @ B0 - B0 @ Sd
        lhs = A @ A
        rhs = q * q * (B0 @ B0) + 4 * p * p * np.eye(len(diag)) + 2 * p * q * np.diag(np.repeat(EPS, 2)) @ comm
        ok &= np.array_equal(lhs, rhs)
    # commutator lives on unlike bonds only; the chessboard (S = 1) gives K^2 = H0^2 + m^2
    ok &= np.array_equal(np.diag(np.repeat(EPS, 2)) @ B0 + B0 @ np.diag(np.repeat(EPS, 2)), 0 * B0)
    rep("S", ok, "exact on the 4^3 torus for three arbitrary patterns S: K^2 = H0^2 + m^2 + m eps [S, H0], with [S, H0]_xy = "
                 "(S_x - S_y) H0_xy nonzero only on bonds joining in-step and out-of-step sites; eps anticommutes with H0. So "
                 "every state inside the gap |E| < |c|/2 lives on the walls of the out-of-step pattern")


# ------------------------------------------------------------------ P: one out-of-step site
def fam_P():
    ok = True
    B0 = H0x2()
    # Fourier data on the 4^3 torus: k in (pi/2) Z^3, sin^2 in {0, 1}, e^{ik.x} in {1, i, -1, -i}
    ks = [(a, b, c) for a in range(4) for b in range(4) for c in range(4)]
    s_of = lambda kk: sum(1 for t in kk if t % 2 == 1)
    for (mp_, mq), (Ep, Eq) in (((3, 8), (1, 10)), ((1, 2), (-1, 5)), ((5, 4), (1, 3))):
        m, E = F(mp_, mq), F(Ep, Eq)
        FL = sum(F(1) / (s_of(kk) + m * m - E * E) for kk in ks) / 64
        FL8 = F(1, 8) * sum(comb(3, j) * (F(1) / (j + m * m - E * E)) for j in range(4))
        ok &= FL == FL8
        x0 = SIDX[(1, 2, 3)]
        # u = (H0^2 + m^2 - E^2)^-1 delta_x0 (scalar in the coin), by Fourier, as Gaussian rationals (re, im)
        u = []
        for s in SITES:
            re = im = F(0)
            for kk in ks:
                ph = sum(kk[j] * (s[j] - SITES[x0][j]) for j in range(3)) % 4
                val = F(1, 64) / (s_of(kk) + m * m - E * E)
                if ph == 0:
                    re += val
                elif ph == 1:
                    im += val
                elif ph == 2:
                    re -= val
                else:
                    im -= val
            u.append((re, im))
        for a in range(2):
            # v = (K0 + E) u e_a ; check (K0 - E) v = e_{x0, a} exactly and v_{x0} = (E + m eps_x0) F e_a
            n = 2 * len(SITES)
            ur = [F(0)] * n
            ui = [F(0)] * n
            for i in range(len(SITES)):
                ur[2 * i + a], ui[2 * i + a] = u[i]

            def apply(sign, xr, xi):     # (K0 + sign E) x with K0 = H0 + m eps, 2 H0 = B0 Gaussian integer
                yr, yi = [F(0)] * n, [F(0)] * n
                for r in range(n):
                    accr = acci = F(0)
                    for c in np.nonzero(B0[r])[0]:
                        br, bi = int(B0[r, c].real), int(B0[r, c].imag)
                        accr += br * xr[c] - bi * xi[c]
                        acci += br * xi[c] + bi * xr[c]
                    d = m * int(EPS[r // 2]) + sign * E
                    yr[r] = accr / 2 + d * xr[r]
                    yi[r] = acci / 2 + d * xi[r]
                return yr, yi
            vr, vi = apply(+1, ur, ui)
            wr, wi = apply(-1, vr, vi)
            target = [F(1) if r == 2 * x0 + a else F(0) for r in range(n)]
            ok &= wr == target and all(t == 0 for t in wi)
            ok &= vr[2 * x0 + a] == (E + m * int(EPS[x0])) * FL and vi[2 * x0 + a] == 0 and vr[2 * x0 + 1 - a] == 0
    # monotonicity of f(e) = 2m(m+e)F(e) on (-m, m): F2 <= F/(m^2 - e^2) gives f' > 0 (symbolic inequality core)
    e, m_ = sp.symbols("e m", positive=True)
    core = sp.simplify(2 * e * (m_ + e) / ((m_ - e) * (m_ + e)) - 2 * e / (m_ - e))
    ok &= core == 0
    # substitution q = 2k: the 8^3 grid of 1/sum sin^2 (k away from its 8 zeros) equals twice the 4^3 grid of 1/(3 - sum cos q)
    g8 = [F(0), F(1, 2), F(1), F(1, 2), F(0), F(1, 2), F(1), F(1, 2)]
    lhs = sum(F(1) / (a + b + c + F(1, 10)) for a in g8 for b in g8 for c in g8) / 512
    c4 = [F(1), F(0), F(-1), F(0)]
    rhs = 2 * sum(F(1) / (3 - a - b - c + F(2, 10)) for a in c4 for b in c4 for c in c4) / 64
    ok &= lhs == rhs
    rep("P", ok, "a flipped site x0: V = -2m eps_x0 at x0 (rank 2, scalar in the coin); exact on the 4^3 torus at three (m, E): "
                 "(K0 - E)^-1 at x0 is (E + m eps_x0) F_L(E) I with F_L = (1/8) sum_j C(3,j)/(j + m^2 - E^2); hence a level in the "
                 "gap iff 2m(m + eps_x0 E) F(E) = 1, doubly degenerate; the left side is increasing on (-m, m), so on Z^3 a level "
                 "exists iff 4m^2 W' > 1, W' = int dk/(2pi)^3 / sum sin^2 k = 2 W3 (grid identity under q = 2k checked), i.e. "
                 "iff |c| > c* = 1/sqrt(2 W3)")


# ------------------------------------------------------------------ W: planar walls
def ldl_neg(X, Y, t):
    """Number of eigenvalues < t of the Hermitian X + iY (X, Y Fraction lists), from the realified LDL^T (each counted twice)."""
    n = len(X)
    M = [[(X[i][j] - (t if i == j else 0)) if (i < n and j < n) else None for j in range(2 * n)] for i in range(2 * n)]
    for i in range(2 * n):
        for j in range(2 * n):
            a, b = i % n, j % n
            xi, yi = (i >= n), (j >= n)
            val = X[a][b] - (t if a == b else 0)
            if not xi and not yi:
                M[i][j] = val
            elif not xi and yi:
                M[i][j] = -Y[a][b]
            elif xi and not yi:
                M[i][j] = Y[a][b]
            else:
                M[i][j] = val
    neg = 0
    N = 2 * n
    for c in range(N):
        piv = M[c][c]
        assert piv != 0
        if piv < 0:
            neg += 1
        rowc = M[c]
        for r in range(c + 1, N):
            f = M[r][c]
            if f != 0:
                q = f / piv
                rowr = M[r]
                for k in range(c + 1, N):
                    if rowc[k] != 0:
                        rowr[k] -= q * rowc[k]
    assert neg % 2 == 0
    return neg // 2


def slab_block(kx, ky, m, Lz, wall=True):
    """k_par block of the 4x4xLz torus: basis (z, p, a), p pairs k with k + (pi, pi); entries exact (sin in {0, +-1})."""
    sinv = {0: 0, 1: 1, 2: 0, 3: -1}
    n = 4 * Lz
    X = [[F(0)] * n for _ in range(n)]
    Y = [[F(0)] * n for _ in range(n)]
    idx = lambda z, p, a: ((z % Lz) * 2 + p) * 2 + a
    for z in range(Lz):
        S = 1 if (not wall or z < Lz // 2) else -1
        for p in range(2):
            sx, sy = sinv[(kx + 2 * p) % 4], sinv[(ky + 2 * p) % 4]
            on = sx * SIG[0] + sy * SIG[1]
            for a in range(2):
                for b in range(2):
                    X[idx(z, p, a)][idx(z, p, b)] += int(on[a, b].real)
                    Y[idx(z, p, a)][idx(z, p, b)] += int(on[a, b].imag)
                    # D_z: <z|D|z-1> = i/2, <z|D|z+1> = -i/2, coin sigma_3
                    Y[idx(z, p, a)][idx(z - 1, p, b)] += F(1, 2) * int(SIG[2][a, b].real)
                    Y[idx(z, p, a)][idx(z + 1, p, b)] -= F(1, 2) * int(SIG[2][a, b].real)
                X[idx(z, p, a)][idx(z, 1 - p, a)] += m * S * (-1) ** z
    return X, Y


def fam_W():
    ok = True
    out = []
    # exact decaying eigenvector of the sharp wall, pair sector tau = +1, even parity, gauge psi_z = i^z phi_z
    for c in (F(3, 4), F(4, 3), F(12, 5)):
        m = c / 2
        root = sp.sqrt(sp.Rational(1) + 4 * sp.Rational(m) ** 2)
        ok &= root.is_Rational
        r = 2 * sp.Rational(m) - root
        Eb = (root - 1) / 2
        E = (1 + r) / 2 - sp.Rational(m)
        ok &= sp.simplify(E + Eb) == 0 and abs(r) < 1
        mu = lambda z: sp.Rational(m) * (-1) ** (z % 2) * (1 if z >= 1 else -1)      # integer sign even for z < 0
        phi = lambda z: r ** ((z // 2) if z >= 1 else ((1 - z) // 2))
        for z in range(-6, 8):
            ok &= sp.simplify(sp.Rational(1, 2) * (phi(z - 1) + phi(z + 1)) + mu(z) * phi(z) - E * phi(z)) == 0
        out.append(f"c={c}: r={r}, E=-{Eb}")
    # transverse anticommutation in the pair space (tau acts on p): T = tau_z (x) (sx s1 + sy s2), Z = I (x) s3 * Dz, M = tau_x (x) I
    sx, sy, dz, mm = sp.symbols("sx sy dz mm")
    t_z = sp.Matrix([[1, 0], [0, -1]])
    t_x = sp.Matrix([[0, 1], [1, 0]])
    s1, s2, s3 = [sp.Matrix(M.tolist()).applyfunc(sp.nsimplify) for M in SIG]
    kron = lambda A, B: sp.kronecker_product(A, B)
    T = kron(t_z, sx * s1 + sy * s2)
    Zp = kron(sp.eye(2), dz * s3)
    Mp = kron(t_x, mm * sp.eye(2))
    ok &= sp.simplify(T * Zp + Zp * T) == sp.zeros(4) and sp.simplify(T * Mp + Mp * T) == sp.zeros(4)
    ok &= sp.simplify(T * T - (sx ** 2 + sy ** 2) * sp.eye(4)) == sp.zeros(4)
    # exact inertia on 4 x 4 x Lz slabs (two walls) and the wall-free control
    Lz = 16
    counts = []
    for c in (F(3, 4), F(4, 3)):
        m = c / 2
        Eb = {F(3, 4): F(1, 8), F(4, 3): F(1, 3)}[c]
        X, Y = slab_block(0, 0, m, Lz, True)
        cnt = {t: ldl_neg(X, Y, t) for t in (-Eb * F(11, 10), -Eb * F(9, 10), Eb * F(9, 10), Eb * F(11, 10))}
        n_in = cnt[Eb * F(9, 10)] - cnt[-Eb * F(9, 10)]
        n_near = (cnt[Eb * F(11, 10)] - cnt[Eb * F(9, 10)]) + (cnt[-Eb * F(9, 10)] - cnt[-Eb * F(11, 10)])
        Xc, Yc = slab_block(0, 0, m, Lz, False)
        n_ctrl = ldl_neg(Xc, Yc, m * F(99, 100)) - ldl_neg(Xc, Yc, -m * F(99, 100))
        X1, Y1 = slab_block(1, 0, m, Lz, True)
        n_far = ldl_neg(X1, Y1, m * F(99, 100)) - ldl_neg(X1, Y1, -m * F(99, 100))
        ok &= n_in == 0 and n_near > 0 and n_ctrl == 0 and n_far == 0
        counts.append(f"c={c}: |E| < 0.9E_b: {n_in}, 0.9E_b < |E| < 1.1E_b: {n_near}, no-wall |E| < 0.99m: {n_ctrl}, "
                      f"k=(pi/2,0) block |E| < 0.99m: {n_far}")
    rep("W", ok, "sharp planar wall: exact decaying eigenvector on the line (" + "; ".join(out) + "), so the wall binds levels at "
                 "E = -(sqrt(1+c^2) - 1)/2 and, in the other pair sector (phi_z -> (-1)^z phi_z reverses the sign), +(sqrt(1+c^2)-1)/2; "
                 "the transverse terms anticommute with the rest and square to sin^2 kx + sin^2 ky, so the wall band is "
                 "E^2 = E_b^2 + sin^2 kx + sin^2 ky inside the gap; exact inertia on 4x4x16 slabs with two walls: "
                 + "; ".join(counts))


# ------------------------------------------------------------------ G: the gas
def fam_G():
    ok = True
    g, z = sp.symbols("g zeta", positive=True)
    ex, sxs, sys_ = sp.symbols("e_x s_x s_y")
    # n = (1 + eps S)/2; a bond joins opposite eps. log weight = N log zeta + B log g
    nx = (1 + ex * sxs) / 2
    ny = (1 - ex * sys_) / 2
    bond = sp.expand(nx * ny)
    # per-site field from 6 bonds: (1/4)(eps S) * 6 = (3/2) eps S in B, (1/2) eps S in N  -> zero at zeta = g^-3
    field = sp.Rational(1, 2) * sp.log(z) + sp.Rational(3, 2) * sp.log(g)
    ok &= sp.simplify(field.subs(z, g ** -3)) == 0
    ok &= sp.expand(bond - (1 + ex * sxs - ex * sys_ - ex ** 2 * sxs * sys_) / 4) == 0
    # flip of a site with six like neighbours changes #unlike by 6 -> factor g^(6/2)
    ok &= sp.simplify(g ** sp.Rational(6, 2) / (1 + g ** 3) - g ** 3 / (1 + g ** 3)) == 0
    p_out = F(897, 10000)
    dens = {R: (1 - p_out) ** (sz - 1) for R, sz in ((1, 7), (2, 25), (3, 63))}
    ok &= all(v > 0 for v in dens.values())
    rep("G", ok, "at zeta = g^-3 the content-less gas is the ferromagnetic Ising model with weight g^(#unlike bonds/2) in S "
                 "(the staggered field (1/2)log zeta + (3/2)log g vanishes), so FKG holds for S; a flip whose six neighbours "
                 "are in step has conditional probability exactly g^3/(1+g^3); with block 117's P(S_x = -1) <= 0.0897 "
                 "(g <= 9/62500), a flip isolated within radius R has density >= g^3/(1+g^3) * " +
                 ", ".join(f"{float(v):.4f} (R={R})" for R, v in dens.items()) + "; a cube of side l all out of step has "
                 "probability >= (g^3/(1+g^3))^(l^3) > 0 (FKG, decreasing events)")


# ------------------------------------------------------------------ N: [float]
def fam_N():
    import mpmath as mp
    W3 = mp.sqrt(6) / (32 * mp.pi ** 3) * mp.gamma(mp.mpf(1) / 24) * mp.gamma(mp.mpf(5) / 24) * mp.gamma(mp.mpf(7) / 24) \
        * mp.gamma(mp.mpf(11) / 24) / 3
    cstar = 1 / mp.sqrt(2 * W3)
    n = 160
    k = (np.arange(n) + 0.5) * 2 * np.pi / n
    s1 = np.sin(k) ** 2
    s = s1[:, None, None] + s1[None, :, None] + s1[None, None, :]
    Fv = lambda e, m: np.mean(1.0 / (s + m * m - e * e))
    fe = {c: 2 * (c / 2) ** 2 * 2 * Fv(0.999999 * c / 2, c / 2) for c in (0.95, 1.05)}
    from scipy.optimize import brentq
    c0 = brentq(lambda c: 2 * (c / 2) ** 2 * Fv(0, c / 2) - 1, 1.2, 4)
    ok = fe[0.95] < 1 < fe[1.05] and abs(float(W3) - 0.5054620197) < 1e-9 and 2.2 < c0 < 2.45
    rep("N", ok, f"[float] Watson W3 = {mp.nstr(W3, 12)} (3 - sum cos normalization), c* = 1/sqrt(2 W3) = {mp.nstr(cstar, 10)}; the "
                 f"secular value at the upper edge, 4m^2 F(m), is {fe[0.95]:.3f} at c = 0.95 and {fe[1.05]:.3f} at c = 1.05; the "
                 f"flipped-site level reaches the offset (2m^2 F(0) = 1) at c0 = {c0:.4f}")
    return float(cstar), c0


if __name__ == "__main__":
    fam_Q()
    fam_S()
    fam_P()
    fam_W()
    fam_G()
    cstar, c0 = fam_N()
    print(f"runtime {time.time() - T0:.0f}s; failed families: {sorted(set(FAILS)) or 'none'}")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT check families {sorted(set(FAILS))}")
        sys.exit(1)
    print("SUMMARY: PARTIAL (b) explicit mechanisms: on the gas's typical arrangements the walk's gap |c|/2 around the offset does "
          "not persist. Walls of out-of-step domains carry a band E^2 = E_b^2 + sin^2 kx + sin^2 ky down to E_b = (sqrt(1+c^2)-1)/2 "
          "for every c, and isolated out-of-step sites (density >= of order g^3) bind doubly degenerate levels in the gap iff "
          f"|c| > c* = 1/sqrt(2 W3) = {cstar:.6f}, reaching the offset at c0 = {c0:.3f}. Clocking: c n added to the unclocked walk.")
    print("HIT: with c n added to the unclocked walk, K^2 = H0^2 + m^2 + m eps [S, H0], so in-gap states live only on walls; a planar "
          "wall between out-of-step domains carries the band E^2 = E_b^2 + sin^2 kx + sin^2 ky with E_b = (sqrt(1+c^2) - 1)/2 < |c|/2 "
          "for every c; an isolated out-of-step site binds a doubly degenerate level in the gap iff |c| > 1/sqrt(2 W3) = 0.994582 "
          "(W3 Watson's integral); at zeta = g^-3 the gas is a ferromagnetic Ising model in S, so both defect types have "
          "positive density on typical arrangements (isolated flips >= g^3(0.91)^(|B_R|-1)/(1+g^3)); exact checks on 4^3 tori and slabs.")
