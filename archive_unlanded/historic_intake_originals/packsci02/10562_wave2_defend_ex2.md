# WAVE 2 — steelman and stress-test of EX2 (`r = (g_0/g_1)(w_1/w_0)`, only-the-product-physical)

Date: 2026-07-24. Base: `origin/main` @ `62826882ac` (fetched at session start).
Scope: campaign report only. No repo science surface was created or edited, nothing
committed or pushed, no audit verdict set or predicted, no axiom or primitive proposed,
no new repo vocabulary proposed.

**Verification.** Everything load-bearing below was rebuilt natively and exactly in sympy
(exact rationals/radicals/symbols; no float is ever an input). Scratch runner:
`/private/tmp/claude-502/-Users-jonBridger-Toy-Physics--claude-worktrees-quirky-wiles-92e3b4/66008b76-8d97-42b5-b1e1-4e60c09bb2e9/scratchpad/wave2_ex2_stress.py`
— **SCORECARD PASS=83 FAIL=0**, including 12 construction-mutation probes (A7, B6, B6b,
C2b, C5, D9, E2b, F3c, F7, F7b, G4b, H3b). I did not trust either exercise sector's
arithmetic; where I reproduce it I say so, and I reproduce EX1's central residual by a
*different* route before comparing.

---

## 0. Framework refresher — surfaces actually read before any conclusion

- `docs/MINIMAL_AXIOMS_2026-06-29.md` **in full** (Lattice / Qubit / Admissibility /
  Record; the Qualification; "Relation To The 2026-06-05 Record Wording"; "Open Gates
  Outside The Axioms").
- `docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md` in full (rules 1–6 and the
  three current approved primitives).
- `docs/audit/data/axiom_premise_nodes.json` in full (all four `canonical_ids` and every
  node `note`).
- Source notes of the primitives invoked or ruled out: `docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md`
  (invoked negatively, §4.5); `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md` and
  `docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md` (checked out of chain — `r` and `Q`
  are dimensionless and static).
- Wall surfaces: `GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05.md`,
  `RECORD_GENERATION_READOUT_TWO_SECTORS_2026-06-05.md`,
  `FLAVOR_DOUBLET_METRIC_DEFAULT_IS_DETR_2026-06-02.md`,
  `FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02.md`,
  `FLAVOR_R_HALF_IS_A_STATIONARY_POINT_NOT_FORCED_2026-06-02.md`,
  `KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md`,
  `KOIDE_R_HALF_NOT_SYMMETRY_PROTECTED_DYNAMICAL_NORM_BALANCE_NARROW_NO_GO_NOTE_2026-06-04.md`,
  `CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md`,
  `CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md`, plus the
  live sharded ledger under `docs/audit/data/ledger/**`.
- The two exercise reports I am adjudicating: `.claude/science/exercises/koide-counting-bit-20260724/ex1_assumptions_ledger.md`
  and `.../ex2_first_principles_reduction.md`, and `CAMPAIGN.md`.

---

## 1. Bottom line — four verdicts

| task | claim under test | verdict |
|---|---|---|
| **(a)** | the one-parameter redundancy that makes "only the product physical" | **FICTITIOUS as a symmetry.** No transformation of framework objects realizes it. The automorphism group of the framework's structure on the carrier is the *finite* group `S_3`, and it acts **trivially** on `g_0/g_1`. EX2's mechanism collapses; only the trivial "a product does not determine its factors" survives. |
| **(b)** | `Γ = diag(λ,μ,μ)` in the commutant, transitive on `r`, breaking list `= {algebra, trace, HS metric}` | **group facts TRUE and reproduced; the consequence clause REFUTED.** The positive-spectrum cone also breaks `Γ` — and it is algebra content — and it **bounds the product**: `r < 1` strictly. So the "one object" does *not* fix "only the metric factor". |
| **(c)** | `w_1/w_0` is genuinely free; a selector must be a measure with atoms | **EX2 IS RIGHT — and I sharpen it from an absence-of-theorem into an exact computation.** Record additivity leaves the ratio with a full one-parameter freedom (exact dimension count). Worse for the lane: EX2's own escape hatch is **circular** — *both* horns are cardinalities of landed framework-supplied finite sets. |
| **(d)** | does EX1's associativity pin fix the product or one factor? | **ONE FACTOR — and it was never the free one.** Pushed to consistency (one object supplying *both* factors, which is exactly EX2's requirement for a selector) the same bridge delivers **`r = 1`, not `r = 1/2`.** |

**The single decisive sentence.** EX1's associativity result is *correct arithmetic* (I
reproduce its exact residual by an independent route) but it pins the form to the trace,
and the trace's own weighting of the two blocks is `Tr P_0 : Tr P_1 = 1 : 2`, which is the
`r = 1` horn — so the one new positive result in the campaign, taken to its own natural
conclusion, argues **against** Koide, not for it.

**A framing correction that dissolves half the stated tension.** EX1 and EX2 have **no
arithmetic conflict**. EX1's residual is the counting exponent `s`; EX2's is
`ν := w_1/w_0`; and `ν = 2^s` exactly (gate B10). EX1's own §7 consequence 2 already says
"It does not close `r`". The tension is between two *framings* of one agreed residual, and
both framings are partly wrong.

