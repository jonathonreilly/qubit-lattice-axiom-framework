# Koide Q = 2/3 Extremal-Principle Bridge — Assumptions Audit

**Date:** 2026-05-28
**Claim type:** audit / scratch (NOT a theorem, NOT a closure)
**Status authority:** none. This note imports no axiom, no comparator, no
convention, and promotes no row. It is an assumptions audit of the
existing retained/open Koide surfaces, plus candidate new directions
flagged explicitly as speculative.
**Scope boundary:** local working note. No new primitive is asserted as
derived. Where this note proposes a direction, it states the residual gap
and its circularity status honestly.

---

## 0. The object under audit

The Koide invariant for charged leptons is

```text
Q = (sum m_i) / (sum sqrt(m_i))^2 = 2/3   (empirically, to ~1e-5).
```

The retained algebraic package reduces this, via the `C_3`
circulant/character surface and the kappa block-total Frobenius surface,
to a single statement about the circulant operator
`H = a I + b C + bbar C^2` on `Herm_circ(3)`:

```text
Q_alg(lambda) = (3 a^2 + 6 |b|^2) / (9 a^2) = 1/3 + (2/3) (|b|^2 / a^2).
```

So `Q = 2/3  <=>  |b|^2/a^2 = 1/2  <=>  a^2 = 2 |b|^2  <=>  kappa := a^2/|b|^2 = 2`,
equivalently `E_+ = E_perp` where `E_+ = 3 a^2` (trivial isotype) and
`E_perp = 6 |b|^2` (doublet isotype).

**Decisive structural fact (verified against the runner).** `Q_alg` is a
*monotone* function of the ratio `|b|^2/a^2`. There is no extremum of `Q`
itself. The "extremal principle" is entirely a statement about a
*separately chosen* functional `S` on `(E_+, E_perp)` whose extremum is
*declared* to land at `E_+ = E_perp`. The primary runner
`scripts/koide_q_two_thirds_frobenius_extremum_runner.py` **imports**
`a^2 = 2 |b|^2` as a hypothesis and checks only the downstream algebra; it
never verifies that any principle selects it. The gap the bridge note
(`KOIDE_Q_TWO_THIRDS_FROBENIUS_EXTREMUM_BRIDGE_BOUNDED_NOTE_2026-05-25.md`
§4) flags is therefore the entire load-bearing content.

---

## 1. The full assumption chain (every link)

Listing every assumption between the framework and `Q = 2/3`, load-bearing
ones marked **[LB]**.

| # | Assumption | Status on main |
|---|---|---|
| A0 | **[LB]** The physical packet is produced by *extremizing a scalar functional* of `H`. (The extremal-principle frame itself.) | unforced; frame choice |
| A1 | **[LB]** The mass operator is a `C_3`-circulant Hermitian `H = aI + bC + b̄C²` on a `d=3` generation space. | `d=3` retained_bounded; circulant from `Z_3` |
| A2 | The eigenvalues are sqrt-masses, `λ_k = √m_k` (Brannen/Foot). | NOT claimed by bridge; unaudited import |
| A3 | **[LB]** The functional is a *log of Frobenius block-norms*, `S = μ log E_+ + ν log E_perp`. | Frobenius *inner product* retained as unique Ad-invariant pairing; the *functional* (log, block-norm) unpinned |
| A4 | **[LB]** The weights are `(μ,ν) = (1,1)` (per-isotype / multiplicity). | **OPEN derivation gap.** Nothing retained selects it. `κ = 2μ/ν` ⇒ this is the whole answer. |
| A5 | **[LB]** Extremize at fixed sum `E_+ + E_perp = E_tot`. | constraint choice; entangled with A3/A4 |
| A6 | **[LB]** The extremal eigenvalue vector lies in a positive chamber so `λ_k = √m_k ≥ 0` and `Q_alg` = physical `Q`. | chamber-limited; positive-spectrum readout bridge missing (bridge §3) |

`Q = 2/3` follows by exact rational algebra **only after A0–A6 are all
granted.** The retained narrow theorems supply the algebra connecting A1+A3
to `Q_alg`; they supply *none* of A0, A4, A5, A6, and explicitly disown A2
and A4.

### The six no-go theorems (what is already excluded)

The canonical six (per `SCALAR_SELECTOR_REMAINING_OPEN_IMPORTS_2026-04-20`
§1 and `KOIDE_Q23_OH_COVARIANCE_NOGO_NOTE_2026-04-22` §6) each rule out a
*known mechanism* for forcing the cone point — i.e. for supplying A4/A5
from physics:

1. **`Z_3`-invariance alone** — fixes the circulant algebra but leaves the
   whole `(a,b)` family invariant; pins nothing.
2. **Sectoral universality** — same law across species is consistent with
   non-Koide shared values.
