# WAVE 3 — attack on the `r = 1` degenerate-spectrum exclusion

Date: 2026-07-24. Base: `origin/main` fetched at session start, tip `5807ef17b7`.
Scope: campaign report only. No repo science surface created or edited, nothing
committed, pushed, or PR'd. No audit verdict set, predicted, or implied. No axiom,
no primitive, no new repo vocabulary proposed.

**Verification.** Every load-bearing step below was rebuilt natively and exactly in
sympy (exact rationals/radicals/symbols; no float is ever a proof input). Scratch
runner
`/private/tmp/claude-502/-Users-jonBridger-Toy-Physics--claude-worktrees-quirky-wiles-92e3b4/66008b76-8d97-42b5-b1e1-4e60c09bb2e9/scratchpad/wave3_degenerate_exclusion_probe.py`,
log `…/wave3_run.log` — **SCORECARD PASS=119 FAIL=0**, including **16
CONSTRUCTION-mutation probes** (M1, M1b, M2–M12, plus G4.11.p1/p3/p4). I did not
trust Wave 2's arithmetic; I rebuilt it from the shift matrix up and say below
exactly what reproduces and what does not.

---

## 0. Framework refresher — surfaces actually read before concluding

- `docs/MINIMAL_AXIOMS_2026-06-29.md` **in full** (Lattice / Qubit / Admissibility /
  Record; the Qualification `:76-84`; "Relation To The 2026-06-05 Record Wording"
  `:136-154`; "Open Gates Outside The Axioms" `:156-173`, which lists
  `source/action and physical-observable identification` at `:170`).
- `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` in full (rules 1–6; rule 5
  at `:13-16` names *weighting rule, normalization rule, readout bridge* as separate;
  the three approved primitives at `:21-46`).
- `docs/audit/data/axiom_premise_nodes.json` in full (all four `canonical_ids`; the
  `minimal_axioms` node `note` at `:25` excluding weighting, normalization, K/CPT
  structure and central-sector decomposition; `realized_state_primitive` at `:43-49`).
- Source notes of the primitives invoked: `docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`
  (invoked for the status of the mass data, §3.4; Informative State-Contingency
  Register `:71-74`, item 4 `:88-93`). `SCALE_REFERENCE_PRIMITIVE_NOTE.md` and
  `KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md` checked out of chain (`r` and `Q`
  are dimensionless and static).
- Lane surfaces: `KOIDE_EQUIPARTITION_ENDPOINT_REGISTRATION_ASYMMETRY_BOUNDED_THEOREM_NOTE_2026-07-12.md`
  (**in full** — this is the decisive one), `CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md`,
  `KOIDE_SIGNED_EIGENVALUE_VS_SINGULAR_VALUE_READOUT_NARROW_THEOREM_NOTE_2026-05-29.md`,
  `KOIDE_SIGNED_READOUT_IS_NOT_CHIRALITY_NARROW_NO_GO_NOTE_2026-06-04.md`,
  `GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05.md`,
  `FLAVOR_R_HALF_IS_A_STATIONARY_POINT_NOT_FORCED_2026-06-02.md`,
  `KOIDE_CLOSURE_ATLAS_ISSUES_FLAGGED.md`.
- Live sharded ledger `docs/audit/data/ledger/**` queried directly on `origin/main`
  for every surface cited (statuses tabulated in §6). Per the brief I lean on **no**
  prose status label.
- `CAMPAIGN.md`, the four Wave-2 reports, and exercise sectors EX1–EX6.

---

## 1. Bottom line — four verdicts

| task | verdict |
|---|---|
| **(a)** re-derive natively, verify the witness, confirm `(3a,0,0)` and nothing else | **REPRODUCES EXACTLY.** `e_2 = 3(a^2-|b|^2)` (G1.2), witness (G3.1–G3.2), and `r=1` + nonneg spectrum forces the phase set `theta in {0, 2pi/3, 4pi/3}` and spectrum exactly `(3a,0,0)` (G2.6–G2.9). Wave 2's arithmetic is **correct**. |
| **(b)** does the physics exclusion run? | **NOT AS FRAMEWORK CONTENT — but it survives in a sharper, reduced form.** The eigenvalues are **not** the masses: `m_k = lam_k^2` is a *declared, unadopted* modeling element. And the "positive spectrum" hypothesis is a *branch convention*, not a framework fact — on the sign-allowed branch `r = 1` hosts three distinct nonzero masses (G4.5). **However** I prove `B_plus` is not an extra import: it is **equivalent** to "the `r`-dial computes the physical Koide ratio" (G4.3b–G4.4). That reduces the exclusion to **one** unadopted element, and that element is itself forced up to scale by the same demand (G4.11). |
| **(c)** what stands between it and `r = 1/2` | **An open interval.** The admissible set becomes `0 < r < 1`. It kills `r = 3/2` and `r = 2`; it keeps `r = 1/2` **and** `r = 17/2 - 6 sqrt(2)`. On the landed dial it deletes the endpoint `s = 1` and leaves all of `s < 1`. It also does **not** exclude "count-twice": it excludes the *product* `r = 1`, and the count↔value dictionary runs through the metric factor Wave 2 already demoted. |
| **(d)** gating | 119/0 exact, 16 construction-mutation probes. |

