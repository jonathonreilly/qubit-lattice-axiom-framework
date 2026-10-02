# Hostile review: Lane G (composition law and dynamics between records), c7/hard/dynamics/REPORT.md

Derivation only: no code was run and no files were written. Every source cited is on origin/main at `0485dc0738`. "EXACT" below means I re-derived the step by hand.

**Headline:** Part A's mathematics mostly holds, but its framing is overstated. B4 is a correct lemma, but it rests on a premise that is equivalent to its own conclusion. B7's "J ≠ 0 is forced" is wrong in the covariant setting, and the §5(b) decisive test as specified cannot show anything. The clause wording has three substantive defects. The report also never states that the clause would rule out the active fermion lane's and the photon ring model's generators as microscopic terms.

## Verdict table

| Claim | Verdict |
|---|---|
| A1 (classification of gradings) | HOLDS WITH NARROWED SCOPE (incomplete list; Θ is a real-algebra automorphism) |
| A2 (mutual exclusion) | HOLDS (EXACT); it bites solely in the real category |
| A3 exclusion lemma | HOLDS (EXACT; shorter proof below) |
| A3 confinement to ±n | HOLDS WITH NARROWED SCOPE (Reach is a supplied premise, not an argued one) |
| A4, A4′ | HOLDS (EXACT), with premises that need listing |
| A5 (spanning) | HOLDS for distant pairs; adjacent pairs ARGUED; axis-soldering case missed |
| A6 (tensor product) | HOLDS in the complex category; GAP in the real category that S1 explicitly admits |
| A7 (generation) | ARGUED, and load-bearing in the real category |
| Result A | HOLDS WITH NARROWED SCOPE; "fixed by Record" is overstated |
| B1–B3 | HOLD (already landed in notes 9084/9086 plus Stone); not new |
| B4 (clique lemma) | Algebra HOLDS (EXACT); "bipartite" should be "triangle-free"; A-diff is a supplied premise equivalent to the conclusion |
| B5 (Heisenberg) | HOLDS (landed note 9040), given possibility covariance, which the clause does not contain |
| B6 (Θ and sign of J) | Algebra HOLDS; "sign J is a convention" needs narrowed scope |
| B7 field identity and fingerprint | HOLDS (already landed in note 9041) |
| B7 "J ≠ 0 forced" | WRONG under possibility covariance |
| §5(b) spec | WRONG: a maximally mixed start makes the test vacuous |
| Minimal clause wording | GAP: three defects, plus costs the report does not state |

## 1. Part A re-derived

### A1, and whether Θ is an automorphism of the complex algebra (Q1)

The basic facts check out (EXACT):
- Θ(A) = σ_y Ā σ_y is multiplicative and preserves adjoints.
- It sends σ_k → −σ_k and i → −i, so it is antilinear.
- It is therefore an automorphism of M_2(C) as an 8-dimensional real algebra, i.e. the grade involution of Cl(3,0). It is not an automorphism of the complex algebra.
- Uniqueness checks out. Commuting with every Ad(V) gives UV̄ = cVU. Using V̄ = σ_yVσ_y for V in SU(2), Uσ_y must be central, so U ∝ σ_y.
- Cl(3,0) graded with itself gives Cl(6,0) ≅ M_4(H), as the report says.

The antilinearity matters in two ways.

**(a) Complex S1 rules Θ out before any appeal to Record (EXACT).** If B is complex and the embeddings ι_x are complex-linear, then ι_x(i) = i·1_B is central and even. Under Θ, i_x is odd and anticommutes with ι_y(σ_k), which is impossible. So in the category where A6 applies, the Θ-graded composite is excluded by kinematics and A2 does no work.

**(b) Real S1 keeps Cl(3n,0) alive, but breaks A6 (GAP).** A2 is pure *-algebra, so it still holds. Two things change:
- **A6 no longer gives a unique product.** `GENERATED_FINITE_COMPOSITION_MINIMALITY` states its scope as "finite-dimensional complex C-star". Over R, M_2(C)⊗_R M_2(C) ≅ M_4(C)⊕M_4(C).
  - Commuting, generating real copies therefore leave a central relative-orientation label, i_x·i_y. Generation does not remove it, because the direct sum is itself generated.
  - One of the two sectors identifies site y's complex unit with the opposite sign (ι_y(b) = 1⊗b̄). That structure is not isomorphic to the standard one.
  - A7 (ARGUED) then has to carry the uniqueness claim.