3. **Color-sector correction** — retained color `Z_3 ⊂ SU(3)_c` is
   lepton-blind.
4. **Anomaly-forced cross-species** — anomaly counts are integer; cannot
   fix a continuous amplitude ratio.
5. **SU(2) gauge exchange mixing** — doublet mixing does not force the
   generation-space point.
6. **Observable-principle character symmetry** — the weighted `Z_3`
   character-source kernel is diagonal; every selected basis axis gives
   `Q = 1`, not `2/3`.

The single escape hatch all six leave open: a **retained `Z³` scalar
potential whose physical minimum lands on the cone**. The retained `V(m)`
has its stationary point at `m_V ≈ −0.433`, not the cone point
`m_* ≈ −1.161` (an honest gap; cf. probe 20, `..._VM_CUBIC_EXTREMA_...`).
This audit treats the six as the boundary condition: any new direction
must either supply the scalar-potential forcing or change the *frame* (A0)
so the no-gos no longer apply.

---

## 2. "What if this is wrong?" — link by link

### A0 — what if there is no extremal principle?
`Q = 2/3 ⟺ E_+ = E_perp` is an **equipartition/equality** condition, not
intrinsically an extremum. The extremal framing is one of several ways to
*produce* the equality, and it is the one that introduces the free weight
parameter (A4). Dropping A0 in favor of a direct equality law removes A3,
A4, A5 in one stroke. → **New direction ND1.**

### A1 — what if the carrier is not `Herm_circ(3)`?
The `Z_3`-equivariant anticommuting no-go already shows a single-`R³`-factor
chirality identification collapses `H` to `0`. The *standard multi-factor*
Connes–Lott construction (γ on a separate tensor factor) is the explicit
surviving escape hatch and is untouched. If the true carrier is a larger
space in which the circulant is only a `C_3`-covariant *block*, the
weight-counting problem (A4) changes character entirely (you count modes of
the ambient operator, not of `Herm_circ(3)`). The APS-η route already lives
on `C_3[111] ⊂ S³`, not on `Herm_circ(3)`.

### A2 — what if `λ_k ≠ √m_k`?
Then the whole numerical match is interpretation, not derivation. This is an
unaudited import the bridge wisely disowns. Any closure that uses the
sqrt-mass map silently is importing the target. Flagged: do not let A2 leak
into a "derivation."

### A3 — what if the functional is not `log E_+ + log E_perp`?
Retained surfaces pin Frobenius as the unique Ad-invariant **inner
product**, but probe 18 (AV3) correctly notes this is "one structural level
too coarse": `F1`, `F2`, `F3` all use the *same* inner product. The choice
of *log*, of *block-norms as the arguments*, and of the *weights* are all
unpinned by inner-product uniqueness. → motivates ND2 (the functional may be
a fluctuation determinant, not a free-choice functional).

### A4 — what if `(1,1)` is wrong? **(the crux)**
`κ = 2μ/ν` (MRU weight-class theorem). So:
- `(μ,ν) = (1,1)` (per **isotype**) → `κ = 2` → `Q = 2/3`  ✓
- `(μ,ν) = (1,2)` (per real **dimension**) → `κ = 1` → `Q = 1`  ✗

