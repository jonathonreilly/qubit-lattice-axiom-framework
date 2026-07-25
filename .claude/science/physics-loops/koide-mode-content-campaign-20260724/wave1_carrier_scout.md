# WAVE 1 — CARRIER SCOUT: what the charged-lepton corner carrier actually IS

**Worker:** carrier scout (bounded). **Date:** 2026-07-24.
**Surface:** `origin/main` at `02f9359281f3e6bd849396da33710308a27a3949`
(fetched this session; `origin/main` advanced from `f8f9957` -> `288cdb2` ->
`02f9359` while this scout ran, but no file quoted below changed).
All line numbers below are line numbers in the `origin/main` blob at that
commit. Every file quoted with a worktree-relative path was checked
`git diff --quiet origin/main -- <path>` = IDENTICAL before quoting.

**This report sets no audit verdict, adopts no premise, and derives nothing.**
It reports what landed notes say, verbatim, and where they stop.

---

## HEADLINE FOR THE SUPERVISOR (read this first)

Four things the scout found that bear directly on the campaign's stated attack.
They are reported here as located source facts, not as a kill-check verdict
(that is the kill-check worker's call).

1. **K is an antilinear involution, not a doubling.** The supervisor's recorded
   prediction on K is CONFIRMED by landed text: on the delivered carrier `K` is
   entrywise complex conjugation in a real (corner) basis, i.e. an antilinear
   involution with `K C K = C`, fixing the singlet channel and exchanging the
   two doublet channels. Not a unitary, not a second copy of generators.
   (Section (b).)

2. **The mode-count question the campaign wants to decide has ALREADY been
   computed on the actual matter measure, and the answer is count-once — and it
   does NOT give `r = 1/2`.** The landed staggered note takes the realization
   gate's forced matter measure (one Grassmann pair per site) and computes the
   Berezin integral by explicit exterior-algebra expansion, with no determinant
   identity assumed, and gets the determinant **to the first power**. That note
   then states that the count-twice `|b|^2` structure enters "exactly and only"
   through the K-reality *parameter restriction* `c = conj(b)`, "not through the
   measure, the corner structure, or the taste doubling". So the measure-order
   fork is already resolved in the count-once direction on landed surfaces, and
   `r` is still undetermined afterward. (Section (a)/(f).)

3. **The "6 vs 12 Grassmann generators" axis named in the campaign target is
   explicitly `r`-NEUTRAL in two landed notes.** Passing `det3 -> det3^2`
   doubles the singlet and doublet exponents together and leaves every
   doublet-to-singlet power ratio unchanged. The axis that actually moves `r` is
   a different one: the occupancy/granularity axis (2-cell vs 3-cell menu,
   `w = 1/2` vs `1/3`, `n_d = 1` vs `2`). The identification of the two axes is a
   **declared reading** that its own note flags as "not an equivalence".
   (Section (c) — this is the disagreement finding.)

4. **The inference "count the modes -> read off `r`" is the exact inference an
   independent review already REFUTED and a landed note WITHDREW.** The
   2026-07-10 review of the orbit-occupancy note found that the holomorphic
   (one-complex-slot) Gaussian integral gives `r = 1`, not `1/2`, and that the
   runner had obtained `1/2` by hard-coding a per-slot quantum. The repaired note
   withdraws the map from partition-function data to `r` outright. What survives
   is `r = n_d/2` with `n_d` "a supplied doublet counting unit". (Section (d)/(g).)

Bottom line the scout can support: **the carrier is fully and concretely
specified on landed surfaces — the campaign will not be blocked for lack of a
carrier definition — but the carrier canonically carries BOTH a complex
structure (it is `C^3`) and a real structure (`K`), and no landed note says
which of the two the physical measure grains by. The binary is not
under-defined; the carrier is over-equipped.** That is a sharper version of the
supervisor's circularity risk, and it is where a native mode count will land.

---

## (a) THE CARRIER'S DEFINITION

### (a.1) It is a Hilbert space, not a Grassmann algebra

The charged-lepton corner carrier on landed surfaces is a **3-dimensional
complex subspace of the lattice Hilbert space** — the `hw=1` BZ-corner triplet.
No landed note defines the carrier as a Grassmann algebra; the Grassmann
algebras appear one level down, as the matter *measure* over it.

`docs/STAGGERED_DIRAC_COMMON_HW1_BZ_CORNER_CARRIER_IDENTIFICATION_BRIDGE_NARROW_THEOREM_NOTE_2026-07-05.md:33-44`:

> On the `2 x 2 x 2` periodic representative, sites are `x ∈ {0,1}^3` and the
> three commuting translation unitaries `U_1, U_2, U_3` act on `C^8` by
> `(U_mu f)(x) = f(x + e_mu mod 2)`. The joint character basis is
> `chi_k(x) = e^{i k·x}` with `k ∈ {0, pi}^3` (the BZ corner set), and
> `U_mu chi_k = e^{i k_mu} chi_k` with `e^{i k_mu} ∈ {+1, -1}`.
>
> Write `b(k) := k/pi ∈ (Z_2)^3` and `hw(k) := #{mu : k_mu = pi}`. Define
>
> ```text
> V := span{ chi_k : hw(k) = 1 }
>    = span( chi_(pi,0,0), chi_(0,pi,0), chi_(0,0,pi) ),   dim V = 3.
> ```

Ledger: `staggered_dirac_common_hw1_bz_corner_carrier_identification_bridge_narrow_theorem_note_2026-07-05` = `unaudited`.

### (a.2) The three generation channels

The three generations ARE the three `hw=1` corners.
`docs/GENERATION_LOCALIZATION_MOMENTUM_CORNER_DELTA_JI_PROTECTED_NARROW_THEOREM_NOTE_2026-06-06.md:28-31` (quoting its retained input):

> [`THREE_GENERATION_HW1_DISTINCT_TRANSLATION_CHARACTERS_NARROW_THEOREM_NOTE_2026-05-10`](...)
> (`retained`): the three generations are the `hw=1` Brillouin-zone corners
> `k1=(π,0,0), k2=(0,π,0), k3=(0,0,π)`, distinguished by three distinct joint **translation
> characters** under `(T_x, T_y, T_z)` — they carry **no spatial separation**.

Ledger check: `three_generation_hw1_distinct_translation_characters_narrow_theorem_note_2026-05-10`
= `retained_pending_chain` (NOT bare `retained`; the 2026-06-06 note's inline
"(`retained`)" annotation is stale). `generation_localization_momentum_corner_delta_ji_protected_narrow_theorem_note_2026-06-06` = `unaudited`.

**Two bases on the same 3-space, and they are not the same partition:**
- the **corner / generation** basis `{v_1, v_2, v_3}` (entrywise real), on which
  the `C_3[111]` lattice rotation acts as the real cyclic 3-cycle `C`;
- the **character / channel** basis `{P_1, P_w, P_wbar}` (singlet + doublet
  pair), which diagonalizes `C`.

`docs/KCPT_CORNER_CARRIER_LATTICE_DELIVERY_HW1_DOUBLET_PAIR_POLARIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md:89-101`:

> 1. `U_R V = V C` exactly on the integer lattice, where `V` is the ordered hw=1
>    corner triplet and `C = [[0,0,1],[1,0,0],[0,1,0]]`. The matrix of the
>    `C_3[111]` lattice unitary restricted to the hw=1 kernel triplet, in the corner
>    basis, has entries exactly `{0,1}` — no signs, no phases — and is the real
>    cyclic `C` of the supplied triple. [...]
> 2. `C^3 = I` and `C^T = C^2` exactly — the supplied relations.
> 3. Because the corner basis is entrywise real, ambient complex conjugation on the
>    lattice Hilbert space restricts to entrywise conjugation `K` in the corner
>    basis: `conj(V z) = V conj(z)` for every coefficient vector `z`.
> 4. The character projectors built from the delivered `C` are Hermitian rank-one,
>    mutually orthogonal, resolve the identity, and carry the exact
>    channel-eigenvalue association `C P_chi = chi P_chi`.

The abstract (pre-delivery) carrier spec, `docs/KCPT_COUPLING_TRIPLE_TWO_PRESENTATION_DERIVABLE_CLASS_SPECTRAL_PAIRING_BOUNDED_THEOREM_NOTE_2026-07-16.md:46-52`:

> - **Supplied corner carrier (R1c).** The real cyclic `C` with `C^3 = I_3`
>   and `C^T = C^2`, the character projectors
>   `P_chi = (I + conj(chi)*C + conj(chi)^2*C^2)/3` for
>   `chi in {1, w, conj(w)}`, `w = -1/2 + (sqrt(3)/2)*i`, and entrywise
>   conjugation `K` in the canonical basis. **FLAG — supplied surface:** this
>   is the mechanism note's declared corner surface, not a derived physical
>   carrier.

The channel vectors, explicitly, `docs/KCPT_CORNER_CARRIER_ANTILINEAR_NONHERMITIAN_KREAL_READOUT_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-18.md:41-48`:

> The corner carrier is `C = [[0,0,1],[1,0,0],[0,1,0]]`, real, with `C^3 = I_3`,
> `C^T = C^2`, and `K C K = C`. The unnormalized channel vectors are the singlet
> `v0 = (1,1,1)^T` and the conjugate doublet pair
> `vw = (1, conj(w), conj(w)^2)^T`, `vwb = conj(vw)`, with `C vw = w vw` and
> `C vwb = conj(w) vwb`. In the Hermitian inner product (conjugate-linear first slot)
> `<vw, vwb> = 0` and `<vw, vw> = <v0, v0> = 3`. The cyclotomic bilinear sums,
> which drive the antilinear witness values below, are `vw^T vw = 0`,
> `vwb^T vwb = 0`, and `vwb^T vw = 3`.

### (a.3) The Grassmann/Berezin presentation and its generator count

Two distinct Grassmann presentations exist on landed surfaces, at different
levels. They must not be conflated.

**(a.3.i) The PHYSICAL matter measure (lattice-level, forced).**
`docs/STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md:88-94`:

> **Definition.** "The staggered-Dirac realization from Quantum +
> Lattice" is the conjunction of:
>
> - **Matter-statistics clause.** The matter measure on the Quantum + Lattice
>   baseline is the finite single-mode Grassmann partition, one pair
>   `(χ_x, χ̄_x)` per site, on the dim-2 per-site Cl(3) module;
>   bosonic second quantization is excluded.

Generator count law, `docs/AXIOM_FIRST_SPIN_STATISTICS_THEOREM_NOTE_2026-04-29.md:213-216`:

> **(S1).** The relations (3) are the defining relations of the finite
> Grassmann algebra `Λ_{2|Λ|}` on the `2|Λ|` independent generators
> `χ_x, χ̄_x`. The operatorial realization is left exterior (wedge)
> multiplication of the generators on `Λ_{2|Λ|}` itself
> (`dim = 2^{2|Λ|}`) [...]

So: **2 Grassmann generators per site**, `2|Λ|` in total. Restricted to the
3-dimensional corner carrier `V` that is **3 complex modes = 6 Grassmann
generators total (2 per generation), not 6 per generation.**
(The campaign statement's phrase "6 Grassmann generators per triple copy" is
correct in the source; "per generation" would be 2.)

**(a.3.ii) The DECLARED PROBE Berezin surface (carrier-level).**
`docs/KCPT_COUPLING_TRIPLE_BEREZIN_COUNT_BINARY_MEASURE_COLLAPSE_BOUNDED_THEOREM_NOTE_2026-07-17.md:101-107`:

> - **Declared Berezin probe surface (R4b).** A finite Grassmann algebra on
>   generators `theta_1, ..., theta_n, thetabar_1, ..., thetabar_n` with the
>   quadratic weight `exp(-S)`, `S = sum_(i,j) thetabar_i M_(i,j) theta_j`,
>   integrated against the pinned measure ordering below. **FLAG — declared
>   probe surface:** this finite integral surface is a probe of the count
>   binary's arithmetic, declared here; it is not the physical matter action,
>   not its measure, and not a derived realization of either.

**FLAG (scout):** this note's Grassmann surface is DECLARED, not derived, and
is explicitly disclaimed as the physical matter action or measure.

**(a.3.iii) A landed audit repair the campaign must respect: Grassmann ≠ CAR.**
`docs/AXIOM_FIRST_SPIN_STATISTICS_THEOREM_NOTE_2026-04-29.md:35-49`:

> independent audit found a source-runner convention drift in (S1): the note
> displayed the pure-Grassmann relations (3) — every anticommutator zero,
> including the `{χ̄_x, χ_y}` cross pairs — but claimed they are "realized
> operatorially on the `2^{|Λ|}`-dim Fock space", while the runner's [S1]
> block checked the CAR `{c_x, c_y^†} = δ_xy I`, whose mixed anticommutator
> is NOT zero. [...] the Jordan–Wigner construction is kept as the SEPARATELY LABELED CAR
> operator realization on the `2^{|Λ|}`-dim Fock space (runner [S1-CAR]),
> with a refutation-shaped contrast line computing that the CAR realization
> does NOT satisfy (3) (cross anticommutators exactly `0` vs exactly `I`).

The campaign plans to "build the CAR algebra ... and COUNT the complex modes of
its coherent-state Berezin representation". The landed repair says the Grassmann
symbol algebra and the CAR operator algebra are **different objects with
different anticommutators**; any count that moves between them must carry that
distinction explicitly or it will be caught the same way.

---

## (b) HOW K (AND CPT) ACT ON THE CARRIER — THE CRUX

**Answer: `K` is an ANTILINEAR INVOLUTION (a real structure) on the
3-dimensional complex carrier. It is not a unitary, it is not a doubling, and
it does not pair distinct generations — it pairs the two doublet CHANNELS while
fixing the singlet channel and fixing every corner/generation basis vector.**

### (b.1) Defining relations, verbatim

`docs/KCPT_CORNER_CARRIER_ANTILINEAR_NONHERMITIAN_KREAL_READOUT_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-18.md:41-42`:

> The corner carrier is `C = [[0,0,1],[1,0,0],[0,1,0]]`, real, with `C^3 = I_3`,
> `C^T = C^2`, and `K C K = C`.

`docs/KCPT_CORNER_CARRIER_LATTICE_DELIVERY_HW1_DOUBLET_PAIR_POLARIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md:96-98` (the antilinearity, stated as restriction of ambient conjugation):

> 3. Because the corner basis is entrywise real, ambient complex conjugation on the
>    lattice Hilbert space restricts to entrywise conjugation `K` in the corner
>    basis: `conj(V z) = V conj(z)` for every coefficient vector `z`.

`docs/KCPT_CORNER_CARRIER_LATTICE_DELIVERY_HW1_DOUBLET_PAIR_POLARIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md:110-117` (T2, the channel action):

> 1. `K P_1 K = P_1`: the singlet channel is K-fixed, and its democratic direction
>    `(1,1,1)/sqrt(3)` is entrywise real (a K-fixed vector).
> 2. `K P_w K = P_wbar` and `K P_wbar K = P_w`: the two doublet channels form a
>    single K 2-orbit.
> 3. At the vector level, `vw = (1, wbar, wbar^2)/sqrt(3)` satisfies `C vw = w vw`,
>    `K` maps the `w`-eigenline to the `wbar`-eigenline, and `P_w = vw vw^dagger`
>    exactly.

`docs/KCPT_COUPLING_TRIPLE_TWO_PRESENTATION_DERIVABLE_CLASS_SPECTRAL_PAIRING_BOUNDED_THEOREM_NOTE_2026-07-16.md:117-123` (T1, and the basis-dependence of the action):

> `K(W(a,b,c)) = W(conj(a),conj(b),conj(c))`. The carrier `C` is
> presentation-shared (`K(C) = C`, real), and the integer-cycle basis
> `{I, C, C^2}` is presentation-shared entrywise. The character projectors are
> not: `K(P_1) = P_1` while `K(P_w) = P_conj(w)` and `K(P_conj(w)) = P_w`.
> The swap is the content: the real integer-cycle basis is presentation-fixed,
> the character-projector basis is presentation-swapped, and the coupling
> triple transforms entrywise. (Runner V1, V2.)

`K` is pinned as distinct from the adjoint. Same note, lines 102-111:

> | involution | action on `(a,b,c)` | action on `W` | fixed locus |
> |---|---|---|---|
> | entrywise conjugation `K` | `(conj(a),conj(b),conj(c))` | `K(W(a,b,c)) = W(conj(a),conj(b),conj(c))` | entrywise-real triples |
> | adjoint `dagger` | `(conj(a),conj(c),conj(b))` | `W(a,b,c)^dagger = W(conj(a),conj(c),conj(b))` | Hermitian section: `a` real, `c = conj(b)` |
>
> The two actions differ generically — witness `(a,b,c) = (0,1,2)`, where `K`
> returns `W(0,1,2)` while the adjoint returns `W(0,2,1)` — and agree exactly
> at `b = c` (runner V1).

### (b.2) Antilinear functionals on the carrier are classified (not open)

`docs/KCPT_CORNER_CARRIER_ANTILINEAR_NONHERMITIAN_KREAL_READOUT_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-18.md:50-53`:

> A linear functional is `E_A(psi) = psi^dag A psi`. An antilinear functional is
> `F_B(psi) = psi^dag conj(A) conj(psi)` with `B = K` composed with `A`.

Same file, `:83-88` (T4):

> **T4 (antilinear `K`-real face, equivariance dropped).** `K B K = B` holds iff
> `A` is entrywise real. Then `F_B(vw) = vwb^T A vwb`, only the symmetric part
> contributes, and `F_B(vwb) = conj(F_B(vw))` for the displayed conjugate,
> equal-normalized representatives. Antilinear phase covariance is
> `F_B(c*psi) = conj(c)^2 * F_B(psi)`, so the complex value is not a ray invariant
> but its modulus is.

### (b.3) The presentation swap is ALSO a proper lattice rotation

This is directly relevant to whether "the K-partner copy is an independent
sector" or "the same sector in another frame".
`docs/KCPT_CORNER_CARRIER_TWO_PRESENTATION_SWAP_PROPER_ROTATION_CONJUGACY_BOUNDED_THEOREM_NOTE_2026-07-18.md:13-23`:

> this note delivers the presentation-swap as the
> proper cubic rotation `M`: the pi-rotation about `[1,-1,0]` (`det M = +1`), realized as a
> lattice unitary whose hw=1 kernel action is the transposition `TS` (T1). Rotation
> conjugation by `TS` acts on the supplied projector family exactly as entrywise conjugation
> `K`, `TS P_chi TS = conj(P_chi)` for every channel, so the projector pair is a single
> 2-orbit of the proper rotation and the canonical K-odd separator `D0 = P_w - P_wbar` is exchanged exactly
> as by `K` (T2, T3). On the Hermitian probe section `W_H = a I + b C + conj(b) C^2` the
> antilinear K-exchange coincides exactly with the linear rotation conjugation,
> `conj(W_H) = TS W_H TS`; off the section the two gradings are inequivalent (witnesses
> `C - C^2` and `i I`) (T4). Thus the `w` versus `wbar` projector labeling is a
> rotation-frame orientation at the `C_3[111]` axis.

**Scout reading (flagged as reading, not source):** on the Hermitian section the
"K-conjugate partner copy" is the image of the same carrier under a proper
cubic rotation already named by the LATTICE axiom, not an independent sector.
Off the section the two gradings are computed inequivalent. This is a live
handle for Wave 2 and also a live trap: it makes "is the partner copy an
independent Grassmann sector?" a section-dependent question.

### (b.4) CPT

`K`/CPT is a compound name for **downstream readout-context content**, not axiom
content. `docs/MINIMAL_AXIOMS_2026-06-29.md:152-154`:

> - `K`/CPT orbit structure, central-sector decomposition, and any sector
>   generation rule are downstream readout-context content, not generic axiom
>   content.

Same file `:130-134`:

> Born weights, readout-context selection, central-sector decomposition, `K`/CPT
> structure, transition relations, record-production dynamics, physical
> persistence dynamics, local observability, or any other additional bridge must
> cite separate retained authorities or remain bounded/pending according to the
> audit ledger.

The live Qualification, same file `:76-79`:

> These axioms state only their named primitive content. Further physical
> structure requires a retained derivation or bridge, or explicit approved-
> primitive registration, before use as a premise. A choice not fixed by the
> supplied structure remains a named conditional or open dependency.

**FLAG — no landed note found by this scout gives a CPT operator acting on the
corner carrier's CAR/Fock algebra.** The framework has CPT antiunitaries on
staggered lattice operators (`docs/CPT_D_LEVEL_FINITE_LATTICE_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-17.md:268` gives `T^2 = I` (`K^2 = I`); `docs/AXIOM_FIRST_CPT_THEOREM_STRETCH_NOTE_2026-04-29.md:341` gives `Θ_CPT := (E Σ_PT R_b) · K`), but the corner-carrier notes use only entrywise conjugation `K`. The identification "`K` on the corner carrier = the physical CPT" is NOT established by anything the scout located. **Gap G7 below.**

---

## (c) EVERY GENERATOR / SLOT COUNT STATED IN A LANDED NOTE — AND THE DISAGREEMENT

### (c.1) The complete inventory

| # | Count as stated | Source (file:line) | Status of the statement in its own note |
|---|---|---|---|
| 1 | `2|Λ|` generators `χ_x, χ̄_x`, one pair per site | `docs/AXIOM_FIRST_SPIN_STATISTICS_THEOREM_NOTE_2026-04-29.md:213-216`; `docs/STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md:91-94` | theorem content / forced clause |
| 2 | carrier `dim V = 3` (complex) | `docs/STAGGERED_DIRAC_COMMON_HW1_BZ_CORNER_CARRIER_IDENTIFICATION_BRIDGE_NARROW_THEOREM_NOTE_2026-07-05.md:43` | theorem content |
| 3 | horn `m` uses `6m` generators: `m=1` -> 6, `m=2` -> 12 | `docs/KCPT_COUPLING_TRIPLE_BEREZIN_COUNT_BINARY_MEASURE_COLLAPSE_BOUNDED_THEOREM_NOTE_2026-07-17.md:108-115, 156-176, 188-200` | **DECLARED READING R5b — "not an equivalence"** |
| 4 | doublet = 2 real slots (real polarization) vs 1 complex slot (holomorphic polarization) | `docs/KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md:44-49, 82-87` | **NAMED CONDITIONAL PREMISE `POLARIZATION-SELECT`** |
| 5 | `n_d ∈ {1,2}` = "supplied doublet counting unit", `r = n_d/2` | `docs/KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md:130-149, 169` | supplied integer, explicitly not selected |
| 6 | 2-cell menu `{singlet cell, doublet cell}` vs 3-cell menu `{s, w, wbar}` | `docs/KOIDE_FORMATION_GATE_RELOCATION_TIED_MEASURE_PER_CELL_WEIGHT_COMPATIBILITY_BOUNDED_THEOREM_NOTE_2026-07-12.md:16, 350-352`; `docs/ACPHILAMBDA_OCCUPANCY_GRAIN_MENU_COUNTING_MEASURE_DYNAMICAL_STATIC_CORRESPONDENCE_BOUNDED_THEOREM_NOTE_2026-07-16.md:68-70` | supplied menus, no selection |
| 7 | cell dimensions `(d_s,d_d) = (1,2)`, K-orbit cardinalities `(s_s,s_d) = (1,2)` | `docs/KOIDE_FORMATION_WEIGHT_LAW_EXPRESSIBILITY_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-12.md:66-68` | supplied-object classification |
| 8 | commutant of `C` has complex dimension exactly 3, span `{I, C, C^2}` | `docs/KCPT_CORNER_CARRIER_LATTICE_DELIVERY_HW1_DOUBLET_PAIR_POLARIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md:131-132` | exact computation |
| 9 | K-real Hermitian commutant members form a **2-parameter real family** `a*I + b*(C+C^2)` | same, `:133-136` | exact computation |

The `6m` statement in full, `docs/KCPT_COUPLING_TRIPLE_BEREZIN_COUNT_BINARY_MEASURE_COLLAPSE_BOUNDED_THEOREM_NOTE_2026-07-17.md:108-115`:

> - **Declared count-binary reading (R5b).** The translation "graining horn
>   `m` corresponds to `6m` Grassmann generators" (`m = 1`: one triple copy,
>   6 generators; `m = 2`: the triple copy plus its K-conjugate partner copy,
>   12 generators). **FLAG — declared reading, not an equivalence:** both
>   sides of the translation are computed exactly (runner B2, B3), and the
>   correspondence between the graining slot count and the generator count is
>   declared bookkeeping; no framework clause identifies occupancy slots with
>   Grassmann generators, and T3 makes no equivalence claim.

