I ran out of the time box before writing a separate report file; the notes in `NOTES.md` hold the derivations piece by piece. Here is the report.

# A50 report: non-Pauli dressings and lemma F

## 1. Verdict
- **Product dressings with arbitrary single-qubit unitaries do not evade lemma F under the 24 turns.** I proved a stronger lemma, F″ (EXACT within class): every T-junction phase θ(δ, −δ, ε) is +1 for any finite window. The census and the continuous searches found no exception.
- **One non-product composite does evade lemma F's T-junction statement, but it does not give a fermion.** It is a corner qubit rotated by a link-controlled Pauli, plus CZ phases between link fields. It is covariant under all 24 turns and makes all 12 T-junctions −1 (CHECKED). Every corner junction (three mutually perpendicular legs) is then non-scalar, so the charge has no consistent exchange statistic.
- **One half-turn alone gives θ² = 1 for arbitrary hops and nothing more** (EXACT). Both signs occur, and the {1, C2z} control reaches −1 on all 20 junctions.

## 2. Question
Under the exact soldered action (owner reading Q3), lemmas F and F′ give bosonic charges (θ = +1) when the hop dressings are Pauli monomials. The question was whether non-Pauli dressings evade this, through:
- arbitrary unitary hops under one half-turn;
- product dressings under all 24 turns;
- simple non-product composites.

## 3. Answers

### Task 1: one half-turn, arbitrary unitary hops (EXACT)
- **Configuration hexagon.** With two charges among {v, end₁, end₂, end₃}, the six configurations form one 6-cycle: 01–12–02–23–03–13–01.
- θ(1,2,3) is the holonomy of that hexagon.
  - If it is scalar at one base point, it is the same scalar everywhere.
  - Cyclic reorderings of the legs give the same value. Transpositions run the loop backwards and give θ⁻¹. This needs no symmetry.
- **Covariance under C (the half-turn about ε through v).**
  - C swaps legs ±δ and fixes leg ε, so Ad(U_C) maps the holonomy for (δ, −δ, ε) onto the hexagon traversed backwards.
  - Hop phases cancel, because each hop appears once and so does its adjoint.
  - Gauss-type factors cancel too. Tracking the transformed word step by step, every one acts on a configuration with v empty, and each appears with opposite powers.
  - So θ(δ, −δ, ε) = θ(δ, −δ, ε)⁻¹, hence **θ² = 1**.
- **Nothing further.**
  - +1 is trivial.
  - −1 is the {1, C2z} control (Task 2d).
  - Control for the symmetry's role: with no symmetry, U(1) link-phase dressings give θ = (r₁₃r₃₂r₂₁)/(r₃₁r₂₃r₁₂). Here r_jk is the phase ratio of hop j's dressing on leg link k. One generic instance gave −0.6056 + 0.7957i, matching the formula (CHECKED). C forces this to 1.

### Task 2(a): per-place conditions (EXACT)
- **Non-link places.** These carry a free qubit, so scalar products need every per-site word W_x = u_i†u_j u_k†u_i u_j†u_k to equal λ_x.
- **Equivalent form.** XY = λ_x YX, with X = u_i u_j† and Y = u_k u_j†.
  - For a qubit, the determinant forces λ_x = ±1 automatically.
  - In SO(3), the relative rotations must commute; λ = −1 exactly when they are perpendicular half-turns.
- **All 20 triples scalar at one place** means the six rotations lie in a coset of an abelian subgroup:
  - SO(2) about one axis: all λ = +1;
  - or a Klein group: rotated Paulis times a common right factor.
- **Links.** Preserving Gauss's law forces field-diagonal factors off the hop's own link (the window has no closed flip loops). Their total contribution is the r-formula above.
- **Swapped pairs.** λ_{Cx} = λ_x⁻¹, because the word at Cx is a cyclic rotation of the inverse word at x.

### Task 2(b): Lemma F″ (EXACT within class)
**Class.**
- Any finite window.
- Arbitrary single-qubit unitaries on non-link places; field-diagonal factors on links.
- Covariant under the 24 turns up to phases and Gauss factors.
- One T-junction product scalar. The 12 T-junctions form one orbit under the 24 turns, so then all are scalar.

