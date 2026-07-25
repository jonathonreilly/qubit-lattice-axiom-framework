# Wave 1 KILL-CHECK: is the CAR / Berezin mode-content route already foreclosed?

**Date:** 2026-07-24
**Role:** adversarial kill-check per CAMPAIGN.md hard rule 1. This report sets
no audit verdict and predicts none. All ledger statuses quoted below are
pipeline-derived data read off `docs/audit/data/ledger/`, reported as facts
about the ledger, not as judgements.
**Base:** `origin/main` @ `02f9359281` (fetched 2026-07-24).

**Bottom line up front: DEAD ON ARRIVAL.** Not because the 07-04 no-go
forecloses it — that no-go does leave the door the campaign quotes, verbatim
and correctly — but because (i) the route was already executed end-to-end on
this exact carrier seven days ago and produced both horns without selecting
either, (ii) the quantity it proposes to compute is proved *r*-neutral by exact
computed algebra, so even a successful derivation would not move `r`, and
(iii) the campaign's four-way "equivalently" chain contradicts landed content
at two of its three joints.

---

## 1. Method and scope

`git fetch origin main`, then exhaustive search of `origin/main:docs/` and
`origin/main:scripts/` on: Koide, AC_phi_lambda, Brannen, K/CPT orbit,
det_C / holomorphic grain, 2-cell vs 3-cell menu, Grassmann generator counting,
orbit-occupancy, r=1/2 vs r=1, weight `w`, corner carrier, realified/complex
grain, Berezin measure, complex structure, polarization, CAR.

Fourteen landed documents and five runners bear directly. The load-bearing ones:

| file | date | ledger `effective_status` \| `audit_status` |
|---|---|---|
| `docs/ACPHILAMBDA_RECORD_OUTCOME_ORBIT_OCCUPANCY_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md` | 07-04 | unaudited \| unaudited |
| `docs/ACPHILAMBDA_FERMIONIC_REALIFICATION_PFAFFIAN_POWER_IDENTITY_NARROW_THEOREM_NOTE_2026-07-12.md` | 07-12 | **retained \| audited_clean** |
| `docs/KCPT_ORBIT_CONSTANCY_AND_DETERMINANT_CHARACTER_BOUNDARY_SUPPLIED_CONTEXT_BRIDGE_NOTE_2026-07-04.md` | 07-04 | audited_conditional \| audited_conditional |
| `docs/AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md` | 07-11 | audited_renaming \| audited_renaming |
| `docs/KCPT_COUPLING_TRIPLE_BEREZIN_COUNT_BINARY_MEASURE_COLLAPSE_BOUNDED_THEOREM_NOTE_2026-07-17.md` | 07-17 | unaudited \| unaudited |
| `docs/KCPT_COUPLING_TRIPLE_TWO_PRESENTATION_DERIVABLE_CLASS_SPECTRAL_PAIRING_BOUNDED_THEOREM_NOTE_2026-07-16.md` | 07-16 | unaudited \| unaudited |
| `docs/KCPT_CORNER_CARRIER_LATTICE_DELIVERY_HW1_DOUBLET_PAIR_POLARIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md` | 07-17 | unaudited \| unaudited |
| `docs/KOIDE_R_HALF_POLARIZATION_SELECTOR_TESTED_STATIC_READOUT_NO_GO_NOTE_2026-06-08.md` | 06-08 | unaudited \| unaudited |
| `docs/KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md` | 06-04 | unaudited \| unaudited |
| `docs/FLAVOR_FIND_J_ROUND2_POWER_NOT_COUNT_2026-06-02.md` | 06-02 | unaudited \| unaudited |
| `docs/FLAVOR_FIND_J_CONSOLIDATION_KAPPA_IS_THE_INPUT_2026-06-02.md` | 06-02 | unaudited \| unaudited |
| `docs/KOIDE_CONVENTION_INVARIANT_SCALAR_SELECTOR_DOUBLET_CONSTANCY_NARROW_THEOREM_NOTE_2026-07-12.md` | 07-12 | unaudited \| unaudited |
| `docs/ACPHILAMBDA_OCCUPANCY_GRAIN_MENU_COUNTING_MEASURE_DYNAMICAL_STATIC_CORRESPONDENCE_BOUNDED_THEOREM_NOTE_2026-07-16.md` | 07-16 | unaudited \| unaudited |
| `docs/OCCUPANCY_READOUT_EXPONENT_BEREZIN_SUBSUMPTION_BOUNDED_THEOREM_NOTE_2026-06-09.md` | 06-09 | unaudited \| unaudited |

**FLAG — status caveat, stated up front and not smoothed.** Only *one* of the
kill-relevant documents is retained-grade (the 07-12 realification/Pfaffian
identity). Most of the evidence below is landed-on-main but `unaudited`. So the
honest form of this kill-check is: *the route is foreclosed by landed content,
most of which has not yet been through the audit lane.* That weakens
"foreclosed by a **retained** no-go" but not "already done and it did not
work" — the executed-runner evidence in §4 is a fact about what exists on main
regardless of grade.

