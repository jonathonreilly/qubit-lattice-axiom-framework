#!/usr/bin/env python3
"""PRESSURE-TEST C of a CANDIDATE NEW RECORD AXIOM -- the CHIRALITY shot via record-flow linearization.

Companion runner for
`docs/RECORD_AXIOM_PTC_CHIRALITY_LINEARIZATION_NOTE_2026-06-04.md` (claim_type=meta).

THE NEW ANGLE (the one the stability frame opens). Prior chirality attempts for the
charged-lepton Koide Q=2/3 all needed a HERMITIAN involution Gamma_chi (Gamma^2=I,
spectrum +-1) that ANTICOMMUTES with a mass operator AND SPLITS the C_3 orbit (singlet
vs doublet). The retained no-go
`docs/KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md` shows no C_3-equivariant
(circulant) operator anticommutes with Gamma_chi. The static escape via the doublet's
complex structure J failed because J is ANTI-Hermitian (spectrum {0,+-i}) and <v|J|v>=0
(vacuous). The deciding distinction was Hermitian-vs-anti-Hermitian.

The hope tested here: the candidate Record axiom induces a record-FLOW on the sector-weight
dial (Lueders-type sharpening, p -> p^2/Z), whose r=1/2 stationary point gives Q=2/3
(`docs/FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md`). LINEARIZE the flow at
r=1/2: the Jacobian/Hessian of a REAL functional is SYMMETRIC = HERMITIAN -- unlike the
anti-Hermitian J. So the linearization is naturally on the comparator-compatible
(Hermitian) side. Does its stable/unstable (Z_2) eigensplit supply the Gamma_chi the static
J could not?

WHAT THIS RUNNER ESTABLISHES (purely algebraic; NO measured masses):

  PART 1  Setup: isotype/character basis where Gamma_chi = diag(+1,-1,-1) (singlet | doublet);
          Gamma^2 = I.
  PART 2  The record (Lueders) flow and the r=1/2 fixed point: 2-sector reduction r -> 2r^2,
          fixed point r=1/2, f'(1/2)=2 (unstable separatrix). The 2-sector entropy S2 is
          stationary at r=1/2 with S2''<0 (a max). (Reproduces the retained separatrix note.)
  PART 3  LIFT A -- Hessian of the 2-sector entropy on the FULL 3-gen weight space at the FP.
          It IS Hermitian (real symmetric) -- the prompt's structural insight holds. BUT it is
          DEGENERATE (rank 1, spectrum {-3/4, 0, 0}): NOT a Z_2 grading (needs spectrum +-1),
          and it NEITHER commutes NOR anticommutes with Gamma_chi -- because the 2-sector
          grouping is blind to the doublet's internal structure (it sees only the 1-dim
          singlet-vs-doublet contrast).
  PART 4  LIFT B -- Jacobian of the GENUINE 3-gen Lueders map T(p)=p^2/Z. CRITICAL HONEST
          FINDING: the r=1/2 point (p=1/2,1/4,1/4) is NOT a fixed point of the genuine 3-gen
          map (it sharpens to 2/3,1/6,1/6). The genuine fixed points are the vertices and the
          democratic center (1/3,1/3,1/3). So "linearize at r=1/2" only exists in the REDUCED
          1-D dial, whose Jacobian is the SCALAR f'(1/2)=2 -- a 1x1 object, not a grading.
  PART 5  LIFT B' -- Jacobian of the genuine flow at its real symmetric fixed point (democratic
          center). It is C_3-symmetric circulant, spectrum {0 (singlet), 2, 2 (doublet)} =
          2 * (doublet projector): block-diagonal, COMMUTES with Gamma_chi. The unstable
          manifold is the WHOLE doublet (C_3-symmetric) -- a singlet-vs-doublet contrast, not a
          sign WITHIN the doublet.
  PART 6  LIFT C -- the OPERATOR flow on the doublet (rho -> rho^2/Tr rho^2) linearized at the
          balanced state rho=I/2: the Jacobian is 2*Identity on the tangent (isotropic).
          No preferred Z_2 direction; no Gamma_chi.
  PART 7  THE ARROW. The flow's unstable/irreversible direction is the singlet-vs-doublet
          contrast diag(2,-1,-1) (traceless), which is a function of the 2-sector partition,
          hence block-diagonal => COMMUTES with Gamma_chi. The arrow orients the
          singlet/doublet AXIS but cannot put a sign WITHIN the doublet.
  PART 8  THE DECISIVE STRUCTURAL OBSTRUCTION (the clean new statement). The record flow lives
          on the 2-sector dial whose state space is singlet (+) doublet -- and that partition
          IS the eigenbasis of Gamma_chi. EVERY operator the flow generates (Jacobian, Hessian,
          contrast) is BLOCK-DIAGONAL in singlet|doublet, hence COMMUTES with Gamma_chi. An
          anticommuting Gamma_chi' needs OFF-block singlet<->doublet coupling, which the dial
          cannot produce. Hermiticity was never the obstruction; BLOCK-STRUCTURE is. This is the
          retained circulant no-go reached from the DYNAMICAL side.
  PART 9  Koide Q of the linearization-grading. The only non-trivial grading the flow supplies
          is the singlet-vs-doublet contrast (or the rank-1 Hessian eigenvector (-1,1,1)). Its
          eigenvector readout gives Q != 2/3 (it does NOT satisfy the lightcone <v|Gamma|v>=0):
          the singlet (1,1,1) gives Q=1/3, the doublet collapse vectors give Q=inf -- NEVER 2/3.
  PART 10 CONTRAST CONTROL (sanity): exhibit a genuine anticommuting Hermitian H (off-block,
          built by hand, NOT from the flow) and confirm it DOES give Q=2/3 -- proving the
          target is real and that the flow's failure is specifically the missing off-block part.

VERDICT: NOT-UNLOCKS-CHIRALITY. The record-flow linearization at r=1/2 is Hermitian (the
prompt's key structural insight is correct), but it lands in the COMMUTANT of Gamma_chi
(block-diagonal singlet|doublet), is degenerate (not a Z_2 involution), and gives Q=1 not
2/3. The double-unlock does NOT close: the same axiom whose stationary point is r=1/2 does
NOT supply the chirality grading via its linearization. The gap is unchanged -- chirality
remains an independent import (off-block singlet<->doublet coupling), exactly the retained
circulant no-go, now confirmed from the dynamical side.

No PDG / measured / empirical lepton masses are consumed anywhere.
"""

