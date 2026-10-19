# C4d — Bound pairs in U(1), cubic-covariant one-qubit QCAs: a spectator lemma, exact rigidity at range 1, and where the obstruction stops

**Block:** C4d of `toe-scale-ladder-20261018`. It follows up C4b Lemma 3 and C4c, and asks:
does any one-qubit, Z^3-translation-invariant (TI), U(1)-conserving QCA that is covariant under O
(full action) or T (the axis-action vacuum stabiliser) transport a bound pair, or carry charge at
finite density? **Date:** 2026-10-19. **Status:** Reviewed in a separate agent context (same model as the author); unaudited.
No axiom, primitive or dynamics clause is adopted.

## Result up front

1. **Spectator lemma (proved; any range r, any dimension, no symmetry needed).** Suppose a U(1)
   QCA freezes single magnons, so α(σ⁺_w)|Ω⟩ = e^{iφ}|w⟩, and has range r. Then for every finite
   cluster C and every site w with dist(w, C) > r,

   U|C ∪ {w}⟩ = e^{iφ} (U|C⟩) ⊗ |w⟩.

   A lone magnon farther than r from a cluster is an exact spectator, even when the cluster
   moves toward it. The same holds for U^† = α^{-1} with the phase e^{−iφ}:
   U^†|C ∪ {w}⟩ = e^{−iφ} (U^†|C⟩) ⊗ |w⟩. A consequence: the images of every
   configuration "pair + far magnon" are fixed by the pair walk W alone. So unitarity of U on the
   3-magnon sector gives **W-only constraints**. These are the "3-magnon consistency
   constraints" the task asked for, and they come out in closed form.
2. **Range 1: pairs are exactly static (exact certificate, every deduction re-verified).** Take any
   TI one-qubit U(1) QCA on Z^3 of Chebyshev range 1 whose pair sector is T-covariant by site
   permutations. This covers the axis action with Q_n conserved, and the full action with SU(2).
   Its two-magnon sector is then **diagonal**:

   U|x, y⟩ = e^{iθ(y−x)}|x, y⟩ for every pair.

   Under T, 59 of the 62 symmetry-reduced amplitudes are forced to zero by unitarity plus the
   spectator isometries. Under O, 33 of 36 are. The 3 survivors are the "stay" phases (axis, face
   and body pairs). No pair moves, so no pair band exists to be flat or dispersive. **The
   face-diagonal channel of C4c Observation M is therefore not realisable at range 1.** The
   monomial case is also enumerated exhaustively: 6 T-equivariant bijective pair maps, 2 of which
   glide, and only the identity survives.
3. **Range 2: the 3-body obstruction disappears (exact).** At range 2, the face-diagonal glider
   with velocity 1 site/tick passes the exact 3-magnon spectator test, in both directions. The
   v = 2 version fails it. The range-1 mechanism therefore does not extend: at range ≥ 2, pair
   transport is **open**. It is not excluded at the level of the pair walk plus one extra magnon.
4. **Finite density at range 1: reduced, not closed.**
   - *Lemma D (proved, any r).* Take a U(1) QCA with frozen singles. If U is diagonal on all
     configurations with ≤ k magnons, then it is diagonal on every (k+1)-configuration of
     diameter > r. So U is diagonal on every sector if and only if every **clique walk** W_k is
     diagonal. W_k is U restricted to sets of diameter ≤ r, and at r = 1 these are subsets of a
     unit cube, k ≤ 8. If all W_k are diagonal, all densities are frozen.
   - k = 2 is item 2.
   - For k = 3, the same single-term deduction leaves 159 of 255 off-diagonal unknowns undecided.
     The prediction "W_3 is diagonal by the same argument" FAILs, and the FAIL is kept in the log.
     A numerical probe finds near-solutions of the full W_3-only system that are non-diagonal
     and COM-moving. Their residual norm is ‖r‖ ≈ 5e−7 to 8e−7 (see the k = 3 section) and they
     carry moving weight 0.2, with a W_3(K) band variation of about 1e−2 rad. *Evidence, not a
     conclusion:* this suggests the W-only constraints may not freeze triples at k = 3. It is not
     established, and whether any solution extends to a QCA is open.
