# WAVE 3 — adjudicating (P1) [positive spectral WEIGHT] against (P2) [positive SPECTRUM]

**Date:** 2026-07-24
**Role:** adjudicate the campaign's stated contradiction exactly; decide whether
(P1) and (P2) are about the same `r`; if different, compute the intersection.
**Status:** campaign working note. Not a repo science surface, not a claim, not
an audit input. No axiom, no primitive, no new repo vocabulary, no verdict set
or predicted, nothing committed, pushed, or PR'd. The only file I wrote is this
one.
**Base:** `origin/main` @ `5807ef17b7aa7074112fe1defdd683099967afda` (fetched at
session start; the campaign brief's `62826882ac` was superseded on the remote
during the fetch, so every quote below is taken from `5807ef17b7`).
**Runner (exact, sympy, no float is ever an input):**
`/private/tmp/claude-502/-Users-jonBridger-Toy-Physics--claude-worktrees-quirky-wiles-92e3b4/66008b76-8d97-42b5-b1e1-4e60c09bb2e9/scratchpad/wave3_reconcile.py`
**Runner close: `TOTAL: PASS=177 FAIL=0`**, output at `.../scratchpad/out3.txt`,
including **19 construction-mutation gate rows across 13 distinct probes**
(G1, G1b, G1c, G2×4, G3×3, G3b×2, G4, G5, G6, G6b, G6c, G7, G8), plus the
convention probes D1b/D1d/D1e and the independence witnesses F4a/F4b.
Every numbered sentence below is written FROM that
output. I did not trust the arithmetic of any prior wave or exercise sector: the
lattice heat-trace identity, the circulant algebra, the Gram, the isotype
weights, both `r`-formulas and both positivity claims are rebuilt from scratch
here, and where I reproduce a prior number I say so.

---

## 0. Framework refresher — surfaces actually read before concluding

1. `docs/audit/data/axiom_premise_nodes.json` in full — all four `canonical_ids`
   and every node `note`. Load-bearing for this report: `:25` states Record
   "still supplies no context-selection rule, formation rule (which admissible
   possibility a new record locks, at which site, **with what weight**, or at
   what rate), **weighting, normalization**, probability, … **K/CPT structure,
   central-sector** decomposition".
2. `docs/MINIMAL_AXIOMS_2026-06-29.md` in full (Lattice / Qubit / Admissibility /
   Record, the Qualification, the 2026-06-05 relation section, the open-gate
   list). Load-bearing: `:70-72` (the exact Record readout clause — additivity
   over disjoint records, `I(empty)=0`, nothing else); `:156-173` "Open Gates
   Outside The Axioms", which places **Born weights, probability rules,
   normalization, context selection** (`:164-167`) and **source/action and
   physical-observable identification** (`:170`) outside axiom content;
   `:97-101` ("no admission class exists").
3. `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` in full — rules 1–6
   and the three approved primitives. Rule 5 names *weighting rule*,
   *normalization rule*, *probability rule* as things a primitive never grants.
4. Source notes of every primitive I could have invoked:
   `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md` and
   `docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md` — **not invoked** (`r`
   and `Q` are dimensionless and static); `docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`
   — **invoked once, minimally**, for the single realized-state fact used in §4
   ("at least two charged leptons have nonzero mass"), which under `:43-45` is
   *registered data*, not derivation output. I record that explicitly rather
   than laundering it.
5. Lane surfaces read in the load-bearing part:
   `docs/FLAVOR_DOUBLET_METRIC_DEFAULT_IS_DETR_2026-06-02.md`,
   `docs/FLAVOR_R_HALF_IS_A_STATIONARY_POINT_NOT_FORCED_2026-06-02.md`,
   `docs/GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05.md`,
   `docs/CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md`,
   `docs/CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md`,
   `docs/ACPHILAMBDA_AMBIENT_EQUIVARIANT_HEAT_TRACE_FACE_2026-07-02.md`,
   `docs/FLAVOR_GAUGE_REPRESENTATION_CHANNEL_CANNOT_SOURCE_THE_SECTOR_R_SPREAD_NARROW_NO_GO_NOTE_2026-06-15.md`,
   plus `CAMPAIGN.md`, `ex3_literature_templates.md`, `wave2_defend_ex2.md`,
   `wave2_breach_target.md`.

**Live ledger statuses, read from the tracked shards under
`docs/audit/data/ledger/**` (never from note prose):**

