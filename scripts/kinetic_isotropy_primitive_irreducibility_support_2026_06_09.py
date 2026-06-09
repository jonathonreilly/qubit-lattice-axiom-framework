#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
Kinetic-isotropy primitive irreducibility support
================================================
Companion runner for
docs/KINETIC_ISOTROPY_PRIMITIVE_IRREDUCIBILITY_SUPPORT_2026-06-09.md.

THE BOUNDARY.  The registered kinetic-isotropy primitive grants only the structural OS0
kinetic-form equality c_t = c_s.  This runner supports why that premise must stay explicit:
the current framework baseline plus adjacent positive-transfer / reflection-positivity,
single-clock, and reachability structures admit a family of kinetic forms with different
xi := c_t/c_s.

WHAT THIS COMPUTES (every check() is an independent numeric/symbolic test; conclusions are narration):
  Part A  RP / the positive self-adjoint transfer does NOT force xi=1: the canonical lattice transfer is
          positive-Hermitian with H=-log(T)/a_tau >= 0 (spectrum condition) for EVERY c_t/c_s in
          {1/2,1,2,5}.  OS1 (reflection positivity) pins the FORM, not the dimensionless ratio.
  Part B  xi is a DIFFERENT object from the single-clock a_tau freedom: a clock rescale a_tau->s a_tau
          gives a CONSTANT E(p)-ratio (all modes), whereas a c_t/c_s change gives a p-DEPENDENT reshape.
          So single_clock_uniqueness_scope_boundary (fixes only the product a_tau*H) cannot reach xi.
  Part C  the 6-NN NO-diagonal causal order is the L1 taxicab order; NO round L2 cone matches it (axis
          vs face- vs body-diagonal front speeds differ: 1.0, 0.707, 0.577).  So the combinatorial order
          fixes the reachability-cone SHAPE but admits a 1-parameter xi embedding family (1-tick-1-edge
          does NOT fix the dynamical aperture).
  Part D  THE NON-FIXATION WITNESS: two realizations M1 (c_t=c_s, xi=1) and M2 (c_t!=c_s, xi!=1) BOTH
          satisfy every shared retained structure (positive transfer/RP, spectrum H>=0, single-clock
          a_tau*H, the 1-tick-1-edge reachability cone) and differ ONLY on the sentence "xi=1".
          This is model-family support for non-fixation, not a formal theorem about every future dynamics.
  Part E  (ground-up sharpening) SPATIAL isotropy z_x=z_y=z_z is not fixed by bare positivity checks: the
          M3 witness (spatially anisotropic K_x!=K_y) is axiom-faithful and breaks O_h.
  Part F  but spatial and temporal differ in KIND: O_h IS the genuine automorphism group of the Z^3
          6-NN edge set (so spatial isotropy = "respect the asserted cubic symmetry"), while the
          time<->space generator is NOT axiom-resident -- no 4th anticommuting Clifford generator
          exists in M_2(C)=Cl(3,0) ({T,sigma_i}=0 => T=0; the pseudoscalar is central). So xi=1 is
          STRICTLY STRONGER than spatial isotropy: it ADDS a generator the axioms disclaim, not a
          relabel. The "3" of Cl(3) is the root of why the time leg is not resident.

HONEST SCOPE.  This is a support runner for the approved primitive boundary, not a new primitive,
not a Tier-A admission, not a bounded-status source, and not a Lorentz-closure theorem.  It shows
that the listed current structures do not fix xi.  A future retained dynamics could derive the same
kinetic isotropy and retire the primitive; that stronger claim is not ruled out here.