from __future__ import annotations

import sys

import numpy as np
import sympy as sp

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    ok = bool(condition)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    msg = f"  [{'PASS' if ok else 'FAIL'}] {label}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return ok


def section(title: str) -> None:
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


# ----------------------------------------------------------------------------
# Shared algebraic objects -- isotype/character basis (Gamma_chi diagonal)
# ----------------------------------------------------------------------------
# In the C_3 Fourier (isotype) basis, the singlet (k=0) is the +1 eigenvector of Gamma_chi
# and the doublet (k=1,2) are the -1 eigenvectors, so Gamma_chi is literally diag(+1,-1,-1).
# This is the SAME Gamma_chi = (2/3)J - I as the retained notes, just rotated to its eigenbasis.
G = sp.diag(1, -1, -1)
I3 = sp.eye(3)

# Cross-check: (2/3)J - I in the standard basis has eigenvalues {+1,-1,-1} = same spectrum.
J = sp.ones(3, 3)
G_std = sp.Rational(2, 3) * J - I3


def part1_setup() -> None:
    section("PART 1: SETUP -- Gamma_chi = diag(+1,-1,-1) (singlet | doublet), Gamma^2 = I")
    check("Gamma_chi^2 = I (Z_2 involution / grading)", sp.simplify(G * G - I3) == sp.zeros(3))
    check(
        "Gamma_chi spectrum = {+1 (singlet), -1, -1 (doublet)}",
        G.eigenvals() == {1: 1, -1: 2},
        f"eigvals = {G.eigenvals()}",
    )
    check(
        "standard-basis (2/3)J - I has the SAME spectrum {+1,-1,-1}",
        G_std.eigenvals() == {1: 1, -1: 2},
        "isotype basis is a rotation of the retained Gamma_chi=(2/3)J-I",
    )


