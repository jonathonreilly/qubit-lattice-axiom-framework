# A26 report: matter on a static shape field through fixed lapse and frame couplings (A23 decisive test 4)

Scratch directory: `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A26/`
- **Modules.**
  - `walk2d.py`: 2D Bloch cycle, used for the symbol checks.
  - `rs2d.py`: real-space 2D stepper, Bloch batches and packet preparation.
- **Scripts.**
  - `s0_sanity.py`, `t0_consistency.py`, `s1_span.py`, `s2_shear_symbol.py`, `s3_span3d.py`;
  - `t1_field1d.py`, adapted from A18's `lapse1d.py`;
  - `t2_bend2d.py` with `a2_bend_analysis.py`;
  - `t3_fall2d.py`, `t4_shear2d.py`, `t5_nosignal.py`.
- **Logs.** `out_symbols.txt`, `out_1d.txt`, `out_2d_bend.txt`, `out_2d_fall.txt`, `out_2d_shear_ns.txt`.
- **How runs were made.** Every run went through `run.sh` with `nice -n 10`, all four thread caps at 1, and a 58 s alarm. The longest wall time was 35 s. Every run quoted below peaked at 187 MB or less. Two superseded 2D-fall attempts peaked at 263–294 MB, still under the 300 MB cap.
- **Nothing adopted.** Everything here is a supplied toy. I made no git operations, no repo edits and no PRs, and ran no review lanes. Two repo notes were read as plain files in the worktree.

---

## 1. Question

Couple A18's time-symmetric one-site-mass Dirac step, in 1D and then 2D, to a static field configuration: lapse N = 1 − U and spatial metric h_ij = 2Uδ_ij (A23 D16). The coupling uses fixed operators:
- the lapse multiplies one-site terms;
- lapse × frame multiplies hop terms;
- a frame-type coupling carries shear.

Then four questions:
1. Do massless packets delay and bend with γ = 1 without a hand-chosen composition rule, because h_ij supplies the spatial factor?
2. Do one-site-mass packets fall universally, on geodesics?
3. Does matter respond to a TT shear h_xy, and how?
4. Do two-site masses keep A18 D3's order-one equivalence-principle violation?

## 2. Answer

**Conditional yes.**

**The metric matter sees.** If matter couples through the fixed operators of A23's F2, then every massless packet and every one-site-mass packet sees the field's own metric, ds² = −N²dt² + (δ_ij + h_ij)dx^i dx^j [EXACT in the eikonal, small-dose limit, at first order]. The fixed operators are:
- one lapse factor on every term;
- one frame factor, including its off-diagonal part, on every hop.

**Light and γ = 1.** With A23 D16's static solution, light delays and bends with γ = 1, and no composition rule is needed:
- any symmetric average of the two endpoint lapses gives the same first-order result;
- A18's "b = 2a" becomes b = a + γ_field, inherited from h rather than chosen.

CHECKED as follows:
- 1D delay ratio and 2D deflection ratio, field against lapse-only, extrapolate to 1.999 and 1.995 at zero field;
- matter's 1 + γ follows the field's h: 1.000, 1.505 and 2.019 for h = 0, U and 2U, while A18's product rule gives 2.019 whatever h is;
- moving massive packets fall with 1 + γv², γ = 0.988.

**Why the coupling form is not free.** If the coupled system keeps the field's gauge symmetry (part of A23's F4), then the form of the coupling is fixed: one lapse per term, one frame per hop, no frame on mass terms [EXACT at linear order and long wavelength; a named conditional on the lattice].

**One-site masses** fall alike on geodesics [EXACT: their rest frequency is exactly μN at any dose; CHECKED].

**Two-site masses** keep the factor-2 violation only under an "operator-support" coupling. That coupling makes a resting clock respond to a pure-gauge stretch, which the tensor branch's conserved-source requirement excludes [EXACT core; ARGUED application]. Under the allowed "stress" coupling they fall alike [CHECKED: 1.980 against 0.993 in 1D].

