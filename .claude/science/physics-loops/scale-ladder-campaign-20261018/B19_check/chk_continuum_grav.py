#!/usr/bin/env python3
"""B19 check, gravity sector (fresh code; Fourier-kernel zero test, sympy euler_equations).

K11  [sqrt g R]^(2) symbol == 09-23 note's R2 (block 62 T3) formula, with the same normalisation as R1.
K8   TT graviton speed^2 from C(N=1) = kin - K1 R1 - K2 R2: K2/(4 alpha)  (block-62 kinetic at beta=-alpha).
K12  {C_g(N), lam1 G1 + G2} at degree 1 in h with a FULLY GENERAL (no rotation covariance, no parity) local
     G2 = sum P_ab W_ab, W_ab = sum alpha h_cd d_k xi_l + beta xi_l d_k h_cd  (648 coefficients),
     and a fully general lapse rule N' = S1_kl xi_k d_l N + S2_kl N d_k xi_l (18 coefficients):
     is (S1, S2) unique, = (-lam1 K2/K1) delta, 0 ?  Exact rationals at three random parameter points.
K12b G2 = 0 has no solution (unless K2 = 0).
K12c the same with the ISOTROPIC 12-term ansatz written independently, symbolic lam1, K1, K2.
"""
from __future__ import annotations
import sys, time, pickle, random
from fractions import Fraction
import sympy as sp
from sympy.polys.matrices import DomainMatrix
from fourier_core import X, vd, I
from grav_common import COMP, HF, PF, NF, XIF, h, kin, ft, D

RES = {"pass": 0, "fail": 0}
def check(tag, ok, msg):
    RES["pass" if ok else "fail"] += 1
    print(("PASS" if ok else "FAIL") + f": {tag} {msg}", flush=True)

R1, R2 = pickle.load(open("R12.pkl", "rb"))
kN = sp.symbols("kN0:3"); kX = sp.symbols("kX0:3")
kH = [-kN[j] - kX[j] for j in range(3)]
AX = sp.symbols("X0:3")
AH = {ab: sp.Symbol(f"H{ab[0]}{ab[1]}") for ab in COMP}
mom = {"N": (sp.Integer(1), kN), **{f"xi{k}": (AX[k], kX) for k in range(3)},
       **{f"h{a}{b}": (AH[(a, b)], kH) for (a, b) in COMP}}

def Hm(i, j): return AH[(min(i, j), max(i, j))]

# ---------------------------------------------------------------- K11
def k11():
    p = sp.symbols("p0:3")
    H1 = {ab: sp.Symbol(f"U{ab[0]}{ab[1]}") for ab in COMP}
    # polarised kernel of int R2: h = U e^{ipx} (copy 1) + U' e^{-ipx} (copy 2), coefficient of the bilinear, then U'=U
    t1, t2 = sp.symbols("t1 t2")
    sub = {}
    for (a, b) in COMP:
        f1 = sp.Function(f"h{a}{b}__1")(*X); f2 = sp.Function(f"h{a}{b}__2")(*X)
        sub[HF[(a, b)]] = t1 * f1 + t2 * f2
    E = sp.expand(R2.subs(sub).doit())
    E = sp.Poly(E, t1, t2).coeff_monomial(t1 * t2)
    m = {**{f"h{a}{b}__1": (H1[(a, b)], p) for (a, b) in COMP}, **{f"h{a}{b}__2": (H1[(a, b)], [-x for x in p]) for (a, b) in COMP}}
    ker = sp.expand(ft(E, m) / 2)
    Hm1 = sp.Matrix(3, 3, lambda i, j: H1[(min(i, j), max(i, j))])
    pv = sp.Matrix(p); p2 = sum(x ** 2 for x in p); tr = Hm1.trace()
    # 09-23 note: R2 = -(p^2/4) tr(h^2) + (hp).(hp)/2 - (p.h.p) tr h/2 + p^2 (tr h)^2/4
    b62 = -(p2 / 4) * (Hm1 * Hm1).trace() + (Hm1 * pv).dot(Hm1 * pv) / 2 - (pv.T * Hm1 * pv)[0] * tr / 2 + p2 * tr ** 2 / 4
    # R1 normalisation: 09-23 R1 = p^2 tr h - p.h.p ; continuum R1 = d_i d_j h_ij - lap tr h -> symbol -(p.h.p) + p^2 tr h
    r1 = sp.expand(ft(R1, {f"h{a}{b}": (H1[(a, b)], p) for (a, b) in COMP}))
    r1_note = p2 * tr - (pv.T * Hm1 * pv)[0]
    check("K11", sp.expand(ker - b62) == 0 and sp.expand(r1 - r1_note) == 0,
          "[sqrt g R]^(2) of g = delta + h has exactly the 09-23/block-62 R2 symbol AND [sqrt g R]^(1) has the note's R1 symbol "
          "with the same sign/normalisation: one K on both in K wbar(u R1 + R2) <=> K1 = K2 in C = kin - K1 R1 - K2 R2")