### (c.2) THE DISAGREEMENT — this is the finding the task asked for

**No two landed notes contradict each other on a stated theorem. But the
`6m` generator axis and the occupancy/menu axis are arithmetically DIFFERENT
axes, and only one of them moves `r`. The campaign's target statement treats
them as four equivalent framings of one binary. Landed text does not support
that equivalence; the one note that asserts the correspondence flags it as
declared bookkeeping and disclaims equivalence.**

Evidence 1 — the `6 -> 12` doubling is `r`-neutral, stated twice.

`docs/KCPT_COUPLING_TRIPLE_BEREZIN_COUNT_BINARY_MEASURE_COLLAPSE_BOUNDED_THEOREM_NOTE_2026-07-17.md:177-183` (T2 item 3):

> 3. **r-neutral doubling.** `lam_0^2 * |lam_1|^4 = (lam_0 * |lam_1|^2)^2`
>    identically on entrywise-real triples: the singlet exponent and the
>    doublet exponent double together, and every doublet-to-singlet power
>    ratio is unchanged. The two realizations satisfy the product identity
>    `count_twice = count_once * det3` identically — a multiplier `det3`,
>    not a constant — and the quotient reading `count_twice / count_once =
>    det3` is valid only where `det3` is nonzero (runner B2).

`docs/KCPT_COUPLING_TRIPLE_TWO_PRESENTATION_DERIVABLE_CLASS_SPECTRAL_PAIRING_BOUNDED_THEOREM_NOTE_2026-07-16.md:186-193` (T4 item 1):