---

## 2. (a) The open-door sentence: verified verbatim, and exactly what it covers

The campaign asserts the no-go "explicitly DECLINES to foreclose a future
physical CAR/action theorem that derives a specific Gaussian measure."

**The sentence exists, verbatim, and is unique in the repo.**
`git grep -c "future physical CAR/action theorem"` over `docs/` returns exactly
one hit, in one file. In full context,
`docs/ACPHILAMBDA_RECORD_OUTCOME_ORBIT_OCCUPANCY_NON_SUPPLY_NO_GO_NOTE_2026-07-04.md:17-48`:

> ## Narrow no-go claim
>
> Grant an auxiliary invertible complex block carrier. Even with that grant, the
> [four axioms](MINIMAL_AXIOMS_2026-06-29.md) do not entail whether an additive,
> K-even determinant readout uses one complex determinant grain or the
> realified two-power grain.
>
> [... `F_C(A) = log |det_C A|`, `F_R(A) = log det_R R(A) = 2 F_C(A)` ...]
>
> This is a current-surface non-entailment result. It does not rule against a
> future physical CAR/action theorem that derives a specific Gaussian measure.

The campaign's reading of that sentence is **correct**: the 07-04 no-go does
not foreclose the route. It is a non-entailment result about the four-axiom
surface, not about future theorems.

**But three things the campaign's framing gets wrong about it.**

**(a.1) The door is symmetric between the horns, not a door to `r = 1/2`.**
CAMPAIGN.md calls this "*the ONE door* the landed no-go explicitly leaves
open". The no-go's N6 table lists five preserved paths, and the *second* one is
the mirror image (`...NO_GO_NOTE_2026-07-04.md:189`):

> | real or Majorana action theorem | future physical theorem outside the four axioms and this note | derive a real determinant or Pfaffian grain if that action is selected |

with the CAR row immediately above it at `:188`:

> | action-native CAR/Berezin theorem | future physical theorem outside the four axioms and this note | derive the complex first-power grain from the physical action |

So the no-go preserves an action-native route to *each* horn, even-handedly.
Reading it as a door to count-once is a selection the source does not make.

**(a.2) The door is to an ACTION theorem, not to a mode count.** Both rows say
"derive ... **from the physical action**". The obligation's closure criterion,
verbatim (`docs/AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md:21-24`):

> A closing theorem must derive the physical matter action and its measure, then
> distinguish the count-once `det_C`/holomorphic realization from the
> count-twice `|det_C|^2`/realified realization without inserting the desired
> charged-lepton value or readout dictionary.

The gate is **two-part and ordered**: derive the action *and its measure* first;
the count is then read off. The campaign proposes to skip part one and count
modes directly. A mode count is *downstream* of the measure — the generator set
is an input to a Berezin integral, not an output of it. Counting the modes of a
Berezin representation you yourself specified derives nothing about which
representation the physics selects.

**(a.3) The no-go's own scope paragraph disclaims exactly the campaign's use**
(`...NO_GO_NOTE_2026-07-04.md:118-121`):

> The result does not derive a physical matter action, Berezin measure, K/CPT
> structure, determinant line, polarization, orbit quotient, or physical
> record-to-action map. It does not set `r`, `delta`, or any mass, and it does
> not force `r=1/2`.

**Answer to (a):** No landed no-go covers the CAR/mode-content route as an
impossibility claim. The quoted sentence is real, verbatim, unique, and the
campaign read it correctly. What it excludes: nothing about the future. What it
does *not* exclude: it does not exclude the campaign's route — **and it does not
endorse it either**; it names a symmetric pair of *action* routes, one to each
horn. The campaign is not killed here. It is killed in §3 and §4.

---

## 3. (b) Is the mode count independent, or definitionally circular?

**The supervisor's worry is correct, and it is landed in three independent
places, one of which uses the word "circular".**

### 3.1 The carrier is 3-dimensional; its CAR algebra has three channel atoms

The corner carrier is no longer abstract — it was lattice-delivered on 07-17.
`docs/KCPT_CORNER_CARRIER_LATTICE_DELIVERY_HW1_DOUBLET_PAIR_POLARIZATION_BOUNDED_THEOREM_NOTE_2026-07-17.md:87-101`
computes that the `C_3[111]` rotation restricted to the hw=1 kernel triplet of
the staggered operator on the periodic `4^3` torus **is** the real cyclic `C`:

> 1. `U_R V = V C` exactly on the integer lattice, where `V` is the ordered hw=1
>    corner triplet and `C = [[0,0,1],[1,0,0],[0,1,0]]`.
> [...]
> 3. Because the corner basis is entrywise real, ambient complex conjugation on the
>    lattice Hilbert space restricts to entrywise conjugation `K` in the corner
>    basis: `conj(V z) = V conj(z)` for every coefficient vector `z`.

So the carrier is `R^3` with a `C_3` action and entrywise `K`. Its channel
decomposition, with `w = -1/2 + (sqrt(3)/2) i` and
`P_chi = (I + conj(chi) C + conj(chi)^2 C^2)/3`:

```text
C^3 = I_3,        C P_chi = chi P_chi,       chi in {1, w, conj(w)}
W(a,b,c) = a I + b C + c C^2
lam_k    = a + b w^k + c w^(2k),   k = 0,1,2
det W    = a^3 + b^3 + c^3 - 3abc = lam_0 lam_1 lam_2
```

and `K` fixes `P_1` and swaps `P_w <-> P_wbar` (`...LATTICE_DELIVERY...:109-117`).
Three channel atoms; two K-orbits.

A CAR/Berezin representation of *that* carrier carries one `(theta, thetabar)`
pair per channel — **three complex modes.** This is not my construction; it is
what the landed runner literally does. `scripts/kcpt_coupling_triple_berezin_count_binary_measure_collapse_2026_07_17.py`
sets `th3 = [0, 2, 4]`, `tb3 = [1, 3, 5]` and gates

```python
check("B3.1", "generator-count bookkeeping: horn m uses 6m generators, read "
      "off the constructed integration orders (m=1: 6; m=2: 12)",
      len(th3 + tb3) == 6 and len(order12) == 12
      and len(order12) == 2 * len(th3 + tb3))
```

Three thetas, three thetabars: **n = 3 complex modes**, one per channel atom.

### 3.2 The circularity, stated exactly

The campaign's decision rule is: *"If the carrier has n complex modes
(n theta, n theta-bar), the K-conjugate partner copy is NOT independently
integrated, the measure grain is det_C, and count-once is DERIVED => r = 1/2."*

Run it. The carrier has `n = 3`. The rule returns "count-once", grain `det_C`.
But `det_C` on this carrier is

```text
det3 = lam_0 * lam_1 * lam_2
```

and on entrywise-real `(a,b,c)` (where `lam_2 = conj(lam_1)`, `lam_0` real),

```text
det3 = lam_0 * |lam_1|^2          singlet exponent 1, doublet exponent 2
```

The doublet already enters **squared** in the count-once grain, because the
carrier has two doublet channels. Getting "one factor per K-orbit" would require
the grain `lam_0 * lam_1` — which is not the determinant of anything on this
carrier. It is the determinant on the **K-orbit quotient**.

So the count-once/count-twice binary is *not* "n modes vs 2n modes on the
carrier". It is: **do you build the CAR algebra on the carrier (3 atoms) or on
the K-orbit quotient (2 atoms)?** And "the K-orbit is one record content" is
exactly the supplied premise ORBIT-INDEXING. From
`docs/KCPT_ORBIT_CONSTANCY_AND_DETERMINANT_CHARACTER_BOUNDARY_SUPPLIED_CONTEXT_BRIDGE_NOTE_2026-07-04.md:60-71`:

> - **ORBIT-INDEXING:** the context's record contents are indexed by `K`-orbits,
>   so `K`-conjugate outcomes carry the same record content;
> [...]
> ORBIT-INDEXING and the determinant-character/log-character homomorphism
> boundary are supplied context structure. They are not derived from Record.

and `docs/KOIDE_CONVENTION_INVARIANT_SCALAR_SELECTOR_DOUBLET_CONSTANCY_NARROW_THEOREM_NOTE_2026-07-12.md:124-127`:

> Thus the unlabeled three-block partition is convention-stable and resolves all
> three sectors without privileging either doublet member. Convention freeness
> alone does not derive ORBIT-INDEXING or identify the conjugate sectors as one
> record content.

**That is the circularity, sharply:** to count "one complex mode per K-orbit"
you must first have identified the K-orbit as one occupancy slot. Counting the
modes of "the carrier's CAR algebra" returns 3 (one per channel) by
construction. Returning 2 requires having already assumed count-once. The
question is definitionally circular exactly as the supervisor predicted.

### 3.3 The repo already names this move a "category slip" and "circular"

`docs/KOIDE_R_HALF_POLARIZATION_SELECTOR_TESTED_STATIC_READOUT_NO_GO_NOTE_2026-06-08.md:52-60`,
verbatim:

> 1. **The Koide magnitude is a sesquilinear energy, not a determinant or a
>    mode-count — and its modulus is rank-2.** `E_d = Tr(M†M)|_doublet = 6|b|²`; its
>    real Hessian over `(Re b, Im b)` is `diag(12,12)`, **rank 2** → two real modes →
>    `(1,2) → r=1`. This is the `#2624` Coleman-Weinberg modulus wall, robust for any
>    smooth modulus `f(|b|²)` (verified: the wall runner). The det_C-vs-det_R
>    distinction is real but lives on `det(M)` (the operator), where `det_R=|det_C|²`;
>    the Koide magnitude is **not** a determinant of `M`. Transferring an
>    operator-symmetry onto "the energy counts `b` once" is a category slip and is
>    **circular** (it assumes the asymmetric `(1,1)` split it claims to derive).

That note tested **eight** selection-principle lenses on exactly this question
(`:42-47`):

> **8 selection-principle lenses** were tested (framework-native complex structure `J_cs`;
> geometric quantization / Kähler polarization; minimum-information / MDL record;
> equivariant holomorphic index; KMS / modular; **Grassmann / Pfaffian statistics**; CPT /
> antiunitary; canonical quantization uniqueness). **Result inside the tested class: 0 of 8
> survived.**

The campaign's route is lens 6 (Grassmann/Pfaffian statistics), reached through
lens 1 (native complex structure) and lens 2 (Kähler polarization). All three
were tested. None survived.

### 3.4 The polarization *is* the count — landed as a named conditional premise

`docs/KOIDE_BEREZIN_DETC_VS_DETR_FORK_MECHANISM_NOTE_2026-06-04.md:43-49`:

> ```text
> POLARIZATION-SELECT (named conditional premise): a polarization for the
> generation doublet is SUPPLIED: either real (the doublet counts as two real
> slots) or holomorphic (the doublet complex structure J is chosen and the
> doublet counts as one complex slot). Not derived: no landed route selects a
> polarization; this note's four-cell mechanism shows the choice is not made by
> moving between Gaussian and Berezin statistics.
> ```

and its four-cell table (`:82-87`) computes that **Berezin statistics do not
decide it**:

| action family | polarization | doublet count | result |
|---|---|---:|---|
| real Gaussian | real | 2 real slots | `r = 1`, `Q = 1` |
| Majorana Berezin | real | 2 real slots | `r = 1`, `Q = 1` |
| holomorphic Gaussian | holomorphic | 1 complex slot | `r = 1/2`, `Q = 2/3` |
| holomorphic Berezin | holomorphic | 1 complex slot | `r = 1/2`, `Q = 2/3` |

Reading down the "polarization" column: the result is constant in the statistics
and varies only with the polarization. `:38` states it flatly:

> The fork separation is that polarization, not Gaussian versus Berezin statistics,
> decides the doublet slot count.

The **retained, audited_clean** 07-12 realification note closes off the
remaining escape — that the count could be read off from a change of Grassmann
coordinates.
`docs/ACPHILAMBDA_FERMIONIC_REALIFICATION_PFAFFIAN_POWER_IDENTITY_NARROW_THEOREM_NOTE_2026-07-12.md:102-113`:

> For an invertible coordinate change `Psi=M Xi`, the kernel becomes
> `M^T A_K M`. Pfaffians and Berezin measures transform as
>
> ```text
> Pf(M^T A_K M) = det(M) Pf(A_K),
> D(Psi) = det(M)^(-1) D(Xi)
> ```
>
> for the paired orientation convention. The factors cancel in the Gaussian.
> Thus a complex-to-Majorana coordinate change cannot alter the determinant
> power. A second power arises after the independent conjugate block is
> adjoined.

and `:143-145`:

> Within the displayed Grassmann-Gaussian construction, obtaining the modulus square instead
> uses a **supplied** conjugate sector or conjugate-paired readout.

"Supplied". The second power is an *input* (does the theory contain an
independent conjugate sector?), not an *output* of counting. Same finding at
`docs/OCCUPANCY_READOUT_EXPONENT_BEREZIN_SUBSUMPTION_BOUNDED_THEOREM_NOTE_2026-06-09.md:53-55`:

> 6. **Adversarial multiplicity (B6):** in the complex-mode realization the
>    exponent-2 atom (`a²`) is obtainable *only* by doubling the field content
>    (computed: two independent modes → `a²`) — i.e. by changing the
>    *realization*, never by a readout choice.

**Answer to (b):** The mode count is **not** an independent fact about the
carrier. It is fixed by (i) the polarization choice, which the repo carries as
the named conditional premise POLARIZATION-SELECT and which Berezin statistics
provably do not decide, and (ii) the orbit-vs-channel identification
(ORBIT-INDEXING), which is supplied context explicitly not derived from Record.
The question is definitionally circular. The repo says so in the word
"circular" at `KOIDE_R_HALF_POLARIZATION_SELECTOR..._2026-06-08.md:60`.

---

## 4. (c) Has anyone computed this count already? Yes — twice, on this carrier

### 4.1 The full construction was run on 2026-07-17, both horns