5. **Emptiness-shell pair gates cannot form commuting layers (proved; instance-checked).**
   Consider monomial gates that act on a pattern region R only when a surrounding shell is empty.
   If some generic linear functional has both of its extreme sites on R toggled by the gate, the
   gate's translates do not all commute. This holds for every *surrounding* shell, meaning both ℓ-extreme sites of the support lie in the shell, for example S ⊇ vertices of conv A (Proposition E). Partial, one-sided or empty shells are not covered. It
   turns C4c's "boundary-shell conflict" from an argument into a theorem. It kills every
   tetrahedral or caterpillar realisation of the face-diagonal move as a commuting emptiness-
   controlled layer, at any range.

**Bottom line.** The task asked whether some such QCA transports a bound pair or charge at finite
density. This is **not decided in general.**
- *Decided negatively at range 1, for pairs.* Under T or O, every range-1 U(1) one-qubit QCA has
  exactly static pairs (item 2).
- *Not decided at range 1 for k ≥ 3 clusters or finite density.* It is reduced there to finitely
  many clique walks (item 4).
- *Not decided at range ≥ 2.* There the face-diagonal glider passes every constraint that the
  pair walk alone can see (item 3).
- No construction that transports anything is exhibited, so no pair dispersion is reported.

## Premises (named, supplied)

- **Lattice and Qubit axioms**; **(D-QCA):** a TI, finite-range *-automorphism α, not assumed to be
  Clifford; **(S):** soldering with C4 conventions.
- **Range.** α(A_x) ⊂ A_{B_r(x)}, with B_r the Chebyshev ball. The inverse has the same
  neighbourhood (−B_r = B_r; Arrighi–Nesme–Werner, recalled, as in C4c).
- **U(1).** α conserves Q_n under the axis action. Under the full action it conserves global SU(2)
  (C4b Lemma 2(a)). The vacuum Ω is all spins along −n. Single magnons are frozen
  (C4b Lemma 2(b), H ⊇ T). The phase φ is normalised away, so W = 1 on far pairs.
- **Covariance used.** Only that the two- and three-magnon matrix elements are invariant under
  site permutations by T (or by O) together with translations:
  - Axis action: even R act on-site by rotations about n. In the n-basis these are phases that
    depend only on the magnon number, so they cancel within a sector.
  - Full action: SU(2) symmetry undoes the on-site part.
  - Odd R under the axis action relate particle and hole sectors, and are not used.

  A T statement therefore covers both actions.

## Lemma S — spectator lemma (proved)

*Proof.* We have U|C ∪ {w}⟩ = α(σ⁺_C) α(σ⁺_w) U|Ω⟩ = e^{iφ} α(σ⁺_C)|w⟩.
- α(σ⁺_C) is supported in N_r(C), and w ∉ N_r(C). So α(σ⁺_C)|w⟩ = (α(σ⁺_C)|Ω⟩) ⊗ |w⟩.
- α(σ⁺_C)|Ω⟩ = U|C⟩, which has no magnon at w.

The same argument applies to α^{-1}. Its neighbourhood is −B_r = B_r, and
α^{-1}(σ⁺_w)|Ω⟩ = e^{−iφ}|w⟩. So U^†|C ∪ {w}⟩ = e^{−iφ}(U^†|C⟩) ⊗ |w⟩. ∎

It needs no TI and no symmetry. Sanity check (`c4d_01`): U = V D V^†, where V is an XY layer on
the even bonds of a 10-site ring and D = exp(iφ Σ n_x n_{x+1}).
- Singles are exactly frozen, pairs move (1 − |⟨xy|U|xy⟩| up to 0.13), and the range is 3.
- The identity holds in all 40 cases with dist(w, C) > 3, for clusters of size 2 and 3.
- It fails in 1100 cases with dist ≤ 3, so the test discriminates.
- PASS = 7.

**The W-only constraints.** Call (p, w) *valid* if p is a pair and dist(w, p) > r. Then
U(p ∪ {w}) = (W p) ⊗ w. For two different valid triples, isometry of U gives

  Σ_u conj(⟨w₂, u|W|p₁⟩) ⟨w₁, u|W|p₂⟩ = 0     (w₁ ≠ w₂),     (S)