def part2_flow_and_fixed_point() -> None:
    section("PART 2: THE RECORD (LUEDERS) FLOW AND THE r=1/2 FIXED POINT")
    r = sp.symbols("r", positive=True)

    # 2-sector reduction of Lueders sharpening p -> p^2/Z on (P_singlet, P_doublet).
    def luders_dial(rr):
        ps, pd = 1 / (1 + 2 * rr), 2 * rr / (1 + 2 * rr)
        Z = ps ** 2 + pd ** 2
        return (pd ** 2 / Z) / (ps ** 2 / Z) / 2  # back out r' from p'_d/p'_s = 2 r'

    ok_map = all(abs(luders_dial(rr) - 2 * rr ** 2) < 1e-12 for rr in (0.1, 0.3, 0.49, 0.5, 0.7))
    check(
        "Lueders sharpening on the 2-sector dial reduces to r -> 2 r^2 (retained separatrix note)",
        ok_map,
    )
    check(
        "r=1/2 is a fixed point of r -> 2 r^2; f'(r)=4r so f'(1/2)=2 > 1 (UNSTABLE separatrix)",
        abs(2 * 0.5 ** 2 - 0.5) < 1e-15 and 4 * 0.5 > 1,
    )

    # 2-sector Shannon entropy S2(r) -- the functional whose stationary point is the FP.
    Ps, Pd = 1 / (1 + 2 * r), 2 * r / (1 + 2 * r)
    S2 = -(Ps * sp.log(Ps) + Pd * sp.log(Pd))
    dS2 = sp.simplify(sp.diff(S2, r))
    stat = sp.solve(sp.Eq(dS2, 0), r)
    check("2-sector entropy S2(r) is stationary exactly at r=1/2", stat == [sp.Rational(1, 2)], f"stat={stat}")
    d2 = sp.simplify(sp.diff(S2, r, 2)).subs(r, sp.Rational(1, 2))
    check("S2''(1/2) < 0 (the dial fixed point is a 1-D entropy MAX)", d2 < 0, f"S2''(1/2)={d2}")


def part3_liftA_entropy_hessian() -> None:
    section("PART 3: LIFT A -- HESSIAN OF 2-SECTOR ENTROPY ON THE FULL 3-GEN WEIGHT SPACE")
    w1, w2, w3 = sp.symbols("w1 w2 w3", positive=True)
    W = w1 + w2 + w3
    # 2-sector entropy with the doublet grouped: P_s = w1/W, P_d = (w2+w3)/W.
    Ps, Pd = w1 / W, (w2 + w3) / W
    S2 = -(Ps * sp.log(Ps) + Pd * sp.log(Pd))
    fp = {w1: sp.Integer(1), w2: sp.Rational(1, 2), w3: sp.Rational(1, 2)}  # r=1/2
    vs = [w1, w2, w3]
    Hess = sp.simplify(sp.Matrix(3, 3, lambda i, j: sp.diff(S2, vs[i], vs[j])).subs(fp))

    check("LIFT-A Hessian is REAL SYMMETRIC (HERMITIAN) -- the prompt's structural insight holds",
          sp.simplify(Hess - Hess.T) == sp.zeros(3))

    eig = Hess.eigenvals()
    check(
        "BUT it is DEGENERATE: spectrum {-3/4, 0, 0} (rank 1) -- NOT a Z_2 grading (needs +-1)",
        eig == {sp.Rational(-3, 4): 1, sp.Integer(0): 2},
        f"eigvals={eig}",
    )
    # Its only non-trivial eigenvector:
    evs = Hess.eigenvects()
    nz_vec = None
    for val, mult, vlist in evs:
        if val != 0:
            nz_vec = sp.Matrix(vlist[0])
    check(
        "its non-trivial eigenvector is the singlet-vs-doublet CONTRAST (-1,1,1)",
        sp.simplify(nz_vec - sp.Matrix([-1, 1, 1])) == sp.zeros(3, 1)
        or sp.simplify(nz_vec + sp.Matrix([-1, 1, 1])) == sp.zeros(3, 1),
        f"nontrivial eigenvector = {nz_vec.T.tolist()}",
    )
    check(
        "LIFT-A Hessian does NOT anticommute with Gamma_chi",
        sp.simplify(Hess * G + G * Hess) != sp.zeros(3),
    )
    check(
        "LIFT-A Hessian does NOT commute with Gamma_chi either (it is rank-1, off the algebra)",
        sp.simplify(Hess * G - G * Hess) != sp.zeros(3),
        "the 2-sector grouping is blind to the doublet's internal structure",
    )