`docs/KCPT_COUPLING_TRIPLE_BEREZIN_COUNT_BINARY_MEASURE_COLLAPSE_BOUNDED_THEOREM_NOTE_2026-07-17.md`
with runner `scripts/kcpt_coupling_triple_berezin_count_binary_measure_collapse_2026_07_17.py`
(`TOTAL: PASS=121 FAIL=0`) builds exactly the object the campaign proposes:
a finite Grassmann algebra on `theta_1..n, thetabar_1..n` with quadratic weight
`exp(-S)`, `S = sum thetabar_i M_ij theta_j`, on the supplied `C_3` corner
carrier, with pinned measure ordering and *computed* (not chosen) sign.

Results, both computed exactly (`:156-176`, runner checks B2.3–B2.6):

```text
6 generators  (theta_1..3, thetabar_1..3), kernel W(a,b,c):
    Integral = det3 = lam_0 * |lam_1|^2                     [count-once]

12 generators (adjoin the K-conjugate partner copy W(conj a, conj b, conj c)):
    Integral = det3 * conj(det3) = |det3|^2
             = lam_0^2 * |lam_1|^4                          [count-twice]
```

Negative control 3 (`:336-339`), verbatim:

> 3. **Neither horn forced** (runner B5): at the entrywise-real witness
>    `(3,1,1)` the count-once Berezin integral is `20` and the count-twice
>    12-generator Berezin integral is `400`; both are nonzero and
>    well-defined, and nothing on the surface prefers either.

Both horns are computable, both are well-defined, neither is selected. The
campaign's Wave 1 deliverable already exists and returned "no selection".

### 4.2 Why it did not settle the binary — reason 1: the bridge is declared, not derived

`...BEREZIN_COUNT_BINARY...2026-07-17.md:108-115`, verbatim:

> - **Declared count-binary reading (R5b).** The translation "graining horn
>   `m` corresponds to `6m` Grassmann generators" (`m = 1`: one triple copy,
>   6 generators; `m = 2`: the triple copy plus its K-conjugate partner copy,
>   12 generators). **FLAG — declared reading, not an equivalence:** both
>   sides of the translation are computed exactly (runner B2, B3), and the
>   correspondence between the graining slot count and the generator count is
>   declared bookkeeping; **no framework clause identifies occupancy slots with
>   Grassmann generators**, and T3 makes no equivalence claim.

This is fatal to the campaign's premise independently of everything else.
CAMPAIGN.md states the binary "four equivalent ways", one of which is
"6 Grassmann generators per triple copy". Landed content says that leg is
**declared bookkeeping, explicitly not an equivalence**, with no framework
clause supporting it. Even a perfect Wave 1 derivation of "the carrier has
`n` complex modes" would land on the wrong side of a bridge nobody has built.

### 4.3 Why it did not settle the binary — reason 2: the quantity is *r*-neutral

This is the sharpest kill and it is exact computed algebra, stated in two
independent landed notes.

`...BEREZIN_COUNT_BINARY...2026-07-17.md:177-183`:

> 3. **r-neutral doubling.** `lam_0^2 * |lam_1|^4 = (lam_0 * |lam_1|^2)^2`
>    identically on entrywise-real triples: the singlet exponent and the
>    doublet exponent double together, and every doublet-to-singlet power
>    ratio is unchanged.

`docs/KCPT_COUPLING_TRIPLE_TWO_PRESENTATION_DERIVABLE_CLASS_SPECTRAL_PAIRING_BOUNDED_THEOREM_NOTE_2026-07-16.md:186-190`:

> 1. **Positive control (exact).** On entrywise-real triples
>    `|det3|^2 = lam_0^2 * |lam_1|^4`: passing from `det3` to `|det3|^2`
>    doubles the singlet exponent and the doublet exponent together, so every
>    doublet-to-singlet power ratio is unchanged. The pairing statement is
>    r-neutral (runner V3).

Rebuilt natively — the exponent bookkeeping in full:

```text
count-once :  det3    = lam_0^1 * |lam_1|^2
              singlet exponent  s = 1
              doublet exponent  d = 2
              ratio d/s = 2

count-twice:  det3^2  = lam_0^2 * |lam_1|^4
              singlet exponent  s = 2
              doublet exponent  d = 4
              ratio d/s = 4/2 = 2        <-- IDENTICAL
```

The generator-count binary is a **global factor-2 multiplicity**. It multiplies
every exponent by 2 and therefore cannot move any ratio. But `r` *is* a ratio:
`r = |b|^2 / a^2`, doublet over singlet.

What actually moves `r` is **menu cardinality**, a partition-refinement, not a
doubling. From
`docs/ACPHILAMBDA_OCCUPANCY_GRAIN_MENU_COUNTING_MEASURE_DYNAMICAL_STATIC_CORRESPONDENCE_BOUNDED_THEOREM_NOTE_2026-07-16.md:16-19`,
with `r = (1-w)/(2w)` and `Q = (1+2r)/3`:

```text
2-cell menu {singlet, doublet-orbit}      uniform w = 1/2
    r = (1 - 1/2)/(2 * 1/2) = (1/2)/1     = 1/2      Q = (1+1)/3 = 2/3
3-cell menu {singlet, w-atom, wbar-atom}  uniform w = 1/3
    r = (1 - 1/3)/(2 * 1/3) = (2/3)/(2/3) = 1        Q = (1+2)/3 = 1
```

equivalently, in the section-tie energy form quoted at
`...BEREZIN_COUNT_BINARY...2026-07-17.md:312-317`, for `epsilon > 0`:

```text
per-outcome-cell:  3a^2 = eps,  6|b|^2 = eps    =>  a^2 = eps/3, |b|^2 = eps/6
                   r = (eps/6)/(eps/3) = 1/2,   Q = 2/3
per-real-mode:     3a^2 = eps,  6|b|^2 = 2 eps  =>  a^2 = eps/3, |b|^2 = eps/3
                   r = (eps/3)/(eps/3) = 1,     Q = 1
```

**Doubling ≠ refining.** `6 -> 12` generators is a doubling: r-neutral,
computed. `2 -> 3` cells is a refinement of the doublet: r-moving. The campaign
proposes to decide the second by computing the first. Those are different
operations on different objects, and the landed algebra shows the first has
zero leverage on `r`.

**A stronger form of the same point, derived here** (my arithmetic, flagged as
mine, not a landed sentence): apply the campaign's decision rule literally.
The carrier has `n = 3` complex modes. Under the most natural mode↦slot reading
— one complex mode is one occupancy slot — three modes give the **3-cell menu**,
`w = 1/3`, `r = 1`. That is the *opposite* of what the campaign expects
count-once to yield. The campaign's dictionary calls 6 generators "count-once ⇒
r = 1/2" while the algebra those 6 generators actually implement is one mode
per channel atom, i.e. the per-channel horn. This inconsistency is only
invisible because the slot↦generator map is the undischarged declared reading of
§4.2. **FLAG:** the "natural reading" is itself a reading; the repo's position
is that no framework clause fixes it (`R5b`, quoted above), which is precisely
the point.

### 4.4 The route was already pruned by name on 2026-06-02

`docs/FLAVOR_FIND_J_ROUND2_POWER_NOT_COUNT_2026-06-02.md` — title:
*"Fermionic Power Does Not Select the `J` Pairing"*. Its closed packet
(`:16-27`):

> > The fermionic/Berezin determinant power does not by itself choose the
> > antisymmetric `J=C-C^2` pairing of the real `C3` doublet.
>
> Equivalently, the route
>
> ```text
> fermionic first-order matter -> Berezin determinant -> forced det_C/J pairing
> ```
>
> is pruned.

Its three direct checks (`:30-49`) are the campaign's route dismantled
piece by piece:

> 1. **Power is not count.** [...] This is an exponent statement, not a count of
>    whether the generation doublet should be treated as two real modes or one
>    complex mode.
> 2. **Berezin gives a determinant product, not a Frobenius block-total.** [...]
>    That cubic determinant functional is not the quadratic block-total functional
>    `E_singlet=3a^2`, `E_doublet=6|b|^2` whose equal-block convention would set
>    `r=1/2`.
> 3. **`C3` admits both invariant bilinears.** The symmetric identity `I` and
>    the antisymmetric `J=C-C^2` both satisfy `C^T X C = X`. Therefore the
>    finite `C3` covariance condition does not select `J` over `I`.

Check 2 is the same "the Koide magnitude is not a determinant" wall as §3.3,
found independently six days earlier. Check 3 shows the carrier's own
equivariance permits both polarizations.

And the round-4 consolidation
(`docs/FLAVOR_FIND_J_CONSOLIDATION_KAPPA_IS_THE_INPUT_2026-06-02.md:36-42`)
closes the last version of "just count the blocks":

> 2. The real regular `C3` central projectors have ranks `(1,2)`. The
>    Plancherel/character measure therefore weights the trivial and standard
>    sectors by dimension, not by equal irreducible-block count.
> 3. `K0(R[C3]) = K0(R (+) C) = Z^2` counts the two central blocks, but the same
>    central idempotents admit positive `C3`-invariant metric families with
>    different trivial:standard energy ratios. `K0` therefore does not by itself
>    select an energy weighting.

That is the decisive general form: **the count is already available and equals
2** — `K0(R[C_3]) = Z^2`, two central blocks, the count-once answer, handed
over for free — **and it still does not give `r = 1/2`**, because a count is
not a weight. Even granting the campaign its desired count, the count→weight
bridge (the equipartition/energy law) is a separate residual, and the
section-tie note keeps the two explicitly independent
(`...BEREZIN_COUNT_BINARY...2026-07-17.md:319-323`):