> 1. **Positive control (exact).** On entrywise-real triples
>    `|det3|^2 = lam_0^2 * |lam_1|^4`: passing from `det3` to `|det3|^2`
>    doubles the singlet exponent and the doublet exponent together, so every
>    doublet-to-singlet power ratio is unchanged. The pairing statement is
>    r-neutral (runner V3) [...]

A third, independent instance on the actual staggered surface —
`docs/KOIDE_STAGGERED_FIRST_ORDER_GENERATION_DETERMINANT_BOUNDED_THEOREM_NOTE_2026-06-11.md:77-80`:

> The taste-conjugate hw=2 triplet **squares** the generation circulant
> factor — a *holomorphic* square, not a modulus (check 11). The square is
> channel-uniform, so it cancels in any doublet:singlet weight ratio (the
> landed pruning lemma, reproven; check 12).

Evidence 2 — the axis that DOES move `r` is the occupancy/menu axis, and it is a
different arithmetic object:
`docs/KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md:130-149`:

> Define one aggregate condition with a supplied doublet counting unit `n_d`:
>
> ```text
> E_s = epsilon,
> E_d = n_d epsilon.
> ```
>
> Using `E_s = 3a^2` and `E_d = 6|b|^2` gives
>
> ```text
> r = |b|^2/a^2 = n_d/2,
> Q = (1+2r)/3 = (1+n_d)/3.
> ```
>
> The two constructed extensions are:
>
> ```text
> aggregate real-dimension count:  n_d = 2  ->  r = 1    ->  Q = 1
> aggregate outcome-cell count:    n_d = 1  ->  r = 1/2  ->  Q = 2/3
> ```

