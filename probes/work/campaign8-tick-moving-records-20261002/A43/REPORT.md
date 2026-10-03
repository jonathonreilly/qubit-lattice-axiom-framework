# A43 report: can two-part matter that turns with the grid come from one qubit per place?

**Housekeeping.**
- No git writes, no repo edits, no PRs. The repo was read only with `git show origin/main:` at `b6fda5ae1d`; no fetch.
- Scripts are in `SP/c8/A43/` and every run went through `run.sh`: load gate below 6, the shared `NUMLOCK`, `nice -n 10`, the four BLAS caps at 1, and a 28 s CPU cap. Loads at run time were 2.4–4.0. The longest run took 10.5 s and the largest used 60 MB. The lock was released after each run and is now gone.
- I did not write `SP/c8/A43/REPORT.md`, because my harness forbids subagent report files. This message is the full report.

**Grades.** EXACT (proof or exact arithmetic), CHECKED (numerics with a stated tolerance), ARGUED (reasoning without proof), COMPARATOR (literature from memory, not verified), SUPPLIED (a named premise put in by hand). Every model is a supplied toy; nothing here is adopted.

## 1. Question

The two-part walk H = Σ_a σ_a sin k_a (repo block 54; A1 D21; G5 row R3) has two internal states per place that turn with the grid, and eight clean round crossings. With one qubit per place, one flip of a calm product background has only one internal state. So:
- (1) Confirm the walk's crossings and its covariance under full soldering.
- (2) Give the cost of each route to two internal parts: (a) more room per place, (b) composites over two places, (c) ripples of patterned backgrounds, (d) fractionalized partons.
- (3) Check each route against the gate, A39's Theorem T, A33's Theorem C and the owner's Q3.
- (4) Give a verdict.

## 2. Answer (graded)

**Q1. The walk (EXACT; CHECKED to 1e-15).**
- It has exactly eight crossings, at k ∈ {0,π}³. The velocity matrices there are (−1)^{n_a}σ_a, which form a Clifford set.
- The hand at node n is (−1)^{n₁+n₂+n₃}, so four nodes have each hand and the sum is 0.
- The speed is exactly 1 in every direction at every node. Around every node |E| = √(Σ sin² q_a), so all eight have the same shape, including the lattice corrections. At |q| = 0.2, E/|q| is 0.9933 along (100) and 0.9978 along (111).
- The symbol is 2×2, so there are only two bands and no heavy or flat partner. The gap is at least 0.309 farther than 0.3 from every node.
- **Covariance under full soldering, with the same U(R) at every site (EXACT):** U(R)h(k)U(R)† = h(Rk), because sin(Rk) = R sin k for signed permutations. CHECKED for all 24 turns, in Bloch form and as a 128×128 operator on the 4³ torus (deviation 1.6e-16, 16 zero modes).
- It is time-reversal invariant. Its mirror image is −H, and inversion combined with the staggered sign (−1)^{x+y+z} is an exact symmetry.
- **Scope (EXACT, by Schur).**
  - At Γ and R = (π,π,π) the full group O acts, so roundness is forced.
  - At the six X and M nodes only D₄ acts, which allows two speeds (v_∥ ≠ v_⊥). Equal round speeds there are a property of the nearest-neighbour form, not of covariance.
  - The covariant scalar hop of the sibling note moves the nodes to four energy levels (1,3,3,1) without changing their local slopes.

**New lemma S: the obstruction is the spinor class, not only the count of states (EXACT).**
- **S1.** No genuine 2-dimensional representation of O has a vector among its internal operators. The multiplicity of T1 in End(D) is 0 for A1+A1, A1+A2, A2+A2 and E, but 1 for the spin-½ class. So the walk's pair must carry the spinor (projective) class, like a site's own qubit.
- **S2.** On qubits (any number per place, ordinary tensor product, soldered action), local operators carry genuine representations. So every disturbance created by local operators from any background carries a genuine representation relative to that background. At k = 0 that is a genuine representation of the point group.
  - Corollary: no local space can hold an invariant empty state next to a spin-½ doublet without a grading. The quarter-turn lift raised to the fourth power is diag(1,−1,−1).
