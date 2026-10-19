# C4e — A moving bound pair exists: an explicit T-covariant, U(1), one-qubit QCA on Z^3 with frozen magnons and a speed-1 face-diagonal pair glider (CA radius ≤ 6; QCA range between 5 and 18), plus 3-magnon consistency at range 2

**Block:** C4e of `toe-scale-ladder-20261018`, following C4d (spectator lemma, Theorem P1, range-2
glider passes the W-only test, Prop. E) and C4c (Observation M). **Date:** 2026-10-19.
**Status:** Reviewed in a separate agent context (same model as the author); unaudited. See `REVIEW.md` and "Review dispositions". No axiom, primitive or dynamics
clause is adopted; the QCA below is a *constructed example* inside the premise class, not a
proposal for the framework's dynamics.

## Result up front

1. **Construction (proved; implementation exact-checked).** U = L2 ∘ L1 is a translation-invariant
   (TI), one-qubit-per-site, magnon-number-conserving QCA on Z^3. It is covariant under T (axis
   action, phases included), it freezes single magnons, and its two-magnon sector is **exactly** the
   speed-1 face-diagonal glider W_{s=−1} of C4d/C4c: {0, e1+e2} → {e3, (1,1,1)}, and in general a
   face pair with zero coordinate a and nonzero coordinates b, c moves by v = ρ_bρ_c e_a.
   All other pairs are static. So a **genuinely moving bound pair exists**.
   - Unitarity and locality hold on **all** sectors and densities, including infinite
     configurations. Each L_i is an involutive cellular automaton (Lemma I, proved for every
     configuration). So U is a reversible CA with inverse L1 ∘ L2.
2. **Range: the range-2 target is NOT met.** As a CA, U and U^{-1} have Chebyshev radius ≤ 6
   (each layer has radius ≤ 3; exact dependency-region computation). The empirical lower bound is
   4 (`c4e_04`; an earlier run with fewer effective samples found 3). As an automorphism (the (D-QCA) notion of range), α(A_x) ⊂ A_{B_18(x)} is proved (crude bound, below), and the review found an exact witness that α has range ≥ 5 (and α^{-1} ≥ 4). So the QCA range lies in [5, 18]. Whether a range-2
   realisation exists is **open**. At range 2 the strongest exact statement is item 3.