**Claim.** θ_T = +1.

**Proof.**
1. θ = Φ_links · ∏λ_x. Swapped pairs cancel, and Φ_links = 1 under C. What remains are the C-fixed corners v + 2kε.
2. **The corner v.** The turns fixing leg δ include the 90° turn C4δ, so u_δ(v) rotates about δ. Scalarity then forces the angle to be 0 or π, giving λ_v = +1. At 90°, X is a half-turn but Y is a 120° turn.
3. **The far pair x = v + 2kε and x′ = v − 2kε.** C2δ gives λ_{x′}(δ, −δ, ε) = λ_x(δ, −δ, −ε). I proved an identity: the pair product equals the commutation sign s(P_δ, P_ε), where P_δ = u_δu_{−δ}† and P_ε = u_εu_{−ε}† at x.
   - C2ε fixes x, so P_ε lies in O(2)_ε and P_δ = C2_{Aε}·C2ε, where A = u_δ(x).
   - A sign of −1 needs Aε ⊥ ε, with P_ε equal to C2ε or C2_{Aε}.
   - Scalarity of the collinear-ε junction (ε, −ε, δ) at x contradicts both options.

So each pair gives +1, and θ_T = +1. ∎

**What is load-bearing.**
- The far-pair cancellation uses only the three axis half-turns (D2), so it holds already under D2 (EXACT).
- Only step 2, the corner v, uses the 90° turns.
- Why Pauli-only reasoning missed nothing here: the far corners have independent rotation angles for the ±ε hops (non-Pauli freedom). Taken alone, (δ, −δ, ε) can be −1 there, but the collinear-ε junction rules that out.

### Task 2(c): census, 27-place window (CHECKED)
1,500 seeds per mode; half the samples also carry random Gauss factors.

| Group | T-scalar samples | T-junction phases | Corners (all-20-scalar samples) |
|---|---|---|---|
| O | 1,014 | all +1 | 265 all −1, 746 all +1 |
| T | 890 | all +1 | mixed |
| D2 | 460 | +1, or mixed (some −1); never all 12 = −1 | mixed |
| {1, C2z} | 174 | generic phases on unpaired junctions; −1 on paired ones | mixed |

- Random continuous seeds were never scalar (0 of 1,500 per mode, all groups).
- **Continuous search** (Levenberg–Marquardt over non-Clifford seeds on the axis places), as a falsification test of F″:
  - **O, far corners, no target:** 30/30 scalar optima, all +1.
  - **O, far corners, target θ_T = −1:** 0/30 reached it. The best residual is √48, which is exactly all 12 T-junctions stuck at +1.
  - **O on v + links; T and D2 with an all-12 target:** none reached −1.
  - **D2, target on one junction orbit only:** reachable on v + links (some T-junctions −1, the rest +1). This is not a consistent statistic.
- **Side finding (CHECKED).** Under O, 265 product-dressing samples have every corner junction at −1 while every T-junction is +1. The sign depends on the junction's geometry, so it is not a fermion.

### Task 2(d): control (CHECKED)
The same search under exact {1, C2z} on v + links:
- **Target all 12 T-junctions:** 11 of 25 starts reached all 12 at −1.
- **Target all 20 junctions:** 6 of 25 starts reached all 20 at −1, with non-Clifford vertex factors and continuous link angles.

This matches A48's escape. That escape is itself a frame change of exactly this kind of non-Pauli dressing (A48's Corollary 3).

### Task 3: non-product candidates (CHECKED, dense 7 qubits)
- **SWAP-type** (t_j = O_j ⊗ SWAP(v, v + 2d_j)).
  - Covariant under the 24 turns automatically.
  - The holonomy is exactly SWAP(v, e₋ₓ)·SWAP(e₊ₓ, e₊_z) on its support (residual 0; eigenvalues +1 ×10 and −1 ×6). It is not a scalar, so θ is undefined.
  - ARGUED: these are bosons carrying an internal qubit (exchange = +SWAP). A fermion would need −SWAP.