# ---------------------------------------------------------------- K8
def k8():
    al, K2 = sp.symbols("alpha K2", positive=True)
    pz = sp.Symbol("pz")
    # potential -K2 R2 on h01(z) only: symbol from K11 formula with H = [[0,b,0],[b,0,0],[0,0,0]], p = (0,0,pz)
    b = sp.Symbol("b")
    Hm1 = sp.Matrix([[0, b, 0], [b, 0, 0], [0, 0, 0]]); pv = sp.Matrix([0, 0, pz]); p2 = pz ** 2; tr = 0
    r2 = -(p2 / 4) * (Hm1 * Hm1).trace() + (Hm1 * pv).dot(Hm1 * pv) / 2 - (pv.T * Hm1 * pv)[0] * tr / 2
    # Hamiltonian per mode: P01^2/(8 alpha) + (-K2) r2 ;  H = A P^2 + B b^2  -> omega^2 = 4 A B
    B = sp.expand(-K2 * r2).coeff(b, 2); A = 1 / (8 * al)
    w2 = sp.simplify(4 * A * B / p2)
    check("K8", sp.simplify(w2 - K2 / (4 * al)) == 0 and sp.simplify(B) == sp.simplify(K2 * pz ** 2 / 2),
          f"TT h01(z): omega^2/k^2 = {w2} (positive for K2 > 0: -K2 R2 is the GR-sign potential); cf. 09-23 T2 K wbar^2 p^2/(4 alpha)")

# ---------------------------------------------------------------- K12
def W_general():
    """general W_ab with 648 coefficients, returned in Fourier form."""
    al = {}; W = {}
    for ab in COMP:
        w = 0
        for cd in COMP:
            for k in range(3):
                for l in range(3):
                    a1 = sp.Symbol(f"a_{ab[0]}{ab[1]}_{cd[0]}{cd[1]}_{k}{l}")
                    b1 = sp.Symbol(f"b_{ab[0]}{ab[1]}_{cd[0]}{cd[1]}_{k}{l}")
                    al[a1] = 1; al[b1] = 1
                    w += a1 * AH[cd] * (I * kX[k]) * AX[l] + b1 * AX[l] * (I * kH[k]) * AH[cd]
        W[ab] = sp.expand(w)
    return W, list(al)