3. **Range 2: 3-magnon consistency (exact certificate, corrected after review).** Assume a monomial
   QCA of range 2, with frozen singles and the face glider (all other pairs fixed). Necessary
   conditions on its 3-magnon sector are F-, G- and X-locality (from α(Z_x), α(X_x) ∈ A_{B_2(x)})
   plus equivariance.
   - My `c4e_02` matching imposed only F/G-locality and stabilisers: 478 source = 478 target orbits,
     9002 orbit edges, matching 478/478. That map passes F/G-locality but has **336 X-locality
     conflicts** (found by the review), so `c4e_02` alone does **not** certify a range-2 sector.
   - **Certificate (the reviewer's, built on my candidate generator):** after X-local filtering
     (6142 of 9002 edges kept) a perfect matching 478/478 again exists, and the re-matched map passes
     F/G-locality and the full X-locality check on all 2,578,011 tested k ≤ 3 transitions
     (`review_scripts/logs/xfilter`, `xlocal_xfiltered`; 600 diameter-5 classes with diameter-6
     preimage skipped). I did not re-implement this within this block.

   So a T-equivariant monomial 3-magnon extension compatible with range 2 exists (k ≤ 3 only, with
   the stated coverage gap). This extends C4d's
   "pair + far magnon" test to the full 3-magnon sector. It does not reach k ≥ 4.
4. **Pair band** (exact, from the glider identity). Write |ρ, K⟩ = Σ_x e^{iK·x}|P_x(ρ)⟩. Then
   U|ρ,K⟩ = e^{−iK·v(ρ)}|ρ,K⟩. With U = e^{−iE}, E_ρ(K) = K·v(ρ) mod 2π, and the group velocity is
   ∇_K E = v(ρ), with |v| = 1 site/tick along the face normal. (The `c4e_04` log writes the
   eigenphase as ε = −K·v and calls −v the group velocity; that is the same statement in the
   opposite sign convention for the phase.)
   - There are six dispersive bands, one per face orientation. These are the only dispersive
     two-magnon bands; the other 56 near relative positions are static (flat).
5. **Single magnons do not move** (exact: U|x⟩ = |x⟩ and U^{-1}|x⟩ = |x⟩), as C4b Lemma 2 requires.
6. **Symmetry scope (exact checks).**
   - Covariant under all 12 elements of T.
   - **Not** O-covariant under the axis action. U commutes exactly with global particle–hole
     conjugation. So for odd R, covariance would need U P_R = P_R U, and that fails for all 12 odd R
     on the pair {0, e1+e2}.
   - **Not** covariant under the full (SU(2)) action. Under that action the pair sector would have
     to be O-covariant by pure permutations, and it is not.
   - This matches C4c Observation M and C4d P1: the glider exists only under T.
7. **3+ magnon clusters (exact simulation, descriptive).**
   - Of the 478 connected-triple orbits: 403 are static, 6 are periodic, 69 split (a pair escapes),
     and 0 move rigidly.
   - A pair meeting a single head-on is **reflected**. Its orientation rotates (1,1,0) → (1,−1,0),
     so its velocity reverses, and the single is not displaced. A laterally missed single is
     transparent.
   - Head-on pairs pass through each other, with a position shift of 0–2 sites.

## Premises (named, supplied)

- Lattice and Qubit axioms. **(D-QCA):** a TI finite-range automorphism, not necessarily Clifford.
  **(S):** soldering with the C4 conventions.
- **(U1):** conservation of Q_n (axis action). Vacuum: all spins along −n. Magnon = flipped spin.
  Under the axis action, even R act on-site by rotations about n, i.e. by phases e^{iθ_R N} in a
  fixed-N sector (C4b/C4d). Odd R act by P_R ∘ C (C = on-site flip, particle–hole), up to
  N-dependent phases.
- Range is the Chebyshev radius. A configuration is a set of occupied (magnon) sites.

## The construction

**Parity data.** par(z) = z1+z2+z3 mod 2. For the unit cube K(k) = k + {0,1}^3, let
B(k) = {z ∈ K(k) : par(z) ≠ par(k)} (the "B-tetrahedron"). Under T (signed even permutations with
an even number of sign flips, about any site) the lower corner of a cube maps to a corner of the
image cube at an even offset. So B is T-covariant. Odd elements of O swap B with its complement:
that is the only place where T versus O enters.

**Units.** A unit u has a site set S_u = D_u ⊔ D'_u, with two states. *Crossing* u replaces
c ∩ S_u = D_u by D'_u, or the reverse.
- **L1 units (squares):** every unit plaquette, with D and D' its two diagonals.
- **L2 units (tetra-axes):** for every cube k and axis j, S = B(k), D = B(k) ∩ {x_j = k_j},
  D' = B(k) ∩ {x_j = k_j + 1}. These are two opposite, parallel edges of the B-tetrahedron, both
  face diagonals.

**Rule.** u is a *candidate* in c if c ∩ S_u ∈ {D_u, D'_u}. Write N1(u) for the units ≠ u that share
a site with u, and N2(u) for the units that share a site with some unit of N1(u). Then u is
**active** in c if:
- (a) u is a candidate;
- (b) for **both** states of u, with the rest of c fixed, no unit of N1(u) is a candidate;
- (c) no unit of N2(u) ∖ (N1(u) ∪ {u}) is a candidate.

L(c) is c with every active unit crossed. The active units are site-disjoint, so this is
well-defined. L1 uses squares and L2 uses tetra-axes, and **U = L2 ∘ L1**.

**Lemma I (involution; proved, any unit family, any configuration).** For L defined this way,
L(L(c)) = c for every configuration c, finite or infinite.

*Proof.*
1. **Pairwise lemma.** Let Q1 ≠ Q2 both be active in c, and write c' = cross_{Q2}(c). Then:
   - (i) S_{Q1} ∩ S_{Q2} = ∅. Otherwise Q2 ∈ N1(Q1) is a candidate, which violates (b) for Q1.
   - (ii) Q1 is active in c'. By (b) and (c), Q2 ∉ N1(Q1) ∪ N2(Q1). So no unit shares a site with
     both Q1 and Q2. Crossing Q2 changes only S_{Q2}, so the content of a unit changes only if that
     unit lies in N1(Q2) ∪ {Q2}. Hence:
     - Q1's own content is unchanged (a).
     - The units of N1(Q1) are unchanged, for either state of Q1 (b).
     - A unit w ∈ N2(Q1) ∖ N1(Q1) either is unchanged, or lies in N1(Q2). In the second case,
       Q2's condition (b), which ranges over both states of Q2, says w is a non-candidate in c and
       in c' (c).
   - (iii) Q2 is active in c'. Its state flips, which (a) and (b) allow because they are symmetric
     in the state. The units of N2(Q2) ∖ N1(Q2) do not meet S_{Q2}, so they are unchanged (c).
2. **Invariance of the active set.** Activity of a unit u depends on c only through the finite
   region R(u) = ⋃_{v ∈ {u} ∪ N1 ∪ N2} S_v. Only finitely many active units meet R(u).
   - Cross them one at a time. By the pairwise lemma, the units of A(c) stay active at every step.
     So A(c) ⊆ A(L(c)), and this argument is local, so it applies to infinite c too.
   - Conversely, suppose u ∈ A(L(c)). In L(c), u and the units of A(c) that meet R(u) are all
     active. Crossing those units back one at a time keeps u active (pairwise lemma). It also
     reproduces c on R(u). So u ∈ A(c).
   - Hence A(L(c)) = A(c), and crossing the same disjoint units twice is the identity. ∎

**Consequences.**
- **Reversible CA and QCA.** L is a TI bijective CA that is its own inverse. Its radius is the
  largest distance from x to a site of some v ∈ {u} ∪ N1(u) ∪ N2(u) with u ∋ x: 3 for both layers
  (computed exactly in `c4e_04`). So U is a bijective CA of radius ≤ 6, with inverse L1 L2 of
  radius ≤ 6. U acts on the configuration basis as a permutation (no phases), and
  α(A) = U A U^† is an automorphism of the quasi-local algebra.
- **Support bound for α (proved, crude).** Let F have radius r and F^{-1} radius r'. For A on site
  x, ⟨d'|α(A)|d⟩ ≠ 0 only if d' agrees with d off B_r(x). Its value depends on F^{-1}(d) on
  B_{2r}(x), and so on d on B_{2r+r'}(x). Hence α(A_x) ⊂ A_{B_{2r+r'}(x)}. Per layer this gives
  B_9, and for U it gives B_18. This is an upper bound only.
- **U(1):** crossings permute sites, so N is conserved.
- **TI:** the unit families are TI.
- **T-covariance:** the unit families and the rule are T-invariant, and in fixed-N sectors the
  on-site phases cancel.
- **Particle–hole:** candidacy and crossing are complement-symmetric, so U C = C U.
- **Frozen singles:** a single magnon is in no candidate.

**The glider (proved).** Let P be a face pair with nothing else within reach. Its square Q is the
unique plaquette containing P, and the other two sites of Q are empty. No other square holds two
magnons, so Q is active and L1 crosses P to the other diagonal X(P) of Q. X(P) lies on the
opposite parity. It is an edge of exactly one B-tetrahedron, namely the one in the cube on the
v-side of P. Once more nothing else is a candidate, so L2 maps X(P) to the opposite edge,
which is P + v. For example, {0, e1+e2} → {e1, e2} → {e3, e1+e2+e3}.

*Why 3D and T matter.* Each face pair lies in exactly one plaquette and in exactly one
B-tetrahedron, so the two involutions never compete for an isolated pair. The B-tetrahedron is
defined only up to T. The 1D probe (`c4e_01`, intuition only) found no reversible radius ≤ 3 CA
with frozen singles and a moving pair. The C4c caterpillar and the C4d Prop. E commuting-shell
layers failed. This construction escapes Prop. E because its layers are **not** products of
commuting emptiness-controlled gates: condition (b) is a *non-emptiness* control, and the layer
is an involution of a self-consistent active set rather than a commuting product.

## Range-2 3-magnon consistency (`c4e_02` + review re-match)

*Reduction (necessary conditions; corrected after review).*
- **Monomial QCAs are permutations by reversible CAs.** Suppose U|c⟩ = e^{iθ(c)}|π(c)⟩. Then
  α(Z_x) = Σ_c z_x(c)|π c⟩⟨π c| is diagonal and supported in B_2(x). So π^{-1}, and likewise π,
  is a reversible CA of radius 2.
- **Low-magnon windows are fixed.** With frozen singles and W fixed, the local rules f and g are
  known on every window holding ≤ 2 magnons.
- **3-magnon sector.** A configuration c with a magnon z at distance > 2 from the rest (class D)
  maps to W(c∖z) ∪ z, by the spectator lemma. For a connected c (class C3), F(c) = known1(c) ∪ Y
  with Y ⊂ X(c) = ⋂_z B_2(z).
- **The unknowns are independent.** Each 3-magnon window value belongs to exactly one translation
  class of C3. So existence at k ≤ 3 **implies** an equivariant bijection C3 → (C3 ∖ π(D)) ∪
  {d ∈ D : π^{-1}d ∈ C3}, whose edges obey F-locality, G-locality and equal stabilisers. Equal
  stabilisers turn this into a perfect matching between orbits. The converse ("⇔") stated in an
  earlier draft is false: range 2 also requires **X-locality**, i.e. α(X_x): d ↦ π(π^{-1}(d) ⊕ x)
  may change only sites in B_2(x) and may depend only on d ∩ B_2(x). This couples different classes
  and is not encoded in `c4e_02`.

*Result.*
- **Consistency checks** (PASS): the D-part is self-consistent (π^{-1}π = id on spectator
  configurations), and the connected images π(D) are G-local.
- **Counts:** |π(D) ∩ C3| = 17 orbits and the D-targets are 17 orbits, so sources = targets = 478.
  Every source and every target has at least one admissible edge. The maximum matching is 478.
- **X-locality (review):** this matching has 336 X-locality conflicts (each involving one free C3
  choice; forced data alone are X-local, 0 conflicts). The reviewer's X-filtered re-match (6142 edges)
  is again 478/478 and passes all F/G/X checks on k ≤ 3 transitions tested. That re-match is the
  certificate for Result 3.

*Scope.*
- Monomial (permutation-with-phases) QCAs only.
- s = −1. The s = +1 case is the inversion conjugate: inversion commutes with T and maps W_s to
  W_{−s}.
- W is the glider on face pairs and the identity on all other pairs.
- k ≤ 3 only. A k = 4 analysis by the same method was not attempted: an estimated ~5·10^5 orbits,
  coupled to the k = 3 choice.

The construction above is not of range 2, so it does not settle range 2.

## What happens to clusters (`c4e_05`, exact simulation, descriptive)

| object | outcome |
|---|---|
| connected triples (478 orbits, range-2 connectivity) | 403 static, 6 periodic, 69 split (a free pair leaves), 0 rigid movers within 60 steps |
| pair {0,e1+e2} + single at (a,b,3), a,b ∈ [−3,4] | 48 transparent (no change); 16 **reflected**: the pair leaves as a (1,−1,0) pair moving −e3, single unmoved, with lag depending on (a,b) |
| head-on (1,1,0)↑ and (1,−1,0)↓ pairs, lateral offsets in [−2,2]², gaps 5, 6 | all 50 end as two free pairs that have passed through each other; positions shifted by 0–2 sites relative to free motion |

The "0 rigid movers" statement covers only those 478 orbits. Bound triples moving at larger
separation, and finite-density transport, were not analysed. Finite-density charge transport is
plausible, because pairs at density move ballistically until they collide, but it is not claimed.

## Checks and logs (`logs/SUMMARY.txt`)

| script | what it checks | result |
|---|---|---|
| `c4e_01_sat1d.py` | 1D intuition probe (SAT) | descriptive; UNSAT for r ≤ 3 with all windows; SAT only with ≤ 4-magnon windows |
| `c4e_02_k3_matching.py -1` | range-2 exact 3-magnon matching | PASS=4 FAIL=0 |
| `c4e_04_verify_construction.py` | L_i² = id on 58654 configs (all k ≤ 3 near the origin) + 17550 (all k = 4 in a 3³ box) + 1500 random finite configs (density 0.02–0.98); TI; N conservation; T covariance (12 g); O∖T failure; U C = C U; glider (1098 relative positions); range | PASS=11 FAIL=0 (re-run; first run PASS=10 FAIL=1, kept) |
| `c4e_05_clusters.py` | cluster dynamics | PASS=4 FAIL=0 |
| `c4e_06_independent_check.py` | **separate implementation**: flat-index torus code with units and N1/N2 built by brute-force site sharing. Involutions on L = 8, 10 tori at density 0.02–0.98; agreement with `c4e_layers` | PASS=5 FAIL=0 |
| `c4e_07_stress.py` | 700 packed face-pair configurations at the activity thresholds (4083 active-unit crossings); U^{−8}U^{8} = id | PASS=1 FAIL=0 |

Logged FAIL (kept): the first run of `c4e_04` predicted that the hole pair in the filled state would
be static. That made "no O covariance" rest on a false premise, and the check FAILed. It was false
because U is exactly particle–hole symmetric. The check was replaced by a direct particle–hole test,
and the O-failure argument now rests on U C = C U together with the permutation failure. The
earlier FAIL is recorded in `logs/c4e_04_first_run_FAIL.txt`.

## Claim types

| claim | type |
|---|---|
| Lemma I (each L_i is an involution on every configuration) | proved; implementation checked exhaustively on small sectors and by an independent implementation (same author) |
| U is a TI, T-covariant, U(1) QCA with frozen singles and the face glider | proved from Lemma I and the definitions; exact checks |
| CA radius ≤ 6 (empirical ≥ 4); QCA range ≤ 18 | proved upper bounds (computed / crude) |
| QCA range ≥ 5 | exact witness (review, `qca_range`) |
| not O-covariant (axis), not full-action covariant | exact (explicit witnesses) |
| pair band ε = −K·v, |v_g| = 1 | exact |
| range-2 monomial 3-magnon extension exists (k ≤ 3) | exact finite certificate: reviewer's X-filtered re-match; my `c4e_02` matching is only a relaxation (F/G) |
| cluster outcomes | exact simulation, descriptive (finite windows and times) |
| 1D UNSAT | SAT certificate for the stated 1D encodings only; intuition |

## No-go discipline / scope

- **Positive and exhibited:** the existence of a T-covariant one-qubit U(1) QCA on Z^3 with frozen
  singles and a genuinely moving bound pair. This answers the C4b/C4c/C4d open question at finite
  range: transport by bound pairs is possible.
- **Not achieved:** Chebyshev range 2. No negative claim is made at range 2. The k ≤ 3 sector is
  consistent there, and k ≥ 4 is untested.
- **Not claimed:** finite-density transport coefficients, O covariance (excluded), or
  physical identification of the glider with any framework excitation.

## Load-bearing step for independent check

The load-bearing step is **Lemma I, the pairwise lemma**. Check in particular:
- that (c) excludes Q2 ∈ N2(Q1), so no unit meets both;
- that units in N1(Q2) are non-candidates in both states of Q2 (condition (b) of Q2), which is
  what protects (c) of Q1.

Then check the glider identity for one orientation by hand: L1 crosses within the unique
plaquette, and L2 swaps opposite edges of the unique B-tetrahedron. Finally, check that the
B-tetrahedron is T-covariant but not O-covariant.

A blind route would be to implement the rule from this text alone and test L∘L = id on dense
random tori. `c4e_06` is such a second implementation, but by the same author.

## Novelty

Reversible CAs with gliders are classical (Margolus, BBM, Critters). Those are partitioned, and so
not TI under all translations. I know of no TI, point-group-covariant, number-conserving construction
of this "two involutions with self-consistent active sets" type, but I did no literature search. The
general Lemma I (activity via N1 in both states plus N2 exclusion makes any two-state-unit
crossing an involution) looks standard-style but is not recalled from a source. Novelty does not
bear on correctness.

## Reproduction

```bash
cd blocks/C4e/scripts   # OMP_NUM_THREADS=1 nice -n 10
python3 c4e_02_k3_matching.py -1        # ~6 min
python3 c4e_04_verify_construction.py   # ~11 min
python3 c4e_05_clusters.py              # ~15 s
python3 c4e_06_independent_check.py     # ~2 min
python3 c4e_07_stress.py                # ~2 min
python3 c4e_01_sat1d.py 2 cons one      # 1D probe lines as in logs/c4e_01_sat1d.txt
```

## Review dispositions (`REVIEW.md`)

The review reproduced the construction blind with two independent implementations (sparse and
dense), confirmed Lemma I step by step, and reproduced every table number.

| item | disposition |
|---|---|
| Fix 1: "range ≤ 6" is the CA radius, not the QCA range | **accepted.** Title and Result 2 now state CA radius ≤ 6 and QCA range in [5, 18] (≥ 5 by the reviewer's exact witness, ≤ 18 proved) |
| Fix 2: range-2 reduction omits α(X_x)-locality; "⇔" false; `c4e_02` matching has 336 X-locality conflicts | **accepted.** Reduction restated as necessary conditions with X-locality added; "⇔" withdrawn; Result 3 now cites the reviewer's X-filtered re-match (478/478, all F/G/X checks pass on tested k ≤ 3 transitions) as the certificate. Not re-implemented by me in this block |
| random-torus coverage thin; stress tests carry Lemma I's load | noted; no change |
| provenance of checks | noted: `c4e_06` is same-author; the review's implementations are a separate context, same model |