Evidence 3 — the Berezin note nevertheless declares the two axes correspondent,
`docs/KCPT_COUPLING_TRIPLE_BEREZIN_COUNT_BINARY_MEASURE_COLLAPSE_BOUNDED_THEOREM_NOTE_2026-07-17.md:190-200`:

> The spectral-pairing note's underived binary, quoted in R2b — one occupancy
> slot per K-orbit versus one slot per channel atom — maps under the declared
> reading R5b onto the generator-count binary of T2: horn `m` uses `6m`
> generators, with `m = 1` giving the count-once value with singlet/doublet
> exponent pair `(1,1)` and `m = 2` giving the count-twice value with exponent
> pair `(2,2)` (runner B2, B3). This is a fourth exact translation of the same
> underived binary [...] The translation is declared, not derived: the
> `m` to generator-count correspondence is declared bookkeeping, never an
> equivalence claim, and the selection between the horns is not made here.

**Scout's arithmetic observation, offered as an observation and NOT as a claim
about any note's correctness:** the 6-generator integral over the 3-complex-mode
carrier computes `det3 = lam_0 * lam_1 * lam_2` — it integrates all three
channel atoms separately, and the grouping into `lam_0 * |lam_1|^2` is applied
afterwards by the quoted pairing license. Under the occupancy language that
resolution is the **per-channel-atom** one (3 cells, `w = 1/3`, `r = 1`), not the
per-K-orbit one, which R5b assigns to `m = 1`. Correspondingly, **no landed note
states the generator count that would be the arithmetically matching Grassmann
translation of the 2-cell menu (2 complex modes = 4 generators, vs 3 complex
modes = 6 generators).** Whether R5b's assignment is a defect or a different and
legitimate bookkeeping is NOT something this scout can settle, and R5b's own
FLAG pre-empts a defect finding. It is flagged here because **the campaign's
target statement inherits the equivalence that R5b explicitly declines to
assert.**