- **S3.** Take a disturbance with a clean round crossing at Γ (H² = c²k² at linear order). Then its internal space is C² ⊗ C^m, with Γ_a = c σ_a ⊗ 1, and the turns act as U(R) ⊗ W(R) with W of the spinor class. So m ≥ 2:
  - The minimum is four internal states: the walk's pair times an inert spinor partner, with both copies of the same hand at that node. CHECKED: the volume element is +i·1.
  - Opposite hands at one point need at least 8 states.
  - Odd-dimensional multiplets always keep a partner. A spin-1 triplet has a flat band (exactly 0 to 6e-16) or a heavy one (curvature 0.47 and −0.05 for a general covariant hop).
- **Consequence.** The walk's two-part matter is never a locally created disturbance on qubits. With exactly two parts it needs either a grading (fermionic room) or fractionalization.

**Q2. Routes and their costs.**
- **(a) More room per place.** This is parked: DEFERRED_DECISIONS §4 keeps the standing default "M₂(ℂ) stands as postulated". Stated here only as named premises.
  - **P_room-g.** One place holds the Fock space of a spin-½ mode pair, with the full-turn acting as parity and a graded composition between places. This gives exactly the walk as the one-disturbance band (EXACT). Costs:
    - the domain enlargement;
    - the grading;
    - graded composition (an open owner decision on main);
    - negative energies over the empty state (A39 escape (a)), or with an on-site offset the crossings move to E = μ (A39 (a′)).
  - **P_room-u.** Two qubits per place, ungraded, give a singlet vacuum with triplet disturbances: spin-1 matter with a flat or heavy partner (EXACT/CHECKED). A clean doubled walk needs at least 5 states per place, plus a tuning or a flavour symmetry (d·σ·σ′ splits it: −0.3 versus 0.1 at d = 0.1).
- **(b) Composites over two places.**
  - Bond-centred objects can be covariant with no pattern at all, because bonds are lattice structure (EXACT).
  - Two-site cells need a pairing pattern. Put into the law, it goes against "Sites are distinguished by the supplied lattice structure alone". Held in the state, it is a 1-of-N pick.
  - Either way, two qubits carry only singlet ⊕ triplet (integer spin), so by S2/S3 they never give the walk's pair (EXACT). Bonds also come in three orientations, which gives at least 3 bands per internal state.
- **(c) Ripples of patterned backgrounds.** All of these are bosons with integer spin and no hand.
  - **Heisenberg antiferromagnet (J > 0), Néel order:**
    - 2 degenerate linear branches, ω = 12J√(1−γ²) in linear spin waves (CHECKED to 4e-14);
    - speed 4√3·J ≈ 6.928 (Pauli units), round at leading order over 66 directions, with small cubic anisotropy at |k| = 0.2 (6.905–6.913);
    - no heavy partner at Γ, and protected as Goldstone modes of the law's spin symmetry.
    - Costs:
      - It needs J > 0, whereas the calm aligned vacuum is the ground state only for J < 0 (EXACT; repo D2 note).
      - It needs an entangled vacuum: the Néel product is not stationary (pair-creation block 4.0; EXACT double-flip amplitude 2J per bond).
  - **Compass:**
    - The classical ground states form a degenerate family.
    - Uniform states (K < 0) have, in closed form, ω = 2√((Σw_a x_a)² − |Σz_a x_a|²) with x_a = 1 − cos k_a. The zero set is planes, lines, or a plane plus a line, depending on the axis. Away from these zero sets the dispersion is quadratic (EXACT; CHECKED).
    - Staggered states (K > 0) have 5–6 zero modes at Γ, zero planes and lines, and linear branches whose slopes range 1.15–3.27 with direction.
    - So there is no round cone.
  - **Moriya:**
    - The classical ground state is a period-4 spiral, q = (π/2)(±1,±1,±1), with E = −√3|D|. This is EXACT by the Luttinger–Tisza bound, and a greedy search from 6 starts agrees.
    - It has one soft branch at Γ, linear and round at leading order, slope 2√2·D (CHECKED over 66 directions). The other branches are at 6.93 or above.
    - But that branch comes from an accidental classical degeneracy (the in-plane phase, flat to 1e-12), not from a symmetry of the law. It is harmonic-order only and is expected to be gapped beyond that (ARGUED; COMPARATOR: order by disorder).
  - **What kind of light-like.** These are ω = c|k| ≥ 0 massless bosons (sigma-model Goldstones; COMPARATOR). They are not Weyl crossings: they carry no ±1 hand per node, have integer spin, and have no lower branch that needs filling.