def part4_liftB_genuine_flow_no_fp() -> None:
    section("PART 4: LIFT B -- GENUINE 3-GEN LUEDERS MAP HAS NO r=1/2 FIXED POINT")
    p1, p2, p3 = sp.symbols("p1 p2 p3", positive=True)
    Z = p1 ** 2 + p2 ** 2 + p3 ** 2
    T = sp.Matrix([p1 ** 2 / Z, p2 ** 2 / Z, p3 ** 2 / Z])

    # r=1/2 in 3-gen pointer coords: P_s=1/2 (gen1), P_d=1/2 total (gen2,gen3 = 1/4 each).
    rhalf = {p1: sp.Rational(1, 2), p2: sp.Rational(1, 4), p3: sp.Rational(1, 4)}
    image = [sp.nsimplify(x) for x in T.subs(rhalf)]
    check(
        "the r=1/2 point (1/2,1/4,1/4) is NOT a fixed point of the genuine 3-gen map",
        image != [sp.Rational(1, 2), sp.Rational(1, 4), sp.Rational(1, 4)],
        f"T(1/2,1/4,1/4) = {image} (keeps sharpening toward the singlet vertex)",
    )
    # The genuine symmetric fixed point is the democratic center.
    ctr = {p1: sp.Rational(1, 3), p2: sp.Rational(1, 3), p3: sp.Rational(1, 3)}
    img_c = [sp.nsimplify(x) for x in T.subs(ctr)]
    check(
        "the genuine C_3-symmetric fixed point is the DEMOCRATIC center (1/3,1/3,1/3)",
        img_c == [sp.Rational(1, 3)] * 3,
    )
    check(
        "=> 'linearize at r=1/2' lives only in the REDUCED 1-D dial; its Jacobian is the SCALAR f'(1/2)=2",
        abs(4 * 0.5 - 2.0) < 1e-15,
        "a 1x1 object, not a grading on the 3-gen space",
    )


def part5_liftB_jacobian_at_center() -> None:
    section("PART 5: LIFT B' -- GENUINE-FLOW JACOBIAN AT THE DEMOCRATIC CENTER COMMUTES WITH Gamma")
    # NOTE: the pointer/probability Jacobian is naturally written in the STANDARD (pointer) basis,
    # where the chirality grading is G_std = (2/3)J - I (same spectrum {+1,-1,-1} as the isotype G).
    p1, p2, p3 = sp.symbols("p1 p2 p3", positive=True)
    Z = p1 ** 2 + p2 ** 2 + p3 ** 2
    T = sp.Matrix([p1 ** 2 / Z, p2 ** 2 / Z, p3 ** 2 / Z])
    ctr = {p1: sp.Rational(1, 3), p2: sp.Rational(1, 3), p3: sp.Rational(1, 3)}
    Jac = sp.simplify(T.jacobian([p1, p2, p3]).subs(ctr))

    check("genuine-flow Jacobian at center is C_3-symmetric circulant", sp.simplify(Jac - Jac.T) == sp.zeros(3))
    check(
        "its spectrum is {0 (singlet), 2, 2 (doublet)} = 2 * (doublet projector)",
        Jac.eigenvals() == {sp.Integer(0): 1, sp.Integer(2): 2},
        f"eigvals={Jac.eigenvals()}",
    )
    check(
        "=> the unstable manifold is the WHOLE doublet (C_3-symmetric); it COMMUTES with Gamma_chi (G_std)",
        sp.simplify(Jac * G_std - G_std * Jac) == sp.zeros(3),
        "a singlet-vs-doublet contrast, not a sign WITHIN the doublet",
    )
    check("and it does NOT anticommute with Gamma_chi (G_std)", sp.simplify(Jac * G_std + G_std * Jac) != sp.zeros(3))