### The two findings that matter most

**FINDING A — this is not a new result. It is a landed bounded theorem from
2026-07-12 that no wave and no exercise sector cited.**
`docs/KOIDE_EQUIPARTITION_ENDPOINT_REGISTRATION_ASYMMETRY_BOUNDED_THEOREM_NOTE_2026-07-12.md`
is titled, verbatim in its `:1` header, *"the `r = 1` Positive Branch Is Forced to
`(3a,0,0)`, While `r = 1/2` Has an Open Three-Distinct Positive Sector with
`Q = 2/3`; Allowing Signs Restores `r = 1` Non-Degeneracy but Unpins `Q`"*. Its T1
(`:191-194`), T2 (`:217-222`), T3 (`:254-259`) and T4 (`:315-323`) are Wave 2's
result plus the caveat Wave 2 dropped. A grep over every Wave-1/2 report and every
exercise sector returns **zero** citations of it. The lane's own `:41` L8 row in the
chain of custody has carried `[0,0,3a]` since 2026-06-02.

**FINDING B — the campaign's stated contradiction is not a contradiction, and the
resolution is sharp.** Imposing P2's `r < 1` on P1's own formula
`r = (1 + 2x)/(1 - x)`, `x := F/S`, forces **`x` in `(-1/2, 0)` exactly** (G5.i–G5.j).
P1's own breach value `x = -1/5` lies inside that window (G5.l). So P1 and P2 **agree**:
both demand a **graded / negative-`F` (supertrace)** equivariant weight, and `x = 0`
is precisely the `r = 1` boundary point (G5.k). The conflict existed only while P1's
`F > 0` positivity was retained.

---

## 2. (a) Native re-derivation — what reproduces, exactly

### 2.1 The carrier, from the shift matrix up

`C` = the `3x3` cyclic shift, `C^3 = I`, `C != I`, `C^T = C^2 = C^{-1}` (G0.1–G0.3).
`H = a I + b C + conj(b) C^2` with `a` real, `b = br + i bi` complex; `H` is Hermitian
and `[H, C] = 0` (G0.4–G0.5). The Fourier vectors `f_k = (1, w^k, w^{2k})` are exact
eigenvectors with **exactly zero** residual (G0.6.0–G0.6.2) and real eigenvalues
(G0.7).

**One convention correction, stated because it is easy to trip on.** With the
eigenvector `f_k = (1, w^k, w^{2k})` the eigenvalue is
`lam_k = a + 2|b| cos(theta - 2pi k/3)`, not `cos(theta + 2pi k/3)` (G0.8). The
corpus writes the `+` form. The two differ by `k -> -k`, i.e. by relabelling only,
and the **spectral multiset is identical** — verified at five exact phases
(G0.8m). Every statement below depends only on the multiset, so nothing is affected;
I record it so no downstream reader re-derives a phantom discrepancy.

### 2.2 The elementary symmetric functions

Rebuilt three independent ways (from the eigenvalues, from `Tr`/`det` of the matrix,
and from `(Tr^2 - Tr H^2)/2`), all agreeing exactly (G1.1–G1.7):

```text
e_1 = Tr H  = 3a                                                            (G1.1)
e_2         = 3(a^2 - |b|^2)                                                (G1.2)
e_3 = det H = a^3 + b^3 + conj(b)^3 - 3a|b|^2
            = a^3 + 2|b|^3 cos(3 theta) - 3 a |b|^2                         (G1.3, G1.8)
```

and with `r := |b|^2/a^2` (`a != 0`),

```text
e_2   = 3 a^2 (1 - r)        =>   sign(e_2) = sign(1 - r)                   (G1.9)
Q_H  := Tr(H^2)/(Tr H)^2 = 1/3 + (2/3) r     for ALL (a,b), all phases      (G1.10)
```