> > The stage-selection residual and the equipartition-granularity residual
> > are independent. One may specify when K-reality acts without choosing
> > an energy law, or impose one of the two energy laws without deriving
> > when the physical action imposes K-reality.

### 4.5 Also relevant: CAR itself is supplied on this surface

`docs/FREE_STAGGERED_POLE_RESIDUE_DIRAC_CARRIER_CAR_RELABELING_BOUNDED_THEOREM_NOTE_2026-07-17.md:36-38`:

> That construction supplies the *given-CAR* finite mode algebra used by the
> downstream bounded runner. It does not assert that the four framework axioms
> select CAR statistics.

So "build the CAR algebra natively" starts from a structure the framework does
not select. That is a further supplied input, not a wall by itself, but it means
the route has at least three supplied premises before it reaches the count:
CAR statistics, the polarization, and ORBIT-INDEXING.

**Answer to (c):** Yes, and more than once. The mode/generator count was
computed for **both** horns on **this exact lattice-delivered carrier** by
`scripts/kcpt_coupling_triple_berezin_count_binary_measure_collapse_2026_07_17.py`
(2026-07-17, PASS=121): 6 generators → `det3 = lam_0|lam_1|^2`, 12 generators →
`det3^2 = lam_0^2|lam_1|^4`. It did not settle the binary for three landed
reasons: the slot↦generator bridge is declared bookkeeping with no framework
clause behind it; the horn difference is exact-computed *r*-neutral; and the
generic route "Berezin power ⇒ count" was pruned by name on 2026-06-02, with a
consolidation showing that even the correct count (`K0 = Z^2`) does not select
the weighting.

---

## 5. (d) VERDICT

**Wave 1 as specified is DEAD ON ARRIVAL. Do not run it.**

The single sentence that kills it, from
`docs/KCPT_COUPLING_TRIPLE_BEREZIN_COUNT_BINARY_MEASURE_COLLAPSE_BOUNDED_THEOREM_NOTE_2026-07-17.md:111-115`:

> **FLAG — declared reading, not an equivalence:** both sides of the translation
> are computed exactly (runner B2, B3), and the correspondence between the
> graining slot count and the generator count is declared bookkeeping; no
> framework clause identifies occupancy slots with Grassmann generators, and T3
> makes no equivalence claim.

and the one that makes even a successful Wave 1 worthless, from
`docs/KCPT_COUPLING_TRIPLE_TWO_PRESENTATION_DERIVABLE_CLASS_SPECTRAL_PAIRING_BOUNDED_THEOREM_NOTE_2026-07-16.md:186-190`:

> passing from `det3` to `|det3|^2` doubles the singlet exponent and the doublet
> exponent together, so every doublet-to-singlet power ratio is unchanged. The
> pairing statement is r-neutral (runner V3).

The five findings, ranked:

1. **The construction already exists and returned "neither horn forced"**
   (07-17, PASS=121, both horns computed exactly at witness `(3,1,1)`: 20 and
   400). Wave 1 would re-run a finished computation.
2. **The output is r-neutral.** `6 -> 12` generators is a global doubling;
   `r` is a ratio; doubling cannot move a ratio. Even a derived count would not
   derive `r`.
3. **The route is definitionally circular.** Counting modes of "the carrier's
   CAR algebra" returns 3 (one per channel). Returning 2 requires ORBIT-INDEXING,
   which is supplied and explicitly not derived from Record. The repo already
   calls the move "a category slip and ... **circular**".
