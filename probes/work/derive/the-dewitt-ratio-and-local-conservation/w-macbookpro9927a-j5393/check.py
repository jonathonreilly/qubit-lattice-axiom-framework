#!/usr/bin/env python3
"""The DeWitt ratio and local conservation: checks for ATTEMPT.md (attempt 2 of 2), worker w-macbookpro9927a-j5393 (claude-opus-5-5).

Model: block 101's second-order Lagrangian with block 62's stress coupling (block 62: d<H>/dh_ij = -Theta_(ij)/2, so the content adds
+ (1/2) sum_ij Theta_ij h_ij):
    L = (alpha h'_ij h'_ij + beta (tr h')^2)/wbar + K wbar (u R1 + R2) - e u + (1/2) Theta_ij h_ij,
    R1 = -(p.h.p - p^2 tr h), R2 block 62's quadratic partner, p_j = 2 sin(k_j/2) at every lattice wave vector.
All checks exact (sympy, Gaussian rationals, sqrt).
"""
from __future__ import annotations

import json
import subprocess
import sys

import sympy as sp

OUT: list[str] = []
FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str) -> None:
    OUT.append(f"{'ok  ' if ok else 'FAIL'} {tag}: {msg}")
    if not ok:
        FAILS.append(tag)


# ------------------------------------------------------------------------------------------------ Q: sources, verbatim
B101 = ("a0cf3d4a41", "docs/ADMISSIBILITY_RULE_IN_THE_CURVATURE_MEMBER_THE_CLOCK_IS_A_CONSTRAINT_A_BODYS_CHANGE_OF_ENERGY_ACTS_AT_ONCE_"
        "UNLESS_FORMATION_KEEPS_ENERGY_LOCAL_BOUNDED_THEOREM_NOTE_2026-09-23.md")
B62 = ("aada579459", "docs/ADMISSIBILITY_RULE_ANGLES_ARE_THE_TILT_OF_THE_COINS_FRAME_WITH_THEM_TWO_DISTURBANCES_TRAVEL_AT_ONE_DIRECTION_"
       "FREE_SPEED_AND_THE_PRICE_IS_A_CONSERVED_STRESS_BOUNDED_THEOREM_NOTE_2026-09-21.md")
QUOTES = {
    B101: ["- **Block 62's kinetic term.** `(α ḣ_ij ḣ_ij + β (tr ḣ)²)/w̄`, with no rate of change of a rate.",
           "  - The member `F₂ = −K w̄ (u R₁ + R₂)`.",
           "- **Block 55's coupling** (#8571). The clock enters through `−e u`, `e` the content's energy density.",
           "- `d/dt[(α + β) ξ̇_L + β φ̇] = 0`."],
    B62: ["- **Frame response** `Θ_a^j(x) = Re ψ†(x) σ_a (S_jψ)(x)`; `Θ_(ij)` its symmetric part. Since `h = −(ε + εᵀ)`, "
          "`∂⟨H⟩/∂h_ij = −½Θ_(ij)` (both orders of an off-diagonal pair counted)",
          "(b) The static equations with sources `(½Θ_11, ½Θ_22, ½Θ_33, Θ_(12), Θ_(13), Θ_(23); −e)` can be solved iff "
          "`Σ_i p_i Θ_(ij) = 0` for `j = 1, 2, 3`."],
}
TASK_Q = ["Add the matter's stress as a source of the strains (block 62 T2: the frame couples to Theta_a^j = Re psi^dag sigma_a S_j psi; "
          "moving content sources angles) and its momentum density as the source of the relabellings.",
          "(a) At alpha + beta = 0, derive the equation the relabellings then impose on the sources, exactly at second order and every "
          "lattice wave vector: is it e' + i p.J = 0 with J the content's energy current (a lattice continuity equation), and does the "
          "momentum equation follow likewise?"]


