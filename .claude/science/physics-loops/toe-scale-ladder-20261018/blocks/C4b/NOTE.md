# C4b — Beyond Clifford: index lemma, charge sectors and partitioned QCAs for cubic-covariant one-qubit dynamics

**Block:** C4b of `toe-scale-ladder-20261018`, a follow-up to `blocks/C4/` (OBL-R1.2: a
one-qubit-per-site dynamics compatible with the soldering (S) that propagates in 3D).
**Date:** 2026-10-18. **Status:** Independently reviewed (REVIEW.md); unaudited. No axiom,
primitive or dynamics clause is adopted.

## Result up front

The question was: does any one-qubit-per-site, Z^3-translation-invariant (TI) QCA that is
O-covariant under the **axis** or **full** soldering action transport anything? There is no
complete answer here. The block gives one exhibit inside the premise and four lemmas. Together
they cut the open part down to one precise sub-question.

1. **Something does propagate inside the premise (exhibit, exact certificate).** Compose the two
   commuting-Pauli-rotation circuits from C4:
   - α_C, built on Chamon strings X(±x)Y(±y)Z(±z);
   - α_K, built on the 12-site cuboctahedral string.

   The composite α_C α_K is a TI, one-qubit, O-covariant Clifford QCA of range 4, for both the
   axis and the full action. Its trace polynomial τ is nonconstant (24 monomials, the orbit of
   (4,2,0)), so operators spread ballistically. Exact iteration confirms this: the Chebyshev
   radius of α^n(X_0) is 4n for n = 1..8, and in fact for every n: range 4 gives the upper bound,
   and C4 Theorem 2(c) at the vertex (4,2,0) gives the lower bound. The result holds in both
   layer orders, as the reviewer checked. C4's finding "nothing propagates under soldering" is
   therefore a statement about range ≤ 2 only. What spreads is operators. No local-operator
   glider exists (C4 Theorem 2(d), O, any range). Motion of excitations relative to an invariant
   state is **not** addressed, and no invariant state of E1 has been identified.
   `logs/c4b_05_commuting_layers.txt`.
2. **Non-Clifford covariant QCAs exist inside the premise (proved).** The family
   α(θ1,θ2) = Ad(∏_r e^{iθ1 C_r} ∏_r e^{iθ2 K_r}) is TI and O-covariant (axis and full) for every
   θ. This holds because β_R(C_0) = +C_0 and β_R(K_0) = +K_0, with the sign checked, and each
   family's translates commute. It is non-Clifford for generic θ, and the C and K layers do not
   commute. Its transport at generic θ is **not established**: it has no conserved charge and no
   identified stationary vacuum.
3. **Index lemma (proved, given recalled GNVW facts).** Take any TI QCA on Z^3, of any range and
   with any finite cell. Suppose it is covariant under a subgroup H ≤ O that fixes no nonzero
   vector, with any on-site action. Then its strip-compactified GNVW index is 1 in every lattice
   direction, for every admissible transverse size. So there is no net chiral flow, and every
   compactification is a 1D finite-depth circuit. This rules out shift-type transport. It does
   **not** rule out transport of excitations, and it does not imply that the 3D QCA is trivial.
4. **Charge sectors (proved, any range, non-Clifford).**
   - *Single particles.* Suppose a TI one-qubit QCA conserves an on-site U(1) charge
     Q = Σ_r m·σ_r. Under full soldering this forces global SU(2) symmetry. Under axis soldering
     it forces m = ±n, with n = (1,1,1)/√3, or else global SU(2). If the QCA is also O-covariant (or only T-covariant)
     under any menu action, its one-particle sector is a constant phase.
   - *Pairs.* Two particles then move only as a **bound pair within the range r**. The pair
     sector splits as (frozen far-apart states) ⊕ (a finite-coin quantum walk of the pair
     centre). The walk is covariant under the vacuum stabiliser H_m, which is T for the axis
     action and O for full/SU(2). The coin space is the set of near-pair relative positions.

   A nonflat pair band is **sufficient** for in-premise U(1) transport, but **not necessary**.
   Bound clusters of k ≥ 3 particles and transport at finite density or above other vacua remain
   open.
