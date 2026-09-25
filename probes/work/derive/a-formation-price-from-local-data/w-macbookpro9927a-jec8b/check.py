#!/usr/bin/env python3
"""check.py for J:derive:a-formation-price-from-local-data:a2 (worker w-macbookpro9927a-jec8b, claude-opus-5-5).

Every finite claim of ATTEMPT.md is checked with exact rational arithmetic: a factor-once banded LU of (1 - A) on the
held cube, Green columns by substitution, Woodbury solves for small-support amplitudes, exact residuals, and sympy.

Families
  Q  quoted definitions pinned by commit and SHA-256 (block 116 on its branch, block 57 on main, the task text)
  I  the ledger is the total effective source (Lambda = Q = sum K phi); the price E' = Q/phi'_y; the post-event field
     is k Q g(., y); block 116's cube prices, star price 1188/1091 and cross prices reproduced exactly
  R  records only: g at the centre strictly grows with the box (and the whole Green function does); pairs for R = 0, 1, 2
  C  amplitude sourcing: the Faraday cage (1 - A)[g(., y) 1_{outside B_(R+1)}] has total charge 1 and zero field in
     B_(R+1); adding c of it leaves every window datum unchanged and moves the price; exact residual; uniqueness certificate
  P  point-equivalent effective sources: the local rule E' = Q/(phi_y + k f_y) is exact in every held box; block 116's star
     is the case f = -6 s_1 delta_y; the quartic harmonic P = x^4 - 6x^2y^2 + y^4 - 2z^2 separates the cross from the star
  B  (b) under block 57's reduced law: the kept-ledger condition fixes the record's effective source; the step response
"""
import hashlib
import itertools
import json
import os
import subprocess
import sys
import time
from fractions import Fraction as F

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
N116 = ("0981f09c94f1ef15eb88112662338b946257c8b0",
        "docs/ADMISSIBILITY_RULE_FORMING_ONE_RECORD_KEEPS_THE_LEDGER_ONLY_AT_A_PRICE_ONE_PRICE_SERVES_EVERY_SITE_ONLY_WITH_THE"
        "_AMBIENT_AT_INFINITY_AND_A_SOURCE_IN_TWO_PLACES_SEPARATES_THE_READINGS_BOUNDED_THEOREM_NOTE_2026-09-24.md",
        "dadb61a47c2460ba7cede378864b19c07fead8fff8b0f227841e7dece6b3b159",
        ["A record at rest at `y`, with bare energy `E'`, has ledger `E'/(1 + kE' g_yy)`. It keeps `Λ` iff `E' = Λ/(1 − kΛ g_yy)`",
         "`g = (1 − A)⁻¹` inside, with zero wall values.",
         "*Records only*: only records enter, and an unrecorded amplitude sources nothing.",
         "The price of forming the record at `y` is `E' = c/(1 − kc)`, with `c = m₀/(1 + km₀) + 6m₁`."])
N57 = ("c3f8c47a58bfba48c1d9e030d6d79ecda00a294e",
       "docs/ADMISSIBILITY_RULE_A_DELAY_FOR_THE_RATE_FIELD_NEIGHBOUR_REFERRED_MOTION_DOES_NOT_PROPAGATE_A_REFERENCE_TO_DISTANT_"
       "CLOCKS_DOES_AT_A_SPEED_SET_BY_THE_LOCAL_RATE_BOUNDED_THEOREM_NOTE_2026-09-21.md",
       "9aa6121efd32e12be72601e75a259e4d5077fd4c8eadb319068bb55ef58e2acc",
       ["A fixed source switched on at zero gives (1-cos(omega_0 t))u_static.",
        "`Lambda[(kappa/wbar)ddotu+(wbar/gamma)u]=-P_0 s`."])
TASKQ = ("4b9441676514ccf4ce38d0b170828f761b1e9fb5", "J:derive:a-formation-price-from-local-data:a2",
         ["(a) show that no rule using only the amplitude and the pre-event rates within a fixed radius R of y gives E' in every held box",
          "(b) with block 57's delayed field law (landed), does the self-consistent condition E' phi'_y = Lambda, imposed as the field "
          "relaxes, reach the price without overshoot, and in what time?", "HIT: (a) settled exactly; (b) optional."])


def git_show(spec, branch=None):
    r = subprocess.run(["git", "show", spec], cwd=REPO, capture_output=True)
    if r.returncode != 0:
        subprocess.run(["git", "fetch", "--quiet", "origin", branch or spec.split(":")[0]], cwd=REPO, capture_output=True)
        r = subprocess.run(["git", "show", spec], cwd=REPO, capture_output=True)
    return r.stdout if r.returncode == 0 else None