def W_iso(mu):
    """isotropic 12-term ansatz, written independently (Fourier form)."""
    q = kX; p = kH
    Hm1 = lambda i, j: Hm(i, j)
    trh = sum(Hm1(k, k) for k in range(3))
    dx = lambda i, j: I * q[i] * AX[j]          # d_i xi_j
    div = sum(dx(k, k) for k in range(3))
    dh = lambda k, i, j: I * p[k] * Hm1(i, j)
    dtr = lambda k: I * p[k] * trh
    dl = lambda i, j: 1 if i == j else 0
    terms = [
        lambda i, j: sum(AX[k] * dh(k, i, j) for k in range(3)),
        lambda i, j: sum(Hm1(i, k) * dx(j, k) + Hm1(j, k) * dx(i, k) for k in range(3)),
        lambda i, j: sum(Hm1(k, i) * dx(k, j) + Hm1(k, j) * dx(k, i) for k in range(3)),
        lambda i, j: dl(i, j) * sum(Hm1(k, l) * dx(k, l) for k in range(3) for l in range(3)),
        lambda i, j: dl(i, j) * trh * div,
        lambda i, j: Hm1(i, j) * div,
        lambda i, j: trh * (dx(i, j) + dx(j, i)),
        lambda i, j: dl(i, j) * sum(AX[k] * dtr(k) for k in range(3)),
        lambda i, j: sum(AX[k] * (dh(i, j, k) + dh(j, i, k)) for k in range(3)),
        lambda i, j: dl(i, j) * sum(AX[k] * dh(l, k, l) for k in range(3) for l in range(3)),
        lambda i, j: AX[i] * dtr(j) + AX[j] * dtr(i),
        lambda i, j: sum(AX[i] * dh(k, k, j) + AX[j] * dh(k, k, i) for k in range(3)),
    ]
    return {ab: sp.expand(sum(mu[n] * terms[n](*ab) for n in range(12))) for ab in COMP}


def grav_pieces():
    """Fourier pieces: V_ab = FT vd(-N R1, h_ab) [N only];  Q = sum_ab FT vd(-N R2, h_ab) * FT(d_a xi_b + d_b xi_a);
       R1h = FT(R1(h)) [h only]."""
    V = {ab: ft(vd(-NF * R1, HF[ab]), mom) for ab in COMP}
    Q = 0
    for ab in COMP:
        a, b = ab
        sym = I * kX[a] * AX[b] + I * kX[b] * AX[a]
        Q += ft(vd(-NF * R2, HF[ab]), mom) * sym
    R1h = ft(R1, mom)
    return V, sp.expand(Q), R1h


def lapse_general():
    S1 = sp.Matrix(3, 3, lambda k, l: sp.Symbol(f"S1_{k}{l}"))
    S2 = sp.Matrix(3, 3, lambda k, l: sp.Symbol(f"S2_{k}{l}"))
    Np = sum(S1[k, l] * AX[k] * (I * kN[l]) + S2[k, l] * (I * kX[k]) * AX[l] for k in range(3) for l in range(3))
    return S1, S2, sp.expand(Np)


def eqs_from(expr):
    gens = list(kN) + list(kX) + list(AX) + list(AH.values())
    return [c for c in sp.Poly(sp.expand(expr), *gens).coeffs() if c != 0]


def solve_unique(eqs, unknowns, targets):
    """exact linear solve; returns (consistent, {target: value or None if not unique}, nullity)."""
    A, b = sp.linear_eq_to_matrix(eqs, unknowns)
    M = DomainMatrix.from_Matrix(A.row_join(b)).convert_to(sp.QQ_I)
    R, piv = M.rref()
    n = len(unknowns)
    if n in piv:
        return False, {}, None
    Rm = R.to_Matrix()
    free = [j for j in range(n) if j not in piv]
    out = {}
    for t in targets:
        j = unknowns.index(t)
        if j not in piv:
            out[t] = None; continue
        r = piv.index(j)
        if any(Rm[r, f] != 0 for f in free):
            out[t] = None
        else:
            out[t] = sp.nsimplify(Rm[r, n])
    return True, out, len(free)


