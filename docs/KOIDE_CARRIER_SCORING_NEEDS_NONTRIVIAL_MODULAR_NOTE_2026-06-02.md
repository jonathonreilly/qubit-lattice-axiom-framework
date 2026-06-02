# Koide carrier scoring needs non-tracial modular input

**Date:** 2026-06-02
**Claim type:** bounded_theorem
**Claim boundary:** structural bounded result plus open-gate reduction. This note proves a
property of the *tracial* carrier (its Tomita-Takesaki modular operator is `Delta=1`) and uses
it to show the surviving channel-vs-direction **scoring** residual is not supplied by the
carrier's own tracial modular data or by the tested canonical kinematic mechanisms. The
`r=1/2` channel weight requires a **non-tracial finite-`beta` Gibbs/density weight** on the
scoring space. This note does
**not** derive `r=1/2`, does **not** supply the dynamics, does **not** approve any import or
Tier-A admission, and does **not** set an audit verdict. The specific weight that lands on
`r=1/2` remains dynamics-supplied and is the honest residual.
**Primary runner:** [`scripts/koide_carrier_scoring_needs_nontrivial_modular_2026_06_02.py`](../scripts/koide_carrier_scoring_needs_nontrivial_modular_2026_06_02.py) (SCORECARD PASS=8, FAIL=0).

## The residual this addresses

The just-built tracial-standard-form carrier note
[`KOIDE_TRACIAL_STANDARD_FORM_CARRIER_NARROW_NOTE_2026-06-02.md`](KOIDE_TRACIAL_STANDARD_FORM_CARRIER_NARROW_NOTE_2026-06-02.md)
(an unaudited source candidate strengthening
[`FLAVOR_MISSING_AXIOM_CARRIER_MEASURE_NOTE_2026-05-30.md`](FLAVOR_MISSING_AXIOM_CARRIER_MEASURE_NOTE_2026-05-30.md),
`unaudited`) showed the GNS cyclic vector `Omega=e` **ranks the `(1,N-1)` identity/non-identity
split** above the idempotent split, but left one commitment undetermined — the **scoring rule on
that split**:

| scoring on the `(1,N-1)` split | balance | `r=|b|^2/a^2` | `Q=1/3+(2/3)r` |
|---|---|---:|---:|
| equal energy **per channel** (2 channels: `{e}`-line, `{g,g^2}`-plane) | `a^2·1 = b^2·2` | **1/2** | **2/3** (Koide target) |
| equal energy **per direction** (Plancherel/dimension, 3 directions) | `a^2 = b^2` | 1 | 1 |

The retained algebra
([`KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md`](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md),
`retained`;
[`CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md`](CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-10.md),
`retained`) gives `Q=1/3+(2/3)r` and `Q=2/3 ⟺ r=1/2`. The prior campaign — and the two
2026-06-02 flow notes
([`FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md`](FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md),
[`FLAVOR_R_HALF_STABLE_UNDER_THERMALIZING_ARROW_2026-06-02.md`](FLAVOR_R_HALF_STABLE_UNDER_THERMALIZING_ARROW_2026-06-02.md),
both `unaudited`) — found that the tested canonical measures (Plancherel, dimension, Born, spectral,
max-entropy) gives the direction/spectral weighting (`r∈{0,1}`), never `r=1/2`. **This note explains
why, structurally, and pins the consequence.**

## The structural fact: the tracial carrier has a trivial modular operator (`Delta=1`)

The carrier state is the normalized group trace `tau` (`tau(g^k)=delta_{k,0}`);
the source carrier is `R[Z_3]` in its tracial standard form. For **any** trace, the GNS representation is
in standard form with a **trivial** Tomita-Takesaki modular structure:

> **Lemma (tracial ⟹ `Delta=1`).** Let `tau` be a faithful trace on a finite-dimensional
> `*`-algebra `M`, with GNS triple `(L^2(M,tau), pi, Omega)`, `Omega=1`. The Tomita operator
> `S: x·Omega ↦ x^*·Omega` has polar decomposition `S=J·Delta^{1/2}` with **`Delta=1`**; the modular
> Hamiltonian `K=-log Delta=0`; the modular automorphism flow `sigma_t(x)=Delta^{it} x Delta^{-it}=x`
> is the identity for all `t`. (A trace is the canonical KMS state at `beta=0` / infinite temperature.)

This is verified two independent ways in the runner for the carrier `R[Z_3]`:

- **explicit realified GNS construction** — `S(x·Omega)=x^*·Omega` built as a real `2N×2N` operator
  on `(Re,Im)`; `Delta=S^#S=I_6` exactly; `spec(-log Delta)={0,…,0}`;
- **textbook finite-dimensional density check** — with the tracial density matrix on the
  representation, `rho=I/N`, every conjugation/density reweighting visible to the carrier is
  scalar, so the modular flow is trivial and the Gibbs weight is uniform per direction.

**Consequence — the carrier's own distinguished weight is _direction_-counting.** The trace's
density matrix `rho_tau=I/N` is maximally mixed, and the modular Gibbs reweighting `exp(-K)` is
**uniform** per direction `(1,1,1)`. A uniform per-direction weight **is** direction-counting
(`w_0/w_1=1 ⟹ r=1 ⟹ Q=1`). So to the extent the tracial carrier weights anything at all from its own
modular/state data, it weights toward **`Q=1`, not** the Koide target `Q=2/3`.

## The crux: channel-counting (`r=1/2`) is provably a finite-`beta` KMS weight

Write the scoring rule as per-direction weights `w=(w_0,w_1,w_1)` (the most general
`Aut(Z_3)`- and `(g↔g^2)`-invariant weight); the balance `w_0 a^2 = w_1 b^2` gives `r=w_0/w_1`.

- **direction-counting** is `w_0/w_1=1` — the **uniform** (`beta=0`, tracial) weight → `r=1`;
- **channel-counting** needs `w_0/w_1=1/2`, i.e. the identity direction down-weighted to half a
  non-identity direction. As a Gibbs factor `w_0/w_1=exp(-beta·gap)=1/2` this requires
`beta·gap = ln 2 != 0` — a **finite `beta`** and a **non-zero density gap**.

The reduction target is concrete and well-posed: the runner exhibits an **explicit non-tracial
faithful density weight** `rho=diag(1/5,2/5,2/5)` whose id/non-id density gap
`log(p_1/p_0)=ln 2` yields the finite-`beta` KMS/Gibbs weight **exactly** `r=1/2`,
`Q=2/3`. The trace (`rho=I/3`, `gap=0`) **cannot** supply this weight — by the Lemma its modular flow
is trivial.

> **So the channel-vs-direction scoring residual is not supplied by the tracial modular data.
> In the tested canonical routes, obtaining `r=1/2` is equivalent to choosing a non-tracial
> finite-`beta` Gibbs/density weight — a dynamics / a temperature — which the trace by construction
> lacks.**

## Tested flow-free candidates do not force channel-counting

Each tested candidate that might force channel-counting **without** importing a dynamics either
gives direction-counting or is circular (verified in the runner):

- **Representation theory.** The `{g,g^2}`-plane is **not** a sub-representation of the left-regular
  rep (`g` maps `e_2→e_0`, off the plane), so it is **not** an "irreducible channel." The
  rep-canonical decomposition is **3 distinct 1-dimensional irreps** (characters `1,ω,ω^2`) — 3 equal
  lines — i.e. direction-counting → `r=1`. Treating the plane as "one channel" has **no**
  representation-theoretic backing.
- **Number operator / second quantization.** The `Z_3` **charge** number `n=diag(0,1,2)` (intrinsic
  to the group law via the Fourier dual) gives **3 singleton** particle-number sectors →
  direction-counting → `r=1`. The "excitation-**level**" number `diag(0,1,1)` that *would* give
  channel-counting requires declaring `{g,g^2}` a degenerate level — i.e. a Hamiltonian with
  spectrum `{0,1,1}`, which is the operator whose `r` we are fixing → **circular**. The most general
  `Aut(Z_3)`- and `(g↔g^2)`-invariant operator diagonal in the group ONB is `diag(α,β,β)` — a
  2-parameter family whose ratio is **free**, so invariance alone does not pin channel vs direction.