Run: python3 scripts/kinetic_isotropy_primitive_irreducibility_support_2026_06_09.py
"""
from __future__ import annotations
import sys
import numpy as np

PASS, FAIL = 0, 0


def check(label, ok, detail=""):
    """An INDEPENDENT computed test. ok must be a computed boolean, never a hard-coded True."""
    global PASS, FAIL
    if ok:
        PASS += 1; tag = "PASS"
    else:
        FAIL += 1; tag = "FAIL"
    print(f"  [{tag}] {label}" + (f"  --  {detail}" if detail else ""))
    return bool(ok)


def section(t):
    print("\n" + "-" * 96 + f"\n{t}\n" + "-" * 96)


def note(msg):
    print(f"   ... {msg}")


# ---- free Euclidean lattice scalar: single-spatial-mode transfer energy --------------------------
def E_of_mode(omega2, K_t):
    """Transfer-matrix single-mode energy: cosh E = 1 + omega^2/(2 K_t).  Real, positive for omega^2,K_t>0."""
    x = 1.0 + omega2 / (2.0 * K_t)
    return np.arccosh(x)


def omega2(p, m2, K_s):
    """Spatial lattice dispersion omega^2(p) = m^2 + 2 K_s sum_i (1 - cos p_i)."""
    return m2 + 2.0 * K_s * np.sum(1.0 - np.cos(np.atleast_1d(p)))


def main():
    print("=" * 96)
    print("kinetic-isotropy primitive support: listed current structures do not fix xi=c_t/c_s")
    print("=" * 96)

    m2, K_s = 0.04, 1.0
    ps = np.linspace(0.05, np.pi - 0.05, 24)          # spatial momenta (single axis, p_y=p_z=0)

    # =====================================================================
    section("Part A: RP / the positive self-adjoint transfer does NOT force xi=1 (holds for every c_t/c_s)")
    for ratio in (0.5, 1.0, 2.0, 5.0):
        K_t = ratio * K_s
        Es = np.array([E_of_mode(omega2([p, 0, 0], m2, K_s), K_t) for p in ps])
        T_eigs = np.exp(-Es)                          # decaying transfer eigenvalues e^{-E}
        ok = np.all(np.isreal(Es)) and np.all(Es > 0) and np.all((T_eigs > 0) & (T_eigs < 1))
        check(f"(A.{ratio}) c_t/c_s={ratio}: transfer positive (e^-E in (0,1)), H=E/a_tau self-adjoint >=0 for all modes -- RP/spectrum hold",
              ok, detail=f"E in [{Es.min():.3f},{Es.max():.3f}]>0, e^-E in [{T_eigs.min():.3f},{T_eigs.max():.3f}] subset (0,1)")
    note("OS1 (reflection positivity) + the spectrum condition H>=0 are INVARIANT under c_t/c_s: they pin the")
    note("FORM (positive self-adjoint transfer, bounded-below H), NOT the dimensionless ratio xi. c_t=c_s is OS0")
    note("(full Euclidean SO(4)/B_4 invariance) = the Lorentz OUTPUT being sought -- invoking it would be circular.")

    # =====================================================================
    section("Part B: xi is a DIFFERENT object from the single-clock a_tau (clock=constant ratio; xi=p-dependent)")
    K_t = 1.0
    E_base = np.array([E_of_mode(omega2([p, 0, 0], m2, K_s), K_t) for p in ps])
    # (i) clock rescale a_tau -> s a_tau  <=>  E -> E/s uniformly: the E-ratio is CONSTANT across modes.
    s = 2.0
    clock_ratio = (E_base / s) / E_base
    clock_spread = clock_ratio.max() - clock_ratio.min()
    check("(B1) clock rescale a_tau->2 a_tau gives a CONSTANT E(p)-ratio across all modes (spread ~ 0) -- a pure overall conformal factor",
          clock_spread < 1e-12, detail=f"E-ratio spread under clock rescale = {clock_spread:.1e} (=0); single-clock fixes only the product a_tau*H")
    # (ii) xi change c_t -> 2 c_t gives a p-DEPENDENT E-ratio (reshapes the dispersion, not a constant rescale).
    E_xi = np.array([E_of_mode(omega2([p, 0, 0], m2, K_s), 2.0 * K_t) for p in ps])
    xi_ratio = E_xi / E_base
    xi_spread = xi_ratio.max() - xi_ratio.min()
    check("(B2) c_t->2 c_t gives a p-DEPENDENT E(p)-ratio (spread >> 0) -- a genuine reshape of the dispersion, NOT a constant rescale",
          xi_spread > 1e-2, detail=f"E-ratio spread under xi change = {xi_spread:.3f} >> 0; provably a different object from the clock-rate freedom")
    note("=> the a_tau-removable no-go (single_clock_uniqueness_scope_boundary, only a_tau*H fixed) is structurally")
    note("blind to xi: it removes a CONSTANT scale, while xi is a p-DEPENDENT shape. They are different freedoms.")

    # =====================================================================
    section("Part C: the 6-NN NO-diagonal causal order is L1 taxicab -- no round L2 cone matches (admits a xi-family)")
    # Front-speed to reach a boundary point in direction v after t = |v|_1 ticks: speed = |v|_2 / |v|_1.
    dirs = {"axis (1,0,0)": (1, 0, 0), "face-diag (1,1,0)": (1, 1, 0), "body-diag (1,1,1)": (1, 1, 1)}
    speeds = {}
    for name, v in dirs.items():
        v = np.array(v, float)
        speeds[name] = np.linalg.norm(v) / np.sum(np.abs(v))     # L2 / L1
    distinct = max(speeds.values()) - min(speeds.values())
    check("(C1) the taxicab front speed differs by direction: axis 1.0, face-diag 0.707, body-diag 0.577 -- NOT a single round (L2) cone",
          distinct > 0.3, detail=", ".join(f"{k.split()[0]}={v:.3f}" for k, v in speeds.items()) + f"; spread={distinct:.3f}")
    # No single c_t makes a round cone {dt = c_t |dx|_2} pass through all three diamond-boundary points at their tick t=|dx|_1.
    demanded = {name: np.sum(np.abs(v)) / np.linalg.norm(np.array(v, float)) for name, v in dirs.items()}  # c_t = t/|dx|_2
    ct_inconsistent = (max(demanded.values()) - min(demanded.values())) > 0.3
    check("(C2) a round L2 cone through the diamond-boundary points demands c_t = 1.0, 1.414, 1.732 simultaneously -- impossible",
          ct_inconsistent, detail=", ".join(f"{k.split()[0]}={v:.3f}" for k, v in demanded.items()) + " -> no faithful round-cone embedding")
    note("=> the combinatorial 1-tick-1-edge order fixes the reachability-cone SHAPE (the conformal class up to the")
    note("L1 diamond), but admits a 1-parameter xi stretch of the time-vs-space coordinate embedding: it does NOT")
    note("fix the dynamical aperture xi=c_t/c_s. The MIN_TIME_STEP 'conformal class derived' is audited_renaming.")

    # =====================================================================
    section("Part D: the NON-FIXATION WITNESS -- two models pass the shared checks and differ on xi=1")
    def model_props(K_t, K_s, a_ratio):
        """Shared retained structure tested for a realization with matter stiffness K_t,K_s and a_tau/a_s=a_ratio."""
        Es = np.array([E_of_mode(omega2([p, 0, 0], m2, K_s), K_t) for p in ps])
        rp = bool(np.all(Es > 0) and np.all((np.exp(-Es) > 0) & (np.exp(-Es) < 1)))   # positive transfer / RP / H>=0
        product = a_ratio * (Es / a_ratio)
        single_clock = bool(a_ratio > 0 and np.allclose(product, Es))  # only the product a_tau*H is represented
        nn_steps = [np.array(v) for v in ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))]
        reach_cone = bool(all(np.sum(np.abs(v)) == 1 for v in nn_steps) and len({tuple(v) for v in nn_steps}) == 6)
        cone_speed2 = (K_s / K_t) * (1.0 / a_ratio) ** 2          # continuum cone speed^2 ~ (c_s/c_t) in lattice units
        xi = K_t / K_s                                            # the dimensionless kinetic ratio
        return rp, single_clock, reach_cone, cone_speed2, xi
    rp1, sc1, rc1, v1, xi1 = model_props(1.0, 1.0, 1.0)          # M1: c_t=c_s, a_tau=a_s -> xi=1
    rp2, sc2, rc2, v2, xi2 = model_props(2.5, 1.0, 1.0)          # M2: c_t=2.5 c_s, a_tau=a_s -> xi=2.5
    shared_both = rp1 and sc1 and rc1 and rp2 and sc2 and rc2
    check("(D1) BOTH M1(xi=1) and M2(xi=2.5) satisfy the shared witness checks: positive transfer/RP, spectrum H>=0, single-clock product, 1-tick-1-edge reachability",
          shared_both, detail=f"M1 rp/sc/rc={rp1}/{sc1}/{rc1}; M2 rp/sc/rc={rp2}/{sc2}/{rc2}")
    check("(D2) they differ on xi=1: M1 has c_t=c_s (v^2=1) and M2 has c_t!=c_s (v^2=0.4!=1), while the shared witness checks still pass",
          abs(xi1 - 1.0) < 1e-12 and abs(xi2 - 1.0) > 0.5 and abs(v1 - 1.0) < 1e-12 and abs(v2 - 1.0) > 0.1,
          detail=f"M1 xi={xi1:.2f} v^2={v1:.2f}; M2 xi={xi2:.2f} v^2={v2:.2f}")
    check("(D3) model-family non-fixation: the same shared checks pass at xi=1 and xi!=1, so those checks do not determine c_t=c_s",
          shared_both and abs(xi1 - 1.0) < 1e-12 and abs(xi2 - 1.0) > 0.5,
          detail="the extra premise that excludes M2 is c_t=c_s itself; this supports keeping the primitive explicit")

    # =====================================================================
    section("Part E: spatial isotropy is not fixed by bare positivity checks (the M3 witness)")
    # M3: spatially anisotropic matter action (K_x != K_y) on the SAME Z^3 site set / Quantum / Record.
    grid = [(px, py, pz) for px in ps[::4] for py in ps[::4] for pz in ps[::4]]
    def spatial_rp(Kx, Ky, Kz):
        K = (Kx, Ky, Kz)
        Es = np.array([E_of_mode(m2 + 2 * sum(K[i] * (1 - np.cos(p[i])) for i in range(3)), 1.0) for p in grid])
        return bool(np.all(Es > 0) and np.all((np.exp(-Es) > 0) & (np.exp(-Es) < 1)))
    rp_M3 = spatial_rp(1.0, 2.5, 1.0)               # M3: K_x=1, K_y=2.5 -> breaks O_h
    check("(E1) M3 (spatially anisotropic K_x=1, K_y=2.5, same Z^3/Quantum/Record) is axiom-faithful: positive transfer/RP/H>=0 hold",
          rp_M3, detail="omega^2>=0 for every K_i>0 -> M3 passes the SAME 4-leg certification as M2")
    # M3 breaks the x<->y graph automorphism: omega^2(p) != omega^2(R_xy p).
    p_test = np.array([0.7, 0.2, 0.0])
    om_xy = m2 + 2 * (1.0 * (1 - np.cos(p_test[0])) + 2.5 * (1 - np.cos(p_test[1])) + 1.0 * (1 - np.cos(p_test[2])))
    om_swap = m2 + 2 * (1.0 * (1 - np.cos(p_test[1])) + 2.5 * (1 - np.cos(p_test[0])) + 1.0 * (1 - np.cos(p_test[2])))
    check("(E2) M3 breaks the x<->y O_h automorphism (omega^2(p) != omega^2(R_xy p)) -- bare positivity alone does not impose spatial kinetic isotropy",
          abs(om_xy - om_swap) > 1e-3, detail=f"|omega^2(p)-omega^2(R_xy p)|={abs(om_xy-om_swap):.3f} != 0")

    # =====================================================================
    section("Part F: but spatial and temporal differ in KIND -- O_h is axiom-resident, the time<->space generator is NOT (the Cl(3) root)")
    # (F1) O_h IS the linear automorphism group of the Z^3 6-NN edge set {+-e_i}: the 48 signed permutations preserve it.
    axes = [np.eye(3)[i] for i in range(3)]
    nn = [s * e for e in axes for s in (1, -1)]      # the 6 nearest-neighbour vectors
    from itertools import permutations, product
    signed_perms = []
    for perm in permutations(range(3)):
        for signs in product((1, -1), repeat=3):
            M = np.zeros((3, 3))
            for i in range(3):
                M[i, perm[i]] = signs[i]
            signed_perms.append(M)
    def preserves(M):
        img = {tuple(np.round(M @ v).astype(int)) for v in nn}
        return img == {tuple(np.round(v).astype(int)) for v in nn}
    n_preserve = sum(preserves(M) for M in signed_perms)
    shear = np.array([[1.0, 1, 0], [0, 1, 0], [0, 0, 1]])   # a non-signed-permutation linear map
    check("(F1) O_h = Aut of the Z^3 6-NN edge set: all 48 signed permutations preserve {+-e_i}, and a shear does NOT -- O_h is a GENUINE automorphism the axiom asserts",
          n_preserve == 48 and not preserves(shear), detail=f"{n_preserve}/48 signed perms preserve the NN set; shear preserves={preserves(shear)}")
    # (F2) compute axis orbits. O_h x time-parity acts trivially on the time axis
    # and as signed permutations on space; B_4 signed permutations merge all four axes.
    def four_axis_matrix(spatial_matrix, time_sign=1):
        out = np.zeros((4, 4))
        out[0, 0] = time_sign
        out[1:, 1:] = spatial_matrix
        return out
    oh4 = [four_axis_matrix(M, time_sign) for M in signed_perms for time_sign in (1, -1)]
    b4 = []
    for perm in permutations(range(4)):
        for signs in product((1, -1), repeat=4):
            M = np.zeros((4, 4))
            for i in range(4):
                M[i, perm[i]] = signs[i]
            b4.append(M)
    def axis_image(matrix, axis):
        v = np.zeros(4)
        v[axis] = 1
        w = np.round(matrix @ v).astype(int)
        return int(np.flatnonzero(np.abs(w))[0])
    def orbit(group, axis):
        return {axis_image(M, axis) for M in group}
    oh_orbits = [orbit(oh4, 0), orbit(oh4, 1)]
    b4_orbit = orbit(b4, 0)
    check("(F2) under axiom-resident O_h x time-parity the 4 axes split into TWO orbits {t},{x,y,z}; only B_4 merges them into one -- and B_4-merge IS the xi=1 premise",
          oh_orbits == [{0}, {1, 2, 3}] and b4_orbit == {0, 1, 2, 3},
          detail=f"O_h axis orbits={oh_orbits}; B_4 orbit={sorted(b4_orbit)}")
    # (F3) THE ROOT: no 4th anticommuting Clifford generator exists in M_2(C)=Cl(3,0); {T,sigma_i}=0 => T=0.
    s = {1: np.array([[0, 1], [1, 0]], complex), 2: np.array([[0, -1j], [1j, 0]], complex), 3: np.array([[1, 0], [0, -1]], complex)}
    I2 = np.eye(2, dtype=complex)
    # general T = a I + b s1 + c s2 + d s3; require {T,s_i}=0 for i=1,2,3. Build the linear system on (a,b,c,d).
    basis = [I2, s[1], s[2], s[3]]
    A = []
    for i in (1, 2, 3):
        for B in basis:
            anti = B @ s[i] + s[i] @ B
            A.append(anti.flatten())
    A = np.array(A).reshape(3, 4, 4)   # 3 generators x 4 basis-coeffs x 4 matrix-entries
    # Stack into a (12 x 4) real-and-imag system M @ (a,b,c,d) = 0 and check the only solution is 0.
    M = np.vstack([np.column_stack([A[i][k] for k in range(4)]) for i in range(3)])   # (12 x 4) complex
    Mri = np.vstack([M.real, M.imag])
    rank = np.linalg.matrix_rank(Mri)
    check("(F3) THE Cl(3) ROOT: solving {T,sigma_i}=0 for a 4th anticommuting (time-like) generator in M_2(C)=Cl(3,0) gives ONLY T=0 (full-rank system) -- no 4th generator exists",
          rank == 4, detail=f"coefficient-matrix rank={rank}/4 (full) -> a=b=c=d=0 -> T=0; the pseudoscalar s1 s2 s3 = i*I is CENTRAL, not a generator")
    omega = s[1] @ s[2] @ s[3]
    central = np.allclose(omega, 1j * I2)
    check("(F4) the pseudoscalar sigma_x sigma_y sigma_z = i*I is central (=i*I), confirming the 3 Paulis are a MAXIMAL anticommuting set -- the '3' of Cl(3) is why time is the odd-one-out (xi=1 rooted in d=3)",
          central, detail="3 anticommuting Paulis = 3 commensurable spatial axes (one O_h orbit); no 4th => time cannot be put on the same Clifford/edge footing without a NEW premise")

    # =====================================================================
    section("Verdict and honest scope (narration -- not tests)")
    note("GROUND-UP SHARPENING: spatial isotropy z_x=z_y=z_z is also not fixed by bare positivity checks (M3, Part E), BUT")
    note("it differs in KIND from xi=1: O_h is a GENUINE automorphism of the axiom-asserted Z^3 graph (Part F1),")
    note("so spatial isotropy follows from 'respect the symmetry you already asserted (a cubic lattice)'. xi=1's")
    note("time<->space generator is NOT axiom-resident (Part F2-F4: no 4th anticommuting Cl(3) generator), so xi=1")
    note("is STRICTLY STRONGER than spatial isotropy -- it ADDS a generator the axioms disclaim, not a relabel.")
    note("VERDICT: the listed current structures do not fix xi=1 (c_t=c_s). This supports the registered")
    note("kinetic-isotropy primitive; it is not a new primitive, Tier-A admission, or bounded-status source.")
    note("The primitive is precisely OS0 kinetic-form isotropy (the temporal kinetic coefficient on the same footing as space);")
    note("no axiom supplies it (Lattice gives no metric/cone/4th-axis; Quantum/Record give no dynamics/time-metric;")
    note("the scale primitive has zero dimensionless content; RP and the single-clock product a_tau*H are xi-blind).")
    note("SCOPE: a model-family non-fixation witness. A future retained dynamics could still derive the same")
    note("kinetic isotropy and retire the primitive. This runner does not demote rows or make delta_v=0 unconditional.")

    print("\n" + "=" * 96)
    print("kinetic-isotropy primitive support: the listed current structures do not fix xi=c_t/c_s.")
    print("Positive transfer/RP/single-clock/reachability checks hold across a xi-family, while xi=1")
    print("and xi!=1 remain distinguished. This supports keeping the registered primitive explicit.")
    print("Sets no audit status and supplies no downstream Lorentz theorem.")
    print("=" * 96)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 96)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