---

## (d) THE LICENSED WEIGHT SET AND THE `w -> r` MAP

### (d.1) The coordinate map, verbatim

`docs/KOIDE_FORMATION_WEIGHT_LAW_EXPRESSIBILITY_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-07-12.md:46-55`:

> Using the relocation theorem's explicitly unadopted energy dictionary
> (Residual Atom 2), the coordinate map is
>
> ```text
> cell probabilities = (w, 1-w) = (singlet, doublet),
> r = (1-w)/(2w).
> ```
>
> Therefore `w = 1/3` gives `r = 1`, while `w = 1/2` gives `r = 1/2`. These are
> exact fork arithmetics only; neither implication is a selection.

### (d.2) The licensed set

Same file, `:19-28` (the claim box):

> > **Claimed (bounded):** under the note-owned licensing criterion stated first
> > in Residual Atoms, the supplied carrier and orbit-constant formation quotient
> > carry
> > exactly two distinct canonical formation assignments: carrier/orbit counting
> > gives singlet weight `w = 1/3`, while counting or left-regular/Hilbert-Schmidt
> > weighting of the **licensed commutative quotient** gives `w = 1/2`. Thus the
> > expressible set is exactly `{1/3, 1/2}`. **Not claimed:** that bare
> > functoriality alone proves this completeness, that either value is derived or
> > selected, that `w = 1/5` is lawful, or that this classification applies off
> > the stated two-cell `C_3` menu.

The set symbol and its conditionality, as consumed downstream —
`docs/ACPHILAMBDA_OCCUPANCY_GRAIN_MENU_COUNTING_MEASURE_DYNAMICAL_STATIC_CORRESPONDENCE_BOUNDED_THEOREM_NOTE_2026-07-16.md:89-105`:

> 4. **The licensed static formation-weight set and its classification
>    convention** from the expressibility classification note (unaudited
>    `bounded_theorem`), verbatim:
>
>    ```text
>    W_expr = {1/3, 1/2}.
>    ```
>
>    This set is conditional on the source note's Supplied-Object
>    Canonical-Measure Licensing Criterion (SOCMLC), which the source explicitly
>    calls "a classification convention, not a theorem derived from the minimal
>    axioms." Both values concern the same fixed singlet/doublet quotient:
>    "carrier/orbit counting gives singlet weight `w = 1/3`, while counting or
>    left-regular/Hilbert-Schmidt weighting of the **licensed commutative
>    quotient** gives `w = 1/2`." The source expressly says it is "Not a
>    classification for a different carrier, a refined menu, a menu with
>    different orbit sizes, or a three-cell registration."

### (d.3) The equivalence chain, verbatim

`docs/KOIDE_FORMATION_GATE_RELOCATION_TIED_MEASURE_PER_CELL_WEIGHT_COMPATIBILITY_BOUNDED_THEOREM_NOTE_2026-07-12.md:178-193`:

> The named laws are exact specializations:
>
> | formation law | solved cell weights `(w,1-w)` | solved `r` |
> |---|---:|---:|
> | per-outcome-cell: `E_s = E_d` | `(1/2, 1/2)` | `1/2` |
> | per-real-mode: `E_d = 2 E_s` | `(1/3, 2/3)` | `1` |
>
> Thus
>
> ```text
> w = 1/2  <=>  uniform over the two registrable outcome cells
>            <=>  per-outcome-cell law  <=>  r = 1/2,
>
> w = 1/3  <=>  weights proportional to carrier dimensions (1,2)
>            <=>  per-real-mode law     <=>  r = 1.
> ```

### (d.4) THE LOAD-BEARING CAVEAT the campaign must carry

The `w -> r` map is a note's **own declared modeling element**, not framework
content. Same file, `:359-368` (Residual Atom 2):

> 2. **The energy dictionary.** The identification that a formation state
>    distributes the total channel energy as shares —
>    `E_s = w E_tot`, `E_d = (1-w) E_tot`, against the first-order section
>    fork's channel decomposition `E_s = 3a^2`, `E_d = 6|b|^2` — is **this
>    note's own declared modeling element** (the energy-to-formation-state
>    bridge). It is what makes
>    the relocation's `r`-image exact rather than merely analogical. It is not
>    supplied by the Record axiom, by either cited source note, or by the R-D
>    surface; an auditor who rejects it keeps T1 (compatibility) and T3 (the two
>    canonical states) but loses the bijection `r = (1-w)/(2w)` of T2.

And the set-level correspondence between the dynamical menu and the static
weight set is explicitly NOT an identification —
`docs/ACPHILAMBDA_OCCUPANCY_GRAIN_MENU_COUNTING_MEASURE_DYNAMICAL_STATIC_CORRESPONDENCE_BOUNDED_THEOREM_NOTE_2026-07-16.md:22-31`:

> The resulting numerical set `{1/3, 1/2}` equals the static classification's
> licensed weight set. That equality is a SET-LEVEL ARITHMETIC CORRESPONDENCE
> between independent conditional constructions. [...] No identification of
> measure granularity, formation weighting, and dynamical menu is made here;
> such an identification is the missing binding theorem preserved by the
> formation-gate relocation source. This note selects no menu, weight, horn, or
> dial value.

### (d.5) The `r`-from-slot-count dictionary, as CODE

`scripts/berezin_detc_detr_fork_2026_06_04.py:173-174` (origin/main):

```python
def r_from_slot_count(slot_count: int) -> Fraction:
    return F(slot_count, 2)
```

i.e. **`r = (doublet slot count)/2` by definition in that runner**, matching
`r = n_d/2` in the occupancy note. This is the single most important line for
the circularity question: on landed surfaces, the doublet slot count and `r` are
related by a *dictionary*, and the dictionary is declared, not derived.

---

## (e) THE CLOSURE OBLIGATION, EXACT WORDING

`docs/AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md:9-24`:

> ## Exact target
>
> Derive from the retained framework chain whether the physical charged-lepton
> matter action counts the `K`/CPT orbit or holomorphic pair once rather than
> counting each sector or channel.
>
> The statement was historically adopted through a governance decision recorded
> in `TIER_A_RESIDUAL_OWNER_ADOPTION_RETIREMENT_2026-07-04.md`.
> That decision now has historical weight only and supplies no physics premise.
>
> ## Closure criterion
>
> A closing theorem must derive the physical matter action and its measure, then
> distinguish the count-once `det_C`/holomorphic realization from the
> count-twice `|det_C|^2`/realified realization without inserting the desired
> charged-lepton value or readout dictionary.

Same file, `:30-31`:

> Until such a theorem is independently audited and retained, every result that
> uses this statistical-grain selection remains conditional or pending-chain.

Ledger: `ac_orbit_occupancy_statistical_grain_derivation_obligation` =
`audited_renaming`, claim_type `open_gate`.

**The one open door named in the landed no-go** —
`docs/ACPHILAMBDA_RECORD_OUTCOME_ORBIT_OCCUPANCY_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md:47-48`:

> This is a current-surface non-entailment result. It does not rule against a
> future physical CAR/action theorem that derives a specific Gaussian measure.

That same note's N7 already computes the shape of the count-twice mechanism —
same file, `:210-215`:

