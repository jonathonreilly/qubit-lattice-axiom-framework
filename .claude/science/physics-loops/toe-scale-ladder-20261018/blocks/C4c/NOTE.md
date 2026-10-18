# C4c — Bound-pair transport in U(1), O-covariant one-qubit QCAs: a vertex lemma, a scoped flat-band theorem, and one open glider channel

**Block:** C4c of `toe-scale-ladder-20261018`, a follow-up to C4b Lemma 3 (the open question: does
any U(1)-conserving, translation-invariant (TI), O-covariant one-qubit QCA on Z^3 have a nonflat
two-magnon band?). **Date:** 2026-10-18. **Status:** author note. It has not been independently
reviewed. No axiom, primitive or dynamics clause is adopted.

## Result up front

- **No dispersive bound pair is exhibited.** I give no explicit covariant QCA with a moving pair.
- **Scoped no-go (proved).** Take any finite product of
  - TI *commuting layers* of U(1)-conserving gates (each layer a closed O-orbit, so the layer is
    O-covariant by itself), and
  - covariant on-site gates.

  If every gate support is "covered" (defined below), the QCA is diagonal in the n-basis for the
  axis action, and is the identity for the full action. Covered supports include:
  - two-site gates at any separation (so phases on |11⟩ and XY/exchange-type gates);
  - every subset of a unit cube;
  - collinear triples;
  - the 7-site star;
  - collinear 4-site segments.

  As a result, **every** configuration is stationary, so all k-magnon sectors are frozen at any
  density. The 13 two-magnon bands are exactly flat, ε_ρ(K) = const, with group velocity 0. This
  holds at any range, because the covered/uncovered distinction depends on support shape, not
  range.
- **What is still open.** The question stays open for:
  - gates with ≥ 2 uncovered sites, e.g. a 3×3 square or the full 27-cell;
  - QCAs that are not circuits of commuting TI layers.

  Under the axis action, symmetry permits one deterministic channel. A face-diagonal pair
  {0, e1+e2} can step by ±e3 (the normal to its face) while staying consistent with its
  T-stabiliser. My declared prediction "monomial pair maps freeze pairs" therefore FAILs for T,
  and that FAIL is kept in the log. If some QCA realised this channel it would be a pair glider
  with v = 1 site/tick. None is constructed here.

The coordinator's scope note applies: flat pair bands are not a no-go for transport. The 3+
clusters and finite density are frozen **inside the covered family** only, and are open outside
it.

## Premises (named, supplied)

- Lattice/Qubit axioms; (D-QCA) TI finite-range automorphism, not necessarily Clifford; (S)
  soldering with C4 conventions. Covariance is α β_R = β_R α.
- U(1): α conserves Q_n = Σ n·σ (axis action, n = (1,1,1)/√3). For the full action C4b Lemma 2(a)
  gives SU(2). The vacuum is all spins along −n. Single magnons are frozen (C4b Lemma 2).
- C4b review: under the axis action the vacuum-fixing group is T. Even R act on U(1)-neutral
  operators as pure site permutations; odd R include particle–hole. The pair walk is therefore
  only T-covariant. Under the full action it is O-covariant: global SU(2) undoes the on-site part.

## Lemma K — two-magnon kinematics (proved; `logs/c4c_01`)

Let α have range r. Its inverse has neighbourhood −N = N (Arrighi–Nesme–Werner; recalled). For a
near pair c = {x, y} with 0 < |x−y|_∞ ≤ r:

1. α(σ⁺_x) and α(σ⁺_y) commute.
2. So W|x,y⟩ = A_x|y⟩ = A_y|x⟩. The first expression has its magnons in B_r(x) and the second in
   B_r(y), so all magnons lie in B_r(x) ∩ B_r(y).

The relation c ~ c' (all four cross distances ≤ r) is symmetric, and W and W^† are supported on
it. The near-pair space has d_1 = 13 = 3 + 4 + 6 and d_2 = 62.

This kinematics does **not** forbid motion. Of the 89 pairs related to {0,e1}, 88 have a different
centre of mass (COM), e.g. {0,e1} ~ {e2, e1+e2}. Any no-go must therefore come from QCA structure,
not from locality alone.

## Lemma F — a single commuting layer never transports (proved, any charge, any range)

