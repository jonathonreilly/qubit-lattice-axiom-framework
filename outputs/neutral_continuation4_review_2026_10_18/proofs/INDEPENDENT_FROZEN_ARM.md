<!-- Owning original: PR9753; source SHA256 8db5f41b076ed435c080daf759f952e101bd6812ca806a5f02d83bf12e08bbb9. -->
**Source boundary:** Complete mathematical source follows. Original review dispositions, execution stories, provisional questions and PASS labels are historical annotations, not current certification. Later explicit addenda supersede earlier provisional statements. Mathematical hypotheses and conclusions are retained; terminal exclusion interpretations require separate admission and are not promoted by this source enclosure.

# Fixed-order frozen-arm elimination check

Checked 2026-10-18 against `/private/tmp/neutral_frozen_arm_root.md`. The low-order classification and conditional fixed-order elimination are sound. The finite-rank assertion needs the momentum-fiber clarification below.

## All-length low orders

Let the two columns be non-nearest neighbors with common interval ell>=3. A single transverse operation cannot move their common endpoint, move an entire column, or change the pair while staying in the four-wall/even-plane sector. Thus K1 vanishes on F and between F and R.

For the second-order diagonal, there are four affected longitudinal layers per column: the layers just inside and outside each of its two walls. Each layer has four transverse edges incident on that column. Since the columns are not nearest neighbors, these 32 edge operations are distinct. Their excitation cost is 4 rather than the vacuum cost8 (Jz units): toggling the wall-end spin costs zero, and the other column's isolated flip costs4. Each gives a vacuum-subtracted contribution -1/4+1/8=-1/8. All other repeated-edge contributions equal their vacuum values. Therefore K2 diagonal=-4 for every such pair and every ell>=3, not just ell4.

A same-pair endpoint displacement by one layer requires a two-edge transverse path connecting the columns. At axial distance two the two same-color steps add, producing the retained slow arms. At diagonal separation (1,1), each two-step path has one X and one Y edge, with equal cost4 denominators in the two orders; their Pauli products anticommute at the shared intermediate site and cancel. Greater Manhattan distance needs at least three edges. No two-step process can move a whole column of length>=3; nor can it remove enough interval layers to enter ell1/2 from these F pairs. This establishes K2_F=-4I and K2_FR=0 in the prescribed homological convention.

Calling K2 'unique' should mean the specified zero-block homological inverse convention, or an explicitly aligned gauge. An arbitrary extra block-diagonal first-order gauge rotation can alter off-diagonal K2 entries; no unrestricted gauge uniqueness is needed here.

## Positive potential plus bounded remainder

At fixed order, connected finite support confines all interior diagonal dependence to a coefficient affine in ell. Offdiagonal transitions are endpoint moves for long intervals; changes of the column pair require ell bounded by the order/support size. All hop ranges and row degrees are uniformly bounded. Short intervals permit motion of a whole column even at arbitrarily large transverse separation, but that moves r only by a bounded amount and still has uniformly bounded degree. It does not invalidate the bounded operator remainder.

Only finitely many relative-position patterns are within a fixed interaction diameter. At larger r the local contributions split into separate column contributions, so affine slope and endpoint constants are uniformly bounded in r. The direct plaquette result gives six changed plaquettes for a diagonal pair, hence slope3/32; other F pairs change eight, hence1/8. Higher fixed-order coefficients change these by O_m(lambda), uniformly. Thus the slope remains positive for sufficiently small positive lambda (at fixed m>=4).

Subtracting the full affine diagonal leaves a bounded B_F=O_m(Jz lambda^3). Symmetry and uniform row-degree/amplitude bounds give an operator bound, rather than a bound on each entry alone. The resulting self-adjoint closed-channel operator is a positive unbounded diagonal potential plus a bounded perturbation, with the natural potential domain. Discarding the positive potential yields

    H_F/Jz >= 8-4lambda^2-C_m lambda^3.

The proposed slow energy has real part8-6lambda^2+O(lambda^(10/3)), so its distance from this spectrum is at least c Jz lambda^2. This lower spectral bound controls the ordinary resolvent even when the energy has a small negative imaginary part; no outgoing continuation in the closed F channel is needed.

## Cross-channel support and rank

F-to-R transitions which change the column pair require a bounded ell, and the finite transverse support restricts r to a bounded neighborhood of the retained adjacent/axial-two separations. Transitions which keep the pair but shorten into ell1/2 must flip endpoint sites on BOTH columns; a connected local term can do that only when r is bounded by its diameter. Hence both r and ell are bounded on cross-channel matrix entries at fixed order.

However, this is genuinely finite-dimensional support only after fixing all center-of-mass momenta, including transverse momentum. The draft says longitudinal COM q0, while describing states solely by r already suppresses the transverse COM coordinate. Please state a full translation fiber (in particular total momentum zero). With only longitudinal momentum fixed, there remain infinitely many transverse translates: the coupling is finite-channel and fiberwise finite-rank, not finite-rank on the entire unfibered space. The norm bounds can still be uniform over those translates/fibers.

In a fixed full momentum fiber, H_RF is finite-rank O_m(Jz lambda^3). Therefore

    Delta_R=H_RF(E-H_F)^-1 H_FR = O_m(Jz lambda^4),
    ||partial_E Delta_R||=O_m(lambda^2).

The correction is analytic throughout the slow-energy neighborhood separated by the gap. Its range lies in the fixed finite set of R boundary/host channels even though the F resolvent itself spreads through infinitely many closed states.

## Consumer limitation

In slow units the correction is O(lambda^2) at finitely many boundary channels. In an independently controlled regular-host Airy problem, boundary weight O(f)=O(lambda^2) then gives a physical pole displacement O(Jz lambda^6). This estimate requires retained-host matching/resolvent stability; the Schur norm bound alone does not ensure it. In particular it cannot be used to assume away a retained-host threshold or pole.

Conclusion: the argument removes these extra frozen long separations as resonant open channels at the slow edge within the fixed-order E8 model, with the explicit full-momentum-fiber qualification. It does not bound actual transitions to other N sectors, the untruncated microscopic remainder, or a full-H resonance.