- **A1's list is incomplete.** It omits the antilinear real structures A ↦ UĀU† with UŪ = +1. These give the graded algebra Cl(1,2), and each one picks an axis.

This does not change the verdict, because A4 is general and the lemma below covers every family. It also bears on B6: "Θ is a relabelling" needs the real presentation, while a clean A6 needs the complex one. The report uses both, and should pick one category.

### A2 (EXACT)

All three parts check:
- If uψ = vψ = ψ, then (uv+vu)ψ = 2ψ = 0.
- PvP = (v + uvu)/4 = 0, so PQP = P/2.
- Σ± P±QP± = ½.

A2 can be strengthened. In the Θ composite each site's even part is H (the quaternions), which has no nontrivial projectors. So every possible record is odd, and any two records at distinct sites exclude each other.

### A3

**A one-line proof replaces the Jordan–Wigner frame computation (EXACT).** Split each record operator into even and odd parts: u = a + b and v = c + d. In a graded product:
- a and c commute with everything at the other site;
- b and d anticommute with each other;
- so [u,v] = 2bd, and (bd)² = −b²d² = −|n_odd|²|m_odd|².

If both odd parts are nonzero, [u,v] is invertible, so u and v share no eigenvector at all. This covers axis gradings, Θ, and the omitted real structures. It is also independent of the instrument used: no joint lock exists, whatever forms it. The report's frame computation is also correct.

**Confinement to ±n.** I would not label this EXACT. It is conditional on Reach. Reach says that a condition C recurs at a distant y, which then forms using an instrument with an off-axis Kraus operator. That is a premise about where and how fast formation happens, and the axiom memo explicitly assigns that to downstream suppliers. So Reach should be listed as a supplied input, not as ARGUED.

The report also misses one case. Under axis soldering (s|g|, which decomposes as A2 + E), the line along (1,1,1) is invariant. So an axis grading along (1,1,1) is lattice-covariant there too, not just under the trivial and sign-twist actions.

What A3 adds over landed work is a lock-based mechanism. The restriction itself is the price already recorded in `MATTER_RECORD_GRADING…` (Theorem 1, and Option G: "One-site readable quantum events are restricted to the fixed parity PVM"). With standard parity superselection the confinement is automatic.

### A4 and A4′ (EXACT)

QP = PQP holds when Tr(Qρ) > 0. When Tr(Qρ) = 0, then QP = 0. Either way [P,Q] = 0, so the step from QP = PQP for all Lüders formations to [A_y, P] = 0 is sound.

The general-instrument version is also correct. The set {X : (1−P)XP = 0} is a non-* algebra, so you need the non-* algebra generated by the Kraus operators of every instrument used after the lock to equal A_y. A single Lüders menu generates a commutative 2-dimensional algebra, which is not enough.

Premises the report leaves unstated:
- a faithful prior;
- histories in which x forms, then y forms, with nothing between (part of Reach);
- for A4′, states that separate B, i.e. no superselection.

This is the standard theorem that non-disturbance holds exactly when the observables commute.

### A5, Result A

The span criterion and the octahedral-orbit argument are EXACT. For adjacent pairs, the deterministic-repeat case leaves the antisymmetric part of [σ_a^x, σ_b^y] unconstrained, so adjacent pairs remain ARGUED, as the report says.

The corrected statement of Result A is:

> In the complex category, under these premises, distant site algebras commute (EXACT), adjacent ones are ARGUED, and A6 gives the ordinary product.
> - Premises: S1 (generated), L, F, a faithful prior, Reach (supplied), and spanning (full soldering, possibility covariance, or the "not privileged" reading).
> - The axis grading is excluded by Record together with the spanning/Qubit reading, not by Record alone.
> - Θ is excluded by complex-linearity. In the real category it is excluded by A2, but A6 then fails.

## 2. Fermions (Q2): no contradiction with landed science

Result A excludes site-level gradings. It does not exclude encoded fermions. The landed notes claim the following:

- **`MATTER_RECORD_GRADING_SAME_CARRIER…`**
  - On its finite typed products, "those displayed data do not select the cross-site product".
  - "No global four-axiom model or covariant lattice-wide role law is constructed."
  - It gives a two-mode even code carrying a full logical qubit.
  - Its retained routes include "a rotation-covariant real Clifford carrier".
  - Result A, under its premises, rules out Options G and M as site-level laws. A2 rules out the real-Clifford route, in the real category.