and the same holds with W^† in place of W, which is (S†). Together with unitarity of W on near pairs
(U), and Lemma K support (C4c), these are necessary conditions for W to belong to some QCA. At
r = 1, the forward/backward cross-consistency conditions are automatic (shown in the derivation
notes of `c4d_monomial.py`), so (U), (S) and (S†) are the whole W-only content.

## Theorem P1 — range-1 pair rigidity (exact finite certificate)

*Statement.* Take r = 1 and G ∈ {T, O}. Let W be a G-covariant, TI unitary pair walk on near pairs
with Lemma-K support that satisfies (U), (S) and (S†). Then W is diagonal: W|x, x+ρ⟩ = e^{iθ_ρ}|x, x+ρ⟩,
with θ constant on G-orbits of ρ. Conversely, every such diagonal W satisfies all the constraints.
Hence every QCA in the premise has static pairs.

*Certificate* (`c4d_05`; logs `c4d_05_range1_exact_{T,O}.txt`, PASS = 5 + 5):
- The unknowns are the amplitudes ⟨σ|W|p⟩, keyed by G ⋉ Z^3 orbits of (σ, p): 62 for T, 36 for O.
- The constraints are enumerated geometrically: 6565 unitarity constraints, and 80172 each of (S)
  and (S†).
- *Deduction rule.* After inserting the zeros already proved, if a constraint reduces to
  m·|x_k|² = 0 with m a positive integer, then x_k = 0.
- Fixpoint, T: 59 zeros in 3 rounds, and every non-stay amplitude vanishes. O: 33 zeros.
- *Re-verification.* Every deduction's witness, a geometric constraint (p₁, w₁, p₂, w₂) or a
  unitarity pair (p₁, p₂), is re-evaluated by a separate implementation. It has its own orbit
  keying, its own enumeration of W|p⟩, and its own validity test. Each witness reproduces
  m|x_k|²: 59/59 for T and 33/33 for O.
- The same deduction is reproduced a third time by the general k-clique code `c4d_07` at k = 2
  (59 zeros). That code has a different constraint generator.

*Example deduction* (the first one logged). Let x be the amplitude for the axis pair {0, e₃}
moving to {−e₁ − e₂, −e₁ − e₂ + e₃}. By C2z covariance, the pair p₂ = {−2e₁ − 2e₂, −2e₁ − 2e₂ + e₃}
moves to the same place with the same amplitude x. In ⟨W p₁|W p₂⟩ = 0, every other term contains
an amplitude already proved zero, so the constraint reads |x|² = 0.

*Monomial version* (`c4d_02`, exhaustive): T has 6 equivariant bijective deterministic maps, 2 of
which are the face-diagonal gliders. All 5 non-identity maps violate injectivity on the
3-magnon sector. Example collision: a pair arrives next to a third magnon, and the same final
configuration is also produced by the third magnon's pair partner arriving from a different
direction. O has 2 maps, and only the identity survives.

*Numerical companion (evidence only)* (`c4d_04`): local minimisation with a prescribed
COM-moving weight μ. The minimal violation scales as 0.14 μ² for μ = 0.02, 0.1 and 0.3. This
is consistent with Theorem P1. **Disclosure:** that script's final check used a threshold of 1e−4
that I fixed in advance without accounting for the μ² scaling. At μ = 0.02 the cost is 5.6e−5, so
the line FAILs. The FAIL is kept in the log. It reflects a badly chosen threshold, not a
near-solution: all 6 restarts give the same nonzero optimum, as they do at every μ.

## Range 2 — the obstruction stops (exact, `c4d_06`, PASS = 2)

Under T at r = 2, the face representative ρ = (0,1,−1) has 10 stabiliser-fixed images. I take W
to move only that orbit, by a fixed image, and to fix all other pairs. Then:
- The maps that move the pair by ±1 along the face normal (the Observation-M glider,
  v = 1 site/tick) produce **0 spectator conflicts**.
- The maps that move it by ±2 produce 16 each.
- Among the COM-preserving images, those at offset 0 or ±1 (crossed diagonals and the identity)
  pass, and those at ±2 fail (16 conflicts each).