**Shear.** Matter responds to h_xy only through a frame rotation of the hops' spin structure:
- bond-length coupling is blind to h_xy;
- no nearest-neighbour, cell-periodic hop modulation gives a taste-blind cross shear [EXACT in the small-dose limit; CHECKED at finite dose, in 2D and 3D];
- period-2 phases give the two tastes opposite shears;
- a fixed depth-3 in-cell "frame sandwich" gives every band the metric response [CHECKED].

**No signalling** [EXACT; CHECKED to 2.5e-16].

**Still supplied:**
- F1–F4 themselves, including D16's condition that the lapse also paces the field;
- the lattice form (dose, or amplitude-form coupling);
- a vacuum-centred cone;
- the mass/kinetic split of bond terms;
- the shear sandwich.

## 3. Derivation

### 3.0 Conditionals used

- **A23's conditionals.** F1 (field sector), F2 (fixed coupling), F3 (energy–momentum source) and F4 (constraint preservation), as named there.
- **G1, introduced here.** The coupled matter–field system keeps the field's linearized gauge symmetry: a uniform n (a time rescaling) or a uniform h_ij (a coordinate stretch or shear) must be undetectable by local matter. This is the matter-side half of F4.
- **Owner readings.** I1–I6 and the Q-readings are not used.

### 3.1 The coupled step (D1, a definition)

**1D**, one excitation, sites j, cells (2c, 2c+1). The cycle is

U = M_h · E_h · O · E_h · M_h

- M_h = ∏_j exp(−i(μ/2)N_j ε_j n_j), with ε_j = (−1)^j. This is the one-site sublattice mass (A10 S11) times the lapse.
- E_h applies exp(−i(θ_b/2)σ_x) on even bonds and O applies exp(−iθ_b σ_x) on odd bonds. This is A10's time-symmetric word, which A18 D6 needs.
- The bond angle is θ_b = θ0 · N_b · e_b, with N_b = (N_j + N_{j+1})/2 and e_b = 1 − (h_j + h_{j+1})/4. That is, the lapse at the bond times the frame along the bond.
- A two-site (A10 B-type) mass splits the angles θ0 ± δ, with two options:
  - operator-support (OS): θ_b = (θ0 ± δ)N_b e_b;
  - stress (ST): θ_b = N_b(θ0 e_b ± δ).

**2D** uses A10's KS signs η_x = 1, η_y = (−1)^x, with a time-symmetric x-block and y-block.
- Diagonal frame: a-bonds carry e = 1 − h_aa/2.
- Off-diagonal frame: the x-block is conjugated, U_x → R U_x R†, with R(β) = S P(β) S†, sin 2β = h_xy, where
  - S = exp(−i(π/4)·[unsigned in-cell y-hops]) is fixed;
  - P(β) = exp(−iβ·[in-cell x-hops with sign (−1)^y]) is set by the field.
- R(β) equals exp(iβ X_x Y_y) = exp(β A_x A_y). This is a spin-frame rotation and an in-cell diagonal operator [EXACT; CHECKED to 1.1e-16].
- R and every other layer are fixed nearest-neighbour gates controlled by the field's site values.

### 3.2 Eikonal (D2–D3)

**D2 [EXACT, small dose, linear in q].**
- Near the cone K*, the step's generator is H = Nμε + θ0 N Σ_{a,i} A_a E_a^i q_i.
- For the cycle above: E_x^x = e_x cos 2β, E_y^x = −e_x sin 2β, E_y^y = e_y, E_x^y = 0.
- ε anticommutes with every A_a, and the A_a anticommute among themselves. So H² = N²μ² + N²θ0² q^T(E^TE)q.
- Hence g_00 = −N² and g^{ij} = (E^TE)^{ij} = δ^{ij} − h^{ij} + O(h²), i.e. g_ij = δ_ij + h_ij.
- Massless packets follow Fermat rays and massive packets follow geodesics, in the same metric.
- An overall rotation of every block's spin frame is the antisymmetric part of E and is undetectable (pure gauge). Only the relative rotation between hop directions, the symmetric shear, acts.

**D3 [EXACT].** In A18's notation (one-site pace N^a, two-site pace N^b, γ = b/a − 1):
- the lapse gives a = 1;
- the bond factor is N·e ≈ N^{1+γ_f} when h = 2γ_f U δ, so b = 1 + γ_f and γ_matter = γ_field;
- with A23 D16 (γ_f = 1), b − a = 1 comes from the frame, not from a composition choice;
- N_b enters only through its midpoint value at first order, so mean, min and geometric-mean bond lapses agree.