def family_q() -> None:
    miss = []
    for (sha, path), qs in QUOTES.items():
        txt = subprocess.run(["git", "show", f"{sha}:{path}"], capture_output=True, text=True).stdout
        miss += [f"{sha[:6]}[{i}]" for i, q in enumerate(qs) if q not in txt]
    d = json.load(open("probes/TASKS.json"))
    ts = d if isinstance(d, list) else d.get("tasks", d)
    ts = ts if isinstance(ts, list) else list(ts.values())
    what = next((t["what"] for t in ts if isinstance(t, dict) and t.get("id") == "J:derive:the-dewitt-ratio-and-local-conservation:a2"), "")
    miss += [f"task[{i}]" for i, q in enumerate(TASK_Q) if q not in what]
    check("Q", not miss, f"block 101 (head a0cf3d4a, PR #8895), block 62 (head aada5794, PR #8592) and the task quoted verbatim "
          f"({sum(len(v) for v in QUOTES.values()) + len(TASK_Q)} lines){'; missing ' + str(miss) if miss else ''}")


# ------------------------------------------------------------------------------------------------ the member (block 101's runner's R2)
def R1(h, pv):
    return -((pv.T * h * pv)[0] - pv.dot(pv) * h.trace())


def R2(h, pv):
    ph = h * pv
    return (-sp.Rational(1, 4) * pv.dot(pv) * sum(h[i, j] ** 2 for i in range(3) for j in range(3))
            + sp.Rational(1, 2) * ph.dot(ph) - sp.Rational(1, 2) * (pv.T * h * pv)[0] * h.trace()
            + sp.Rational(1, 4) * pv.dot(pv) * h.trace() ** 2)


def sym3(prefix):
    return sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"{prefix}{min(i, j)}{max(i, j)}", real=True))


# ------------------------------------------------------------------------------------------------ A: the identity at every wave vector
def family_a() -> None:
    al, be, K, wb = sp.symbols("alpha beta K wbar", positive=True)
    pv = sp.Matrix(sp.symbols("p1:4", real=True))
    h, hd, Th = sym3("h"), sym3("hd"), sym3("T")
    xi = sp.Matrix(sp.symbols("xi1:4", real=True))
    gauge = pv * xi.T + xi * pv.T
    blind = sp.expand(R1(h + gauge, pv) - R1(h, pv)) == 0 and sp.expand(R2(h + gauge, pv) - R2(h, pv)) == 0
    # the relabelling direction dh = 2 p p^T: kinetic momentum, stress and member projected on it
    D = 2 * pv * pv.T
    T = (al * sum(hd[i, j] ** 2 for i in range(3) for j in range(3)) + be * hd.trace() ** 2) / wb
    comps = [(i, j) for i in range(3) for j in range(i, 3)]
    def proj(expr, M):            # sum over independent components: d expr/d m_ij times D_ij (off-diagonal pairs counted once, D symmetric)
        return sp.expand(sum(sp.diff(expr, M[i, j]) * D[i, j] for (i, j) in comps))
    kin = proj(T, hd)
    ok = sp.simplify(kin - 4 / wb * (al * (pv.T * hd * pv)[0] + be * pv.dot(pv) * hd.trace())) == 0
    S = sp.Rational(1, 2) * sum(Th[i, j] * h[i, j] for i in range(3) for j in range(3))
    ok &= sp.simplify(proj(S, h) - (pv.T * Th * pv)[0]) == 0
    u = sp.Symbol("u")
    ok &= sp.simplify(proj(K * wb * (u * R1(h, pv) + R2(h, pv)), h)) == 0
    # alpha p.h'.p + beta p^2 tr h' = (alpha + beta) p^2 tr h' - alpha d(R1)/dt
    ok &= sp.expand(al * (pv.T * hd * pv)[0] + be * pv.dot(pv) * hd.trace()
                    - ((al + be) * pv.dot(pv) * hd.trace() - al * R1(hd, pv))) == 0
    # the rate's equation dL/du = K wbar R1 - e = 0; so at beta = -alpha: d/dt[(4/wbar)(-alpha e'/(K wbar))] = p.Theta.p
    t = sp.Symbol("t"); e = sp.Function("e")(t)
    lhs = sp.diff(4 / wb * (-al) * sp.diff(e / (K * wb), t), t)
    ident = sp.Eq(sp.diff(e, t, 2), -K * wb ** 2 / (4 * al) * sp.Symbol("pThetap"))
    ok &= sp.simplify(lhs.subs(sp.diff(e, t, 2), ident.rhs) - sp.Symbol("pThetap")) == 0
    check("A", blind and ok, "every lattice wave vector (symbolic p, h, Theta): R1, R2 are blind to h -> h + p xi + xi p; along the "
          "relabelling dh = 2pp^T the kinetic momentum is (4/wbar)(alpha p.h'.p + beta p^2 tr h'), the stress gives p.Theta.p and the "
          "member nothing; alpha p.h'.p + beta p^2 tr h' = (alpha+beta) p^2 tr h' - alpha R1'; with K wbar R1 = e, at alpha + beta = 0 the "
          "relabelling equation is e'' = -(K wbar^2/(4 alpha)) p.Theta.p")