- **`COMPOSITION_DISCRIMINATOR…`** compares "ungraded and Jordan-Wigner ladders". A physical record reading "additionally requires separately supplied ground-state/Born and occupation-to-record bridges". It is a conditional comparison of finite matrices.
- **`COMPOSITION_LAW_SELECTION…`**: "Neither a grading clause nor an encoding clause is established as necessary or sufficient by this census."
- **PR 7834's note, since renamed `FINITE_BKSF_SIGN_AND_SUPERLATTICE_MARKER_CENSUS…`**:
  - It uses no "Jordan-Wigner strings, graded tensor products"; its fermions are an encoding inside the ordinary tensor product.
  - "These results do not construct one framework Admissibility law."
- **`RECORD_READOUT_LOCALITY…_EXCLUDES_THE_GRADED_ONE` (09-24)**: this already selects the ordinary composite, using local tomography, and states it "does not exclude every graded theory: larger even logical encodings… change the question".

So Result A is consistent with landed science. The report's line that fermions live in multi-site even encodings is right. However, B4 (next section) then rules out those encodings' hopping terms as microscopic generator terms. The report does not mention this.

## 3. B4 clique lemma (Q3)

**The construction checks (EXACT).**
- T = T_x ⊗ S_rest is a Hermitian Pauli string.
- Its N[x]-marginal vanishes because S_rest at z is not the identity.
- The only strings that contribute are σ^a ⊗ S_rest (a = 0..3). The a = 0 term commutes with T.
- [A⊗B, C⊗B] = [A,C]⊗B² with B² = 1, so L_x(T) = 2^{|W|−1}[M, T_x] ≠ 0.
- Terms not containing x drop out under the partial trace.
- The converse holds.

**Bipartite vs triangle-free.** The lemma needs triangle-free, not bipartite.
- Z³, open windows, and tori with L ≠ 3 are triangle-free.
- The L = 3 torus has triangles {x, x+e, x+2e} along each axis. Landed note 9040's covariance checks use exactly that 3×3×3 torus.
- A-diff must hold for all states. On the states the process actually reaches (§5 below), every H passes.

**A-diff is a supplied premise, not a faithful reading of Admissibility.** It differs from the axiom on three points:
- **Object:** it constrains the rate of change of the reduced state, not the formation distribution.
- **Data:** it conditions on the full quantum marginal, including the site's own state, not on neighbour conditions.
- **Time:** it is infinitesimal. Finite-time locality fails; note 9084 says "Heisenberg evolution spreads operators beyond one bond at nonzero time".

Two consequences:
- **The finite-time reading would force H to be trivial (ARGUED).** Requiring ρ_x(τ) to be fixed by ρ_{N[x]}(0) at every τ, under possibility covariance, would force J = 0, because Heisenberg spreads operators at second order.
- **B4 renames a decision rather than removing it.** B4 is an equivalence, so it moves D-dyn's "sum of two-site terms" into the clause's last sentence. The claim that this decision "stops being an independent decision" is overstated.