*Why range 1 is special.* At r = 1 every near pair is "short". The configuration produced when a
moving pair lands next to a spectator therefore always contains a second near pair that could
have arrived instead. At r ≥ 2, a pair moving 1 site cannot get within distance 1 of a magnon
that started more than r away. *Scope:* this is only the W-only level. A full QCA also needs
consistent data on pair–pair and cluster sectors (two pairs, k-cliques), which W does not fix.

## Lemma D — reduction of all densities to clique walks (proved)

Suppose U is diagonal on every configuration with ≤ k magnons. Let C be a (k+1)-configuration
with two magnons x, y at distance > r. Write D = (C ∖ x) ∩ B_r(x), so |D| ≤ k − 1. Then

U|C⟩ = α(σ⁺_x) U|C∖x⟩ = e^{iθ} (α(σ⁺_x)|D⟩) ⊗ |C∖x∖B_r(x)⟩ = phase · |C⟩,

because α(σ⁺_x)|D⟩ ∝ U|D ∪ x⟩ ∝ |D ∪ x⟩ by hypothesis. ∎

So U preserves the span of the (k+1)-cliques, which are the sets of diameter ≤ r, and acts there
as a TI clique walk W_{k+1}. **U is diagonal (all sectors and densities frozen) iff every W_k is
diagonal.** At r = 1 there are k ≤ 8 cases, each a finite exact problem. Lemma S again gives
W_k-only constraints, from the configurations "k-clique + far magnon" together with the already
diagonal non-clique (k+1)-configurations.

**k = 3 at r = 1, T** (`c4d_07` k = 3; log `c4d_07_clique_k3_T.txt`):
- 44 clique translation classes, 260 orbit-keyed unknowns, 5 of them "stay".
- 19076 unitarity constraints and 596408 spectator constraints.
- Single-term deduction proves 96 zeros, with no stay amplitude forced. **159 off-diagonal unknowns
  remain undecided**, so the check FAILs.
- What this means: the k = 3 sector is *not* settled by the method that settles k = 2. It does
  not exhibit a non-diagonal W_3.

Numerical probe: see "k = 3 numerics" below.

## Proposition E — emptiness-shell gates never commute (proved)

*Setup.* A monomial gate g is a tuple (A, R, S = A∖R, Λ, π):
- A is a finite support;
- R ⊂ A is the pattern region;
- Λ is a family of subsets of R;
- π ≠ id is a permutation of Λ (phases allowed).

g acts on a configuration c, viewed as a set of occupied sites, when c ∩ S = ∅ and c ∩ R ∈ Λ. It
then replaces c ∩ R by π(c ∩ R). A site v ∈ R is *toggled-in* if v ∉ λ and v ∈ π(λ) for some
λ ∈ Λ.

*Claim.* Suppose there is a generic linear functional ℓ, injective on A, such that:
- argmax_A ℓ and argmin_A ℓ lie in S, which holds whenever S contains the vertices of conv A;
- both argmin_R ℓ and argmax_R ℓ are toggled-in.

Then the translates of g do not all commute.

*Proof.*
1. **Witness configuration.** Put p = argmax_A ℓ, v = argmin_R ℓ and t = p − v. Then
   (R+t) ∩ A = {p}. Take λ with v ∉ λ and v ∈ π(λ). Suppose some non-fixed μ ∈ Λ (π(μ) ≠ μ) has
   μ ∩ (A+t) = ∅, and let c = (λ+t) ∪ μ.
2. **Both gates active, and they do not commute.** Both g₀ and g_t are active on c. Then
   g₀g_t c = (π(λ)+t) ∪ μ, because g_t fills p ∈ S and so switches g₀ off. But
   g_t g₀ c ∈ {(π(λ)+t) ∪ π(μ), (λ+t) ∪ π(μ)}. These differ from g₀g_t c, so the gates do not
   commute.
3. **If no such μ exists for ℓ.** Every non-fixed μ then meets A + t. That needs
   max_μ ℓ ≥ max_A ℓ + min_A ℓ − min_R ℓ.
4. **The same for −ℓ.** If the witness also fails for −ℓ, then min_μ ℓ ≤ max_A ℓ + min_A ℓ − max_R ℓ.
5. **Contradiction.** Steps 3 and 4 together give width_ℓ(μ) ≥ width_ℓ(R). So every non-fixed μ
   contains both ℓ-extremes of R. But argmin_R ℓ is toggled-in, so some non-fixed λ omits it.
   Contradiction. ∎

