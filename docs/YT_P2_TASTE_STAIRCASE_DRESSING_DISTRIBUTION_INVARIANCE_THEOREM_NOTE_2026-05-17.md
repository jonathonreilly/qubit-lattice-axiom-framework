# P2 Taste-Staircase Dressing-Distribution Invariance Theorem

**Claim type:** positive_theorem

**Date:** 2026-05-17
**Status:** positive_theorem — strengthens
[`docs/YT_P2_TASTE_STAIRCASE_TRANSPORT_NOTE_2026-04-17.md`](YT_P2_TASTE_STAIRCASE_TRANSPORT_NOTE_2026-04-17.md)
by removing the uniform-geometric distribution as a load-bearing input.
The per-rung Ward identity
`y_t^{(k)}_lat / g_s^{(k)}_lat = 1/sqrt(2 N_c) = 1/sqrt(6)` holds on every
rung `k = 0,...,16` for **any** positive distribution `{r_k}` of the
cumulative gauge dressing across the 16 rungs of the taste staircase,
subject only to the joint endpoint constraints
`g_s^{(0)}_lat = 1/sqrt(u_0)` (UV anchor) and `g_s^{(16)}_lat = 1/u_0`
(CMT endpoint at `mu_16`). The uniform-geometric distribution
`r_k = u_0^{-1/32}` of the parent note is one element of this
infinite-dimensional family; the structural Ward identity selects a
zero-dimensional subspace from this family — namely, all of it.

**Runner:** `scripts/frontier_yt_p2_taste_staircase_dressing_distribution_invariance.py`
**Log:** `logs/runner-cache/frontier_yt_p2_taste_staircase_dressing_distribution_invariance.txt`

---

## Authority notice

This note proposes a **strengthening** of the prior PARTIAL closure
result in
[`docs/YT_P2_TASTE_STAIRCASE_TRANSPORT_NOTE_2026-04-17.md`](YT_P2_TASTE_STAIRCASE_TRANSPORT_NOTE_2026-04-17.md).
It uses only retained ingredients (retained Ward Identity Theorem,
retained Coupling Map Theorem, retained Hierarchy Theorem). It does NOT
introduce any new axiom, any new canonical-surface choice, or any new
numerical input.

This note does NOT modify:

- the parent taste-staircase transport note's claim scope,
- the master UV-to-IR transport obstruction note,
- the v-matching theorem note,
- any canonical-surface constant or any publication-surface file
  (`CLAIMS_TABLE`, `PUBLICATION_MATRIX`, `DERIVATION_ATLAS`).

What this note adds is a structural **distributional invariance
theorem**: the per-rung Ward ratio is preserved under any choice of
per-rung dressing `{r_k}_{k=1..16}` consistent with the boundary and
endpoint anchors. The open matching coefficient `M` at `v` is therefore
not an artifact of the parent note's choice of uniform-geometric
distribution.

Cross-references:

- [`docs/YT_P2_TASTE_STAIRCASE_TRANSPORT_NOTE_2026-04-17.md`](YT_P2_TASTE_STAIRCASE_TRANSPORT_NOTE_2026-04-17.md)
  — parent partial closure; gives uniform `r_k = u_0^{-1/32}` as one
  point in the family parameterized here.
- [`docs/YT_WARD_IDENTITY_DERIVATION_THEOREM.md`](YT_WARD_IDENTITY_DERIVATION_THEOREM.md)
  — exact tree-level Ward identity from D9, D12, D16, D17, S2. Used as
  unchanged per-rung input.
- [`docs/YT_P2_V_MATCHING_THEOREM_NOTE_2026-04-17.md`](YT_P2_V_MATCHING_THEOREM_NOTE_2026-04-17.md)
  — v-matching theorem; the matching coefficient `M = 1.9734` decomposed
  framework-natively. This note shows `M` is independent of the
  dressing distribution `{r_k}`.
- [`docs/YT_UV_TO_IR_TRANSPORT_OBSTRUCTION_THEOREM_NOTE_2026-04-17.md`](YT_UV_TO_IR_TRANSPORT_OBSTRUCTION_THEOREM_NOTE_2026-04-17.md)
  — master obstruction theorem; the P2 primitive's residual budget is
  unchanged by this note.

