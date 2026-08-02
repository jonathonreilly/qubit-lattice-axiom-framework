# A cotangent-lift bookkeeping extension of the executed Cycle-700 projected output, with auxiliary-momentum conservation, an explicit inverse, and a measured kernel — Cycle 704

Date: 2026-08-01
Claim type: bounded_theorem
Authority: none. Audit: unset. Constitutional effect: none. This cycle edits no axiom, foundation, Qualification, primitive, registry, policy, queue, audit-status, or PR-control surface. No new axiom or primitive is proposed or adopted.
No coupling value, sign, or scale is selected or derived in this cycle; every such object is named as supplied.
Runner: `scripts/physical_record_register_symplectic_dilation_cycle704_2026_08_01.py` — TOTAL: PASS=54 FAIL=0.

## 1. The wall

The Cycle-700 evidence-ceiling tally carries one cell that its own harness could not fill:

| exact reversibility with conservation, deletion, sign, scale, and range mutations | PARTIAL | C4–C4b; no Stinespring or unitary dilation of the open-system readout channel is constructed |

The first column lists what the Cycle-700 harness did establish about its numerical output: it reversed the field dynamics to tolerance, conserved its named quantities, and responded correctly to deletion, sign, scale, and range mutations of the supplied source. The second column says PARTIAL, and the third says why. The reversibility on offer was reversibility of the *dynamics*, run on a state from which the four-number output had already been extracted and omitted. This cycle supplies a larger real symplectic bookkeeping system for that deterministic projection and measures its kernel. It does **not** fill the quoted Cycle-700 cell: no Stinespring representation, framework-site unitary, or physical apparatus is constructed, so that cell remains PARTIAL.

## 2. The channel as executed

Cycle 700 integrates an affine-linear leapfrog on a scalar pair (phi, pi) over a cubic box in Z^3 of side L. Each step is a half kick, a drift, and a half kick, with a supplied frozen source rho entering through a supplied coupling scale. The source is switched on over n_ramp steps by the smooth profile g(step) = 4u^3 - 3u^4 with u = min(1, max(0, step/n_ramp)), and then held fixed for n_hold = 1000 further steps. During the hold the harness accumulates phi and divides by n_hold; the kept output is the value of that time average at four detector sites, and the published scalar is the ratio of two differences of those four values.

Named as supplied, not derived in this cycle: the source profile, the coupling scale, the ramp profile, the association of four particular sites with detectors, the hold window, and — the one easiest to walk past — the 1/n_hold normalization of the hold average. The Record axiom supplies an additive scalar readout over pairwise-disjoint framework-Record collections. It supplies no weighting and no normalization. The uniform weight over hold steps and the division by n_hold are a supplied convention of the Cycle-700 harness, carried through unchanged here and gated against it, never re-derived. Nothing in this construction identifies hold-step samples with framework Records.

At L = 9 the Cycle-700 field state has 2N = 1458 real components and the kept output has k = 4 numbers. The final field/momentum coordinates are omitted from that output. Here “projected output map” means only this deterministic many-to-one map; the phrase “open-system” is retained only inside the quoted Cycle-700 residual and is not promoted to a quantum channel or a derived physical mechanism.

The harness first gates the landed Cycle-700 anchors on this machine before constructing the auxiliary pair. The four hold-window ratios across the ramp ladder are byte-stable in the current environment, and the dynamical reversal returns the state to its zero initial data at the floating floor. The sparse static solves vary in their final round-off digits across numerical-library builds, so the current observed values and the fixed gate tolerances are carried in the transcript rather than restated as universal bytes here. Ten anchor gates pass before any new object exists.

## 3. The bookkeeping extension (bounded theorem statement)

Adjoin an auxiliary canonical accumulator pair. The augmented phase space is R^{2N} x R^{2k} with (phi, A) as positions and (pi, B) as momenta, carrying the standard symplectic form J on the m = N + k position/momentum split. Let P be the k x N detector projector. Add to each hold step the time-one flow of the auxiliary coupling Hamiltonian

    H_c = B . (P phi).

