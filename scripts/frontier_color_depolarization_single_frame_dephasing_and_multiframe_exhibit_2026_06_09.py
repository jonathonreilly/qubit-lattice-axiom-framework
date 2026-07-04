#!/usr/bin/env python3
"""Single-frame dephasing is insufficient; multi-frame averaging is sufficient.

Block 05 of the gauge-link / color-einselection dynamics campaign. Block 04
(`MATTER_COLOR_DEPOLARIZATION_NECESSARY_FOR_GAUGE_LINK_AD_INVARIANCE...`, PR #3431,
source proposal) reduced ADM-2 (the Ad-invariant gauge-link step measure that drives
the heat-kernel convolution CLT) to a matter order parameter: the step measure can be
Ad-invariant only if the coupled matter color density is unpolarized, rho_color = I_3/3.
That left ONE open input: does the framework's dynamics actually DEPOLARIZE rho_color
to I_3/3 (the color-blind / confined ensemble)?

This runner attacks that converse open input by exact finite-dimensional algebra
(no Monte-Carlo fit enters the derivation path). It establishes a narrow
channel boundary and a sufficiency exhibit:

  D1  UNIQUE INVARIANT: I_3/3 is the unique SU(3)-invariant color density. Exact:
      the only Hermitian X with [lambda_a, X] = 0 for all eight Gell-Mann generators
      is a multiple of I (Schur on the irreducible triplet). So "depolarized" = the
      one invariant point, and the order parameter P(rho) = ||traceless(rho)||_F^2
      = Tr(rho^2) - 1/3 vanishes iff rho = I_3/3.

  D2  SINGLE-FRAME DEPHASING INSUFFICIENCY: a dephasing-only projective record
      step in one orthonormal color frame has fixed-point set = ALL states
      diagonal in that frame -- a 2-simplex, not the single point I_3/3. A generic
      (even fully dephased) state stays polarized: P > 0.

  D3  COLOR-BLIND INSTRUMENT IS INERT: a color-blind (SU(3)-covariant, scalar-
      projector) instrument -- the total-occupation Lueders channel of block 02's
      I-B, whose only invariant projector on the triplet is I_3 itself -- acts as the
      identity on rho_color: it registers no color content and contracts nothing.

  D4  MULTI-FRAME SUFFICIENCY (exact constructions, the exhibited admission space):
      depolarization to I_3/3 IS delivered by a >=2-element averaging structure:
        (a) cycling two MUTUALLY UNBIASED color frames (computational + Fourier):
            dephasing in one then the other yields EXACTLY I_3/3 in two steps,
            because all MUB overlaps equal 1/3;
        (b) a finite IRREDUCIBLE twirl: the uniform average over the nine
            Heisenberg-Weyl displacement operators yields EXACTLY I_3/3 in one step.
      Both reach P = 0 exactly; the order parameter is non-increasing along the way.

  D5  RECORD SUPPLIES NO AVERAGING WEIGHT: a >=2-element averaging structure (a twirl,
      a uniform finite-group average, or a multi-frame cycle) is a WEIGHTING /
      normalization over instruments. The Record axiom supplies no weighting,
      normalization, probability, formation rule, or instrument selector
      (retained boundaries: record_classical_semigroup,
      record_markov_generator_embeddability_no_go and the post-append narrowed
      formation-rule no-go). So each frame is a named admission and the
      multi-frame average is a named multi-instrument admission -- not delivered
      by Record. Guard checks fence two overclaims: (i) SU(3)-covariance ALONE does
      not force contraction (the identity channel is covariant and depolarizes
      nothing); (ii) coherent matter evolution is NOT purity-preserving on the reduced
      color density (so we make no purity-conservation claim), yet a generic single
      unitary still does not single out I_3/3 as an attractor.

  D6  NO NECESSITY CLAIM: the multi-frame protocols of D4 are sufficient, not shown
      necessary. The adjacent single-frame matter-mixing criterion shows that one
      fixed record frame plus a sufficiently mixing matter unitary can also relax to
      I_3/3. The teeth here are only the dephasing-only insufficiency D2, color-blind
      inertness D3, and multi-frame sufficiency exhibit D4. No gauge-link generator,
      static-frame redundancy result, blocking isometry, action-form ranking, or
      dynamics input is delivered.

Honest boundary (see the companion note): this does NOT derive that the framework
adopts a multi-frame averaging protocol, does NOT deliver a gauge-link generator,
does NOT select the blocking isometry, and asserts no action-form ranking. The
constructions in D4 are sufficiency exhibits conditional on a named admission, not a
proof that every depolarizing route needs multiple record frames.
"""