*Coverage.*
- The tetrahedral complement gate covers every "caterpillar" realisation of the
  Observation-M move as a commuting emptiness-controlled layer. This gate acts on an even
  tetrahedron with exactly 2 magnons, moving them to the opposite edge, and the tetrahedron's 6
  edges are exactly 3 opposite face-diagonal pairs. Every site of the tetrahedron is toggled, so
  the claim applies for every surrounding shell.
- *Instance checks* (`c4d_09`, PASS = 2): explicit non-commuting translate pairs are found for
  shells N₁, N₂ and N₃ and for 12 random T-symmetric shells. The witness provably does not apply
  to a collinear "inchworm" gate whose end partner is never toggled.

*Escape routes not covered:*
- gates with an untoggled extreme site, such as inchworm gates. Under T their reflected partner
  gate overlaps them on the shared state {0, 2e} and does not commute with them, by direct check
  in the analysis, not in the script;
- non-monomial (superposition) gates;
- controls other than emptiness;
- non-commuting or staircase constructions.

## k = 3 numerics

*Evidence only* (`c4d_08`, `c4d_10`).

**Setup.**
- Unknowns: the 164 W_3 unknowns left by the deduction.
- Constraints: all 1674 distinct surviving constraints of c4d_07, plus the 44 column-norm
  conditions. None was dropped, because no surviving constraint contains an unknown-phase term.
- Method: least squares with a prescribed weight μ on off-diagonal, or on COM-moving,
  amplitudes. Every column is normalised, so the unbounded-diagonal degeneracy noted in the C4c
  review cannot occur.

**Results.**

Every value in this table and in the run reports below is the script's printed "cost",
np.sum(s.fun**2) = ‖r‖². That includes the moving-weight penalty row. The residual norm is the
square root of the cost.

| target | μ = 0 | μ = 0.05 | μ = 0.2 |
|---|---|---|---|
| off-diagonal weight | 1.7e−25 | 4.1e−17 | 2.0e−18 |
| COM-moving weight | 1.5e−23 | 5.0e−14 | 5.6e−12 |

- Contrast with k = 2 (c4d_04): there the optimum scales as 0.14 μ².
- **Moving solution** (`c4d_10`, μ = 0.2, 4000 evaluations): printed cost 3.0e−13, so the
  residual norm is ‖r‖ ≈ 5.5e−7, not "≤ 3e−13" as an earlier draft said. The review reads the
  printed value as scipy's ½‖r‖² and gets ‖r‖ ≈ 8e−7. The script sums the squares directly, so I
  get 5.5e−7. Either way the residual is of order 1e−6, far from machine precision. The log line
  "satisfies the W₃-only system to 1e−10" compares this cost, not ‖r‖, so it is weaker than it
  reads. W_3(K) is unitary to 1.4e−8. Its eigenphases vary by 1.2e−2 rad over a 6³ K-grid (Hausdorff distance on
  the circle). With 500 evaluations the residual was 1.4e−12 and the variation 3e−3.

**Reading.**
- Off-diagonal W_3 solutions appear to exist: the cost reaches 2e−18, so ‖r‖ ≈ 1.4e−9.
- COM-moving ones are reached only to ‖r‖ of order 1e−6. Convergence is slow, so I cannot tell from this
  data whether exact moving solutions exist or the infimum is not attained.
- No claim of a dispersive triple band is made. The `c4d_10` logs print "DISPERSIVE bands for
  this solution". That label only means the spectral variation of this *approximate* solution
  exceeded 1e−4. Given ‖r‖ ~ 1e−6 and the unknown status of exact solutions, it is **not** a
  claim of a dispersive band. The old logs are left unedited.
- The open k = 3 problem is now concrete. It needs an exact solution of a 164-unknown bilinear
  system, then the 2→3 local data of α(σ⁺_x) (the 4-magnon sector) to decide whether any solution
  extends.

## Symmetry is load-bearing (scope probe, `c4d_05 C1`)