- **(d) Partons.** σ_x = f†_x σ f_x with exactly one fermion per place, so this is literally one qubit per place.
  - The soldered hopping iλσ·e gives h(k) = −2λΣσ_a sin k_a, which is exactly the walk (EXACT).
  - At half filling the filling level sits at the eight crossings (CHECKED: 16 zero modes on the periodic 6³ torus, 208 levels below).
  - It is invariant under the 24 turns with no gauge factor (EXACT). Inversion acts together with the staggered gauge sign, which forces ⟨Moriya⟩ = 0 in the mean-field state (EXACT; 1e-17).
  - It needs:
    1. a projection;
    2. an emergent gauge field. The hopping-only form keeps at least U(1), so the spinons carry its charge; neutral spinons need breaking down to Z₂ by pairing, which is open.
    3. a parent rule, which is not identified. The unprojected per-bond energy 0.080(J−K) is far above the classical compass value −K/3 (crude; ARGUED).
    4. the covariant scalar hop t = 0, either by a tuning or by inversion with the staggered gauge, which the axioms do not include.
  - Literature (COMPARATOR, from memory): Affleck–Zou–Hsu–Anderson and Wen's projective symmetry groups; Wen (2002–03) and Levin–Wen (2005) on emergent photons and fermions; Hermele–Fisher–Balents (2004); Weyl spin liquids (Hermanns–O'Brien–Trebst 2015). I know of no cubic spin-½ model shown to realize this phase.

**Q3. Compatibility with the record-tick shape, route by route.**

| Route | (i) Gate | (ii) Theorem T | (iii) Theorem C | (iv) Q3 |
|---|---|---|---|---|
| Walk / (a)-graded | Empty vacuum: quiet product state, but negative energies. A filled sea is full rank at edges (A28 floor). | Escape (a) over the empty state; with a sea, T2 fails at edges. | Outside its class (graded). A qubit encoding brings back "more checks than qubits" (ARGUED). | Exact on the even algebra; the full turn acts as parity on the place. |
| (b) | Same as (c) | Composites: no linear bottom (A39 (c), EXACT) | Disturbances are locally creatable, so outside its scope | Holds for bonds |
| (c) Néel | Voids quiet; edges full rank (A39 c2, CHECKED) | **No contradiction.** T2 and T3 fail together (EXACT, bond grouping); the product corollary does not bind (the vacuum is entangled); T4 fails at k₀ = 0. | Magnons are locally creatable, so outside its scope | Holds for the law; the order breaks the symmetry in the state |
| (d) | Voids quiet; edges full rank (ARGUED) | Open (A39 open edge 1) | Consistent with it: superselected 3D movers need a gauge structure, here the emergent U(1) | Holds, with a trivial gauge factor (EXACT, mean field) |

**Q4. Verdict.**
- As locally created disturbances, clean round two-part crossings with one qubit per place are impossible (EXACT, lemma S).
- The cleanest local light-like ripples on one qubit per place are the antiferromagnet's two bosonic Goldstone branches. They are round and protected, but have no hand and no spinor, and cost the calm vacuum.
- The walk's exact crossings do appear, with one qubit per place, as fractionalized spinons of an entangled background. That is EXACT at mean field and COMPARATOR/OPEN as a phase. It costs an emergent gauge field (which could double as emergent light), an unidentified parent rule, t = 0, and quietness only under the gate.
- With parked graded room the walk appears directly.

## 3. Derivation per route