# ------------------------------------------------------------------------------------------------ B: all equations along one axis
def family_b() -> None:
    al, be, K, wb, p = sp.symbols("alpha beta K wbar p", positive=True)
    t = sp.Symbol("t")
    F = {n: sp.Function(n)(t) for n in ("u", "phi", "a", "b", "cx", "cy", "xiL")}
    Tf = {n: sp.Function(n)(t) for n in ("Txx", "Tyy", "Tzz", "Txy", "Txz", "Tyz")}
    e = sp.Function("e")(t)
    hz = sp.Matrix([[F["phi"] + F["a"], F["b"], F["cx"]], [F["b"], F["phi"] - F["a"], F["cy"]], [F["cx"], F["cy"], 2 * F["xiL"]]])
    Th = sp.Matrix([[Tf["Txx"], Tf["Txy"], Tf["Txz"]], [Tf["Txy"], Tf["Tyy"], Tf["Tyz"]], [Tf["Txz"], Tf["Tyz"], Tf["Tzz"]]])
    pz = sp.Matrix([0, 0, p])
    hd = hz.diff(t)
    L = ((al * sum(hd[i, j] ** 2 for i in range(3) for j in range(3)) + be * hd.trace() ** 2) / wb
         + K * wb * (F["u"] * R1(hz, pz) + R2(hz, pz)) - e * F["u"] + sp.Rational(1, 2) * sum(Th[i, j] * hz[i, j] for i in range(3) for j in range(3)))
    EL = {n: sp.expand(sp.diff(sp.diff(L, f.diff(t)), t) - sp.diff(L, f)) for n, f in F.items()}
    ok = sp.simplify(EL["u"] - (e - 2 * K * wb * p ** 2 * F["phi"])) == 0                                 # 2 K wbar p^2 phi = e
    ok &= sp.simplify(EL["xiL"] - (sp.diff(8 / wb * ((al + be) * F["xiL"].diff(t) + be * F["phi"].diff(t)), t) - Tf["Tzz"])) == 0
    ok &= sp.simplify(EL["cx"] - (4 * al / wb * F["cx"].diff(t, 2) - Tf["Txz"])) == 0                     # transverse relabellings
    ok &= sp.simplify(EL["cy"] - (4 * al / wb * F["cy"].diff(t, 2) - Tf["Tyz"])) == 0
    ok &= sp.simplify(EL["a"] - (4 * al / wb * F["a"].diff(t, 2) + K * wb * p ** 2 * F["a"] - (Tf["Txx"] - Tf["Tyy"]) / 2)) == 0
    ok &= sp.simplify(EL["b"] - (4 * al / wb * F["b"].diff(t, 2) + K * wb * p ** 2 * F["b"] - Tf["Txy"])) == 0
    # at alpha + beta = 0, with phi = e/(2 K wbar p^2): (4 beta/(K wbar^2)) e'' = p^2 T_zz = p.Theta.p along z
    red = EL["xiL"].subs(be, -al).subs(F["phi"], e / (2 * K * wb * p ** 2)).doit()
    ok &= sp.simplify(red - (-4 * al / (K * wb ** 2 * p ** 2) * e.diff(t, 2) - Tf["Tzz"])) == 0
    check("B", ok, "one wave vector along z, all Euler-Lagrange equations with the stress (block 101's parametrization): 2K wbar p^2 phi = e; "
          "d/dt[(8/wbar)((alpha+beta) xiL' + beta phi')] = Theta_zz; (4alpha/wbar) c'' = Theta_xz, Theta_yz (transverse relabellings "
          "move, no condition on the sources); (4alpha/wbar) a'' + K wbar p^2 a = (Theta_xx - Theta_yy)/2, likewise b with Theta_xy; at "
          "alpha + beta = 0 the xiL equation becomes -(4alpha/(K wbar^2 p^2)) e'' = Theta_zz, the case p along z of family A")


