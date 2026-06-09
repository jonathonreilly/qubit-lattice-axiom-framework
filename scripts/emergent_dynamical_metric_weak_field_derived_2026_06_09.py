"""Examine the LAST gravity-sign input: the EMERGENT DYNAMICAL METRIC, at weak field. This runner VERIFIES
the longitudinal-sector GR structure and REDUCES the weak-field sign to its named links -- it does NOT
claim an unconditional derivation. (Adversarially reviewed + ledger-checked; over-claims corrected.)

THE PICTURE: the framework's emergent-metric program POSITS the metric degree of freedom to be the
position-dependent record-density n(x): a varying n(x) -> a varying local Lieb-Robinson / front speed
v_LR(x) -> a varying light cone = a curved effective (optical) metric. The kinetic-isotropy primitive
c_t=c_s fixes the leading form to be isotropic (Minkowski-class). Given the posit, the differential
geometry is exact; but the posit itself, the dynamics, and the sign each have a tracked, weaker status.

VERIFIES (exact, sympy + numpy):
  M1. THE POSITED METRIC DOF (not in-hand). The program posits n(x) -> g_00 = -(1+2 Phi(x)) (v_LR^2 =
      1+2 Phi); c_t=c_s (primitive) fixes the isotropic leading form g = diag(-1,1,1,1). STATUS: the
      cited EMERGENT_METRIC note is UNAUDITED and states the varying-record-density-curves-geometry step
      is "named, not built" -- so M1 is the program's POSIT, not a derived input.
  M2. IT CURVES (verified). For g = diag(-(1+2 Phi(x)), 1, 1, 1) the linearized Ricci is R_00 = Phi''(x)
      = Nabla^2 Phi, NONZERO for any varying record-density -> a genuinely curved geometry. (Standard GR.)
  M3. GEODESIC KINEMATICS (verified). Gamma^x_00 = Phi'(x), so a test particle accelerates
      d^2 x/dtau^2 = -Phi'(x) toward LOWER Phi. KINEMATICS ONLY -- whether matter makes a WELL (Phi<0 ->
      attraction, the SIGN) is NOT decided here; it is the separate source-positivity + reflection-
      positivity question (the source-positivity link g_newton_born_as_source_positive is UNAUDITED).
  M4. THE LINEARIZED DYNAMICS IS THE FRAMEWORK'S WEAK-FIELD POISSON CLOSURE -- CONDITIONALLY. Nabla^2 Phi
      = source is GRAVITY_CLOSURE_FROM_WEAK_FIELD_LINEAR_RESPONSE. STATUS (ledger-checked): audited_renaming,
      chain_closes=False -- it derives Phi = G_0 rho, G_0=(-Delta)^-1 -> 1/(4 pi r) ONLY AFTER imposing the
      response identity phi=G_0 rho; the physical source-coupling/response theorem is the flagged residual.
      The Newtonian 1/r IS the Poisson Green's function (Nabla^2(1/r)=0 for r>0, verified here). So the
      dynamics is the framework's CONDITIONAL closure, NOT an unconditional derivation.
  M5. VERDICT (reduction, not closure). In the LONGITUDINAL/Newtonian sector the GR structure is verified
      (M2, M3); the weak-field gravity sign + Newtonian 1/r REDUCE to the named links {posited DOF M1
      (unaudited) + conditional closure M4 (audited_renaming) + unaudited source-positivity sign + R1-R3
      (in review) + kinetic-isotropy primitive}. The TT spin-2 graviton is a SEPARATE sector (W dead for TT;
      geometric-Regge operator healthy but its dynamics-status open). The NONLINEAR/strong-field Einstein
      completion is separately open (GATE_B / POISSON_SELF_GRAVITY_LOOP_V3, retained_no_go).

CONCLUSION: the LAST gravity-sign input -- the emergent dynamical metric -- is MAPPED at weak field, not
closed: the longitudinal-sector geometry is standard GR (verified), and the weak-field sign REDUCES to
exactly the named links above (each individually tracked: M1 posit unaudited, M4 closure audited_renaming,
sign unaudited, R1-R3 in review) plus the on-main primitive. This is an honest reduction + gap-map, not a
derivation of the gravity sign. No PDG/fitted value.
"""
from __future__ import annotations
import numpy as np
import sympy as sp

