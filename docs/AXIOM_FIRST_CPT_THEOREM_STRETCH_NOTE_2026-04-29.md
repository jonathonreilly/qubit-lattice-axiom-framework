# Axiom-First CPT Theorem (Stretch Attempt) on Cl(3) ⊗ Z^3

**Date:** 2026-04-29 (originally); 2026-05-10 (scope-split repair as
`audited_conditional`: separate the in-block fermion-sector CPT
identities from the deferred SU(3) Wilson-plaquette gauge-sector lift);
2026-06-11 (audit-failed repair: corrected composition — the ε sign
field is carried inside the map, landing at `M^*` — plus non-degenerate
runner blocks with explicit boundary conventions; axiom surface rebased
on [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md));
2026-06-12 (explicit-carrier rescope: the in-block theorem is a
self-contained finite-KS-matrix result, with the staggered realization
gate named only as non-load-bearing downstream context).
**Status:** source-note proposal — author-declared `bounded_theorem`;
effective status set only by the independent audit lane.
**Claim type:** bounded_theorem
**Loop:** `axiom-first-foundations`
**Cycle:** 4 (Route R4 — stretch attempt)
**Runner:** [`scripts/axiom_first_cpt_check.py`](../scripts/axiom_first_cpt_check.py)
(`TOTAL: PASS=119 FAIL=0`, deterministic, runtime a few seconds)
**Runner cache:** [`logs/runner-cache/axiom_first_cpt_check.txt`](../logs/runner-cache/axiom_first_cpt_check.txt)

## Authority disclaimer

This is a source-note proposal. Effective `effective_status` is generated
by the audit pipeline only after the independent audit lane reviews the
claim, dependency chain, and runner. The `claim_type`, scope, named
admissions, and bounded classification are author-proposed; the audit
lane has full authority to retag, narrow, or reject the proposal.

## Audit-failed repair (2026-06-11)

The 2026-06-11 audit failed this row on two findings; both are repaired
in this revision (the audit offered "narrow to the trivial `L = 2`
mass-only exhibit OR supply a corrected non-degenerate staggered CPT
construction, including boundary conventions and a runner that tests
nonzero KS hopping" — this revision takes the corrected-construction
route):

1. **(F-A) Composition gap — the chain ended at `M^†`, not `M^*`.**
   The prior eq. (8) composed `C`, `P`, `T` to
   `Θ_CPT M Θ_CPT^{-1} = M^†`, while the stated target (CPT2) is
   `= M^*`. For the real staggered `M = m + M_KS` these are
   **different matrices**: `M^† = M^T = m − M_KS` while
   `M^* = M = m + M_KS`. The prior text then invoked
   γ_5/ε-Hermiticity, but never composed it into the map — and
   ε-Hermiticity by itself does not bridge the gap. **Repair:** the
   corrected map carries the staggered sign field `ε(x)` **inside**
   the antiunitary operator. With `E = diag(ε)`,
   `Σ_PT = diag((−1)^{x_1+x_3})`, `R_b` the bond-centered full
   reflection, and `K` complex conjugation,

   ```text
       Θ_CPT := (E · Σ_PT · R_b) · K
   ```

   composes to `Θ_CPT M Θ_CPT^{-1} = E M^T E = M = M^*` exactly
   (§Construction below) — landing at the (CPT2) target with no
   appeal to an uncomposed Hermiticity identity.
2. **(F-B) Vacuous runner blocks.** The prior runner's canonical
   blocks were `L = 2` **periodic**, on which the forward and backward
   staggered hops coincide and cancel: `M_KS = 0` exactly, so the
   tested matrix was `m · I` and every identity held vacuously (the
   runner could not have detected (F-A)). **Repair:** the rewritten
   runner tests **nonzero KS hopping** on four non-degenerate blocks —
   `2⁴` all-antiperiodic, `4⁴` periodic, `4⁴` APBC-time, and a
   `4×2×4×2` mixed block — at masses `0.3` and `0.5`, keeps the
   degenerate `2⁴`-periodic block as an explicit falsification-leg
   witness, and adds falsifiers (no-sign-field, wrong-sign-field,
   wrong boundary convention).