**Q1.**
- Writing out S_a gives the symbol Σ sin k_a σ_a. It vanishes only when every sin k_a = 0.
- At πn + q the symbol is Σ(−1)^{n_a} sin q_a σ_a. The Clifford relations give H² = Σ sin² q_a·1 exactly.
- The hand is sign det v = Π(−1)^{n_a}.
- Covariance: R is a signed permutation, so sin((Rk)_a) = (R sin k)_a, and U σ_a U† = Σ_b R_ba σ_b.
- Schur: the little group at Γ and R is O, which acts irreducibly on T1, so v ∝ 1. At X and M the little group is D₄, so v = diag(v_∥, v_⊥, v_⊥).

**Lemma S.**
- **S1 by characters.** For spin ½, |χ|² = (4,1,0,2,0), which is A1+T1. For E, End(E) = A1+A2+E.
- **S2.** Ad(±U) agree, so the action on operators is genuine. A one-dimensional projective representation of the background state can be made linear. Disturbances A|Ω⟩ therefore carry genuine representations. At k = 0, translations act trivially, so the little group's action is the point group.
- **S3.**
  - The volume element Γ₁Γ₂Γ₃ commutes with every Γ_a and is fixed by proper turns (det R = 1). So the turns preserve its ±i eigenspaces, and each block is C² ⊗ C^{m±}.
  - On each block, D(R)(U(R)† ⊗ 1) commutes with σ_a ⊗ 1, so it equals 1 ⊗ W(R). D is genuine and U is spinor, so W is spinor. There is no 1-dimensional spinor representation, so m± ∈ {0} ∪ [2, ∞).
  - An odd total dimension forces a zero eigenvalue, hence a partner.
  - Example: on two spinors, σ_a ⊗ 1 transforms as a vector under U⊗U, and its volume element is i·1.

**(a)** Covered in §2 and S3. The graded place realizes the second-quantized walk directly. Graded composition is the open composition question (repo MG and RL notes). A1 D28's one-qubit grading breaks O to D₄, but the grading here is the full-turn parity, which is O-invariant.

**(b)** Translations and the 24 turns about a site permute the bond set. The bond stabilizer includes the end-swap. Content: 1/2 ⊗ 1/2 = 0 ⊕ 1. By S3 the triplet's helicity-0 state always gives a partner.

**(c) against Theorem T (settled exactly where possible).**
- Shifted bond terms are h_b = J(σ·σ + 3) = 4J·P_triplet(b) ≥ 0.
- By A39's Lemma V, T2 and T3 together imply h_bΩ = 0 on every bond, so every bond would be a singlet.
- That is impossible: if (x,y) is a singlet, then ρ_xz = ½·1 ⊗ ρ_z, and ⟨P_triplet(x,z)⟩ = 3/4 (EXACT). So either the weights fire in the vacuum, which the gate may permit in voids, or they do not see the bond energy (escape (e)).
- The product corollary does not bind, because B ≠ 0 (A31 D3).
- T4 fails at k₀ = 0: the ground state of a finite even torus is a singlet (Lieb–Mattis, COMPARATOR), so S⁺_tot Ω = 0 and S(k) → 0. At k₀ = Q the twist is not a zero mode.
- For other groupings, a full-rank vacuum would exclude every quiet weight. That is CHECKED only in A39's 1D/2D toys, so it stays ARGUED in 3D.
- Compass has no z = 1 branch at long wavelength, so there is nothing to reconcile. Moriya's branch sits on an entangled vacuum (B = 2.9) and is unprotected.
- **Compass closed form.**
  - A = 2Σw_a x_a and B = 2Σz_a x_a, with w_a = 1 − m_a², z_a = (e^a)², |z_a| = w_a and Σz_a = 0.
  - So ω = 0 exactly where the active z_a share one phase.
  - Axis: planes k_x = 0 and k_y = 0. Body diagonal: the three axis lines. Face diagonal: the plane k_z = 0 plus the line k_x = k_y = 0.
- **Moriya.** Λ(q) = iD[sin q]_×, whose lowest eigenvalue is −|D||sin q| ≥ −√3|D|. A single-q spiral reaches this bound with unit length, so it is a ground state.

