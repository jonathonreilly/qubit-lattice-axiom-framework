# C4b findings: does closure with the walker as matter force K1 = K2?

Provenance: a worker of the same model family. Proof-critically checked by a fresh-context same-family agent (`../C4b_check/REPORT.md`, 23/0 plus an audit of C4b's solves): confirmed, and its corrections are applied below. Saved by the supervisor from the hand-back.

| Runner | Method | Result |
|---|---|---|
| `c4b_closure.py` | B21_check's Fourier-kernel engine plus a spinor extension, exact sympy | PASS=21 (183 s) |
| `c4b_operator_route.py` | position-space operator identities | PASS=3 |

Two earlier failing runs are kept:
- run1: an expectation bug in A1;
- run2: a harness bug in D2, plus an F1 expectation that turned out to be a physics result.

**Answer (as corrected by the check).**
- **Invariant result.** Closure with the walker forces γ = a_s K1/K2 = 1. In block-62 variables, where a_s = 1 by definition, this is **K1 = K2**. It is B21's equivalence (d), unit matter coupling ⇔ r = 1, realised for the spinor walker.
- **Speed and α.** With the walker's speed 1 fixed, closure puts both the walker's cone and the TT cone at that speed and forces α = K2/4. With a_s = 1 this is block 62's α = K/4 with a single K. Block 62 T4 said "nothing here forces that value"; within these premises, closure does.
- **Rotation covariance.** The walker as written is not locally rotation covariant. It lacks ¼·N·T(E)·n, the totally antisymmetric part of the Levi-Civita spin connection. Without it, closure fails at the next order. This is already in the repo: block 65, the blind-walk note, has the first-order lattice version, and the 09-13 native-Weyl note uses the full covariant operator. The missing piece is the second-order symmetric-section term.

## Setup

- **Matter.** C_f[N] = ∫χ̄ ½{N E_a^j σ_a, p_j} χ, with χ a spinor half-density.
- **Frame, two routes:**
  - metric route, E = (δ + a_s h)^(−1/2);
  - triad route, E = 1 + ε.
- **Gravity.** C_g = kin0 + kin_X − K1R1 − K2R2, and G = λ1G1 + νG2 with G2 = ν∫P L_ξh.
- **Fermion relabelling.** G_f = λ_f·Kosmann + G_f^(1), with a 20-term isotropic h-linear ansatz.
- **Other.** kin_X is a 3-term P·h·{n, s} ansatz. There is one field-independent lapse rule.

## Results (continuum, flat background)

- **A2** (operator route agrees). {G, C} at ψ̄ψ closes iff a_s = λ_f/λ1, with s1 = −λ_f, s2 = 0 and the Kosmann spin term +i/4.
- **A1b.** The isotropic solution space is exactly 3-dimensional: λ_f × (Kosmann + the walker's coupling), s2, and a trivial phase.
- **A1a.** In a fully general ansatz the null space is 29-dimensional: 24 field redefinitions, λ_f, s2, and 3 stress-free phase directions.
- **C1.** {G, G} at ψ̄ψ forces λ_f ∈ {0, ν}, and λ_f = 0 needs a_s = 0. G_f^(1) is forced, with 5 directions free.
- **C2.** The Kosmann non-closure (the spin-½ note's Result 4) is absorbed by the connection terms. So the metric route closes {G, G} without a triad. This agrees with the 09-13 native-Weyl note's P7/P13, and the spin-½ note's Result 4 has been corrected accordingly.
- **B1 (main result).** Fix a_s = 1 and λ_f = ν. Combining gravity's h-linear {C, G} with the walker's {C, G} has the unique solution λ1 = ν, **K2 = K1**, s1 = −ν, s2 = 0.
- **B2.** With a_s free, λ1 = ν/a_s and K2 = a_s K1. So a_s = K2/K1, and a_s = 1 ⇔ K1 = K2.
- **D1.** {C, C} gives b = −½ and v² = a_s K1/(4α). With B1 this is v² = K1/(4α) = K2/(4α), the TT cone. **D3:** {C, C} at P·ψ̄ψ is identically zero.
- **E1.** {G, C} at P·ψ̄ψ forces kin_X ≠ 0, a P·h·s term with coefficient ν²/(32αλ1²).
- **E2** (second route, using C1's G_f^(1)). a_s = ν/λ1, and β = −a_s.
- **G1** (operator route agrees). On E = 1 + A with A antisymmetric, the walker equals a spin rotation plus ½∫N(∂·θ)n. **The walker is not locally rotation covariant.**
- **G2.** With T = ε_abc E_a^j E_b^k ∂_j e_ck, walker + c_ax N T n is rotation covariant iff c_ax = ¼. This is the totally antisymmetric part of the Levi-Civita spin connection. It is not torsion; in Hehl–Datta terms it is the same algebra.
- **G3.** In the symmetric frame T = 0 at first order, so every result above holds; at second order T ≠ 0.
- **G4** (triad route). Closure at ψ̄ψ iff λ_E = λ_f with a plain Lie derivative. Then λ1 = λ_E, so a_s = 1 directly.
- **F1.** The bare walker's O(h²) coupling has no solution at h·ψ̄ψ, at r = 1 or r = 2.
- **F2.** The axial-completed walker closes at r = 1 and at r = 2 (a_s = ½). The control fails.

## Statement

Within the repo's walker and member, continuum leading-order closure fixes K1 = K2. So α = K/4 (v² = K1/(4α) at the walker's top speed) gives that top speed to both the walker and the TT member.

**Premises:**
- continuum, flat background;
- the orders computed;
- one C, one G, one lapse rule;
- isotropic ansätze;
- G2 = ν L_ξh;
- h_member = (EᵀE)^(−1) − δ.

The rotation constraint matters in the triad route (G1, G2), not in the metric route.

## Derived vs supplied

- **Derived:**
  - a_s λ1 = λ_f;
  - λ_f = ν, s1, s2;
  - the Kosmann coefficient and the forced connection terms;
  - β = −a_s and K2 = a_s K1;
  - the walker's rotation defect and the axial coefficient ¼;
  - the bare walker's next-order failure.
- **Supplied:** the walker operator and lapse placement, h = (EᵀE)^(−1) − δ, the member's √gR form, G2, isotropy, and one lapse rule.

## Caveats

- Only the k = 0 species; doublers have their own spin sets.
- Not computed: {G, G} at h·ψ̄ψ, the h² sectors, non-isotropic G_f^(1).
- Three G_f^(1) directions remain free.
- The connection terms match the 09-13 note's only in size.
- The F results are witnesses at r = 1 and 2.
- The solves assume positive constants.
- **Lattice (remark only):** exact continuum-spectrum closure is impossible (C3). The walker is a step, and its frame coupling matches only at q = 0. Block 65 has the first-order lattice axial term about the identity frame; the second-order symmetric-section term has none.

## Prior art

- Nelson–Teitelboim 1978; Henneaux 1983 (unverified).
- Ashtekar–Romano–Tate 1989; Barbero 1995.
- HKT 1976; Teitelboim 1973.
- Kibble 1961; Hehl–Datta 1971 (Dirac fields couple only to axial torsion).
- Bourguignon–Gauduchon 1992; Clayton gr-qc/9808005; Müller–Nowaczyk 1504.01034.