4. **The generic route was pruned by name on 2026-06-02** ("Power is not
   count"), and the block-count consolidation shows that even handing the
   campaign its count (`K0(R[C_3]) = Z^2`) leaves `r` unfixed, because the
   count→weight step is an independent residual.
5. **The campaign's premise mis-states main.** CAMPAIGN.md asserts a four-way
   equivalence. Landed content denies two of the three joints: the
   slot↦generator leg is "declared bookkeeping, never an equivalence"
   (07-17 R5b), and the menu↦fork leg is "a missing binding theorem"
   (`...GRAIN_MENU...2026-07-16.md:405-408`: "it does not identify its abstract
   2-cell/3-cell menu arithmetic with the physical count-once/count-twice fork.
   The formation-gate relocation source says the latter identification is a
   missing binding theorem"). CAMPAIGN.md must be corrected before any further
   wave, or every downstream wave inherits a false premise.

**Recommendation.** Do not build the CAR/Berezin construction. Two honest
options:

- **(A) Stop and ship the negative.** The publishable content is the
  non-equivalence itself: *the determinant-power/generator-count horn is
  r-neutral, so it is not the Koide binary; the r-moving binary is menu
  cardinality, and the two are joined only by an underived bridge.* Parts of
  this are landed (07-16 T4.1, 07-17 T2.3); the *consequence* — that the
  campaign-style bundling of the four framings is invalid — appears nowhere I
  found. That is a short note, not a construction wave, and it would correct a
  framing error that has been propagating since at least 07-04.
- **(B) Retarget at the actual open door.** The obligation's criterion is
  ordered: derive the physical matter action *and its measure* first. The
  06-08 no-go names the live sub-question precisely (`:96-99`):

  > The decisive open sub-question (the AC_φλ staggered-Dirac corner realization):
  > does the actual matter action deliver a *first-order* `det D` (Pfaffian/index,
  > count-once) or the *second-order* modulus (`det D†D`, rank-2, count-twice)?

  That is a question about the **order of the action in the field**, not about
  mode counting, and it is not foreclosed. But note it is currently leaning the
  wrong way: `docs/KOIDE_KAHLER_DIRAC_REALIZATION_GIVES_R_ONE_INDEX_ROUTE_CLOSED_BOUNDED_NO_GO_NOTE_2026-06-08.md`
  finds the explicit Kähler-Dirac realization gives `det D = |det M|^2 -> r = 1`.

---

## 6. What is honestly NOT foreclosed

Stating this so the negative is not oversold.

- **No universal negative exists.** `...STATIC_READOUT_NO_GO..._2026-06-08.md:146-147`:
  "This gate does **not** certify a universal negative against dynamical,
  off-circulant, or future first-order/index constructions." Its N7 steelman
  (`:187-190`) explicitly preserves "a future off-circulant or first-order
  Pfaffian/index construction [that] could select a one-complex-slot readout
  before the second-order modulus forms."
- **The 07-04 no-go's CAR/action door is genuinely open** (§2). It is a door to
  an *action* theorem, and it is symmetric between the horns.
- **`r = 1/2` is not forbidden.** `...STATIC_READOUT_NO_GO...:107-109`:
  "`r=1/2` is **not forbidden** — it is the un-forced one-complex-slot readout —
  but it is measure-neutral to every tested static framework structure."
- **The 07-17 note's own N6 keeps three live paths**: nonlinear/nilpotent-shifted
  changes of variables (untested), coupling-dependent substitutions as a
  structured conversion mechanism (conversion computed), and a
  record-content/occupancy-law theorem. None is the campaign's mode count.

What is foreclosed is specifically: *deciding the binary by counting the complex
modes of the corner carrier's coherent-state Berezin representation.*

---

## 7. Uncertainties and flags

1. **FLAG — grade.** Only `acphilambda_fermionic_realification_pfaffian_power_identity_narrow_theorem_note_2026-07-12`
   is `retained | audited_clean`. The 07-17 Berezin-count note, the 07-16
   spectral-pairing note, the 06-08 static no-go, the 06-04 fork note and the
   06-02 find-J lane are all `unaudited`. The kill rests mostly on landed
   unaudited content. I did not weaken the conclusion for this, because the
   decisive facts are *computed identities in shipped runners* and *the
   existence of a completed prior construction*, neither of which depends on
   grade — but a reviewer may legitimately discount §3.3, §4.2 and §4.4.
2. **FLAG — I did not execute any runner.** All PASS totals quoted
   (121, 32, 20, 46) are read from note text, not reproduced. I read the
   07-17 runner source directly for the B2/B3 mode-count logic and quote it
   verbatim; I did not run it.
3. **FLAG — §4.3's "stronger form" is mine, not landed.** The claim that the
   campaign's rule, applied literally with a one-mode-one-slot reading, lands on
   `r = 1` rather than `r = 1/2` is my arithmetic on top of the landed
   3-complex-mode fact. It depends on a mode↦slot reading that the repo
   explicitly does not fix. It should be treated as a sharpening to be tested,
   not as established content. If it survives scrutiny it strengthens the kill;
   if it fails, findings 1–4 stand unchanged.
4. **FLAG — one tension I could not fully resolve.** The obligation phrases the
   binary in determinant-power terms (`det_C` vs `|det_C|^2`,
   `AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md:21-24`), while
   the 07-16/07-17 notes prove that on the `C_3` corner carrier that same
   determinant-power step is *r*-neutral. Either the obligation's determinant
   gloss is not the r-moving binary, or the corner carrier is not the surface the
   obligation means. I lean to the first, and §4.3 argues for it, but I flag
   that I did not find a landed sentence resolving it. Whichever way it
   resolves, it does not rescue the mode-count route: on reading one the route
   computes an r-neutral quantity, on reading two it computes it on the wrong
   surface.
5. **Not searched exhaustively:** `docs/work_history/` (scanned only via
   full-repo grep hits) and the ~11.5k non-`docs/` tracked files beyond
   `scripts/`. I consider the docs/ + scripts/ coverage sufficient for a
   kill-check, but I did not read every hit.
