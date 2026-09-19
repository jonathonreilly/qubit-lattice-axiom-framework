#!/usr/bin/env python3
"""J:attack-g:PR8169 — brute-force Thm 1–3 algebraic identities.

Bisector 180° at the orthogonal reference is (x,y,z)↦(z,-y,x), equals
Rodrigues 2uu^T-I about u=(e_x+e_z)/√2, swaps q↔q' and preserves S.
180° about q sends q'↦-q' at t=0. Cube Aut: S(gq,gq')=gS.
Gibbs α/γ=exp(2β(1+t)); at t=0, e^{2β}=2: α=1/3, γ=1/6.
Linear α=(1+λ(1+t))/4; distinct iff |q·q'|<1.
"""
from __future__ import annotations

import itertools
import sys
from fractions import Fraction as Fr

import sympy as sp


def hits(msg: str) -> int:
    print(f"HIT: {msg}")
    print(f"SUMMARY: HIT - {msg}")
    return 0


def main() -> int:
    q = sp.Matrix([0, 0, 1])
    qp = sp.Matrix([1, 0, 0])
    S = [q, qp, -q, -qp]
    R = sp.Matrix([[0, 0, 1], [0, -1, 0], [1, 0, 0]])
    if R.det() != 1 or R.T * R != sp.eye(3):
        return hits("stated bisector map is not in SO(3)")
    u = sp.Matrix([1, 0, 1]) / sp.sqrt(2)
    Rrod = 2 * u * u.T - sp.eye(3)
    if sp.simplify(Rrod - R) != sp.zeros(3):
        return hits("stated map != Rodrigues 180° about (e_x+e_z)/√2")
    images = [sp.simplify(R * s) for s in S]
    if R * q != qp or R * qp != q:
        return hits("bisector 180° does not swap q with q'")
    if {tuple(sp.simplify(v)) for v in images} != {tuple(s) for s in S}:
        return hits("bisector 180° does not preserve S")
    print("bisector 180° (x,y,z)->(z,-y,x) swaps q↔q' and preserves S: True")

    Rz = sp.Matrix([[-1, 0, 0], [0, -1, 0], [0, 0, 1]])  # 180° about q=e_z
    if Rz * qp != -qp or Rz * q != q:
        return hits("180° about q does not send q' to -q' at t=0")
    if {tuple(Rz * s) for s in S} != {tuple(s) for s in S}:
        return hits("180° about q does not preserve S")
    print("180° about q sends q' to -q' and preserves S: True")

    # cube Aut: proper signed permutation matrices
    def cube_rotations():
        out = []
        for perm in itertools.permutations(range(3)):
            for signs in itertools.product((-1, 1), repeat=3):
                M = sp.zeros(3)
                for i in range(3):
                    M[i, perm[i]] = signs[i]
                if M.det() == 1:
                    out.append(M)
        return out

    rots = cube_rotations()
    if len(rots) != 24:
        return hits(f"|cube SO|={len(rots)} != 24")
    axes = [
        sp.Matrix([1, 0, 0]),
        sp.Matrix([0, 1, 0]),
        sp.Matrix([0, 0, 1]),
        sp.Matrix([-1, 0, 0]),
        sp.Matrix([0, -1, 0]),
        sp.Matrix([0, 0, -1]),
    ]
    n_checked = 0
    for g in rots:
        for a, b in itertools.product(axes, repeat=2):
            t = (a.T * b)[0]
            Sa = [a, b, -a, -b]
            npts = len({tuple(p) for p in Sa})
            if (sp.Abs(t) < 1) != (npts == 4):
                return hits(f"distinct iff |q·q'|<1 fails at t={t} n={npts}")
            gS = {tuple(sp.simplify(g * p)) for p in Sa}
            Sg = {tuple(sp.simplify(p)) for p in [g * a, g * b, -g * a, -g * b]}
            if gS != Sg:
                return hits("S(gq,gq') != g S(q,q') under a cube rotation")
            n_checked += 1
    print(f"cube Aut covariance and distinctness on {n_checked} pairs: True")

    # Gibbs ratio
    beta, t = sp.symbols("beta t", real=True)
    qsum_dot = {  # s · (q+q') = ±(1+t)
        "copy": 1 + t,
        "flip": -(1 + t),
    }
    ratio = sp.exp(beta * qsum_dot["copy"]) / sp.exp(beta * qsum_dot["flip"])
    if sp.simplify(ratio - sp.exp(2 * beta * (1 + t))) != 0:
        return hits("Gibbs α/γ != exp(2β(1+t))")
    # masses at t=0, e^{2β}=2
    e2b = Fr(2)
    # α/γ = e^{2β} = 2; 2α+2γ=1
    # α=2γ, 2(2γ)+2γ=1, 6γ=1, γ=1/6, α=1/3
    gamm = Fr(1, 6)
    alph = Fr(1, 3)
    if alph / gamm != e2b or 2 * alph + 2 * gamm != 1:
        return hits("t=0 e^{2β}=2 masses are not α=1/3, γ=1/6")
    if alph != Fr(1, 3) or gamm != Fr(1, 6):
        return hits("stated 1/3, 1/6 failed")
    print("Gibbs α/γ=exp(2β(1+t)); t=0 e^{2β}=2 => α=1/3 γ=1/6: True")

    lam, tt = sp.symbols("lam t", real=True)
    # four unnormalized masses: two copies 1+λ(1+t), two flips 1-λ(1+t); sum=4
    Z = 2 * (1 + lam * (1 + tt)) + 2 * (1 - lam * (1 + tt))
    if sp.simplify(Z - 4) != 0:
        return hits("linear family normalizer != 4")
    alpha_lin = (1 + lam * (1 + tt)) / 4
    if sp.simplify(alpha_lin - (1 + lam * (1 + tt)) / 4) != 0:
        return hits("linear α formula")
    for lam0, want in ((0, Fr(1, 4)), (1, Fr(1, 2)), (-1, 0)):
        a0 = (1 + lam0 * (1 + 0)) / 4
        if a0 != want:
            return hits(f"linear t=0 λ={lam0} α={a0} != {want}")
    print("linear family α=(1+λ(1+t))/4; λ=0,±1 at t=0: True")

    # Born four-tuple at orthogonal reference
    born = []
    for s in S:
        val = (1 + (s.T * q)[0]) / 2
        born.append(sp.simplify(val))
    if born != [1, sp.Rational(1, 2), 0, sp.Rational(1, 2)]:
        return hits(f"Born four-tuple {born}")
    if sum(born) != 2:
        return hits(f"Born sum {sum(born)} != 2")
    print("Born on S at t=0 is (1,1/2,0,1/2) sums to 2: True")

    # path3 cardinalities
    L = q
    Rvec = qp
    chain = {tuple(L), tuple(-L)}
    ends = {tuple(p) for p in [L, Rvec, -L, -Rvec]}
    print(f"chain |supp|={len(chain)} ends-first |supp|={len(ends)}")
    if len(chain) != 2 or len(ends) != 4:
        return hits("path3 support cardinalities are not 2 vs 4")
    collinear = {tuple(p) for p in [L, L, -L, -L]}
    if len(collinear) != 2:
        return hits("collinear control does not collapse to 2")

    print(
        "SUMMARY: pattern has no purchase on this note: bisector/axis 180° maps, "
        "cube Aut covariance, Gibbs ratio and 1/3–1/6 masses, linear family, "
        "Born sum 2, and path3 cardinalities 2 vs 4 all hold as written"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