CHECKED: delays 74.841, 74.978 and 74.841 differ only at second order.

### 3.3 Why the coupling form is forced, given G1 (D4)

[EXACT at linear order, long wavelength.]
- A uniform h_ij is pure gauge (ξ_i = ½h_ij x^j). Matter's coordinate dispersion must then be the flat one in transformed coordinates, ω² = μ² + c²(δ − h)^{ij}q_iq_j.
- That requires exactly one frame factor (1 − h/2, off-diagonal part included) per hop, i.e. per lattice derivative, and none on derivative-free (mass) terms.
- A uniform n is a time rescaling, so every term carries exactly one lapse factor.
- Terms with p derivatives get frame^p. That is the dimension-based weight A18 D7 asked for, now supplied by the field's gauge symmetry rather than chosen per term.
- On the lattice there are no exact diffeomorphisms, so G1 fixes the rule only at leading order. The lattice-level form remains a named conditional.

### 3.4 Finite dose (D5) [EXACT; CHECKED]

- Multiplying the gate angle gives cone speed sin(θ0 N e)/sin θ0, so γ_eff = 2θ0 cot θ0 − 1, exactly A18 D4.
- The ratio field/lapse is 2 at any dose at first order. The dose factor cancels.
- Multiplying the hop amplitude instead (sin θ_b = N e sin θ0) gives cone speed N e exactly at any dose. CHECKED at θ0 = 0.6: 1.005 of the small-dose metric, against 0.884 for the angle form.
- The frame rotation R is exact at any dose. With angle coupling, diagonal and off-diagonal frame components respond with different dose factors, an O(θ0²) anisotropy; the amplitude form removes it.

### 3.5 Massive one-site packets (D6) [EXACT; CHECKED]

- At K*, every bond layer cancels, so the rest frequency is μN exactly at any dose and any μ (CHECKED to 1e-12).
- So g_00 is the same for all one-site species: fall rate c²∇U at first order, geodesic in the eikonal.
- The velocity-dependent part of the fall uses the same spatial metric, a_⊥ = c²g(1 + γv²).
- A resting packet does not feel a uniform shear: the one-site rest frequency is independent of e and β.

### 3.6 Two-site masses (D7)

**[EXACT; CHECKED] Rest frequencies.**
- OS: 2δNe. ST: 2δN (both to 1e-12).
- So OS falls at (1 + γ_field) times the one-site rate, which is 2 for h = 2U; ST falls at the one-site rate.

**[EXACT core] OS fails the gauge test.**
- Under OS, a uniform pure-gauge h changes a resting two-site clock's rate relative to a one-site clock.
- Equivalently, OS's stress source S^ij includes the two-site rest energy, so ∫S^ij ≠ 0 at rest. A conserved stress has ∫T^ij = 0 for a static body (Laue identity, from ∂_jT^ij = 0).
- Then ∂_jS^ij ≠ −∂_tT^{0i}, so the field's momentum constraint fails to propagate, against A23 D13 and D17.

**[ARGUED] Consequence.** In the tensor branch, A18 D3's order-one violation is a symptom of a coupling the field forbids, not a prediction. The price: the lattice coupling must class the staggered part of each bond angle as mass (frame-free) and the uniform part as motion (one frame). That split is supplied.

### 3.7 Shear (D8–D11)

**D8 [EXACT] Bond lengths are blind to h_xy.** An axis bond's length depends only on h_aa (A23 D18). CHECKED: h_xy changes no band, residual 3e-12.

**D9 [EXACT in the Trotter limit; CHECKED at finite dose, 2D and 3D] What nearest-neighbour modulations can reach.**
- The cone's spin–taste structure in 2D: A_x = −Y_x = γ1⊗1 and A_y = −Z_xY_y = γ2⊗1. The tastes T_b commute with both A's.
- Dictionary [CHECKED]:

| Lattice operator | Spin–taste form |
|---|---|
| X_y (unsigned real y-hop) | −γ1⊗ξ3 |
| Y_y (unsigned imaginary y-hop) | 1⊗ξ1 |
| Z_yX_x ((−1)^y real x-hop) | γ2⊗ξ3 |
| Z_yY_x ((−1)^y imaginary x-hop) | −1⊗ξ2 |
| X_xY_y (in-cell diagonal) | G3⊗1, the spin rotation |

- A y-hop moves only the y-bit, so its q_y-linear part always carries a y-bit Pauli. γ1⊗1 carries none.
- Over all 16 cell-periodic nearest-neighbour hop modulations (8 bond classes × real or imaginary), restricted to those that leave the cone ungapped and unshifted:
  - the taste-blind frame they reach has rank 2, the diagonal only;
  - the cross shear lies wholly outside it (residual 1.000);
  - the plus shear lies inside it (residual 0).
- The same holds at Floquet doses θ = 0.1, 0.3, 0.6 and 1.0 (spurious singular values ≤ 5e-10).
- In 3D, over 48 modulations: rank 3 (diagonal), cross residual 1.000.
- This class includes the repo TT note's period-2 intertwiner. That note's observable is sea pair statistics, a different question, so there is no contradiction.

**D10 [EXACT; CHECKED] Period-2 phases give a taste-graded shear.**
- Staggered Peierls phases ∝ h_xy, pattern (−1)^{x+y} on x-bonds and −(−1)^y on y-bonds, give (γ1q_y + γ2q_x)⊗ξ3.
- So the two tastes see h_xy with opposite signs.

**D11 [EXACT; CHECKED] What works.**
- The taste-blind cross shear needs G3⊗1 = (γ1⊗ξ3)(γ2⊗ξ3)·phase, the product of the two taste-graded operators. The S P S† sandwich builds exactly that product.
- It is "curl-shaped": a y–x–y path around a plaquette.
- In the axioms' register: if Q3's gluing of change to the grid's rotations may tilt locally, the field's shear is a relative tilt of the gluing between hop directions. A common tilt does nothing.

### 3.8 Locality and no signalling (D12) [EXACT; CHECKED]

- The coupled step is a fixed, finite-depth circuit of nearest-neighbour gates controlled by the field's site possibilities: W = Σ_n |n⟩⟨n|_f ⊗ S(n).
- It is linear in the state, so the light cone is strict and nothing signals (A23 D1).
- Pace "dials" computed from the branch state do signal.

### 3.9 Lattice effects found (D13–D14)

**D13 [EXACT at second-order BCH; CHECKED] Taste-dependent sideways drift from the block order.**
- A10's x-then-y order adds sin²θ q_x q_y G3 to the generator.
- With a one-site mass this splits the two tastes linearly in q_y: v_y = ±μ sin²θ q_x/ω. Measured 0.0347 against predicted 0.0349 cells/cycle.
- This drifting coupling biases moving massive packets by about 2–5%.
- Alternating the order each cycle (xy, yx, …) removes it: split 0.
- It vanishes at small dose and for massless or resting packets.

**D14 [EXACT, inherited] Cone offset.**
- A18 D5's cone offset persists. Lapse and frame multiply any vacuum-relative offset of the hop generator, giving a colour-dependent potential.
- My toys use offset-free hop generators, so E_c = 0 is supplied, not derived.

### 3.10 Supplied versus derived

| Item | Status |
|---|---|
| Matter's metric = the field's metric; γ_matter = γ_field; composition-independent | Derived given F2 (D2, D3) |
| Coupling form (lapse per term, frame per hop, none on mass terms) | Forced by G1 at linear order; lattice form supplied (D4) |
| h = 2Uδ, n = −U | A23 D16, conditional on the lapse pacing the field |
| Small dose, or amplitude-form coupling | Supplied (D5) |
| One-site masses universal on geodesics | Derived (D6) |
| Two-site mass split (ST) | Selected by F4/G1; the lattice split is supplied (D7) |
| In-cell frame rotation for shear | Supplied structure, fixed π/4 gates (D11) |
| E_c = 0, block order | Supplied (D13, D14) |
| β (second order) | Open; the matter side is exact, so β is the field's question (A23 D20) |