- **Entropy / records / objectivity.** The maximally-mixed (max-entropy) state **is** the trace
  `I/N` → uniform → `r=1`. Decoherence in the pointer (group) basis gives 3 distinct, independently
  broadcastable records → spectrum-broadcast/objectivity counts **3** records → `r=1`. Merging
  `{g,g^2}` into one record is an **extra** sub-`sigma`-algebra choice, not forced (they are
  orthogonal, perfectly distinguishable pointer states). [This is the same `r→2r^2` Lüders /
  thermalizing structure of the two flow notes, anchored on
  `luders_rule_from_composition_consistency_note_2026-05-20`, `retained_bounded`.]
- **Kähler/Dirac corroborator.** Its `r=1/2` comes from rank-prefactors `(p,q)=(1,2)` in
  `r=(q-p)/(4p-q)`; equal prefactors `(1,1)` give `r=0`, not `1/2`. The prefactor **ratio** `q/p` **is**
  the channel-vs-direction choice in disguise — the corroborator fixes the **value given** the
  weighting, never the weighting.

## No-Go Discipline Gate

This gate applies to the negative/open part of the claim: the tracial carrier's own modular data
and the tested kinematic routes do not supply the `r=1/2` channel weight.

- **N1 alternative routes:** (1) tracial Tomita-Takesaki modular flow; (2) left-regular
  representation decomposition; (3) intrinsic `Z_3` charge number; (4) max-entropy / records /
  objectivity counting on the pointer basis; (5) Kähler/Dirac rank-prefactor corroborator; (6) the
  general `Aut(Z_3)`-invariant diagonal family `diag(alpha,beta,beta)`. Routes (1)-(4) give
  direction-counting or a free ratio; route (5) imports the channel ratio as a prefactor; route (6)
  leaves the ratio free.
- **N2 wall independence:** the tracial modular calculation (`Delta=1`), the finite-`beta`
  density weight, the 2-sector coarse-graining, and the future dynamics that might select it are distinct.
  This note closes only the tracial-modular subquestion.
- **N3 hidden-wall scan:** no finite-`beta` state is admitted as framework input. The explicit
  `diag(1/5,2/5,2/5)` state is a witness for the form of the missing input, not an adopted weight.
- **N4 residual matching:** the residual is only the channel-vs-direction scoring on the
  tracial-standard-form carrier. It is not a derivation of charged-lepton masses, `Q=2/3`, or
  the dynamics that would select the finite-`beta` weight.
- **N5 rhetoric audit:** "not supplied by the tracial carrier" means the trace's modular/state data
  and the listed kinematic routes. It does not claim that no future source note can derive the
  weight dynamically.
- **N6 partial-closure scan:** the flow notes and future records/einselection dynamics are explicit
  partial-closure paths. They are not new axioms merely because they may retire this residual; they
  still need source derivation and audit.
- **N7 steelman:** a canonical non-tracial state could be derived from emergent-time dynamics,
  records-flow stability, or an independently audited 2-sector coarse-graining. Such a result would
  defeat the open residual without contradicting this note.
- **N8 cross-cycle echo:** prior records-flow notes already point toward dynamics for `r=1/2`.
  This note narrows why the tracial carrier alone did not supply that input.

## Net: the residual reduces to the emergent-time dynamics (a unification)

The channel-vs-direction scoring is the last undetermined input of the tracial-standard-form carrier.
This note shows it is **not** resolvable at the tracial (kinematic) level: the carrier's modular
flow is trivial (`Delta=1`), its own distinguished weight is direction-counting (`Q=1`), and
channel-counting (`Q=2/3`) is realized as the KMS/Gibbs weight of a non-tracial / finite-`beta` density.
This **explains** — at the structural level — why the two 2026-06-02 flow notes had to invoke a
**dynamics** (a thermalizing arrow, einselection from the commutant of a `C_3`-invariant interaction
Hamiltonian, or the records `r→2r^2` flow): the carrier's *own* modular flow supplies nothing, so any
selection of `r=1/2` must come from an evolution/temperature **on** the carrier.