Let L = ∏_r g_r, with [g_r, g_{r'}] = 0 and supp g_r = S + r. Then
L^n = ∏ g_r^n, and the factors that miss supp A commute with A and with the rest. So

supp L^n(A) ⊂ supp A + S − S for all n.

The light cone is bounded uniformly in n, so every band is flat. Transport requires at least two
mutually non-commuting layers, as in C4b E1. Numerical sanity check (ZXZ layer, ring L = 10):
|supp α^n(X_0)| = 5 for n = 1..12 (`logs/c4c_02` (d)).

**Why a layer must be commuting.** In a TI layer, every translate of a gate is applied. An infinite
product of non-commuting translates needs an ordering. Any ordering function that is invariant
under Z^3 is constant, so a non-commuting layer either is not TI or is not well defined. This is
the ordering issue for exchange gates: a "layer of XY gates on all bonds" is not a TI QCA.

## Lemma V — vertex lemma (proved; ingredients checked exactly in `logs/c4c_02`)

*Statement.* Let {h_r = τ_r h τ_r^{-1}} be a TI family of U(1)-conserving operators on one qubit
per site, each Hermitian or each unitary, with pairwise commuting translates and
supp h = S (h nontrivial at every site of S). Suppose s ∈ S and t ≠ 0 satisfy S ∩ (S+t) = {s}.
Then h acts **diagonally** (as a σ^z-basis control) at s and at s − t. Every vertex v of conv(S) is
such an s: take a generic ℓ with unique maximiser v and unique minimiser w, and set t = v − w.

*Proof.*
1. Write h_0 = Σ A_i ⊗ P_i and h_t = Σ Q_j ⊗ B_j, Schmidt-decomposed at the single overlap site
   s, with the A_i (resp. B_j) linearly independent. Then [h_0, h_t] = Σ A_i ⊗ [P_i, Q_j] ⊗ B_j,
   so V_s := span{P_i} and V'_s := span{Q_j} = τ_t V_{s−t} commute elementwise.
2. By U(1) invariance each span is a direct sum over the charges {1, σ^z}, Cσ⁺ and Cσ⁻.
3. Commutants (sympy, exact): comm(σ^z) is the diagonal matrices; comm(σ⁺) = span{1, σ⁺};
   comm(σ⁺, σ⁻) = C1.
4. For Hermitian h the spans are †-closed, so σ⁺ ∈ V ⇔ σ⁻ ∈ V. Then V ∋ σ^± forces the other span
   to be scalar, which contradicts the support assumption. For unitary h, a span inside
   span{1, σ⁺} would make the σ^z-coefficient of h^†h equal to G₊^†G₊/2, so G₊ = 0.
5. Hence both spans lie in span{1, σ^z}. ∎

A commuting unitary family can be reduced to the Hermitian case via h = −i log g (a function of g,
so it commutes with the same operators).

**Corollary C (proved).** Call a site *forced* if it arises as s or s − t above. Suppose at most
one site of S is unforced. Then h is diagonal: h ∈ diag^{⊗(S∖s₀)} ⊗ M_2(s₀), and a σ^± at the
single site s₀ would change the charge.

Covered supports, checked in `logs/c4c_02` and `c4c_05`:
- two-site bonds of any orientation and length;
- all 255 subsets of the unit cube (all in convex position; every vertex is a single overlap);
- collinear triples;
- the 7-site star.

Of 300 random subsets of the 27-cell, 283 are fully forced and 13 have one unforced site. So
296/300 are covered. This is a sample, not a theorem about all subsets. Not covered: the 3×3 square
(5 unforced sites) and the full 27-cell (19 unforced sites).

**Proposition S4 (exact certificate; `logs/c4c_04`, PASS = 5).** For the collinear 4-segment the
two interior sites are unforced. By Lemma V the most general h is
D(n_0..n_3) + Σ_κ [a_κ P_κ0 σ⁺_1σ⁻_2 P_κ3 + b_κ (h.c.-slot)], which has 24 unknowns.

- The commutator equations for t = 1, 2, 3 were solved by `sympy.solve`. Every branch has
  a_κ b_κ = 0.
- Independent route: for each κ, the Gröbner basis of the commutator ideal plus ⟨a_κ b_κ − 1⟩ is
  [1]. This uses the fact that the equations are homogeneous quadratic, so a Hermitian hop with
  |a_κ|² > 0 can be normalised to a_κ b_κ = 1.

So h is diagonal.

The direct two-site gate computation (`c4c_02` (c)) is a separate route. With generic symbolic
entries it shows that [g_01, g_12] = 0 forces the {01, 10} block of a U(1) gate to be diagonal.

## Theorem N — scoped flat-band theorem (proved from Lemma V / Cor. C / Prop. S4 and C4b Lemma 4)

**Family 𝓕.** α = L_m ∘ … ∘ L_1, where each L_j is either:
- a covariant on-site gate (axis: id or Ad σ_n^{⊗}; full: id, by C4b Lemma 4a); or
- a TI commuting layer ∏_r ∏_{R∈O} g^{(j)}_{R,r}, where the gate set is closed under the soldered
  O action, each gate is U(1)-conserving (axis: Q_n; full: SU(2)-invariant), and every gate
  support is covered (Cor. C or Prop. S4).

There is no bound on m, on the range, or on the number of orbits per layer.

**Claim.** Every α ∈ 𝓕 is diagonal in the n-eigenbasis:
- Lemma V/C/S4 applies to each gate's own translate family, since a gate must commute with its own
  translates. So every gate is diagonal.
- Ad σ_n is diagonal in the n-basis.

For the full action, a diagonal SU(2)-invariant α fixes σ_z everywhere, so α = id
(C4b Lemma 4b). Consequences:
- every configuration is an eigenvector;
- the k-magnon sectors for all k, and every finite-density state, are frozen (bounded light cone,
  in fact on-site supports for occupation numbers);
- the two-magnon walk is W(K) = diag(e^{iφ(ρ)}), up to the K-dependent gauge of the COM
  convention, so the 13 bands are flat and the group velocity is 0.

Explicit instance (`c4c_05` (b), 5³ torus, axis/face/body σ_nσ_n phases 0.31/0.57/0.23 and
Ad σ_n): the 13 bands are three flat levels with multiplicities 6/4/3, −2.1809, 2.7423 and 3.0623
rad, and band width 0.0.

## Observation M — monomial pair maps (exact certificate; `logs/c4c_01`, PASS = 6, FAIL = 1)

**Setup.** A "monomial" QCA has a two-magnon sector that permutes configurations, up to phases.
Covariance under the vacuum-fixing space group forces the image c' of each near pair c to satisfy
two conditions:
- c' ~ c;
- c' is fixed by Stab(c).

If every such c' has the same COM as c, the pair is frozen forever.

**Results.**
- **Full action (pure O permutations), r = 1:** every near pair is frozen (PASS).
- **Axis action (T only), r = 1:** six relative positions are exceptions, namely the face
  diagonals ρ = (1,±1,0), …. Their stabiliser is {1, C2 about the face normal}, so it fixes that
  normal. COM steps of ±e_⊥/… are allowed, e.g. {0,(1,1,0)} → {(0,0,1),(1,1,1)}. This is the
  FAIL line. The prediction was formed before the run but was not recorded in a file
  beforehand; disclosed.
- **r = 2:** 56 of 62 relative positions are exceptions under T, and 36 of 62 under O. This is
  informational only.

**The glider candidate.** The exception gives a symmetry-consistent pair glider. It can be built
from a two-layer caterpillar: P(z) ↔ Q(z+1), then Q(z) ↔ P(z+1), where P and Q are the two face
diagonals at height z. The two-layer form is T-covariant, which I checked by hand.

**Why I could not realise it.** Each layer must be a commuting family. With "rest of region
empty" controls, two active gates at distance just beyond the control radius toggle each other's
control. This boundary-shell conflict means the order of the gates matters (argued, not proved
impossible). Also, the four moving sites form a rectangle in convex position. By Lemma V they must
lie in the *unforced interior* of a larger gate support, which is outside the covered family.

## Answers to the tasks

1. **Family.** The honest family is 𝓕 above. Exchange-type 2-site gates cannot be put in a TI
   layer: their translates do not commute (Lemma V; also checked directly in `c4c_02` (c)). Layer
   ordering does not break O for 𝓕, because each layer is orbit-closed and commuting. Products of
   individually non-covariant layers are **not** covered. Within 𝓕, U(1) plus covariance leaves
   only diagonal phase type, so pairs cannot move (Theorem N).
2. **Two-magnon sector.** It has 13 internal states (3 axis + 4 body + 6 face, up to ±). For 𝓕,
   ε_ρ(K) is exactly constant (symbolically: W is diagonal and K-independent).
3. **Range 2 / three magnons.** Theorem N is range-independent, and its 3+-magnon sectors are
   frozen. The monomial r = 2 symmetry map is computed.
4. **Conclusion.** This is a proof of flatness, for all sectors, within 𝓕. It is not an exhibit.
   The open target is now sharper: a U(1) T-covariant QCA whose gates have ≥ 2 unforced sites, or
   that is not a commuting-layer circuit, realising the face-diagonal channel or some quantum
   nonflat W(K).

## Claim types

| claim | type |
|---|---|
| Lemma K, F, V, Cor. C, Thm N | proved (V's commutant facts are also sympy-checked) |
| Prop. S4 | exact computer-algebra certificate (two routes) |
| 296/300 sampled supports covered | sampled, not exhaustive |
| Obs. M | exact finite certificate; the glider is symmetry-allowed but **not realised** |
| Caterpillar shell conflict | argument, not a no-go |

## No-go discipline (brief)

- **N1, routes tried:**
  - single layers (frozen);
  - convex/forced supports (diagonal);
  - 4-segment (diagonal, exact);
  - monomial maps (r = 1 full frozen; axis open channel);
  - emptiness-controlled involution layers (shell conflict, not closed).
- **Not tried:** 3×3/27-cell gate supports; non-circuit QCAs.
- **N7, steelman.** Under the axis action a face-diagonal pair glider is symmetry-allowed at
  range 1, and non-convex gates could realise it. This is why **no universal no-go is claimed**.
- A numerical search script for non-convex supports (`scripts/c4c_03_commuting_search.py`) was
  written but did not finish within budget, at more than 8 min per restart. It has no log, and
  nothing is claimed from it.

## Reproduction

```bash
cd blocks/C4c/scripts
python3 c4c_01_pair_kinematics.py     # PASS=6 FAIL=1 (kept: falsified freeze prediction under T)
python3 c4c_02_vertex_lemma.py        # PASS=9 FAIL=0
python3 c4c_04_seg4_exact.py          # PASS=5 FAIL=0 (~ minutes; Groebner)
python3 c4c_05_forcing_and_bands.py   # PASS=4 FAIL=0
```
Combined: PASS=24 FAIL=1.