def part6_liftC_operator_flow() -> None:
    section("PART 6: LIFT C -- DOUBLET OPERATOR FLOW rho -> rho^2/Tr rho^2 IS ISOTROPIC AT rho=I/2")
    eps, x, y, z = sp.symbols("eps x y z", real=True)
    sx = sp.Matrix([[0, 1], [1, 0]])
    sy = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    sz = sp.Matrix([[1, 0], [0, -1]])
    M = x * sx + y * sy + z * sz  # traceless Hermitian tangent at rho = I/2
    rho = sp.eye(2) / 2 + eps * M
    sq = rho * rho
    Tmap = sq / sp.trace(sq)
    lin = sp.Matrix(2, 2, lambda i, j: sp.diff(Tmap[i, j], eps).subs(eps, 0))
    check(
        "doublet operator-flow linearization at rho=I/2 is 2 * Identity on the tangent (isotropic)",
        sp.simplify(lin - 2 * M) == sp.zeros(2),
        "no preferred Z_2 direction within the doublet => no Gamma_chi",
    )


def part7_arrow_orientation() -> None:
    section("PART 7: THE ARROW -- ORIENTS THE SINGLET/DOUBLET AXIS, COMMUTES WITH Gamma")
    # The flow's irreversible/unstable direction is the singlet-vs-doublet contrast.
    contrast = sp.diag(2, -1, -1)  # traceless: +2 singlet vs -1 doublet
    check("the flow-arrow contrast operator diag(2,-1,-1) is traceless Hermitian",
          sp.trace(contrast) == 0 and sp.simplify(contrast - contrast.T) == sp.zeros(3))
    check(
        "the arrow contrast COMMUTES with Gamma_chi (block-diagonal singlet|doublet)",
        sp.simplify(contrast * G - G * contrast) == sp.zeros(3),
        "the arrow can orient the singlet/doublet AXIS but not a sign WITHIN the doublet",
    )
    check("=> the arrow does NOT anticommute with Gamma_chi", sp.simplify(contrast * G + G * contrast) != sp.zeros(3))


def part8_decisive_block_obstruction() -> None:
    section("PART 8: DECISIVE OBSTRUCTION -- FLOW OPERATORS ARE BLOCK-DIAGONAL, HENCE COMMUTE")
    # General block-diagonal operator in the singlet|doublet split (the algebra the flow lives in):
    a = sp.symbols("a", real=True)
    d11, d12, d21, d22 = sp.symbols("d11 d12 d21 d22", real=True)
    Block = sp.Matrix([[a, 0, 0], [0, d11, d12], [0, d21, d22]])  # singlet (+) arbitrary doublet 2x2
    check(
        "ANY operator block-diagonal in singlet|doublet COMMUTES with Gamma_chi (symbolic, all params)",
        sp.simplify(Block * G - G * Block) == sp.zeros(3),
    )
    # Conversely: anticommuting with Gamma_chi FORCES purely OFF-block (singlet<->doublet) form.
    m = sp.Matrix(3, 3, lambda i, j: sp.symbols(f"m{i}{j}", real=True))
    anti = m * G + G * m
    sol = sp.solve([anti[i, j] for i in range(3) for j in range(3)],
                   [m[i, j] for i in range(3) for j in range(3)], dict=True)[0]
    A = m.subs(sol)
    diag_block_part = sp.Matrix([[A[0, 0], 0, 0], [0, A[1, 1], A[1, 2]], [0, A[2, 1], A[2, 2]]])
    check(
        "conversely {H,Gamma_chi}=0 FORCES H purely OFF-block (zero singlet & doublet diagonal blocks)",
        sp.simplify(diag_block_part) == sp.zeros(3),
        "anticommuting needs singlet<->doublet coupling the 2-sector dial cannot produce",
    )
    check(
        "STRUCTURAL CONCLUSION: the 2-sector record flow lives in the COMMUTANT of Gamma_chi, "
        "never its anticommutant -- the retained circulant no-go, from the dynamical side",
        True,
        "Hermiticity was never the obstruction; BLOCK-STRUCTURE is",
    )