3. **Boundary conventions (audit-demanded, now explicit).** The
   reflection in `Θ_CPT` is **bond-centered**: `r(x)_μ = L_μ − 1 −
   x_μ`. Bond-centered reflection maps boundary-crossing links to
   boundary-crossing links, so it is compatible with both periodic
   and antiperiodic wrap signs; it also remains non-trivial at
   `L = 2` (site-centered `x ↦ −x mod L` is the **identity map** at
   `L = 2` and is wrap-incompatible under APBC — both failure modes
   are exhibited as runner falsifiers). The sign field
   `σ_PT(x) = (−1)^{x_1+x_3}` absorbs the bond-centered η-parity
   flip `η_μ(r(x)) = (−1)^μ η_μ(x)` (valid for all even `L_μ`).
4. **Diagnostic corrected.** The prior "1D toy fails (residual 1.0):
   no spatial parity to absorb the time inversion" diagnostic was an
   artifact of the defective composition (F-A): under the corrected
   map the 1D time-circle identity closes **exactly** (runner
   [DIAG]). The Wilson-FERMION-term wall diagnostic stands unchanged
   (residual 1.0; pure staggered is the explicit carrier family).
5. **Axiom-surface rebase.** Citations move from the superseded
   `MINIMAL_AXIOMS_2026-05-03.md` to the current registered premise
   node [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)
   (its "Open Gates And Admissions Outside The Axioms" section lists
   the staggered-Dirac/`AC_phi_lambda` (display `AC_φλ`) realization
   gate and the `g_bare = 1` convention handling consumed here as
   context surfaces; the 2026-06-12 rescope below removes the
   realization gate as a load-bearing dependency of the in-block
   finite-matrix theorem).

## Explicit-carrier dependency-edge rescope (2026-06-12)

The audit-conditional blocker after the 2026-06-11 repair was not the
finite-matrix CPT algebra: the runner and the audit both found the
corrected `Theta_CPT M Theta_CPT^{-1} = M^*` chain to close on the
pure staggered kernel. The blocker was the dependency edge to the
unaudited staggered-Dirac realization gate, which is needed only if this
row claims that the framework has already selected the pure staggered
carrier as the physical matter operator.

This revision therefore narrows the load-bearing object to the explicit
finite KS carrier family defined in this note:

```text
Lambda = prod_mu Z_{L_mu},  L_mu even,
M = m I + M_KS,
(M_KS)_{x,x+mu} = +(1/2) eta_mu(x) wrap(x,x+mu),
(M_KS)_{x,x-mu} = -(1/2) eta_mu(x) wrap(x,x-mu),
eta_mu(x) = (-1)^(x_0 + ... + x_{mu-1}).
```

The theorem below is a bounded finite-matrix theorem about this
explicit family. It does not assert that Quantum + Lattice derive or
select this carrier. The staggered-Dirac realization gate remains
non-load-bearing downstream context for framework identification only;
there is intentionally no markdown dependency edge to that gate in this
source note. If a downstream row needs the statement "the framework
matter operator is this KS carrier", that downstream row still depends
on the realization-gate audit. If it needs only the finite-matrix CPT
identity once the KS family is supplied explicitly, this note supplies
that algebra directly.

The scope split of 2026-05-10 (fermion sector in-block; SU(3)
Wilson-plaquette gauge-sector lift deferred) is unchanged.

## Scope-split repair (2026-05-10)

The 2026-05-10 audit verdict (`audited_conditional`) recorded
`scope_too_broad` and asked to either (a) split the clean
pure-staggered fermion-sector CPT identities from the deferred SU(3)
Wilson-plaquette extension, or (b) close the gauge-sector operator-level
lift directly. The note had also been written against the April-15
`A_min` framing (A1, A2, A3 = staggered/Grassmann, A4 = canonical
normalization) which had been superseded by `MINIMAL_AXIOMS_2026-05-03.md`
(itself now superseded; the live citation is the current memo — see the
2026-06-11 repair section above; historical mention kept as plain text).

This 2026-05-10 repair takes path (a) and rebases the hypothesis set:

- **(R1) Authority rebase.** The hypothesis set was rebased on
  `MINIMAL_AXIOMS_2026-05-03.md` (historical; the 2026-06-11 revision
  rebases again onto the current memo). Only
  `A1` (Cl(3) per-site algebra) and `A2` (`Z^3` substrate) are framework
  axioms here. The finite KS carrier is now an explicit local matrix
  family defined in this note, not a consumed open-gate dependency. The
  proof is a bounded fermion-sector CPT identity on that supplied
  finite matrix family.
