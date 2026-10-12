# Lane RM, probe M1: composites, two-particle continua, and integrable lattices

**Provenance.** Worker: Claude Opus 5.5 (same family as the supervisor). Ran 17:10Z to about 17:40Z on 2026-10-11. Not refereed. No repository files were edited.

**Scratch folder:** `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C4/M1/`

| Script | Output | What it does |
|---|---|---|
| `m1_twobody.py` | `m1_twobody.out` | Exact two-body bound bands on Z^d (d = 1, 2, 3). Lattice-KG constituents ε = √(m² + Σ2(1−cos k)), so β = 1. Contact attraction U, solved with the Green function 1/U = G_Q(E). |
| `m1_nbody1d.py` | `m1_nbody1d.out` | N = 2, 3, 4 clusters on Z, in a truncated relative box (the fibre stays exactly 2π-periodic). XXZ n-magnon strings against the exact formula. |
| `m1_fibre_bracket.py` | `m1_fibre_bracket.out` | The two-particle sector fibre by fibre: the first-moment K, P = i[H,K], C = [H,P] and D = i[K,P] + βH as exact finite matrices. Bound-state leakage, Hellmann–Feynman check, fibre norms against R. |
| `m1_integrable_boost.py` | `m1_integrable_boost.out` | Exact Pauli-string algebra on the infinite chain: [H,P] and i[K,P] for XX, XXZ, TFIM and XXZ+NNN. |

Notation follows I1, I2 and C3. K_b is the first moment of the energy density, P_b = i[H,K_b], and u = E²/2. Closure means [H,P] = 0 and i[K_b,P_c] = −βδ_bc H. A = Hess u/β − I.

## Reading against the FIXED lines (lane RM, probe M1)

**PASS is not met.** No interacting nearest-neighbour qubit law was found whose composites close C1 + C3. Three obstructions cover most of the open ground.

**FAIL (bounded) is met for the stated classes:**
- **(T1) Band lemma: any isolated band.** This covers any interaction, any internal dimension (finite or infinite), any d, and many-body bands. Exact closure on the band forces Hess u = βI on it. The band is a function on the Brillouin torus, so its zone-averaged anomaly is exactly −β. The sum rule therefore applies to **every isolated composite band separately**, and closure on it is impossible. PROVED; CHECKED.
- **(T2) Bounded-sector theorem.** This covers number-conserving laws whose vacuum is the empty product state, with bounded local terms. Every finite-N sector, including all composites built from N constituents and the whole infinite-dimensional two-particle continuum, has bounded H and P. With β > 0, exact closure on such a sector forces H = 0 there. PROVED.
- **(T3) 1D index theorem (conditional).** This covers a qubit chain with any interaction (no number conservation needed). The I1 decomposition T = U(1)V forces V to carry the shift index log 2. Given asymptotic completeness, a mass gap, a unique vacuum and rational tower centres, V has finite order, so its index is 0. Contradiction. PROVED, conditional on comparator facts (GNVW/RWW index, lattice Haag–Ruelle) and those assumptions.

**Open, and not closed here:**
- non-number-conserving interacting matter in d ≥ 2, whose would-be tower members are embedded, non-isolated, face-touching one-particle states, stabilized exactly;
- irrational tower centres in 1D;
- massless sectors;
- non-first-moment (altered) generators.

**Against the supervisor expectation:**
- Composite bands obey the sum rule: confirmed, and stronger than expected. It holds band by band, and does not need finite dimension per internal level.
- The continuum averages the constituents' anomaly: confirmed for free constituents (energy-weighted). In addition, T2 removes the whole continuum for number-conserving laws.
- The index question was expected to be INCONCLUSIVE. It became a conditional 1D no-go (T3); d ≥ 2 remains SUGGESTED only.

## 1. Bound states and the composite sum rule

### 1.1 Lemma (T1, PROVED)

**Setting.**
- The system is lattice-translation covariant, so T_j K_b T_j⁻¹ = K_b − j_b H for any first-moment K.
- Π is the spectral projector of H onto an isolated band, a translation-invariant subspace on which lattice momentum Q ∈ T^d is a good label.
- The band's dispersion E(Q) > 0 is C¹, and its frame may be twisted (any Chern number).

**Step 1: the compressed boost.**
- ΠKΠ − ½{i∂_Q, E} commutes with every T_j, so it is a multiplication operator f(Q) in a local band frame (plus the Berry connection, which is gauge).
- Hence ΠPΠ = i[E, ΠKΠ] = ∇u.