Equivalently: the carrier-scoring residual is **transported** from "a scoring posit on a kinematic carrier" to
"**which finite-`beta` density / 2-sector coarse-graining the emergent-time dynamics realizes**" — the same
object the flow notes' open gate (the det_C / einselected 2-sector partition) names, now derived as
the necessary form of this residual rather than one option among the tested kinematic ones.

## Honest residual (what this does **not** do)

- It does **not** derive `r=1/2`: the specific density gap (`= ln 2`, -> `r=1/2`) is still
  **dynamics-supplied**. This note proves channel-counting *requires* a non-tracial structure; it does
  **not** show the emergent-time dynamics *delivers exactly that* structure. That (which `beta`, which
  coarse-graining, non-circularly) is the live open object — now sharply a dynamical question.
- It is **not** an import approval. The tracial carrier source remains unaudited, and relating the
  residual to a finite-`beta` state is a **diagnosis**, not a new admitted input or Tier-A
  admission.

## Falsifiable content (kept)

The channel-counting weight gives `r=1/(N-1)` at each `N` (for `Z_N`: `‖I_N‖^2=N`,
`‖J_N-I_N‖^2=N(N-1)`), so `r=1/2` is tied to the **derived** `n_gen=3` (`N=2→1`, `N=3→1/2` `Q=2/3`,
`N=4→1/3`, `N=6→1/5`). A dynamics that supplied the *wrong* gap would break this `N`-scaling — a
structural cross-check on any future dynamical derivation.

## Decoupling from the chirality no-go

`r=1/2` sits at `[H,S]=0` (interior of the commuting circulant family) and `H` does **not**
anticommute with the `C_3` chiral grading `Gamma_chi=(2/3)J-I`, so this note introduces no chiral
operator and does **not** trip
[`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md`](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md)
(`retained_bounded`). The value-lane reduction is structurally decoupled from the generation-chirality
gate.

## Non-circularity

`r=1/2` and `Q=2/3` are never assumed: they appear only as **outputs** of an externally imposed
weight (the finite-`beta` state). The carrier's intrinsic structure is shown to output `r=1` (`Q=1`),
and the Koide target value is shown to require a non-tracial input — the opposite of presupposing it.
`Delta=1` is computed from the trace alone (two independent methods), upstream of any Koide value.

## Tiers verified on `origin/main` (`.rows[claim_id].effective_status`)

| claim_id | effective_status | role here |
|---|---|---|
| `flavor_missing_axiom_carrier_measure_note_2026-05-30` | `unaudited` | the carrier-measure note the standard-form note strengthens |
| `flavor_r_half_is_the_records_flow_separatrix_2026-06-02` | `unaudited` | flow note this explains (records `r→2r^2` separatrix) |
| `flavor_r_half_stable_under_thermalizing_arrow_2026-06-02` | `unaudited` | flow note this explains (thermalizing attractor) |
| `koide_circulant_q_two_thirds_algebraic_narrow_theorem_note_2026-05-10` | `retained` | `Q=1/3+(2/3)r` algebra |
| `charged_lepton_koide_cone_algebraic_equivalence_narrow_theorem_note_2026-05-10` | `retained` | `Q=2/3 ⟺ r=1/2` biconditional |
| `koide_q23_block_weight_frontier_bounded_note_2026-05-29` | `retained_bounded` | block-weight algebra anchor |
| `luders_rule_from_composition_consistency_note_2026-05-20` | `retained_bounded` | the `r→2r^2` records-flow anchor of the flow notes |
| `koide_z3_equivariant_anticommuting_no_go_note_2026-05-16` | `retained_bounded` | chirality decoupling |
