# A record-register symplectic dilation of the executed Cycle-700 readout channel, with exact conservation, an explicit inverse, and measured openness — Cycle 704

Date: 2026-08-01
Claim type: bounded_theorem
Authority: none. Audit: unset. Constitutional effect: none. This cycle edits no axiom, foundation, Qualification, primitive, registry, policy, queue, audit-status, or PR-control surface. No new axiom or primitive is proposed or adopted.
No coupling value, sign, or scale is selected or derived in this cycle; every such object is named as supplied.
Runner: `scripts/physical_record_register_symplectic_dilation_cycle704_2026_08_01.py` — TOTAL: PASS=54 FAIL=0.

## 1. The wall

The Cycle-700 evidence-ceiling tally carries one cell that its own harness could not fill:

| exact reversibility with conservation, deletion, sign, scale, and range mutations | PARTIAL | C4–C4b; no Stinespring or unitary dilation of the open-system readout channel is constructed |

The first column lists what the Cycle-700 harness did establish about its readout: it reversed exactly, it conserved, and it responded correctly to deletion, sign, scale, and range mutations of the supplied source. The second column says PARTIAL, and the third says why. The reversibility on offer was reversibility of the *dynamics*, run on a state from which the readout had already been extracted and thrown away. Nothing in the Cycle-700 note cited below exhibited a larger reversible system inside which the extraction is itself a step, so the discard stayed outside the reversible description. This cycle builds that larger system for the classical channel Cycle 700 actually executed, and measures exactly what the extraction throws away.

## 2. The channel as executed

Cycle 700 integrates an affine-linear leapfrog on a scalar pair (phi, pi) over a cubic box in Z^3 of side L. Each step is a half kick, a drift, and a half kick, with a supplied frozen source rho entering through a supplied coupling scale. The source is switched on over n_ramp steps by the smooth profile g(step) = 4u^3 - 3u^4 with u = min(1, max(0, step/n_ramp)), and then held fixed for n_hold = 1000 further steps. During the hold the harness accumulates phi and divides by n_hold; the kept output is the value of that time average at four detector sites, and the published scalar is the ratio of two differences of those four values.

Named as supplied, not derived in this cycle: the source profile, the coupling scale, the ramp profile, the association of four particular sites with detectors, the hold window, and — the one easiest to walk past — the 1/n_hold normalization of the hold average. The Record axiom supplies an additive scalar readout over pairwise-disjoint record collections. It supplies no weighting and no normalization. The uniform weight over hold steps and the division by n_hold are a supplied convention of the Cycle-700 harness, carried through unchanged here and gated against it, never re-derived.

At L = 9 the physical state has 2N = 1458 real components and the kept output has k = 4 numbers. Everything else is integrated and then discarded. That discard is the open-system step, and it is what the tally row is about.

The harness first reproduces the landed Cycle-700 anchors on this machine before touching them. The four hold-window ratios across the ramp ladder come back as -4.209568736178572, -4.150939492487698, -4.121308954024253 and -4.1145788661621125; the Cycle-700 dynamical reversal returns the state to its zero initial data at 2.916316e-16; the static long-range anchors return R_static = -3.9169789686578382 with residual 0.003745783167973915 against the split prediction, face-mutated ratio -4.0411929130059585, mutation separation 0.12421394434812028, and separation-to-residual ratio 33.161007665936864. Ten gates, all reproduced, before any new object exists.

## 3. The dilation (theorem statement)

Adjoin a record register. The augmented phase space is R^{2N} x R^{2k} with (phi, A) as positions and (pi, B) as momenta, carrying the standard symplectic form J on the m = N + k position/momentum split. Let P be the k x N detector projector. Add to each hold step the time-one flow of the record-coupling Hamiltonian

    H_c = B . (P phi).

Its equations of motion are dphi/dt = 0, dB/dt = 0, dpi/dt = -P^T B, dA/dt = P phi. Since phi and B are both constant along that flow, the time-one map is exactly two assignments,

    pi[det] -= B          (back-reaction)
    A       += phi[det]   (record)