---

## 2. The objects, defined natively (not as labels)

### 2.1 The carrier

`C` is the `3x3` cyclic shift, `C^3 = I`, `C != I` (A1). The framework's mass-operator
surface is

```text
W  :=  Herm(circ_3)  =  { H = a I + b C + conj(b) C^2 :  a in R,  b in C },   dim_R W = 3.
```

`H` is Hermitian and `[H, C] = 0` (A2, A2b); the commutant of `C` in `M_3(C)` is exactly the
circulants, 3 free complex parameters (A3).

**Two canonical coordinate systems, and the fact that decides everything below.**

```text
coefficient coordinates :  (a, Re b, Im b)
eigen-slot coordinates  :  lam_k = a + b w^{-k} + conj(b) w^{k} = a + 2 Re(b w^{-k}),  k = 0,1,2
```

with `w` a primitive cube root of unity (A0). Eigenvector residuals are **exactly zero**
(A4.0–A4.2); the `lam_k` are real (A4b); and `H |-> (lam_0, lam_1, lam_2)` is a linear
isomorphism `W -> R^3` with `det = 6*sqrt(3) != 0` (A5). Hermitian circulants commute (A6),
and in eigen-slot coordinates the **matrix product is componentwise** (A6b.0–A6b.2):

```text
(H H')  <->  (lam_0 lam'_0,  lam_1 lam'_1,  lam_2 lam'_2).
```

So `W` is the **real commutative algebra `R x R x R`**, and its three slots are the three
mass slots. This is the framework object; every structural claim below is about it.

### 2.2 Which group actually cuts the cone (and a correction to EX1's flag)

- **The generation shift acts trivially on the coefficients:** `Ad_C(H) = H` for every
  circulant (gate A7, a mutation probe). EX1's E2 is right that the runner at
  `scripts/frontier_koide_real_rep_block_count_permitted_not_forced_2026_05_30.py:57-59` is
  mis-labelled.
- **The group that does act** is conjugation by the clock `D = diag(1, w, w^2)`, giving
  `b -> w b` (A8).
- **But EX1's further inference is wrong.** EX1 (`ex1_assumptions_ledger.md:111`) calls the
  clock "a *different group*, not supplied anywhere as a framework symmetry". It is
  supplied. On eigen-slots the clock is **exactly the cyclic relabelling of the three mass
  slots**, `lam_k -> lam_{k-1}` (gate A9). The framework privileges no site and no
  possibility (`docs/MINIMAL_AXIOMS_2026-06-29.md:39-41`, `:50-51`), and the three
  generation patterns are cycled by the lattice's own order-3 rotation
  (`GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05.md:36-39`). Requiring the weighting rule not
  to privilege one of the three leptons **is** clock invariance. So the cone is safe; only
  its label was wrong. This matters: EX1's flag, read literally, would have knocked out the
  whole cone.

### 2.3 `g_0`, `g_1` — the metric factor

The clock-invariant symmetric forms on `(a, Re b, Im b)` are **exactly 2-parameter** (B5),
and the cone is exactly `diag(g_0, g_1, g_1)` (B5b); adding the `K`/CPT reflection
`diag(1,1,-1)` changes nothing (B5c). Non-vacuity: with no group the space is
6-dimensional (B6); with the `K` reflection alone, 4-dimensional (B6b). Define

```text
E_0(H) := G restricted to the singlet  =  g_0 a^2
E_1(H) := G restricted to the doublet  =  g_1 |b|^2
```

Both are basis-free (values of one form on two invariant subspaces). The Hilbert–Schmidt
point is fixed by

```text
Tr(H^dag H) = Tr(H^2) = 3 a^2 + 6 |b|^2        (B2)     =>  (g_0, g_1) = (3, 6),
gamma := g_0/g_1 = 1/2                          (B8).
```

`gamma` is canonical, **not** basis-dependent: `a` and `b` are the circulant coefficients of
`H`, so `E_0 = 3a^2` and `E_1 = 6|b|^2` are frame-free statements. (EX1's E4 remark that
"the same HS form reads `diag(1,1,1)` in the HS-orthonormal frame" is true of the matrix but
not of `gamma`, because rewriting the frame also rewrites `r`.)

### 2.4 `w_0`, `w_1` — the mode-count factor, and the factorization

The balance rule is one equation on `W`:

```text
E_0 / w_0  =  E_1 / w_1
       =>   r := |b|^2 / a^2  =  (g_0/g_1) * (w_1/w_0)  =  gamma * nu,   nu := w_1/w_0.   (B7)
```

and the readout is `Q = Tr(H^2)/(Tr H)^2 = 1/3 + (2/3) r` at generic phase (B1, B3). The four
metric x weight cells reproduce exactly `1/2, 1, 1, 2` (B9) — including EX2's unnamed third
value `r = 2`. And the landed dial is the same object: `r(s) = 2^{s-1}` is
`gamma = 1/2, nu = 2^s` (B10; `GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05.md:80-94`).