**Wave 2's `e_2 = 3(a^2 - |b|^2)` (its D5) is exactly right.** I found no arithmetic
error anywhere in the Wave-2 positivity block.

### 2.3 `r = 1` forces `(3a, 0, 0)` — and nothing else

Two independent routes, both exact.

*Route 1 (spectral, coordinate-free).* With all `lam_k >= 0`, `e_2` is a sum of three
nonnegative pairwise products (G2.1–G2.2). `e_2 = 0` therefore forces every product
to vanish, so **at most one** `lam_k` is nonzero — verified by exhaustive case split
over all eight vanishing patterns (G2.3–G2.4). Combined with `e_1 = 3a`, that one
equals `3a`: the spectrum is `(3a, 0, 0)` (G2.5). If all `lam_k > 0` strictly then
`e_2 > 0`, hence **`r < 1` strictly** (G2.10).

*Route 2 (circulant realizability — this is the "nothing else" half).* At `r = 1`
(`|b| = a`), `det H = 2 a^3 (cos 3theta - 1) <= 0` for `a > 0` (G2.6). A nonnegative
spectrum requires `det >= 0`, so `cos 3theta = 1`, whose solution set on `[0, 2pi)`
is **exactly** `{0, 2pi/3, 4pi/3}` (G2.7). At each of those three phases the spectrum
is exactly a permutation of `(3a, 0, 0)` (G2.8). At every other phase tested
(`pi/12, pi/6, pi/3, pi/2, pi`) the spectrum carries a **strictly negative**
eigenvalue (G2.9). So the answer to "and nothing else" is **yes**, and the solution
set is the three cyclic placements — a measure-zero point set in the phase.

I also confirmed the Newton/Descartes characterisation the argument implicitly uses:
for a real-rooted cubic, all `lam_k >= 0` **iff** `e_1, e_2, e_3 >= 0`, checked in
both directions on four exact `(a,b)` witnesses (G2.11).

### 2.4 The witness, verified

```text
(a,b) = (1, 1/2)   ->  spectrum exactly ( 2,  1/2,  1/2 )   r = 1/4,  e_2 = +9/4
Gamma_{1,3}        ->  (a,b) = (1, 3/2)
                   ->  spectrum exactly ( 4, -1/2, -1/2 )   r = 9/4,  e_2 = -15/4
```

(G3.1–G3.4). `Gamma = diag(1,3,3)` on `(a, Re b, Im b)` does commute with the clock
action `b -> w b` and with the K/CPT reflection `diag(1,1,-1)` (G3.5–G3.6). And the
**same ray crosses `r = 1` at `(a,b) = (1,1)`, where the spectrum is exactly
`(3, 0, 0)`** (G3.7) — the witness passes straight through the degenerate point.

---

## 3. (b) THE PHYSICS QUESTION — attacked, not defended

The task is: determine exactly what the object whose spectrum is `(3a,0,0)` **is**,
and whether its eigenvalues are the masses. I found four things, in order of how
badly they hurt the inference.

### 3.1 The object is the `C_3`-equivariant generation/mass operator; its eigenvalues are NOT the masses

`GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05.md:67` does call `Y = aI + bC + conj(b)C^2`
"the C_3-equivariant **mass operator** on the 3-generation carrier". But the corpus is
unanimous and explicit that its eigenvalues are **not** masses. The identification is

```text
B_map:   m_k = lam_k^2         (so lam_k is a SIGNED sqrt(m_k), not a mass)
```

and its status is declared, repeatedly, as **not supplied**:

- `KOIDE_EQUIPARTITION_ENDPOINT_REGISTRATION_ASYMMETRY_..._2026-07-12.md:361-363`
  registers `B_map` as **Residual Atom 1**: "*This note's own declared
  bridge/modeling element; unadopted and load-bearing for T2-T3*". `:353-357` says the
  R-D anatomy note "**does not carry** `m_k = lambda_k^2`, a per-member
  spectral-to-mass map, or the nonnegative-eigenvalue branch. `B_map`, `B_plus`, and
  the alternative `B_abs` are therefore this note's own explicitly unadopted modeling
  elements; they are **not laundered through R-D or Record**."
- `CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md:94`: "*The physical
  statement `m_k = λ_k²` additionally requires the unresolved P1/species/carrier
  bridge.*" Its `:39` (L6) says "*Neither identity assigns the eigenvalues to positive
  square-root masses*"; its `:41` (L8) tags the `[0,0,3a]` boundary "*algebraic
  boundary checked here; **no physical assignment***"; its `:43` (L10) "*no
  charged-lepton mass-square-root assignment is supplied*"; and its claim boundary
  `:9-11` states "*Identifying `Q_H` with the physical charged-lepton Koide ratio is
  not supplied by this row.*"