which read and write disjoint variables, so their order is immaterial and the pair is a single exact symplectic shear. The theorem is the conjunction of five claims, each carrying its own gate.

**(i) Non-disturbance is bit-for-bit on the physical slice B = 0.** On that slice the back-reaction leg subtracts positive zero, which preserves every bit of every float, and the record leg writes only into A. Running the full augmented integrator at the longest ramp beside the untouched Cycle-700 integrator, the final phi, the final pi and the whole hold average agree by array equality, not by tolerance. The dilation does not perturb the channel it dilates; it is the same trajectory with more of it kept in view.

**(ii) A carries the executed readout.** Dividing the register by n_hold reproduces the hold average at the four detector sites to relative 0.0 — the two summation orders happen to agree bit for bit here, and the gate is stated as a relative bound at 1e-12 because only summation order is ever at stake. The register-side published ratio, formed from differences of register entries rather than from the discarded field, is -4.11457886616211, matching the field-side ratio to 6.47584e-16 relative and the landed Cycle-700 anchor to 2.664535e-15 absolute. The readout is genuinely in the register, not merely alongside it.

**(iii) The augmented step is a composition of exact symplectic shears.** Each factor — half kick, drift, record shear — is the time-one flow of a quadratic Hamiltonian (1/2) z^T H z whose generator satisfies two conditions: H is symmetric, and JH is nilpotent of order two. Those two conditions are enough. The exponential series terminates at S = I + JH, and

    S^T J S - J = (JH)^T J + J(JH) + (JH)^T J (JH) = H - H + H J H = 0

identically, because (JH)^2 = 0 forces HJH = 0. This is worth stating in that uniform form because the record shear is not a triangular shear in the position/momentum split the way the kick and the drift are; it is a point transformation on positions with the induced cotangent action on momenta. The generator formulation covers all three with one exact algebraic criterion, and it is discriminating: a wrong transpose in either leg of the record coupling breaks the symmetry of H rather than being absorbed into a tolerance. Measured at the structural box size, generator asymmetry is 0.0, generator nilpotency defect is 0.0, the numerically formed per-factor defect is 0.0, and each factor's algebraic inverse multiplies to the identity at 0.0. Composing all 1100 steps of the structural trajectory into a single 58 x 58 affine map, the entrywise symplectic defect is 3.637979e-12 against a product-norm normalizer of 6.615678e+08, so the normalized defect is below 1e-20; the determinant is unit with sign 1.0 and log-determinant 4.82947e-14. The composed matrix is checked against the real integrator rather than living beside it: applied to a seeded augmented initial state it reproduces the integrator's final augmented state to 6.255091e-16 relative.

**(iv) The inverse is explicit and factor-wise.** Each shear is un-applied in reverse order by its own algebraic inverse S^{-1} = I - JH. This is not the Cycle-700 momentum-flip reversal reused under a new name; it inverts the record coupling too, which the momentum flip cannot see. Applied to the full augmented trajectory at the longest ramp, the inverse returns the physical state to its zero initial data at 2.916316e-16 and drives the register back to the zero register at 2.414735e-15. That second number carries the interesting content: un-registration is exact inversion, not deletion. Nothing erases the record by a separate rule; the record is run backwards. Factor-wise inversion of the composed structural map deviates from the identity by 3.274181e-11 entrywise, or 4.949e-20 against the same product-norm normalizer of 6.615678e+08, and the affine round trip through the composed map recovers a seeded vector to 1.803016e-13 relative. That entrywise figure is worth naming plainly: it is the largest raw deviation anywhere in the harness, it sits above a naive 1e-11 entrywise bound, and it is gated in normalized form for the ordinary reason that an entrywise bound on a product of more than four thousand dense factors, whose one-norm and infinity-norm are each a few times 1e+04, is a bound on the normalizer rather than on the construction. The independent round-trip gate, which is normalization-free, agrees.