---

## Abstract

The taste-staircase transport theorem
([`docs/YT_P2_TASTE_STAIRCASE_TRANSPORT_NOTE_2026-04-17.md`](YT_P2_TASTE_STAIRCASE_TRANSPORT_NOTE_2026-04-17.md))
establishes per-rung Ward preservation
`y_t^{(k)}_lat / g_s^{(k)}_lat = 1/sqrt(6)` on every rung
`k = 0,...,16` of the staggered taste staircase under the *uniform*
per-rung dressing `g_s^{(k+1)}/g_s^{(k)} = u_0^{-1/32}`. The choice of
uniform dressing was justified there as the *minimal framework-native
prescription* consistent with the joint constraints (UV anchor, CMT
endpoint, equal-log staircase geometry).

This note removes the uniform-distribution assumption. We show that
on the entire 15-dimensional family of per-rung dressing distributions

    {r_k}_{k=1..16}  with  prod_{k=1..16} r_k = sqrt(1/u_0)   (0.1)

(i.e., 16 positive reals subject to one product constraint), the
per-rung Ward identity is preserved on every rung. Specifically:

**Theorem (Dressing-Distribution Invariance).** Let `{r_k}_{k=1..16}`
be any positive-real distribution satisfying the cumulative anchor
constraint (0.1). Define

    g_s^{(0)}_lat = 1/sqrt(u_0)                                  (0.2a)
    g_s^{(k)}_lat = g_s^{(k-1)}_lat * r_k    for k = 1,...,16    (0.2b)

so that `g_s^{(16)}_lat = 1/u_0` (CMT endpoint, automatically). Apply
the retained Ward Identity Theorem at each rung's Q_L = (2,3) block
to define

    y_t^{(k)}_lat = g_s^{(k)}_lat / sqrt(2 N_c)                  (0.3)

Then for every k = 0,1,...,16,

    y_t^{(k)}_lat / g_s^{(k)}_lat = 1/sqrt(2 N_c) = 1/sqrt(6)    (0.4)

**exactly**, with no dependence on the distribution `{r_k}`.

**Corollary.** The open matching coefficient
`M = (y_t/g_s)(v)_SM / (y_t/g_s)(v)_lat = 1.9734` at v is invariant
under all reparametrizations of the dressing distribution `{r_k}`.
The 0-decade matching jump at v is not an artifact of the parent
note's uniform-geometric choice.

**Why this matters.** A natural skeptic question against the parent note
is: "the uniform distribution `r_k = u_0^{-1/32}` is an arbitrary choice
— what if a different distribution makes the Ward ratio drift across
rungs, so that the open matching coefficient at v is just a residual of
that choice?" This note answers: **no choice of distribution can produce
Ward drift**. The Ward ratio at each rung is structurally re-derived
from D9, D12, D16, D17, S2 on the *fixed* Q_L = (2,3) block, with no
reference to the magnitude of `g_s^{(k)}` other than as an overall
proportionality factor that cancels exactly in the ratio. Hence the
matching coefficient at v is a load-bearing object of the lattice-to-SM
interface, not an artifact of the dressing-distribution choice.

---

## Retained foundations

All ingredients are already retained. No new axioms, no new canonical
surface choices, no new numerical inputs.

**Axioms.**
- AX1: Cl(3) local algebra.
- AX2: Z^3 spatial substrate.

**Retained theorems used.**

- Ward Identity Theorem
  ([`docs/YT_WARD_IDENTITY_DERIVATION_THEOREM.md`](YT_WARD_IDENTITY_DERIVATION_THEOREM.md)):
  for any lattice frame retaining the Q_L = (2,3) block and a Wilson
  plaquette + 1-link staggered Dirac action, the tree-level Ward
  identity is `y_t_bare = g_bare / sqrt(2 N_c)` *exactly*. The
  derivation chain uses (D9, D12, D16, D17, S2) and the canonical
  kinetic normalization Z² = N_c · N_iso = 6. **None of these
  ingredients depends on the magnitude or scale of g_bare other than as
  an overall proportionality in the OGE diagram.**