## 4. Checks

| Script | What it checks | Result (tolerance) |
|---|---|---|
| `s0_sanity.py` | Flat 2D cycle | Cone slope/sin θ = 0.9999999996–0.9999999998 over 13 directions; rest frequencies 0.05/0.045/0.16 = μN exactly; two-site rest 2δ; sandwich identity 1.1e-16 |
| `t0_consistency.py` | Real-space step vs Bloch eigenvalue, 7 coupling cases | ≤ 2.3e-15; two Bloch builders agree to 5.6e-16 |
| `s1_span.py` (2D) | Reachable frame | Detailed in §3.7 D9 |
| `s3_span3d.py` (3D) | Reachable frame | Detailed in §3.7 D9 |
| `s2_shear_symbol.py` (θ = 0.3) | Plus shear, bond lengths | b = −0.04849 in every band = −h·θ cot θ (fit residual ≤ 1.6e-10) |
| | Cross shear, bond lengths | No change |
| | Cross shear, period-2 | Slopes at 45° = {0.97499, 0.97499, 1.02499, 1.02499}: taste-split |
| | Cross shear, frame rotation | All four bands 0.97468 = √(1−h) at 45° and 1.02470 at 135° |
| | Conformal coupling | 1+γ (dose-normalized) = 2.011 (field), 1.005 (lapse-only), 1.005 (frame-only) at U = 0.01 |
| `t1_field1d.py`, delay (θ0 = 0.2, U0 = 0.05) | Couplings vs exact-dispersion eikonal | field 74.841 (eikonal 74.840), min 74.978, geo 74.841, A18 product 74.841, lapse 36.723, frame 36.723; all within 2e-5 of eikonal |
| | Field/lapse ratio | 2.038; 2.0185 at U0 = 0.025; extrapolates to 1.999 |
| | Higher dose θ0 = 0.6 | Ratio 2.043; absolute delay 0.887 of metric |
| | Amplitude form (θ0 = 0.6) | 1.005 of metric; ratio 2.018 |
| | h = 0, U, 2U | 1.000 / 1.505 / 2.019; A18 product rule 2.019 always |
| `t1_field1d.py`, fall (σ = 300) | a/(c²g) | 0.9969 (μ = 0.05), 0.9950 (μ = 0.10), 1.9742 (OS), 0.9902 (ST); measured/semiclassical 0.994–0.998 |
| | Ratios to μ = 0.05 | 0.9981 / 1.9803 / 0.9933 (semiclassical 0.9975 / 1.988 / 0.994) |
| `t2_bend2d.py` + `a2_bend_analysis.py` | 2D deflection, U0 = 0.03 | field −0.0575, lapse −0.0283, frame = lapse; ratio 2.0325 |
| | 2D deflection, U0 = 0.015 | ratio 2.0135; extrapolated ratio 1.995 |
| | Against spread-averaged ray prediction | Extrapolates to 0.998 (field), 1.001 (lapse); norm conserved to 1e-14 |
| `t3_fall2d.py`, standard order (σ = 72, g = 1e-4) | a/(c²g) at rest | 0.9881 (μ = 0.15), 0.9912 (μ = 0.08), 1.9654 (OS), 0.9878 (ST) |
| | Ratios | 1.0032 / 1.989 / 0.9997 |
| `t3_fall2d.py`, alternating order, moving | v = 0.586c | field/lapse 1.3361 (lattice semiclassical 1.3403, continuum 1+v² 1.343) |
| | v = 0.871c | 1.7555 (1.7645, 1.759); implied γ = 0.988; measured/semiclassical 0.992–0.998 |
| `t4_shear2d.py` (h = 0.1) | Axis-packet tilt (metric −0.0997 rad) | flat 2e-5; bond lengths 2e-5; period-2 −0.1030 (+ taste), +0.1018 (− taste); frame −0.1006 / −0.0972 |
| | Plus shear, diagonal packet | tilt 0.0940 (0.0941 predicted with dose factor) |
| `t5_nosignal.py` (6 qubits: distant b, field f, 2×2 matter cell; formation at one matter site, record statistics at another; 60 random states) | No signalling | TV 2.5e-16 (fixed coupling) vs 4.0e-3 (dial); distant qubit unchanged to 2.8e-16 |