- `KOIDE_SIGNED_EIGENVALUE_VS_SINGULAR_VALUE_READOUT_..._2026-05-29.md:274-276`: "Does
  **not** identify `H = aI + bC + b̄C²` (or its eigenvalues with `√m_k`) as *the*
  charged-lepton mass operator".
- `MINIMAL_AXIOMS_2026-06-29.md:170` puts "source/action and **physical-observable
  identification**" explicitly outside axiom content.

**So the plain answer to the task's question is: they are neither the masses nor the
squared masses as a matter of framework content. They are abstract circulant spectral
values, and the mass reading is a declared bridge that no surface adopts.** Any
statement of the form "`(3a,0,0)` means two massless leptons" inherits that bridge.

### 3.2 The harder problem: `B_plus` is a *branch convention*, and the framework's own native class is the signed one

Even granting `B_map`, `m_k = lam_k^2` does **not** give `lam_k >= 0`. The nonnegative
branch is a second, separate element:

```text
B_plus:  lam_k >= 0 for every k        (=> sqrt(m_k) = lam_k)
B_abs:   lam_k of either sign          (=> sqrt(m_k) = |lam_k|)
```

`…REGISTRATION_ASYMMETRY…:364-366` registers the branch convention as **Residual
Atom 2**, "*Neither branch is adopted here*". And the framework's *native* operator
class points at the **signed** side:
`KOIDE_SIGNED_EIGENVALUE_VS_SINGULAR_VALUE_READOUT_..._2026-05-29.md:219-226` — "*The
native framework operator class is Hermitian (real, signed spectrum)*". A landed no-go
says so directly: `KOIDE_SIGNED_READOUT_IS_NOT_CHIRALITY_NARROW_NO_GO_NOTE_2026-06-04.md:51-54`
— Hermiticity "*does **not by itself FORCE** the map `√m_k := λ_k` over
`√m_k := |λ_k|`. That selection is an extra identification*".

**And on `B_abs` the exclusion simply fails.** I built the counterexamples exactly
(G4.5):

```text
r = 1, theta = pi/6 :  m = (4 + 2sqrt3,  4 - 2sqrt3,  1)      three DISTINCT, all NONZERO
r = 1, theta = pi/12:  m = (3 + sqrt2 + sqrt3 + sqrt6,  3 - 2sqrt2,
                            3 + sqrt2 - sqrt3 - sqrt6)         three DISTINCT, all NONZERO
r = 1, theta = pi/2 :  m = (1,  4 - 2sqrt3,  4 + 2sqrt3)      three DISTINCT, all NONZERO
```

**So `r = 1` is fully compatible with three distinct nonzero charged-lepton masses.**
Taken at face value, the campaign's "most promising positive lead" is refuted. This is
exactly T4 of the landed note (`:315-323`), which Wave 2 did not report.

### 3.3 The repair that survives — `B_plus` is *equivalent* to "`r` is the Koide readout"

This is the one place where I can strengthen the argument rather than break it, and it
is new relative to the landed note (which treats `B_plus` and `B_abs` as two free
branches and stops there).

The *physical* Koide ratio uses **positive** square roots by definition of a mass:

```text
Q_phys := (sum_k m_k) / (sum_k sqrt(m_k))^2  =  (sum_k lam_k^2)/(sum_k |lam_k|)^2
Q_H    := Tr(H^2)/(Tr H)^2                   =  (sum_k lam_k^2)/(sum_k lam_k)^2 = (1+2r)/3
```

These are the **same functional only when the spectrum is sign-homogeneous**. Proved
per-term rather than by sampling: `|u| - u = 0` for `u >= 0` and `= 2|u| > 0` for
`u < 0` (G4.3b), so `sum|lam| - sum lam = 2 sum_{lam<0}|lam|` (G4.3c), which vanishes
iff no `lam_k` is negative. Hence, with `a > 0`:

> **Lemma (readout biconditional, G4.3–G4.4).**
> `Q_phys = 1/3 + (2/3) r`  **iff**  `lam_k >= 0` for every `k`.