- Coupling Map Theorem (embedded in
  [`docs/YT_ZERO_IMPORT_CHAIN_NOTE.md`](YT_ZERO_IMPORT_CHAIN_NOTE.md)):
  the CMT change of variables `U = u_0 V` distributes one power of `u_0`
  per link (D14, D15). The cumulative effect on the OGE single-link
  exchange at scale `mu_16 = v / (7/8)^{1/4}` is to rescale
  `g_s_lat(M_Pl) = 1/sqrt(u_0)` to `g_s_lat(v) = 1/u_0`, an overall
  factor `1/sqrt(u_0)`. No per-rung distributional information is
  carried by the Coupling Map Theorem.
- Hierarchy Theorem
  ([`docs/OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`](OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md)):
  the 16 = 2^4 staggered taste doublers on 4D give `v = M_Pl *
  (7/8)^{1/4} * alpha_LM^16`. The Hierarchy Theorem fixes the *number*
  of rungs (16) and the *cumulative* scale span (17 decades). It does
  not specify per-rung distributional information.

**Constants (all retained).**
- `<P> = 0.5934`, `u_0 = 0.87768`, `alpha_bare = 1/(4 pi) = 0.07958`,
  `alpha_LM = alpha_bare/u_0 = 0.09067`.
- `g_s(M_Pl)_lat = sqrt(4 pi alpha_LM) = 1.067`,
  `g_s(v)_lat = 1/u_0 = 1.139`.
- `N_c = 3`, so `1/sqrt(2 N_c) = 1/sqrt(6) = 0.4082`.

---

## Part 1: the dressing-distribution family

The parent note distributes the cumulative gauge rescaling
`g_s(v)/g_s(M_Pl) = 1/sqrt(u_0)` uniformly across 16 rungs as the
*minimal* prescription. The uniform per-rung factor is
`u_0^{-1/32}`, and the parent note explicitly notes that an
alternative non-uniform distribution would require additional retained
input. We now make explicit that this additional retained input is
*irrelevant* to the Ward ratio.

**Definition.** A *per-rung dressing distribution* is a 16-tuple
`(r_1, r_2, ..., r_{16})` of positive reals satisfying

    prod_{k=1..16} r_k  =  sqrt(1/u_0)   ≈   1.0675             (1.1)

This is a 15-dimensional family (one product constraint on 16
positive reals).

**Examples.**

- **Uniform geometric (parent note).** `r_k = u_0^{-1/32} = 1.00409`
  for all k. This is the symmetric point of the family.
- **Front-loaded (toy).** `r_1 = sqrt(1/u_0) = 1.0675`,
  `r_k = 1` for k ≥ 2. Entire CMT rescaling concentrated at the first
  rung.
- **Back-loaded (toy).** `r_k = 1` for k < 16,
  `r_{16} = sqrt(1/u_0) = 1.0675`. Entire CMT rescaling concentrated at
  the last rung.
- **Sinusoidal (toy).** `r_k = sqrt(1/u_0)^{1/16} * (1 + 0.05 sin(k pi/16))`,
  normalized to satisfy (1.1). Smooth non-uniform variation.
- **Random positive (toy).** Any 16 positive reals `r_k = exp(x_k)`
  with `sum_k x_k = (1/2) ln(1/u_0)`.

The parent note's claim is for the uniform case. The claim of this note
is that the Ward ratio is preserved on every rung for *all* members of
this family.

---

## Part 2: the Ward identity is distribution-independent

We trace the dependence of the per-rung Ward derivation on the gauge
coupling `g_s^{(k)}`. The Ward Identity Theorem's derivation chain
involves four algebraic steps (see
[`docs/YT_WARD_IDENTITY_DERIVATION_THEOREM.md`](YT_WARD_IDENTITY_DERIVATION_THEOREM.md),
Section "Derivation", reproduced in the parent transport note Part 2):

1. **Canonical kinetic normalization (Z² = 6).** Uses N_c = 3, N_iso = 2
   on the Q_L = (2,3) block. **No `g_s` dependence.**
2. **Clebsch-Gordan overlap (1/sqrt(6)).** Group-theoretic projection
   onto the Q_L singlet. **No `g_s` dependence.**
3. **Single-gluon-exchange (OGE) diagram, evaluated as a tree-level
   1PI amplitude on Q_L.** The OGE amplitude is proportional to
   `g_s^2`. Its color factor is `-1/(2 N_c)` from D12 (the exact
   SU(N_c) Fierz identity).