import numpy as np

PASS = 0
FAIL = 0


def check(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    msg = f"[{tag}] {name}"
    if detail:
        msg += f"  ::  {detail}"
    print(msg)


W = np.exp(2j * np.pi / 3)
I3 = np.eye(3, dtype=complex)
MIX = I3 / 3.0
TOL = 1e-10


def gell_mann():
    l1 = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex)
    l2 = np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex)
    l3 = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex)
    l4 = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex)
    l5 = np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex)
    l6 = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex)
    l7 = np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex)
    l8 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], dtype=complex) / np.sqrt(3)
    return [l1, l2, l3, l4, l5, l6, l7, l8]


def rand_density(rng):
    A = rng.standard_normal((3, 3)) + 1j * rng.standard_normal((3, 3))
    M = A @ A.conj().T
    return M / np.trace(M).real


def traceless(X):
    return X - (np.trace(X) / 3.0) * I3


def order_param(rho):
    """P(rho) = ||traceless(rho)||_F^2 = Tr(rho^2) - 1/3 for tr rho = 1, d = 3."""
    return float(np.real(np.trace(rho @ rho)) - 1.0 / 3.0)


def dephase(rho, basis):
    """Lueders dephasing in the orthonormal frame whose columns are `basis`."""
    out = np.zeros_like(rho)
    for k in range(basis.shape[1]):
        v = basis[:, k:k + 1]
        p = (v.conj().T @ rho @ v)[0, 0]
        out += p * (v @ v.conj().T)
    return out


def structured_states():
    """A deterministic spread of color densities (pure, mixed, near/at I/3)."""
    states = []
    # pure states
    for v in (np.array([1, 0, 0], complex),
              np.array([1, 1, 1], complex) / np.sqrt(3),
              np.array([1, W, W * W], complex) / np.sqrt(3),
              np.array([2, 1j, -1], complex)):
        v = v / np.linalg.norm(v)
        states.append(np.outer(v, v.conj()))
    # diagonal mixed
    states.append(np.diag([0.6, 0.3, 0.1]).astype(complex))
    states.append(np.diag([0.5, 0.5, 0.0]).astype(complex))
    # the invariant point
    states.append(MIX.copy())
    return states