**(v) B is exactly conserved, including when actively coupled.** Setting B to a nonzero value and integrating 3000 steps, the drift in B is 0.0 — not small, zero, because no update ever writes to B. The register momentum is a conserved quantity of the dilation whether or not it is doing anything.

## 4. Openness, measured

With the source set to zero the map from the initial physical state to the register is exactly linear, so it has a matrix R of shape 4 x 1458, and the openness of the channel becomes a rank statement that can be measured rather than asserted.

The harness builds R by four adjoint runs rather than 1458 forward ones, using the Horner recursion v <- F^T (v + chi(t) c_j) run backwards over the whole trajectory, at the shortest ramp of the Cycle-700 ladder, with chi the indicator of the hold window. That is the affordable construction, and it is checked, not trusted: three seeded probes agree with the forward integrator to 6.270474e-14 relative, and against the real sourced channel the affine identity A(x0; rho) - A(0; rho) = R x0 holds to 1.800173e-13 relative. R is tied to the executed channel, not to a parallel model of it. It is also shown to be sensitive to what it encodes: rebuilding the adjoint with the hold window short by a single step changes its entries by up to 0.022060595687201985 of its largest, so the agreement just quoted is a real constraint rather than the property of a construction that would have matched anything.

The singular values of R are 77.5680609707272, 54.09257575502038, 47.78606367793194 and 39.56216442318937. The rank is exactly k = 4 and the kernel has dimension 2N - 4 = 1454. Three witnesses run through the real forward integrator:

- **Silence.** A normalized kernel state produces a record of relative size 3.433735e-19, the float floor, while its final physical state has norm 1.4554301648969057, order one. It moves; it says nothing.
- **Loudness.** A normalized row-space state produces a record of relative size 0.0008532113036548952. The contrast against the silent state is 2.484791e+15.
- **Same record, different environment.** Two initial states differing by a full-norm kernel vector produce records agreeing to 2.940279e-19 while their final physical states differ by 1.4554301648969066 in relative norm. Identical records, visibly different worlds.

The channel is therefore strictly many-to-one, by 1454 dimensions at L = 9, and the number is measured. What the dilation contributes is that those 1454 dimensions are not destroyed by the readout. They sit in the environment factor of the augmented state, and the explicit inverse of claim (iv) recovers them along with the record. Discarding is a choice made by the harness about what to look at, not a fact about the evolution.

## 5. The C4 mutation family through the dilation

Every element of the tally row's first cell keeps its gate here, and every dynamical element passes through the register.

*Deletion.* With the source zeroed, the hold average is exactly the all-zeros vector and the register is exactly the zero register, by array equality rather than tolerance; the deletion ratio against the sourced record is 0.0.

*Sign.* Negating the source negates the register bit for bit, because negation commutes with every float operation under round-to-nearest. The register-side published ratio is blind to the flip, agreeing with the positive-source ratio to within 1e-12, while the two detector differences that actually carry the sign — one from the positive source, one from the negated source — sum to 0.0. The register reproduces the Cycle-700 finding that the published ratio is sign-blind and the underlying differences are not.

*Scale.* Doubling and halving the source scales the register exactly, float by float, because those factors are powers of two.

*Detector swap.* Exchanging the two register pairs inverts the published ratio, to 2.775558e-17.

*Range.* The static long-range anchors listed in section 2 are reproduced unchanged. Cycle 700 gated its range mutation by static solves, with no dynamics in them, so there is nothing for the register to carry here: the anchors are verified beside the dilation, and the separation of genuine range structure from residual keeps its gate.

*Conservation and reversibility.* Register momentum is conserved at 0.0; the augmented inverse returns the trajectory at 2.916316e-16, the same floor as the Cycle-700 dynamical reversal, while additionally inverting the extraction.

## 6. Record-axiom reading

The Record axiom's register-not-read structure becomes computational here, and each part of it has a measurement.

*Registration does not change the registered system's path.* Not approximately: bit-identity of phi, of pi, and of the whole hold average against the undilated run.

*There is no readback on the physical slice.* Readback would be the register acting on the field, which is exactly the B-dependent back-reaction leg, and B = 0 is the physical slice.