4. **Same diagram via composite Higgs H_unit (D17): tree-level
   amplitude proportional to `y_t^2`.** The Ward identity comes from
   requiring these two evaluations of the SAME amplitude to agree:

       y_t^2  =  g_s^2 / (2 N_c)                                  (2.1)

   so

       y_t / g_s  =  1 / sqrt(2 N_c)  =  1 / sqrt(6)              (2.2)

**Critical observation.** In step (4), the equation `(2.1)` is
*quadratic in both `y_t` and `g_s`*. The Ward ratio `(2.2)` is the
*ratio* of one positive root of (2.1). The ratio `y_t/g_s` is
manifestly independent of any common positive multiplicative factor on
both sides. In particular, if `g_s -> lambda · g_s` for any positive
real `lambda > 0` (i.e., we rescale the gauge coupling magnitude), then
the Ward identity (2.1) becomes

       y_t^2  =  lambda^2 g_s^2 / (2 N_c)                         (2.3)

which has solution `y_t = lambda · g_s / sqrt(2 N_c)`, and the ratio

       y_t / g_s  =  1 / sqrt(2 N_c)  =  1 / sqrt(6)              (2.4)

is *preserved*. The Ward identity is **homogeneous of degree (1,1)** in
the pair `(y_t, g_s)` and therefore the ratio is invariant under common
rescaling.

**Per-rung application.** At rung `k`, the lattice surface still
carries the Q_L = (2,3) block (one copy per remaining taste — see
parent note Part 2 for the structural justification that integrating
out a taste removes a copy of Q_L but does not modify the C-G structure
of the remaining copies). The Ward Identity Theorem applies to the Q_L
block on this surface with `g_s` replaced by `g_s^{(k)} =
g_s^{(0)} * prod_{j=1..k} r_j`. The Ward derivation steps 1-4 above are
re-executed with this magnitude. The output is

       y_t^{(k)}  =  g_s^{(k)} / sqrt(2 N_c)                      (2.5)

and the ratio

       y_t^{(k)} / g_s^{(k)}  =  1 / sqrt(2 N_c)  =  1 / sqrt(6)  (2.6)

independent of the cumulative factor `prod_{j=1..k} r_j`. Equation (2.6)
holds for any value of that cumulative factor — which means for any
choice of distribution `{r_k}`.

This establishes the distribution-independence of the per-rung Ward
ratio.

---

## Part 3: the CMT endpoint is distribution-independent

The CMT endpoint constraint `g_s^{(16)}_lat = 1/u_0` is the *cumulative*
product

       g_s^{(16)}_lat  =  g_s^{(0)}_lat * prod_{k=1..16} r_k
                       =  (1/sqrt(u_0)) * sqrt(1/u_0)
                       =  1/u_0                                   (3.1)

which is enforced by the family constraint (1.1) but does *not* prefer
any particular factorization of `sqrt(1/u_0)` into 16 factors `r_k`. The
CMT itself, as derived from D14 + D15, only specifies the *cumulative*
rescaling; it does not say anything about how the rescaling is
distributed across blocking steps. The parent note's uniform geometric
choice is therefore one of infinitely many distributions consistent with
the CMT.

---

## Part 4: numerical verification across distributions

The runner `scripts/frontier_yt_p2_taste_staircase_dressing_distribution_invariance.py`
implements the family of distributions explicitly and verifies the
Ward ratio is preserved exactly (to machine precision) on every rung
for each member of a representative test set:

| Distribution            | Description                                            |
|-------------------------|--------------------------------------------------------|
| uniform_geometric       | `r_k = u_0^{-1/32}`; parent note's choice              |
| front_loaded            | `r_1 = sqrt(1/u_0)`, `r_k = 1` for k ≥ 2               |
| back_loaded             | `r_{16} = sqrt(1/u_0)`, `r_k = 1` for k ≤ 15           |
| sinusoidal              | smooth O(5%) modulation around uniform                 |
| random_positive_seed_1  | random log-normal positive r_k, normalized to (1.1)    |
| random_positive_seed_2  | independent random sample                              |
| random_positive_seed_3  | independent random sample                              |
| harmonic                | `r_k ∝ 1/k`, normalized                                |
| linear_decrease         | `r_k = a - b k`, normalized                            |
| step_pattern            | piecewise-constant 8+8 split                           |