Exact witnesses on both sides: `(2, 1/2, 1/2)` gives `Q_phys = Q_H = 1/2` (G4.1);
`(4, -1/2, -1/2)` gives `Q_phys = 33/50` while `Q_H = 11/6` (G4.2). And at `r = 1` on
`B_abs`, `Q_H = 1` identically while `Q_phys` takes the *distinct* exact values
`9/(13 + 4sqrt3)` at `theta = pi/6` and `9/(9 + 4sqrt2)` at `theta = pi/12`
(G4.7–G4.10) — `Q_phys` is **phase-dependent**, so `r` pins no Koide value at all.

**Consequence.** `B_plus` is not an extra import stacked on top of the campaign's
premise; it **is** the campaign's premise. "The counting bit `r` selects the Koide
value" and "the spectrum is sign-homogeneous" are the same statement. The `B_abs`
escape saves `r = 1` only by dissolving the `r <-> Q` dictionary that makes `r` the
counting bit in the first place.

Likewise `B_map` is not free either, once the same demand is made: among
spectral-to-mass power maps `m_k = lam_k^p`, **only `p = 2`** yields `Q_phys = Q_H`
(G4.11.p1–p4, M12) — `p = 1, 3, 4` all fail. So `B_map` is forced up to scale by the
same requirement.

### 3.4 Robustness check — the alternative reading gives the same answer by a different route

Suppose instead the eigenvalues *were* the masses (`m_k = lam_k`). Then mass
nonnegativity `m_k >= 0` **forces** `lam_k >= 0` outright: `B_plus` is automatic and
there is no sign escape at all (G4.14). And `r = 1` still yields `m = (3a, 0, 0)`, i.e.
two massless members (G4.15). Under that reading the exclusion runs unconditionally —
but `Q_phys != Q_H` (G4.11.p1), so `r` is not the Koide bit.

> **Unified statement (G4.16).** `{r = 1}` + `{three distinct nonzero masses}` +
> `{sign-homogeneous spectrum}` is **impossible**, and sign-homogeneity follows from
> *either* reading — from mass nonnegativity under `m = lam`, or from the
> Koide-readout identity under `m = lam^2`.

### 3.5 The status of "three distinct nonzero masses"

This is realized-state data. `docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md:60-63`
and `axiom_premise_nodes.json:49` are explicit that a quoted number that would differ
under another law-admissible state is **registered data, not derivation output**. The
landed note handles this with the same discipline, inheriting the non-degeneracy
element `ND_3` "*at exactly its comparator/premise grade, labeled and never
thresholded; no numerical dataset is consumed*" (`:367-370`). I use it the same way:
as a **labelled supplied condition**, not a fit. That makes the result a *no-go
against a horn given supplied data*, never a derivation of `r`.

**Sensitivity (M8).** The exclusion is carried **entirely** by the three-distinct-and-
nonzero element. Weaken `ND_3` to "two distinct values" and it evaporates: `(3a,0,0)`
*has* two distinct values.

---

## 4. (c) The theorem, stated with every hypothesis — and what still stands

### 4.1 Statement

> **Theorem (r = 1 registration exclusion; conditional).**
> Let `C` be the `3x3` cyclic shift and `H = a I + b C + conj(b) C^2` the Hermitian
> circulant, `a` real and nonzero, `b` complex, `r := |b|^2/a^2`,
> `lam_k` its spectrum. Assume:
>
> - **(H1) carrier** — the generation carrier is the `C_3`-commutant, so `H` is the
>   circulant above. *(Mutation M3, M11: dropping the `C_3` commutant or replacing the
>   order-3 clock destroys the `(a,b)` coordinates and the `e_2` identity.)*
> - **(H2) `B_map`** — the spectral-to-mass map is `m_k = lam_k^2` (equivalently, any
>   `m_k = c lam_k^2`, `c > 0`). **Unadopted declared bridge.**
> - **(H3) readout** — the physical Koide ratio is `Q_phys = sum m / (sum sqrt m)^2`,
>   with positive roots, and the counting bit computes it: `Q_phys = 1/3 + (2/3) r`.
>   *(By §3.3 this is EQUIVALENT to `B_plus`, i.e. sign-homogeneity — it is not an
>   additional assumption beyond it.)*
> - **(H4) `ND_3^*`** — the registered pattern has three **distinct** and **nonzero**
>   values. **Supplied realized-state data, labelled, never thresholded.**
>
> Then `0 < r < 1` **strictly**. In particular `r = 1` is excluded; at `r = 1` the
> phase is forced to `theta = 0 (mod 2pi/3)` and the spectrum is exactly `(3a, 0, 0)`,
> masses `(9a^2, 0, 0)`, which violates (H4).
>
> Moreover the two horns are geometrically asymmetric: the nonnegative-phase window
> has half-width `alpha(r) = pi/3 - arccos(1/(2 sqrt r))`, which is **exactly `pi/12`
> at `r = 1/2`** (open interior sector) and **exactly `0` at `r = 1`** (measure-zero
> boundary point) — G4.4a–G4.4b.