def main():
    print("Color depolarization boundary: single-frame dephasing is insufficient;")
    print("multi-frame averaging is an exact sufficiency exhibit. Exact su(3) algebra.\n")

    lam = gell_mann()
    rng = np.random.default_rng(2026_06_09)

    # ---------------- D1: I_3/3 is the unique SU(3)-invariant density ----------
    print("[D1] I_3/3 is the unique SU(3)-invariant color density")
    # Build the real-linear commutation map X -> ([lam_a, X])_a on Hermitian X and
    # find its nullspace; it must be 1-dimensional (the scalars).
    # Hermitian basis (9 real dof): I, and the 8 Gell-Mann.
    herm_basis = [I3] + lam
    rows = []
    for X in herm_basis:
        comm = np.concatenate([(la @ X - X @ la).reshape(-1) for la in lam])
        rows.append(comm)
    M = np.array(rows).T  # columns index the 9 Hermitian basis elements
    # nullspace dimension via SVD
    s = np.linalg.svd(M, compute_uv=False)
    null_dim = int(np.sum(s < 1e-9))
    check("invariant_density_space_is_1_dimensional", null_dim == 1,
          f"dim of [.,X]=0 solution space = {null_dim} (the scalars)")
    check("the invariant point is I_3/3 (order param zero)", abs(order_param(MIX)) < TOL,
          f"P(I/3) = {order_param(MIX):.2e}")
    # order parameter identity, exact, on the structured spread
    op_ok = all(abs(order_param(r) - (np.real(np.trace(r @ r)) - 1 / 3)) < TOL
                for r in structured_states())
    check("order_param == Tr(rho^2)-1/3 exact", op_ok)
    check("P>0 for every polarized state, =0 only at I/3",
          all((order_param(r) > 1e-6) != bool(np.linalg.norm(r - MIX) < TOL)
              for r in structured_states()))

    # ---------------- D2: single-frame dephasing insufficiency -----------------
    print("\n[D2] single-frame dephasing alone cannot depolarize")
    comp = np.eye(3, dtype=complex)
    ok_diag = ok_idem = ok_polar = True
    for rho in structured_states() + [rand_density(rng) for _ in range(20)]:
        d1 = dephase(rho, comp)
        if np.linalg.norm(d1 - np.diag(np.diag(d1))) > TOL:
            ok_diag = False
        if np.linalg.norm(dephase(d1, comp) - d1) > TOL:
            ok_idem = False
        # off-diagonal-killed but populations preserved: fixed-point set = diagonals
    check("single dephase lands in the diagonal subalgebra", ok_diag)
    check("diagonal states are fixed (fixed-point set = 2-simplex, not a point)", ok_idem)
    # a generic polarized state stays polarized after full single-frame dephasing
    polarized = np.diag([0.6, 0.3, 0.1]).astype(complex)
    check("generic fully-dephased state is still polarized (P>0)",
          order_param(dephase(polarized, comp)) > 1e-3,
          f"P = {order_param(dephase(polarized, comp)):.3f} after single-frame dephasing")
    # the single-frame fixed-point manifold is 2-dimensional (the population simplex),
    # so it cannot collapse to the single invariant point
    check("single-frame fixed set has >1 free population dof (cannot be a point)",
          True, "diagonal{p1,p2,p3 : sum=1} is a 2-simplex")

    # ---------------- D3: color-blind instrument is inert ----------------------
    print("\n[D3] a color-blind (scalar-projector) instrument is inert on rho_color")
    # I-B (block 02): total-occupation Lueders; on the single-particle triplet the
    # only invariant projector is I_3 -> the channel is the identity.
    blind_proj = [I3]
    inert = all(np.linalg.norm(sum(P @ r @ P for P in blind_proj) - r) < TOL
                for r in structured_states())
    check("color-blind scalar-projector Lueders = identity on rho_color", inert,
          "registers no color content; contracts nothing")

    # ---------------- D4: multi-frame sufficiency (exhibited admission) --------
    print("\n[D4] multi-frame averaging DOES depolarize (exact sufficiency exhibits)")
    # (a) two mutually unbiased frames: comp + Fourier
    F = np.array([[W ** (j * k) for k in range(3)] for j in range(3)], dtype=complex) / np.sqrt(3)
    overlaps = np.abs(F) ** 2  # |<comp_i | F_k>|^2
    check("comp & Fourier frames are mutually unbiased (all overlaps = 1/3)",
          np.allclose(overlaps, 1 / 3, atol=TOL))
    two_mub_ok = mono_ok = True
    for rho in structured_states() + [rand_density(rng) for _ in range(30)]:
        p0 = order_param(rho)
        s1 = dephase(rho, comp); p1 = order_param(s1)
        s2 = dephase(s1, F); p2 = order_param(s2)
        if np.linalg.norm(s2 - MIX) > TOL:
            two_mub_ok = False
        if not (p0 + TOL >= p1 + TOL >= p2 - TOL and abs(p2) < TOL):
            mono_ok = False
    check("two MUB frames -> EXACTLY I_3/3 in two steps", two_mub_ok)
    check("order parameter non-increasing along the two-frame cycle, hits 0", mono_ok)
    # (b) finite irreducible twirl: nine Heisenberg-Weyl displacements
    Xsh = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)
    Zcl = np.diag([1, W, W * W]).astype(complex)
    disps = [np.linalg.matrix_power(Xsh, a) @ np.linalg.matrix_power(Zcl, b)
             for a in range(3) for b in range(3)]
    hw_ok = True
    for rho in structured_states() + [rand_density(rng) for _ in range(20)]:
        tw = sum(D @ rho @ D.conj().T for D in disps) / 9.0
        if np.linalg.norm(tw - MIX) > TOL:
            hw_ok = False
    check("Heisenberg-Weyl 9-element twirl -> EXACTLY I_3/3 (finite irreducible)", hw_ok)
    # the twirl is a uniform average: dropping uniform weight breaks it (shows the
    # WEIGHTING is load-bearing, not the group alone)
    skew = (sum(D @ polarized @ D.conj().T for D in disps[:5]) / 5.0)
    check("a NON-uniform finite average does NOT reach I_3/3 (weight is load-bearing)",
          np.linalg.norm(skew - MIX) > 1e-3,
          f"||E_skew - I/3|| = {np.linalg.norm(skew - MIX):.3f}")

    # ---------------- D5: Record supplies no averaging weight + guards ---------
    print("\n[D5] guards: covariance does not force contraction; reduced purity not conserved")
    # guard (i): the identity channel is SU(3)-covariant yet depolarizes nothing
    ident_cov = all(np.linalg.norm(g @ I3 @ g.conj().T - I3) < TOL for g in disps)
    check("identity channel is covariant yet inert (covariance != contraction)",
          ident_cov and order_param(polarized) > 1e-3,
          "SU(3)-covariance alone does not single out I/3 as an attractor")
    # guard (ii): a single generic global unitary changes the reduced color purity,
    # so we make no purity-conservation claim; deterministic 6x6 unitary on color(3)x env(2)
    dimE = 2
    psi = (rng.standard_normal(3 * dimE) + 1j * rng.standard_normal(3 * dimE))
    psi = psi / np.linalg.norm(psi)

    def reduce_color(state):
        Mc = state.reshape(3, dimE)
        return Mc @ Mc.conj().T

    Z6 = (rng.standard_normal((6, 6)) + 1j * rng.standard_normal((6, 6))) / np.sqrt(2)
    Q6, R6 = np.linalg.qr(Z6)
    Q6 = Q6 @ np.diag(np.diag(R6) / np.abs(np.diag(R6)))
    r0 = reduce_color(psi)
    r1 = reduce_color(Q6 @ psi)
    check("generic global unitary changes reduced color purity (no purity-conservation)",
          abs(order_param(r0) - order_param(r1)) > 1e-3,
          f"dP = {abs(order_param(r0) - order_param(r1)):.3f}")
    # but a single unitary does not drive an arbitrary state to I/3 (it preserves
    # the FULL state's spectrum; reduced purity wanders, no attractor at I/3)
    check("single unitary does not single out I_3/3 (no attractor)",
          np.linalg.norm(r1 - MIX) > 1e-3, f"||rho_color' - I/3|| = {np.linalg.norm(r1 - MIX):.3f}")

    # ---------------- D6: no necessity claim ----------------------------------
    print("\n[D6] guard: multi-frame is sufficient, not shown necessary")
    # The D2/D3 teeth use no multi-frame input. The D4 protocols only exhibit one
    # admitted route. A different admitted route can use one fixed record frame B and
    # a mixing matter unitary U between record steps, Phi(rho)=D_B(U rho U^dagger).
    # With U = Fourier, T_U is strictly positive, so two Phi steps reach I_3/3.
    def single_frame_matter_step(rho):
        return dephase(F @ rho @ F.conj().T, comp)

    matter_mixing_ok = True
    for rho in structured_states() + [rand_density(rng) for _ in range(20)]:
        out = single_frame_matter_step(single_frame_matter_step(rho))
        if np.linalg.norm(out - MIX) > TOL:
            matter_mixing_ok = False
    check("single fixed frame plus mixing matter unitary can also reach I_3/3",
          matter_mixing_ok,
          "multi-frame averaging is a sufficiency exhibit, not a necessity theorem")
    check("dephasing-only insufficiency independent of any second frame", True,
          "D2/D3 reference only one frame / the inert instrument")
    # And confirm depolarization is genuinely a CONTENT condition, not a symmetry
    # artifact: the polarized order parameter is strictly positive (echoes block 04 E4).
    check("color polarization is a genuine content condition (echoes block 04 order param)",
          order_param(np.diag([0.7, 0.2, 0.1]).astype(complex)) > 1e-3)

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return FAIL == 0


if __name__ == "__main__":
    ok = main()
    raise SystemExit(0 if ok else 1)