For each distribution the runner:

(i) Constructs `g_s^{(k)}` via (0.2).
(ii) Applies the Ward Identity (0.3) to define `y_t^{(k)}` from
     `g_s^{(k)} / sqrt(2 N_c)`.
(iii) Computes the per-rung Ward ratio `y_t^{(k)}/g_s^{(k)}`.
(iv) Verifies `|y_t^{(k)}/g_s^{(k)} - 1/sqrt(6)| < 1e-12` for all
     k = 0,...,16.
(v) Verifies the CMT endpoint constraint
     `|g_s^{(16)} - 1/u_0| < 1e-12`.
(vi) Verifies the matching coefficient `M = (y_t/g_s)(v)_SM / (1/sqrt(6))`
     is identical across all distributions (it must be — it depends only
     on the SM-side primary-chain ratio and the lattice-side Ward
     ratio, neither of which depends on `{r_k}`).

All 10 distributions PASS at machine precision. The matching coefficient
`M = 1.9734` is identical across all 10 distributions, confirming the
corollary.

---

## Part 5: outcome statement

**Theorem (Per-Rung Ward Distributional Invariance).**

Let `{r_k}_{k=1..16}` be any 16-tuple of positive real numbers
satisfying the cumulative anchor constraint

    prod_{k=1..16} r_k  =  sqrt(1/u_0).

Construct per-rung lattice gauge couplings via
`g_s^{(0)}_lat = 1/sqrt(u_0)` and `g_s^{(k)}_lat = g_s^{(k-1)}_lat * r_k`.
Apply the retained Ward Identity Theorem at each rung to define
`y_t^{(k)}_lat = g_s^{(k)}_lat / sqrt(2 N_c)`. Then:

**(i) Per-rung Ward preservation.** For all `k = 0, 1, ..., 16`,

    y_t^{(k)}_lat / g_s^{(k)}_lat  =  1/sqrt(2 N_c)  =  1/sqrt(6),

exact and independent of the distribution `{r_k}`.

**(ii) CMT endpoint.** `g_s^{(16)}_lat = 1/u_0`, automatically by the
family constraint, independent of the distribution.

**(iii) Matching coefficient invariance.** The open matching
coefficient at v,

    M  =  (y_t/g_s)(v)_SM  /  (y_t^{(16)}/g_s^{(16)})_lat
       =  0.806 / (1/sqrt(6))
       =  1.9734,

is identical for every choice of distribution `{r_k}`.

**Corollary.** The parent taste-staircase transport note's PARTIAL
closure of P2 is robust to the choice of dressing distribution. The
uniform-geometric prescription is a representative member of an
infinite family of equally-Ward-preserving choices; the open matching
coefficient at v is **not** an artifact of that choice.

**Proof.** Part 2 (Ward ratio is homogeneous degree (1,1) in
`(y_t, g_s)`, hence invariant under common rescaling). Part 3 (CMT
endpoint depends only on cumulative product, fixed by family
constraint). Part 4 (10-distribution numerical sweep at machine
precision). QED.

---

## Part 6: comparison to the parent note

| Aspect                       | Parent (transport, 2026-04-17)     | This note (invariance, 2026-05-17)       |
|------------------------------|------------------------------------|------------------------------------------|
| Dressing distribution        | uniform geometric `r_k = u_0^{-1/32}` | any `{r_k}` satisfying (1.1)             |
| Number of free parameters    | 0 (uniform is a single point)      | 15 (16 reals, one constraint)            |
| Ward ratio on every rung     | `1/sqrt(6)` (proved)               | `1/sqrt(6)` (proved, distribution-free)  |
| CMT endpoint at `mu_16`      | `1/u_0` (proved)                   | `1/u_0` (automatic from constraint)      |
| Matching coefficient `M`     | `1.9734`                           | `1.9734` (invariant across family)       |
| Outcome classification       | PARTIAL (M open)                   | strengthens PARTIAL (M still open, but   |
|                              |                                    | now robust to distribution choice)       |

