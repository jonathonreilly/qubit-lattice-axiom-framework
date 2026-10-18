# Independent coefficient tolerance for a common-product program cell

Claim type: bounded theorem.

The [common-product positive cell](COMMON_PRODUCT_PROGRAM_CELL_BOUNDED_THEOREM_NOTE_2026-10-18.md) admits a nonzero independent scalar-coefficient error box whenever its stated finite-horizon certificate has positive slack. This removes exact correlation of the actual coefficients within that box. Block shapes, occupation frames, legal program contents, absent interactions and literal input preparation remain supplied. The result is for one cell, not a robust chain or native physical law.

The [complete source](../outputs/common_product_program_2026_10_18/proofs/common_product_coefficient_tolerance__PROPOSAL.md) and [distinct analytical check](../outputs/common_product_program_2026_10_18/proofs/common_product_coefficient_tolerance_check__REVIEW.md) carry the full argument. No numerical operating point or scientific program is used.

## Independent errors and phase

Fix b>0, D1>D0>2b and a=2b²/D0. With the parent's full positive Q convention, install

    Htilde = Q_bL(u,m)+Q_bR(m,v)
           +cu(1-nu)+cv(1-nv)
           +(d0 P0_cm+d1 P1_cm)nm
           +au P0_cu nu+av P0_cv nv.

For 0<=e<1, allow ALL eight coefficients independently in

    bL,bR,cu,cv in b[1-e,1+e],
    dp in (Dp-2b)[1-e,1+e], p=0,1,
    au,av in a[1-e,1+e].

Every block remains positive. Program triples are legal000/111 and may be coherently superposed or entangled with endpoint inputs and arbitrary passive references. The literal injection J inserts a vacant mediator and the redundant program encoding. All four endpoint occupations and every physical output remain in the theorem.

On legal program p, the exact actual scalar is Ctilde=cu+cv. After subtracting it, the endpoint potentials are bL-cu+(1-p)au and bR-cv+(1-p)av; the mediator potential is bL+bR+dp; the two hopping coefficients are -bL and -bR. These are full qubit identities. Centering does not remove occupied-state or program-dependent errors.

Set Xh=(X_L X_R+Y_L Y_R)/2 on the logical endpoints, Rminus=(nL+nR-Xh)/2, Rplus=(nL+nR+Xh)/2 and Ac=P0 a Rminus. Rminus and Rplus both have double-occupation value1. Two distinct targets are retained:

    actual scalar: exp(-it Ctilde) J exp(-it Ac),
    fixed nominal scalar: exp(-i2bt) J exp(-it Ac).

There is no program-dependent or input-dependent fitted phase.

## Complete finite-time bound

Use the parent's nominal dressed isometry Jd only as a proof device. Define

    eps_off=4b²/(sqrt(D1²+8b²)+D1),
    r0=sqrt(2)b/D0, r1=sqrt(2)b/(D1+eps_off),
    alphap=(1+rp²)^(-1/2), betap=rp alphap,
    kappa=sqrt(2-2alpha0)<=r0,
    Bact=(6+sqrt(2))b+2a,
    Bfix=(8+sqrt(2))b+2a.

For every real t, the actual-scalar comparison has complete operator error at most

    min{2, 2kappa+|t|(eps_off+e Bact)}.                 (1)

The fixed-nominal-scalar comparison has complete operator error at most

    min{2, 2kappa+|t|(eps_off+e Bfix)}.                 (2)

Passive references preserve these norms; the corresponding unhalved channel-distance bound is at most twice the vector bound on this stated input domain. The common scalar is irrelevant to the isolated channel, but relative occupation/program phases are not. No ordering of the two exact vector errors is asserted: only their certified envelopes are ordered. Restricting all programs to enabled000 removes eps_off.