| claim id | effective_status | audit_status |
|---|---|---|
| `flavor_doublet_metric_default_is_detr_2026-06-02` | **retained_bounded** | **audited_clean** |
| `flavor_r_half_is_a_stationary_point_not_forced_2026-06-02` | **retained_bounded** | **audited_clean** |
| `acphilambda_ambient_equivariant_heat_trace_face_2026-07-02` | unaudited | unaudited |
| `generation_weight_dial_structure_2026-06-05` | unaudited | unaudited |
| `charged_lepton_koide_value_full_chain_of_custody_2026-06-02` | unaudited | unaudited |
| `charged_lepton_value_reduces_to_one_counting_bit_synthesis_note_2026-06-05` | meta | unaudited |
| `koide_frobenius_isotype_split_uniqueness_note_2026-04-21` | unaudited | unaudited |
| `record_generation_readout_two_sectors_2026-06-05` | unaudited | unaudited |
| `flavor_gauge_representation_channel_cannot_source_the_sector_r_spread_…_2026-06-15` | unaudited | unaudited |

Exactly two of the nine are retained-grade, and both are ones I lean on for the
*definition* of the objects (never for a status inference). Everything else is
rebuilt natively. Per the brief I take no prose status label in this lane at
face value: the synthesis note calls
`koide_frobenius_isotype_split_uniqueness` "**retained_no_go**"
(`CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md:72`)
while the shard reads `unaudited`; I rely on that note for nothing but its
verbatim horn table.

---

## 1. Headline — the decision, in five sentences

1. **(P2) is correct and elementary.** It is Maclaurin/Newton on the nonnegative
   orthant: `e_2 = 3(a^2 - |b|^2)`, and two strictly positive eigenvalues force
   `e_2 > 0`, hence `r < 1` strictly (gates A4b, B1f, B1g). It cannot fail.
2. **(P1) is arithmetically correct but its identification with `r` is wrong**,
   and I locate the failing step exactly: `ex3_literature_templates.md:395-397`
   reads an **operator** matrix as a **form** matrix, dropping the Gram factors
   `(3, 6)` of the circulant coefficient surface. That dropped factor is exactly
   **2**, and 2 *is* the counting bit the campaign is trying to derive.
3. **As stated, the two claims are about the same `r` and are jointly
   unsatisfiable** (`{r>1} ∩ {r<1} = ∅`, gate F1b). Since (P2) cannot fail,
   that empty intersection is a *reductio against (P1)*, not a no-go against
   both horns.
4. **Corrected, they are about different objects and both survive**, and they
   squeeze from opposite sides exactly as the supervisor predicted: weight
   positivity gives `gamma ≥ 1/2` (a **lower** bound on the metric factor, whose
   extreme point is the landed HS/Koide point), spectrum positivity gives
   `gamma·nu < 1` (an **upper** bound on the product).
5. **The intersection is non-empty, and it decides the campaign's binary
   against count-twice.** `nu = 2` is admissible only for `F/S < 0`, which the
   positive-weight class forbids; `nu = 1` is admissible exactly on `F/S ∈ [0, 1/4)`,
   giving `r ∈ [1/2, 1)` with the Koide value `r = 1/2` as the **closed lower
   endpoint**, attained exactly at `F = 0`. The sign of EX3's obstruction is
   inverted: positivity falls on the **count-twice** horn, not on Koide.

---

## 2. (a) The two objects, in one common notation

### 2.0 Common notation (everything below is in these symbols)

Built natively in Block A of the runner, not cited:

```text
C          3x3 cyclic shift, C^3 = I, C != I                                (A1)
W          := Herm(circ_3) = { H = aI + bC + conj(b)C^2 : a in R, b in C },  dim_R W = 3
(a, Re b, Im b)      the COEFFICIENT coordinates on W
lam_k = a + 2 Re(b w^k),  k = 0,1,2      the EIGEN-SLOT coordinates      (A3, A3b)
r     := |b|^2 / a^2
Q     := Tr(H^2)/(Tr H)^2 = 1/3 + (2/3) r                                  (A5a)
e_1 = 3a,   e_2 = 3(a^2 - |b|^2),   e_3 = a^3 + b^3 + conj(b)^3 - 3a|b|^2  (A4a-A4d)
```