5. **Diagonal and on-site route (proved).**
   - Full action: the only covariant on-site automorphism is the identity, and every covariant
     QCA that fixes σ_m at every site, for any axis m, is the identity.
   - Axis action: the covariant on-site automorphisms are {id, Ad σ_n}. QCAs that fix every
     σ_n exist, and they include non-Clifford, entangling, range-1 examples (exhibited). Every such
     QCA is frozen: the support of α^k(A) is bounded uniformly in k.
   - So "controlled-phase/diagonal layers + covariant on-site gates" moves nothing, under either
     action.
6. **Partitioned (Margolus 2×2×2) QCAs leave the premise (exact check).** The alternating pair
   (P0, P0+(1,1,1)) is preserved exactly by 2Z^3 ⋊ O_c, where O_c is O about a cube centre:
   - O about a site is **not** a symmetry; only the C3 about (1,1,1) survives.
   - e_1 is not a symmetry.
   - (1,1,1) is a symmetry only up to the half-step glide.

   Inside that relaxed symmetry, SU(2)-invariant O_c-covariant blocks work for every soldering
   action. They transport single magnons ballistically, with maximal group velocity 2 per two-step.
   With a block that is the identity on ≤ 1 magnon per block:
   - one magnon is frozen (exact);
   - two magnons are confined to one cube (proved, and checked exactly);
   - all 120 sampled 3-magnon clusters are confined (exact closed reachable sets);
   - 9 of 40 sampled 4-magnon clusters have reachable sets that are not closed. The weight that
     leaves stays below 5e−8 within 6 two-steps, so no probability-weighted transport was found.

**Bottom line.** Inside the premise (Z^3-TI, one qubit, axis/full O-covariance) there is now an
exhibit that propagates: ballistic operator spreading at range 4. There is still **no exhibit that
transports a localized excitation or a conserved charge**. For conserved charges, a nonflat
pair walk (Lemma 3) would suffice. The k ≥ 3 cluster sectors and finite-density transport are also
open. No moving-particle framework-compatible dynamics is claimed.

## Premises (all supplied; named)

- **Lattice and Qubit axioms** (`docs/MINIMAL_AXIOMS_2026-06-29.md`): Z^3, translations, O about
  each site, and M_2(C) per site.
- **(D-QCA), supplied dynamics premise.** A tick is a *-automorphism α of the quasi-local algebra.
  It is TI under Z^3 and has finite range r. It is **not** assumed to be Clifford.
- **(S), soldering.** These are C4's conventions. β_R = (on-site rotation by Q(R)) ∘ (site
  permutation r → Rr). The menu is trivial, sign diag(1,s,s), axis s|R| and full R. Covariance
  means α β_R = β_R α for R ∈ H ≤ O. Every Q(R) lies in SO(3), so β_R's on-site part is a global
  SU(2) rotation D(Q(R))^{⊗Z^3}.
- **"Transport"** is used in three graded senses, which are kept apart throughout:
  - (T1) net flow, meaning a nontrivial index;
  - (T2) ballistic operator spreading, meaning a light cone that grows linearly;
  - (T3) motion of a localized excitation or of a conserved charge, meaning a glider, a moving
    particle or a bound state with nonzero group velocity.

  OBL-R1.2 in the map asks for T3. T2 is weaker.

## Lemma 1 — symmetry kills the index (proved, conditional on recalled GNVW properties)

**Definition used.** For a 1D QCA γ on a chain of finite cells, ind(γ) ∈ Q_{>0} is the GNVW index
(Gross, Nesme, Vogts, Werner, CMP 310 (2012) 419). The following properties are *recalled, not
re-derived*:
- (I2) ind(γδ) = ind γ · ind δ;
- (I4) the right shift of d-dimensional cells has index d;
- (I5) ind γ = 1 iff γ is a finite-depth (two-layer block-partitioned) circuit;
- (I6) the index is invariant under cell-wise algebra isomorphisms, and an on-site unitary layer
  has index 1;
- (I7) ind(PγP^{-1}) = ind(γ)^{-1} for the spatial reflection P.