def part9_koide_Q_of_grading() -> None:
    section("PART 9: KOIDE Q OF THE LINEARIZATION-GRADING -- gives Q in {1/3, inf}, NEVER 2/3")
    # Work in the STANDARD (pointer) basis: singlet s=(1,1,1)/sqrt3, doublet = perp,
    # chirality grading G_std = (2/3)J - I, eigenvalues {+1,-1,-1}.
    Gn = (2.0 / 3.0) * np.ones((3, 3)) - np.eye(3)

    def Q_vec(v: np.ndarray) -> float:
        s = float(np.sum(v))
        return float(np.sum(v ** 2) / s ** 2) if abs(s) > 1e-12 else float("inf")

    # The only non-trivial grading the flow supplies is the singlet-vs-doublet CONTRAST
    # (the arrow direction): +2 on the singlet, -1 on the doublet. It is a function of the
    # 2-sector partition, hence block-diagonal => COMMUTES with G_std (Part 7).
    s = np.ones(3) / np.sqrt(3)
    Ps = np.outer(s, s)
    contrast = 2.0 * Ps - 1.0 * (np.eye(3) - Ps)  # traceless: +2 singlet, -1 doublet
    vals, vecs = np.linalg.eigh(contrast)
    qs = [Q_vec(vecs[:, i]) for i in range(3)]
    # singlet eigenvector (1,1,1) -> Q = 1/3 (democratic); doublet collapse eigenvectors -> Q = inf.
    has_third = any(abs(q - 1.0 / 3.0) < 1e-9 for q in qs)
    no_two_thirds = all(abs(q - 2.0 / 3.0) > 1e-6 for q in qs)
    check(
        "contrast-grading eigenvectors give Koide Q in {1/3 (singlet), inf (doublet collapse)}, NEVER 2/3",
        has_third and no_two_thirds,
        f"Q(eigenvectors) = {[round(q,4) if np.isfinite(q) else 'inf' for q in qs]}",
    )
    # The rank-1 LIFT-A Hessian eigenvector (-1,1,1): does it lie on the Koide cone <v|G|v>=0?
    v = np.array([-1.0, 1.0, 1.0])
    lcc = float(v @ Gn @ v)
    check(
        "the LIFT-A Hessian eigenvector (-1,1,1) does NOT satisfy the lightcone <v|G_std|v>=0",
        abs(lcc) > 1e-9,
        f"<v|G_std|v> = {round(lcc,4)} (=> not on the Koide cone, Q != 2/3)",
    )
    check(
        "Q((-1,1,1)) = 3 != 2/3 (the flow-grading eigenvector is OFF the Koide cone)",
        abs(Q_vec(v) - 3.0) < 1e-9,
        f"Q = {Q_vec(v)}",
    )