Hypotheses (H2) and (H4) are the entire unadopted content. (H1) is landed carrier
structure. (H3) is the campaign's own defining premise. **`B_plus` does not appear as
a separate hypothesis** — that is the reduction this wave contributes.

**What the theorem is NOT.** It does not derive `r`, does not select `r = 1/2`, does
not adopt any bridge, and is not an empirical claim: `r = 1 => Q_H = 1` was already
incompatible with the comparator by one number. The theorem's content is
**structural** — that the `r = 1` horn is not an interior alternative but a
boundary/degenerate configuration.

### 4.2 What still stands between this and `r = 1/2` — four separate gaps

**Gap 1 — an endpoint exclusion is not a selection.** The admissible set is the open
interval `(0, 1)`, a continuum. Against the landed candidate values (G5.*):

| landed value | source | survives `0 < r < 1`? |
|---|---|---|
| `1/2` (`s=0`, block-count / `det_C`) | `GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05.md:86-88` | **YES** |
| `17/2 - 6 sqrt(2)` ≈ `0.0147` (idempotent/eigenvalue) | `FLAVOR_MISSING_AXIOM_CARRIER_MEASURE_NOTE_2026-05-30.md:76`; `C1_FRAME_COMPONENT_..._2026-07-02.md:210` | **YES** (G5.a, G5.b) |
| `1` (`s=1`, Born / `det_R`) | `GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05.md:88-90` | no — excluded |
| `0` (degenerate) | `FLAVOR_R_HALF_IS_A_STATIONARY_POINT_NOT_FORCED_2026-06-02.md:29` | no — excluded |
| `3/2` (`alpha_s=3, alpha_d=1`; 4-cell menu) | `FLAVOR_MAX_RECORD_ENTROPY_..._2026-06-15.md:60`; `ACPHILAMBDA_..._CORRESPONDENCE_..._2026-07-16.md:270` | no — **excluded** |
| `2` (metric x weight cell) | Wave 2 `wave2_defend_ex2.md:156` | no — **excluded** |

So the theorem is genuinely informative — it kills two landed values — but it does
**not** discriminate `1/2` from `17/2 - 6 sqrt(2)`. On the landed dial `r(s) = 2^(s-1)`
it deletes exactly the endpoint `s = 1` and leaves all of `s < 1` (G5.d–G5.e).

**Gap 2 — it excludes a VALUE, not the COUNT.** This is the subtlest gap and I flag it
as the load-bearing one. Wave 2's factorization is `r = gamma * nu` with
`gamma = g_0/g_1` the metric factor and `nu = w_1/w_0 = 2^s` the mode-count factor.
"Count-twice" is `nu = 2`; it maps to `r = 1` **only at `gamma = 1/2`**. Wave 2
demoted `gamma = 1/2` from theorem to conditional (the associativity/Frobenius
condition is an import), and showed that pushed to consistency the same bridge argues
for `r = 1`. So the theorem constrains the **product**: `gamma * nu < 1`. Count-twice
at `gamma < 1/2` is untouched. **Excluding `r = 1` is not the same as excluding
count-twice**, and the campaign should not state it that way.

**Gap 3 — the two unadopted elements remain unadopted.** `B_map` and `ND_3^*` are
where the whole thing rests. `B_map` is registered as an open residual atom; `ND_3^*`
is supplied data. Neither is discharged by anything in this wave.

**Gap 4 — positivity is not free even at `r = 1/2`.** At `r = 1/2` the nonnegative
window is the closed set `delta(theta) <= pi/12`; **outside** it an eigenvalue is
negative (M6c, exact at `theta = pi/6`). So `B_plus` — equivalently (H3) — is a real
joint constraint on `(r, theta)`, not an automatic consequence of `r < 1`. Inside the
window the sector is genuinely occupied: at `theta = pi/24` the spectrum is three
distinct strictly positive values with `Q_phys = Q_H = 2/3` exactly (M6, M6b).

### 4.3 The P1/P2 reconciliation (the campaign's stated contradiction)