**Costs the report does not state (EXACT, given the supports quoted from the landed notes).** Under A-diff the following cannot be microscopic generator terms; they could at most be effective:
- the weight-5/7 star term behind the chiral Majorana Chern bands (#9112);
- the composite-site bonds J τ_i^λ τ_j^λ (σ_i·σ_j), four qubits on a non-clique. This is the current fermion lane;
- BKSF hopping;
- the photon ring term U_p (four link qubits).

Separately, possibility covariance (B5) excludes the compass K term that the Kitaev carvings (notes 9048 and 9054) need. Those carvings are compatible with B4 under full soldering.

## 4. B1–B3, B5–B7

**B1–B3.** These are landed results plus Stone's theorem. The CP note's premises are "operational availability of arbitrary finite ensembles", branchwise evolution, no-signalling, tomography and ancilla-extension positivity. That note is conditional and unaudited, so B1 should be labelled conditional rather than citing it as landed authority.

**B5.** The result needs possibility covariance, plus translation and rotation covariance of H. Note 9040 calls possibility covariance "an option, not adopted". Neither is in the clause wording.

**B6.** The algebra is EXACT: K is Θ-invariant, J flips to −J, and every lock p goes to −p. The equivalence between the J and −J worlds, however, needs two things:
- a preparation that is Θ-invariant and does not depend on H;
- Θ-covariant formation.

Energy-selected preparations break it. A Gibbs state at β in the J world maps to one at −β in the −J world, so sign(βJ) is physical. Note 9041 already records ground-state relaxation giving "c = 1 for J < 0 (repeat certainty) and c = -1 for J > 0". "No free continuous parameter" applies to H, not to the clause together with formation, which still leaves the ratio γ/J free.

**B7 "J ≠ 0 forced" is wrong (EXACT).** Start from 1/2^N, the only possibility-covariant product preparation. By induction the state is always P_R ⊗ 1_U/2^{|U|}:
- Lüders formation or coherent-state formation gives odds of ½ and keeps the unrecorded block maximally mixed.
- The compressed unitary evolution fixes 1_U.

So every formation odds is ½, for every J, rate and order, and "varies with" fails whatever J is. With entangled covariant preparations, J = 0 already produces variation through steering; note 9046's Bell-state control is "readable despite no coupling". So "varies with" does not force J ≠ 0 under possibility covariance. The conclusion holds solely for product preparations that are not maximally mixed, and those privilege directions.

## 5. §5(b) is vacuous as specified

With the stated start 1/2^N, the finished law is uniform and a product. The cross-ratio test passes trivially, so outcome (A) appears at every γ and would be misread as "the clause is compatible with the static reading". The report's own expected outcome, (B), cannot appear.

To make the test meaningful:
- use a declared non-trivial preparation, such as the ring's Heisenberg ground or Gibbs state at a stated β, a singlet covering, or a declared pure product state;
- run a "varies with" check, i.e. non-constant conditionals, before the cross-ratio.

## 6. The minimal clause

1. **"One joint possibility state, built from their site domains alone" does not force operator kinematics.** Classical spin dynamics satisfies all three sentences: a Liouville flow on (S²)^N with ds_x/dτ = J s_x × Σ s_y is continuous, reversible, homogeneous and nearest-neighbour, and has CHSH ≤ 2. The clause must name a joint state on the algebra generated by the site domains, with complex-linear site embeddings (see A6).
2. **"State" collides with the axioms' wording.** The axioms' Qualification says "A state is a configuration of records".
3. **"Set by its nearest neighbours" omits the site itself, and that open-neighbourhood reading forces H = const (EXACT).** For ρ = (1/2)⊗ω, L_x = 0 because Tr[P_rest, ω] = 0. Every ρ shares its open-neighbourhood marginal with such a state, so L_x ≡ 0 for every x, and B4's computation then kills every term. The wording must say "the site together with its nearest neighbours".
4. **Missing pieces:**
   - covariance of the change under translations and rotations;
   - possibility covariance, which B5 needs;
   - how records interact with the change (compression);
   - the preparation, which is load-bearing (§4).
5. **"Minimal" is not shown.**

## 7. Required corrections

1. Choose the complex category throughout. Exclude Θ by complex-linearity. Keep A2 as the result for the real-category route and state that A6 needs complex S1 (otherwise the orientation sector appears and A7 has to carry it).
2. Complete A1 with the Cl(1,2) real structures and the (1,1,1) axis-soldering case, and replace the A3 frame computation with the [u,v] = 2bd lemma.
3. Relabel Reach as a supplied premise about formation site and rate. List L, F, a faithful prior and the no-superselection condition among A4's premises.
4. Retitle Result A: Record permanence plus spanning supports fix commuting composition. Do not credit Record alone.
5. In B4, write "triangle-free (L ≠ 3)", present A-diff as a supplied premise equivalent to D-dyn's two-site form, and state the costs to the star-term, composite-site, BKSF and ring generators.
6. Retract "J ≠ 0 forced" (or narrow it as in §4) and fix the §5(b) preparation.
7. Scope B6 to Θ-invariant preparations that do not depend on H.
8. Repair the clause wording as in §6, items 1–4.

## Bottom line: what is new against the landed dynamics-clause campaign

**New:**
- **A4 as a route for the framework.** Lock permanence gives commuting site algebras. This is a Record-native replacement for the local-tomography premise of the 09-24 note. The mathematics is standard.
- **A2 applied to Θ.** In Cl(3n,0) at most one record can exist. This bears on the landed "real Clifford carrier" route, in the real category.
- **The B4 equivalence lemma.**
- **The Θ map between the J and −J worlds**, once narrowed as above.

**Already landed:**
- B1–B3 (notes 9084/9086);
- B5 (note 9040);
- B7's field identity and vector-sum fingerprint (note 9041);
- O1 (notes 9043/9046);
- generation (07-13);
- the axis-grading price (09-01).

**Defective:** B7's "J ≠ 0 forced", the §5(b) specification, and the clause wording.

The report never puts the most important consequence in front of the owner: adopting the clause together with A-diff would turn the active composite-site fermion lane and the photon ring model into effective theories only.

The report's arXiv identifiers were not re-verified; none of them is load-bearing.