To verify the important detuning dependence, nm Jd_p has two orthogonal nonzero images: beta_p times the mediator one-head state and beta_p times the symmetric two-head state containing the mediator. Thus its full four-state norm is beta_p, and Dp beta_p<sqrt(2)b for either p. The actual centered perturbation has endpoint errors at most2eb+ea(1-p), mediator error at most eDp, and each hopping error at most eb. Acting on Jd costs at most4eb+2ea at endpoints, sqrt(2)eb at the mediator and2eb in hopping. Conserved program sectors combine by a maximum. Hence

    ||[(Htilde-Ctilde)-(H-2b)]Jd|| <= e Bact.

The nominal exact identity (H-2b)Jd=Jd(Ac-P1 eps_off Rplus) then bounds the full rectangular residual by eps_off+eBact. Duhamel and two replacements of Jd by J prove(1). Adding the scalar discrepancy2|sin[t(Ctilde-2b)/2]|<=2eb|t| proves(2). No perturbed eigenvector, invariant dressed code or actual spectral gap is presumed. This is why the perturbation coefficient is O(b) rather than the coarse full-space O(D1).

## A nonzero box, loads and sensitivity

For T>0 and0<eta<2, require the explicit nominal certificate slack

    mu=eta-2kappa-T eps_off>0.

Then

    e_star=min{1/2, mu/(2 T Bfix)}                     (3)

is positive. Every independent tuple with e<=e_star has fixed-scalar error at most eta-mu/2<eta throughout |t|<=T. The actual-scalar upper envelope is no greater. Lack of this slack means only that this certificate does not provide a nonzero box.

The two mediator projectors can be counted as one positive block with norm max(d0,d1). In this convention every actual incident sum is at most1+e times its nominal sum; the nominal maximum is D1+2b. Therefore the simultaneous condition D1+2b<=2Lambda/3 ensures actual loads<=Lambda for(3). There are six qubits, eight independent scalar coefficients and seven combined listed blocks. If the mediator projectors are implemented as two separately counted blocks, their incident norms add; the cap must be recomputed under that convention. Exact block shapes and geometry are unchanged.

At Tgate=pi/a, the perturbation term in(2) is

    pi e[(8+sqrt(2))D0/(2b)+2].                       (4)

For nominal slack proportional to eta, this is a sufficient relative tolerance of order eta b/D0; if b/D0 is itself proportional to eta, the sufficient box is of order eta². These are conditional sufficient scalings, not necessary hardware laws or optimized tolerances.

A concrete allowed direction explains why independent compensation errors still matter. Keep all coefficients nominal except cu=cv=b(1+e). The literal antisymmetric one-head state (|100>-|001>)/sqrt(2) remains an exact eigenvector with centered energy a(1-p)-eb. Its discrepancy from the actual-scalar target is exactly2|sin(ebt/2)|. Vacuum has no centered shift, so vacuum/antisymmetric coherence detects the relative error. A common rephasing cannot in general fix both columns. Special phase-return times are allowed; this is not an every-time failure or universal no-go claim.

## Evidence and retained obligations

Source final SHA256 `496cd963122ac22bdc3a66c475a83536a484a23e306d2a667596604973aff24c`; distinct check SHA256 `8c81728048223b2a20486f82671d8f152c284efbc48659d848fbeb7eaaeb31ab`. The original source8934d4f0 and review181a80d0 are preserved as history. ROOT requested a wording correction from apparent ordering of exact errors to ordering of certified envelopes; no equation or hypothesis changed. The exact parent source739e99c4 and check809a2083 are pinned in the packet and reused at their checked scope.

ROOT proposed the coefficient-error question and read the full source, review, exact correction and this synthesis. The source author authored the parent cell; the distinct checker checked that parent and shares its ancestry. ROOT's integration is not an additional independent mathematical check or retained audit. No scientific program, dynamics, solver, sweep or numerical point was run.

This theorem does not cover erroneous block directions, hopping phases, program flips, extra interactions, state preparation, network attachments or transfer to the old processor. Native Hamiltonian/Record supply, capture, reset and permanent finite halt remain open. Actual coefficient correlation is relaxed only within the explicit box; the nominal design and the other supplied premises remain necessary.