**Step 2: the bracket on the band.**
- If P is conserved, it commutes with every spectral projector of H, so (1−Π)PΠ = 0.
- Then Π i[K_b,P_c] Π = i[ΠKΠ, ∂_c u] = −E ∂_b∂_c u.
- Closure on the band therefore requires Hess u = βI pointwise.

**Step 3: periodicity.**
- u is a periodic function on T^d. This is gauge-invariant, so twisted bundles do not help.
- So ∫_T Hess u = 0, which gives ⟨A⟩_zone = −I exactly.
- The conclusion holds distributionally, so no smoothness beyond Lipschitz is needed (P bounded and E > 0 give that).

**Isolated multiplets.** I1's finite-N trace rule applies to the group's Riesz projector.

**Infinite-dimensional fibre at fixed Q.** Isolation is the only thing used. The relative-motion space may be infinite-dimensional.

**Partial bands, i.e. bands that dissolve into the continuum at some Q.** An integrated boost maps a normalizable mass-shell state to normalizable states at every lifted momentum. A band that exists only on part of the zone is therefore not boost covariant (PROVED under H-int).

### 1.2 Exact computations (CHECKED)

**Universal result.** Every isolated bound band computed obeys ⟨A_b⟩ = −1.000000 (|⟨u″⟩| ≤ 5e-15), both against its own IR β_b and against the universal β = 1. This was checked in d = 1, 2, 3, on x-lines and body diagonals, for N = 2, 3, 4 clusters, and for XXZ strings (`m1_twobody.out`, `m1_nbody1d.out`).

**Where the −β sits, as a function of binding and size.**

*Weak binding means a large composite.*
- The 1D NN pair has the exact band E_b(Q) = 2(m+2t) − √(U² + 16t²cos²(Q/2)).
- At the face this gives **A(π) = −4/|U|**, i.e. −16, −8, −4 and −2 for U = −0.25, −0.5, −1 and −2 (reproduced numerically).
- The width is ∝ |U|, while the weight stays −2π.
- Since ξ ∝ t/|U|, **the face spike grows linearly with the composite's size**. As ξ → ∞ the composite tends to a smooth 4π-periodic branch plus a SLAC-type face delta. It never tends to a paraboloid on the whole zone.
- Lattice-KG pair (1D, m = 1):

| U | ξ (sites) | min A_b at the face | share of the negative weight within 0.5 of the face |
|---|---|---|---|
| −0.2 | 6.8 | −3.58 | 0.52 |
| −0.5 | 2.6 | −2.69 | 0.41 |
| −1.0 | 1.2 | −2.19 | 0.34 |

- In the IR a weakly bound N-cluster sees a COM lattice of spacing a/N: A_N(Q) ≈ A_1(Q/N). For N = 2 at U = −0.25: A(π/4) = +0.118, against A_1(π/8) = +0.141 and A_1(π/4) = +0.414. This is I2's finer-lattice picture appearing dynamically: the IR improves, the face pays.

*Strong binding means a compact composite.*
- The band is a narrow cosine, A_b ≈ cos Q − 1. The anomaly is spread across the zone, and the face value is −2.0 (m = 3, U = −4 in 1D and 2D).

*IR mismatch of the composite's own speed (a second anomaly, not lattice-scale).*
- With instantaneous contact binding, β_b ≠ β. β_b/β by case:

| Case | β_b/β |
|---|---|
| 1D KG, U = −0.2 | 0.976 |
| 1D KG, U = −0.5 | 0.865 |
| 1D KG, U = −1.0 | 0.599 |
| 1D KG, U = −1.5 | 0.369 |
| 2D, U = −1.5 | 0.783 |
| 3D, m = 1, U = −4 | 0.061 |
| 1D NN, N = 3, U = −0.5 | 0.83 |

- I1 requires a universal β for all matter. So each composite species would need its own IR tuning; nothing in the rule protects it.
- Relativistic, field-mediated binding was **not** tested.
- Rows with E_b < 0 (bound below the vacuum) are printed in `m1_nbody1d.out` but excluded from all claims.

*d = 3 partial band.* At m = 1 and U = −2 there is no true bound state at Q = 0: the grid-induced binding falls as 5.3e-3, 1.1e-3 and 2.8e-4 for n = 24, 40 and 64. It is bound at (π,π,π), with B = 1.42. A partial band of this kind is excluded by boost covariance (§1.1).