**So the factorization is real as an identity.** `EX1`'s `s` and `EX2`'s `nu` are the same
residual: `nu = 2^s`.

---

## 3. (a) THE REDUNDANCY IS FICTITIOUS

EX2 §4 claims a "one-parameter redundancy … it can be moved freely between 'the metric' and
'the partition/mode count', and only the product is physical"
(`ex2_first_principles_reduction.md:157-161`). The task is to exhibit the transformation on
**framework objects** or declare it fictitious. I declare it fictitious, with a theorem.

**What is true (and trivial).** The *numeric* map `(gamma, nu) -> (t*gamma, nu/t)` preserves
`r` (C1). This is the statement that a product does not determine its factors. It is true of
any factorization of any number and carries no physics.

**What is false.** There is no transformation of framework objects that realizes it.
`W` carries three framework structures — the product, the unit `I`, the adjoint — and:

```text
unital algebra ENDOmorphisms of W  =  pullbacks along maps {0,1,2} -> {0,1,2}  =  3^3 = 27
the INVERTIBLE ones, Aut(W)        =  the 6 slot permutations, S_3                    (C2)
dropping the unit requirement does NOT enlarge Aut(W): still exactly 6               (C2b, MUT)
every element of Aut(W) fixes the HS form exactly, hence fixes gamma                  (C3)
```

and EX2's own `Γ` is not in it:

```text
Gamma_{lambda,mu} := lambda P_0 + mu P_1  is an algebra map  <=>  lambda = mu = 1      (C4)
[MUT] Gamma_{2,1} does move the metric ratio, so C4 is not vacuous                     (C5)
```

**Theorem (gated, C2–C6).** *The group of transformations of `W` preserving the framework's
structure is the finite group `S_3` — the relabelling of the three mass slots — and it acts
trivially on `gamma`. Hence no framework-object transformation rescales `gamma`, and a
fortiori none rescales `gamma` and `nu` inversely. There is no continuous group at all.*

**Consequence.** `gamma` and `nu` are **not two halves of one gauge-dependent split**. They
are two separately meaningful framework quantities: `gamma` is a property of a form on `W`
(and is independently pinned — twice, see §5), `nu` is a property of a balance rule. The
correct statement is not "only the product is physical, so fixing one factor fixes nothing";
it is the much weaker "**the product has two independently-sourced factors, and one of them
is still unsourced**". EX2's diagnosis of prior lens failures — "each lens fixed one
gauge-dependent factor while the compensating factor stayed free"
(`ex2_first_principles_reduction.md:172-173`) — is therefore mis-stated: nothing
*compensated*; the lenses simply never touched `nu`.

**EX2 conflates two different objects.** `Γ` is not the redundancy. `Γ` **moves** `r`
(D2, D3) and **breaks** the algebra (C4). It is a *sweep*, not a symmetry. A sweep whose
generator is not a framework symmetry proves nothing about physicality.

---

## 4. (b) THE COMMUTANT THEOREM: half true, its consequence clause refuted

### 4.1 What I reproduce and confirm

```text
Gamma = diag(lambda, mu, mu) commutes with the clock rep                              (D1)
Gamma commutes with the K/CPT reflection                                              (D1b)
Gamma^T diag(g_0,g_1,g_1) Gamma = diag(l^2 g_0, m^2 g_1, m^2 g_1)                     (D2)
=> the metric ratio transforms as gamma -> (lambda/mu)^2 gamma, transitively on (0,oo) (D3)
```

All four are exactly as EX2 states them (`ex2_first_principles_reduction.md:210-217`). The
one-line invariance theorem that follows — *a module invariant cannot be a non-constant
function of a `Γ`-transitive coordinate* — is **correct and is EX2's real contribution**. It
subsumes the Wave-1 Frobenius–Schur census as a corollary, and I do not dispute it.

### 4.2 What is refuted: "the complete `Γ`-breaking list is `{algebra, trace, HS metric}`, all one object, fixing only the metric factor"

The **positive-spectrum surface** breaks `Γ`, and EX2's seven-item census
(`ex2_first_principles_reduction.md:233-241`) does not contain it. Exact witness (D9, MUT):

```text
(a, b) = (1, 1/2)      ->  spectrum ( 2,  1/2,  1/2 )    all positive
Gamma_{1,3} applied    ->  (a, b) = (1, 3/2)
                       ->  spectrum ( 4, -1/2, -1/2 )    NOT positive
```

And it is not a fourth independent object — it *is* algebra content: the positive cone of
`W` is exactly the set of squares `{y o y}` (H1). So EX2's "all one object" survives. **Its
consequence clause does not.** The same object also constrains the **product**:

```text
e_1 = Tr H              = 3a                                                          (D4)
e_2 = sum_{j<k} lam_j lam_k = 3(a^2 - |b|^2)                                          (D5)
e_3 = det H             = a^3 + b^3 + conj(b)^3 - 3 a |b|^2                           (D6)
```

If all three `lam_k > 0` then `e_2 > 0` as a sum of positive products, hence

```text
3(a^2 - |b|^2) > 0   =>   |b|^2 < a^2   =>   r < 1     strictly.                      (D7)
```