> The companion runner executes this objection rather than checking its wording:
> it verifies `F_R/2=F_C` on exact finite carriers and record collections,
> computes the block-Pfaffian determinant power of a generic supplied complex
> Grassmann sector, and shows that the modulus-square power appears when an
> independent conjugate sector is adjoined. It then checks directly that the
> accepted axiom memo withholds the physical CAR/action and readout selector.

**Note the phrase "without inserting the desired ... readout dictionary" in the
closure criterion. The `r = slot_count/2` / `r = (1-w)/(2w)` maps ARE readout
dictionaries. A closing theorem may not import them.** This is the tightest
constraint on the campaign and Wave 2 should treat it as a hard gate.

---

## (f) WHAT IS ALREADY BUILT IN RUNNERS TOUCHING THE CARRIER'S CAR/BEREZIN STRUCTURE

All paths are `origin/main`.

### (f.1) `scripts/kcpt_coupling_triple_berezin_count_binary_measure_collapse_2026_07_17.py`
Self-contained exact sympy **finite Grassmann engine** (sparse dict, monomials
keyed by `frozenset` of generator indices), header comment at `:132-136`:
"Finite Grassmann engine (own exact implementation, sparse dict)". Provides:
- `gadd`, `gmul` with explicit inversion-count sign bookkeeping (`:139-158`);
- `gexp_product` = `prod (1 + t_k)` for even nilpotent quadratic terms, and
  `gexp_series` as the independent power-series cross-check (`:165-182`);
- `integrate_one` (single Berezin derivative with sign) and `berezin(F, order)`
  with the measure order convention "rightmost differential acts first"
  (`:185-201`);
- `minus_action_terms`, `holo_integral`, `holo_integral_reversed` — the pinned
  `d theta_1 d thetabar_1 ...` ordering and its reversal (`:204-236`);
- checks: anticommutation/nilpotency, product-exp == series-exp, integral
  `= det M` at `n = 1,2,3`, reversed-order sign `(-1)^n`, disjoint-copy
  factorization `det M * det N` (`:239-290`), then B2 (6-generator count-once,
  12-generator count-twice, direct witness at `(2, 1+i, -i)`), B3 (`6m`
  bookkeeping), B4 (top-form `det S` law and the coupling-dependent conversion
  witness `A(W) = W`), B5 controls, B6 verbatim quote gates.
This is the closest existing thing to "the machinery" the campaign describes.
**It has NO CAR anticommutator gate and NO Fock/intertwiner content** — it is
purely the Grassmann symbol algebra.

### (f.2) `scripts/acphilambda_fermionic_realification_pfaffian_power_identity_2026_07_12.py`
Paired to the only **`retained`** note in this stack. The note
`docs/ACPHILAMBDA_FERMIONIC_REALIFICATION_PFAFFIAN_POWER_IDENTITY_NARROW_THEOREM_NOTE_2026-07-12.md:14-33` builds the exact object Wave 2 needs:

> Let `K` be an `n x n` complex matrix and introduce independent Grassmann
> columns `chibar` and `chi`. In the ordered column
>
> ```text
> Psi = (chibar_1,...,chibar_n,chi_1,...,chi_n)^T
> ```
>
> define the antisymmetric kernel
>
> ```text
> A_K = [[0, K],
>        [-K^T, 0]].
> ```
>
> Then
>
> ```text
> (1/2) Psi^T A_K Psi = chibar^T K chi,
>
> Pf(A_K) = (-1)^(n(n-1)/2) det_C(K).
> ```

and, decisively for the count question, same file `:51-64`:

> This remains true when `chibar,chi` are reorganized into Majorana-paired
> Grassmann coordinates: an invertible linear coordinate change transforms the
> kernel by congruence and the Berezin measure by the inverse Jacobian, leaving
> the Gaussian value unchanged. No physical Majorana reality condition is used.
>
> By contrast, adjoin an independent conjugate sector and order the direct-sum
> variables by concatenating the `A_K` block before the `A_conjugate(K)` block.
> Then Pfaffian direct-sum multiplicativity gives exactly
>
> ```text
> Pf(A_K direct_sum A_conjugate(K))
>   = det_C(K) det_C(conjugate(K))
>   = |det_C(K)|^2
> ```

and `:110-113`:

> Thus a complex-to-Majorana coordinate change cannot alter the determinant
> power. A second power arises after the independent conjugate block is
> adjoined.

**This is the sharpest landed statement of the crux: on a fixed carrier with `n`
complex modes, re-coordinatizing (real vs complex polarization) does NOT change
the count; only ADJOINING an independent conjugate sector does.** Its own scope
boundary, same file `:138-153`:

> This theorem corrects the interpretation of the determinant-power fork. It
> shows that a Majorana-paired Grassmann presentation of a supplied single
> complex fermionic Gaussian preserves the first determinant power. The
> coordinate statement does not impose a physical reality condition. Within the
> displayed Grassmann-Gaussian construction, obtaining the modulus square instead
> uses a supplied conjugate sector or conjugate-paired readout.
>
> The theorem domain is a supplied Grassmann action, Berezin measure, and
> determinant carrier. Framework derivation of the charged-lepton carrier,
> global CAR structure, physical single-sector readout, K/CPT-orbit occupancy
> grain, registered `r`, `delta`, and R-eta readout lies outside this theorem.

### (f.3) `scripts/frontier_koide_staggered_first_order_generation_determinant_2026_06_11.py`
The most physically-anchored Berezin computation in the stack — it works on the
**actual matter measure**, not a probe surface. Note
`docs/KOIDE_STAGGERED_FIRST_ORDER_GENERATION_DETERMINANT_BOUNDED_THEOREM_NOTE_2026-06-11.md:56-64`:

> **Fact 1 — the measure is first-order.** The Berezin integral of the
> single-pair-per-site Grassmann measure is computed by explicit
> exterior-algebra expansion and nested single-generator Berezin
> integrals — no determinant identity is assumed at any point. For a generic
> symbolic 3×3 coupling, and for an antisymmetric-kinetic-plus-coupling toy
> of the staggered shape, the partition function is `det(D + A)` to the
> **first power** (checks 6–7). The measure does not produce `|det|²`; the
> Hermitian L/R doubling of the Kähler-Dirac note is an additional
> construction step, not a consequence of the matter-statistics clause.

and its relocation of the fork, same file `:110-130`:

> The gate question "first-order or second-order?" has, on this surface, a
> computed answer: **the measure side is first-order.** What remains is not
> a measure-order question at all. The binary that decides `r` is:
>
> > read the generation determinant on the **K-real section** of the
> > coupling space (Hermitian channel; `|b|²` dependence; sector slots;
> > `r = 1`), or read the **holomorphic first-order output** with outcomes
> > grained by K-orbits (one slot per `ω/ω̄` pair; `r = 1/2`).
>
> This is the same binary as the occupancy atom of [...]
> now realized dynamically on the actual matter surface rather than at the
> bookkeeping level: the sector-vs-orbit slot choice appears as the
> K-real-section-vs-K-orbit-quotient reading of one and the same first-order
> determinant. In particular, on this surface the custody note's two named
> selectors are not independent knobs: imposing K-reality on the coupling
> **is** what creates the rank-2 `|b|²` (count-twice) structure that the
> modulus-route no-gos then read out as `r = 1`. Neither horn is derived
> here; the runner prints both as declared-open residuals.