**(d)**
- Under a turn, u = iλσ·e → U(iλσ·R⁻¹e)U† = iλσ·e, so no gauge factor is needed.
- Inversion maps u to −u. The staggered gauge f_x → (−1)^x f_x restores it, and leaves every σ_x unchanged. The combined map is a mean-field symmetry that reverses the Moriya operator, so its expectation is zero.
- The scalar hop t·1 is allowed by the bond stabilizer (span{1, σ·e}). This combined map flips t, so t = 0 is forced only if inversion is included.

## 4. Checks (all in `SP/c8/A43/`, with outputs in `out_*.txt`)

| Script | Key results |
|---|---|
| `w1_walk_and_reps.py` (0.3 s, 49 MB) | Lift error 3e-16. Eight nodes with Clifford defect 0, slopes ±1.00000000 in 300 directions, hands [+,−,−,+,−,+,+,−]. Shape deviation 4e-16. Bloch covariance 8.5e-16, real-space 1.6e-16, 16 zero modes; inversion, staggered-sign and time-reversal identities exact. Class sizes [1,8,3,6,6]; the T1 multiplicities above. Spin-1 flat band 6e-16; triplet heavy partner. A1⊕T1 Clifford at \|a\| = \|γ\| (1.8e-15), volume element +i·1; walk⊗spinor covariance 1e-15. |
| `w2_lswt.py` (10.5 s, 35 MB) | Ferromagnet control has exponent 2.00. Néel: 2 zero modes, slope 6.9282 in all 66 directions, B = 4.0. Compass and Moriya as in §2; all backgrounds stable (lowest BdG eigenvalue > 0). |
| `w3_followups_and_parton.py` (2.2 s, 60 MB) | Néel closed form to 3.6e-14. Spiral: zero modes only at Γ-equivalent points, phase degeneracy to 1e-12, greedy search −1.73205. Partons: as above. |

**Superseded runs, recorded honestly.**
- The first `w2` run hit the 28 s cap with no output (20³ grid). It was rerun at 10³ with unbuffered output.
- `w2`'s line comparing against 24√(1−γ²) used my own factor-2 slip; the run caught it, and `w3`(i) replaces it.
- `w3`'s singlet-ansatz line is discarded: the degenerate Fermi shell at finite size gives ⟨σ⟩ ≠ 0.

## 5. Open edges

1. Is there a parent rule for (d)? Next step: Gutzwiller-projected energies (variational Monte Carlo) for the soldered ansatz under (J, K, D) plus star terms, and whether the hopping-only U(1) structure survives. Is there a Z₂ version with neutral spinons?
2. Does a frustration-free vacuum with no zero-mode twist admit z = 1 (A39 open edge 1)? This decides (ii) for route (d).
3. How large is the Moriya spiral's gap from order by disorder? Do helices of J + D behave the same way (helimagnons are anisotropic; COMPARATOR)?
4. Can a nonsymmorphic patterned background give clean crossings at zone-boundary points? S3 binds only at Γ; A38's 8-fold corner point is the precedent, and it was not clean.
5. Is the antiferromagnet's vacuum full rank on 3D stars? This is not proved.
6. Graded composition and the parked §4 premise interact; that is an owner decision, framed here, not taken.
7. **Correction for G5 row R3.** "It needs more than one qubit's worth per place" is too strong. As a locally created disturbance it needs a grading, or an inert spinor partner with at least 5 states per place. With one qubit per place it can appear only fractionalized.

## 6. Plain-language summary

The two-part walk really does have eight perfectly round crossings, four of each hand, all at the same speed, and it treats every turn of the grid alike. But I proved that its two internal parts belong to the "half-turn" kind of object: one full turn of the grid flips their sign. A disturbance made by acting locally on ordinary qubits can never be of that kind, however many qubits each place holds. So with one qubit per place there are only two ways in. One is the "magnet" kind of ripple: these move at one speed in every direction when neighbours prefer opposite settings, but they have no handedness, and that preference rules out the calm, all-aligned empty background. The other gives the walk's exact crossings, but only as half-pieces of a highly entangled background that carries a hidden field of its own (which might itself act like light); nobody yet knows a rule that produces that background, and empty space stays quiet only if records form solely next to other records.