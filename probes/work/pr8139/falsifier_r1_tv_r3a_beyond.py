#!/usr/bin/env python3
"""J:falsifier:PR8139 — R1 face-diagonal TV witness and R3(a) D_κ sets.

Falsifiers: γ^{+++}_x does not change when ω_{x+e1−e2} changes with the rest
at +x (TV would vanish); a corner κ'∉{κ,−κ} with D_{κ'}(x)=D_κ(x).
Machinery disjoint from the runner: Gibbs unnormalized weight from −log K
on the six axial bonds and +log K_3 on the three successor triples, Fraction
K=φ/Z1. Beyond: the R1 TV at (5,2,4) and (2,1,2) as well as (3,1,2); D_κ(x)
for every x in [-2,2]^3.
HIT if the stated (3,1,2) TV disagrees, the extra nonconstant triples have
TV=0, the constant rule has TV≠0, or two non-opposite corners share D.
"""
from __future__ import annotations

from fractions import Fraction as F
from itertools import product

VALS = ("+x", "-x", "+y", "-y", "+z", "-z")
OPP = {
    "+x": "-x",
    "-x": "+x",
    "+y": "-y",
    "-y": "+y",
    "+z": "-z",
    "-z": "+z",
}
E = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
CORNERS = tuple(product((-1, 1), repeat=3))
HITS: list[str] = []
STATED_TV = F(793975879125, 24719290847393)


def hit(msg: str) -> None:
    HITS.append(msg)
    print("HIT:", msg)


def phi_val(s, t, p, q, r):
    if s == t:
        return p
    if OPP[s] == t:
        return q
    return r


def make_K(p, q, r):
    Z1 = p + q + 4 * r
    K = {a: {s: F(phi_val(s, a, p, q, r), Z1) for s in VALS} for a in VALS}
    return Z1, K


def K3(K, a, b, c):
    tot = F(0)
    for s in VALS:
        tot += K[a][s] * K[b][s] * K[c][s]
    return tot


def add(x, d):
    return tuple(x[i] + d[i] for i in range(3))


def D_set(kappa, x=(0, 0, 0)):
    out = []
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            d = tuple(kappa[i] * E[i][a] - kappa[j] * E[j][a] for a in range(3))
            out.append(add(x, d))
    return frozenset(out)


def grouping(kappa):
    groups = []
    for i in range(3):
        g = frozenset(
            tuple(kappa[i] * E[i][a] - kappa[j] * E[j][a] for a in range(3))
            for j in range(3)
            if j != i
        )
        groups.append(g)
    return frozenset(groups)


def gamma_plus(K, diag):
    """γ^{+++}(s) at the origin. Axial neighbors all +x; face-diagonal
    x+e1−e2 takes value `diag`; other face-diagonals +x.

    Weight ∝ Π_{6 axial} K(s, +x)  /  Π_{k=1}^3 K_3(s, pred, pred)
    of the three successors origin+e_k. For successor e1, the other two
    predecessors are e1-e2 and e1-e3, i.e. the face-diagonals.
    """
    plus = "+x"
    # axial: six neighbors all +x → K(s,+x)^6
    # successor +e1: predecessors of +e1 are 0, e1-e2, e1-e3
    #   so K_3(s, ω_{e1-e2}, ω_{e1-e3}); e1-e2 is the distinguished diagonal
    # successor +e2: preds 0, e2-e1, e2-e3 → K_3(s, +x, +x)
    # successor +e3: preds 0, e3-e1, e3-e2 → K_3(s, +x, +x)
    w = []
    for s in VALS:
        num = K[plus][s] ** 6
        den = (
            K3(K, s, diag, plus)
            * K3(K, s, plus, plus)
            * K3(K, s, plus, plus)
        )
        w.append(num / den)
    z = sum(w)
    return [wi / z for wi in w]


def tv(u, v) -> F:
    return sum(abs(a - b) for a, b in zip(u, v)) / 2


def check_r1() -> None:
    print("== R1 face-diagonal TV (beyond executed (3,1,2) only) ==")
    triples = {
        (3, 1, 2): STATED_TV,
        (5, 2, 4): None,
        (2, 1, 2): None,
        (2, 2, 2): F(0),
    }
    for tr, stated in triples.items():
        _, K = make_K(*tr)
        g0 = gamma_plus(K, "+x")
        best = F(0)
        for alt in VALS:
            if alt == "+x":
                continue
            t = tv(g0, gamma_plus(K, alt))
            if t > best:
                best = t
        print(f"  {tr}: max TV over alt of ω_{{e1-e2}} = {best}")
        if stated is not None and best != stated:
            hit(f"R1 TV at {tr} = {best} != stated {stated}")
        if tr != (2, 2, 2) and best == 0:
            hit(
                f"R1: γ does not depend on the face-diagonal at {tr} "
                f"(TV=0; falsifier fires)"
            )
        if tr == (2, 2, 2) and best != 0:
            hit(f"R1 constant-rule control TV={best} != 0")


def check_r3a() -> None:
    print("== R3(a) D_κ(x) on [-2,2]^3, all eight corners ==")
    box = list(product(range(-2, 3), repeat=3))
    n_bad = 0
    for x in box:
        ds = {k: D_set(k, x) for k in CORNERS}
        gs = {k: grouping(k) for k in CORNERS}
        for k in CORNERS:
            mk = tuple(-a for a in k)
            if ds[k] != ds[mk]:
                n_bad += 1
                hit(f"D_κ(x) != D_{{-κ}}(x) at x={x} κ={k}")
            if len(ds[k]) != 6:
                hit(f"|D_κ(x)|={len(ds[k])} != 6 at x={x} κ={k}")
            for k2 in CORNERS:
                if k2 in (k, mk):
                    continue
                if ds[k2] == ds[k]:
                    n_bad += 1
                    hit(f"D_{k2}(x)=D_{k}(x) at x={x} with κ' not ±κ")
                if gs[k2] == gs[k]:
                    n_bad += 1
                    hit(f"grouping({k2})=grouping({k}) (not opposite)")
            if n_bad >= 3:
                break
        if n_bad >= 3:
            break
    print(f"  sites={len(box)} corners=8 mismatches_logged={n_bad}")


def main() -> int:
    check_r1()
    check_r3a()
    if HITS:
        print("SUMMARY: FALSIFIER (PR #8139): " + "; ".join(HITS[:3]))
        return 0
    print(
        "SUMMARY: FALSIFIER (PR #8139): R1 face-diagonal TV at (3,1,2) equals "
        f"{STATED_TV}; extra triples (5,2,4) and (2,1,2) have TV>0 and the "
        "constant rule has TV=0; R3(a) D_κ(x)=D_{−κ}(x) and is distinct for "
        "other corners at every x in [-2,2]^3; does not fire"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