**XXZ n-magnon strings: an exact infinite composite family.**
- E_n(K) = J sinh η (cosh nη − cos K)/sinh nη, verified to ≤ 1.0e-14 for n ≤ 4 at Δ = 1.5 and 3.
- Every string band is periodic, so ⟨A⟩ = −1.
- The energies are **bounded** (→ J sinh η) and the bandwidths fall as 1/sinh nη.
- An infinite family of ever larger composites therefore gets heavier and flatter. It does not fill a tower.

## 2. The two-particle sector: can an infinite fibre close?

### 2.1 Bounded-sector theorem (T2, PROVED)

**Hypotheses:**
- K preserves a sector 𝓗_N, for example the N-particle sector of a number-conserving law whose energy density conserves N;
- H − E_vac and P are bounded on 𝓗_N;
- β > 0.

**Proof.**
- Set A_± = H ± P/√β. Then i[K_b, A_±] = ∓√β A_±.
- K_b restricted to 𝓗_N is essentially self-adjoint on finitely supported configurations. This follows from Nelson's commutator theorem with comparison operator 1 + Σ|X_i|²: K's coefficients grow linearly (COMPARATOR: Reed–Simon X.37).
- A_± maps that core into itself, so e^{iηK}A_±e^{−iηK} = e^{∓√βη}A_±.
- Unitary conjugation preserves the norm, so A_± = 0, i.e. H = P = 0 on 𝓗_N. ∎

**Applies to:**
- every N-particle sector of a number-conserving qubit law over an empty product vacuum with bounded local terms, where ‖H − E_vac‖_N ≤ 2N|supp|·‖h‖;
- therefore every composite of N constituents, at any binding, size or number of internal levels;
- the full infinite-dimensional relative-motion fibre;
- partial bands;
- **every member of a would-be tower**, since K commutes with N and all members of one Poincaré orbit share N. So the I1 referee's loophole of "infinitely many extended composite species" cannot assemble into one tower in this class.

**What this answers.** The two-particle fibre at fixed Q is infinite-dimensional but **bounded**. Its relative energies fill a bounded band [E_min(Q), E_max(Q)], not a tower {√(M² + β|Q+2πn|²)}.

**Exact fibre numbers** (`m1_fibre_bracket.out`, U = −1). The sup over Q is taken on wall-free states.

| R | sup‖H(Q)‖ | sup‖P(Q)‖ |
|---|---|---|
| 10 | 5.83 | 3.95 |
| 20 | 5.94 | 4.23 |
| 40 | 5.98 | 4.35 |
| 80 | 5.99 | 4.39 |

These converge; the bound is 7.0.

**Exact sum rule on the infinite fibre (PROVED).**
- In the periodic gauge, H(Q) is a trigonometric polynomial (or analytic periodic function) with operator coefficients.
- So ∫_T dQ ∂_b∂_c H(Q)² = 0 as an **operator identity**: no trace is needed and it survives R = ∞.
- Through the integrated density of states, this reads as a per-mode zone-averaged anomaly of −β over the continuum. That reading of the identity is a READING.

**Free continuum (PROVED, second quantization).**
- On |q₁,q₂⟩: i[K,P] + βH = Σ_i ε_i(β − Hess u(q_i)).
- So the two-particle anomaly is the energy-weighted average of the constituents' anomalies.

### 2.2 The first-moment current on the interacting two-particle sector (CHECKED)

Setting: 1D, distinguishable particles, contact U, R = 60.

- **Hellmann–Feynman holds exactly:** ⟨b|P|b⟩ = du_b/dQ to all printed digits.
- **The unimproved P is not conserved once U ≠ 0.**
  - On wall-free states, ‖C‖ = 0.76 for U = −1, against 1.6e-14 for U = 0.
  - The bound state leaks into the continuum. At U = −1, ‖(P−p_b)b‖ = 0.23, 0.59, 1.35 and 2.12 at Q = π/4, π/2, 3π/4 and π.
  - So C1 fails already for the naive generators.
- **An improvement can remove the leakage.** It costs a translation-invariant ΔK with energy denominators, which are non-local in general. By T1 it cannot change the band value Hess u_b.
- **Consistency check.** At Q = 0, where the leakage vanishes, ⟨b|D|b⟩/(βE_b) = −A_b(0) exactly: +0.0597 for U = −0.5 and +0.2112 for U = −1.

### 2.3 Relation to I1's complete tower

- Exact closure needs, at each Q, the whole orbit {Q + 2πn} of one mass shell, with unbounded energies (I1).
- A fixed-Q two-particle continuum is a bounded band of **relative** energies, labelled by relative momentum. It is not a set of COM paraboloids.
- Only an unbounded sector could host the tower. In number-conserving laws no finite-N sector is unbounded (T2).