def k12():
    t0 = time.time()
    V, Q, R1h = grav_pieces()
    W, coeffs = W_general()
    S1, S2, Np = lapse_general()
    Wdot = sp.expand(sum(V[ab] * W[ab] for ab in COMP))
    print(f"   pieces built in {time.time()-t0:.1f}s", flush=True)
    Svars = list(S1) + list(S2)
    rng = random.Random(20261018)
    allok = True
    for trial in range(3):
        lam1 = sp.Rational(rng.randint(1, 9), rng.randint(1, 9))
        K1 = sp.Rational(rng.randint(1, 9), rng.randint(1, 9))
        K2 = sp.Rational(rng.randint(1, 9), rng.randint(1, 9))
        # {C(N), G} degree 1 = K1 * Wdot (C = -K1 R1 - K2 R2 acts on delta h = W) + lam1*K2*Q ;  RHS C^(1)(N') = -K1 N' R1
        expr = K1 * Wdot + lam1 * K2 * Q - (-K1 * Np * R1h)
        eqs = eqs_from(expr)
        ok, sol, nul = solve_unique(eqs, coeffs + Svars, Svars)
        exp1 = -lam1 * K2 / K1
        good = ok and all(sol[S1[k, l]] == (exp1 if k == l else 0) for k in range(3) for l in range(3)) \
            and all(sol[S2[k, l]] == 0 for k in range(3) for l in range(3))
        print(f"   trial {trial}: lam1={lam1} K1={K1} K2={K2}: consistent={ok}, #eqs={len(eqs)}, nullity(G2 space)={nul}, "
              f"S1 diag={[sol.get(S1[k,k]) for k in range(3)]} (expect {exp1}), S1 offdiag unique-zero={all(sol.get(S1[k,l])==0 for k in range(3) for l in range(3) if k!=l)}, S2 all 0={all(sol.get(x)==0 for x in S2)}", flush=True)
        allok = allok and good
        if trial == 0:
            # K12b: G2 = 0
            expr0 = lam1 * K2 * Q + K1 * Np * R1h
            ok0, _, _ = solve_unique(eqs_from(expr0), Svars, Svars)
            check("K12b", not ok0, "with G2 = 0 (only the linear shift lam1 G1) the degree-1 bracket has NO lapse rule N' (general 18-coefficient N'), K2 != 0")
    check("K12", allok, "fully general local G2 (648 coeffs, no isotropy/parity assumed) + fully general N' (18 coeffs): the h-linear "
          "{C_g(N), lam1 G1 + G2} = C^(1)(N') is solvable and FORCES N' = -(lam1 K2/K1) xi.dN exactly (S1 = -lam1 K2/K1 * delta, S2 = 0), "
          "at three random rational points; G2 itself has a nonzero null space")
    return V, Q, R1h


def k12c(V, Q, R1h):
    mu = sp.symbols("m1:13"); s1, s2 = sp.symbols("s1 s2"); lam1, K1, K2 = sp.symbols("lam1 K1 K2", nonzero=True)
    W = W_iso(mu)
    Np = s1 * sum(AX[k] * I * kN[k] for k in range(3)) + s2 * sum(I * kX[k] * AX[k] for k in range(3))
    expr = K1 * sum(V[ab] * W[ab] for ab in COMP) + lam1 * K2 * Q + K1 * Np * R1h
    sol = sp.solve(eqs_from(expr), list(mu) + [s1, s2], dict=True)
    print("   isotropic solution:", sol)
    ok = len(sol) == 1 and sp.simplify(sol[0][s1] + lam1 * K2 / K1) == 0 and sol[0][s2] == 0
    free = [m for m in mu if m not in sol[0]]
    # Lie completion lam1*K2/K1*(T1+T2) must be a particular solution
    lie = {m: 0 for m in mu}; lie[mu[0]] = lam1 * K2 / K1; lie[mu[1]] = lam1 * K2 / K1
    lie_ok = all(sp.simplify(sol[0][m].subs(lie) - lie[m]) == 0 for m in sol[0] if m in mu) if ok else False
    check("K12c", ok and lie_ok, f"isotropic 12-term ansatz (independent transcription), symbolic: s1 = -lam1 K2/K1, s2 = 0 unique; "
          f"G2 = (lam1 K2/K1) * Lie completion + {len(free)}-dim null family {free}")


if __name__ == "__main__":
    k11(); k8()
    V, Q, R1h = k12()
    k12c(V, Q, R1h)
    print(f"TOTAL: PASS={RES['pass']} FAIL={RES['fail']}")