I ran the same deduction with no point-group symmetry (TI only, frozen singles assumed). It
proves 174 zeros out of 679 unknowns, and every one of those deductions is re-verified. It leaves
492 off-diagonal unknowns undecided, and the two "diagonal" checks FAIL. Those FAILs are logged.
Theorem P1 therefore really uses T: the decisive self-overlap constraints m|x|² = 0 come from
pairing an amplitude with its own T-image. This does *not* show that non-diagonal non-symmetric
range-1 pair walks exist. It shows only that this certificate needs the symmetry.

## Claim types

| claim | type |
|---|---|
| Lemma S (spectator) | proved; toy check |
| Theorem P1 (range-1 pairs static, T and O) | exact finite certificate; each deduction re-verified by independent evaluator; third reproduction by `c4d_07` |
| monomial range-1 enumeration | exhaustive exact certificate |
| range-2 glider passes 3-magnon test | exact finite certificate (positive statement about constraints, not a construction) |
| Lemma D | proved |
| k = 3 single-term deduction insufficient | exact (FAIL kept) |
| Proposition E | proved; instance checks |
| C1 probe (no symmetry: deduction incomplete) | exact for what it proves; scope statement |
| c4d_04, c4d_08, c4d_10 minimisations | numerical evidence only |

## No-go discipline (scoped negatives)

- **What is excluded, with quantifiers.** The scope is all TI one-qubit U(1) QCAs on Z^3 of
  Chebyshev range ≤ 1 (for α, hence for α^{-1}) with frozen singles, whose 2- and 3-magnon matrix
  elements are T-invariant. This includes the axis action (Q_n) and the full action (SU(2)).
  Their two-magnon sector is diagonal.
- **Not excluded:**
  - range ≥ 2, where the glider is consistent with every W-only constraint;
  - k ≥ 3 cluster motion and finite-density transport at range 1;
  - all non-U(1) dynamics (C4b W2).
- **N1, routes tried:**
  - W-only constraints at r = 1 (closed: diagonal);
  - monomial maps at r = 1, exhaustive (closed);
  - r = 2 glider (open, consistent);
  - commuting emptiness-shell layers (closed by Prop. E);
  - k = 3 clique walk (open).
- **N7, steelman.** A range-2 QCA might realise the face-diagonal glider by a construction that
  is neither a commuting emptiness-controlled layer nor a commuting covered layer: a staircase, a
  non-monomial gate, or a gate with catalytic or other non-emptiness controls. Nothing here
  forbids it. That is why no general no-go is claimed.

## Logged FAILs (all kept; `logs/SUMMARY.txt` TOTAL: PASS=37 FAIL=4)

1. `c4d_04`: a pre-set threshold of 1e−4 on the cost at μ > 0. The cost is 0.14 μ², which is
   5.6e−5 at μ = 0.02. This is a badly chosen threshold. The optimum is the same nonzero value
   for all 6 restarts at every μ.
2. `c4d_05 C1` (2 lines): without symmetry the single-term deduction does not reach a diagonal W.
   This is a scope finding, not a prediction made beforehand.
3. `c4d_07 k = 3`: the prediction, made before the run, that W_3 is diagonal by single-term
   deduction is falsified (159 undecided). The prediction was not recorded in a file
   beforehand; disclosed.

## Answers to the task items

- **(a) Characterise via one- and two-magnon sectors.**
  - One-magnon: frozen (C4b Lemma 2). Lemma S then makes every far magnon a spectator.
  - Pair walks: the admissible ones are fixed by (U), (S) and (S†).
  - At r = 1 under T/O the only admissible walks are diagonal (Theorem P1).
  - At r = 2 the face glider is admissible.
- **(b) Construct Observation M's moves.**
  - Not possible at r = 1 (Theorem P1).
  - As commuting emptiness-controlled layers, not possible at any range (Prop. E).
  - At r ≥ 2 no construction was found. The coordinator's suggestion of products over sublattice
    colourings was not pursued. A product of sublattice-colour layers that do not commute is
    translation-covariant only up to the cyclic reordering of the colours. So it is not TI unless
    the layers commute, and commuting layers fall under Prop. E or C4c Theorem N. The NOTE does
    not claim this as a theorem.