### (f.4) `scripts/berezin_detc_detr_fork_2026_06_04.py`
Exact-fraction/`CPair` engine. Builds `R[Z_3] = R (+) C`, the projectors
`P_s`/`P_d`, the doublet complex structure `J` with `J^2 = -P_d`
(`:226-236`), the `2x2` Majorana Pfaffian cell (`:266-274`), and the four-cell
table. Critical: `r_from_slot_count` (see (d.5)) and the recorded checks
`real_gaussian_slot_count_from_projector == 2`,
`holomorphic_berezin_complex_slot_count == 1`,
`polarization_decides_doublet_count`, `statistics_not_decisive_in_tested_cells`
(`:247-303`). Its premise, `docs/KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md:44-49`:

> POLARIZATION-SELECT (named conditional premise): a polarization for the
> generation doublet is SUPPLIED: either real (the doublet counts as two real
> slots) or holomorphic (the doublet complex structure J is chosen and the
> doublet counts as one complex slot). Not derived: no landed route selects a
> polarization; this note's four-cell mechanism shows the choice is not made by
> moving between Gaussian and Berezin statistics.

### (f.5) `scripts/frontier_koide_orbit_occupancy_independence_2026_06_09.py`
Carries the **review-forced repair** that is the campaign's most direct
precedent. `docs/KOIDE_ORBIT_OCCUPANCY_INDEPENDENCE_AND_PREMISE_CANDIDATE_NOTE_2026-06-09.md:29-43`:

> The 2026-07-10 independent review identified the decisive arithmetic error:
>
> > “The holomorphic Gaussian integral does not yield the claimed one-slot
> > equipartition moment: with `Z=pi/g` and `g=6 beta`, it gives
> > `<|b|^2>=1/(6 beta)`, hence `r=1`, not `1/2`. The runner obtains `r=1/2` by
> > hard-coding a per-slot quantum rather than deriving it from that integral.”
>
> The finding is correct. The repair makes four changes.
>
> 1. It derives every Gaussian moment directly and removes the hard-coded
>    `per_slot_quantum`.
> 2. It withdraws the former map `r = 1/(2 rho)` and every inference from a
>    partition-function ratio to an `r` ratio.

and the surviving decoupled arithmetic, same file `:104-126`:

> The runner also reproduces four older integral/kernel facts:
>
> ```text
> real two-coordinate Gaussian kernel:  Z = 2 pi/g
> Majorana two-by-two Pfaffian kernel:    Z = 2 pi/g
> polar complex Gaussian kernel:         Z = pi/g
> one-by-one complex Berezin kernel:      Z = pi/g
> ```
>
> These cells use different quadratic kernels or determinant powers. They are
> not two coordinate presentations of the identical diagnostic density above.
> Their factor-two ratio is therefore kept only as decoupled
> quadratic-kernel/determinant-power arithmetic. The values alone contain no
> equation for `r`. The former definitions
>
> ```text
> rho = (pi/g)/Z_d,
> r = 1/(2 rho)
> ```
>
> are withdrawn as an unsupported attribution of `r` to `Z_d`.

### (f.6) Adjacent CAR/Fock machinery (not on the corner carrier)
- `scripts/free_staggered_3plus1_reflected_gram_car_fock_representation_2026_07_12.py`
  / `docs/FREE_STAGGERED_3PLUS1_REFLECTED_GRAM_CAR_FOCK_REPRESENTATION_BOUNDED_THEOREM_NOTE_2026-07-12.md:20-33`:
  reflected two-slice Berezin Gram, OS quotient and stable-transfer frames,
  multitime Wick determinant == CAR-Fock exterior inner product. Its own scope
  line: "The theorem is conditional on the CAR/Grassmann branch and on the
  displayed free staggered action. It does not select CAR, does not select the
  physical carrier or one taste".