def fam_Q():
    ok, msg = True, []
    for tag, (c, p, h, quotes), br in (("block116", N116, "physics-loop/admissibility-induced-law-block116-forming-one-record-keeps"
                                                             "-the-ledger-only-at-a-price-20260924"), ("block57", N57, None)):
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
    rep("Q", ok, "; ".join(msg) + " (block 116 is an open hand-off PR, read on its branch as the task directs)")


# ------------------------------------------------------------------ exact held-box machinery
class HeldBox:
    """Held cube of odd side n: the boundary layer is the wall; (1 - A) on the interior with zero wall values."""

    def __init__(self, n):
        self.n, self.m = n, n - 2
        self.sites = list(itertools.product(range(1, n - 1), repeat=3))
        self.idx = {s: i for i, s in enumerate(self.sites)}
        self.N = len(self.sites)
        self.nb = [[self.idx.get(tuple(s[i] + (sg if i == j else 0) for i in range(3))) for j in range(3) for sg in (1, -1)]
                   for s in self.sites]
        bw = self.m * self.m
        U = [{i: F(1), **{j: F(-1, 6) for j in self.nb[i] if j is not None}} for i in range(self.N)]
        L = [dict() for _ in range(self.N)]
        for i in range(self.N):
            piv = U[i][i]
            for r2 in range(i + 1, min(self.N, i + bw + 1)):
                f = U[r2].get(i)
                if not f:
                    continue
                q = f / piv
                L[r2][i] = q
                for c, v in U[i].items():
                    if c > i:
                        U[r2][c] = U[r2].get(c, F(0)) - q * v
                del U[r2][i]
        self.L, self.U, self._cols = L, U, {}

    def solve(self, rhs):
        b = [F(x) for x in rhs]
        for i in range(self.N):
            for c, q in self.L[i].items():
                b[i] -= q * b[c]
        x = [F(0)] * self.N
        for i in range(self.N - 1, -1, -1):
            s = b[i] - sum(v * x[c] for c, v in self.U[i].items() if c > i)
            x[i] = s / self.U[i][i]
        return x

    def col(self, i):
        if i not in self._cols:
            e = [F(0)] * self.N
            e[i] = F(1)
            self._cols[i] = self.solve(e)
        return self._cols[i]

    def lap(self, v):
        return [v[i] - sum(v[j] for j in self.nb[i] if j is not None) / 6 for i in range(self.N)]

    def centre(self):
        return ((self.n - 1) // 2,) * 3


BOXES = {}


def box(n):
    if n not in BOXES:
        BOXES[n] = HeldBox(n)
    return BOXES[n]


def small_solve(A, b):
    n = len(A)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for c in range(n):
        p = next(r for r in range(c, n) if M[r][c] != 0)
        M[c], M[p] = M[p], M[c]
        M[c] = [x / M[c][c] for x in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]
                M[r] = [x - f * y for x, y in zip(M[r], M[c])]
    return [M[i][n] for i in range(n)]


def static(B, masses, k):
    """Amplitude sourcing, bodies at rest (K = diag(m), e = m): ((1-A) + k diag m) psi = k m. Woodbury on the support."""
    S = sorted(masses)
    cols = {i: B.col(i) for i in S}
    A = [[(F(1) if a == b else F(0)) + k * cols[b][a] * masses[b] for b in S] for a in S]
    phiS = small_solve(A, [F(1)] * len(S))
    s = {j: masses[j] * p for j, p in zip(S, phiS)}
    psi = [k * sum(cols[j][x] * s[j] for j in S) for x in range(B.N)]
    return psi, s


def post_phi(B, Ep, iy, k):
    """Record at rest at y with bare energy Ep: phi'_y = 1/(1 + k Ep g_yy)."""
    g = B.col(iy)[iy]
    return 1 / (1 + k * Ep * g)


def residual_zero(B, masses, psi, k):
    L = B.lap(psi)
    return all(L[i] + k * masses.get(i, F(0)) * (psi[i] - 1) == 0 for i in range(B.N))


def cheb(a, b):
    return max(abs(a[i] - b[i]) for i in range(3))


# ------------------------------------------------------------------ I
def fam_I():
    ok, notes = True, []
    k = F(1, 12)
    B = box(7)
    cube = {B.idx[(x, y, z)]: F(1, 27) for x in (2, 3, 4) for y in (2, 3, 4) for z in (2, 3, 4)}
    psi, s = static(B, cube, k)
    ok &= residual_zero(B, cube, psi, k)
    phi = [1 - p for p in psi]
    Lam = sum(m * phi[i] for i, m in cube.items())
    Q = sum(s.values())
    ok &= Lam == Q
    prices = []
    for y in [(2, 2, 2), (2, 2, 3), (2, 3, 3), (3, 3, 3)]:
        iy = B.idx[y]
        gyy = B.col(iy)[iy]
        Ep = Lam / (1 - k * Lam * gyy)
        php = post_phi(B, Ep, iy, k)
        ok &= Ep * php == Lam and Ep == Q / php
        # post-event field is k Q g(., y)
        post_psi = [k * Ep * php * B.col(iy)[x] for x in range(B.N)]
        ok &= residual_zero(B, {iy: Ep}, post_psi, k)
        prices.append(Ep)
    ok &= prices == sorted(prices) and len(set(prices)) == 4
    want = [1.105484, 1.106710, 1.108108, 1.109712]
    ok &= all(abs(float(p) - w) < 1e-6 for p, w in zip(prices, want)) and abs(float(Lam) - 0.984627) < 1e-6
    for n in (7, 9):
        Bn = box(n)
        c = Bn.centre()
        iy = Bn.idx[c]
        star = [c] + [tuple(c[i] + (sg if i == j else 0) for i in range(3)) for j in range(3) for sg in (1, -1)]
        cross = [c] + [tuple(c[i] + (2 * sg if i == j else 0) for i in range(3)) for j in range(3) for sg in (1, -1)]
        for tag, pts in (("star", star), ("cross", cross)):
            ms = {Bn.idx[p]: F(1, 7) for p in pts}
            ps, ss = static(Bn, ms, k)
            Qn = sum(ss.values())
            Ep = Qn / (1 - k * Qn * Bn.col(iy)[iy])
            if tag == "star":
                ok &= Ep == F(1188, 1091)
            else:
                notes.append(f"cross n={n}: {float(Ep):.9f}")
                ok &= abs(float(Ep) - {7: 1.105773, 9: 1.105054}[n]) < 1e-6
    rep("I", ok, "held box of side 7, uniform 3^3 cube (E = 1, gamma = 1): Lambda = Q = sum K phi = 0.984627...; prices "
                 f"{', '.join(f'{float(p):.6f}' for p in prices)} at corner, edge, face, centre (block 116 T2); each satisfies E' "
                 "phi'_y = Lambda and its post-event field k Lambda g(., y) solves the law exactly; uniform star 1188/1091 in the "
                 "boxes of side 7 and 9; " + ", ".join(notes) + " (block 116 T3(d))")


# ------------------------------------------------------------------ R
def fam_R():
    ok = True
    k = F(1, 12)
    gc = {}
    for n in (3, 5, 7, 9):
        B = box(n)
        c = B.centre()
        gc[n] = B.col(B.idx[c])[B.idx[c]]
    ok &= gc[3] == 1 and gc[5] == F(22, 17) and gc[7] == F(136, 99) and gc[3] < gc[5] < gc[7] < gc[9]
    # the whole Green function grows: g_(n+2)(x, y) - g_n(x, y) > 0 at every interior x of the smaller box
    for n in (5, 7):
        Bs, Bl = box(n), box(n + 2)
        cs, cl = Bs.centre(), Bl.centre()
        gs, gl = Bs.col(Bs.idx[cs]), Bl.col(Bl.idx[cl])
        ok &= all(gl[Bl.idx[tuple(x + 1 for x in s)]] > gs[Bs.idx[s]] for s in Bs.sites)
    E = F(1)
    pr = {n: E / (1 - k * E * gc[n]) for n in gc}
    ok &= len(set(pr.values())) == 4
    rep("R", ok, f"records only (the amplitude sources nothing, phi = 1 before the event): g at the centre of the held cubes of "
                 f"side 3, 5, 7, 9 is 1, 22/17, 136/99, {gc[9]} and the whole g(., y) grows with the box (maximum principle); the "
                 f"same amplitude with E = 1 at the centre has window data identical in the pairs (3,5), (5,7), (7,9) (R = 0, 1, 2) "
                 f"and prices {', '.join(f'{float(pr[n]):.6f}' for n in (3, 5, 7, 9))}")


# ------------------------------------------------------------------ C
def fam_C():
    ok, out = True, []
    k = F(1, 12)
    for n, R, A, c in ((7, 0, {(3, 3, 3): F(1, 2)}, F(1, 5)), (9, 1, {(4, 4, 4): F(1, 2), (5, 4, 4): F(1, 3)}, F(1, 4)),
                       (9, 1, {(4, 4, 4): F(2, 3), (4, 3, 4): F(1, 6), (3, 4, 5): F(1, 5)}, F(-1, 7))):
        B = box(n)
        y = B.centre()
        iy = B.idx[y]
        masses = {B.idx[p]: v for p, v in A.items()}
        psi1, s1 = static(B, masses, k)
        phi1 = [1 - p for p in psi1]
        Lam1 = sum(s1.values())
        g = B.col(iy)
        v = [g[i] if cheb(B.sites[i], y) > R + 1 else F(0) for i in range(B.N)]
        cage = B.lap(v)
        ok &= sum(cage) == 1 and all(cheb(B.sites[i], y) in (R + 1, R + 2) for i in range(B.N) if cage[i] != 0)
        phi2 = [phi1[i] - k * c * v[i] for i in range(B.N)]
        m2 = dict(masses)
        for i in range(B.N):
            if cage[i] != 0:
                m2[i] = c * cage[i] / phi2[i]
        psi2 = [1 - p for p in phi2]
        ok &= residual_zero(B, m2, psi2, k)
        # uniqueness: lambda_min(1 - A) = 1 - cos(pi/(m+1)) >= 1 - cos(3/(m+1)) >= x^2/2 - x^4/24 at x = 3/(m+1)
        x = F(3, B.m + 1)
        lam_low = x * x / 2 - x ** 4 / 24
        ok &= lam_low + k * min(min(m2.values()), F(0)) > 0
        win = [i for i in range(B.N) if cheb(B.sites[i], y) <= R]
        ok &= all(phi1[i] == phi2[i] and masses.get(i, 0) == m2.get(i, 0) for i in win)
        Lam2 = sum(m2[i] * phi2[i] for i in m2)
        ok &= Lam2 - Lam1 == c
        gyy = g[iy]
        E1, E2 = Lam1 / (1 - k * Lam1 * gyy), Lam2 / (1 - k * Lam2 * gyy)
        ok &= E1 != E2
        out.append(f"side {n}, R = {R}, c = {c}: {sum(1 for q in cage if q)} cage sites, prices {float(E1):.6f} vs {float(E2):.6f}")
    rep("C", ok, "amplitude sourcing: the cage (1-A)[g(., y) 1_{outside B_(R+1)}] sits at Chebyshev radius R+1, R+2, has total "
                 "charge exactly 1 and field exactly g(., y) outside B_(R+1), zero inside; adding c of it (bodies at rest, signed "
                 "masses) solves the static law exactly (zero residual; positive definite, so unique), leaves the amplitude and "
                 "every rate within radius R unchanged, and shifts the ledger by exactly c: " + "; ".join(out))


# ------------------------------------------------------------------ P
def fam_P():
    ok, out = True, []
    k = F(1, 12)

    def lap_sparse(B, f):
        o = {}
        for i, v in f.items():
            o[i] = o.get(i, F(0)) + v
            for j in B.nb[i]:
                if j is not None:
                    o[j] = o.get(j, F(0)) - v / 6
        return o
    for n, y, Q, fsh in ((7, (3, 3, 3), F(9, 10), {(0, 0, 0): F(-1, 5), (1, 0, 0): F(1, 10), (0, -1, 0): F(1, 20)}),
                         (9, (4, 3, 5), F(9, 10), {(0, 0, 0): F(-1, 5), (1, 0, 0): F(1, 10), (0, -1, 0): F(1, 20)}),
                         (9, (4, 4, 4), F(3, 4), {(0, 0, 0): F(1, 3), (0, 1, 1): F(-1, 4), (-1, 0, 0): F(1, 6)})):
        B = box(n)
        iy = B.idx[y]
        f = {B.idx[tuple(y[i] + d[i] for i in range(3))]: v for d, v in fsh.items()}
        w = lap_sparse(B, f)
        s = dict(w)
        s[iy] = s.get(iy, F(0)) + Q
        s = {i: v for i, v in s.items() if v != 0}
        psi = B.solve([k * s.get(i, F(0)) for i in range(B.N)])
        phi = [1 - p for p in psi]
        masses = {i: v / phi[i] for i, v in s.items()}
        psi_chk, s_chk = static(B, masses, k)
        ok &= psi_chk == psi and sum(s_chk.values()) == Q
        Ep = Q / (1 - k * Q * B.col(iy)[iy])
        rule = Q / (phi[iy] + k * f[iy])
        ok &= rule == Ep and post_phi(B, Ep, iy, k) == phi[iy] + k * f[iy]
        # f is supported strictly inside the bounding box of supp(s - Q delta_y): computable from the window
        out.append(f"side {n} at {y}: {float(Ep):.9f}")
    m0, m1, kk, a, b = sp.symbols("m0 m1 k a b", positive=True)
    Qs = m0 * a + 6 * m1 * b
    c_ = m0 / (1 + kk * m0) + 6 * m1
    rule_star = (Qs / (a - 6 * kk * m1 * b)).subs(a, b / (1 + kk * m0))
    ok &= sp.simplify(rule_star - c_ / (1 - kk * c_)) == 0
    X, Y, Z = sp.symbols("X Y Z")
    P = X ** 4 - 6 * X ** 2 * Y ** 2 + Y ** 4 - 2 * Z ** 2
    lapP = sum(P.subs(v, v + 1) + P.subs(v, v - 1) - 2 * P for v in (X, Y, Z))
    ok &= sp.expand(lapP) == 0
    pairP = lambda pts, scale: sum(P.subs({X: scale * p[0], Y: scale * p[1], Z: scale * p[2]}) for p in pts)
    unit = [tuple(sg if i == j else 0 for i in range(3)) for j in range(3) for sg in (1, -1)]
    star_pair = pairP(unit, 1) - 6 * P.subs({X: 0, Y: 0, Z: 0})
    cross_pair = pairP(unit, 2) - 6 * P.subs({X: 0, Y: 0, Z: 0})
    ok &= star_pair == 0 and cross_pair == 48
    rep("P", ok, "if the effective source s = K phi is point-equivalent at y (s - Q delta_y = (1-A)f, f finitely supported; f is "
                 "then supported inside the bounding box of the source, so read from the window), the price in every held box is "
                 "E' = Q/(phi_y + k f_y) and the post-event clock is phi'_y = phi_y + k f_y exactly: " + "; ".join(out) + " (three "
                 "asymmetric sources); block 116's star is f = -6 s_1 delta_y and the rule reduces to c/(1 - kc) symbolically; the "
                 "discrete harmonic quartic x^4 - 6x^2y^2 + y^4 - 2z^2 pairs to 0 with the star's excess and to 48 per unit arm "
                 "source with the distance-two cross's, so the cross is not point-equivalent (its price moves with the box)")


# ------------------------------------------------------------------ B
def fam_B():
    t, w0, u = sp.symbols("t omega0 u_st", positive=True)
    sol = (1 - sp.cos(w0 * t)) * u
    ok = sp.simplify(sp.diff(sol, t, 2) + w0 ** 2 * sol - w0 ** 2 * u) == 0 and sol.subs(t, 0) == 0 and sp.diff(sol, t).subs(t, 0) == 0
    ok &= sp.simplify(sol.subs(t, sp.pi / w0) - 2 * u) == 0 and sp.simplify(sol.subs(t, sp.pi / (2 * w0)) - u) == 0
    rep("B", ok, "(b), conditional: E' phi'_y = Lambda makes the record's effective source the constant Lambda delta_y from the "
                 "event on; under block 57 T2's reduced law each mode then follows u(t) = (1 - cos w0 t) u_static from rest: the "
                 "offset reaches the static value first at t = pi/(2 w0), overshoots to twice it at t = pi/w0 and never settles")


if __name__ == "__main__":
    for fam in (fam_Q, fam_I, fam_R, fam_C, fam_P, fam_B):
        fam()
    print(f"runtime {time.time() - T0:.0f}s; failed families: {sorted(set(FAILS)) or 'none'}")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT check families {sorted(set(FAILS))}")
        sys.exit(1)
    print("SUMMARY: PARTIAL settled exactly in the negative for general amplitudes under both readings: no rule using only the "
          "amplitude and the pre-event rates within radius R gives the price in every held box, for any R (records only: one "
          "amplitude in two boxes; amplitude sourcing: a charged cage just outside the window, field zero inside, shifts the "
          "ledger by c). Positive: when the effective source K phi is point-equivalent at y, E' = Q/(phi_y + k f_y) is exact in "
          "every held box (block 116's star is a case). Open: window-confined sources that are not point-equivalent.")
    print("HIT: (a) under either reading no local rule of any fixed radius R sets the formation price in every held box: records "
          "only, the pre-event rates are uniform and g_yy grows with the box; amplitude sourcing, adding c times the cage "
          "(1-A)[g(.,y) 1_{outside B_(R+1)}] (total charge 1, zero field in B_(R+1)) leaves every datum within radius R unchanged "
          "and shifts Lambda by c; and whenever the effective source is point-equivalent (s - Q delta_y = (1-A)f, f finite), "
          "the local rule E' = Q/(phi_y + k f_y) holds in every held box, which is why block 116's star price ignores the walls.")