**Rapidity is compact on a lattice band (PROVED for band-diagonal K, d = 1; READING beyond that).**
- The first-moment boost flows Q along dQ/dη = −E(Q) on the circle.
- It is periodic, with rapidity period τ = ∮dQ/E. The continuum value diverges.
- For KG constituents, τ = 4.04, 6.54 and 8.76 for m = 1, 0.3 and 0.1.
- This is the same fact as the real period of the rapidity in the elliptic uniformization of integrable lattices (Baxter/Thacker; COMPARATOR from memory).

## 3. Many-body: solitons, integrable lattices, and the index

### 3.1 Integrable chains have an exact "boost", and it generates the next charge (CHECKED, exact operator algebra)

For XX, XXZ (Δ = 0.5, 1, 2) and the critical and gapped TFIM (symmetric bond density), on the infinite chain (`m1_integrable_boost.out`):
- **[H,P] = 0 exactly.** So C1 holds in these 1D models.
- **i[K,P] = −βH + R.** R is a range-3 or range-4 operator, and it is itself conserved: |i[H, i[K,P]]| = 0.
- The relative residual |R|/|i[K,P]| is:

| Model | \|R\|/\|i[K,P]\| |
|---|---|
| XX | 0.707 |
| XXZ Δ = 0.5 | 0.745 |
| XXX | 0.745 |
| XXZ Δ = 2 | 0.791 |
| TFIM g = 1 | 0.707 |
| TFIM g = 0.5 | 0.825 |

- **Reading.** The first moment K is the Tetel'man / Sogo–Wadati / Thacker boost operator (COMPARATOR, from memory). It climbs the ladder of conserved charges, K: H → Q₃ = J_E → Q₄ → …, instead of closing on H. So 1D integrability buys C1 and fails C3 by an O(1) conserved operator.

**Two controls:**
- XXZ+NNN (non-integrable): |i[H,P]| = 0.104, so C1 fails.
- A non-symmetric TFIM density: |i[H,P]| = 8. The density choice, i.e. the improvement, matters for C1, as the RN-L3/C1 referees noted.

**String bound states.** They are isolated, periodic and bounded (§1.2), so T1 applies.

### 3.2 Classical integrable lattices (Toda, Ablowitz–Ladik)

All of this is COMPARATOR or READING, from memory and not re-derived.

**What makes them look like an evasion.** Both have exact soliton families with continuous position and velocity: no Peierls–Nabarro barrier.

**Why they do not carry a Poincaré algebra:**
- **Toda.** Each site is a canonical pair (q_n, p_n). That is an infinite-dimensional local space, so the Qubit price is already paid.
  - Its Σp_n generates field displacements, not translations along n.
  - Soliton speeds are supersonic and grow without bound with amplitude, so there is no invariant speed.
  - Its continuum limits are KdV/Boussinesq, not Lorentzian.
- **Ablowitz–Ladik.** The soliton frequency and velocity are periodic in the carrier wavenumber k (ω ∝ cosh μ cos k − 1).
- **Quantized.** Soliton bands are labelled by lattice quasi-momentum mod 2π. Isolated soliton bands therefore fall under T1, and embedded soliton bands protected by commuting charges do too: a conserved P commutes with a joint spectral projector of charges that it commutes with, as in XXZ, where P = Q₃.

**Relativistic integrable lattice regularizations** (Destri–de Vega light-cone lattice; Faddeev–Volkov lattice sine-Gordon) reach Lorentz invariance only in the scaling limit. At finite spacing their particle dispersions are lattice-bounded (COMPARATOR, from memory).

**Verdict (SUGGESTED).** No 1D integrable lattice known to me carries an exact Poincaré algebra at finite spacing. This is consistent with T1 and T3.

### 3.3 The index question, settled in 1D under stated assumptions (T3)

**Setting.** A qubit chain with any interaction.

**Assumptions:**
- exact integrated positive-energy Poincaré, with first-moment covariance T K T⁻¹ = K − H;
- quasi-local P, i.e. a finite-range energy current;
- a unique vacuum and a mass gap;
- asymptotic completeness (AC) for the particles of the exact (H, P) spectrum. Haag–Ruelle is taken with the quasi-local translations e^{−iaP/β}, since tower members n ≠ 0 are embedded at fixed lattice momentum. That convergence step is assumed, not proved (lattice HR: COMPARATOR, Bachmann–Dybalski–Naaijkens 2016);
- every tower centre θ_s ∈ (2π/q)Z. The natural centres 0 and π qualify.