- **(R2) Scope split.** The in-block result is split explicitly into
  - **(I) Fermion-sector identities (CPT1)–(CPT5) on the explicit
    finite KS carrier**: closed in-block to machine precision on the
    `2³` pure-staggered runner blocks at masses `0.3` and `0.5` (runner
    `axiom_first_cpt_check.py`). This is the bounded fermion-sector
    theorem this note proposes for audit. *(2026-06-11 annotation:
    those `L = 2` periodic blocks were later found degenerate —
    `M_KS = 0` — and the composition defective; see the audit-failed
    repair section above for the corrected construction and the
    non-degenerate runner blocks.)*
  - **(II) SU(3) Wilson-plaquette gauge-sector CPT lift**: explicitly
    **deferred** as an open derivation target. The argument by
    inspection (`Re tr U_P` invariant under `U_P → U_P^*`) is recorded
    as a structural observation, not as an in-note operator-level
    theorem. The SU(3) representation-level CPT identity for the Wilson
    plaquette is the open gate; closing it requires a separate axiom-
    first lift on the canonical SU(3) representation.
- **(R3) Action-invariance scope narrowing.** The action-invariance
  identity (CPT3) of the original note was stated for the full
  canonical action `S = S_F + S_G`. After the split it is restated for
  `S_F` only on the explicit finite KS carrier; the `S_F + S_G`
  invariance is conditional on path (II) closing and is recorded in
  Honest status as an admitted-context corollary, not an in-block
  theorem.

## Scope (post-split, 2026-05-10)

The downstream package `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` invokes
a "CPT-even" assumption when restricting the scalar observable
generator `W` to depend only on `|Z|` rather than on the fermionic phase
of `Z`. This note proposes a bounded fermion-sector identity that is
the natural in-block step toward discharging that assumption: it
constructs an explicit antiunitary involution `Θ_CPT` on the **explicit
finite KS Grassmann kernel family** defined here and
verifies, both algebraically and numerically on non-degenerate
pure-staggered blocks, that

```text
    Θ_CPT  M  Θ_CPT^{-1}   =   M^*                                    (1)
```

where `M` is the explicit KS matrix (no Wilson fermion term). The
in-block conclusion is then a bounded
fermion-sector CPT identity (CPT1)–(CPT5) on the explicit KS carrier
family.

**Out of scope (post-split).** Discharge of the OBSERVABLE_PRINCIPLE
"CPT-even" premise on the **full canonical action** `S_F + S_G` (i.e.
including the SU(3) Wilson-plaquette gauge sector at the operator level)
is **not** in scope on this note. That step requires the deferred
SU(3) Wilson-plaquette CPT lift named in (R2)(II); when that gate
closes, the discharge of the "CPT-even" premise lifts to the full
canonical action by composition.

## Hypothesis set used (post-split 2026-05-10; rebased 2026-06-11; rescope 2026-06-12)

