All three scripts ran cleanly through the gated runner. One more by-hand check is needed before writing: whether A45's quarter-phase control is a legitimate looser action. On a fixed qubit the twisted half-turn is S = R(z, π/2)·R(z, π) = R(z, 3π/2), so S² = R(z, π) ≠ 1. That breaks C2z² = 1, so the control is not a group action. Here is the report.

# A48 report: exact turns versus turns up to a local relabeling

This message is the full report. I did not write `REPORT.md`.

## 1. Verdict

- **The looser reading has two different halves (EXACT).**
  - **A fixed relabeling pattern.** "Exact turns up to one fixed relabeling at each place" (for example A44's Klein map) is the exact-turn reading in disguise. Laws, spectra, junction phases and condition-set menus all carry over unchanged.
  - **Undoing the turn.** Everything genuinely new comes from relabelings that undo the possibilities' turning, so a place's possibilities stop turning with the grid, wholly or partly. For the sign pattern it also needs translations that compose only up to the charge parity.
- **Lemma F survives every version (EXACT within its class; CHECKED).** With one qubit per place, light's point charges with Pauli-monomial dressings are never fermions under any looser action that keeps the three axis half-turns about the charge's corner.
  - A single half-turn is not enough. Under {1, C2z} alone a fully fermionic, covariant hop set exists (control).
  - So the looser reading raises lemma F's symmetry requirement from one half-turn to three; it does not remove the obstruction.
- **Decision 28's first two costs disappear only under the "undo the turn" half** (plus projective translations for the sign pattern). Under a fixed relabeling of exact turns, all three costs stand.

## 2. Question

Decision 28 asks whether turns are exact (Q3) or exact only up to a local relabeling at every place. The lane:
- makes the looser reading precise and classifies it;
- redoes lemma F under it;
- checks the claims that the sign-pattern cost (§10) and the one-part charged-hop cost (§14) disappear;
- states what each reading buys and costs.

Q3 stands. The looser reading is explored as a supplied alternative only.

## 3. Answers

### Q1. What the looser reading is (EXACT unless marked)

**Definition.**
- A looser action gives each grid symmetry g a map β_g = (⊗ₓ Ad u_g(x)) ∘ α_g, where α_g is the exact soldered action.
- On place y this is an on-site rotation S_g(y) ∈ SO(3) = Aut(M₂(C)).
- "Group law up to phases" for the unitaries means an exact group law for the β's: S_gh(y) = S_g(y)·S_h(g⁻¹y).
- "Up to Gauss-law factors" means β_gβ_h = Ad(product of Gauss operators)·β_gh. I treat it as a separate, relaxed variant.

**Theorem 1 (reduction).**
- Every looser action of the full grid group (translations plus the 24 turns about each place) is a frame change V β^ρ V⁻¹ of a uniform action β^ρ.
  - In β^ρ, translations are pure shifts and every turn rotates every place by ρ(its linear part).
  - ρ: O → SO(3) is a homomorphism, fixed up to conjugation.
  - The frame is V_y = S_{t_y}(y), and ρ(k) = S_k(0).
- Proof: a Shapiro-type argument; the reconstruction formulas are verified directly.
- On the coarse grid of the 2×2×2 role pattern the same holds orbit by orbit:
  - corner and cube-centre places have stabilizer O: 4 classes each;
  - edge and face places have stabilizer D₄: 6 classes each.

**Theorem 2 (the classes).** Hom(O, SO(3)) up to conjugacy has exactly four classes:

| Class | Characters | What the turns do to a place's possibilities |
|---|---|---|
| Trivial | A1³ | Nothing |
| Sign twist | A1 + 2A2 | Odd turns act by one fixed half-turn |
| Axis soldering | A2 + E | Through O → S₃ ≅ D₃ |
| Soldered (Q3) | T1 | Exact turning |

- All four are realised by Pauli-preserving relabelings. There are 58 homomorphisms into the 24 Clifford rotations: 1 trivial, 9 sign twist, 24 axis soldering and 24 soldered, and the soldered ones are exactly the conjugates of the identity.
- These are the four actions main already lists.
- For comparison: the 12 even turns (T) have 3 classes and the link stabilizer D₄ has 6.

**Corollary 3 (frame changes against genuinely new actions).**
- **Frame changes of Q3.** A law H is covariant under β = Vα V⁻¹ exactly when V†HV is Q3-covariant. V is on-site, so spectra, entanglement, Levin–Wen phases, locality and condition-set menus are identical. Only objects pinned to a fixed basis can tell the difference, such as "Pauli-monomial dressings" or a fixed readout basis.
- **Example: the Klein frame (CHECKED, 8³).** All its twists are Pauli relabelings. In that frame the 24 turns about the origin act exactly, and each unit translation along e_a comes with a uniform half-turn about a at every place. The apparent pattern (KS-type staggered couplings, A44's duals) is entirely the frame.
- **Genuinely new actions** are the three non-faithful classes, in any frame. They are uniform and carry no pattern. What they change is that possibilities stop turning with the grid, wholly or partly.

**Corollary 4 (projective translations).**
- With the exact group law, twisted translations are frame-conjugate to pure shifts. They commute, and on-site phase defects can always be removed.
- The spinor class of the soldered lift (the ±iσ half-turns) is invisible on the algebra and is already present in Q3.
- A genuinely projective translation algebra, with twisted translations commuting only up to a global symmetry of the law such as (−1)^N, needs the relaxed group law. When matter is gauged, (−1)^N is a product of Gauss operators.

**Answer to "is the looser reading the same as letting the law carry a pattern?" No.**
- With the exact group law it allows only on-site frame patterns, which carry no physics, plus ungluing, which is uniform.
- Laws whose places are physically different (a 2×2×2 pattern of coupling strengths, or a mass pattern that is not a relabeling) stay excluded.
- With the relaxed group law it also allows a uniform background flux of a global symmetry, which is exactly the π-flux/KS case. That is a "pattern in the law" only in the gauge sense: every plaquette carries the same flux.

### Q2. Lemma F under the looser reading: **No fermions (EXACT within class; CHECKED)**

**Lemma F′.**
- **Setting.**
  - One qubit per place, and lemma F's hop class.
  - One-link hops O_δ ⊗ D_δ, with D_δ a Pauli monomial in one fixed Pauli frame and the opposite-link factor 1 or field-type.
  - An exact U(1) or Z₂ Gauss law on the links.
  - The hop set is covariant up to phases and endpoint Gauss parities under any looser action: exact group law, or group law up to Gauss factors.
- **If the action includes the three axis half-turns about the corner v,** the charges are not fermions.
- **If it also includes the 90° turns or the 120° turns,** every T-junction phase θ(δ, −δ, ε) is +1.

**Proof sketch.**
1. **The junction phase.** Let C be the half-turn about ε through v. Then θ(δ, −δ, ε) = s(t_δ, β_C t_δ). The Gauss-parity exponent c′ = 0 is forced on the link ℓ₋ε, because no on-site map turns 1 into σ^ε.
2. **Swapped places cancel.** For a pair (x, Cx), the group law gives M at x and M⁻¹ at Cx. The pair contributes s(A_x, M A_Cx)·s(A_Cx, M⁻¹ A_x) = +1. This also holds up to Ad(σ^f) Gauss factors. So only places on the ε-axis count.
3. **Links on the axis.** The action must keep each link's field axis, for Gauss covariance with charges mapped to charges.
   - U(1) factors are field-type, so they give +1.
   - Z₂ transverse factors could give −1 only when M is a 90° turn about the link. The 90° grid turn then maps them off the Pauli axes, and the pairing in step 4 cancels them anyway.
4. **Other places on the axis.**
   - *With 90° turns:* the 90° action N satisfies N² = M, with N⁴ equal to 1 or to a half-turn about a Pauli axis. If a, Na and N²a are all Pauli axes, the angle between a and Na has cos = (n·a)² ∈ {0, 1}, so N²a ∥ a. The fixed-place factor commutes with its image.
   - *With the half-turn about δ:* it fixes t_δ and maps v + kε to v − kε. The group law makes the two contributions equal, so they cancel.
5. **The corner's own qubit.** Its factors p(δ) are Paulis, so any two are parallel or perpendicular.
   - Fermionic T-junctions need p(e_x) at 45° to the axes of both ρ(C2y) and ρ(C2z), and likewise for p(e_y). If ρ is faithful on D₂, that forces p(e_x)·p(e_y) = ±½, which is impossible. If ρ is not faithful, some ρ(C2b) = 1 and those junctions are +1.
   - With 120° or 90° turns, the factors of one hop and its image would be 60° apart, so every T-junction is +1.

**The obstruction in one sentence.** The fermion sign needs a place on a half-turn axis where the looser half-turn swaps two Pauli directions. No 90° turn about that axis can keep such a factor Pauli. Without 90° turns, the half-turn about the hop's own axis cancels such places in pairs, except at the corner itself, where two hops would need Pauli factors 60° apart.

**Correction to A45's control.** "C2z with an extra quarter phase on fixed qubits" (1483/3000 anticommuting) is not a legitimate action: S² = R(z, π) ≠ 1 on fixed qubits. A legitimate single-half-turn action (a half-turn about a 45° axis) does give fermions; that is my control.

**Smallest construction.** None exists in the class. The positive control under {1, C2z}:
- On the vertex qubit, C2z acts by the half-turn about (e_y + e_z)/√2.
- The vertex factors are Y, Z, Y, Z, I, I for hops +x, −x, +y, −y, +z, −z, with link decorations from the census.
- All 20 junction phases are −1 and the covariance residual is 2.4e-16.
- No Clifford 90° or 120° vertex action extends it (0 found).

### Q3. Decision 28's first two costs

**(i) "The painted sign pattern keeps all 24 turns": CORRECTED (true only under the ungluing version, with a caveat for translations).**
- **Each symmetry individually: CHECKED, 4³ torus.** With Z relabelings (c → −c on a pattern of places), all 24 turns about a place and all unit translations are symmetries of the KS signs. Without relabelings, only 4 of 24 turns about the origin keep the signs.
- **Turns about one place compose exactly: CHECKED.** All 576 composition defects are +1, W_a⁴ = W_b³ = (W_aW_b)² = 1, and the turn–translation relations are exact.
- **Unit translations: EXACT (π flux), CHECKED.** Their relabeled versions anticommute: T_xT_y = −T_yT_x for all three pairs.
  - Turns about all places generate such translations, so for the whole grid the reading needs the relaxed group law (up to the charge parity).
  - Period-2 translations commute, so the 2×2×2 coarse group acts exactly.
  - Tying the pattern to the role layout keeps the 24 turns about corner places with an exact group law (CHECKED for the origin plus period-2 shifts). Turns about cube-centre places: ARGUED.
- **The possibility axis.** "All 24" holds only if the matter's possibilities do not turn.
  - Under relabelings of exact turns, the hop-only form keeps at most 8 of 24 turns about any place. EXACT: the only conserved one-site charge of an XY bond is the matter number (null-space dimension 1), and a soldered turn must keep that axis at its centre. CHECKED: no axis is kept by more than 8 turns.
  - The glued form is not covariant at all. The spectra {−3, 1, 1, 1} of σ·σ and {−1, −1, −1, 3} of −σ·σ differ (as in A31).

**(ii) "The one-part charged hop becomes possible": CONFIRMED only for genuinely new link and corner actions; FALSE for relabelings of exact turns.**
- **Impossible under Q3 and every fixed-frame relabeling (EXACT; CHECKED).**
  - The 90° turn about a link's own axis fixes the link and both corners.
  - It multiplies the link's outward raising operator by −i. This holds exactly and for 200 random non-Clifford frames (to 4e-16), because it is an eigenvalue.
  - The corners' single charged states contribute χχ* = 1 and Pauli dressings contribute ±1, so κt + h.c. becomes −iκt + h.c. The hop is not covariant.
  - One qubit per corner has no turn-invariant charge axis at all.
- **Possible under a link action where links turn only as wholes (EXACT; CHECKED).**
  - The outward raising operator maps to the image link's outward raising operator with no phase: the link's stabilizer acts by C4 ↦ 1 and reversal ↦ a perpendicular half-turn, which is non-faithful and so genuinely new.
  - The corners carry the trivial or sign-twist action, the only option with one qubit per corner.
  - With these, t_δ = σ⁺_v O_δ σ⁻_{v+δ} is covariant under all 24 turns. The group-law residual is 0 and the phases are all 1.
  - The Gauss law holds exactly: ‖[G, t]‖ = 0 at both ends. The ring term stays covariant; it is covariant under exact Q3 too (phase 1).

### Q4. Bottom line: what each reading buys and costs (no recommendation)

| Reading | Buys | Costs |
|---|---|---|
| **Q3, exact turns** (decided) | Full gluing. One way to get A42's hard limit. The spinor class that partons use | The sign pattern keeps 8 of 24 turns (hop-only form), or none (glued form), or 12 when tied to the layout. No one-part charged hop through spin-½ links. Light's charges are bosons |
| **Q3 up to a fixed relabeling pattern** | Nothing new. It only changes how laws look (for example, soldered partons appear as π-flux) | Nothing new. All three costs stand (EXACT) |
| **Turns that may undo the possibilities' turning** (trivial, sign-twist or axis action at some places), exact group law | Covariant one-qubit charges. The one-part hop. The KS pattern with all 24 turns about a place, and the 2×2×2 shifts | Those places' possibilities no longer turn with the grid: a privileged possibility axis, a step back from Q3 itself. Under A42's no-gluing or sign-twist actions, next-door spreading exists but favours directions |
| **As above, plus a group law up to the charge parity / Gauss factors** | KS for unit translations: the law carries a uniform background π flux | Turns and translations act on the possibilities only projectively. They are exact on charge-neutral and gauge-invariant operators |

**Under every reading,** light's charges with simple dressings stay bosons when each place holds one qubit. Electron-like matter still needs one of these:
- state-held patterns;
- partons (A47's energy contest failed);
- non-monomial hops;
- more room (parked).

## 4. Methods

- **Algebra.**
  - Cocycle reduction (Shapiro-type).
  - Real character tables with determinant bookkeeping for O, T and D₄.
  - Commutation-sign calculus for Pauli-type hops: θ = s₁₂s₁₃s₂₃.
  - An angle lemma for square roots of half-turns.
- **Censuses.**
  - All homomorphisms from the symmetry group about v into the 24 Clifford rotations, for O, T, D₂ and {1, C2z}.
  - Vertex-qubit factors covariant under each such action, combined with A45's GF(2) link-decoration system (with Gauss-parity switching).
  - Far corner places v ± 2e_a with induced looser actions.
- **Dense checks.**
  - 7-qubit Levin–Wen junction phases for random looser O-actions with random covariant dressings.
  - The {1, C2z} escape, run as a control.
- **KS one-particle tests (4³ torus).** Z relabelings solved by GF(2) for the 24 turns, the translations and the period-2 translations; composition defects and the projective-class invariant λ₁³λ₂⁴λ₃⁻⁶.
- **One-part hop.** SU(2) conjugation phases, random-frame invariance, an explicit looser frame field, and a dense 3-qubit Gauss-law check.

## 5. Checks

All runs went through `run.sh`: load 1.5–2.0, free memory 33–35%, the shared lock, `nice` 10, BLAS = 1, and alarms of at most 280 s.

| Script | Wall time | Peak memory | Key numbers |
|---|---|---|---|
| `q1_classify.py` | 0.40 s | 36 MB | O: 4 classes; T: 3; D₄: 6. 58 Clifford homs O → rotations: 1 / 9 / 24 / 24. Reduction residuals ≤ 1.7e-15; non-cocycle control 2.82. Klein twists all Pauli; translation twists uniform (e₁: diag(1, −1, −1)) |
| `q2_lemma.py` (final run) | 4.43 s | 37 MB | Fixed-place lemma: 0 of 48 Clifford cases; 0 of 120 non-Clifford cases. Control: half-turns alone give 12 anticommuting cases. Vertex census, fermion-consistent: O 0/124, T 0/132, D₂ 0/1600, {1, C2z} 96/1408. Far places: O 0, T 0. {1, C2z} control: 5376/25600. D₂ pairing: net −1 in 0/40. Dense check, 48 random looser O-actions (all four classes): covariance 2.7e-15, T-junctions +1 in 576/576 (corners mixed ±1). {1, C2z} escape: 20/20 junctions −1, covariance 2.4e-16, 0 Clifford C4 or C3 extensions |
| `q3_costs.py` | 0.31 s | 38 MB | KS: all 24 turns and 3 unit translations solvable with Z relabelings; 4/24 without. Turn defects all +1; invariant +1. T_aT_b T_a⁻¹T_b⁻¹ = −1 (all pairs); period-2 commutators +1. XY null space dim 1 (σᶻ_x + σᶻ_y); max turns keeping an axis 8. Link 90° phase −i (exact and 200 random frames, residual 4e-16). Looser link action: group law 0, phases 1. Gauss ‖[G, t]‖ = 0. Ring phase 1 under Q3 |

Files are in `SP/c8/A48/`: `a48lib.py`, `q1_classify.py`, `q2_lemma.py`, `q3_costs.py`, with `out_*.txt` and `time_*.txt` for each. A first run of `q2_lemma.py` (4.44 s, 40 MB) gave the same census numbers; its control slot was empty, which led to the {1, C2z} control above.

## 6. Open edges

1. **More room (parked).** With two qubits per place the angle lemma fails. For example, Ad(SWAP·(H⊗1)) has N⁴ = 1 and N²(X₁) = Z₁ (ARGUED by hand). Escape (d) may reopen with more room, whereas lemma F under exact Q3 holds for any room.
2. **Outside the class.** Non-monomial hops (partons) and charges with an internal frame are untouched, as in A45.
3. **Matter qubits in the Gauss law** (standard Z₂ gauge theory with matter): bosons by the same steps (ARGUED, not run).
4. **Turns about cube-centre places with the KS pattern tied to the layout:** exact group law ARGUED (body-diagonal shifts enclose an even flux), not run.
5. **Theorem N** (the hard limit) under the "undo the turn" reading was not re-derived here; A42 covers the trivial and sign-twist actions.

## 7. Plain-language summary

"Turns up to a local relabeling" can mean two things. If the relabeling is one fixed pattern, nothing physical changes: it is the same as exact turns written in different labels, and all three of decision 28's costs stay. The costs of the painted sign pattern and of the simple charged hop disappear only if the relabeling may undo the turning, so some places' possibilities stop turning with the grid. For the sign pattern, the sideways steps must also combine only up to an overall sign. The third cost does not go away under any version: with one qubit per place and simple ways of dressing hops, light's charges always behave as bosons, never as electrons. This holds whenever the grid's three straight half-turns about each corner are kept. With only one half-turn kept, electron-like charges become possible.