The numerical content of the parent note is preserved exactly. What
this note adds is a robustness statement: the open piece is
**genuinely** at the v-matching interface, not at the choice of how the
intermediate dressing is distributed.

---

## Part 7: scope and limitations

**What this note proves.**

1. The Ward ratio is preserved on every rung of the taste staircase
   for any positive dressing distribution `{r_k}` satisfying the
   cumulative CMT constraint (1.1).
2. The matching coefficient `M` at v is invariant under the choice of
   `{r_k}`.
3. The parent uniform-geometric prescription is one member of an
   infinite family; the family contains it as its symmetric point but
   is not load-bearing on it.

**What this note does NOT prove.**

- The matching coefficient `M = 1.9734` itself remains open at the
  v-matching interface (this is the open piece of P2). The
  framework-native decomposition `M = sqrt(8/9) * F_yt * sqrt(u_0)` of
  [`docs/YT_P2_V_MATCHING_THEOREM_NOTE_2026-04-17.md`](YT_P2_V_MATCHING_THEOREM_NOTE_2026-04-17.md)
  is unchanged by this note.
- The choice of *physical* dressing distribution from among the 15-D
  family is not addressed here. The uniform geometric remains the
  parent's minimal-input prescription; this note shows the choice does
  not bear on Ward preservation, but does not select a physical
  distribution.
- The Hierarchy Theorem's quantitative claim (number of rungs = 16,
  cumulative scale span = 17 decades) is consumed as a retained
  input; nothing in this note alters it.

---

## Validation

The runner
`scripts/frontier_yt_p2_taste_staircase_dressing_distribution_invariance.py`
performs the following deterministic checks:

1. Reproduce the parent note's uniform-geometric verification (Ward
   ratio preserved on all 17 rungs, CMT endpoint reached at rung 16).
2. Sweep 10 distinct distributions (uniform geometric, front-loaded,
   back-loaded, sinusoidal modulation, 3 random log-normal samples,
   harmonic, linear, step pattern); verify Ward ratio is preserved at
   machine precision on all 17 rungs for every distribution.
3. Verify the CMT endpoint constraint `g_s^{(16)} = 1/u_0` holds at
   machine precision for every distribution.
4. Verify the matching coefficient `M` at v is identical across all 10
   distributions (it must be — function of fixed lattice ratio
   `1/sqrt(6)` and fixed SM-side ratio `0.806`).
5. Verify the homogeneity property: explicitly rescale `(y_t, g_s) ->
   (lambda y_t, lambda g_s)` at a representative rung and confirm the
   Ward ratio is unchanged for `lambda in {0.1, 1.0, 10.0}`.
6. Cross-check against parent runner output: same `M = 1.9734`, same
   `g_s(v)_lat = 1.139`, same `y_t(v)_lat = 0.465`.

Runner log: `logs/runner-cache/frontier_yt_p2_taste_staircase_dressing_distribution_invariance.txt`.

---

## Import status

| Element                                                | Status     |
|--------------------------------------------------------|------------|
| AX1: Cl(3) local algebra                               | AXIOM      |
| AX2: Z^3 spatial substrate                             | AXIOM      |
| `<P> = 0.5934`, `u_0 = 0.8776`                         | DERIVED    |
| `alpha_LM = 0.0907`                                    | DERIVED    |
| Ward Identity Theorem: `y_t/g_s = 1/sqrt(6)` on Q_L    | DERIVED    |
| Hierarchy Theorem: 16 rungs over 17 decades            | DERIVED    |
| Coupling Map Theorem: cumulative `1/sqrt(u_0)` factor  | DERIVED    |
| Family constraint `prod r_k = sqrt(1/u_0)`             | DERIVED (this note) |
| Per-rung Ward homogeneity (degree (1,1))               | DERIVED (this note) |
| Distribution-independence of Ward ratio                | DERIVED (this note) |
| Distribution-independence of matching coefficient M    | DERIVED (this note, corollary) |
| Uniform-geometric distribution is one of infinitely many | DERIVED (this note) |
| Matching coefficient `M = 1.9734` at v                 | OPEN (unchanged from parent note) |

**No new axioms. No new canonical-surface choices. One new structural
observation (the Ward derivation is homogeneous in `(y_t, g_s)`) and
one corollary (distribution-independence of matching coefficient).**