Its equations of motion are dphi/dt = 0, dB/dt = 0, dpi/dt = -P^T B, dA/dt = P phi. Since phi and B are both constant along that flow, the time-one map is exactly two assignments,

    pi[det] -= B          (auxiliary back-reaction)
    A       += phi[det]   (accumulation)

which read and write disjoint variables, so their order is immaterial and the pair is a single exact symplectic shear. This is the standard cotangent lift of the position shear A -> A + P phi. The theorem is the conjunction of five conditional mathematical claims, each carrying its own gate.

**(i) Non-disturbance is bit-for-bit on the chosen zero-B subspace.** On that subspace the back-reaction leg subtracts positive zero on the executed finite-valued trajectory, and the accumulator leg writes only into A. Running the full augmented integrator at the longest ramp beside the untouched Cycle-700 integrator, the final phi, the final pi and the whole hold average agree by array equality, not by tolerance. No premise selects B = 0 as “physical”; it is a supplied initial condition whose invariance follows because B is unchanged. Off that subspace the auxiliary coupling does perturb the original trajectory.

**(ii) A carries the executed numerical accumulator.** Dividing A by n_hold reproduces the hold average at the four detector sites to relative 0.0 — the two summation orders happen to agree bit for bit here, and the gate is stated as a relative bound at 1e-12 because only summation order is ever at stake. The accumulator-side published ratio, formed from differences of A entries rather than from the omitted field, is -4.11457886616211, matching the field-side ratio to 6.47584e-16 relative and the landed Cycle-700 anchor to 2.664535e-15 absolute. This shows that A carries the Cycle-700 numerical output; it does not type A as a framework Record.

**(iii) The augmented step is a composition of exact symplectic shears.** Each factor — half kick, drift, accumulator shear — is the time-one flow of a quadratic Hamiltonian (1/2) z^T H z whose generator satisfies two conditions: H is symmetric, and JH is nilpotent of order two. Those two conditions are enough. The exponential series terminates at S = I + JH, and

    S^T J S - J = (JH)^T J + J(JH) + (JH)^T J (JH) = H - H + H J H = 0

identically, because (JH)^2 = 0 forces HJH = 0. This is worth stating in that uniform form because the accumulator shear is not a triangular shear in the position/momentum split the way the kick and the drift are; it is a point transformation on positions with the induced cotangent action on momenta. The generator formulation covers all three with one exact algebraic criterion, and it is discriminating: a wrong transpose in either leg of the auxiliary coupling breaks the symmetry of H rather than being absorbed into a tolerance. Measured at the structural box size, generator asymmetry is 0.0, generator nilpotency defect is 0.0, the numerically formed per-factor defect is 0.0, and each factor's algebraic inverse multiplies to the identity at 0.0. Composing all 1100 steps of the structural trajectory into a single 58 x 58 affine map, the entrywise symplectic defect is 3.637979e-12 against a product-norm normalizer of 6.615678e+08, so the normalized defect is below 1e-20; the exact factor proof, rather than the ill-conditioned product determinant, carries the mathematical symplecticity claim. The composed matrix is also checked against the integrator on a seeded augmented initial state.

**(iv) The inverse is explicit and factor-wise.** Each shear is un-applied in reverse order by its own algebraic inverse S^{-1} = I - JH. This is not the Cycle-700 momentum-flip reversal reused under a new name; it inverts the accumulator coupling too, which the momentum flip cannot see. Applied to the full augmented trajectory at the longest ramp, the inverse returns the Cycle-700 state to its zero initial data at the numerical floor and returns A to zero at the numerical floor. Algebraically this is inverse accumulation, not deletion or physical erasure. The exact factor inverses carry the theorem; dense-product and seeded round-trip diagnostics exercise the implementation at finite precision.

**(v) B is exactly conserved by the declared update, including when actively coupled.** Setting B to a nonzero value and integrating 3000 steps, the drift in B is 0.0 — not small, zero, because no update ever writes to B. This is a formal conservation law of the auxiliary extension by construction, not a derived physical charge or conservation mechanism.