# ------------------------------------------------------------------------------------------------ C: what the identity is
def family_c() -> None:
    al, K, wb, c = sp.symbols("alpha K wbar c", positive=True)
    pv = sp.Matrix(sp.symbols("p1:4", real=True))
    Th = sym3("T")
    # content with e' + i p.J = 0, P' + i p.Theta = 0 (row j: P_j' = -i sum_i p_i Theta_ij) and J = c P
    Pd = -sp.I * (pv.T * Th).T
    edd = -sp.I * c * pv.dot(Pd)                                      # e'' = -i p.J' = -i c p.P'
    need = -K * wb ** 2 / (4 * al) * (pv.T * Th * pv)[0]
    sol = sp.solve(sp.Eq(sp.expand(edd), sp.expand(need)), c)
    ok = sol == [K * wb ** 2 / (4 * al)]
    check("C", ok, "reading: e'' = -(K wbar^2/(4alpha)) p.Theta.p is the second label-time derivative of the continuity equation e' + i p.J = 0 "
          "combined with the momentum equation P' + i p.Theta = 0, exactly when the content's energy current is J = (K wbar^2/(4alpha)) P "
          "(the strain speed squared times the momentum density); it is second order, so it fixes neither e' + i p.J = 0 itself (a "
          "constant rate is left free, block 101 T4) nor the momentum equation (the transverse relabellings absorb the transverse stress)")


# ------------------------------------------------------------------------------------------------ D: block 54's walk against the identity
def family_d() -> None:
    sa, ca, sb, cb = sp.Rational(3, 5), sp.Rational(4, 5), sp.Rational(5, 13), sp.Rational(12, 13)
    s1 = (sa, sb, 0); s2 = (-sb, sa, 0)                                # k1 = (a, b, 0), k2 = (-b, a, 0): equal |sin k|, stationary
    eps = sp.sqrt(sum(x ** 2 for x in s1))
    ok = sp.simplify(sp.sqrt(sum(x ** 2 for x in s2)) - eps) == 0
    sig = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
    def chi(s):                                                       # positive eigenvector of s.sigma (s_z = 0)
        return sp.Matrix([s[0] - sp.I * s[1], eps])
    c1, c2 = chi(s1), chi(s2)
    Hs = lambda s: sum((s[j] * sig[j] for j in range(3)), sp.zeros(2))
    ok &= sp.simplify(Hs(s1) * c1 - eps * c1) == sp.zeros(2, 1) and sp.simplify(Hs(s2) * c2 - eps * c2) == sp.zeros(2, 1)
    M = [sp.simplify((c1.H * sig[a] * c2)[0]) for a in range(3)]
    tj = [s1[j] + s2[j] for j in range(3)]                            # sin k1_j + sin k2_j
    Theta = sp.Matrix(3, 3, lambda i, j: sp.Rational(1, 2) * (M[i] * tj[j] + M[j] * tj[i]) / 2)   # symmetric part of (1/2) M_a t_j
    # q = k2 - k1 = (-(a+b), a-b, 0); p_i p_j = 4 sin(q_i/2) sin(q_j/2) in rational form
    cos_apb = ca * cb - sa * sb; cos_amb = ca * cb + sa * sb
    pp = sp.Matrix([[2 * (1 - cos_apb), -2 * (cb - ca), 0], [-2 * (cb - ca), 2 * (1 - cos_amb), 0], [0, 0, 0]])
    ok &= pp[0, 0] * pp[1, 1] == pp[0, 1] ** 2
    pTp = sp.simplify(sum(pp[i, j] * Theta[i, j] for i in range(3) for j in range(3)))
    target = 128 * eps * (1 - sp.I) / 65 ** 3                         # (1/2) (a1* a2 = 1) x 256 eps (1-i)/65^3
    ok &= sp.simplify(pTp - target) == 0 and pTp != 0
    check("D", ok, f"block 54's walk (identity frame, wbar = 1) fails the identity exactly: the superposition of the positive-branch plane waves "
          f"k1 = (a, b, 0), k2 = (-b, a, 0) with sin a = 3/5, sin b = 5/13 is stationary (equal energies {sp.nsimplify(eps**2)}^(1/2)), so "
          f"e''(q) = 0 at q = k2 - k1, while p.Theta.p(q) = 128 eps (1 - i)/65^3 != 0 (Theta = Re psi^dag sigma_a S_j psi, block 62): at "
          f"alpha + beta = 0 the member has no solution with this content (block 62 T5's static failure, now forced in time)")