The two results constrain **different objects**: P1 (exercise sector 3) constrains an
isotypic **spectral-weight ratio** built from a heat trace, `r = (S + 2F)/(S - F)`;
P2 constrains the **spectrum of the realized element** `H`. They collide only because
sector 3 identifies `r` with `g_0/g_1` outright, i.e. sets `nu = 1`.

Under that identification they are jointly inconsistent while `F > 0` is retained
(G5.f–G5.g). But solving the constraint exactly rather than declaring a contradiction:

```text
r = (1 + 2x)/(1 - x),   x := F/S                                           (G5.i)
r < 1     <=>   x in (-1/2, 0)   EXACTLY                                   (G5.j)
x = 0     <=>   r = 1            (the boundary point)                      (G5.k)
x = -1/5  <=>   r = 1/2          (sector 3's own breach number)            (G5.h, G5.l)
```

**So P1 and P2 agree.** Both force a **graded** equivariant weight (`F < 0`, a
supertrace with negative contributions), and P1's own breach value sits inside the
window P2 forces. The supervisor's Wave-3 prediction — "different objects, both can
hold, squeezed from opposite sides" — is confirmed, and the intersection is **not
empty**: it is `x in (-1/2, 0)`, equivalently `r in (0,1)`, with `r = 1/2` interior.
The campaign's graded-operator target is thereby sharpened from "a pass/fail number"
to "a one-sided sign requirement with an exact admissible window".

---

## 5. (d) Gating and mutation probes

Runner: `…/scratchpad/wave3_degenerate_exclusion_probe.py`, log `…/wave3_run.log`.
**PASS=119, FAIL=0.** All inputs are exact symbols, rationals or radicals.

Construction-mutation probes (each must, and does, break the result):

| probe | mutation | outcome |
|---|---|---|
| **M1 / M1b** | drop Hermiticity: `H = aI + bC + cC^2`, `c` free | `e_2 = 3(a^2 - bc)`, which collapses to `3(a^2-|b|^2)` **only** at `c = conj(b)`. The identity is Hermiticity-specific. |
| **M2** | `N = 4` circulant | `e_2 = 2(3a^2 - 2b^2)`; neither the coefficient nor the `(3a,0,0)` conclusion survives the group order. Confirms the wall exercise's "`N=3` artifact" flag. |
| **M3** | non-circulant Hermitian, same trace | `e_2 = 3a^2 - br^2` — different; the `C_3` commutant is load-bearing. |
| **M4** | `a < 0` | `e_1 = 3a < 0`, so a *nonnegative* spectrum is impossible (an all-nonpositive one is not — see M7). |
| **M5** | drop `lam >= 0` from the `e_2 = 0` step | `(1, 1+sqrt3, 1-sqrt3)` has `e_2 = 0` with **three distinct nonzero** eigenvalues. **The rank-one conclusion is bought entirely by the sign condition.** |
| **M6 / M6b** | non-vacuity at `r = 1/2`, `theta = pi/24` | three distinct strictly positive values, `Q_phys = Q_H = 2/3` exactly. The `r<1` side is genuinely occupied. |
| **M6c** | `r = 1/2`, `theta = pi/6` (outside the window) | an eigenvalue is negative — positivity is **not** automatic even at `r = 1/2`. |
| **M7** | all-negative branch | `Q_phys = Q_H` still holds — the operative hypothesis is **sign-homogeneity**, not positivity; `a > 0` is the normalization. |
| **M8** | weaken `ND_3` to "two distinct" | exclusion evaporates: `(3a,0,0)` has two distinct values. |
| **M9** | drop K-reality (`Im b != 0`) | `e_2 = 3(a^2-|b|^2)` unchanged — the theorem does **not** secretly consume the K/CPT tie. |
| **M10** | perturb to `|b| = 9a/10 < a` at `theta = 0` | spectrum `(1/10, 1/10, 14/5)` stays nonnegative and is no longer `(3a,0,0)`: the forcing is exactly at `r = 1`. |
| **M11** | replace the order-3 clock by a transposition | commutant is no longer the 3-parameter circulant algebra; `(a,b)` do not exist. |
| **M12 / G4.11** | `m_k = lam_k^p`, `p in {1,2,3,4}` | only `p = 2` gives `Q_phys = Q_H`; `B_map` is forced up to scale by the readout demand. |

---

## 6. Live ledger status of every surface cited (queried from `origin/main`)

I set no status and predict none. This is a read of `docs/audit/data/ledger/**`.