- **(c) Strongest scoped obstruction.**
  - Theorem P1, for pairs at range 1, any T- or O-covariant U(1) one-qubit QCA.
  - Lemma D, reducing range-1 finite density to clique walks.
  - Prop. E, ruling out emptiness-shell commuting gates.
- **Pair dispersions.** None to report: there is no construction. At range 1 the pair spectrum
  is flat by Theorem P1; indeed W is diagonal and K-independent.

## Reproduction

```bash
cd blocks/C4d/scripts      # set OMP_NUM_THREADS=1 to respect the one-core budget
python3 c4d_01_spectator_toy.py        # PASS=7 FAIL=0   (~10 s)
python3 c4d_02_range1_monomial.py      # PASS=3 FAIL=0   (~5 s)
python3 c4d_04_range1_quantum_search.py 1   # PASS=2 FAIL=1 (~15 min; numerical)
python3 c4d_05_range1_exact.py T       # PASS=5 FAIL=0   (~1 min)   Theorem P1
python3 c4d_05_range1_exact.py O       # PASS=5 FAIL=0   (~1 min)
python3 c4d_05_range1_exact.py C1      # PASS=3 FAIL=2   (~2 min)   scope probe
python3 c4d_06_range2_glider.py        # PASS=2 FAIL=0   (~3 min)
python3 c4d_07_clique_walks.py 2 T     # PASS=2 FAIL=0   (~1 min)   regression = P1
python3 c4d_07_clique_walks.py 3 T     # PASS=1 FAIL=1   (~2 min)
python3 c4d_08_clique_numeric.py 3     # PASS=1 FAIL=0 (own) (~15 min)
python3 c4d_09_shell_nogo.py           # PASS=2 FAIL=0   (seconds)
python3 c4d_10_clique3_solution.py moving 0.2 2 4000   # PASS=2 FAIL=0 (~12 min)
```

A brute-force cross-check of the constraint builder, which built the 3-magnon images on a large
window, was started and then abandoned because it used about 70% of RAM. It left no log. It is
replaced by the per-witness re-verification in `c4d_05`, which uses a different implementation.

## Load-bearing step for independent check

The load-bearing step is **Theorem P1's certificate**. For each of the 59 deductions (T),
recompute from scratch the overlap of the two witness vectors, without using `c4d_quantum.py`:
- W p₁ ⊗ w₁ and W p₂ ⊗ w₂ for a spectator witness;
- W p₁ and W p₂ for a unitarity witness.

Confirm that, after the zeros already established, the overlap is m|x|². The derivation of
(S) and (S†) from Lemma S should be checked too. Two points need care:
- the inverse range (−B_r = B_r);
- the claim that T acts on the 2- and 3-magnon sectors by pure site permutations under the axis
  action.

A blind route would be best: an independent exact solve, for example a Gröbner basis or exact
elimination of the 62-unknown system (U) + (S) + (S†), that does not use the single-term rule.

## Novelty

As far as I know, the spectator lemma and the resulting closed-form "pair walk + one magnon"
constraints are standard-looking but not written down for this setting. They resemble the
cluster-decomposition arguments in Schumacher–Werner reversible QCA theory (recalled, not
re-checked). No literature search was done. The cubic-covariant range-1 rigidity and Prop. E
appear new. Novelty does not bear on correctness.

## Review dispositions (`REVIEW.md`)

The review reproduced Theorem P1 for T and O with a blind independent solver.

| item | disposition |
|---|---|
| Spectator lemma: U† phase | **accepted.** e^{−iφ} is now explicit, in Result 1 and in the proof |
| Prop. E: "every finite shell" is too broad | **accepted.** Now "every surrounding shell" (both ℓ-extreme support sites in S), in Result 5 and Coverage |
| k = 3 residual misreported | **accepted in substance.** The printed figure is a cost, not a residual. My script computes np.sum(fun²) = ‖r‖², giving ‖r‖ ≈ 5.5e−7. The review assumes ½‖r‖² and gets 8e−7. The disagreement is recorded, and both are of order 1e−6 |
| "W-only constraints do not freeze triples" stated too strongly | **accepted.** Relabelled as evidence, not a conclusion |
| log "DISPERSIVE" vs "no dispersive claim" | **accepted.** Explanatory line added. The logs are not edited |