*Readback is nevertheless detectable by the same machinery.* This matters, because a non-disturbance claim that could not fail would be worth nothing. Switching B on shifts the hold average by 0.024162430644096317 in max norm, the shift is linear in B to 1.740479e-14 relative, and the bit-identity comparison correctly reports inequality. The gate that passes on the physical slice is the same gate that fails off it.

*Additivity over disjoint windows.* Splitting the hold window at step 500, the register accumulated over the first half plus the register accumulated over the second half reproduces the register over the whole window to 1.047724e-15 relative. The register is an additive scalar readout over pairwise-disjoint record collections, which is the form the Record axiom asks for, realized by a symplectic flow rather than imposed.

## 7. What this does not do

The executed Cycle-700 channel is classical: a real symplectic flow on a real phase space, with a real linear functional read out at the end. What this cycle constructs is the classical reversible symplectic dilation of that classical channel, together with a measurement of what it discards. A quantum Stinespring representation, or a unitary dilation on the site algebra M_2(C) of the framework's qubits, is not constructed here and no claim about one is made. The record-coupling Hamiltonian H_c = B . (P phi) is the classical shadow of a controlled unitary, and quantizing it on the qubit algebra is the next route this construction opens; whether the resulting dilation is unique, and what it costs, are open questions this cycle does not touch.

Two further boundaries. First, the dilation is a reconstruction in the framework's own sense — a calculational device establishing that the executed readout admits a reversible completion. The record remains the reality; the environment factor is bookkeeping for what the harness chose not to look at, and nothing here promotes it to an observable. Second, every supplied object named in section 2 stays supplied. The dilation inherits the source, the coupling, the detector association, the window and the normalization; it does not select or derive any of them. The construction itself is indifferent to those choices — the dilation-side gates are stated relative to whatever channel is executed — while the anchor gates pin, deliberately, the one channel Cycle 700 actually ran.

## 8. Structural verification scope

The explicit-matrix block, which composes all 1100 steps into a single 58 x 58 affine map and gates symplecticity, unit determinant, factor-wise inversion and agreement with the integrator, runs at box side 3 with a two-site stand-in register and the small dipole stand-in source. That is forced: the Cycle-700 detector template and frozen source are both out of range on a box of side 3, so no faithful four-site version of the dense block exists at that size. The dense block therefore verifies the algebra of the construction — the generator conditions, the composition, the inverse — and not the physical geometry.

The physical-geometry claims are carried entirely by the L = 9 trajectory-level gates, which use the real detector template, the real source and the real windows: the bit-identity claims, the register-carries-the-readout claims, the augmented inverse, the conservation of register momentum, the rank and kernel measurements, and the whole mutation family. Nothing physical rests on the box of side 3, and nothing algebraic rests on it alone either, since the trajectory-level inverse independently exercises the same shear structure at full size.

## 9. Reproduction

    cd <worktree> && python3 scripts/physical_record_register_symplectic_dilation_cycle704_2026_08_01.py --no-receipt

exits 0 and prints TOTAL: PASS=54 FAIL=0. The transcript is 3826 bytes and is byte-identical across consecutive runs; elapsed time is carried only in the receipt so that the transcript stays deterministic. A cold run takes roughly six and a half to eight and a half seconds on the development machine, most of it in the four longest leapfrog trajectories and the two sibling-runner imports. Run without `--no-receipt`, the harness writes `outputs/physical_record_register_symplectic_dilation_cycle704_receipt_2026-08-01.json`, carrying the full summary, the runner self-hash, the pass and fail counts and the elapsed time.

Reported round-off diagnostics — defects, residuals and round-trip errors — are printed to six significant digits, a display convention applied uniformly to every such quantity; the gates always compare the unrounded values, and physical magnitudes, landed anchors and singular values are printed at full precision.

## Citations

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Cycle 700 source-response-readout chain](PHYSICAL_OPERATIONAL_SOURCE_RESPONSE_READOUT_CHAIN_CYCLE700_NOTE_2026-07-25.md)