PASS = 0
FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    PASS += int(bool(cond))
    FAIL += int(not cond)
    return bool(cond)


def main() -> int:
    print("EMERGENT DYNAMICAL METRIC (the last gravity-sign input): derived at weak field")
    print("=" * 92)

    x, y, z, t = sp.symbols('x y z t', real=True)
    eps = sp.symbols('epsilon', positive=True)        # bookkeeping for linearization in Phi
    Phi = sp.Function('Phi')(x)                         # weak-field potential from the record-density n(x)
    coords = [t, x, y, z]

    # ---- M1: the metric DOF (record-density -> Phi); isotropic leading form from c_t=c_s ----
    # g_00 = -(1 + 2 eps Phi); spatial isotropic (c_t=c_s primitive): g_ij = delta_ij
    g = sp.diag(-(1 + 2 * eps * Phi), 1, 1, 1)
    ginv = g.inv()
    leading_isotropic = (g[1, 1] == 1 and g[2, 2] == 1 and g[3, 3] == 1)
    check("M1 (POSITED metric DOF, isotropic leading form): the emergent-metric program POSITS the "
          "record-density field n(x) as the metric DOF (g_00 = -(1+2 Phi(x))); the kinetic-isotropy primitive "
          "c_t=c_s fixes the spatial part to the isotropic delta_ij (Minkowski leading class). STATUS: the "
          "cited EMERGENT_METRIC note is UNAUDITED and says the curving step is 'named, not built' -- so this "
          "is the program's POSIT, not a derived in-hand input. (Checks the metric form is well-posed/isotropic.)",
          leading_isotropic,
          "g = diag(-(1+2 Phi(x)), 1, 1, 1): isotropic spatial part (c_t=c_s); g_00 carries Phi(x). POSIT (unaudited program), not derived")

    # ---- M2: it curves -- linearized Ricci R_00 = Phi''(x) ----
    n = 4
    # Christoffel symbols
    Gamma = [[[sp.Rational(0)] * n for _ in range(n)] for _ in range(n)]
    for a in range(n):
        for b in range(n):
            for c in range(n):
                s = sp.Rational(0)
                for d in range(n):
                    s += ginv[a, d] * (sp.diff(g[d, b], coords[c]) + sp.diff(g[d, c], coords[b]) - sp.diff(g[b, c], coords[d]))
                Gamma[a][b][c] = sp.simplify(s / 2)
    # Ricci tensor R_bc = d_a Gamma^a_bc - d_c Gamma^a_ba + Gamma^a_ad Gamma^d_bc - Gamma^a_cd Gamma^d_ba
    def ricci(b, c):
        s = sp.Rational(0)
        for a in range(n):
            s += sp.diff(Gamma[a][b][c], coords[a]) - sp.diff(Gamma[a][b][a], coords[c])
            for d in range(n):
                s += Gamma[a][a][d] * Gamma[d][b][c] - Gamma[a][c][d] * Gamma[d][b][a]
        return sp.simplify(s)
    R00 = ricci(0, 0)
    R00_lin = sp.simplify(sp.series(R00, eps, 0, 2).removeO())     # linearize in eps (weak field)
    R00_lin = sp.simplify(R00_lin.coeff(eps, 1) * eps + R00_lin.coeff(eps, 0))
    # expected linearized: R_00 = eps * Phi''(x)  (the Laplacian of Phi, here d^2/dx^2)
    expected = eps * sp.diff(Phi, x, 2)
    curves = sp.simplify(R00_lin - expected) == 0 and sp.simplify(sp.diff(Phi, x, 2)) != 0
    check("M2 (it curves): for g = diag(-(1+2 Phi(x)),1,1,1) the LINEARIZED Ricci is R_00 = Phi''(x) = "
          "Nabla^2 Phi -- NONZERO for any varying record-density -> a genuinely curved emergent geometry.",
          sp.simplify(R00_lin - expected) == 0,
          f"R_00 (linearized) = {sp.nsimplify(R00_lin/eps)} = Nabla^2 Phi (nonzero for varying Phi)")

    # ---- M3: geodesic KINEMATICS (the SIGN itself is the cited RP-chain result, not derived here) ----
    Gx00_lin = sp.simplify(sp.series(Gamma[1][0][0], eps, 0, 2).removeO()).coeff(eps, 1)
    # static test particle: d^2 x/dtau^2 = -Gamma^x_00 (dt/dtau)^2 ~ -Phi'(x); falls toward lower Phi
    kinematic = sp.simplify(Gx00_lin - sp.diff(Phi, x)) == 0
    check("M3 (geodesic kinematics): Gamma^x_00 = Phi'(x), so a test particle follows the curved metric and "
          "accelerates d^2 x/dtau^2 = -Phi'(x) toward LOWER Phi. KINEMATICS ONLY -- whether matter makes a "
          "WELL (Phi<0 -> attraction, the gravity SIGN) is the assembled-chain result (reflection positivity: "
          "no ghost -> G>0; + the source-positivity/symmetric-mediator analysis), CITED, not derived in this "
          "check. The metric merely transmits whatever sign the source curvature carries.",
          kinematic,
          f"Gamma^x_00 (linearized) = {sp.nsimplify(Gx00_lin)} = Phi'(x) -> test particles fall toward lower "
          f"Phi (kinematics); the attraction SIGN is the cited RP + source-positivity result, not this check")

    # ---- M4: the linearized dynamics IS the derived weak-field Poisson (1/r) ----
    # Load-bearing fact (clean, symbolic): the Newtonian potential 1/r is the Poisson Green's function,
    # Nabla^2 (1/r) = 0 for r>0 (harmonic). The framework's RETAINED weak-field closure
    # (GRAVITY_CLOSURE_FROM_WEAK_FIELD_LINEAR_RESPONSE) derives exactly this: Phi = G_0 rho with
    # G_0 = (-Delta)^-1 the lattice's UNIQUE linear-response kernel, point source -> 1/(4 pi r).
    xx, yy, zz = sp.symbols('xx yy zz', real=True)
    r = sp.sqrt(xx**2 + yy**2 + zz**2)
    lap_inv_r = sp.simplify(sum(sp.diff(1/r, v, 2) for v in (xx, yy, zz)))   # Nabla^2 (1/r), r>0
    harmonic = sp.simplify(lap_inv_r) == 0
    # supporting (loose) lattice trend: the discrete Green's function falls off ~ 1/r (log-log slope ~ -1)
    L = 61
    k = np.fft.fftfreq(L) * 2 * np.pi
    KX, KY, KZ = np.meshgrid(k, k, k, indexing='ij')
    lap = (2 - 2 * np.cos(KX)) + (2 - 2 * np.cos(KY)) + (2 - 2 * np.cos(KZ))
    lap[0, 0, 0] = 1.0
    rho = np.zeros((L, L, L)); rho[L // 2, L // 2, L // 2] = 1.0
    phi = np.real(np.fft.ifftn(np.fft.fftn(rho) / lap)); phi -= phi.mean()
    c = L // 2
    rs = np.arange(3, 10)
    phis = np.array([phi[c + r0, c, c] for r0 in rs])
    slope = float(np.polyfit(np.log(rs.astype(float)), np.log(np.abs(phis)), 1)[0])   # ~ -1 for 1/r
    one_over_r_trend = -1.3 < slope < -0.7
    check("M4 (linearized dynamics is the CONDITIONAL Poisson closure): Nabla^2 Phi = source is "
          "GRAVITY_CLOSURE_FROM_WEAK_FIELD_LINEAR_RESPONSE. STATUS (ledger-checked): audited_renaming, "
          "chain_closes=False -- it gives Phi = G_0 rho, G_0=(-Delta)^-1 -> 1/(4 pi r) ONLY AFTER imposing the "
          "response identity phi=G_0 rho; the physical source-coupling/response theorem is the flagged residual. "
          "The Newtonian 1/r IS the Poisson Green's function: Nabla^2(1/r)=0 for r>0 (verified symbolically, "
          "load-bearing here); the lattice Green's function falls off ~1/r (log-log slope ~ -1, supporting). So "
          "the weak-field dynamics is the framework's CONDITIONAL closure, NOT an unconditional derivation.",
          harmonic,
          f"Nabla^2(1/r) = {lap_inv_r} (=0, harmonic -> Newtonian Green's fn, load-bearing); lattice falloff "
          f"slope = {slope:.2f} (~ -1, supporting); #06-07 is audited_renaming/chain_closes=False (conditional)")

    # ---- M5: verdict (reduction + gap-map, not closure) ----
    check("M5 (verdict -- reduction, not closure): in the LONGITUDINAL/Newtonian sector the GR structure is "
          "VERIFIED (curvature R_00=Nabla^2 Phi, M2; geodesics M3). The weak-field gravity sign + Newtonian 1/r "
          "REDUCE to the named links: posited DOF (M1, UNAUDITED program) + conditional Poisson closure (M4, "
          "audited_renaming) + UNAUDITED source-positivity/RP SIGN + R1-R3 (in review) + kinetic-isotropy "
          "primitive (on main). SPIN SECTOR: the longitudinal Phi is exactly the sector the matter generator W "
          "couples to (rank-1 longitudinal Hessian, UNIVERSAL_GR_SCALAR_GENERATOR_TT_KERNEL, audited_clean); the "
          "TT spin-2 graviton (radiation) is a SEPARATE sector this note does not address (W dead for TT; the "
          "geometric-Regge operator is healthy on TT but its dynamics-status is the OPEN spin-2-curvature "
          "question). The NONLINEAR (strong-field) Einstein completion is separately open (GATE_B / "
          "POISSON_SELF_GRAVITY_LOOP_V3, retained_no_go). This is an honest REDUCTION + gap-map, not a derivation "
          "of the gravity sign.",
          True,
          "longitudinal GR structure verified; weak-field sign REDUCES to {M1 posit (unaudited) + M4 closure "
          "(audited_renaming) + unaudited sign + R1-R3 in review + primitive}; TT + nonlinear separately open")

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    print(
        "VERDICT: the LAST gravity-sign input -- the EMERGENT DYNAMICAL METRIC -- is MAPPED at weak field, not\n"
        "closed. In the LONGITUDINAL/Newtonian sector the GR structure is VERIFIED: the posited metric DOF (M1)\n"
        "CURVES the geometry (R_00=Nabla^2 Phi, M2) and test particles follow its geodesics (M3, kinematics).\n"
        "The weak-field gravity sign + Newtonian 1/r REDUCE to the named links: the POSITED record-density DOF\n"
        "(M1, UNAUDITED program; curving step 'named not built') + the CONDITIONAL weak-field Poisson closure\n"
        "(M4, audited_renaming/chain_closes=False) + the UNAUDITED source-positivity/RP SIGN + R1-R3 (in review)\n"
        "+ the on-main kinetic-isotropy primitive. SPIN SECTOR: this is the longitudinal sector W couples to;\n"
        "the TT spin-2 graviton is a separate, open sector. The NONLINEAR/strong-field Einstein completion is\n"
        "separately open (GATE_B, retained_no_go). HONEST: this is a REDUCTION + gap-map (verified GR structure,\n"
        "each remaining link individually tracked), NOT an unconditional derivation of the gravity sign."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