(I7) is a consequence of the definition as a ratio of right-moving to left-moving information.
`scripts/c4b_01_index_sanity.py` checks I2, I4, I7 and I8 = (I2 + I6) numerically on 8-site qubit
rings, using an independent formula: the Choi-state mutual information of Ranard–Walter–Witteveen
(AHP 2022), also recalled. All 10 cases agree exactly, e.g. ind(P S W P^{-1}) = 1/2
(`logs/c4b_01_index_sanity.txt`, PASS=10 FAIL=0). This is a sanity check of recalled facts, not a
proof of them.

**Strip compactification.** Let α be TI with range r, and let α^{-1} have range r'. The inverse of
a QCA is a QCA (recalled). Fix a direction e_i and L > 4·max(r,r'). Define α_L^{(i)} on
Z × (Z/L)^2 by reading the local rule of α with the transverse coordinates taken mod L. It is a
*-homomorphism, because every algebraic relation among images involves only sites within diameter
4·max(r,r') < L, where the wrapped and unwrapped rules coincide. The same construction for α^{-1}
gives its inverse. So α_L^{(i)} is a 1D QCA along e_i with cells of dimension 2^{L^2}. Put
f_i(L) := log ind(α_L^{(i)}).

**Lemma 1.** Let α be H-covariant, for H ≤ O, under any on-site action of the form
β_R = Ad(u_R^{⊗}) ∘ π_R. Then f(L) = (f_1, f_2, f_3)(L) satisfies f = R f for every R ∈ H. If H
fixes no nonzero vector, then f(L) = 0 for every L. This covers O, T, D4, D3 and the axis D2. So
every compactification is a finite-depth circuit (I5): there is no net flow through any lattice
plane.

*Proof.*
1. Write R e_i = s e_j with s = ±1, since R is a signed permutation.
2. π_R α π_R^{-1}, compactified along e_j, equals the relabelling by R of α compactified along e_i.
   Under this relabelling the chain coordinate becomes x → s x, and the transverse torus maps
   bijectively onto the transverse torus, so this is a cell-wise isomorphism.
3. By (I6) and (I7), f_j(π_R α π_R^{-1}) = s f_i(α).
4. The on-site layer drops out by (I2) and (I6).
5. Covariance gives β_R α β_R^{-1} = α. Hence f_j(α) = s f_i(α) for every i, that is, f = R f.
∎

*Scope.* The lemma excludes T1 only. Trivial index does not exclude T3: two oppositely moving
sublattice shifts have index 1. It also does not make the 3D QCA a circuit: nontrivial 3D QCAs
with trivial flow are known (Haah–Fidkowski–Hastings). The underlying observation, that an
O-invariant translation is 0, is elementary. The content of the lemma is that it survives all
non-Clifford, higher-range, entangling corrections. *Novelty:* likely folklore. The flow for 2D TI
QCAs is in Freedman–Hastings, CMP 376 (2020) 1171 (recalled). No literature search was done.

## Lemma 2 — conserved on-site charge: single particles are frozen (proved, any range)

Let α be TI and one-qubit, and suppose α commutes with the U(1) automorphisms
γ_φ = Ad(e^{iφ Σ_r m·σ_r/2}) for some unit vector m.

(a) **Which charges are compatible with soldering.** Covariance gives α γ'_φ = γ'_φ α, where
    γ'_φ = β_R γ_φ β_R^{-1}, which is the same U(1) with m replaced by Q(R)m. Two cases:
    - Full action: the O-orbit of any m spans R^3 (`c4b_02`, exact). α therefore commutes with
      the U(1)s of three independent axes, hence with all of global SU(2).
    - Axis action: Q(O) ≅ D3 preserves only the line ±n, with n = (1,1,1)/√3. Any other m again
      generates SU(2). Odd R map Q_n to −Q_n, which is still conserved.

(b) **The single-particle sector is a constant phase** under full, axis, trivial or sign soldering
    with H = O, and in every case under H = T.
    1. On the torus (L > 4r; construction as in Lemma 1), α_L = Ad(U_L). The automorphism
       Ad(U_L) commutes with Ad(e^{iφQ}). So U_L Q U_L^† = Q + c, and c = 0 because the spectrum
       is fixed.
    2. Take the vacuum to be all spins along −m, the unique minimal-charge state, so it is an
       eigenvector. The one-particle states are |x⟩ = σ^+_x|Ω⟩.
    3. TI makes U_L act on one-particle states as u(k) = Σ_t a_t e^{ik·t}, with finitely many t
       (|t|_∞ ≤ r) and with a_t independent of L.
    4. |u(k)| = 1 on (2π/L)Z^3 for all large L, hence on all of the torus. So u ū = 1 as a
       Laurent polynomial, and units of C[x^±] are monomials: u = e^{iφ} e^{ik·t₀}.
    5. The subgroup H_m ≤ H that fixes the vacuum acts on |x⟩ by |x⟩ → c_R|Rx⟩, with |c_R| = 1
       independent of x. This gives u(Rk) = u(k), so R t₀ = t₀.
    6. The fixing subgroup H_m always contains T (here H ⊇ T):
       - trivial, sign and axis actions: their kernel, which is T for sign and axis, acts on-site
         either trivially or by rotations about m;
       - full action: after SU(2) symmetry is used to undo the on-site part.

       T fixes no nonzero vector, so t₀ = 0.

(c) This is the many-body analogue of the 10-16 walk freeze, but it covers any range, unlike the
    walk freeze. It differs from that note's coin setting: here a particle is an excitation of a
    one-qubit-per-site many-body QCA and carries **no** internal coin. That is why it freezes at
    every range.

## Lemma 3 — pairs move only as tight bound pairs on a finite-coin walk (proved)

Under the hypotheses of Lemma 2(b), let d(x,y) > r. The images α(σ^+_x) and σ^+_y have disjoint
supports, so they commute. Hence α(σ^+_x σ^+_y)|Ω⟩ = α(σ^+_x) e^{iφ} σ^+_y |Ω⟩ = e^{2iφ}|x,y⟩, up
to the vacuum phase.

- Far pairs are therefore fixed. By unitarity, the span of the near pairs,
  S_near = span{|x, x+ρ⟩ : 0 < |ρ|_∞ ≤ r}, is invariant.
- By TI, U restricted to S_near is a matrix-valued Laurent polynomial W(K) in the pair-centre
  momentum K. Its size is d_r = ((2r+1)^3 − 1)/2: d_1 = 13 = 3 + 4 + 6 and d_2 = 62. Covariance
  makes it covariant, through the permutation action on ρ, under the vacuum stabiliser H_m.
  - H_m = O for the full action, or for any SU(2)-symmetric α.
  - H_m = T for the axis action with only Q_n conserved, because odd R map the two-particle
    sector over Ω to the (N−2)-particle sector over the anti-vacuum.

  The orbit structure 3 + 4 + 6 is the same under T.

So the two-particle sector is (frozen continuum) ⊕ (an H_m-covariant d_r-coin quantum walk).
Transport of pairs is equivalent to W(K) having a nonflat eigenphase.

**Scope of the reduction.** This reduces only the **two-particle** sector.
- A flat W does not exclude mobile bound clusters of k ≥ 3 particles. The same argument gives
  (frozen) ⊕ (finite-coin cluster walks) in each k-sector, and these are not analysed here.
- Transport at finite density or above other vacua is not reduced either.

So a nonflat W is sufficient for T3, but not necessary.

The single-particle walk freeze does not apply here. The coin is a permutation representation of
dimension d_r (13 for r = 1), not the spin-1/2 coin. The 10-16 two-qubit-site note shows that
larger coins can move. **Open:** whether some U(1) one-qubit O-covariant QCA realises a nonflat W,
or a nonflat k-cluster walk for some k ≥ 3.
The only in-premise U(1) examples constructed here are diagonal ones (Lemma 4), for which W is
diagonal and constant.

## Lemma 4 — diagonal and on-site layers freeze (proved; exact checks in `logs/c4b_02_onsite_diagonal.txt`)

(a) **Covariant on-site automorphisms**, Ad(u) ↔ O_u ∈ SO(3) commuting with Q(O).
    - Full action: the real commutant of Q(O) is the scalars, so the only such automorphism is the
      identity.
    - Axis action: the commutant is span{P_n, P_E}, so the automorphisms are {id, Ad σ_n}, where
      Ad σ_n is the π rotation about n.

(b) **Full action.** If a covariant α fixes σ_m at every site, then covariance and TI make it fix
    σ_{Q(R)m} for every R. These span R^3, so α fixes all single-site operators and α = id. In
    particular every Z-diagonal layer, in any basis, is non-covariant unless it is trivial.

(c) **Axis action.**
    - The only axis that can be fixed non-trivially is ±n.
    - **Exhibit:** Ad(∏ exp(iφ σ_n(r) σ_n(r+e))) over face bonds, with φ = 0.3. It is checked
      O-covariant on explicit matrices for all 24 R, max error 2e−15. It is entangling and
      non-Clifford. Restricted to {0, e_x}, α(X_0) has 9 Pauli components. The full α(X_0) is
      supported on the whole 7-site star and has 10272 Pauli components, according to the
      reviewer's count.
    - **Freeze:** if α fixes every σ_n, then α(σ^+_0) = σ^+_0 f with f diagonal on a finite set.
      So α^k(σ^+_0) = σ^+_0 f^k, which has the same support for every k. Composing with
      Ad(σ_n)^{⊗} keeps this form.

    Conclusion: any product of covariant diagonal layers and covariant on-site gates has uniformly
    bounded light cone. This excludes T2 and T3, at any range.

## Exhibit E1 — range-4 soldered Clifford QCA that spreads (exact; `logs/c4b_05_commuting_layers.txt`, PASS=10 FAIL=0)

- C and K satisfy β_R(P_0) = +P_0 for all 24 R, for both axis and full. Each family's translates
  commute.
- C_0 anticommutes with 24 translates of K, so the two layers do not commute.
- The composite at θ = π/4 is checked to preserve commutation. α(X_0) and α(Z_0) each have
  145-site support and Chebyshev range 4.
- τ = Σ over the 24-point orbit of (4,2,0). This is nonconstant, and every exponent is even
  (Frobenius).
- By C4 Theorem 2(c), the front is at n·vert(Newt τ), a permutohedron of radius 4n. Direct
  iteration, which does not use Theorem 2, gives Chebyshev radius 4, 8, …, 32 for n = 1..8, and
  |supp α^n(X_0)| = 145, 633, 2449, 4369, 5921, 12841, 25089, 33697.
- No glider exists, by C4 Theorem 2(d), since O admits no τ = x^r + x^{-r}.

*Second route* (`scripts/c4b_08_tau_laurent.py`, `logs/c4b_08_tau_laurent.txt`, PASS=7 FAIL=0).
This computes tr(M_C M_K) in the Laurent ring from M_P = 1 + v v^†Λ, a different implementation
from c4b_05's site iteration. It reproduces the same 24-monomial τ, together with symplecticity
and det = 1. Disclosure: it was written by the same author, and the expected τ was taken from
c4b_05's output. This is a cross-implementation check, not an independent review.

*Claim type:* exact finite certificate. Range 4 lies outside C4's range ≤ 2 classification, so
this does not contradict C4.

## Partitioned QCAs (out of premise) — `logs/c4b_03`, `c4b_04`, `c4b_06`, `c4b_07`

**Symmetry (exact, c4b_03, PASS=5).** Write g = (R, t) for the map x → Rx + t. Then g preserves
both partitions iff t ≡ c − Rc (mod 2), with c = (½,½,½). The stabiliser is therefore exactly
2Z^3 ⋊ O_c.
- t = 0 leaves only the C3 about (1,1,1).
- Pure translations: only 2Z^3.
- (1,1,1) swaps the two partitions, so it is a symmetry only up to the half-step glide
  U → V_{P0} U V_{P0}^{-1}.

So the 2×2×2 Margolus QCA is a framework-group-covariant dynamics for a proper subgroup of index 8
in the translations. It is not an instance of (D-QCA). In effect it has an 8-qubit unit cell.

**Dynamics (c4b_04, PASS=19 FAIL=0).** Blocks are SU(2)-invariant and commute with all 24 corner
permutations of O_c. This is checked on the full 256-dimensional space. They are therefore
covariant for every menu action. Three blocks were run:
- inversion permutation: single-magnon group velocity 2 per two-step, moving rigidly along the
  body diagonals;
- generic exp(i Σ_d J_d H_d), with J = (0.7, 0.4, 0.25): one-magnon bands disperse, maximum
  |∂ω/∂K| = 1.97;
- block c = exp(i Π_{S≤2} H Π_{S≤2}), which is the identity on ≤ 1 magnon per block:
  - one magnon: flat bands, and exactly static on Z^3 for 6 two-steps;
  - two magnons: confined to the cube where they first share a block.

**Lemma 5 (proved).** For block c, two distinct sites of a P0 cube lie in distinct P1 cubes, and
vice versa. A pair that shares a block is therefore separated, and so frozen, in the other
partition. It is confined to the 8 sites of that cube forever. A pair that never shares a block
never moves. This is checked exactly on Z^3 for four initial pairs over 8 two-steps.

**Multi-magnon survey (c4b_06 sampled, exact per sample; c4b_07 weighted).**
- k = 3: all 120 random clusters have closed reachable sets, so each sampled cluster is exactly
  confined. This is a per-sample certificate, not a theorem for k = 3.
- k = 4: 9 of 40 reachable sets are not closed, with support growing about linearly. The check
  "all closed" is a FAIL, and that FAIL is kept in the log. It falsifies the guess "block c
  confines every cluster".

  The probability-weighted COM displacement does **not** grow (c4b_07, run on two flagged
  clusters for 6 two-steps, with pruning |amp| < 1e-6 and a reported discarded norm ≤ 5.3e−8):
  - ⟨ΔCOM²⟩ = 0.11, 0.21, 0.23, 0.29, 0.32, 0.32 for the first cluster;
  - ⟨ΔCOM²⟩ = 0.05, 0.11, 0.11, 0.14, 0.16, 0.12 for the second;
  - P(|ΔCOM| > 2) = 0 among kept configurations in both, so it is ≤ 5e−8 in total.

  The declared mobility prediction therefore FAILs, and both FAIL lines are kept in
  `logs/c4b_07`. The non-closed reachable sets carry negligible weight. *Reading:* there is no
  evidence of 4-magnon transport within 6 two-steps. Mobility at longer times or for other
  clusters is untested.

## Answers to the three tasks

1. **Index lemma.** Proved: Lemma 1, conditional on recalled GNVW properties I2, I4–I7, which are
   sanity-checked numerically. Every TI QCA covariant under O, or under any H ≤ O fixing no
   vector, with any on-site action, has trivial flow through every lattice plane.
2. **Beyond Clifford.**
   - Diagonal + on-site layers: frozen (Lemma 4).
   - U(1)/SU(2) charges: singles frozen (Lemma 2); pairs reduce to a finite-coin walk (Lemma 3).
   - Commuting covariant Pauli layers: non-Clifford covariant family exists, and its Clifford
     point spreads (E1). No gliders.
   - Partitioned QCAs: they break Z^3-TI and O-about-a-site down to 2Z^3 ⋊ O_c. Inside that
     relaxed group they transport single magnons ballistically, and they freeze 1 and 2 magnons
     for block c.
3. **Conclusion.** Inside the premise there is a soldered dynamics that propagates in the T2 sense
   (E1). There is a scoped no-go for T3 in the families tried: diagonal/on-site at any range;
   U(1) single particles at any range; Clifford gliders at any range (C4); and T1 for everything
   (Lemma 1). There is **no** explicit in-premise T3 exhibit. One natural next target is Lemma 3's
   pair walk: construct a U(1) (axis: Q_n) one-qubit O-covariant QCA with a nonflat near-pair band.
   That would be sufficient for T3. Proving that no such pair band exists would **not** close U(1)
   transport, because the k ≥ 3 cluster sectors and the finite-density case would remain open.

## No-Go Discipline Gate (N1–N8) for the scoped negative parts

- **N1, routes.** Route families and their status:

  | # | route | status |
  |---|---|---|
  | (i) | index/flow | ATTEMPTED; T1 excluded (Lemma 1) |
  | (ii) | diagonal + on-site | ATTEMPTED; frozen (Lemma 4) |
  | (iii) | conserved-charge single particle | ATTEMPTED; frozen (Lemma 2) |
  | (iv) | conserved-charge pairs | ATTEMPTED; reduced, **not closed** (Lemma 3) |
  | (v) | commuting covariant Pauli layers | ATTEMPTED; T2 positive (E1); local-operator gliders at the Clifford point excluded by C4 Thm 2(d) (RULED OUT BY PRIOR); excitations above an invariant state not addressed; generic θ not closed |
  | (vi) | partitioned Margolus | ATTEMPTED; leaves the premise |
  | (vii) | Clifford at any range | RULED OUT BY PRIOR, C4 Theorem 2(d), gliders only |

  Five or more distinct families are tried. Two of them, (iv) and (v) at generic θ, are not
  closed. So **no universal T3 no-go is claimed**.
- **N2, walls.** The collapsed open set is
  {W1: a nonflat k-cluster walk, for some k ≥ 2, in a U(1) QCA; W1': U(1) transport at finite
  density or above other vacua; W2: T3 for non-conserving non-Clifford QCAs, including
  excitations above invariant states}.
  - Closing W1 positively implies T3. Proving that no W1 walk exists does not settle W1' or W2.
  - Pairwise independence is otherwise unresolved.
  - Their independence is *not asserted*: whether a non-conserving moving excitation would induce
    a conserved one is unknown.
- **N3, hidden walls.** Three were found and promoted to explicit premises:
  - Lemma 1 rests on recalled facts I5–I7 and on the existence of the inverse QCA;
  - Lemma 2 uses "vacuum = minimal-charge product state";
  - "translation-invariant" means Z^3, not a sublattice. This is why Margolus is out of premise.
- **N4, residual matching.**
  - C4 Theorem 2 is cited only for Clifford gliders, which is the exact matching residual.
  - The 10-16 walk freeze is cited only as an analogue, not as a witness. Its residual is a coin
    walk, not a many-body sector.
- **N5, resolutions.**
  - per-element: on-site automorphisms, exact;
  - per-site/per-block: Margolus blocks, exact sectors;
  - per-mode: one-particle symbol u(k) for every k (Lemma 2), and Bloch bands (c4b_04);
  - lattice-wide: index (Lemma 1), and exact iteration on Z^3 (E1, c4b_04).
  - **Not tested:** generic-θ non-Clifford dynamics, and the multi-particle (k ≥ 3) sectors in
    premise.
- **N6, partial-closure paths.** Two relax a premise rather than add an axiom: an 8-qubit unit
  cell (Margolus) and two qubits per site (`TWO_QUBIT_SITE_UNFREEZES...`). Both are recorded as
  premise changes. No "new axiom required" is claimed.
- **N7, steelman.** "Lemma 3 shows that the only obstruction to pair transport is constructing
  one U(1) QCA. Fracton models such as Chamon's, which is O-covariant here (E1 strings), have
  mobile dipoles but immobile monopoles. That is exactly the pattern 'singles frozen, pairs
  move'. A Chamon-defect-number-conserving QCA, or a generic-θ Floquet α(θ1,θ2), may already
  carry mobile bound states." This is a concrete unclosed mechanism. It is why the T3 no-go is
  scoped to the families listed and not stated universally.
- **N8, cross-cycle echo.**
  - The 10-16 walk freeze was "unfrozen" by enlarging the site, to two qubits. The analogous
    mechanism here is the enlarged effective coin of the pair walk (Lemma 3). It has been
    considered, and it is precisely what keeps W1 open.
  - C4's "nothing propagates" is narrowed here to range ≤ 2 (E1).

**Gate status: PASS for the scoped claims** (Lemmas 1, 2, 4, 5; frozen families). **No universal
negative is shipped.**

## What is not covered

- Generic-θ dynamics of α(θ1,θ2). This is 3D and non-Clifford; exact simulation is infeasible
  beyond about 27 qubits, and no reduction was found.
- Chamon-defect-conserving constructions.
- U(1) QCAs with a nontrivial off-diagonal part. None was constructed in premise.
- Range > 4.
- Weighted mobility of 4-magnon Margolus clusters.
- More than one qubit per site.
- Any physical identification.

## Reproduction

```bash
cd .claude/science/physics-loops/toe-scale-ladder-20261018/blocks/C4b/scripts
python3 c4b_01_index_sanity.py        # PASS=10 FAIL=0, < 1 s
python3 c4b_02_onsite_diagonal.py     # PASS=8  FAIL=0, ~1 s
python3 c4b_03_margolus_symmetry.py   # PASS=5  FAIL=0, < 1 s
python3 c4b_04_margolus_magnons.py    # PASS=19 FAIL=0, ~15 s
python3 c4b_05_commuting_layers.py    # PASS=10 FAIL=0, ~2 min
python3 c4b_06_margolus_kbody_survey.py  # PASS=1 FAIL=1 (k=4 not all closed: genuine), ~5 min
python3 c4b_07_margolus_4body.py      # PASS=0 FAIL=2 (declared mobility prediction fails: no weighted transport), ~15 min
python3 c4b_08_tau_laurent.py         # PASS=7 FAIL=0, < 1 s (second route for E1)
# combined: logs/SUMMARY.txt  TOTAL: PASS=60 FAIL=3 (3 FAILs = falsified predictions, kept)
```

## Load-bearing steps for independent check

1. **E1.** Re-derive τ = tr(M_C M_K) for the composite in the Laurent ring, independently of
   c4b_05's sparse F2 code, for example using C4's matrices M = 1 + v v^†Λ. Then confirm that it
   is nonconstant and that the composite is covariant with phases. This one certificate carries
   the claim "soldered dynamics propagates (T2) at range 4".
2. **Lemma 1, step (I7).** Confirm from GNVW's definition that the reflection inverts the index.
3. **Lemma 2(b), step 5.** Check that the vacuum-fixing subgroup acts on one-particle states with
   an x-independent phase. This holds for the axis action under T.

## Review dispositions

The independent review is in `REVIEW.md`. The reviewer is the same model family as the author,
working in a fresh context with its own code. Its log is `review_scripts/rv_SUMMARY.log`,
PASS=83 FAIL=0.

**Confirmed by independent code:**
- E1, including covariance with phases for both actions and both layer orders C·K and K·C;
- τ = the O-orbit sum of (4,2,0);
- Chebyshev radius 4n, which the reviewer argues holds for all n;
- Lemma 1, with (I7) proved from the GNVW support-algebra definition and checked by a second
  index route;
- Lemmas 2 and 4, and the exact group steps of Lemma 3;
- the Margolus stabiliser and Lemma 5's combinatorial step.

The magnon bands for the generic block and the k = 3 and k = 4 survey results remain author
evidence only.

- **3c (moderate): accepted and applied.** The reduction covers the two-particle sector only. A
  nonflat pair walk is sufficient for U(1) transport, not necessary. The k ≥ 3 cluster sectors and
  finite-density transport stay open. Edited: Result 4, Bottom line, Lemma 3 scope, Answer 3,
  N2.
- **1' (minor): accepted and applied.** "No localized excitation moves" is narrowed to "no
  local-operator glider" (C4 Theorem 2(d)). Excitations above an invariant state are not
  addressed. Edited: Result 1, N1 row (v).
- **3b (minor): accepted and applied.** The pair walk is H_m-covariant: T under the axis action,
  O under full/SU(2). Edited: Result 4, Lemma 3.
- **Cosmetic: applied.**
  - Lemma 2(a) now reads "m = ±n or global SU(2)".
  - The component count in Lemma 4(c) is now marked as restricted to {0, e_x}; the full image
    has 10272 components.
  - Radius 4n for all n, and validity in both layer orders, are added to Result 1.