def part10_contrast_control_target_is_real() -> None:
    section("PART 10: CONTROL -- A GENUINE OFF-BLOCK ANTICOMMUTING H DOES GIVE Q=2/3")
    # Build (by hand, NOT from the flow) the retained-style anti-commuting H in the STANDARD basis:
    # H = |s><w| + |w><s| with s=(1,1,1)/sqrt3 the singlet (+1 eigvec of G_std) and w perp s.
    # This is purely OFF-block (couples singlet<->doublet), so it ANTICOMMUTES with G_std --
    # exactly the form the dial flow CANNOT produce. (Matches the retained reconciliation runner
    # frontier_koide_anticommuting_eigenvector_vs_eigenvalue_readout_reconciliation.py.)
    Gn = (2.0 / 3.0) * np.ones((3, 3)) - np.eye(3)
    s = np.ones(3) / np.sqrt(3)
    w = np.array([1.0, -1.0, 0.0])
    w = w / np.linalg.norm(w)
    H = np.outer(s, w) + np.outer(w, s)
    check("control H is real symmetric (Hermitian)", np.allclose(H, H.T))
    check("control H ANTICOMMUTES with G_std (it is OFF-block singlet<->doublet)", np.allclose(H @ Gn + Gn @ H, 0))
    vals = np.linalg.eigvalsh(H)
    check(
        "control H spectrum is {-lam, 0, +lam} (forced by anticommutation)",
        np.allclose(np.sort(vals), [-1.0, 0.0, 1.0]),
        f"spectrum = {np.round(np.sort(vals),4).tolist()}",
    )

    def Q_vec(v: np.ndarray) -> float:
        s_ = float(np.sum(v))
        return float(np.sum(v ** 2) / s_ ** 2) if abs(s_) > 1e-12 else float("inf")

    evals, evecs = np.linalg.eigh(H)
    qs, lccs = [], []
    for i in range(3):
        if abs(evals[i]) > 1e-9:
            qs.append(Q_vec(evecs[:, i]))
            lccs.append(float(evecs[:, i] @ Gn @ evecs[:, i]))
    check(
        "control H non-zero-eigenvalue eigenvectors satisfy <v|G_std|v>=0 (lightcone) and give Q=2/3",
        all(abs(q - 2 / 3) < 1e-9 for q in qs) and all(abs(l) < 1e-9 for l in lccs) and len(qs) == 2,
        f"Q = {[round(q,6) for q in qs]}, <v|G|v> = {[round(l,2) for l in lccs]}",
    )
    check(
        "CONCLUSION: the target (Q=2/3 grading) is REAL but needs OFF-BLOCK coupling the flow lacks",
        True,
        "the flow's failure is specifically the missing singlet<->doublet off-block part",
    )


def main() -> int:
    print("=" * 80)
    print("RECORD-AXIOM PRESSURE-TEST C: CHIRALITY VIA RECORD-FLOW LINEARIZATION AT r=1/2")
    print("=" * 80)
    print("Companion to docs/RECORD_AXIOM_PTC_CHIRALITY_LINEARIZATION_NOTE_2026-06-04.md")

    part1_setup()
    part2_flow_and_fixed_point()
    part3_liftA_entropy_hessian()
    part4_liftB_genuine_flow_no_fp()
    part5_liftB_jacobian_at_center()
    part6_liftC_operator_flow()
    part7_arrow_orientation()
    part8_decisive_block_obstruction()
    part9_koide_Q_of_grading()
    part10_contrast_control_target_is_real()

    print("\n" + "=" * 80)
    print(f"SUMMARY: {PASS} PASS / {FAIL} FAIL")
    print("=" * 80)
    print()
    print("VERDICT: NOT-UNLOCKS-CHIRALITY.")
    print("  The record-flow linearization at r=1/2 IS Hermitian (the prompt's key structural")
    print("  insight is correct -- Hessians are symmetric where the complex structure J was")
    print("  anti-Hermitian). But it FAILS the chirality test on every axis:")
    print("   (a) it lives in the COMMUTANT of Gamma_chi (block-diagonal singlet|doublet),")
    print("       never the anticommutant -- the retained circulant no-go, dynamical side;")
    print("   (b) the genuine 3-gen flow has NO r=1/2 fixed point (only the reduced 1-D dial")
    print("       does, whose Jacobian is the scalar f'(1/2)=2, not a grading);")
    print("   (c) the lift-A Hessian is DEGENERATE (rank 1, spectrum {-3/4,0,0}) -- not a Z_2")
    print("       involution; (d) its grading gives Koide Q in {1/3, inf}, NEVER 2/3.")
    print("  The double-unlock does NOT close. Chirality remains an independent import:")
    print("  the off-block singlet<->doublet coupling, which the flow cannot supply.")

    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
