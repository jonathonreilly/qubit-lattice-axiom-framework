# Wave 2 — the breach target: verify and sharpen the positivity obstruction

**Date:** 2026-07-24
**Role:** verify/sharpen the EX3 positivity obstruction and its breach condition.
**Status:** campaign working note. Not a repo note, not a claim, not an audit
input. No axiom, no primitive, no new vocabulary, no verdict, no promotion.
Nothing here sets or predicts an audit status.
**Working tree:** `origin/main` fetched at session start,
tip `62826882ac69e1abd03355e91bf548d608cf585c`. Nothing committed, pushed, or
PR'd; the only file written in the repo is this one.
**Probe (exact, sympy, no float inputs):**
`/private/tmp/claude-502/-Users-jonBridger-Toy-Physics--claude-worktrees-quirky-wiles-92e3b4/66008b76-8d97-42b5-b1e1-4e60c09bb2e9/scratchpad/wave2_breach_probe.py`
**Probe close:** `TOTAL: PASS=123 FAIL=0`
(output at `.../scratchpad/out.txt`). Every sentence in §2–§6 that carries a
number is written FROM that output; nothing here is asserted from memory.

---

## 0. Framework refresher — surfaces actually read before concluding

1. `docs/audit/data/axiom_premise_nodes.json` — resolved `minimal_axioms.current_path`
   → `docs/MINIMAL_AXIOMS_2026-06-29.md`; read all four registry nodes and their
   exclusion notes.