| surface | claim_type | effective_status | audit_status |
|---|---|---|---|
| `koide_equipartition_endpoint_registration_asymmetry_bounded_theorem_note_2026-07-12` | bounded_theorem | **unaudited** | unaudited |
| `koide_first_order_section_tie_vs_outcome_label_residual_localization_bounded_theorem_note_2026-07-11` | bounded_theorem | unaudited | unaudited |
| `records_only_os_reconstruction_untied_first_order_measure_bounded_theorem_note_2026-07-11` | bounded_theorem | unaudited | unaudited |
| `charged_lepton_koide_value_full_chain_of_custody_2026-06-02` | open_gate | unaudited | unaudited |
| `koide_signed_eigenvalue_vs_singular_value_readout_narrow_theorem_note_2026-05-29` | positive_theorem | unaudited | unaudited |
| `koide_signed_readout_is_not_chirality_narrow_no_go_note_2026-06-04` | no_go | unaudited | unaudited |
| `generation_weight_dial_structure_2026-06-05` | positive_theorem | unaudited | unaudited |
| `record_generation_readout_two_sectors_2026-06-05` | bounded_theorem | unaudited | unaudited |
| `charged_lepton_koide_cone_algebraic_equivalence_narrow_theorem_note_2026-05-10` | positive_theorem | audit_in_progress | audit_in_progress |
| `rd_bridge_anatomy_agreement_conditioned_double_registration_bounded_note_2026-06-12` | bounded_theorem | unaudited | unaudited |
| `flavor_einselection_2sector_modulo_kreality_2026-06-02` | bounded_theorem | audited_conditional | audited_conditional |
| **`flavor_r_half_is_a_stationary_point_not_forced_2026-06-02`** | bounded_theorem | **retained_bounded** | **audited_clean** |
| **`koide_circulant_q_two_thirds_algebraic_narrow_theorem_note_2026-05-10`** | positive_theorem | **retained** | **audited_clean** |
| **`flavor_doublet_metric_default_is_detr_2026-06-02`** | bounded_theorem | **retained_bounded** | **audited_clean** |

Consistent with the brief's warning: **the entire spine this result would land on —
the equipartition-asymmetry note, the two 2026-07-11 parents, the chain of custody,
the signed-readout notes, the dial — is `unaudited`.** Only three of fourteen carry
retained grade, and none of those three carries `B_map`, `B_plus`, or the `(3a,0,0)`
forcing. Nothing in §3–§4 should be described as retained.

---

## 7. Net for the campaign

1. **Wave 2's arithmetic is correct and its result is real — but it is not new.** It
   is `KOIDE_EQUIPARTITION_ENDPOINT_REGISTRATION_ASYMMETRY_BOUNDED_THEOREM_NOTE_2026-07-12`
   (T1/T2/T3), landed twelve days before the campaign opened, cited by **no** wave and
   **no** exercise sector. The campaign's discovery procedure has a prior-art hole.
2. **Wave 2 dropped that note's T4, which is the refutation of the lead as stated.**
   On the sign-allowed branch `r = 1` hosts three distinct nonzero masses; I rebuilt
   three exact witnesses. "The `r = 1` horn is excluded because the leptons are
   massive" is **false** as an unconditional claim.
3. **The salvage is real and is this wave's contribution.** `B_plus` is not an extra
   import: `Q_phys = 1/3 + (2/3)r` **iff** the spectrum is sign-homogeneous. The
   `B_abs` escape rescues `r = 1` only by destroying the `r <-> Q` dictionary that
   makes `r` the counting bit. So within the campaign's own framing the horn is
   excluded, conditional on `B_map` (a registered open residual) plus supplied
   three-distinct-nonzero-mass data — and `B_map` is itself forced up to scale by the
   same readout demand (`p = 2` uniquely).
4. **The stated Wave-3 contradiction dissolves into an agreement, with an exact
   window.** `r < 1` applied to sector 3's `r = (1+2x)/(1-x)` forces `x = F/S` into
   `(-1/2, 0)`; sector 3's own `-1/5` is inside. Both results demand a **graded /
   supertrace** equivariant weight, and `x = 0` is exactly the `r = 1` boundary. This
   is the sharpest surviving handle in the campaign: the target is now a **sign**
   requirement on an equivariant trace with a computed admissible window, not a bare
   number.
5. **Do not overstate the reach.** The result excludes a *value* (`r = 1`), not the
   *count* — count-twice maps to `r = 1` only at `gamma = 1/2`, which Wave 2 demoted.
   And excluding an endpoint leaves the open interval `(0,1)`: it kills the landed
   values `3/2` and `2`, but keeps both `1/2` and `17/2 - 6 sqrt(2)`.