**Argument.**
1. As in I1, V = U(1)⁻¹T commutes with the Poincaré group, where U(1) = e^{−iP/β}.
2. ind U(1) = 0, because s ↦ e^{−isP/β} is a path of locality-preserving automorphisms from the identity (RWW; COMPARATOR).
3. Hence ind V = ind T = log 2.
4. V maps Haag–Ruelle creation operators to quasi-local operators that create the same one-particle state up to the phase e^{−iθ_s}.
5. So V acts on in-states as the product of per-particle phases. With AC, V^q is implemented by 1.
6. The GNS representation is faithful, so V^q = id as an automorphism, and q·ind V = 0.
7. The index group is torsion-free, so ind V = 0. That contradicts log 2. ∎

**Label.** PROVED, conditional on the comparator facts (GNVW 2012, RWW 2022, lattice Haag–Ruelle) and the assumptions.

**What this resolves.** It answers the I1 referee's objection ("V merely carries the index") in this class. A finite-order commutant symmetry cannot carry a nonzero index.

**What it does not cover:**
- irrational centres;
- failure of AC;
- massless sectors;
- d ≥ 2. A Freedman–Hastings-type flow index across a cut would be needed, so the d ≥ 2 extension is SUGGESTED only.

**Zero-energy (frozen) sectors.** A decoupled frozen sector could carry the shift index, but it is excluded by the unique-vacuum and gap assumptions (cf. the I1 referee's zero-energy-block caveat).

### 3.4 What survives in d ≥ 2 (SUGGESTED)

**Number-conserving matter.** Excluded by T2.

**Non-number-conserving matter.** The tower members n ≠ 0 would have to be exact, stable one-particle states, embedded in multi-particle continua and touching band 0 at the face. There is also an energy-density bound:
- the excess energy per site is ≤ 2‖h‖;
- so a member at energy E ≈ 2π|n|√β spreads over at least E/(2‖h‖) sites. This is I1's size bound.
- Under boosts the lattice therefore enforces anti-contraction. That is incompatible with local (HDA/Schwinger-level) Lorentz contraction, but **not** with the global algebra alone.

## Q-RM readouts

- **Band-averaged anomaly per isolated composite band:** −β exactly, for every binding, size, N and d checked.
- **Face concentration (1D NN pair):** A(π) = −4/|U| ∝ −ξ, with fixed weight −2πβ.
- **IR:** A_N(Q) ≈ A_1(Q/N).
- **Composite IR speed mismatch under contact binding:** β_b/β from 0.98 (ξ = 6.8) down to 0.06 (compact 3D). One tuning per species.
- **XXZ strings:** sup E_n → J sinh η, bandwidth ∝ 1/sinh nη.
- **Integrable chains:** |R|/|i[K,P]| = 0.71–0.83, with R conserved.

## Labels and strong words

**PROVED (same-family, unrefereed):**
- T1 band lemma;
- T2 bounded-sector theorem;
- the operator-identity sum rule on the infinite fibre;
- the free-continuum energy-weighted anomaly;
- the exclusion of partial bands under H-int;
- the 1D rapidity period for band-diagonal K;
- T3, conditional on comparators and AC, gap and rational centres.

**CHECKED:**
- all band numbers in §1.2, including the exact XXZ string formula;
- the fibre numbers in §2.2;
- the exact Pauli-algebra identities in §3.1.

**SUGGESTED:**
- d ≥ 2 index;
- no integrable lattice with exact Poincaré;
- the anti-contraction reading.

**READING:**
- the large composite as "smooth branch + face delta" = SLAC;
- integrable boosts as "climbing the charge ladder";
- the per-mode reading of the operator sum rule.

**COMPARATOR (from memory, not re-fetched):**
- GNVW 2012; RWW 2022; Bachmann–Dybalski–Naaijkens 2016;
- Nelson commutator theorem (Reed–Simon X.37);
- Tetel'man 1982; Sogo–Wadati 1983; Thacker 1986; Grabowski–Mathieu 1995;
- Toda / Ablowitz–Ladik soliton facts;
- Destri–de Vega; Faddeev–Volkov;
- Freedman–Hastings.

**Scope of "impossible":**
- T1: isolated bands with first-moment generators and conserved P.
- T2: K-invariant sectors with bounded H and P, and β > 0.
- T3: 1D only, under its listed assumptions.

**Not claimed:**
- non-first-moment generators;
- non-number-conserving interacting matter in d ≥ 2 with embedded face-touching one-particle states;
- irrational centres; massless sectors;
- relativistic (field-mediated) binding for the IR β_b mismatch.