The 30-probe BAE campaign shows the **physically natural measure gives
`(1,2)`, not `(1,1)`**: the Gaussian free energy is
`F = ½ log det K = ½ Σ_I (real_dim_I) log E_I`, i.e. the real-dimension
count `(1,2)` (probe 25 §"log det K", lines 204–211; "basic
statistical-mechanics free energy", line 362). The classical
equipartition theorem assigns energy *per real degree of freedom* — that is
`(1,2)`, giving `Q = 1`, the wrong answer. **The physically natural reading
falsifies, rather than supports, the weight the bridge needs.** → ND2, ND4.

### A5 — what if the constraint is not fixed-sum?
The extremum of `S` depends jointly on the functional (A3), the weights
(A4), and the constraint (A5). At fixed `det = E_+ E_perp` or fixed
`E_+`-only, the stationary `κ` moves. The triple (A3,A4,A5) carries enough
free structure to land on *any* `κ`; this is the formal statement that the
extremal principle is underdetermined. Choosing all three to hit `κ = 2` is
a fit unless each is independently forced.

### A6 — what if positivity fails?
`Q_alg = 2/3` is a **signed** identity. Physical Koide needs
`λ_k = a + 2|b| cos(δ + 2πk/3) ≥ 0`, which holds only in certain phase
chambers (bridge §3). The chamber is controlled by the Brannen phase `δ`
— the object of **Gate 2**. So positivity *couples* the magnitude gate to
the phase gate. The source-selector firewall's "`dQ/dδ = 0`, Q is
phase-blind" result is computed *on the `κ = 2` surface*; it does not see
the *upstream* chamber constraint that positivity imposes. → ND3.

---

## 3. Circular-reasoning stress test of every candidate weight mechanism

| Mechanism for `(1,1)` | Verdict |
|---|---|
| "Equal-weight" / democratic across isotypes | **CIRCULAR.** "Equal across isotypes" presupposes the 2-real-dim doublet counts as one object — i.e. that `|b|` (not `(Re b, Im b)`) is the coordinate. That is the `|b|^2/a^2` coordinate system itself. Probe 28 INT-AV8 lists it verbatim: "Constraint `|b|=const` → Circular (=BAE itself)." |
| Parent "Frobenius-reciprocity multiplicity measure" (`..._MEASURE_THEOREM_2026-04-19`) | **DEMOTED.** Rested on an `SO(2)` quotient collapsing `(Re b, Im b) → |b|`. `KOIDE_MRU_DEMOTION_NOTE_2026-04-20` found the quotient is an *unproven import*: under `b → e^{iθ}b` the spectrum is not permuted (only the discrete `θ ∈ {0, 2π/3, 4π/3}` cycle is a symmetry), so `SO(2)` is not a spectral symmetry and scalar observables are not `SO(2)`-invariant. |
| Plancherel / Peter–Weyl weight | gives **`(1,2)`** when counted over `R` (probe 12). |
| Gaussian / thermal / free-energy measure | gives **`(1,2)`** (probe 25, 28). |

**Conclusion of the stress test:** every *currently articulated* route to
`(1,1)` is either circular or rests on the demoted `SO(2)` quotient, while
every *physically natural* measure gives `(1,2)`. The bridge's required
weight is, on the current surface, the one weight that physics does not
hand you. This is the real obstruction — sharper than "open gap."

---

## 4. New directions (from the what-ifs)

Each is flagged speculative; each states its residual gap and circularity
status. None is asserted as derived. **No new axiom or import is claimed.**

### ND1 — Equipartition reframe (drop A0)
Replace "extremize a tuned functional" with "find a law forcing
`E_+ = E_perp`." The equality is **weight-free**, so it dodges A4's
circularity by construction. The new question — *what forces equal
Frobenius energy in the trivial and doublet isotypes?* — is cleaner.
**Residual / honest wall:** an isometry exchanging a 1-dim and a 2-dim
subspace does not exist, so a naive "exchange symmetry" cannot force the
equality. ND1 relocates the wall to "what prior/measure assigns equal
energy to a 1-dim and a 2-dim subspace," which is precisely the `(1,1)`
question in measure clothing. Progress = a *cleaner statement*, not a
closure. Not circular, but not obviously closable.

### ND2 — Separate the classical EOM from the fluctuation determinant (re A3/A4)
The `(1,2)` result is a **fluctuation determinant** about a classical
solution `H_0` (probe 25, line 337: "classical solution `H_0`,
block-diagonal on isotypes"). The extremal-principle framing may conflate
the *fluctuation measure* (which gives `(1,2)`) with the *classical
equations of motion* (which set `a, b` and may sit at the Koide point for
an entirely separate reason). **Direction:** ask what sets `H_0`, treating
`(1,2)` as a statement about fluctuations *around* `H_0`, not about `H_0`
itself. This dissolves the apparent `(1,2)`-falsification: `Q = 1` is the
extremum of the *fluctuation* functional, not necessarily the classical
configuration. **Residual:** requires a retained action whose classical
solution is the cone point — i.e. the same scalar-potential `V(m)` hatch
the six no-gos leave open, now with the `(1,2)` objection defused. Not
circular; ties directly to the surviving escape hatch.

### ND3 — Couple the two gates through positivity (re A6)
Positivity of `λ_k` at `κ = 2` is a constraint on the phase `δ` (Gate 2),
and the APS-η route gives `δ = 2/9` with a parity-odd basepoint `δ = 0`.
The gates are currently treated as independent (firewall: Q is
phase-blind), but the firewall's phase-blindness is computed *on* the
`κ = 2` surface and does not capture the *chamber* constraint upstream.
**Direction:** a single selected-line dynamics that fixes `δ` (chamber)
may thereby constrain which `(a,b)` are admissible, feeding back on the
magnitude. **Residual:** needs the selected-line endpoint/transport law
(open in both the firewall and the composition note's `N(m_*)=1`
conjecture). Not circular; reframes "two independent gates" as "one
coupled selection."

### ND4 — Real-vs-holomorphic measure: the weight is a *complex-structure* choice (re A4) — **the strongest lead**
The `(1,1)` vs `(1,2)` fork is exactly the `R`-vs-`C` counting probe 12
identified as the root. Sharpen it:

- The doublet isotype is, *as a real space*, `R⟨C+C²⟩ ⊕ R⟨i(C−C²)⟩`. But
  the map `b ↦ bC + b̄C²` makes it canonically a **single complex line**
  `C⟨C⟩` with complex coordinate `b`. The canonical complex structure
  `J` is multiplication by `i` on `b` (i.e. `B_1 ↦ B_2 ↦ −B_1`).
- The trivial isotype `aI`, `a ∈ R`, is genuinely **real**.
- A **real Gaussian** measure on the doublet counts 2 real dimensions →
  `log det ∝ 2 log E_perp` → `(1,2)` → `κ = 1`.
- A **holomorphic / Bargmann (coherent-state)** measure on the *complex
  line* counts 1 complex dimension:
  `∫_C e^{−|b|²/E} (i/2) db∧db̄ ∝ E^1` → `log det ∝ 1·log E_perp` →
  `(1,1)` → `κ = 2 = Koide`. ✓

So **F1 = holomorphic measure on the (genuinely complex) doublet + real
measure on the (genuinely real) trace coordinate; F3 = real measure on
both.** The dispute is not an arbitrary integer — it is *real Gaussian vs
Kähler/coherent-state* prior.

**Why this is plausibly non-circular** (the stress test applied to ND4
itself): the `SO(2)` quotient was demoted because it required `SO(2)` to be
a *spectral symmetry of `H`* (it is not). ND4 does **not** require that. A
measure/prior needs a **complex structure on the configuration space**, not
a spectral symmetry — and `J` is canonically present because `b ∈ C`. The
complex structure has an **independent physical motivation**: the phase
`δ = arg b` is the physical Brannen phase (Gate 2), and `δ` *only exists*
because `b` is a genuine complex amplitude. The very object that makes Gate
2 nontrivial (a `U(1)` phase) is the object that, taken seriously as a
complex coordinate, selects `(1,1)` for Gate 1. **This couples the two
gates through a single structure** (cf. ND3) and is in principle
falsifiable: it asserts the source dynamics is a coherent-state /
holomorphic path integral in `b`, a specific claim checkable against the
framework's Clifford/qubit dynamics.

**Residual gap (honest):** ND4 converts "which integer weight `(μ,ν)`?"
into "is the source measure real-Gaussian or holomorphic/Bargmann in `b`?"
That is a *better* gap — more physical, testable, and gate-coupling — but
it is still a gap, not a closure. **Circularity caveat:** if one justifies
the holomorphic measure by "we want the doublet counted once," that is
circular and adds nothing. The non-circular version *requires deriving the
coherent-state/Kähler structure of the `b`-dynamics from the framework's
axioms independently of the Koide target.* Until that derivation exists,
ND4 is a relocation of the gap, not its resolution — but it is the
relocation that turns an arbitrary-looking integer into a concrete physical
question and links it to the already-live phase structure.

---

## 5. Summary verdict

1. The Koide `Q = 2/3` "extremal principle" carries a single free
   parameter — the isotype weight ratio `μ/ν` — and `κ = 2μ/ν` shows the
   observed value `κ = 2` is reproduced **iff** `μ = ν`. The principle does
   not predict `2/3`; it is tuned to it through the weight choice.
2. Every currently articulated route to the needed weight `(1,1)` is either
   **circular** (the "equal-weight"/`|b|=const` collapse) or rests on the
   **demoted** `SO(2)` quotient. Every physically natural measure (Gaussian,
   thermal, Plancherel-over-`R`) gives `(1,2)` → `Q = 1`. The bridge needs
   the one weight physics does not hand you.
3. The six no-go theorems confirm no *known symmetry/gauge/anomaly/character*
   mechanism supplies the weight; the lone surviving hatch is a retained
   scalar-potential forcing, currently an honest gap (`m_V ≠ m_*`).
4. The most promising new direction (**ND4**) reframes the integer-weight
   dispute as a **real-Gaussian vs holomorphic/Kähler measure** choice on
   the genuinely-complex doublet coordinate `b`. This is independently
   motivated by the physical Brannen phase `δ = arg b`, is not blocked by
   the `SO(2)`-spectral-symmetry objection (a prior needs a complex
   structure, not a spectral symmetry), and **couples Gate 1 to Gate 2**.
   Its residual — derive the coherent-state structure of the `b`-dynamics
   from the axioms — is the sharpest, most physical form of the open gap.
5. Secondary directions: **ND2** (classical EOM vs fluctuation determinant,
   which defuses the `(1,2)` "falsification") and **ND3** (positivity
   couples the two gates) both point at the same surviving object: a
   retained `b`-dynamics / scalar action whose classical configuration is
   the cone point. ND1 (equipartition reframe) is clean but relocates the
   wall without lowering it.

**No closure is claimed. No import or axiom is asserted. ND2–ND4 are
candidate derivation targets, each with its residual stated.**