2. `docs/MINIMAL_AXIOMS_2026-06-29.md` in full — Lattice / Qubit / Admissibility /
   Record, the Qualification clause, and `:97-101` ("Axioms and approved primitives
   are the complete supplied foundation… No admission class exists"). Load-bearing
   for this report: `:156-173` lists **weighting, normalization, probability rules,
   Born weights, context selection** among the gates the axioms do **not** close,
   and `:103-118` states Admissibility supplies **no** transfer operator or weights.
3. `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` — the four approved
   primitives; item 5 ("do not grant more than the source note declares") names
   *weighting*, *normalization rule*, and *probability rule* as separate.
4. Source notes of every primitive I could have been tempted to invoke:
   `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md`,
   `docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md`,
   `docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`.
   **I invoke none of them.** Nothing below needs a scale, a kinetic-form ratio,
   or a realized state.
5. Lane surfaces read in full or in the load-bearing part:
   `docs/ACPHILAMBDA_AMBIENT_EQUIVARIANT_HEAT_TRACE_FACE_2026-07-02.md`,
   `docs/FLAVOR_DOUBLET_METRIC_DEFAULT_IS_DETR_2026-06-02.md`,
   `docs/CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md`,
   `docs/SUPERTRACE_INDEX_HOLOMORPHIC_ROUTE_TO_KOIDE_R_HALF_OPEN_LEAD_NOTE_2026-06-04.md`,
   `docs/KOIDE_KAHLER_DIRAC_REALIZATION_GIVES_R_ONE_INDEX_ROUTE_CLOSED_BOUNDED_NO_GO_NOTE_2026-06-08.md`,
   `docs/KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md`,
   `docs/KOIDE_GENERATION_ID_CL3_GRADE1_BRIDGE_NARROW_THEOREM_NOTE_2026-06-02.md`,
   plus `.claude/science/exercises/koide-counting-bit-20260724/ex3_literature_templates.md`.

**Ledger statuses checked on the tracked shards (not from note headers):**

| claim id | effective_status | audit_status |
|---|---|---|
| `flavor_doublet_metric_default_is_detr_2026-06-02` | **retained_bounded** | **audited_clean** |
| `koide_frobenius_isotype_split_uniqueness_note_2026-04-21` | unaudited | unaudited |
| `acphilambda_ambient_equivariant_heat_trace_face_2026-07-02` | unaudited | unaudited |
| `koide_kahler_dirac_realization_gives_r_one_index_route_closed_bounded_no_go_note_2026-06-08` | unaudited | unaudited |
| `charged_lepton_value_reduces_to_one_counting_bit_synthesis_note_2026-06-05` | meta | unaudited |
| `supertrace_index_holomorphic_route_to_koide_r_half_open_lead_note_2026-06-04` | unaudited | unaudited |

Only one surface I lean on is retained-grade, and it is the decisive one:
`flavor_doublet_metric_default_is_detr_2026-06-02` (**retained_bounded /
audited_clean**). Everything else is rebuilt natively in the probe; the heat-trace
identity is **re-derived, not cited** (Block A).

*(Wave-1 flagged a stale `retained_no_go` label for
`koide_frobenius_isotype_split_uniqueness` at
`CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md:72`.
The shard still reads `unaudited`. I do not rely on that note's status either way.)*

---

## 1. Headline

The EX3 obstruction is **arithmetically correct and structurally void**. Its
algebra reproduces exactly; its *identification* of that algebra with the
campaign's `r` silently drops the Gram factors `(3, 6)` of the generation
coefficient surface — a factor of exactly **2**, which **is** the counting bit.

> **What EX3 computed is `w_triv / w_nontriv`, the per-real-dimension isotypic
> weight ratio. That equals `r` only in the `det_R` (count-twice) reading. The
> campaign's stated convention `r = g_0/g_1` is the `det_C` (count-once) reading,
> which is exactly half of it. So "no positive weight reaches `r = 1/2`" is a
> statement made *after* the counting bit has already been set to count-twice —
> and in that reading `r > 1` is not news, it is the landed sentence "the
> heat-kernel arrow flows `r -> 1`"
> (`CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md:97-98`)
> with a finite-`t` sign attached.**

The consequences, all gated:

1. In the campaign's own `det_C` reading the same positive weights give
   `r(t) = (S + 2F) / (2(S - F))`, the breach is `F/S = 0`, and it is **attained
   exactly** by a nonnegative spectral function of the landed lattice Laplacian
   (Block E2). **No grading is needed and none is missing.**
2. Even in the `det_R` reading, `F/S = -1/5` is attained exactly by a
   positive-semidefinite `C_3`-covariant weight (Block E3). The obstruction's true
   scope is the strictly narrower class `{f(Delta) : f >= 0}` (equivalently
   entrywise-nonnegative covariant kernels), **not** "any positive weight".
3. `F/S = -1/5` names the perfectly ordinary cone point `diag(1,4,4)` — a
   positive-definite `C_3`-invariant form, interior to the landed uniqueness cone
   (Block F7a/F7b). It is not exotic and it is not a grading.
4. **The breach condition is grading-invariant.** `F/S` depends on a `Z_2` grading
   only through the signed products `eps_pi * h_pi`, and `F/S = -1/5` forces
   `eps_1 = eps_0` — i.e. the grading collapses to a global sign — plus
   `h_1/h_0 = 2`, which is precisely the ungraded isotype-weight freedom the
   landed uniqueness no-go already leaves open (Block F7c). **A grading cannot
   supply the breach; it can only relabel it.**
5. Every landed graded object computes to a value that is not `-1/5`, with margin:
   the framework's own chiral grading `Gamma_chi` has reachable set
   `(-inf, -1/2) U (1, +inf)` and never induces a positive-definite form at all;
   the physical `L/R` grading and the Kähler-Dirac grading give `0/0`; the
   staggered grading gives `S = 0` identically; and integrality forbids denominator
   5 for every index-type grading (Block F).

So the deliverable is a **double sharp negative**: the spectral-weight route does
not close the bit, *and* the graded route named as the repo's one open handle
cannot close it either — but for a reason different from the one EX3 proposed.
The reason is not that `-1/5` is out of reach. It is that `-1/5` is **not a
well-posed target**: it is the image of `r = 1/2` under a map that has already
fixed the bit.

---

## 2. (a) Native re-derivation of the heat weight and the cone point

### 2.1 The landed identity, quoted then rebuilt

`docs/ACPHILAMBDA_AMBIENT_EQUIVARIANT_HEAT_TRACE_FACE_2026-07-02.md:14-30`:

```text
:14  Let `Z_N^3` be the periodic cubic lattice, let `A` be nearest-neighbor
:15  adjacency, and let `Delta = 6I - A`. Let `R` be the proper cubic coordinate
:16  cycle
:18      R(x1,x2,x3) = (x3,x1,x2).
:20  For `j = 1, 2` and any function `f`,
:22      Tr(f(Delta) R^j) =
:23        sum_{R^j k = k} f(Delta_hat(k)).
:25  The fixed momenta are exactly the `[111]` diagonal momenta
:26  `k = (kappa,kappa,kappa)`, each with unit trace weight. Therefore
:28      Tr(exp(-t Delta) R^j) =
:29        sum_{m=0}^{N-1} exp(-t (6 - 6 cos(2 pi m/N))).
```

Per the repo's build-cited-algebra rule this is **rebuilt, not cited**. Probe
Block A constructs `Z_N^3` site-by-site, forms `A`, `Delta = 6I - A`, and the
permutation matrix of `R`, then certifies exactly:

```
PASS  A1 N=2..5   fixed momenta = [111] diagonal, count N
PASS  A2 N=2..5 j=1,2  Tr(Delta^p R^j) = sum_diag dhat^p, p=0..4
PASS  A3 N=2..5   dhat(kappa,kappa,kappa) = 6 - 6 cos(kappa)
PASS  A4 N=3,4    j=0 gives the FULL momentum sum, not the diagonal
```

Matching the moments `p = 0..4` on a finite spectrum pins `Tr(f(Delta)R^j)` for
every `f`, so `A2` re-derives the displayed identity rather than checking one `f`.
`A4` reproduces the landed rejector at `:99-100` ("The identity component `j = 0`
gives the full heat trace, not the diagonal sum"), which is the exact reason `F`
is a *proper* sub-object of `S`.

Write, as EX3 does,

```text
S(t) = Tr(e^{-t Delta})     = sum over all N^3 momenta of exp(-t Delta_hat(k))
F(t) = Tr(e^{-t Delta} R)   = sum over the N diagonal momenta   (= Tr(e^{-tDelta}R^2))
```

### 2.2 `F` is a strict sub-sum of `S`

```
PASS  A5 N=2,3,4,6  0 < F < S strictly (complement has N^3-N terms)
PASS  C4 N=3,6,12   S-F = sum over the N^3-N non-diagonal momenta,
                    all multiplicities positive   (|complement| = 24, 210, 1716)
```

`S - F` is built directly as the sum over the complement of the diagonal set;
it has `N^3 - N > 0` terms for every `N > 1`, each `exp(-t * real) > 0`. So

```text
0 < F(t) < S(t)     for every t > 0 and every N > 1        (strict)
```

This part of EX3 is correct and I confirm it.

### 2.3 Isotypic weights

`P_pi = (1/3) sum_j conj(chi_pi(R^j)) R^j`, with `chi_triv = (1,1,1)`,
`chi_omega = (1, omega, omega^2)`, `chi_omegabar = (1, omega^2, omega)` and
`omega = -1/2 + i sqrt(3)/2` built exactly:

```text
w_triv    = Tr(P_triv  rho) = (S + 2F)/3
w_nontriv = Tr(P_omega rho) = Tr(P_omegabar rho) = (S - F)/3
```

```
PASS  B1a  w_triv = (S+2F)/3
PASS  B1b  w_omega = w_omegabar = (S-F)/3
PASS  B1c N=2,3  Tr(P_triv)=(N^3+2N)/3, Tr(P_om)=(N^3-N)/3
```

Confirmed. EX3's §4.2 weights are right.

### 2.4 The step EX3 gets wrong: weights → cone point

EX3 writes (`ex3_literature_templates.md:395-402`):

> `G(t) = w_triv P_triv + w_nontriv P_doublet`, i.e. the cone point
> `diag(g_0, g_1, g_1)` with `g_0 = w_triv`, `g_1 = w_nontriv`
> (per real doublet direction). Therefore `r(t) = g_0/g_1 = (S + 2F)/(S - F)`.

The operator statement is fine; the coordinate statement is not. The campaign's
`g_0, g_1` are the diagonal entries **on the circulant coefficient surface
`(a, Re b, Im b)`** — that is what makes `diag(3,6,6)` "the HS point" and
`diag(1,1,1)` "the flat point". On that surface the carrier vector is
`v = a u_0 + b u_1 + conj(b) u_2` with `u_j = (1, omega^j, omega^{2j})`, and the
Gram factors are not 1:

```text
||P_0 v||^2 = 3 a^2            ||P_d v||^2 = 6 |b|^2
```

```
PASS  B2b  ||P_0 v||^2 = 3a^2      = 3*a**2
PASS  B2c  ||P_d v||^2 = 6|b|^2    = 6*b_im**2 + 6*b_re**2
```

Hence the quadratic form of `G = w_0 P_0 + w_1 P_d` in coefficient coordinates is

```text
G(v,v) = 3 w_0 a^2 + 6 w_1 |b|^2      ==>   diag(g_0, g_1, g_1) = diag(3 w_0, 6 w_1, 6 w_1)
```

```
PASS  B2d  coefficient-coordinate metric = diag(3w0, 6w1, 6w1)   g0=3*w0 g1=6*w1
```

So `g_0/g_1 = w_0 / (2 w_1)`, **not** `w_0/w_1`. Dropping the `(3,6)` is a single
mutation, and it is exactly the mutation that produces EX3's formula:

```
PASS  D4  MUTATION drop the Gram factors (3,6): det_C reading collapses to
          (S+2F)/(S-F)   ["this single mutation reproduces the EX3 formula"]
```

### 2.5 The two landed readings, rebuilt

`docs/FLAVOR_DOUBLET_METRIC_DEFAULT_IS_DETR_2026-06-02.md` — **retained_bounded,
audited_clean** — is the governing surface. `:16-19`:

```text
:16  > On the `C3` circulant coefficient surface `(a, Re b, Im b)`, the
:17  > Hilbert-Schmidt/coherent-state metric is `diag(3,6,6)`. The metric is
:18  > reading-neutral: it does not by itself choose whether the doublet is counted
:19  > as two real directions or one complex block.
```

and `:35-39`:

```text
:35  det_R / per-real-direction reading:
:36    3a^2 = 6(Re b)^2 = 6(Im b)^2 -> |b|^2=a^2 -> r=1 -> Q=1
:38  det_C / equal-complex-block reading:
:39    3a^2 = 6|b|^2 -> r=1/2 -> Q=2/3
```

Solving both readings on a general `diag(g_0, g_1, g_1)`:

```text
det_C:   g_0 a^2 = g_1 |b|^2                    ==>  r = |b|^2/a^2 = g_0/g_1
det_R:   g_0 a^2 = g_1 (Re b)^2 = g_1 (Im b)^2  ==>  r = 2 g_0/g_1
```

```
PASS  B3a  det_C (equal-complex-block) reading: r = g0/g1        r = g0/g1
PASS  B3b  det_R (per-real-direction) reading: r = 2 g0/g1       r = 2*g0/g1
PASS  B3c  landed HS point diag(3,6,6) -> (det_C, det_R) = (1/2, 1)
PASS  B3d  flat point diag(1,1,1) -> (det_C, det_R) = (1, 2)
```

`B3c/B3d` reproduce the landed table at
`CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md:69-70`:

```text
:69  | **block-count `(1,1)`** = det_C | equal weight / equal HS energy per block
:69    (`3a^2 = 6|b|^2`) | **1/2** | **2/3** | charged-lepton target |
:70  | **dimension `(1,2)`** = det_R | real-dimension / Born / trace | **1** | **1** |
```

The campaign's `r = g_0/g_1` is therefore the `det_C` reading — count-once. Also
note the two named horns are only distinct **because** they are coefficient-surface
forms; in an orthonormal (per-real-dimension) reading `diag(3,6,6)` is the
identity and the two horns would collapse:

```
PASS  B4g  both named cone points are COEFFICIENT-coordinate forms; in the
           orthonormal (gamma) reading diag(3,6,6) and diag(1,1,1) would collapse
           to the same ray, so the two horns would not be distinct
```

### 2.6 The corrected cone point, and what EX3 actually computed

```
PASS  B4a  r_detC(t) = (S+2F) / (2(S-F))
PASS  B4b  r_detR(t) = (S+2F) / (S-F)   [ = the EX3 formula ]
PASS  B4c  r_detR / r_detC = 2 exactly (the counting factor)
PASS  B4d  r_detR = gamma_0/gamma_1  (the per-real-dimension weight ratio)
PASS  B4e  r_detC = gamma_0/(2 gamma_1)  -- exactly half
PASS  B4f  EX3's (S+2F)/(S-F) IS gamma_0/gamma_1 = w_triv/w_nontriv, i.e. the
           det_R (count-twice) reading -- not the campaign's r = g0/g1
```

So the exact displayed algebra is:

```text
gamma_0 = w_triv    = (S + 2F)/3          (weight per real dimension, trivial isotype)
gamma_1 = w_nontriv = (S -  F)/3          (weight per real dimension, doublet)

(g_0, g_1) = (3 gamma_0, 6 gamma_1)       (coefficient-surface metric)

r_detC(t) = g_0/g_1   = (S + 2F) / (2 (S - F))        <- the campaign's r
r_detR(t) = 2 g_0/g_1 = (S + 2F) /    (S - F)          <- what EX3 computed
```

Both are strictly monotone in `x = F/S`, and with `0 < F < S`:

```text
r_detR(t) > 1     strictly, every t > 0, every N > 1
r_detC(t) > 1/2   strictly, every t > 0, every N > 1
```

```
PASS  C1a/C1b  r_detR = (1+2x)/(1-x),  r_detC = (1+2x)/(2(1-x)),  x = F/S
PASS  C1c      dr/dx > 0 on x in (-1/2, 1): both readings strictly increasing
PASS  C1d      x>0  <=>  r_detR > 1
PASS  C1e      x>0  <=>  r_detC > 1/2
```

Exact instances (`t` supplied as an exact rational, 16-digit display, gates
evaluated at 80 digits):

```text
  N    t        F/S                      r_detR               r_detC
  3    1/1000   0.1111117786664987       1.375002534626266    0.6875012673131328
  3    1/2      0.3379123837754737       2.531122356746579    1.265561178373289
  3    3        0.9992599065484434       4051.542148887169    2025.771074443585
  3    10       0.9999999999994385       5343237290762.231    2671618645381.116
  6    1/1000   0.02777794444440278      1.085714814693836    0.5428574073469180
  6    1/2      0.06739295423077600      1.216788907621397    0.6083944538106984
  6    3        0.7518547169398507       10.08969182490087    5.044845912450435
  6    10       0.9997276498812528       11013.23294280071    5506.616471400356
  12   1/1000   0.006944486111100694     1.020979147733359    0.5104895738666796
  12   1/2      0.01670163564637298      1.050955954729016    0.5254779773645080
  12   3        0.1474458697936691       1.518838151982156    0.7594190759910780
  12   10       0.6802527316675477       7.382410100469712    3.691205050234856
```

EX3's own quoted numbers reproduce exactly, which is why I say their *arithmetic*
is sound:

```
PASS  C5 N=12 t=1/1000000  reproduces EX3's quoted r_detR = 1.0209790
PASS  C5 N=12 t=1/2        reproduces EX3's quoted r_detR = 1.0509560
PASS  C5 N=12 t=3          reproduces EX3's quoted r_detR = 1.5188382
PASS  C5 N=12 t=10         reproduces EX3's quoted r_detR = 7.3824101
```

### 2.7 A correction to EX3's limit reading, worth keeping

EX3 §4.3 reads the `t -> 0, N -> oo` limit as "the FLAT point". It is not. The
induced **metric** in that limit is the **HS** point:

```
PASS  B5 N=3   t->0 induced metric ratio g0/g1 = 11/16  -> 1/2
PASS  B5 N=6   t->0 induced metric ratio g0/g1 = 19/35  -> 1/2
PASS  B5 N=12  t->0 induced metric ratio g0/g1 = 73/143 -> 1/2
PASS  B5-lim   N->oo of the t->0 metric ratio = 1/2  (the HS point diag(3,6,6))
```

The ultra-local, infinite-volume equivariant heat weight converges to
`diag(3,6,6)` — the Hilbert-Schmidt metric. Which `r` that *is* depends entirely
on the reading, and the retained_bounded theorem says the metric does not choose.
That is the whole campaign question, restated by an independent route.

### 2.8 Construction-mutation probes

Per campaign rule 3 these are mutations of the **construction**, not assertion
checks:

```
PASS  D1  MUTATION C_3 -> C_4 face rotation: fixed-momentum count changes
          (|fix_C4| = 8 vs |fix_C3| = 4 at N=4)     [landed rejector :100-101]
PASS  D2  MUTATION Delta -> 6I-2A: F/S changes, so the relation is not tautological
PASS  D3  MUTATION wrong character in P_omega: weight != (S-F)/3
PASS  D4  MUTATION drop the Gram factors (3,6): reproduces the EX3 formula
PASS  D5 c=1,3,1/2  MUTATION (S+cF)/3 != Tr(P_triv rho)
PASS  D5 d=2,1/2    MUTATION (S-dF)/3 != Tr(P_omega rho)
PASS  D6  MUTATION C_3 -> C_2: no 2-dim doublet, so no (3,6) Gram pair exists
```

`D5` is the probe the brief asked for: it would catch a wrong coefficient in the
`(S + 2F)/(S - F)` relation. `D4` is the probe that actually **fires** on EX3 —
one construction mutation, and the whole `-1/5` number appears.

### 2.9 The finding is convention-robust (steelman closed)

A reviewer's natural escape is: "read `diag(g_0,g_1,g_1)` as the *operator*
eigenvalues `gamma` instead of the coefficient-surface entries, and then EX3's
`(S+2F)/(S-F)` *is* the campaign's `r`." That reading is self-consistent on the two
named points (`gamma = (3,6)` gives `det_R` `r = 1/2`; `gamma = (1,1)` gives
`r = 1`), so it must be answered rather than waved away.

It is not the landed reading — `FLAVOR_DOUBLET_METRIC_DEFAULT_IS_DETR_2026-06-02.md:16-17`
says explicitly "On the `C3` circulant coefficient **surface** `(a, Re b, Im b)`,
the Hilbert-Schmidt/coherent-state metric is `diag(3,6,6)`", and under the operator
reading `diag(3,6,6)` could not be *called* the HS point (the HS metric on the
mass-root vector is the identity operator, `gamma_0 = gamma_1 = 1`, which that
reading labels "flat"). So the names would have to swap.

**But the conclusion does not depend on resolving this.** Under either convention
the map (form) -> `r` carries a free factor of exactly 2, and that factor is the
counting bit:

- coefficient reading: `r_detC = (S+2F)/(2(S-F))`, `r_detR = (S+2F)/(S-F)`;
- operator reading: `r_detC = (S+2F)/(2(S-F))`, `r_detR = (S+2F)/(S-F)`.

They are the *same pair of numbers*; only the label "which one is `r`" moves. In
both, the positivity bound is a bound on `gamma_0/gamma_1` alone (gate B4d), the
target `r = 1/2` is reachable in the complementary reading (gates E2d, C3a), and
`-1/5` is the `det_R` image of `r = 1/2` (gate C2a). Choosing the other convention
relabels the sentence; it does not restore an obstruction.

### 2.10 Scope caveat I must record

The `R` in the landed identity is the **proper cubic coordinate cycle** — a
spatial rotation from the Lattice axiom
(`ACPHILAMBDA_AMBIENT_EQUIVARIANT_HEAT_TRACE_FACE_2026-07-02.md:15-18`), and its
`Delta` is declared "a calculational device, not a claimed dynamics" (`:64-66`).
The generation `C_3` is the circulant `C` on the flavor index. EX3 transfers the
lattice isotypic weights onto the generation carrier without naming a bridge; I
find none landed. So the lattice heat trace is a legitimate **instance** of a
positive `C_3`-covariant weight, but its transfer to the generation carrier is a
modelling step, not supplied structure. This weakens EX3's "on the framework's own
carrier" framing. It does not affect any conclusion below, because §3–§5 are
carrier-independent statements about isotypic weights.

---

## 3. (b) The breach number, verified and re-scoped

### 3.1 `-1/5` is exactly right — in the `det_R` reading

```text
(S + 2F)/(S - F) = 1/2   <=>   2(S + 2F) = S - F   <=>   S + 5F = 0   <=>   F/S = -1/5
```

```
PASS  C2a  r_detR = 1/2  <=>  F/S = -1/5 EXACTLY        solution set = [-1/5]
```

Verified. The number is exact and EX3's derivation of it is correct.

### 3.2 Weight positivity at the breach — and a factor-3 slip in EX3

At `F = -S/5`:

```text
w_triv    = (S + 2F)/3 = (S - 2S/5)/3 = (3S/5)/3 = S/5
w_nontriv = (S -  F)/3 = (S +  S/5)/3 = (6S/5)/3 = 2S/5
```

```
PASS  C2b  at the breach: w_triv = S/5 and w_nontriv = 2S/5 (both > 0 for S>0)
PASS  C2c  EX3's quoted (3S/5, 6S/5) are the NUMERATORS S+2F, S-F, not the weights
PASS  C2d  breach ratio w_triv/w_nontriv = 1/2 either way
```

EX3 `:451` states "`w_triv = 3S/5`, `w_nontriv = 6S/5`". Those are `S + 2F` and
`S - F` — the projector traces **before** the `1/3`. The correct weights are
`S/5` and `2S/5`. Both are positive for `S > 0`, so EX3's positivity conclusion
survives, but the quoted numbers are wrong by `3x` and should not be carried
forward.

### 3.3 What `F/S < 0` means — and the class where it is actually forbidden

`F = Tr(rho R)` is the trace of the weight against the `C_3` generator. Three
distinct classes, and the obstruction holds on exactly two of them:

| class | `F` sign | reason |
|---|---|---|
| **(A)** `rho = e^{-t Delta}` (heat semigroup) | `F > 0` strictly | `F` is a sum of `N` positive exponentials |
| **(B)** `rho = f(Delta)`, `f >= 0` | `F >= 0` | `F` is a sub-sum of nonnegative spectral terms; `F = 0` attainable |
| **(C)** `rho` PSD, `[rho, R] = 0` | **any sign** | `rho = P_omega + P_omegabar` gives `F/S = -1/2` |

```
PASS  E1   class {e^{-t Delta}}: F is a sum of N positive terms => F > 0 strictly
PASS  E3a  rho = alpha P_triv + beta (P_om + P_ombar) is PSD and R-covariant
           for alpha,beta > 0            S = 11a + 16b,  F = 11a - 8b   (N=3)
PASS  E3b  a PSD covariant weight ATTAINS F/S = -1/5 exactly (beta = 11/4 alpha)
PASS  E3c  at that point both isotypic weights are strictly positive
PASS  E3d  therefore 'positive-semidefinite covariant weight' does NOT force
           F >= 0; only f(Delta) with f>=0 (or an entrywise-nonneg kernel) does
```

**This is the first re-scoping.** EX3's headline (`ex3:61-68`) says "for any
positive covariant semigroup `rho`… hence `g_0/g_1 > 1` strictly" and §4.4.1
concludes "**no positive functional of this class exists**". That is false as
stated: an explicitly positive-semidefinite, `C_3`-covariant, positive-definite-form-
inducing weight attains `F/S = -1/5` exactly, at `beta = (11/4) alpha` on `Z_3^3`.
What is true is the narrower statement: **`F >= 0` on the class of nonnegative
*spectral functions of `Delta`*, equivalently entrywise-nonnegative covariant
kernels** (Perron–Frobenius), which is where the heat semigroup lives.

So `F/S < 0` does *not* require a grading. It requires only that the weight not be
a nonnegative function of the lattice Laplacian.

### 3.4 The breach in the campaign's own reading

```
PASS  C3a  r_detC = 1/2  <=>  F/S = 0   (NOT -1/5)     solution set = [0]
PASS  C3b  r_detC = 1    <=>  F/S = 1/4 (inside the positive range)  = [1/4]
```

And `F = 0` with `S > 0` is attained **exactly**, by a nonnegative spectral
function, with no grading at all. On `Z_3^3` the spectrum is `Delta_hat = 3j`
where `j` = number of nonzero momentum components; the `[111]` diagonal carries
only `j in {0,3}`, so the eigenvalue-3 shell misses the diagonal entirely:

```
PASS  E2a  N=3 spectrum = {0,3,6,9} with multiplicities (1,6,12,8)
PASS  E2b  eigenvalue 3 shell contains NO [111] diagonal momentum
PASS  E2c  f = 1{lambda=3} >= 0 gives S=6, F=0, both isotypic weights = 2 > 0
PASS  E2d  ==> a POSITIVE spectral weight attains r_detC = 1/2 EXACTLY
           [r_detC = 1/2, r_detR = 1]
```

Read the last line carefully. **One and the same positive spectral weight gives
`r = 1/2` under `det_C` and `r = 1` under `det_R`.** That is the cleanest
possible demonstration that positivity cannot decide the bit: it is not that
positivity picks the wrong horn, it is that positivity is *evaluated after* the
horn has been picked.

### 3.5 The invariant content of the obstruction

Stripping the reading out, what positivity actually proves is:

> For any weight in class (A)/(B), the trivial isotype receives **at least as much
> weight per real dimension as each nontrivial isotype**:
> `gamma_0/gamma_1 = (S + 2F)/(S - F) >= 1`, strict for `F > 0`, with equality
> only when the weight has no support on the `[111]` diagonal momenta.

That is a bound on the **metric factor alone**. By the retained_bounded
reading-neutrality theorem the metric factor alone does not give `r`. Therefore:

> **The positivity obstruction is orthogonal to the counting bit.** It constrains
> `gamma_0/gamma_1`; `r = (n_1/2) * (gamma_0/gamma_1)` with `n_1 in {1, 2}` the
> doublet mode count; positivity says nothing about `n_1`.

This is an independent instance of the EX2 factorization theorem, arrived at from
the spectral side. It is not an independent selector.

---

## 4. (c) The grading handle, found and turned into numbers

### 4.1 The handle, quoted

`docs/CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md:110-117`:

```text
:110  A static `J` is measure-neutral; what *could* force the count is a **grading**, not
:111  a complex structure — an object that promotes the operator to a mode-count. The
:112  sharpest named candidate is the **chirality-graded supertrace / equivariant index**
:113  (a counting in the representation ring, which genuinely promotes operator -> count),
:114  **conditional on the gated staggered-Dirac mass structure** and the
:115  operator-algebraic **sector-factorization** on the `M_2(C)`-per-site `(x) R[C_3]`
:116  algebra.
```

with the route table row at `:136`
(`| chirality-graded supertrace/index | a grading that promotes operator->count | the one route of the right shape; OPEN … |`)
and the parent open gate
`docs/SUPERTRACE_INDEX_HOLOMORPHIC_ROUTE_TO_KOIDE_R_HALF_OPEN_LEAD_NOTE_2026-06-04.md:63-65`:

```text
:63  5. The supertrace / equivariant index lives in the representation ring `R(G)` with **integer
:64     per-irrep multiplicities**; the plain heat-kernel trace gives **dimensions**. They are
:65     different functionals.
```

That last sentence is the honest form of the whole campaign question, and it
already tells you the answer to (c): the grading changes *which functional* you
take, i.e. it changes `n_1`, not `gamma_0/gamma_1`. The `-1/5` target is a
constraint on `gamma_0/gamma_1`. They are different slots.

### 4.2 The graded census is exhaustive, not a survey

The commutant of the `C_3` regular representation on `C^3` is spanned by the three
isotypic projectors, so **every** `C_3`-equivariant `Z_2` grading on the
generation carrier is `Gamma = eps_0 P_triv + eps_omega P_omega + eps_omegabar P_omegabar`
with `eps in {+-1}^3` — the 8 gradings the landed Kähler-Dirac note enumerates at
`docs/KOIDE_KAHLER_DIRAC_REALIZATION_GIVES_R_ONE_INDEX_ROUTE_CLOSED_BOUNDED_NO_GO_NOTE_2026-06-08.md:55-58`:

```text
:55  4. **The index route is closed on the realization.** For the physical L/R grading,
:56     `Str(ε e^{−tD²}) = 0` (`MM†, M†M` isospectral). Over all 8 `C₃`-equivariant `ℤ₂`
:57     gradings, the index is a signed **mode-count** in `{±1, ±3}` …
```

Rebuilt natively, at index normalization `h_pi = 1`:

```
  (e0,e1,e2)     S(h=1)     F(h=1)          F/S             real?
  (+1,+1,+1)     3          0               0               yes
  (+1,+1,-1)     1          1 + sqrt(3)i    1 + sqrt(3)i    no
  (+1,-1,+1)     1          1 - sqrt(3)i    1 - sqrt(3)i    no
  (+1,-1,-1)     -1         2               -2              yes
  (-1,+1,+1)     1          -2              -2              yes
  (-1,+1,-1)     -1         -1 + sqrt(3)i   1 - sqrt(3)i    no
  (-1,-1,+1)     -1         -1 - sqrt(3)i   1 + sqrt(3)i    no
  (-1,-1,-1)     -3         0               0               yes
```

```
PASS  F1a  index normalization: S in {+-1,+-3} exactly   [reproduces :56-57]
PASS  F1b  reality of F forces e1 = e2 (4 of the 8 survive)  real F/S = {0, -2}
PASS  F1c  NO landed equivariant Z_2 grading gives F/S = -1/5 at index normalization
```

**Attained set `{0, -2}`. `-1/5` is not in it.**

### 4.3 The general graded computation (any positive weight, any grading)

Let `h_0, h_1 > 0` be the ungraded isotypic weights (reality forces
`eps_omega h_omega = eps_omegabar h_omegabar`). Then

```text
S = eps_0 h_0 + 2 eps_1 h_1
F = eps_0 h_0 -   eps_1 h_1
F/S = (eps_0 h_0 - eps_1 h_1) / (eps_0 h_0 + 2 eps_1 h_1)
```

```
PASS  F2a  F/S = -1/5  <=>  eps1*h1 = 2*eps0*h0  (grading enters only via eps*h)
PASS  F2b  a GENUINE grading (eps1 = -eps0) needs lam = h1/h0 = -2 < 0: IMPOSSIBLE
PASS  F2c  so F/S=-1/5 forces eps1 = eps0, i.e. the grading is a global sign
           (ungraded), plus h1/h0 = 2 -- exactly what positivity of f(Delta) forbids
PASS  F7c  ... i.e. exactly the ungraded isotype-weight freedom the landed
           uniqueness no-go already leaves free
PASS  F7d  a grading on an EXTERNAL tensor factor (chirality, Cl(3) grade, site
           parity, gauge-center character) acts as eps_0 = eps_1, so it leaves
           F/S numerically unchanged: it is r-blind
```

**This is the theorem of §4.** A `Z_2` grading enters `F/S` only through the signed
products `eps_pi h_pi`. Requiring `F/S = -1/5` forces `eps_1 = eps_0` — the grading
degenerates to a global sign that cancels in the ratio — and then the condition is
just `h_1/h_0 = 2` on the *ungraded* weights. So:

> **The breach condition is grading-invariant.** No grading can supply it. What
> `F/S = -1/5` asks for is the ungraded isotypic-weight ratio `h_1/h_0 = 2`, which
> is precisely the free parameter that
> `KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21` already says is
> unforced. The "grading" handle and the `-1/5` target do not connect.

### 4.4 Named landed graded objects, one by one

**(i) The framework's own chiral grading `Gamma_chi`.**
`docs/KOIDE_GENERATION_ID_CL3_GRADE1_BRIDGE_NARROW_THEOREM_NOTE_2026-06-02.md:35`
names `Gamma_chi = (2/3) J - I` with eigenvalues `{+1,-1,-1}`. Since `J/3 = P_triv`,
this is exactly `P_triv - P_doublet`, i.e. `(eps_0, eps_1) = (+1, -1)`:

```
PASS  F6d1  Gamma_chi = (2/3)J - I = P_triv - P_doublet, eigenvalues (+1,-1,-1)
PASS  F6d2  Gamma_chi has (eps0,eps1) = (+1,-1) so F/S = (1+lam)/(1-2lam), lam = h1/h0 > 0
PASS  F6d3  its reachable F/S range is (-inf,-1/2) U (1,+inf): -1/5 sits strictly
            inside the EXCLUDED window, not near its edge
PASS  F6d4  positive-definiteness of the induced form needs F/S in (-1/2, 1); that
            window is DISJOINT from Gamma_chi's reachable set, so the chiral
            grading never induces a metric at all
PASS  F6d5  w_triv>0 <=> F/S > -1/2 and w_nontriv>0 <=> F/S < 1 (exact)
```

Two facts, both sharp: `-1/5` is not merely unreached, it lies strictly inside a
forbidden window with margin on both sides; and the `Gamma_chi`-graded weight is
**never a positive-definite form** for any positive `h_0, h_1`, so it is not a
candidate metric at all.

**(ii) The physical `L/R` chirality grading.**

```
PASS  F3a  M circulant  =>  M M^dag = M^dag M exactly (normal)
PASS  F3b  therefore Str(eps e^{-tD^2}) = 0 identically and the equivariant
           Str(eps e^{-tD^2} R) = 0 as well: S = F = 0, F/S undefined  [0/0]
```

I rebuilt `M = a I + b C + conj(b) C^2` and verified `M M^H = M^H M` exactly, which
is the reason behind the landed `:56` claim. Both `S` and `F` vanish identically —
`0/0`, not `-1/5`. EX3 `:448-449` noticed the `S = 0` half of this and read it as
"`S = 0` gives `r = -2`"; the equivariant half also vanishes, so the object is
simply undefined, not `-2`.

**(iii) The Kähler-Dirac / form-degree grading on `Lambda(C^3)`.**
`KOIDE_KAHLER_DIRAC…:45-46` records the Euler characteristic `1-3+3-1 = 0`.
The equivariant partner is the Lefschetz number: `chi_{Lambda^p}(R)` for the
3-cycle is `(1, 0, 0, +1)`.

```
PASS  F4a  Kahler-Dirac: Str = 1-3+3-1 = 0 (Euler characteristic)      S=0
PASS  F4b  Kahler-Dirac equivariant: Str(.R) = 1-0+0-1 = 0 (Lefschetz) F=0
PASS  F4c  so the Kahler-Dirac grading gives 0/0, not -1/5
```

**(iv) The staggered / site-parity grading `(-1)^{x1+x2+x3}` on `Z_N^3`.**

```
PASS  F5 N=2,4  staggered grading: Str(Delta^p) = 0 for p=0..3 (S=0 for all f)
PASS  F5 N=2,4  staggered grading: Str(Delta^p R) = 0 for p=0..3 (F=0)
PASS  F5c      N odd: (-1)^{x1+x2+x3} is not Z_N-periodic, so the staggered
               grading does not exist on Z_N^3 for odd N
```

`S` and `F` vanish to all polynomial orders, hence for every `f`: `0/0`.

**(v) Integrality — covers every index-type grading at once.**

```
PASS  F6a  for any grading whose supertrace is t-independent (McKean-Singer),
           S and F are indices: S in Z, F in Z[omega] (Eisenstein)
PASS  F6b  F/S = -1/5 requires 5 | S in Z[omega]; 5 == 2 mod 3 is INERT in Z[omega],
           so 1/5 is not an algebraic integer
PASS  F6c  the landed equivariant range is |S| <= 3, so 5 | S forces S = 0 and
           then F/S is undefined: -1/5 is UNREACHABLE by every landed index
```

The moment a grading is a genuine grading of a Dirac structure, McKean-Singer makes
both traces `t`-independent indices, `S in Z` and `F in Z[omega]`. `-1/5` needs a
denominator 5; `5 = 2 mod 3` is inert in the Eisenstein integers, so `1/5` is not an
algebraic integer, and `F/S = -1/5` requires `5 | S`. The landed range is
`|S| <= 3`. Impossible.

**(vi) What `-1/5` actually names.**

```
PASS  F7a  the F/S=-1/5 breach names the ordinary cone point diag(1,4,4) in
           coefficient coordinates            g0:g1 = 3/5 : 12/5 = 1:4
PASS  F7b  diag(1,4,4) is POSITIVE DEFINITE and C_3-invariant, i.e. an interior
           point of the landed uniqueness cone -- nothing exotic is required
```

`F/S = -1/5` is the cone point `diag(1,4,4)`. Not a grading, not an index, not a
supertrace — a perfectly ordinary positive-definite `C_3`-invariant form sitting in
the interior of the cone that `koide_frobenius_isotype_split_uniqueness` already
declares free. The only thing that cannot produce it is a nonnegative spectral
function of `Delta`.

---

## 5. (d) Verdict

**The spectral-weight route is closed — for a different and weaker reason than
EX3 proposed, and the closure does not close the counting bit.**

What is genuinely established, gated, and (to my reading) new:

1. **Class-(A)/(B) one-sided bound, exact and finite-scale.** For every
   nonnegative spectral function of the landed lattice Laplacian, the induced
   `C_3`-invariant form satisfies `gamma_0/gamma_1 = (S+2F)/(S-F) >= 1`, strictly
   `> 1` whenever the weight touches the `[111]` diagonal momenta, with equality
   iff `F = 0`. The trivial isotype is never *under*-weighted per real dimension.
2. **The `t -> 0, N -> oo` limit metric is exactly `diag(3,6,6)` = HS.** The
   positive-weight class flows *to* the Hilbert-Schmidt point, not away from it.
3. **The bound lives entirely in the metric slot.** By the retained_bounded
   reading-neutrality theorem the metric slot does not fix `r`. Hence the
   obstruction is `r`-silent: the same positive weight gives `r = 1/2` or `r = 1`
   depending on the reading, demonstrated by an exact instance (`f = 1{lambda=3}`
   on `Z_3^3`).
4. **`-1/5` is not an invariant target.** It is the `det_R` image of `r = 1/2`.
   Under the campaign's stated `det_C` convention the same target is `F/S = 0`,
   which is attained exactly by a positive weight with no grading.
5. **The grading handle cannot reach it in any reading.** `F/S = -1/5` forces
   `eps_1 = eps_0` (grading degenerates to a global sign) plus `h_1/h_0 = 2` on the
   ungraded weights. Every landed graded object computes to `{0, -2}`, `0/0`, or an
   indefinite form; integrality independently forbids denominator 5.

What is therefore **not** true, and should not be carried forward from EX3:

- "no positive functional of this class exists" — false; class (C) reaches `-1/5`
  exactly (gate E3b), class (B) reaches the `det_C` target exactly (gate E2d);
- "`r(t) = g_0/g_1 = (S+2F)/(S-F)`" — the two halves of that equation are
  different objects, differing by exactly the counting factor 2 (gates B4a–B4f);
- "`w_triv = 3S/5`, `w_nontriv = 6S/5`" — off by `3x`; correct values `S/5`, `2S/5`
  (gate C2b/C2c);
- "the flat point is the `t -> 0, N -> oo` limit" — the limit metric is the **HS**
  point (gates B5, B5-lim).

EX3 flagged this exact failure mode itself at `:528-533` ("Risk that §4 collapses
into known content… a reviewer reads `r(t) > 1` as a restatement of 'the
heat-kernel arrow flows `r -> 1`'") and argued the `-1/5` breach condition was
"the part that is unambiguously new". **The risk materialised and the defence does
not hold:** `r(t) > 1` *is* the landed heat-kernel-arrow sentence
(`CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md:97-98`)
with a finite-`t` sign attached, and the `-1/5` number is that same sentence read
through the count-twice convention. The genuinely new residue is items 1–2 above:
a strict finite-scale bound plus the identification of the limiting metric as HS.

### 5.1 Bearing on the EX1 / EX2 tension

My sector was not tasked with adjudicating it, but the computation lands squarely
on it and the evidence should be on the record.

**EX2 is supported on the decisive point, by an independent route.** The
positivity obstruction turns out to constrain only `gamma_0/gamma_1` — one factor
of EX2's `r = (metric ratio) x (mode-count ratio)` — and to be exactly silent on
the other. Gate E2d is a two-line proof of the redundancy: one positive weight,
two readings, `r = 1/2` and `r = 1`.

**EX1's associativity result, even granting it in full, does not close the bit.**
EX1's conclusion is `g_0/g_1 = 1/2`, i.e. the HS ray, i.e. `gamma_0 = gamma_1`.
Under the master relation `r = (n_1/2)(gamma_0/gamma_1)` that gives `r = n_1/2` —
the counting bit, undecided. This is not my inference against EX1; it is the
retained_bounded landed theorem
`FLAVOR_DOUBLET_METRIC_DEFAULT_IS_DETR_2026-06-02.md:16-19` stated verbatim:
`diag(3,6,6)` "is reading-neutral: it does not by itself choose whether the doublet
is counted as two real directions or one complex block". EX1's own concession that
the residual is a "counting exponent `s`" says the same thing. So EX1 and EX2 are
reconcilable: **EX1 fixes the metric factor, EX2 says only the product is physical,
and the surviving residual is the mode count.** My sector adds that the positivity
obstruction fixes (a bound on) the same metric factor and adds nothing to the
mode count.

Anyone proposing to fix `r` from a weight, positive or graded, should be required
to answer one question first: **which reading of the coefficient surface is your
`r`?** Until that is derived rather than adopted, every such computation is a
statement about `gamma_0/gamma_1` wearing the name `r`.

### 5.2 What I did not do

- No verdict, no status, no promotion, no ledger edit. Nothing committed or pushed.
- No axiom, no primitive, no new repo vocabulary. `det_C`/`det_R`, "reading",
  "isotype", "cone point", "grading", "index" are all existing repo terms used as
  the cited surfaces use them.
- No literature imported. Every object is rebuilt from the Lattice-axiom adjacency
  and the `C_3` circulant algebra. McKean-Singer, Perron-Frobenius, Lefschetz and
  the Eisenstein integers are named as comparators for classical facts I re-derive
  or use only structurally; none is a derivation input.
- I did not re-walk the AC_phi_lambda multiplicative bridge, the delta-pattern leg,
  or "chiral => r = 1/2".
- I did not attempt to decide the counting bit. §5.1 records where the evidence
  points; deciding it is not a spectral-weight question.

---

## 6. Probe index (all 123 gates)

```
BLOCK A  native rebuild of Tr(f(Delta) R^j) on Z_N^3, N = 2..5     22 gates
BLOCK B  isotypic weights, Gram factors, the two landed readings   23 gates
BLOCK C  one-sided bounds, breach numbers, exact instances         30 gates
BLOCK D  construction-mutation probes                              10 gates
BLOCK E  true scope of the positivity obstruction                   9 gates
BLOCK F  graded census (8 gradings, Gamma_chi, L/R, Kahler-Dirac,
         staggered, integrality, the diag(1,4,4) identification)   29 gates
                                                    TOTAL: PASS=123 FAIL=0
```