- **CZ-type** (t_i = O_i ⊗ exp(i Σ_m κ_m P_m ⊗ s_m σ^{a_m}_v) ⊗ CZ phases between link pairs, covariant under the 24 turns).
  - My first build failed its covariance check (residual 0.87): the non-commuting factors were multiplied in index order. The fixed build passes at 2.7e-15.
  - Of 18 parameter sets, 14 are not scalar and 3 give T = +1.
  - **One gives all 12 T-junctions = −1** (T residual 3.6e-15):
    - κ_opp = π/2 (a controlled iσ on the corner qubit, controlled by the opposite link);
    - κ_perp = 0;
    - CZ(π) between perpendicular link pairs.
  - In that set every corner junction is non-scalar (residual 1.000), so there is no consistent statistic.
  - ARGUED: purely diagonal field-controlled phases on the links give θ_T = +1 under one half-turn (the phase sum cancels by C-covariance).

## 4. Methods
- **Covariant hop sets.** Seeds are placed on orbit representatives of the seed leg's stabilizer. Each seed lies in the commutant of its place's stabilizer: rotations about the axis for C4, rotations about the axis or half-turns perpendicular to it for C2. Link seeds are field-diagonal. Seeds are carried by the exact SU(2) lifts.
- **Phases.** θ = (link part on the six leg links, 64 dimensions) × ∏(per-site λ). Per-site words are vectorized.
- **Searches.** Levenberg–Marquardt on the non-scalar residuals plus the target terms, from random starts, with only the seeds feeding the chosen places free.
- **Composites.** Dense 128×128 operators.

## 5. Checks
All runs went through `run.sh`: load 2.1–3.8, free memory 32–40%, NUMLOCK, nice 10, BLAS 1, alarms ≤ 285 s.

| Script | Wall time | Peak RSS | Key numbers |
|---|---|---|---|
| t0_sanity | 3.6 s | 36 MB | own-link transport 2.9e-16; covariance ≤ 1.1e-15; factorized = state-vector θ on 298 junctions (13 qubits), 6.7e-15; no-symmetry control matches |
| t2_census O / T / D2 / C2z (1,500 per mode) | 20 / 21 / 27 / 32 s | 36 MB | table above; covariance ≤ 1.3e-15 |
| t2_search (13 runs) | 0.4–96 s | ≤ 79 MB | as listed in 2(b) and 2(d) |
| t2_search C2z far / axis (52–76 parameters) | killed at 285 s | 80–82 MB | no output; superseded by the v + links runs |
| t3_composite | 2.3 s | 44 MB | as listed in Task 3 |

## 6. Open edges
1. **The CZ-type composite is the live lead.** Its corner junctions are non-scalar on the full space. A constraint involving the corner qubit (stabilized corners, or corner qubits in Gauss's law) might make all 20 junction products scalar on the constrained subspace. That would be a fermion candidate with one qubit per place. Not tested.
2. **Under the 12 even turns (T), at v:** no proof for non-Pauli factors; CHECKED only.
3. **Closed flip loops (Wilson-loop dressings)** with non-Pauli factors lie outside the class here.
4. **The corner-versus-T sign split** in product dressings (−1 at corners, +1 at T-junctions) has no physical reading yet.
5. **Link consistency** (t₋δ at v + 2δ ∝ t_δ† under translations) was not imposed. It would only shrink the classes considered.

## 7. Plain-language summary
I asked whether dressing a charge's hops with arbitrary single-qubit rotations, not just Paulis, could make the charges fermions under the 24 turns. It cannot. I proved that every T-shaped exchange gives +1, and searches over continuous rotations found no exception. Dropping to one half-turn does allow −1, which confirms the searches can find it when it exists. One richer composite reaches −1 for every T-shaped exchange: the corner qubit is flipped depending on the opposite link's field, and perpendicular links get controlled phases. But its exchanges through three perpendicular legs are then not simple phases, so it is not a fermion either. That composite is the best lead for further work.

Files are in `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-focused-noyce-9a3983/34c0b720-f781-4af0-9bb7-5d2e1b60d22e/scratchpad/c8/A50/`:
- NOTES.md
- a50lib.py
- t0_sanity.py
- t2_census.py
- t2_search.py
- t3_composite.py
- out_*.txt and time_*.txt