- `scripts/free_staggered_d_dimensional_two_step_many_body_transfer_2026_07_20.py`
  (this session's `d`-dim transfer + conditional Fock assembly). Its runner
  encodes a review-forced RETRACTION list at `:44-54` including the phrases
  `"C = 1 derived"` and `"action-level"` — an ABSENCE gate. **Wave 2 must not
  cite that note as an action-level result.**
- `scripts/acphilambda_record_outcome_orbit_occupancy_non_supply_no_go_2026_07_04.py`
  + helper `scripts/acphilambda_occupancy_wpower_n7_independent_certificate_2026_07_13.py`
  — already compute the block-Pfaffian power of a generic supplied complex
  Grassmann sector and the modulus-square-on-adjoining-a-conjugate-sector fact.
- `scripts/kcpt_corner_carrier_lattice_delivery_hw1_doublet_pair_polarization_2026_07_17.py`,
  `scripts/kcpt_corner_carrier_antilinear_nonhermitian_kreal_readout_classification_2026_07_18.py`,
  `scripts/kcpt_corner_carrier_two_presentation_swap_proper_rotation_conjugacy_2026_07_18.py`
  — exact integer lattice delivery of the carrier, its `K`-polarization, the
  antilinear/non-Hermitian readout faces, and the rotation-conjugacy of the
  presentation swap. **These are one-particle-space computations. None builds a
  CAR algebra or a Fock space over the corner carrier.**

---

## (g) GAP LIST — what a native mode-count computation needs that NO landed note supplies

**G1 — There is no CAR algebra over the corner carrier anywhere on
`origin/main`.** The corner-carrier notes are all one-particle (3x3 matrix)
computations. The CAR/Fock machinery that exists
(`FREE_STAGGERED_3PLUS1_REFLECTED_GRAM_CAR_FOCK...`, the JW realization in the
spin-statistics note) is built on the full lattice site algebra or on abstract
one-particle spaces, never on `V = span{chi_k : hw(k)=1}`. Wave 2 must construct
`CAR(V)` natively — including the map from the lattice `(χ_x, χ̄_x)` generators
to corner modes — and no landed note supplies that map.

**G2 — Nothing identifies "occupancy slot" with "Grassmann generator" or with
"CAR mode".** Verbatim, `docs/KCPT_COUPLING_TRIPLE_BEREZIN_COUNT_BINARY_MEASURE_COLLAPSE_BOUNDED_THEOREM_NOTE_2026-07-17.md:112-115`: "no framework clause identifies occupancy slots with
Grassmann generators, and T3 makes no equivalence claim." A mode count therefore
does not, by itself, produce an occupancy weight. This is the largest gap.

**G3 — The `w -> r` and `slot -> r` maps are declared dictionaries, and the
closure criterion forbids inserting a readout dictionary.** See (d.4) Residual
Atom 2 and (e). So a native mode count that then applies `r = n_d/2` would be
inserting exactly what the criterion excludes. A closing theorem needs an
independently derived energy/weight law, not a dictionary.

**G4 — The `r`-moving axis is an ENERGY-PER-CELL law, not a mode count.** The
two horns are `E_s = E_d` (per-outcome-cell) vs `E_d = 2 E_s` (per-real-mode)
(`docs/KOIDE_FORMATION_GATE_RELOCATION_TIED_MEASURE_PER_CELL_WEIGHT_COMPATIBILITY_BOUNDED_THEOREM_NOTE_2026-07-12.md:180-183`). Nothing on the carrier supplies an energy law.
The Berezin note says so explicitly at `:316-318`: "Both
are conditional on their respective supplied granularity laws; neither
law is derived there or here, and the Berezin surface supplies neither."

**G5 — The measure-order question is already answered count-once, and answering
it again does not move `r`.** See (f.3). Wave 2 must state, up front, what its
mode count would decide that `Fact 1` has not already decided.

**G6 — Two independent residuals, proved non-retiring.** `docs/KOIDE_FIRST_ORDER_SECTION_TIE_VS_OUTCOME_LABEL_RESIDUAL_LOCALIZATION_BOUNDED_THEOREM_NOTE_2026-07-11.md:184-189`:

> **N2 — wall independence.** The stage-selection residual and the
> equipartition-granularity residual are independent. One may specify when
> K-reality acts without choosing an energy law, or impose one of the two energy
> laws without deriving when the physical action imposes K-reality. A future
> Osterwalder–Schrader theorem could close the first while leaving the second
> open.

A mode-count theorem plausibly touches only the first. The second would remain.

**G7 — `K` on the corner carrier is not identified with physical CPT.** The
carrier notes use only entrywise conjugation. The framework's CPT antiunitaries
live on staggered lattice operators
(`docs/AXIOM_FIRST_CPT_THEOREM_STRETCH_NOTE_2026-04-29.md:341`;
`docs/CPT_D_LEVEL_FINITE_LATTICE_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-17.md:268`).
The compound name "K/CPT" is used throughout the occupancy stack without a
landed bridge. If Wave 2's count depends on `K` being CPT, that bridge is
missing.

**G8 — The carrier itself is FLAGGED as supplied at its mechanism origin.**
`docs/KCPT_CORNER_CARRIER_LATTICE_DELIVERY_HW1_DOUBLET_PAIR_POLARIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md:102-107`:

> 5. **Scope.** This is a lattice realization of the spectral-pairing note's supplied
>    triple on the gate note's composed surface, at the gate note's declared premise
>    set (residuals inherited below). On the mechanism-note side the corner surface
>    remains supplied: nothing here converts the mechanism note's declaration into a
>    derivation of its own surface. The FLAG is answered at the gate note's premise
>    set, not erased at its origin.

**G9 — No Yukawa / no physical coupling.** The `C_3[111]` coupling `W(a,b,c)` is
a **declared probe** everywhere it appears:
`docs/KCPT_COUPLING_TRIPLE_TWO_PRESENTATION_DERIVABLE_CLASS_SPECTRAL_PAIRING_BOUNDED_THEOREM_NOTE_2026-07-16.md:85-86`:

> **FLAG — probe, not derived form:** no Yukawa identification, physical
> action, or measure is derived for it, there or here.

So "the physical charged-lepton matter action" — the obligation's actual
target — does not exist on `origin/main` in any form.

**G10 — The whole stack is `unaudited`.** Ledger `effective_status`
(read from `docs/audit/data/ledger/**` on `origin/main`):

| row | effective_status |
|---|---|
| `acphilambda_fermionic_realification_pfaffian_power_identity_narrow_theorem_note_2026-07-12` | **retained** |
| `ac_orbit_occupancy_statistical_grain_derivation_obligation` | audited_renaming (open_gate) |
| `three_generation_hw1_distinct_translation_characters_narrow_theorem_note_2026-05-10` | retained_pending_chain |
| `kcpt_coupling_triple_berezin_count_binary_measure_collapse_...2026-07-17` | unaudited |
| `kcpt_coupling_triple_two_presentation_derivable_class_spectral_pairing_...2026-07-16` | unaudited |
| `kcpt_corner_carrier_lattice_delivery_hw1_doublet_pair_polarization_...2026-07-17` | unaudited |
| `kcpt_corner_carrier_antilinear_nonhermitian_kreal_readout_classification_...2026-07-18` | unaudited |
| `koide_staggered_first_order_generation_determinant_...2026-06-11` | unaudited |
| `koide_orbit_occupancy_independence_and_premise_candidate_note_2026-06-09` | unaudited |
| `koide_berezin_detc_vs_detr_fork_mechanism_note_2026-06-04` | unaudited |
| `koide_formation_gate_relocation_...2026-07-12` | unaudited |
| `koide_formation_weight_law_expressibility_classification_...2026-07-12` | unaudited |
| `acphilambda_occupancy_grain_menu_counting_...2026-07-16` | unaudited |
| `acphilambda_occupancy_grain_rule_class_universality_...2026-07-11` | unaudited |
| `acphilambda_record_outcome_orbit_occupancy_non_supply_no_go_note_2026-07-04` | unaudited |
| `staggered_dirac_realization_gate_note_2026-05-03` | unaudited |
| `staggered_dirac_common_hw1_bz_corner_carrier_identification_bridge_...2026-07-05` | unaudited |
| `axiom_first_spin_statistics_theorem_note_2026-04-29` | unaudited |
| `charged_lepton_koide_value_full_chain_of_custody_2026-06-02` | unaudited |
| `three_generation_observable_theorem_note` | unaudited |

**Exactly one load-bearing row in the entire carrier/count stack is `retained`:
the realification Pfaffian power identity.** Anything Wave 2 builds sits on
`unaudited` premises unless it rebuilds them natively — which the repo's own
lesson ("Build cited algebra, don't just cite") requires anyway.

**G11 — The campaign's own foreclosure list should be checked against a
foreclosure it does not name.** `docs/CORNER_FERMION_DETERMINANT_DOES_NOT_SELECT_KOIDE_R_HALF_NARROW_OBSTRUCTION_NOTE_2026-06-04.md:36-51`
already prunes the corner-fermion-determinant route: at fixed Frobenius scale
`det(M)` is not stationary at `r = 1/2`; its stationary points are `r = 1` and
`r = 4`; and (item 3) `r = 1/2` IS the max-sector-entropy point but "the
dynamical (determinant) criterion and the balanced (entropy) criterion
**disagree**". Its N1 marks 3 of 5 routes ruled out with 2 untested
("taste-breaking scalar normalization", "multi-factor Connes-Lott"). The
campaign's foreclosure list does not mention this row. Flagging for the
kill-check worker; the scout takes no position on whether it bites.

---

## UNCERTAINTIES THE SCOUT IS EXPLICITLY FLAGGING (not smoothed)

1. **The R5b assignment mismatch in (c.2) is an observation, not a defect
   finding.** R5b flags itself as declared bookkeeping and disclaims
   equivalence, which pre-empts a defect reading. The scout cannot rule out that
   the `(1,1)` vs `(2,2)` exponent bookkeeping is a legitimate alternative
   resolution in which `|lam_1|^2` is the atomic doublet grain. **What the scout
   IS confident of: the campaign target statement's claim that the four framings
   are equivalent is not supported by any landed note, and one of the four
   framings is computed `r`-neutral three separate times.**

2. **Whether "the K-conjugate partner copy" is an independent Grassmann sector
   or the same sector in a rotated frame is section-dependent** and, per (b.3),
   is a genuinely open technical question. The scout did not resolve it.

3. **The scout did not locate any landed note stating a mode count of 2 vs 3
   complex modes (4 vs 6 generators).** Absence of a needle after targeted
   grepping (`6 generators|12 generators|N-generator|generator count`, plus
   full-text reads of the 8 notes in the count chain) is weaker evidence than a
   found needle. Treat G2's "no landed 4-vs-6 statement" as
   thorough-search-negative, not proved-absent.

4. **`origin/main` moved three times during this scout** (`f8f9957` -> `288cdb2`
   -> `02f9359`). No quoted file changed, but a Wave-2 worker should re-fetch
   and re-verify line numbers before quoting them in a shippable note.

5. **The scout read only the notes reachable from the count/carrier chain.** The
   audit backlog and the `archive_unlanded/` tree were not searched for further
   generator-count statements; `archive_unlanded/` is unlanded by definition and
   was excluded from all greps.