## 4. Projection rank, measured

With the source set to zero the map from the initial Cycle-700 state to A is exactly linear, so it has a matrix R of shape 4 x 1458. The many-to-one character of this projected output can therefore be tested as a numerical rank statement.

The harness builds R by four adjoint runs rather than 1458 forward ones, using the Horner recursion v <- F^T (v + chi(t) c_j) run backwards over the whole trajectory, at the shortest ramp of the Cycle-700 ladder, with chi the indicator of the hold window. That is the affordable construction, and it is checked, not trusted: three seeded probes agree with the forward integrator to 6.270474e-14 relative, and against the sourced affine map the identity A(x0; rho) - A(0; rho) = R x0 holds to 1.800173e-13 relative. R is tied to the executed fixture, not to a parallel model of it. It is also shown to be sensitive to what it encodes: rebuilding the adjoint with the hold window short by a single step changes its entries by up to 0.022060595687201985 of its largest, so the agreement just quoted is a real constraint rather than the property of a construction that would have matched anything.

The singular values of R are 77.5680609707272, 54.09257575502038, 47.78606367793194 and 39.56216442318937. At the registered numerical-rank threshold s_min >= 1e-8 s_max, the measured rank is k = 4 and the corresponding kernel dimension is 2N - 4 = 1454 for this L = 9, T = 20, four-detector fixture. No all-L, all-window, or all-projector rank claim is made. Three witnesses run through the forward integrator:

- **Silence.** A normalized numerical-kernel state produces an accumulator output at the floating floor while its final field/momentum state remains order one.
- **Loudness.** A normalized row-space state produces a nonzero accumulator output with large contrast against the silent state.
- **Same accumulator, different omitted state.** Two initial states differing by a full-norm numerical-kernel vector produce accumulator outputs agreeing at the floating floor while their final field/momentum states differ at order one.

At the registered threshold, the projected output is therefore many-to-one by 1454 dimensions on this fixture. The auxiliary extension does not destroy those omitted coordinates: it retains the original field/momentum state, and the explicit inverse of claim (iv) recovers it along with A. This is the generic bookkeeping content of the cotangent lift; it is not evidence for a derived environment or physical apparatus.

## 5. The C4 mutation family through the extension

Every element of the tally row's first cell keeps its gate here, and every dynamical element passes through the auxiliary accumulator.

*Deletion.* With the source zeroed, the hold average and A are exactly all-zero arrays; the deletion ratio against the sourced accumulator is 0.0.

*Sign.* Negating the source negates A bit for bit on the executed trajectory. The accumulator-side published ratio is blind to the flip, agreeing with the positive-source ratio to within 1e-12, while the two detector differences that carry the sign sum to 0.0. The auxiliary accumulator reproduces the Cycle-700 finding that the published ratio is sign-blind and the underlying differences are not.

*Scale.* Doubling and halving the source scales A exactly, float by float, because those factors are powers of two.

*Detector swap.* Exchanging the two accumulator pairs inverts the published ratio at the floating floor.

*Range.* The static long-range anchors listed in section 2 are reproduced unchanged. Cycle 700 gated its range mutation by static solves, with no dynamics in them, so there is nothing for A to carry here: the anchors are verified beside the extension, and the separation of genuine range structure from residual keeps its gate.

*Conservation and reversibility.* Auxiliary momentum is unchanged by construction; the augmented inverse returns the trajectory at the same floating floor as the Cycle-700 dynamical reversal while additionally inverting the accumulation.

## 6. Accumulator properties and the Record-axiom boundary

The following gates are properties of the supplied auxiliary construction only. They do not identify A with a framework Record or derive a Record-writing law.

*Conditional non-disturbance.* On the chosen B = 0 subspace, phi, pi, and the whole hold average are bit-identical to the undilated run.

*No auxiliary back-reaction occurs at B = 0.* This is an invariant subspace of the declared map, not a premise-selected physical sector.

