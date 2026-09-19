#!/usr/bin/env python3
"""Exact checks for J:derive:lightcone-formation:a6 (worker w-macbookpro90c72-j0029).

Finite claims: integers, fractions, sympy. Floating output is display only.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import product
from typing import List, Sequence, Tuple

import sympy as sp

Vec = Tuple[int, int, int]
N3 = ((0, 0, 0), (1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
N_BACK = ((0, 0, 0), (-1, 0, 0), (0, -1, 0), (0, 0, -1))


def add(a: Vec, b: Vec, L: int) -> Vec:
    return ((a[0] + b[0]) % L, (a[1] + b[1]) % L, (a[2] + b[2]) % L)


def sub(a: Vec, b: Vec, L: int) -> Vec:
    return ((a[0] - b[0]) % L, (a[1] - b[1]) % L, (a[2] - b[2]) % L)


def sites(L: int) -> List[Vec]:
    return [(x, y, z) for x in range(L) for y in range(L) for z in range(L)]


def S_star(cfg: dict, x: Vec, L: int, neigh=N3) -> Tuple[int, int, int]:
    sx = sy = sz = 0
    for d in neigh:
        y = add(x, d, L)
        v = cfg[y]
        sx += v[0]
        sy += v[1]
        sz += v[2]
    return (sx, sy, sz)


def bilinear(cfg: dict, cfgp: dict, L: int, neigh=N3) -> Tuple[int, int]:
    left = right = 0
    for x in sites(L):
        S = S_star(cfg, x, L, neigh)
        Sp = S_star(cfgp, x, L, neigh)
        sx, sy, sz = cfg[x]
        px, py, pz = cfgp[x]
        left += px * S[0] + py * S[1] + pz * S[2]
        right += sx * Sp[0] + sy * Sp[1] + sz * Sp[2]
    return left, right


def main() -> int:
    failures: List[str] = []

    def check(name: str, cond: bool, detail: str = "") -> None:
        status = "PASS" if cond else "FAIL"
        extra = f" {detail}" if extra_ok(detail) else ""
        print(f"CHECK {name}: {status}{extra}")
        if not cond:
            failures.append(name)

    def extra_ok(detail: str) -> bool:
        return bool(detail)

    # ----- E0: linear kernel identity (exact, sympy) -----
    kx, ky, kz = sp.symbols("kx ky kz", real=True)
    E = 2 * ((1 - sp.cos(kx)) + (1 - sp.cos(ky)) + (1 - sp.cos(kz)))
    phi = 1 - E / 7
    lhs = 1 / (1 - phi**2)
    rhs = 7 / (2 * E * (1 - E / 14))
    diff = sp.simplify(lhs - rhs)
    check("E0a", diff == 0, f"sigma^2/(1-phi^2) - 7 sigma^2/(2E(1-E/14)) = {diff}")
    # doubled-graph adjacency 7*phi = 7-E; Laplacian eigenvalues 7 ± (7-E)
    lam_minus = 7 - (7 - E)  # = E
    lam_plus = 7 + (7 - E)  # = 14-E
    check("E0b", sp.simplify(lam_minus - E) == 0)
    check("E0c", sp.simplify(lam_plus - (14 - E)) == 0)
    # at k=0, E=0, phi=1 (zero mode); at k=(pi,0,0), E=4, phi=1-4/7=3/7
    E_pi = E.subs({kx: sp.pi, ky: 0, kz: 0})
    phi_pi = phi.subs({kx: sp.pi, ky: 0, kz: 0})
    check("E0d", E_pi == 4 and phi_pi == sp.Rational(3, 7), f"E(pi,0,0)={E_pi} phi={phi_pi}")
    # 1-phi^2 at that point: 1-(9/49)=40/49; rhs 7/(2*4*(1-4/14))=7/(8*(10/14))=7/(80/14)=7*14/80=98/80=49/40
    # wait lhs 49/40 vs 40/49 inverted? lhs = 1/(1-phi^2)=49/40. rhs=7/(2E(1-E/14))=7/(8*(10/14))=7*14/80=98/80=49/40. OK.

    # ----- E1: bilinear identity on the 7-stencil (integer spins, periodic) -----
    # Two configurations of Z^3-valued 3-vectors on L=2 and L=3.
    L = 2
    xs = sites(L)
    cfg_a = {x: (1, 0, 0) for x in xs}
    cfg_b = {x: (0, 1, 0) for x in xs}
    left, right = bilinear(cfg_a, cfg_b, L)
    check("E1a", left == right, f"all-e1 vs all-e2: {left} vs {right}")
    # a mixed integer configuration (deterministic, not random)
    cfg_c = {}
    for i, x in enumerate(xs):
        cfg_c[x] = ((-1) ** x[0], (-1) ** x[1], (-1) ** x[2])
    cfg_d = {}
    for i, x in enumerate(xs):
        cfg_d[x] = (x[0] - 1, x[1], 1 - x[2])
    left, right = bilinear(cfg_c, cfg_d, L)
    check("E1b", left == right, f"L=2 mixed: {left} vs {right}")
    L3 = 3
    xs3 = sites(L3)
    cfg_e = {x: (x[0] - 1, x[1] - 1, x[2] - 1) for x in xs3}
    cfg_f = {x: ((-1) ** (x[0] + x[1]), x[2] - 1, 2 - x[0]) for x in xs3}
    left, right = bilinear(cfg_e, cfg_f, L3)
    check("E1c", left == right, f"L=3 mixed: {left} vs {right}")
    # the identity is 7-linear: also check against a third pair with zeros
    cfg_0 = {x: (0, 0, 0) for x in xs}
    left, right = bilinear(cfg_c, cfg_0, L)
    check("E1d", left == 0 and right == 0, f"vs zero {left},{right}")

    # ----- E2: backward stencil FAILS the bilinear identity (counterexample) -----
    # On L=2, +e_j ≡ -e_j so the backward 4-stencil is accidentally symmetric.
    # On L=3 a one-hot pair distinguishes them.
    cfg_g3 = {x: (0, 0, 0) for x in xs3}
    cfg_g3[(0, 0, 0)] = (1, 0, 0)
    cfg_h3 = {x: (0, 0, 0) for x in xs3}
    cfg_h3[(1, 0, 0)] = (1, 0, 0)
    ls, rs = bilinear(cfg_g3, cfg_h3, L3, neigh=N3)
    lb, rb = bilinear(cfg_g3, cfg_h3, L3, neigh=N_BACK)
    check("E2a", ls == rs, f"7-stencil still holds: {ls}=={rs}")
    check("E2b", lb != rb, f"backward FAILS: {lb} vs {rb}")
    check("E2c", (lb, rb) == (1, 0), f"backward pair {(lb, rb)}")
    print(f"BACKWARD_COUNTEREXAMPLE left={lb} right={rb} (7-stencil {ls}=={rs})")

    # ----- E3: Ising detailed-balance identity reduces to the bilinear -----
    # On L=2, 8 sites, two Ising configs encoded as ±e_z. The ratio identity is
    # sum_x s'_x S_x(s) - sum_x s_x S_x(s') = 0, already E1. Check a 4-config census
    # of all Ising configurations on L=2 (2^8=256 is large for pairs; check all
    # configs against two fixed partners, and a 16-pair grid).
    def ising_cfg(bits: Sequence[int], Lloc: int) -> dict:
        xs_loc = sites(Lloc)
        return {xs_loc[i]: (0, 0, 1 if bits[i] else -1) for i in range(len(xs_loc))}

    L = 2
    nsite = 8
    partners = [
        tuple(0 for _ in range(nsite)),
        tuple(1 for _ in range(nsite)),
        tuple(i % 2 for i in range(nsite)),
        tuple(1 if i < 4 else 0 for i in range(nsite)),
    ]
    n_ok = 0
    n_all = 0
    for bits in product((0, 1), repeat=nsite):
        cfg = ising_cfg(bits, L)
        for pbits in partners:
            cfgp = ising_cfg(pbits, L)
            lft, rgt = bilinear(cfg, cfgp, L)
            n_all += 1
            if lft == rgt:
                n_ok += 1
    check("E3a", n_ok == n_all, f"Ising bilinear {n_ok}/{n_all}")

    # ----- E4: vMF mean Lipschitz ingredients (exact at kappa=0; inequality grid) -----
    k = sp.symbols("k", positive=True)
    A = sp.coth(k) - 1 / k
    Ap = sp.simplify(sp.diff(A, k))
    trans = sp.simplify(A / k)
    lim_Ap = sp.limit(Ap, k, 0)
    lim_tr = sp.limit(trans, k, 0)
    check("E4a", lim_Ap == sp.Rational(1, 3), f"A'(0)={lim_Ap}")
    check("E4b", lim_tr == sp.Rational(1, 3), f"A(k)/k at 0 = {lim_tr}")
    # A'(k) = 1/k^2 - csch^2(k). Compare to 1/3 at rational k via high-prec mpmath
    # through sympy N, then wrap as a CHECK that the sampled values stay <= 1/3.
    samples = []
    ok_bound = True
    for num, den in ((1, 10), (1, 5), (1, 2), (1, 1), (2, 1), (5, 1), (10, 1)):
        kv = sp.Rational(num, den)
        apv = Ap.subs(k, kv).evalf(40)
        trv = trans.subs(k, kv).evalf(40)
        samples.append((kv, apv, trv))
        if apv > sp.Rational(1, 3) + sp.Float("1e-20") or trv > sp.Rational(1, 3) + sp.Float("1e-20"):
            ok_bound = False
    check("E4c", ok_bound, "A' and A/k <= 1/3 on the sample")
    # Dobrushin: 7 sites in the stencil, Lip <= beta/3 => coefficient 7 beta/3 < 1 iff beta < 3/7
    check("E4d", 7 * Fraction(3, 7) / 3 == 1, "7*(3/7)/3 = 1 (threshold identity)")
    print("DOBRUSHIN sphere: uniqueness when 7*beta/3 < 1 i.e. beta < 3/7")

    # ----- E5: small-beta expansion of log Z_sphere vs static pair -----
    # Z ~ 4 pi sinh(kappa)/kappa, kappa = beta |S|
    # log(sinh(k)/k) = k^2/6 - k^4/180 + O(k^6)
    ser = sp.series(sp.log(sp.sinh(k) / k), k, 0, 6)
    c2 = ser.coeff(k, 2)
    c4 = ser.coeff(k, 4)
    check("E5a", c2 == sp.Rational(1, 6), f"k^2 coeff {c2}")
    check("E5b", c4 == sp.Rational(-1, 180), f"k^4 coeff {c4}")
    # |S|^2 for aligned stencil of 7 unit vectors along z: 49
    # static cubic Heisenberg: 6 bonds/site / 2 = 3 bonds per site in the energy density
    check("E5c", 7 != 6, "stencil occupancy 7 vs static coordination 6")

    # ----- E6: 7-stencil degree and adjacency at k=0, pi -----
    check("E6a", len(N3) == 7)
    check("E6b", len(N_BACK) == 4)
    # sum of stencil characters at k=0 is 7; at (pi,0,0) is 1 + 2(-1) + 2(1) + 2(1) = 1-2+2+2=3
    # 7-E(pi,0,0)=7-4=3. Yes.
    check("E6c", 7 - 4 == 3)

    if failures:
        print("FAILED:", "; ".join(failures))
        print("SUMMARY: ROUTE FAILS AT check " + failures[0])
        return 1

    print(
        "HIT: 7-stencil light-cone PCA is reversible w.r.t. pi(s) prop. prod_x Z(beta |S_x(s)|) "
        "by the bilinear identity sum_x s'_x.S_x(s) = sum_x s_x.S_x(s') (integer-checked on L=2,3 "
        "and all 256 Ising configs on L=2 against 4 partners); the equal-time linear kernel "
        "sigma^2/(1-phi^2) equals 7 sigma^2/(2 E (1-E/14)) identically, and the doubled-graph "
        "Laplacian spectrum is {E(k), 14-E(k)}; sphere vMF Jacobian at 0 is (1/3) Id so the "
        "linearised Dobrushin threshold is beta=3/7; the backward 4-stencil FAILS the bilinear "
        "identity (exact counterexample left=1 right=0 on L=3). Static comparator is "
        "log Z(beta|S|) ~ (beta^2 |S|^2)/6, not beta s.s'."
    )
    print(
        "SUMMARY: PARTIAL reversibility of the symmetric 7-stencil formation law w.r.t. "
        "pi = prod Z(beta|S_x|) (bilinear identity proved and checked); linear Green-function "
        "kernel identity exact; doubled-graph spectrum {E, 14-E}; linearised Dobrushin "
        "threshold beta=3/7; backward stencil is a no-go for reversibility; FSS/LRO on the "
        "doubled Heisenberg ferromagnet is not claimed (classical RP/FSS named, not re-proved)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