At `r = 1` we get `e_2 = 0`; with all `lam_k >= 0` every pairwise product must then vanish,
so at most one eigenvalue is nonzero — the spectrum is `(3a, 0, 0)` (D8, D8b). Meanwhile
`r = 1/2` is **interior**: at `arg b = 0` the spectrum is `(1+sqrt 2, 1-sqrt2/2, 1-sqrt2/2)`,
all positive (D11).

This reproduces landed content the census missed —
`CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md:41` (L8: "at `r=1` positivity
forces … the boundary spectrum `[0,0,3a]`") and
`FLAVOR_R_HALF_IS_A_STATIONARY_POINT_NOT_FORCED_2026-06-02.md:31` ("`r=1` | maximal
hierarchy, two massless") — and it has a consequence neither surface draws:

> **The two horns are not two interior points of one cone.** `r = 1/2` is interior to the
> positive-spectrum surface; `r = 1` is on its boundary and is reachable with three distinct
> masses only on the signed-`sqrt(m)` branch. The "binary" is a choice between an interior
> point and a boundary/sign-indefinite configuration.

**Net for (b):** the group facts stand, the invariance theorem stands, the completeness
claim as *stated* ("fixing only the metric factor") is **false**, and the correction cuts
*toward* `r = 1/2` — the only place in this whole report where anything does.

---

## 5. (c) THE DECISIVE QUESTION — Record additivity pointed straight at `w_1/w_0`

The campaign brief says this has apparently never been done. I did it. It is computable and
the answer is exact.

### 5.1 The two candidate atom sets, built natively

The `K`/CPT orbits of the three `C_3` characters are exactly (E1, E1b)

```text
{ chi_0 }   and   { chi_1, chi_2 },      i.e. the quotient map is  3 atoms -> 2 atoms,
                                          with fibre sizes (1, 2).
```

This reproduces `RECORD_GENERATION_READOUT_TWO_SECTORS_2026-06-05.md:22-34` natively.

### 5.2 The computation: additivity constrains the ratio by exactly nothing

Take the Boolean algebra of subsets of the record alphabet and impose the axiom's own two
clauses — `I(empty) = 0` and `I(S u T) = I(S) + I(T)` for **every** disjoint pair
(`docs/MINIMAL_AXIOMS_2026-06-29.md:70-72`). Solving the full constraint system:

```text
dim { finitely additive I }  on a 1-atom alphabet  =  1
                             on a 2-atom alphabet  =  2        (E2)
                             on a 3-atom alphabet  =  3        (E2b, MUT)
```

So on the 2-letter record alphabet the additive readouts form a 2-dimensional space; modulo
the overall scale that `Q` divides out, **exactly one free parameter survives, and that
parameter is `nu`.** Additivity imposes **zero** constraints on it. Additivity determines
`I` on unions *given* its values on atoms; the ratio of those values is precisely what it
never touches.

### 5.3 No no-privilege clause can rescue it

Equality `w_0 = w_1` would need a symmetry exchanging the two letters. There is none: the
commutant of the clock action is block-diagonal,

```text
commutant = [[p0, 0, 0], [0, p8, -p7], [0, p7, p8]]                                    (E3)
```

so no module map mixes singlet and doublet — they have different dimensions. This
independently reproduces `KOIDE_R_HALF_NOT_SYMMETRY_PROTECTED_..._2026-06-04.md:46-48` ("no
unitary singlet/doublet swap exists"). The Lattice/Qubit no-privilege clauses apply to
**sites** and **possibilities**, not to inequivalent record letters.

### 5.4 EX2's own escape hatch is circular — the sharpest result in this section

EX2 §6 proposes the decidable obligation **(MODE-COUNT-IS-A-CARDINALITY)**: "does the
framework supply a finite SET whose cardinality is the isotype weight?"
(`ex2_first_principles_reduction.md:278-284`). I discharge it — and it does **not**
discriminate. **Both** candidate weights are cardinalities of landed framework-supplied
finite sets, and they are the fibre counts on the two sides of one quotient map:

| weight | the finite set | landed source | `r` |
|---|---|---|---|
| `(1, 2)` | the **pre-quotient** set: characters `{chi_0}`, `{chi_1, chi_2}`; equivalently the eigen-slots, the group-algebra basis `{I, C, C^2}`, or the isotype real dimensions | `RECORD_GENERATION_READOUT_TWO_SECTORS_2026-06-05.md:59-63` derives "dimensions 1 and 2" | **1** (E4) |
| `(1, 1)` | the **post-quotient** set: the two `K`/CPT-orbit record letters | same note, `:28-30` ("the realized-outcome alphabet … has exactly two letters") | **1/2** (E4b) |

So exhibiting a set does not decide the bit; it **reproduces the bit verbatim** as *"does
the weighting live upstream or downstream of the `K`/CPT quotient?"* (E5). EX2's proposed
falsifier is well-posed and answerable, and its answer is "both, therefore still free".

The same bit appears a third time in the landed entropy functionals, and I reproduce both
stationary points exactly:

```text
2-sector (block) entropy      stationary exactly at  r = 1/2                            (E6)
3-mode (per-dimension) entropy stationary exactly at  r = 1                             (E7)
```

matching the honest caveat at `FLAVOR_R_HALF_IS_A_STATIONARY_POINT_NOT_FORCED_2026-06-02.md:42-47`.
Every dress of the bit is the same 3-vs-2 atom choice.

### 5.5 And the axiom's registered scope closes the door explicitly

This is not a gap in our knowledge; it is a declared exclusion, in two places.

1. `docs/audit/data/axiom_premise_nodes.json:25` (the registered `minimal_axioms` node)
   states Record "still supplies no context-selection rule, formation rule (which admissible
   possibility a new record locks, at which site, **with what weight**, or at what rate),
   **weighting, normalization**, probability, … **K/CPT structure, central-sector
   decomposition**, …". `PRIMITIVE_REGISTRY_CHECK.md:13-16` rule 5 forbids granting more
   than the source note declares, naming "weighting rule, normalization rule" explicitly.
   **Any derivation of `nu` from Record would be over-granting a registered premise.**

2. Sharper, and apparently unnoticed by the lane: the **current** Record axiom contains no
   `K`/CPT clause at all. `docs/MINIMAL_AXIOMS_2026-06-29.md:137-142` records that the
   *superseded* 2026-06-05 wording "gave a `K`/CPT orbit reading", and `:152-155` rules:

   > "`K`/CPT orbit structure, central-sector decomposition, and any sector generation rule
   > are downstream readout-context content, not generic axiom content."

   But `RECORD_GENERATION_READOUT_TWO_SECTORS_2026-06-05.md:91` cites exactly
   `MINIMAL_AXIOMS_2026-06-05.md` for its Record clause, and
   `GENERATION_WEIGHT_DIAL_STRUCTURE_2026-06-05.md:44-47` carries the same "the record names
   only the realized `K`/CPT orbit" wording. **The only axiom-adjacent route to the 2-letter
   alphabet — and hence to `w = (1,1)` and `r = 1/2` — runs through a superseded axiom memo,
   and the current foundation explicitly demotes it to supplied readout context.** Under the
   post-reset foundation the count-once horn has *strictly less* support than it had before
   2026-06-29. (Reported as a live surface-consistency issue; I set no status and this is not
   an audit judgement. Live ledger, queried from `docs/audit/data/ledger/**`:
   `record_generation_readout_two_sectors_2026-06-05` = `bounded_theorem` / `unaudited`;
   `generation_weight_dial_structure_2026-06-05` = `positive_theorem` / `unaudited`.)

### 5.6 Verdict on (c)

**`w_1/w_0` is genuinely free.** Not "we have not found the theorem" — an exact dimension
count says additivity constrains it by nothing (E2), no symmetry can equate the letters
(E3), the cardinality criterion is satisfied by both horns (E4/E4b), and the registered
axiom scope excludes weighting, normalization, `K`/CPT structure and central-sector
decomposition from Record's content. **EX2's central negative survives every attack I could
mount, and is stronger than EX2 stated it.**

---

## 6. (d) WHAT EX1's ASSOCIATIVITY PIN ACTUALLY FIXES — the crux

### 6.1 EX1's arithmetic is correct — verified twice, independently

**Route 1 (mine, in eigen-slot coordinates).** With the product componentwise, write
`B(x,y) = sum_{jk} M_{jk} x_j y_k`. Then

```text
B(uv, t) - B(v, ut)  =  sum_{jk} M_{jk} ( u_j - u_k ) v_j t_k
```

vanishes for all `u, v, t` iff `M_{jk}(u_j - u_k) = 0` for all `j,k,u`, i.e. iff **`M` is
diagonal** (F1). Adding clock invariance (cyclic permutation of the slots) forces all
diagonal entries equal (F2):

```text
associativity  +  clock invariance   =>   B(x,y) = c * sum_j lam_j lam'_j = c * Tr(H H').
```

Exactly one free scale. So the associative ray **is** Hilbert–Schmidt, i.e. `gamma = 1/2`.

**Route 2 (EX1's, in coefficient coordinates), reproduced exactly.** Imposing
`<uv,t> = <v, u^dag t>` on `g_0 a_u a_v + g_1 (b_u . b_v)` over `W` with the actual matrix
product gives the residual

```text
<uv,t> - <v,u^dag t>  =  (2 g_0 - g_1) * ( a_t (b_u . b_v)  -  a_v (b_u . b_t) )        (F3)
```

vanishing identically iff `g_1 = 2 g_0` (F3b), and **not** vanishing at the flat point
`(1,1)` (F3c, MUT). This is EX1's `ex1_assumptions_ledger.md:150-152` **verbatim**, obtained
from a different construction. **EX1's central computation is right.** My dispute is
entirely about what it means.

### 6.2 It fixes one factor, and provably cannot fix the other

The associativity condition is a condition on the **form** alone. Its full symbol set is
`{M_0..M_8, a_u, a_v, a_t, b_u1, b_u2, b_v1, b_v2, b_t1, b_t2, g_0, g_1}` — it contains
neither `w_0` nor `w_1` (F4). And with `G` pinned to HS, both weightings remain available
and give different answers (F4b):

```text
G = HS,  w = (1,1)  =>  r = 1/2
G = HS,  w = (1,2)  =>  r = 1
```

**So the associativity pin fixes `gamma`, not the product.** Formally: `r = gamma * nu` with
`gamma` now `1/2` and `nu` still ranging over `(0, oo)` — bounded to `nu < 2` by §4.2's
positivity, but otherwise untouched.

Moreover the factor it fixes was **never the free one**. EX1's own census finds `rho = 1` —
i.e. `gamma = 1/2` — in *all seven* landed `r`-derivations
(`ex1_assumptions_ledger.md:253`, with the E5 row `:114` listing them), and
`KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21.md:89-90`
asks for exactly this ("an independent authority that fixes the scalar/traceless
isotype-weight ratio to `1`"). The lemma is a genuine **repair of a no-go's scope** — it
shows that no-go foreclosed a family whose non-HS members were never used — and it is worth
having. It is not information about `r`.

### 6.3 THE STING: the same bridge, applied to both factors, gives `r = 1`

EX2's structural corollary is that a selector must be "a single framework object that
supplies the metric **and** the mode set at once"
(`ex2_first_principles_reduction.md:256-259`). EX1's bridge is exactly such an object — the
weighting form is `phi(x^dag y)` for a **linear readout functional `phi` on the observable
algebra** (`ex1_assumptions_ledger.md:186-191`). So apply it consistently. It self-destructs:

1. **The associative form is itself a counting measure on three atoms.** By F1/F2 the form
   is `c * sum_j lam_j lam'_j`: an orthogonal decomposition of `W` into **three equally
   weighted one-dimensional pieces**, the mass slots. Their isotype content is
   `Tr P_0 : Tr P_1 = 1 : 2` (F5).
2. **The same invariance requirement pins the functional to the trace.** The clock-invariant
   linear functionals on `W` are exactly `phi = c_0 * a = (c_0/3) Tr H` (H2). The one bridge
   supplies both the form *and* the functional, and the functional is the trace.
3. **The trace's own weights on the two blocks are `(1, 2)`.** `Tr P_0 = 1`, `Tr P_1 = 2`
   (G4, H3), so `r = (1/2)(2/1) = 1`.
4. **The `(1,1)` weighting is not the value of any linear functional at the two projectors**
   — it assigns `1` to a rank-2 projector (G4b, H3b, MUT).
5. **The measure form of the same statement.** The Gaussian with HS covariance has
   `<c_j^2> = 1` per orthonormal slot (F6), hence `<E_0> : <E_1> = 1 : 2` exactly and its
   mean sits at `r = 1` (F6b).

All five are gated, and all five are corroborated by landed content the campaign has not
connected to EX1's lemma:

- `FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02.md:38-42` — "The genuine
  Born/tracial max-entropy state `rho=I/3` weights the blocks by **dimension**
  (`Tr P_0:Tr P_1 = 1:2`) -> **r=1 -> Q=1**. `r=1/2` needs equal power per block … a
  *separate* input."
- `CHARGED_LEPTON_VALUE_REDUCES_TO_ONE_COUNTING_BIT_SYNTHESIS_NOTE_2026-06-05.md:79-80` —
  "The framework's over-determined default is `Q=1`; the charged-lepton target `Q=2/3` is
  the natively-available-but-unforced block-count reading."

> **Answer to (d), exactly.** EX1's associativity result fixes **one factor**, not the
> product. If it is allowed to supply only the metric factor, the bit is exactly where it
> was. If it is allowed to supply both — which is what "closing the bit" requires — it
> supplies `w = (1,2)` and delivers **`r = 1`**, closing the question **against** Koide.
> Either way it does not deliver `r = 1/2`. This is the crux of the campaign and it is
> negative.

### 6.4 The residual premise EX1 named is the real load, and it is undischarged

EX1 states it honestly (`ex1_assumptions_ledger.md:186-191`): Record gives additivity over
**disjoint records**, not linearity over **algebra elements**. §5.2 shows why that gap is
not bridgeable by additivity alone (the additive-readout space is 2-dimensional with a free
ratio), and §5.5 shows the registered node excludes exactly this. So the associativity
lemma's own premise is currently supplied, not derived — which is why its `r = 1` sting is a
*conditional* sting, not a closure against Koide either.

---

## 7. What survives of EX2, precisely

| EX2 claim | status after this stress-test |
|---|---|
| `r = (g_0/g_1)(w_1/w_0)` is an exact identity | **CONFIRMED** (B7), and identical to the landed dial with `nu = 2^s` (B10) |
| one-parameter redundancy, only the product physical | **REFUTED as a symmetry** (C2–C6). Survives only as "a product does not determine its factors" |
| `Γ = diag(λ,μ,μ)` in the commutant, sweeps `r`, fixes the module | **CONFIRMED** (D1–D3) |
| module invariants cannot select `r` (the one-line theorem) | **CONFIRMED**, and it is EX2's real contribution |
| the complete `Γ`-breaking list is `{algebra, trace, HS metric}`, all one object | **"one object" CONFIRMED** (positivity is algebra content, H1) |
| … "fixing only the metric factor" | **REFUTED** (D5, D7–D11): the same object bounds the product to `r < 1` and puts `r = 1` on the boundary |
| `w_1/w_0` is free; the framework supplies nothing for it | **CONFIRMED and STRENGTHENED** (E2, E3, §5.5) |
| a selector must be a measure with atoms, not an invariant | **CONFIRMED** — and §6.3 shows the framework's own measure-with-atoms gives `r = 1` |
| (MODE-COUNT-IS-A-CARDINALITY) is a decidable, discriminating obligation | **REFUTED as discriminating** (E4/E4b/E5): both horns are cardinalities of landed sets, on the two sides of one quotient |
| F-1: the registered foundation already classifies `r` as non-derivable | **CONFIRMED as text** — `REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md:88-93`, item 4: "dial settings (`r = 0, 1/2, 1`) are sector data, never forced". I add that the primitive's ban on "averaging over alternatives" and on typicality (`:26-30`) independently forecloses the max-entropy/Gaussian route that is the only object that *would* have delivered a value |

---

## 8. Findings against landed content (reported, not adjudicated)

**(W-1) The landed `r = 1` arithmetic is over-determined and frame-dependent.**
`FLAVOR_DOUBLET_METRIC_DEFAULT_IS_DETR_2026-06-02.md:35-37` writes the per-real-direction
reading as

```text
3a^2 = 6(Re b)^2 = 6(Im b)^2   ->   |b|^2 = a^2  ->  r = 1  ->  Q = 1
```

That is **two** independent equations. It fixes `r = 1` **and** `|Re b| = |Im b|`, i.e.
`arg b = pi/4 mod pi/2` (G1) — a phase claim the note neither makes nor wants (`:42-43`
calls these "conditional readings"). Worse, the locus is **not clock-`Z_3` invariant**: at
`a = 1`, `arg b = pi/4`, `(Re b)^2 - (Im b)^2 = 0`, but after `b -> w b` it is `sqrt(3)/2`
(G2). The `r = 1/2` reading `3a^2 = 6|b|^2` **is** invariant (G2b). The invariant repair is
the per-dimension balance `3a^2/1 = 6|b|^2/2`, which still gives `r = 1` (G2c) — so the
value is unaffected and the note's conclusion stands; only its displayed condition needs
narrowing.

**(W-2) The landed `r = 1` locus, as written, sits on the signed-`sqrt(m)` branch.** At
`a = 1`, `b = e^{i pi/4}` the spectrum is
`(1+sqrt2,  1-sqrt2/2+sqrt6/2,  1-sqrt6/2-sqrt2/2) ~ (2.414, 1.518, -0.932)` — one
**negative** eigenvalue (G3). This is the same object as
`CHARGED_LEPTON_VALUE_REDUCES_..._2026-06-05.md:82-85`'s asserted four-way equivalence
("the Dirac-vs-Majorana / signed-`sqrt(m)` choice … one counting bit on different tensor
factors"). Combined with §4.2 it upgrades that assertion, for this leg, from *asserted* to
*computed*: `r = 1` with three distinct masses **requires** a sign flip. (Wave 1 already
flagged the 6-vs-12-generator leg of the same four-way equivalence as `r`-neutral —
`CAMPAIGN.md:146-153`. Two of four legs are now non-generic; the equivalence needs
re-derivation, as Wave 1 said.)

**(W-3) EX1's E2 flag over-reaches.** The cone-cutting group is mis-labelled in
`scripts/frontier_koide_real_rep_block_count_permitted_not_forced_2026_05_30.py:57-59`, but it
is **not** an unsupplied group: on eigen-slots it is the relabelling of the three mass slots
(A9). EX1's `ex1_assumptions_ledger.md:111` ("not supplied anywhere as a framework
symmetry") would, if taken literally, void the cone. It should not be.

**(W-4) The `K`/CPT-orbit Record reading is pre-reset wording.** §5.5 item 2. Two landed
notes carry the 2026-06-05 Record clause; the 2026-06-29 axiom explicitly demotes it. Per
the standing memory rule I do **not** quote the pre-reset wording as current; I note only
that two surfaces cite the superseded memo for a load-bearing clause.

---

## 9. Where this leaves the binary (campaign-facing)

The bit is **not** symmetric, and that is the campaign-relevant deliverable of this wave.
Each horn is blocked by a different structure:

```text
r = 1     is what EVERY measure-with-atoms in the framework delivers
          (trace; tracial state rho = I/3; HS-covariance Gaussian; counting measure on the
          three slots / characters / group elements / matrix entries; per-mode entropy)
          -- but it lies on the BOUNDARY of the positive-spectrum surface: with all
          lam_k > 0 it is unreachable (r < 1 strictly), and with three distinct masses it
          requires a negative sqrt(m).

r = 1/2   is INTERIOR and non-degenerate, and is the stationary point of the 2-sector
          balance/entropy -- but its weighting (1,1) is the value of NO linear functional
          on the observable algebra, is not the trace of any projector, and exists only
          downstream of the K/CPT quotient, which the current axiom explicitly names as
          readout-context content rather than axiom content.
```

So a closing theorem must do exactly one of two things, and both are named honestly:

- **(i)** derive the `K`/CPT quotient as the *physical mode set* — i.e. show that the
  doublet's two real directions are one physical mode and not two — from something that is
  not itself the count. This is the fermionic/Berezin `det_C`-vs-`det_R` fork, and Wave 1
  found the polarization is handed to that machinery at declaration time
  (`CAMPAIGN.md:161-166`); or
- **(ii)** accept the `r = 1` horn, which requires a signed-`sqrt(m)` or degenerate spectrum.

Neither is an invariant. EX2's shape conclusion is therefore right, and this wave's
contribution is to say *which* object of that shape the framework actually has — the trace —
and that it points at `r = 1`.

**A sharp negative is a success (campaign rule 7).** The honest reading of Wave 2 is that
the campaign's Wave-2 target as written in `CAMPAIGN.md:177-183` ("derive `g_0/g_1` from the
landed corner action's own kinetic normalization … is it `3:6` or `1:1`?") is **mis-posed**:
`3:6` and `1:1` are not two candidate values of one quantity. `3:6` is `gamma` (now pinned,
by two independent routes, and never in dispute); `1:1` is `nu` (never touched by any
metric argument). Any kinetic normalization that is a readout-induced form **must** give
`3:6` — that is algebra, not dynamics — so Wave 2 as specified would produce a
convention-laundering false positive. This independently confirms EX1's warning at
`ex1_assumptions_ledger.md:174-179`, which is the one place EX1 and I agree completely.

---

## 10. Honest boundary — what this wave did NOT establish

- I did **not** derive `r`, and I did not adopt a horn. No lepton mass, PDG value, or fit was
  consulted or used.
- I did **not** prove `r` is underivable. §5 proves Record additivity cannot fix `nu` and
  that the cardinality criterion cannot discriminate; it does not quantify over all possible
  future physical inputs. The `Γ`-invariance theorem covers module-level structures only;
  measure-bearing structures remain the live class, exactly as EX2 said.
- The `r = 1` sting of §6.3 is **conditional** on EX1's readout-functional bridge, which
  §6.4 shows is undischarged. It is an argument about what that bridge *would* deliver, not
  a derivation of `r = 1`.
- The positivity results (§4.2) are conditional on the all-positive `sqrt(m)` branch, which
  is itself one dress of the disputed bit (`CHARGED_LEPTON_VALUE_REDUCES_..._2026-06-05.md:74-75`).
  I flag this rather than lean on it: §4.2 is a genuine constraint *given* sign-definiteness,
  and sign-definiteness is not free.
- Everything upstream — the `hw=1` carrier (`ledger: decoration`), the species bridge, and
  `m_k = lam_k^2` (`CHARGED_LEPTON_KOIDE_VALUE_FULL_CHAIN_OF_CUSTODY_2026-06-02.md:11-12`,
  `:94`) — was taken as supplied and not re-verified. All of it is upstream of `r`.
- Nothing here proposes repo vocabulary. "Metric factor", "mode-count factor", "atom set",
  "pre/post-quotient" are descriptions in this report only; the landed native phrases are
  *equal-channel-energy* and *2-sector equipartition*.
- I set, predicted and estimated no audit verdict. The ledger statuses in §5.5 are a live
  query, reported as data.

---

## 11. Verification appendix

Scratch runner (not landed, exact sympy throughout):
`/private/tmp/claude-502/-Users-jonBridger-Toy-Physics--claude-worktrees-quirky-wiles-92e3b4/66008b76-8d97-42b5-b1e1-4e60c09bb2e9/scratchpad/wave2_ex2_stress.py`
— **SCORECARD PASS=83 FAIL=0**.

Blocks: **A** carrier algebra, both coordinate systems, eigen-residuals, the componentwise
product, and which group acts (with the `Ad_C = id` mutation). **B** trace identities, the
`Q` line at generic phase, the invariant-form cone with two mutation probes, the
factorization solve, the four cells, and the dial identification. **C** the redundancy test:
the algebra endomorphism/automorphism count, the triviality of `Aut` on `gamma`, and
`Γ ∩ Aut = {id}` with its non-vacuity mutation. **D** the `Γ` commutant facts, the
elementary symmetric functions, the exact `r < 1` bound, the `(3a,0,0)` boundary, and the
positive-cone mutation witness. **E** the `K`/CPT orbit structure, the additive-readout
dimension count with a 1-and-3-atom mutation, the clock commutant, the two cardinalities, and
both entropy stationary points. **F** the associativity pin by two independent routes,
EX1's residual reproduced verbatim with a flat-point mutation, the `w`-blindness of the
condition, the 3-atom structure of the associative form, the HS-Gaussian expectation, and the
`Z_2` mutation in which the bit disappears. **G** the two corrections to the landed `r = 1`
arithmetic and the tracial-state weights. **H** positivity as algebra content, the
clock-invariant functionals, and the `r = 1` sting.

Per campaign rule 3 every claimed constancy is gated by a construction-mutation probe, not
an assertion probe: A7, B6, B6b, C2b, C5, D9, E2b, F3c, F7, F7b, G4b, H3b. Per rule 4 this
report's verification content was written from the runner output.