*Back-reaction is detectable by the same machinery.* Switching B on shifts the hold average by 0.024162430644096317 in max norm, the shift is linear in B to 1.740479e-14 relative, and the bit-identity comparison correctly reports inequality. The gate that passes at B = 0 is the same gate that fails off it.

*Window linearity is not Record additivity.* Splitting the hold-step index set at step 500, the first-half accumulator plus the second-half accumulator reproduces the whole-window accumulator to the floating floor. This is finite-sum linearity over disjoint time-index subsets. No gate shows that individual samples or windows are pairwise-disjoint framework-Record collections, lock admissible local possibilities, are permanent, or carry content-only scalar readout. The Record axiom's additivity clause is therefore neither realized nor derived by this row.

## 7. What this does not do

The executed Cycle-700 object is a real affine symplectic flow followed by a supplied real linear projection. What this cycle constructs is a reversible real symplectic bookkeeping extension of that projection. In the broad classical sense it may be called a dilation, but it is the generic cotangent lift available for any declared linear projector and is not a derived physical mechanism. A quantum Stinespring representation, a unitary dilation on the framework site algebra M_2(C), and a lawful Record-writing instrument are not constructed. Merely quantizing the polynomial H_c = B . (P phi) would not establish any of those missing bridges, and this cycle makes no such route-closure claim.

Two further boundaries. First, the extension is a calculational device establishing that this supplied projected output admits a reversible canonical completion. The omitted-coordinate factor is bookkeeping for what the harness chose not to output; nothing here promotes it, A, or P to a framework observable or Record. Second, every supplied object named in section 2 stays supplied. The extension inherits the source, coupling, detector association, window, and normalization; it selects or derives none of them. Its algebra is indifferent to those choices, while the anchor gates deliberately pin the one numerical fixture Cycle 700 ran.

## 8. Structural verification scope

The explicit-matrix block, which composes all 1100 steps into a single 58 x 58 affine map and gates symplecticity, unit determinant, factor-wise inversion and agreement with the integrator, runs at box side 3 with a two-site stand-in accumulator and a small dipole stand-in source. That is forced: the Cycle-700 detector template and frozen source are both out of range on a box of side 3, so no faithful four-site version of the dense block exists at that size. The dense block verifies the algebra of the construction — the generator conditions, composition, and inverse — not the L = 9 geometry.

The L = 9 fixture claims are carried by trajectory-level gates using the Cycle-700 detector template, source, and windows: bit identity at B = 0, A carrying the numerical output, augmented inversion, auxiliary-momentum conservation, numerical rank/kernel measurements, and the mutation family. No claim turns that fixture into a physical mechanism. The algebra does not rest on the box of side 3 alone because the full-size trajectory inverse independently exercises the same shear structure.

## 9. Reproduction

    cd <worktree> && python3 scripts/physical_record_register_symplectic_dilation_cycle704_2026_08_01.py --no-receipt

exits 0 and prints TOTAL: PASS=54 FAIL=0. The committed transcript is generated from the final replay runner and is byte-identical across consecutive runs on the review environment; its exact byte count and SHA-256 are reported in the receipt/review evidence. Elapsed time is carried only in the receipt so that stdout stays deterministic. The receipt timer starts before NumPy/SciPy and both sibling-runner imports and records that scope explicitly; interpreter startup before this module begins is outside it. Run without `--no-receipt`, the harness writes `outputs/physical_record_register_symplectic_dilation_cycle704_receipt_2026-08-01.json`, carrying the full summary, runner self-hash, pass/fail counts, timer scope, and elapsed time.

Reported round-off diagnostics — defects, residuals and round-trip errors — are printed to six significant digits, a display convention applied uniformly to every such quantity; the gates always compare the unrounded values, and fixture magnitudes, landed anchors and singular values are printed at full precision.

## Citations

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Cycle 700 source-response-readout chain](PHYSICAL_OPERATIONAL_SOURCE_RESPONSE_READOUT_CHAIN_CYCLE700_NOTE_2026-07-25.md)