The `C_3` action that actually moves anything is conjugation by the clock
`D = diag(1, w, w^2)`: `a -> a`, `b -> w b` (A7a); `Ad_C` is trivial on
circulants (A7b, a mutation probe of EX1's mis-labelling). The carrier splits
canonically into `W_0 = R·I` (real-dim 1) and `W_1 = {a = 0}` (real-dim 2), and
the **Hilbert–Schmidt Gram** on the coefficient coordinates is

```text
||P_0 H||_HS^2 = 3 a^2        ||P_1 H||_HS^2 = 6 |b|^2        Gram = diag(3,6,6)   (A6, A7d, A7e)
```

reproducing verbatim the **retained_bounded / audited_clean** statement at
`FLAVOR_DOUBLET_METRIC_DEFAULT_IS_DETR_2026-06-02.md:16-19`.

The campaign's factorization, restated in these symbols and re-derived (D2a–D2f):

```text
gamma := g_0/g_1     the METRIC factor: the ratio of the two isotype block weights
                     of an invariant form written on (a, Re b, Im b), i.e.
                     E_0 = g_0 a^2  and  E_1 = g_1 |b|^2
nu    := w_1/w_0     the MODE-COUNT factor of the sector-balance rule
r     = gamma * nu
```

with the two named horns being `nu = 1` (count-once / `det_C` / equal power per
**block**) and `nu = 2` (count-twice / `det_R` / equal power per **real mode**):

```text
det_C :  g_0 a^2 = g_1 |b|^2                      =>  r = gamma          (D2a)
det_R :  g_0 a^2 = g_1 (Re b)^2 = g_1 (Im b)^2    =>  r = 2 gamma        (D2b)
landed HS point diag(3,6,6)  ->  (det_C, det_R) = (1/2, 1)               (D2c)
"flat point"    diag(1,1,1)  ->  (det_C, det_R) = (1,   2)               (D2d)
```

`D2c` reproduces `FLAVOR_DOUBLET_METRIC_DEFAULT_IS_DETR_2026-06-02.md:35-39`
verbatim, and `D2f` reproduces the landed dial `r(s) = 2^(s-1)` with `nu = 2^s`
(`GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05.md:81,86-91`).

### 2.1 (P2) — positivity of the SPECTRUM

| | |
|---|---|
| **object required positive** | the **spectrum** `(lam_0, lam_1, lam_2)` of the Hermitian element `H` itself — equivalently `H ⪰ 0`. It is a property of *one element*, the realized mass-root operator, not of any measure. |
| **space it lives on** | the **3-dimensional carrier** `W = Herm(circ_3)`; the positivity condition is a closed convex cone inside `W`. |
| **how `r` is read off** | purely algebraically from the element's own coefficients: `r = |b|^2/a^2 = 1 - 3 e_2/e_1^2` (B1b). No weight, no balance rule, no mode count is used. `r` is an **output** of the realized element. |
| **what it says** | `e_2 - lam_0 lam_1 = lam_2(lam_0 + lam_1) ≥ 0` on the nonneg orthant (B1f), so two strictly positive eigenvalues give `e_2 ≥ lam_0 lam_1 > 0`, hence **`r < 1` strictly** (B1g). Conversely `e_2 = 0` with `lam ≥ 0` leaves at most one nonzero eigenvalue, and `e_1 = 3a` then forces the ray `(3a, 0, 0)` (B1h, B2b). |
| **exact witnesses (re-derived, not taken from wave 2)** | `(a,b) = (1, 1/2)` → spectrum `(2, 1/2, 1/2)`, `r = 1/4` (B3a); `Gamma_{1,3}` → `(a,b) = (1, 3/2)` → spectrum `(4, -1/2, -1/2)`, `r = 9/4` (B3b). Wave 2's witness reproduces exactly. |
| **sharp form** | writing `b = |b| e^{i theta}`: at `r = 1` the normalized determinant is exactly `2 cos(3 theta) - 2 ≤ 0` for **every** phase (B2d), so a nonneg spectrum forces `det = 0`, i.e. `cos 3theta = 1`, i.e. the degenerate ray (B2e). `r = 1/2` is **interior**: `(a,|b|) = (1, 1/sqrt 2)`, `theta = 0` gives `(1+sqrt2, 1-sqrt2/2, 1-sqrt2/2)`, all `> 0` (B3d, B3e). |

This reproduces landed content — `CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md:41`
(L8: "at `r=1` positivity forces … the boundary spectrum `[0,0,3a]`") and
`FLAVOR_R_HALF_IS_A_STATIONARY_POINT_NOT_FORCED_2026-06-02.md:31`
("`r=1` | maximal hierarchy, two massless") — by an independent route.

### 2.2 (P1) — positivity of the WEIGHT

| | |
|---|---|
| **object required positive** | a **weight** `rho`: a self-adjoint operator/kernel on the ambient lattice function space, required to be a *nonnegative spectral function of the Laplacian*, `rho = f(Delta)` with `f ≥ 0` (equivalently: an entrywise-nonnegative covariant kernel — the Perron–Frobenius class). The heat semigroup `rho = e^{-t Delta}` is the instance EX3 uses. |
| **space it lives on** | the **`N^3`-dimensional ambient space** `l^2(Z_N^3)`, with `Delta = 6I - A` and the proper cubic coordinate cycle `R(x_1,x_2,x_3) = (x_3,x_1,x_2)`. For `N = 3` that is dimension **27**, versus dimension **3** for (P2)'s object (F4c). |
| **how `r` is read off** | in **three** steps, and the third is where the campaign's residual hides: (i) isotype weights `w_pi = Tr(P_pi rho)`; (ii) **transport** to the 3-dim carrier as an invariant form; (iii) impose the sector-balance rule with a mode count. `r` is an **input-side** object: a property of a measure, not of a realized element. |
| **what it says (correctly)** | `0 < F < S` for the heat semigroup, hence `w_triv > w_nontriv` strictly. |

The lattice identity is **rebuilt, not cited**. Runner Block C constructs
`Z_N^3` site-by-site for `N = 2, 3`, forms `A`, `Delta = 6I - A` and the
permutation matrix of `R`, and certifies exactly

```text
C1c  fixed momenta are exactly the [111] diagonal, count N
C2   Tr(Delta^p R^j) = sum over the diagonal momenta of dhat^p,  p = 0..4, j = 1,2
C3   j = 0 gives the FULL momentum sum, not the diagonal one
```

Matching the moments `p = 0..4` on a finite spectrum pins `Tr(f(Delta)R^j)` for
**every** `f`, so C2 re-derives the displayed identity of
`ACPHILAMBDA_AMBIENT_EQUIVARIANT_HEAT_TRACE_FACE_2026-07-02.md:14-30` rather
than checking one function. C3 is the reason `F` is a *proper* sub-object of
`S`. With `S(t) = Tr(e^{-tDelta})`, `F(t) = Tr(e^{-tDelta}R)`:

```text
C4b  S - F is a sum of N^3 - N strictly positive exponentials  =>  0 < F < S   (t>0, N>1)
C4c  x := F/S -> 1/N^2 as t -> 0        C4d  x -> 1 as t -> oo
C5a  w_triv    = (S + 2F)/3             C5b  w_om = w_ombar = (S - F)/3
```

All of EX3 §4.1–§4.2 reproduces. **This part of EX3 is right and I confirm it.**

### 2.3 The disputed step, stated precisely

`ex3_literature_templates.md:395-397` writes:

```text
:395  The induced `C_3`-invariant positive form on the carrier is
:396  `G(t) = w_triv P_triv + w_nontriv P_doublet`, i.e. the cone point
:397  `diag(g_0, g_1, g_1)` with `g_0 = w_triv`, `g_1 = w_nontriv` (per real doublet direction).
:401  r(t) = g_0/g_1 = (S + 2F)/(S - F)
```

`G = w_0 P_0 + w_1 P_1` is an **operator**; `diag(g_0, g_1, g_1)` in the
campaign's usage is a **form** on the coefficient surface — that is exactly what
makes `diag(3,6,6)` "the HS point" and `diag(1,1,1)` "the flat point". Turning
an operator into a form requires the reference metric, and on a space of
matrices that is HS. Doing it exactly (D1a–D1c):

```text
G(H,H) = w_0 ||P_0 H||_HS^2 + w_1 ||P_1 H||_HS^2 = 3 w_0 a^2 + 6 w_1 |b|^2
=>  (g_0, g_1) = (3 w_0, 6 w_1)     =>   gamma = g_0/g_1 = w_0 / (2 w_1)
```

The consistency check that settles it: **the unweighted case `w_0 = w_1` must
reproduce the landed metric.** It does — `diag(3·1, 6·1, 6·1) = diag(3,6,6)`
(D1b). Under EX3's reading the unweighted case would be `diag(1,1,1)`, the flat
point, i.e. `r = 1` — the count-twice horn **declared by fiat** (G1c). Worse,
under EX3's reading the landed retained metric `diag(3,6,6)` corresponds to
`w_0/w_1 = 1/2 < 1`, which **EX3's own theorem forbids**: the obstruction, read
that way, excludes a `retained_bounded / audited_clean` surface (G1b). So the
reading is not merely a labelling choice; it is refuted by a retained surface.

**The obvious reviewer challenge, closed.** One might answer "read `g_1` as the
weight per real doublet direction in an *orthonormal adapted frame*, and no Gram
factor appears". It does appear, because the flat metric on the eigen-slot
(mass-root) coordinates **is** the HS metric on `W`:
`sum_k lam_k^2 = Tr(H^2) = 3a^2 + 6|b|^2` (D1d). Transporting through the
orthonormal adapted frame of that flat metric therefore yields the *same*
dictionary `gamma = w_0/(2 w_1)`. The only reference metric that yields
`gamma = w_0/w_1` is the one declaring the coefficient frame `(a, Re b, Im b)`
orthonormal — i.e. declaring `diag(1,1,1)` to be the metric (D1e), which is the
flat point, which is the count-twice horn. There is no third option: every route
to EX3's formula passes through the horn it is trying to adjudicate.

Consequently, in the common notation:

```text
x := F/S
gamma(x)          = (1 + 2x) / (2(1 - x))     the METRIC factor              (D3a)
r_countonce(x)    = gamma(x)                   = (S+2F)/(2(S-F))             (D3b)
r_counttwice(x)   = 2 gamma(x)                 = (S+2F)/(S-F)   <- EX3's formula (D3c)
gamma'(x) = 3/(2(1-x)^2) > 0                   strictly increasing           (D3d)
gamma(0)   = 1/2 exactly  (the LANDED HS point, = the Koide metric value)    (D3e)
gamma(1/4) = 1   exactly  (the flat point) -- at a POSITIVE x                (D3f)
```

**EX3 computed `2·gamma`, i.e. `r` in the count-twice reading.** Gate D4z
reproduces EX3's own quoted number: at `N = 12`, `t = 10^-6`,
`2 gamma = 1.02097902098` (EX3 quotes `1.0209790` at `ex3:423`) — while the
metric factor is `gamma = 0.510489510490`, i.e. **within 2% of the Koide point,
not 2% above the flat point**. Gates D4 give the exact family at `N = 3, 12` and
`t = 10^-3, 1/2, 3`.

Two derived corrections to EX3's own text, both gated:

- `ex3:410` calls the `t→0, N→∞` limit "the FLAT point". It is the **HS point**:
  `gamma → 1/2` (D3e, D4 rows), i.e. the ultra-local infinite-volume equivariant
  weight converges onto the retained metric `diag(3,6,6)`.
- `ex3:417-418`'s breach numbers are the count-twice images. Correctly:
  `gamma = 1/2 ⟺ x = 0` (D3h), `gamma = 1 ⟺ x = 1/4` (D3f). EX3's `x = -1/5`
  is reproduced exactly (D3g) but it is the value of `x` at which the
  *count-twice* reading hits `1/2` — i.e. it is the image of `r = 1/2` under a
  map that has already set the bit.

> **Convergence note.** After deriving the above independently I read
> `wave2_breach_target.md:78-88, 204-245`, which reaches the same correction
> (the dropped `(3,6)` Gram, the factor 2, the HS-not-flat limit) by the same
> route. I record this as convergent confirmation, not as my source; both
> derivations are native and the gates here are my own. Wave 2's arithmetic
> reproduces on every point I re-checked, including its `x`-table
> (`wave2_breach_target.md:343-356`) and its finding that EX3's quoted
> `w_triv = 3S/5, w_nontriv = 6S/5` at `ex3:451` are the numerators `S+2F`,
> `S-F` and not the weights.

---

## 3. (b) THE DECISION

**As stated, (P1) and (P2) are about the same `r`, and they are jointly
unsatisfiable.** (P1) says `r > 1` strictly for every `t > 0, N > 1`
(`ex3:409`); (P2) says `r < 1` strictly whenever two eigenvalues are positive;
`{r>1} ∩ {r<1} = ∅` (F1b). One of them is therefore wrong.

**(P1) is the wrong one.** (P2) is Maclaurin/Newton on the nonneg orthant with
no modelling content at all — it is a two-line consequence of `e_2 ≥ lam_0 lam_1`
(B1f) — while (P1) contains three modelling steps between a lattice trace and a
mass ratio. The failing step is the third one, and it is a single identifiable
line:

> **`ex3_literature_templates.md:395-397`: the isotypic weight operator
> `G = w_triv P_triv + w_nontriv P_doublet` is read as the cone point
> `diag(g_0,g_1,g_1)` on the circulant coefficient surface. It is not. The
> coefficient surface carries the Gram `diag(3,6,6)`, so the induced form is
> `diag(3w_triv, 6w_nontriv, 6w_nontriv)` and `gamma = w_triv/(2 w_nontriv)`.**

The dropped factor is exactly 2 (G1: a single mutation — deleting the `(3,6)`
Gram — reproduces EX3's formula verbatim), and 2 is precisely the count-once /
count-twice factor `nu` (D2e). So (P1)'s conclusion is **circular**: it fixes
the counting bit to count-twice in step (ii) and then reports that count-once is
unreachable. This is the "convention-laundering false positive" failure mode the
campaign's own wall exercise warned about (`CAMPAIGN.md:203-209`), firing on the
exercise's own headline result.

**After the correction they are about different objects**, and the difference is
structural, not verbal:

| | (P1) | (P2) |
|---|---|---|
| positive object | a **weight/measure** `rho` (nonneg spectral function of `Delta`) | the **spectrum of one element** `H` |
| space | ambient `l^2(Z_N^3)`, dim `N^3` (27 at `N=3`) | the carrier `W`, dim 3 |
| role in the derivation | **input**: fixes the invariant form, hence `gamma` | **output**: constrains the realized `r = gamma·nu` |
| bound delivered | `gamma ≥ 1/2` (a LOWER bound on one FACTOR) | `r < 1` (an UPPER bound on the PRODUCT) |

Neither positivity implies the other, and I exhibit both independence
directions natively: a PF-positive weight coexists with a non-positive carrier
element (`rho = e^{-tDelta}` with `(a,b) = (1,3/2)`, spectrum `(4,-1/2,-1/2)`,
F4a); and a non-PF weight coexists with a positive carrier element
(`rho = P_doublet`, `F/S = -1/2`, with `(a,b) = (1,1/2)`, spectrum
`(2,1/2,1/2)`, F4b). They constrain different coordinates of one product.

**One further re-scoping of (P1), computed here.** `ex3:428-432` claims "no
positive functional of this class exists". That is false as stated for
"positive" = positive-semidefinite: `rho = P_doublet` is PSD and `R`-covariant
with `F/S = -1/2` (E3b), giving `gamma = 0` (E3c), and
`rho = alpha P_triv + beta P_doublet` attains EX3's `x = -1/5` exactly at
`beta = 11 alpha/4 > 0` on `Z_3^3` (E3d, E3e). What is true is the narrower
Perron–Frobenius statement:

> **Lemma (weight half-cone).** Let `rho` be `R`-covariant with `Tr rho > 0`
> and either (i) `rho = f(Delta)` with `f ≥ 0`, or (ii) `rho` PSD with
> entrywise-nonnegative kernel. Then `0 ≤ F ≤ S`, hence
> `gamma = (1+2x)/(2(1-x)) ≥ 1/2`, with equality iff `F = 0`.

For (i) `F` is a sub-sum of the nonneg spectral terms of `S`; for (ii)
`F = sum_x rho(x, R^{-1}x) ≥ 0` termwise, and `rho(x,y) ≤ sqrt(rho(x,x)rho(y,y))
≤ (rho(x,x)+rho(y,y))/2` with the diagonal `R`-invariant gives `F ≤ S`
(E4a, E4b, E4c). The bound is **attained**: at `N = 3` the spectral projector
`Pi_3` of `Delta` for eigenvalue 3 is PSD, `R`-covariant, has `S = 6`, `F = 0`
exactly (E2a–E2c), hence `gamma = 1/2` **exactly** with both isotype weights
strictly positive (E2d, E2e). So the Koide metric value is not merely a limit of
the positive class — it is its extreme point and it is realized in it. No
grading is needed and none is missing.

---

## 4. (c) THE INTERSECTION, computed exactly

With `x = F/S` and `nu` the mode-count ratio, the joint constraint set is

```text
r(x, nu) = nu (1 + 2x) / (2(1 - x))                                      (F2a)
(P1) PF class :  x in [0, 1)          i.e.  gamma >= 1/2
(P2)          :  r < 1                i.e.  nu < 2(1 - x)/(1 + 2x)       (F2b)
```

**It is NOT empty** (F2c), and it has a clean description:

```text
nu = 1  (COUNT-ONCE, det_C)  admissible  <=>  x < 1/4                    (F2d)
nu = 2  (COUNT-TWICE, det_R) admissible  <=>  x < 0                      (F2e)
```

Therefore, on the positive-weight class (`x ≥ 0`):

> **Theorem (intersection).**
> *Hypotheses.* (H1) the metric factor `gamma` is the isotype-weight ratio of a
> weight in the Perron–Frobenius class of §3 (in particular `gamma ≥ 1/2`, with
> the unweighted/landed HS point `gamma = 1/2` as extreme point); (H2) the
> sector-balance identity `r = gamma·nu` with the two named readings
> `nu ∈ {1, 2}`; (H3) the realized mass-root operator has nonnegative spectrum
> (the branch already built into the lane's readout identity
> `Q = Tr(H^2)/(Tr H)^2`); (H4) at least two charged leptons have nonzero mass
> (realized-state data, registered as such).
> *Conclusion.* `nu < 1/gamma ≤ 2`. Hence **`nu = 2` (count-twice, `det_R`,
> `r = 1`, `Q = 1`) is EXCLUDED**, and `nu = 1` (count-once, `det_C`) is
> admissible exactly for `x ∈ [0, 1/4)`, i.e.
> **`r ∈ [1/2, 1)`, with `r = 1/2` the closed lower endpoint, attained exactly
> at `F = 0`.**

Gates F2d–F2h, F3a–F3e, F5a–F5c. Sub-statements worth separating:

1. **Under the landed retained metric with no reweighting** (`gamma = 1/2`
   exactly, `FLAVOR_DOUBLET_METRIC_DEFAULT_IS_DETR_2026-06-02.md:16-19`) the
   binary gives `r ∈ {1/2, 1}` (F3b, F3c); (P2) removes `r = 1`; **`r = 1/2`
   and `Q = 2/3` remain, exactly** (F5a).
2. **Reweighting cannot rescue count-twice.** The only escape would be
   `gamma < 1/2`, and PF-positivity forbids it — `gamma` is strictly increasing
   in `x` and `x ≥ 0` (F3e, D3d). This is precisely where the two positivity
   conditions squeeze from opposite sides: (P1) closes the below-Koide region,
   (P2) closes the above-1 region, and `nu = 2` needs one of the two.
3. **The interior is NOT decided.** If the count is allowed to be the
   *continuous* dial `nu = 2^s`, `s ∈ [0,1]`
   (`GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05.md:91`), (P2) gives only
   `s < 1`, i.e. `r ∈ [1/2, 1)` (F5c). **Integrality of the count remains the
   undischarged premise**, exactly as the wall exercise flagged
   (`CAMPAIGN.md:245-247`). What the intersection delivers is: the *binary* is
   decided, the *dial* is not.
4. **The one escape from (2), closed.** `CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md:75`
   ties the count-twice horn to "the sign of `sqrt(m)` on the doublet", so the
   natural objection is that `det_R` lives on the signed branch where (P2) does
   not bite. On that branch the horn stops predicting its own value: at `r = 1`,
   `theta = pi/3` the spectrum is `(2,-1,2)` and, while
   `Tr(H^2)/(Tr H)^2 = 1` still, the **Koide ratio** `sum m/(sum sqrt m)^2` is
   `9/25`, not `1` (F5e, F5f). So the landed horn "count-twice ⟹ `Q = 1`"
   (`:69-70, 78-80`) is a nonneg-branch statement, and on the nonneg branch it
   forces two massless charged leptons. The horn is dead either way — on the
   branch it is stated on, by (P2); off that branch, by loss of its own
   prediction.

**Relation to the supervisor's recorded prediction.** Predicted: "non-empty and
NOT uniquely `1/2`", with the degenerate-spectrum exclusion of `r = 1` as the
most promising lead (`CAMPAIGN.md:378-381`). Confirmed on both counts, and
sharpened: the intersection is the half-open interval `[1/2, 1)`, so `1/2` is
not unique but it is the **extreme point**, and the `r = 1` exclusion is not a
lead but a completed exclusion of one horn under (H1)–(H4).

---

## 5. (d) Gating, including construction-mutation probes

`TOTAL: PASS=177 FAIL=0`. The probes that would catch a wrong coefficient in
either `r`-formula (campaign rule 3 — construction mutations, not assertion
checks):

```text
G1   MUT drop the (3,6) Gram  ->  gamma_mut = w0/w1 = 2 gamma  ->  reproduces the
     EX3 formula (S+2F)/(S-F) EXACTLY.        [this is the probe that FIRES on EX3]
G1b  MUT under that reading the landed diag(3,6,6) needs w0/w1 = 1/2 < 1, which EX3's
     own theorem forbids -- the mutation excludes a retained_bounded surface.
G1c  MUT operator-reading steelman: reading diag(w0,w1,w1) directly as the form makes
     the UNWEIGHTED weight the flat point r = 1, i.e. declares count-twice by fiat.
G2   MUT Gram (3,3)/(6,6)/(1,6)/(3,12) instead of (3,6): the HS point maps to
     gamma = 1, 1, 1/6, 1/4 -- only the true ratio 3/6 puts count-once at 1/2.
G3   MUT w_triv = (S + cF)/3 for c = 1, 3, 1/2 differs from Tr(P_triv rho)  (c = 2 only)
G3b  MUT w_om   = (S - dF)/3 for d = 2, 1/2 differs from Tr(P_om rho)       (d = 1 only)
G4   MUT Delta -> 6I - 2A: Tr(Delta'^2 R) = 324 matches the MUTATED diagonal
     dispersion (6-12cos)^2, not the true (6-6cos)^2 = 162  -> x is construction-sensitive
G5   MUT C_3 coordinate cycle -> C_4 face rotation: fixed-momentum count 4 -> 8 at N=4
G6   MUT Q = 1/3 + (1/3)r fails on the exact r = 1/2 witness
G6b  MUT e_2 = 3(a^2 - 2|b|^2) is not the charpoly coefficient
G6c  MUT r = 1 - 2 e_2/e_1^2 (that is Q, not r)
G7   MUT nu in {1,3}: horns become (1/2, 3/2), which does not reproduce the landed dial
G8   MUT balance r = gamma nu^2: the count-twice horn would sit at r = 2, not the landed 1
```

Non-vacuity of the identity re-derivations is gated separately: C2 matches the
trace identity on moments `p = 0..4` (so it pins `Tr(f(Delta)R^j)` for every
`f`, not one `f`), C3 shows `j = 0` gives the full sum, A3 verifies the
eigenvectors by exact residual rather than by `charpoly`-solve, and A4d checks
`e_1,e_2,e_3` against the characteristic polynomial.

---

## 6. Hypotheses, residuals, and what this is NOT

**Load-bearing hypotheses, named.** (H1) PF-class positivity of the weight —
*not* mere positive-semidefiniteness, which gives no bound at all (E3b, E3c).
(H2) the balance rule `r = gamma·nu` and the binary `nu ∈ {1,2}` — the balance
rule is the landed dial's own construction
(`GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05.md:68-71`, unaudited) and the
*binary* (integrality) is undischarged. (H3) the nonneg branch — it is already
baked into the lane's readout identity, but it is a hypothesis, not a theorem.
(H4) one qualitative realized-state fact.

**Scope caveat I must record, and it is the weakest joint in (P1).** The `R` of
the landed identity is the **spatial** proper cubic coordinate cycle
(`ACPHILAMBDA_AMBIENT_EQUIVARIANT_HEAT_TRACE_FACE_2026-07-02.md:15-18`) and its
`Delta` is declared "a calculational device, not a claimed dynamics" in that
same note; the generation `C_3` is the circulant clock on the flavor index. EX3
transfers ambient lattice isotypic weights onto the generation carrier without
naming a bridge, and I find none landed. So the heat weight is a legitimate
**instance** of a positive covariant weight, but its transfer is a modelling
step. This does **not** affect §3–§4: the weight half-cone lemma and the whole
intersection are carrier-independent statements about isotype weights, and
sub-statement (1) of §4 does not use the lattice at all — it uses only the
retained metric.

**What this is NOT.** It is not a derivation of `r = 1/2`. It is (i) a located
error in (P1), (ii) a corrected one-sided bound whose extreme point is the
Koide metric value, (iii) an exclusion of one of the two horns under named
hypotheses, and (iv) an exact admissible window `[1/2, 1)` for the residual. The
interior of that window is exactly the freedom the campaign's commutant theorem
and Record-additivity computation already established as unsourced; nothing here
sources it. I set and predict no audit status for anything.

---

## 7. Falsifiers this hands to the next wave

1. **Sector window.** The joint constraint predicts `r ∈ [1/2, 1)`, i.e.
   `Q ∈ [2/3, 1)`, for **every** sector built the same way. The registered
   values at `FLAVOR_GAUGE_REPRESENTATION_CHANNEL_CANNOT_SOURCE_THE_SECTOR_R_SPREAD_NARROW_NO_GO_NOTE_2026-06-15.md:31`
   ("charged leptons `r = 1/2`, down-quarks `r ≈ 0.597`, up-quarks `r ≈ 0.773`")
   all lie inside it, with the charged leptons exactly **at the closed lower
   endpoint** (H1, H2). Any sector found with `r < 1/2` refutes the PF-positivity
   half; any with `r ≥ 1` refutes the nonneg branch (H3). This is a
   dimensionless pass/fail target of the same shape as, but sharper than, the
   `F/S = -1/5` target it replaces — and unlike that one it is stated on the
   correct side of the counting bit.
2. **The one live escape from the exclusion of count-twice**, stated as a
   decidable obligation: *exhibit a landed reason the realized mass-root
   operator has a negative eigenvalue AND the Koide readout is still
   `Tr(H^2)/(Tr H)^2`.* Both halves are needed; F5e shows they are jointly
   inconsistent on the explicit signed witness.
3. **The remaining residual, sharpened**: not "which of two counts", but "is
   the count an integer at all". If integrality is discharged, (H1)–(H4) give
   `r = 1/2` exactly under the unreweighted landed metric (F5a). If it is not,
   the honest output stays `r ∈ [1/2, 1)`.

---

## 8. Repo-hygiene items observed (report only; I changed nothing)

- `ex3_literature_templates.md:395-397` (campaign exercise output, not a repo
  surface) carries the operator/form conflation described in §2.3, and
  `:410` mislabels the `t→0, N→∞` limit as the flat point when it is the HS
  point. Both are exercise-local; nothing on `origin/main` inherits them.
- `CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md:72`
  still calls `koide_frobenius_isotype_split_uniqueness` `retained_no_go`
  while the tracked shard reads `unaudited` — the same stale label Wave 1
  flagged. I relied on it for nothing.
- The campaign brief's base commit `62826882ac` is no longer the remote tip;
  `origin/main` is `5807ef17b7`. Future waves should re-anchor quotes.
