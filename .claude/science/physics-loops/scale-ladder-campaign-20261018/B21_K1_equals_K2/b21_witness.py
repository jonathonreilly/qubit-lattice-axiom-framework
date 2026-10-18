#!/usr/bin/env python3
"""B21 witness check on a DIFFERENT code path (B19_check's sympy-Function machinery: euler_equations variational
derivatives + fourier_core kernels; copies, unmodified), with no unknowns: every coefficient fixed to exact rationals.

Witness W(r): lam1 = r nu, nu = 1, K1 = 3, K2 = K1/r, alpha = 5, b = -1/2, G2 = int P L_xi h,
              kin1 = (1/r) DeWitt-h-linear, lapse N' = -xi.dN, structure function zeta = (delta - h/r)(N dM - M dN),
              c0 = K1/(4 alpha lam1).
W1  r = 2 (so K1 = 3, K2 = 3/2: K1 != K2): every bracket computed in b21_brackets closes exactly.
W2  negative control: r = 2 but K2 := K1 (block-62 value with lam1 != nu): the h-linear {C,G} fails.
W3  r = 1 (K1 = K2 = 3): closes (the member's normalisation).
Brackets: {G,G} deg 1, 2;  {C,G} deg 1 (h), deg 2 (P^2);  {C,C} deg 1 (P), deg 2 (P h).
"""
from __future__ import annotations
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
from fourier_core import X, Fn, pb, Slot, kernel_eqs
from grav_common import COMP, HF, PF, NF, XIF, h, D, load_R12

T0 = time.time()
RES = {"pass": 0, "fail": 0}


def check(tag, ok, msg):
    RES["pass" if ok else "fail"] += 1
    print(("PASS" if ok else "FAIL") + f": {tag} [{time.time()-T0:.0f}s] {msg}", flush=True)


ETAF = [Fn(f"eta{k}") for k in range(3)]
MF = Fn("M")
PAIRS = [(HF[ab], PF[ab]) for ab in COMP]
R = range(3)
R1, R2 = load_R12(os.path.join(os.path.dirname(os.path.abspath(__file__)), "R12.pkl"))


def Pt(i, j):
    ab = (min(i, j), max(i, j))
    return PF[ab] if i == j else PF[ab] / 2


trh = sum(h(k, k) for k in R)
trP = sum(Pt(k, k) for k in R)
trPP = sum(Pt(i, j) * Pt(j, i) for i in R for j in R)
trhP = sum(h(i, j) * Pt(j, i) for i in R for j in R)
trhPP = sum(h(i, j) * Pt(j, k) * Pt(k, i) for i in R for j in R for k in R)
SH = Slot("h", [HF[ab] for ab in COMP]); SP = Slot("P", [PF[ab] for ab in COMP])
SP2 = Slot("P", [PF[ab] for ab in COMP], mult=2)
SN = Slot("N", [NF]); SM = Slot("M", [MF]); SX = Slot("xi", XIF); SE = Slot("eta", ETAF)


def G(xi, lam1, nu):
    """lam1 int P L_xi delta + nu int P L_xi h, written directly as Lie derivatives (not via the 12-term ansatz)."""
    g1 = sum(Pt(i, j) * (D(xi[j], i) + D(xi[i], j)) for i in R for j in R)
    lh = lambda i, j: sum(xi[k] * D(h(i, j), k) + h(k, j) * D(xi[k], i) + h(i, k) * D(xi[k], j) for k in R)
    g2 = sum(Pt(i, j) * lh(i, j) for i in R for j in R)
    return sp.expand(lam1 * g1 + nu * g2)


def run(tag, r, K2override=None, expect=True):
    nu = sp.Integer(1); lam1 = r * nu; K1 = sp.Integer(3); al = sp.Integer(5)
    K2 = K1 / r if K2override is None else K2override
    kin0 = (trPP - trP ** 2 / 2) / (4 * al)
    kin1 = (2 * trhPP - trP * trhP - trh * (trPP - trP ** 2 / 2) / 2) / (4 * al * r)
    C = lambda L: sp.expand(L * (kin0 + kin1 - K1 * R1 - K2 * R2))
    out = {}
    # {G,G}
    lb = [sum(XIF[k] * D(ETAF[i], k) - ETAF[k] * D(XIF[i], k) for k in R) for i in R]
    gg = pb(G(XIF, lam1, nu), G(ETAF, lam1, nu), PAIRS) - nu * G(lb, lam1, nu)
    out["GG1"] = kernel_eqs(gg, [SP, SX, SE]) == []
    out["GG2"] = kernel_eqs(gg, [SH, SP, SX, SE]) == []
    # {C,G}
    Np = -nu * sum(XIF[i] * D(NF, i) for i in R)
    cg = pb(C(NF), G(XIF, lam1, nu), PAIRS) - C(Np)
    out["CG1"] = kernel_eqs(cg, [SN, SX, SH]) == []
    out["CG2P"] = kernel_eqs(cg, [SN, SX, SP2]) == []
    # {C,C}
    z0 = [NF * D(MF, i) - MF * D(NF, i) for i in R]
    zeta = [z0[i] - sum(h(i, j) * z0[j] for j in R) / r for i in R]
    c0 = K1 / (4 * al * lam1)
    cc = pb(C(NF), C(MF), PAIRS) - c0 * G(zeta, lam1, nu)
    out["CC1"] = kernel_eqs(cc, [SN, SM, SP]) == []
    out["CC2"] = kernel_eqs(cc, [SN, SM, SP, SH]) == []
    print(f"   {tag}: r={r} lam1={lam1} K1={K1} K2={K2}: {out}", flush=True)
    return out


if __name__ == "__main__":
    o1 = run("W1", sp.Integer(2))
    check("W1", all(o1.values()), "r = 2 (lam1 = 2 nu): K1 = 3, K2 = 3/2 -- all six bracket sectors close exactly "
          "(independent code path, no unknowns): closure does NOT force K1 = K2")
    o2 = run("W2", sp.Integer(2), K2override=sp.Integer(3))
    check("W2", (not o2["CG1"]) and o2["GG1"] and o2["GG2"], "negative control: lam1 = 2 nu with K2 = K1 = 3 fails the h-linear {C,G} "
          "(the bracket fixes lam1 K2 = nu K1, not K1 = K2)")
    o3 = run("W3", sp.Integer(1))
    check("W3", all(o3.values()), "r = 1 (lam1 = nu, h = g - delta): K1 = K2 = 3 closes in all six sectors (the member's point)")
    print(f"TOTAL: PASS={RES['pass']} FAIL={RES['fail']}  ({time.time()-T0:.0f}s)")