**First-run errors, fixed.**
- I first put equal imaginary phases on even and odd bonds. That is a uniform Peierls shift, not a shear; corrected to the staggered pattern.
- The Floquet span initially showed a rank-4 artifact from finite-difference noise. A 4th-order stencil brought the spurious singular values down to 1e-10.
- The sandwich's time order was reversed; fixed (consistency 2.3e-15).
- Early 2D-fall runs gave +18% and a convergence run that went the wrong way. Cause: packet tails wrapping across the boundary jump in U. Fixed with 6σ margins and stripe packets.
- Moving packets came out 3–5% short. Traced to D13; fixed with the alternating order.
- The massive bump-bending run (tag m15) wrapped in y and is superseded by the stripe fall test.

## 5. Real-physics match

**Matches, all COMPARATOR from memory:**
- γ = 1: Cassini |γ−1| ≲ 2e-5, given amplitude coupling or θ0 ≲ 6e-3;
- light bending and Shapiro delay;
- weak-field geodesic fall including the 1 + γv² velocity dependence;
- universal fall of one-site-mass species at eikonal order: no lattice-level violation at first order, against MICROSCOPE's ~1e-15.

**Falsifiers:**
- Any species coupled operator-support style, with rest energy in bonds, would fall at about twice the rate. That is excluded by MICROSCOPE, and by F4.
- Angle coupling at θ0 > 6e-3 fails Cassini (A18 D4).
- A nonzero cone offset gives colour-dependent bending (A18 D5).
- Bond-length-only matter is blind to the cross polarisation. Gravitational-wave response would then depend on a detector's orientation relative to the grid's axes. Detector responses fit both tensor polarisations with standard antenna patterns (COMPARATOR, from memory).
- Period-2 coupling makes the two tastes feel opposite gravitational-wave shears. That is falsified if tastes are distinct species.

**Not tested here:** β, strong field, field dynamics and back-reaction.

## 6. Open edges and next steps

1. **Lattice source conservation.** Build the ST coupling's lattice stress tensor and measure ∂T at O(a²), i.e. the ghost-source leakage (A23 tension f/h).
2. **Derive the frame sandwich.** Derive it from a principle (a Q3 tilt), check covariance under the 24 rotations, and verify the 3D xz and yz planes. The 3D in-cell rotations A_aA_b are face-diagonal operators of the same Pauli type [ARGUED].
3. **Many-body sandwich.** With several excitations, check the sandwich with and without fermionic signs.
4. **Dynamic coupling.** Couple matter to A23 D15's leapfrog spin-2 field: test geodesic deviation from a passing TT wave, and back-reaction, with matter sourcing the field through the same coupling.
5. **Fix the cycle structure.** Choose alternating or palindromic order (D13) and angle or amplitude form (D5). Field and matter must share one light cone (GW170817-type equality).
6. **Remaining inputs.** E_c = 0 (vacuum-normal-ordered generators) and β (A23 D20).
7. **Possible larger check (not needed now, not run).** A 3D one-excitation real-space TT test on a 64³ torus, roughly 0.3M sites. That is similar cost to the 2D runs here.

## 7. Plain-language summary

Suppose each place also carries a smooth "stretch" in its shared possibilities, saying how fast change runs there and how long each step to a neighbour is. Suppose the fixed rule slows each place's own change by the first and each hop between neighbours by both. Then light passing a heavy body is delayed and bent by the full amount seen in nature, because the stretch itself lengthens the steps. No separate choice about how two neighbours' slowings combine is needed, and the small calculations agree to about one percent. Everything whose weight sits at single places falls alike, and moving things fall a little faster in just the proportion nature shows; things whose weight sits in the links fall alike too, provided the links' weight is not also stretched, which the stretch's own bookkeeping forbids. A diagonal squeeze of space, one kind of gravity ripple, is felt only if the rule also turns each hop's sense of direction, using a fixed three-move shuffle inside each small block of places. Still chosen, not derived: that matter is tied to the stretch at all, the stretch's own rules that make space stretch as much as time slows, a few step-level details, and that shuffle.