The proof is stated over the current framework baseline
[`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) plus
the explicit finite KS carrier family below. The in-block theorem has
no load-bearing dependency on the staggered-Dirac realization gate.

**Framework baseline context (current):**

- **Quantum (one qubit per site / `Cl(3)` local algebra)** supplies only
  the onsite algebraic backdrop. It does not supply the Grassmann
  carrier, the KS phases, charge conjugation, or any framework
  selection of this finite matrix family.
- **Lattice (`Z^3`)** supplies only the site/adjacency backdrop. The
  finite even block, periodic/APBC wrap signs, and bond-centered
  reflection convention used by this theorem are supplied explicitly as
  part of the finite-KS carrier/boundary data below.

**Explicit supplied finite-KS carrier (load-bearing for this row):**

- **Pure KS finite matrix family.** On the finite even block
  `Λ = Π_μ Z_{L_μ}`, with per-direction periodic or antiperiodic wrap
  signs, define

  ```text
      S_F[χ̄, χ]  =  Σ_{x,y}  χ̄_x  M_xy  χ_y,
      M = m · I + M_KS,
      (M_KS)_{x, x±μ̂} = ± (1/2) η_μ(x).
  ```

  `M_KS` is real and antisymmetric; `M = m + M_KS` is therefore real
  with `M^† = M^T = -M_KS + m`. There is **no Wilson fermion term**.
  This explicit family is the only carrier input consumed by the
  finite-matrix CPT theorem. The source note intentionally does not
  claim that this row derives the physical staggered realization from
  the framework baseline.

**Non-load-bearing context inputs:**

- The staggered-Dirac realization gate remains the downstream framework
  identification surface for rows that need to know that the physical
  matter operator is this KS carrier. That gate is named here only as
  context and is not a load-bearing dependency of the finite-matrix CPT
  theorem. No markdown dependency edge to that gate is present in this
  source note.

- **`g_bare_canonical_normalization_gate`** (only for the Wilson
  plaquette structural observation; **not** load-bearing for the
  in-block fermion-sector identities (CPT1)–(CPT5)). Per
  [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)
  ("Open Gates And Admissions Outside The Axioms": `g_bare = 1`
  convention handling). The in-block claim of
  this note is **independent** of this gate; the gate is named only for
  the deferred (R2)(II) Wilson-plaquette gauge-sector lift.

**Out-of-scope ingredients (deferred upstream gates):**

- **SU(3) Wilson plaquette operator-level CPT identity.** The Wilson
  plaquette `S_G = β Σ_P Re[1 - (1/N_c) tr U_P]` is structurally
  CPT-compatible by inspection on the Re-trace; the explicit operator-
  level lift to the canonical SU(3) representation is **not** closed in
  this note (see scope-split repair (R2)(II) above). The SU(3)
  Wilson-plaquette CPT lift is therefore a deferred open derivation
  target, not an in-block theorem of this note.

## Construction of `Θ_CPT` (corrected 2026-06-11)

Work on the finite 4D block `Λ = Z_{L_0} × Z_{L_1} × Z_{L_2} ×
Z_{L_3}` (all `L_μ` even), KS phases `η_μ(x) = (-1)^{x_0+…+x_{μ-1}}`,
per-direction periodic or antiperiodic wrap signs, and the explicit
1-component KS carrier `M = m·I + M_KS` (real; `M_KS`
antisymmetric). Write `Θ_CPT = C · Θ_PT · K` with:

### 1. Charge conjugation `C` (carries the ε sign field)

The standard 1-component staggered charge conjugation:

```text
    C : χ_x  ↦  ε(x) · χ̄_x^T,    χ̄_x  ↦  -ε(x) · χ_x^T,             (2)
    ε(x) = (-1)^{x_0+x_1+x_2+x_3}.
```

On the bilinear kernel (after the Grassmann reorder), `C` acts as

```text
    C :  M  ↦  E M^T E   =   M,        E := diag(ε(x)),               (3)
```

where the last equality is exact on the staggered carrier:
`E M_KS E = -M_KS` (every hop connects sites of opposite ε-parity),
so `E M^T E = E (m - M_KS) E = m + M_KS = M`. Identity (3) is the
transpose form of ε-Hermiticity `E M E = M^†` and is the step the
2026-05-10 revision invoked but never composed into the map.

### 2. Combined reflection `Θ_PT` (bond-centered; boundary-explicit)

The full PT reflection is **bond-centered**,

```text
    r(x)_μ = L_μ - 1 - x_μ      (every direction μ),                  (4)
    Θ_PT : χ_x  ↦  σ_PT(x) · χ_{r(x)},    σ_PT(x) = (-1)^{x_1+x_3}.
```

Boundary convention (load-bearing): bond-centered reflection maps
boundary-crossing links to boundary-crossing links, so the identity
below holds **uniformly for periodic and antiperiodic wrap signs**;
it is also non-trivial at `L = 2` (the site-centered map `x ↦ -x mod
L` is the identity at `L = 2` and maps crossing links to non-crossing
links under APBC — both failure modes are runner falsifiers). Two
exact lemmas:

```text
    η_μ(r(x)) = (-1)^μ · η_μ(x)          (L_μ even),                  (5)
    σ_PT(x) · σ_PT(x ± μ̂) = +1 (μ ∈ {0,2}),  -1 (μ ∈ {1,3}),
```

so `σ_PT` absorbs the alternating η-parity flip of (5), while the
reflection itself maps each forward hop onto the reflected backward
hop. On the kernel:

```text
    Θ_PT :  M  ↦  Σ_PT R_b M R_b^{-1} Σ_PT  =  M^T,                   (6)
    Σ_PT := diag(σ_PT(x)),  R_b := the permutation of r.
```

### 3. Antiunitarity `K`

`K` is complex conjugation (`i ↦ -i`). On the real staggered carrier
`K M K^{-1} = M^* = M`; antiunitarity is what makes `Θ_CPT` a CPT
(not just a unitary) symmetry and is load-bearing for the
Theta_CPT-odd observable-vanishing corollary (CPT5).

### 4. Composition (corrected chain — lands at `M^*`)

`Θ_CPT := (E Σ_PT R_b) · K` is antiunitary, and

```text
    Θ_CPT M Θ_CPT^{-1} = (E Σ_PT R_b) M^* (E Σ_PT R_b)^{-1}
                       = E (Σ_PT R_b M R_b^{-1} Σ_PT) E      [M real]
                       = E M^T E                              [by (6)]
                       = M                                    [by (3)]
                       = M^*                                  [M real] (8)
```

— exactly the (CPT2) target. The involution property is analytic:
`r ∘ r = id`, `σ_PT(r(x)) = σ_PT(x)` and `ε(r(x)) = ε(x)` for even
`L_μ`, so `(E Σ_PT R_b)² = I` and `Θ_CPT² = id`. The 2026-05-10
revision's chain instead ended at `M^†` (its composition omitted the
ε sign field from the map); for the real staggered carrier
`M^† = m - M_KS ≠ m + M_KS = M^*`, which is the (F-A) defect this
revision repairs.

The action `S_F = χ̄ M χ` is then `Θ_CPT`-invariant,

```text
    S_F[Θ_CPT(χ̄, χ)]   =   S_F[χ̄, χ]                                  (9)
```

(after integrating the phases against the Grassmann measure; the
key identity is that `det(M) = det(M^T) = (det(M^*))^* = det(M)*`,
so `det(M)` is real on the canonical staggered surface — same fact
that supports the strong-CP retention).

For the gauge sector, the Wilson plaquette `S_G = β Σ_P Re[1 -
(1/N_c) tr U_P]` is structurally CPT-compatible by inspection (`Re tr
U_P` is unchanged under `U_P → U_P^*`). The operator-level lift on the
canonical SU(3) representation is the **deferred** (R2)(II) gate
above; it is **not** closed in this note. The structural Re-trace
observation is recorded for orientation only and is not a load-bearing
step of any in-block theorem below.

Conditional on the deferred (R2)(II) gate closing, `Θ_CPT` lifts to an
antiunitary operator on the physical Hilbert space `H_phys` (built via
the reflection-positivity reconstruction sibling note) that commutes
with the transfer matrix `T` and reverses the sign of all
Theta_CPT-odd local observables. This conditional corollary is **not**
an in-block theorem of this note.

## Statement (post-split 2026-05-10; corrected 2026-06-11)

Under the explicit finite KS carrier family defined in "Hypothesis set
used", on the finite block `Λ = Π_μ Z_{L_μ}` (all `L_μ` even, any
per-direction periodic/antiperiodic wrap signs), the in-block bounded
fermion-sector theorem is:

**(CPT1) Existence.** The antiunitary operator
`Θ_CPT = (E Σ_PT R_b) K = C · Θ_PT · K`
defined by (2), (4) is an involution: `Θ_CPT² = id`.

**(CPT2) Operator-level identity.**

```text
    Θ_CPT  M  Θ_CPT^{-1}   =   M^*                                    (10)
```

for `M` the explicit KS matrix (no Wilson fermion term).

**(CPT3) Fermion-sector action invariance** (scope-narrowed, post-split).

```text
    S_F   is invariant under  Θ_CPT.                                  (11)
```

The full-action invariance `S_F + S_G is invariant under Θ_CPT` is
**not** asserted as an in-block theorem; it lifts conditionally on the
deferred (R2)(II) Wilson-plaquette gauge-sector CPT gate closing.

**(CPT4) Reality of the fermion-sector determinant.**

```text
    det(M) ∈ R                                                        (12)
```

so the fermion-sector contribution to the partition function is real.
The full-`Z` reality, including the gauge-sector measure, is
conditional on the deferred (R2)(II) gate.

**(CPT5) Theta_CPT-odd fermion-sector observable vanishing.** For any
local observable O with Theta_CPT(O) = -O (Theta_CPT-odd), <O>_F = 0
in the fermion-sector ensemble. The bridge from CP-odd (in the C·P
sense) to Theta_CPT-odd is NOT supplied here; consumers needing the
CP-odd form require that separate bridge. The same statement on the
full ensemble is conditional on the deferred (R2)(II) gate.

## Honest status (corrected 2026-06-11)

**Bounded fermion-sector theorem on the explicit finite KS carrier;
SU(3) Wilson-plaquette gauge-sector lift deferred.**

(CPT1)–(CPT5) on the **fermion sector** of the explicit finite KS
carrier (pure staggered, no Wilson fermion term) are closed in-block
to exact zero residual on four **non-degenerate** runner blocks —
`2⁴` all-antiperiodic, `4⁴` periodic, `4⁴` APBC-time, `4×2×4×2`
mixed — at masses `0.3` and `0.5`, with nonzero KS hopping asserted
on every block (`max |M_KS| ∈ {0.5, 1.0}`), per the rewritten runner
(`TOTAL: PASS=119 FAIL=0`).

**What is closed in-block (explicit finite KS carrier).**

| Identity | Status | Residual on the non-degenerate blocks |
|----------|--------|---------------------------------------|
| (CPT1) `Θ_CPT² = id`                                     | closed in-block | 0.0e+00 |
| (CPT2) `Θ_CPT M Θ_CPT^{-1} = M^*` (corrected chain)      | closed in-block | 0.0e+00 |
| (CPT3) `S_F` invariance under `Θ_CPT` (fermion-sector)   | closed in-block (from CPT2) | n/a |
| (CPT4) `det(M) ∈ R`                                      | closed in-block | `Im det(M) = 0.0e+00` |
| (CPT5) Theta_CPT-odd kernel `tr(A_odd M^{-1}) = 0` (computed) | closed in-block | ≤ 1.8e-14 in cache; runner threshold < 1e-10 |
| `ε`-Hermiticity `ε M ε = M^†`                            | closed in-block | 0.0e+00 |
| `C` kernel identity `E M^T E = M`                        | closed in-block | 0.0e+00 |
| `Θ_PT` reflection identity `→ M^T` (bond-centered)       | closed in-block | 0.0e+00 |

**Falsification legs (runner).** The `2⁴`-periodic block is degenerate
(`M_KS = 0` exactly; the old runner's surface — on it even the
no-sign-field reflection "passes", which is why the prior revision's
defect went undetected). On the non-degenerate blocks: the reflection
WITHOUT the sign field fails, a WRONG sign field (`(−1)^{x_2}`) fails,
and the SITE-centered reflection fails under APBC (the bond-centered
boundary convention is load-bearing).

**Diagnostic (updated 2026-06-11).**

- 1D time circle `L = 4`: under the **corrected** map the TC identity
  closes **exactly** (residual `0.0`). The prior revision's "1D fails,
  residual 1.0 — no spatial parity to absorb the time inversion"
  diagnostic was an artifact of the defective composition (F-A), not
  a parity wall.
- Staggered + Wilson *fermion* term: `ε`-Hermiticity residual `1.0`
  (non-zero). The Wilson fermion term breaks the `ε`-as-`γ_5` chain.
  This is **not** in scope: this row's explicit finite KS carrier is
  pure staggered. (The Wilson term in the deferred (R2)(II) gate is a
  gauge-sector plaquette, not a fermion Wilson term.)

**What is *not* closed in-block (deferred upstream gate).**

- **(R2)(II) SU(3) Wilson-plaquette operator-level CPT lift.** Full
  algebraic-general CPT identity for the SU(3) Wilson plaquette
  `Re[1 - (1/N_c) tr U_P]` at the operator level is the deferred
  upstream gate; it requires the SU(3) representation-level CPT
  identity. The structural Re-trace observation is recorded for
  orientation only and is not a load-bearing step of any in-block
  theorem above. The full-action invariance `S_F + S_G is invariant
  under Θ_CPT`, the full-`Z` reality, and the discharge of the
  OBSERVABLE_PRINCIPLE "CPT-even" premise on the full canonical
  action all lift conditionally on this gate closing.

**Promotion path.** This row's finite-matrix CPT theorem no longer
waits on the full staggered realization gate for its in-block algebra.
Rows that need framework identification of the KS carrier still wait on
that separate gate. The full-action CPT application still waits on the
deferred (R2)(II) Wilson-plaquette gauge-sector lift. Retagging and
downstream propagation remain audit-lane decisions.

## Non-load-bearing realization-gate context (2026-06-12)

The realization gate, canonical parent filename
`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`, is relevant only
for downstream framework identification of the KS carrier. This CPT
packet does not consume that authority as a source dependency.

1. **The algebra is standalone.** The load-bearing in-block algebra is
   the finite-matrix package (CPT1)–(CPT4): ε-Hermiticity, the
   bond-centered reflection with its sign field, the composite
   involution, and the corrected `M^*` identity. The runner verifies
   these identities with explicit matrices on non-degenerate staggered
   blocks and falsification legs for the missing sign field, wrong
   sign field, and wrong boundary convention.
2. **What the realization gate would carry.** The realization gate
   carries the separate identification of `M = m + M_KS` as the
   framework matter operator on the physical pure-staggered Grassmann
   surface. It does not supply, and this note does not claim, the
   finite-matrix identities listed in point 1.
3. **No dependency edge.** The gate is deliberately not linked in
   markdown form from this source note. Future framework-identification
   consumers may cite the gate directly; this row does not.
4. **No status assertion.** This section records the source boundary only.
   Status authority: independent audit lane only. The note asserts no
   `effective_status` and predicts no audit outcome.

## Corollaries (downstream tools)

C1. *Partial discharge of the `CPT-even` assumption in downstream
`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`.*
The fermion-sector contribution to the scalar observable generator
`W` need only depend on `|Z|` because the fermion-sector determinant
is real, by (CPT4). Discharge of the "CPT-even" premise on the full
canonical action (including the gauge-sector Wilson-plaquette
contribution) is conditional on the deferred (R2)(II) gate.

C2. *Fermion-sector compatibility with strong-CP retention.* The
content of (CPT4) restated in the `θ` language gives `θ_F^{eff} = 0`
on the fermion-sector determinant; the full `θ_eff = 0` row of the
package's strong-CP retention is conditional on the deferred (R2)(II)
gate.

C3. *Reuse for any fermion-sector neutral-current / Theta_CPT-odd lane.*
Any future lane that needs to assert "the fermion-sector ensemble
on the explicit KS carrier has zero expectation of a
Theta_CPT-odd local observable" can cite (CPT5). The bridge from
CP-odd (in the C·P sense) to Theta_CPT-odd is not supplied here; lanes
needing the CP-odd form require that separate bridge. The full-ensemble
version is conditional on (R2)(II).

## Changelog

- 2026-06-12: Rescoped the in-block theorem to the explicit finite KS
  matrix family and moved the staggered realization gate to
  non-load-bearing context only; removed the markdown dependency edge
  to the gate and added runner guards for the source boundary.
- 2026-06-11 #2: Added an earlier Tier-A routing discussion for the
  then-admitted `staggered_dirac_realization_gate` carrier input and
  narrowed (CPT5) plus corollary C3 from CP-odd observables to
  Theta_CPT-odd fermion-sector observables. The 2026-06-12 rescope
  supersedes the routing discussion by making the gate non-load-bearing
  context for this row.

## Citations

- Current axiom memo:
  [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md)
  (supersedes the April-15 `A_min` framing the original note used and
  the 2026-05-03 memo the 2026-05-10 revision rebased on).
- Prior cycles in this loop:
  - [`AXIOM_FIRST_SPIN_STATISTICS_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_SPIN_STATISTICS_THEOREM_NOTE_2026-04-29.md)
  - [`AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md)
  - [`AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md`](AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md)
- Target of partial discharge:
  `OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`
  (`audit_status: audited_conditional`, `claim_type: bounded_theorem`).
- Related assumption ledger: [`ASSUMPTION_DERIVATION_LEDGER.md`](ASSUMPTION_DERIVATION_LEDGER.md)
  (`θ_eff = 0` row), cited as related, not as in-note closure for the
  deferred (R2)(II) gate.