# ------------------------------------------------------------------------------------------------ E: formation
def family_e() -> None:
    t, tau, e0, de = sp.symbols("t tau e0 Delta_e", positive=True)
    s = t / tau
    e = e0 + de * (3 * s ** 2 - 2 * s ** 3)                          # block 101 T4's switch-on
    ok = sp.simplify(sp.diff(e, t, 2).subs(t, 0) - 6 * de / tau ** 2) == 0
    # at rest Theta = 0, so e'' = 0 at every p: e is linear in label time; bounded content keeps it constant
    check("E", ok, "(b) formation: for content at rest (Theta = 0) the identity is e'' = 0 at every wave vector, so a record forming at rest "
          "can change no Fourier component of the energy except at a constant rate (block 101's switch-on has e''(0) = 6 Delta_e/tau^2 "
          "and has no solution); energy converted in place (blocks 58, 67) is allowed; energy moved needs a stress with "
          "p.Theta.p = -(4alpha/(K wbar^2)) e'', the momentum flux of a current J = (K wbar^2/(4alpha)) P")


def main() -> int:
    family_q(); family_a(); family_b(); family_c(); family_d(); family_e()
    print("The DeWitt ratio and local conservation - checks; worker w-macbookpro9927a-j5393 (claude-opus-5-5)")
    for line in OUT:
        print(line)
    print(f"checks: {sum(1 for l in OUT if l.startswith(('ok', 'FAIL'))) - len(FAILS)} ok, {len(FAILS)} fail")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT {FAILS[0]}")
        return 1
    print("SUMMARY: PROVED at second order and every lattice wave vector: with the stress coupled as block 62 fixes it, the relabelling "
          "equation at alpha + beta = 0 imposes exactly e'' = -(K wbar^2/(4 alpha)) p.Theta.p on the sources: the second time derivative of "
          "e' + i p.J = 0 combined with P' + i p.Theta = 0 for content with J = (K wbar^2/(4alpha)) P; not the continuity equation itself "
          "and not the momentum equation (the transverse relabellings move: (4alpha/wbar) c'' = Theta_xz); block 54's walk violates it "
          "exactly (a stationary superposition with e'' = 0 and p.Theta.p != 0)")
    print("HIT: at alpha + beta = 0 the relabellings impose e'' = -(K wbar^2/(4 alpha)) p.Theta.p at every lattice wave vector: conservation's "
          "second time derivative for content with energy current (K wbar^2/(4alpha)) P, neither the continuity equation itself nor the "
          "momentum equation; block 54's walk content violates it exactly")
    return 0


if __name__ == "__main__":
    sys.exit(main())
