# `alpha_s(v)` Forward-Computation Theorem over Declared Boundary Inputs, with Bounded `M_Z` Corollary

**Date:** 2026-04-15 (status amended 2026-05-01; bounded source hint added
2026-05-24; T1/C1 repair 2026-06-10; B3 algebraic half grounded in the
tadpole-improvement narrow theorem 2026-06-11; B3 operator-counting
authority wired 2026-06-11)
**Type:** bounded_theorem
**Claim scope:** One load-bearing theorem plus one explicitly quarantined
corollary.
(T1, load-bearing) Given the declared boundary inputs B1-B4
below, the forward computation
`alpha_s(v) = alpha_bare / u_0^2 = 1 / (4 pi sqrt(<P>)) = 0.10330382`
is exact zero-free-parameter arithmetic over those inputs, together
with the exact coupling-chain identity
`alpha_LM^2 = alpha_bare * alpha_s(v)`.
(C1, bounded corollary, explicitly NOT load-bearing for T1) Transferring
the T1 output through the registered standard-infrastructure running
kernel from `v` to `M_Z` gives `alpha_s(M_Z) = 0.118067 ~ 0.1181`, with
a 1-loop/2-loop truncation envelope `~5e-4`. C1 uses the running
bridge's bounded transfer-kernel scope and is excluded from the T1 claim
surface.
**Status authority:** independent audit lane only. This source note is a
bounded forward-computation theorem; it does not set or predict an audit
outcome.
**Primary runner:** `scripts/frontier_alpha_s_derived_bounded_chain.py`

**Audit replacement gate (plain-text pointer, not a one-hop authority for
this bounded lane):** `ALPHA_S_DIRECT_WILSON_LOOP_DERIVATION_THEOREM_NOTE_2026-04-30.md`
with runner `scripts/frontier_alpha_s_direct_wilson_loop.py`.

## Why this note was repaired (2026-06-10)

The prior revision of this note carried the load-bearing step

> Given `alpha_s(v) = alpha_bare / u_0^2 = 0.1033` from the canonical
> plaquette/`u_0` chain, the registered bounded standard QCD running
> bridge transfers it to `alpha_s(M_Z) = 0.1181`.

which the 2026-05-05 audit classified as class (B) — a cross-note value
transfer — terminating in the running-bridge dependency. That dependency
is now scoped as the bounded transfer-map kernel
[`QCD_LOW_ENERGY_RUNNING_BRIDGE_NOTE_2026-05-01.md`](QCD_LOW_ENERGY_RUNNING_BRIDGE_NOTE_2026-05-01.md).
The prior framing of this note hid the dependency inside the headline
number.

This repair fixes five defects:

1. **(Critical) Load-bearing chain terminated in the running bridge.**
   The headline `0.1181` hid the bridge dependency. Fix:
   the claim is split into theorem T1 (the forward computation
   `alpha_s(v) = 0.10330382` over declared boundary inputs; load-bearing) and
   corollary C1 (the `M_Z` readout; quarantined, explicitly not
   load-bearing for T1). The bridge dependency is scoped to corollary
   step S5 only — see the dependency-status declaration below.
2. **(High) Miscited plaquette authority.** The prior text called
   `<P> = 0.5934` "same-surface MC-evaluated". Since its 2026-05-25
   finite-diagnostic repair, the plaquette authority
   ([`PLAQUETTE_SELF_CONSISTENCY_NOTE.md`](PLAQUETTE_SELF_CONSISTENCY_NOTE.md))
   licenses `0.5934` **only** as an admitted comparison/reuse number,
   not as a value it derives or certifies. Fix: boundary input B1,
   consuming the value exactly under that license.
3. **(High) Silent scheme/scale identification.** Identifying the
   tadpole-improved lattice coupling `alpha_bare / u_0^2` with the
   strong coupling `alpha_s` at `mu = v` glosses both a scheme
   conversion (lattice scheme vs. MSbar) and a scale assignment. Fix:
   declared boundary input B4.
4. **(High) Unauthorized vertex power.** The prior chain asserted the
   vertex power `n_link = 2` via a "vertex-power theorem" with no
   one-hop authority in the packet. Fix: declared structural boundary
   input B3 (the coupling-map derivation lane
   `docs/ALPHA_S_CMT_COUPLING_MAP_DERIVATION_THEOREM_NOTE_2026-05-17.md`,
   referenced here by file path only, is the derivation target; this
   note does not claim it).
5. **(Medium) Wrong registered runner.** The registered primary runner
   was the shared `scripts/frontier_yt_zero_import_chain.py`, whose
   PASS surface is dominated by class-(D) comparators on other lanes.
   Fix: the dedicated runner
   `scripts/frontier_alpha_s_derived_bounded_chain.py`, which computes
   T1 forward from the declared boundary inputs and tags every check
   [A]/[B]/[D].

The arithmetic of the prior note was verified correct and is retained:
`u_0 = 0.877681381`, `alpha_s(v) = 0.10330382`, 2-loop run
`-> 0.118067 ~ 0.1181`.

## Declared boundary inputs (B1-B4)

T1 is a theorem **over** these local boundary inputs. None of them is
claimed as derived by this note.

- **B1 (licensed reuse number).** `<P> = 0.5934`. License: the plaquette
  authority [`PLAQUETTE_SELF_CONSISTENCY_NOTE.md`](PLAQUETTE_SELF_CONSISTENCY_NOTE.md)
  states that "the canonical value `0.5934` may still be used by
  downstream notes only as an admitted comparison/reuse number unless a
  separate retained MC certificate or analytic beta=6 closure is
  supplied." This note consumes the value exactly and only under that
  license. The specification note
  `docs/PLAQUETTE_VALUE_DERIVATION_PROGRAM_SPECIFICATION_AND_BRACKET_REDUCTION_NARROW_THEOREM_NOTE_2026-06-10.md`
  (follow-up reference) is hereby cited as B1's **declared
  retirement interface**: its S0/T1 give the admission a precise
  referent — the proven-to-exist infinite-volume number
  `<P>* = 1 + f'(6)` with quantitative finite-size rate
  `|f_L - f| <= 6*beta/L` — so `0.5934` stands for a well-defined
  object rather than "the canonical lattice value". Its T2 reduces
  retiring B1 to one certified three-point `ln Z_L` enclosure with a
  proven, honestly priced error budget (`L ~ 3.7e5` for a rigorous
  `0.01`-wide bracket under the unconditional rate), and its T3 closes
  the rival convergent strong-coupling-expansion route at `beta = 6`
  at the standard-certificate level. None of this changes B1's status
  here: the value remains admitted, not derived, until that interface
  is actually discharged.
- **B2 (declared normalization).** `g_bare = 1` on the canonical
  same-surface chain, hence `alpha_bare = g_bare^2 / (4 pi) = 1 / (4 pi)`.
- **B3 (declared structural input; algebraic half and operator-counting
  authority wired 2026-06-11).** The load-bearing operator statement is
  the channel actually supported in-repo: the gauge
  vacuum-polarization channel
  `Pi = -Tr[D^{-1} D' D^{-1} D']` of the staggered Dirac operator
  contains exactly two insertions of the single-link vertex
  `D' = dD/dA`; in the coupling-map parameterization this gives
  `n_link = 2` for that vacuum-polarization channel and the improvement
  factor `u_0^(-2)` for that channel. **One-hop authority for the
  operator half:** [`YT_VERTEX_POWER_OPERATOR_COUNTING_LEMMA_NOTE_2026-05-17.md`](YT_VERTEX_POWER_OPERATOR_COUNTING_LEMMA_NOTE_2026-05-17.md),
  consumed strictly within its named assumptions: the staggered-Dirac
  realization gate and the conventional link-exponential map
  `U_mu(x) = exp(i a g A_mu(x))` (with the lemma also using the
  lattice-spacing-absorbed form `U_mu(x) = exp(i A_mu(x))`), plus the
  lemma's bare-coupling-map identity admission for parameterizing
  `alpha_eff = alpha_bare/u_0^{n_link}` by `n_link`.
  **One-hop authority for the algebraic half:** the standalone
  algebraic equivalences consumed by T1 — `alpha_LM = alpha_bare/u_0`,
  `alpha_s(v) = alpha_bare/u_0²`, the vertex-power identities
  `alpha_s(v)·u_0² = alpha_bare`, `alpha_LM·u_0 = alpha_bare`, and the
  geometric-mean identity `alpha_LM² = alpha_bare·alpha_s(v)` on
  abstract `(alpha_bare, u_0) ∈ R⁺ × R⁺` — are supplied by
  [`ALPHA_S_TADPOLE_IMPROVEMENT_VERTEX_POWER_NARROW_THEOREM_NOTE_2026-05-10.md`](ALPHA_S_TADPOLE_IMPROVEMENT_VERTEX_POWER_NARROW_THEOREM_NOTE_2026-05-10.md)
  (consumed strictly within its abstract-algebra scope; it supplies no
  plaquette value, no scheme conversion, and no operator-level
  justification of the power). The earlier three-gluon-vertex phrasing
  is not used as load-bearing wording; no in-repo authority cited here
  proves a three-gluon-vertex statement. What remains declared-not-derived
  in B3 is the channel-selection step: identifying the
  vacuum-polarization channel count as the vertex power entering the
  physical coupling definition `alpha_s(v) := alpha_bare/u_0^2`. B3
  also inherits the operator lemma's named assumptions and admission
  until that lemma's audit lands. The channel-selection/coupling-map
  retirement work remains tracked by
  `docs/ALPHA_S_CMT_COUPLING_MAP_DERIVATION_THEOREM_NOTE_2026-05-17.md`
  as a file-path pointer only; it is not a one-hop authority here.
- **B4 (declared scheme/scale input).** The tadpole-improved
  lattice coupling `alpha_bare / u_0^2` is identified with the strong
  coupling `alpha_s` at the scale `mu = v = 246.282818290129 GeV`. This
  identification glosses a lattice-to-MSbar scheme conversion and a
  scale assignment; both are declared here, not derived.

## B3 operator-wording repair (2026-06-11)

The audit named the operator-level counting residue in B3. This edit
reconciles the operator wording to the in-repo counting lemma: the
supported statement is that the staggered-Dirac gauge
vacuum-polarization channel contains exactly two single-link `D'`
insertions, giving `n_link = 2` for that channel in the coupling-map
parameter. The lemma is wired above as the named one-hop authority under
its named assumptions and admission; the channel-selection identification
from that vacuum-polarization count to the physical coupling definition
`alpha_s(v) := alpha_bare/u_0^2` remains declared in B3.

## Theorem T1 (load-bearing)

Given B1-B4:

```text
u_0        = <P>^(1/4)                 = 0.877681381
alpha_bare = 1 / (4 pi)                = 0.0795774715
alpha_s(v) = alpha_bare / u_0^2
           = 1 / (4 pi sqrt(<P>))      = 0.10330382
alpha_LM   = alpha_bare / u_0,   with  alpha_LM^2 = alpha_bare * alpha_s(v)
```

Every step after the boundary inputs is exact closed-form arithmetic with
zero free parameters. The runner verifies the chain by two independent
evaluation routes (the stepwise `u_0` chain and the collapsed closed
form `1 / (4 pi sqrt(<P>))`, plus a third log-domain route) agreeing to
`1e-16`, with exact-identity residuals at machine precision
(`|4 pi sqrt(<P>) alpha_s(v) - 1| ~ 2e-16`,
`|alpha_LM^2 - alpha_bare alpha_s(v)| ~ 2e-18`).

### Per-step authority table

| Step | Statement | Class | One-hop authority |
| --- | --- | --- | --- |
| S1 | reuse `<P> = 0.5934` | licensed boundary input | [`PLAQUETTE_SELF_CONSISTENCY_NOTE.md`](PLAQUETTE_SELF_CONSISTENCY_NOTE.md) reuse license (B1) |
| S2 | `u_0 = <P>^(1/4) = 0.877681381` | (A) exact arithmetic | this note + dedicated runner |
| S3 | `alpha_bare = g_bare^2/(4 pi) = 1/(4 pi)` | (A) over declared normalization | B2 (declared in this note) |
| S4 | `alpha_s(v) = alpha_bare/u_0^2 = 1/(4 pi sqrt(<P>)) = 0.10330382`; `alpha_LM^2 = alpha_bare alpha_s(v)` | (A) exact arithmetic over boundary inputs | algebraic identities: [`ALPHA_S_TADPOLE_IMPROVEMENT_VERTEX_POWER_NARROW_THEOREM_NOTE_2026-05-10.md`](ALPHA_S_TADPOLE_IMPROVEMENT_VERTEX_POWER_NARROW_THEOREM_NOTE_2026-05-10.md); operator count `n_link = 2` for the staggered-Dirac gauge vacuum-polarization channel: [`YT_VERTEX_POWER_OPERATOR_COUNTING_LEMMA_NOTE_2026-05-17.md`](YT_VERTEX_POWER_OPERATOR_COUNTING_LEMMA_NOTE_2026-05-17.md) under the staggered-Dirac realization gate, link-exponential convention, and bare-coupling-map identity admission; channel-selection + scheme/scale: B3 + B4 (declared in this note) |
| S5 | (C1 only) `v -> M_Z` standard 2-loop transfer: `alpha_s(M_Z) = 0.118067 ~ 0.1181` | bounded standard-infrastructure transfer | [`QCD_LOW_ENERGY_RUNNING_BRIDGE_NOTE_2026-05-01.md`](QCD_LOW_ENERGY_RUNNING_BRIDGE_NOTE_2026-05-01.md) (scoped to C1 only) |

The load-bearing claim surface of this note is S1-S4 (theorem T1). S5
belongs exclusively to corollary C1.

## Corollary C1 (bounded; explicitly not load-bearing for T1)

Transferring the T1 output `alpha_s(v) = 0.10330382` through the
standard SM 2-loop RGE (Machacek-Vaughn 1984; Arason et al. 1992) with
leading-order active-flavor threshold matching (only the top threshold
`m_t = 172.69 GeV` lies between `v` and `M_Z`), holding the auxiliary
standard SM boundary inputs
`(g_1, g_2, y_t, lambda)(v) = (0.46228, 0.65184, 0.93737, 0.13)` fixed,
gives

```text
alpha_s(M_Z) = 0.118067 ~ 0.1181
1-loop/2-loop truncation envelope ~ 5e-4
```

C1 is a corollary, not part of the T1 claim surface:

- the running kernel, the quark-mass threshold, and `M_Z` are standard
  external infrastructure (registered one hop away in the bridge note),
  not framework-native results;
- the bridge note currently states a bounded transfer-map kernel over
  `D = [0.085, 0.130]`, with PDG comparisons quarantined in its
  comparator appendix; C1 honestly inherits exactly that bounded
  standard-infrastructure scope;
- removing C1 entirely leaves T1 intact — the runner computes T1 first
  and independently, and its C1 section is a self-contained 2-loop RGE
  reimplementation used only for the corollary readout and envelope.

## Dependency-status declaration (one-hop license statements)

This note has exactly four one-hop authorities. The scope on which each
is consumed is:

1. [`PLAQUETTE_SELF_CONSISTENCY_NOTE.md`](PLAQUETTE_SELF_CONSISTENCY_NOTE.md)
   (claim `plaquette_self_consistency_note`). Consumed at S1/B1 only,
   and only under its explicit reuse license: `0.5934` enters as a
   declared reuse input. This note does not claim the value is
   derived, MC-certified, or analytically closed upstream.
2. [`ALPHA_S_TADPOLE_IMPROVEMENT_VERTEX_POWER_NARROW_THEOREM_NOTE_2026-05-10.md`](ALPHA_S_TADPOLE_IMPROVEMENT_VERTEX_POWER_NARROW_THEOREM_NOTE_2026-05-10.md)
   (claim
   `alpha_s_tadpole_improvement_vertex_power_narrow_theorem_note_2026-05-10`).
   Consumed at B3/S4 only for the abstract algebraic equivalences on
   positive `(alpha_bare, u_0)`: `alpha_LM = alpha_bare/u_0`,
   `alpha_s(v) = alpha_bare/u_0^2`, the associated inverse identities,
   and `alpha_LM^2 = alpha_bare alpha_s(v)`. This note does not read
   any plaquette value, scheme conversion, scale assignment, or
   operator-level power count from that theorem.
3. [`YT_VERTEX_POWER_OPERATOR_COUNTING_LEMMA_NOTE_2026-05-17.md`](YT_VERTEX_POWER_OPERATOR_COUNTING_LEMMA_NOTE_2026-05-17.md)
   (claim `yt_vertex_power_operator_counting_lemma`). Consumed at
   B3/S4 only for the statement that the staggered-Dirac gauge
   vacuum-polarization channel contains exactly two single-link
   `D' = dD/dA` insertions, giving `n_link = 2` for that channel under
   the staggered-Dirac realization gate, link-exponential convention,
   and bare-coupling-map identity admission.
   This note does not read from the lemma a three-gluon-vertex statement
   or the channel-selection identification into
   `alpha_s(v) := alpha_bare/u_0^2`.
4. [`QCD_LOW_ENERGY_RUNNING_BRIDGE_NOTE_2026-05-01.md`](QCD_LOW_ENERGY_RUNNING_BRIDGE_NOTE_2026-05-01.md)
   (claim `qcd_low_energy_running_bridge_note_2026-05-01`; bounded
   transfer-map kernel over `D = [0.085, 0.130]`). **Scoped to
   corollary step S5 only.** T1 does not read, transfer, or depend on
   any value from this row. Per the bridge note's own reuse rule, C1
   reads the `v -> M_Z` kernel as bounded standard infrastructure, never
   as a first-principles derivation. Any change in that row's status
   resolves into this note by cascade on C1 alone; T1's claim surface
   is unaffected.

Plain-text progress pointer, not a one-hop authority:
`docs/GAUGE_VACUUM_PLAQUETTE_RHO_PQ6_WILSON_ENVIRONMENT_BOUNDED_NOTE_2026-05-09.md`
records where B1's upstream plaquette analytic work currently stands.
It is not load-bearing for T1, because T1 consumes `<P> = 0.5934` as an
input (B1), not as a derived value.

## 2026-06-12 Residual-Bridge Source Firewall

The B3 algebraic identity and the B3 operator-counting half are now
wired, but this row still cannot honestly promote beyond bounded
forward arithmetic. The remaining promotion blockers are exact and
source-visible:

- **B1 remains an admitted plaquette value.** The bracket-reduction
  program gives `<P>* = 1 + f'(6)` a framework-native referent and
  reduces retirement to a certified three-point `ln Z_L` enclosure, but
  this note does not supply that enclosure and does not derive
  `<P> = 0.5934`.
- **B3 still has a channel-selection residue.** The retained algebraic
  theorem supplies the `u_0^{-2}` identities, and the operator-counting
  lemma supplies the two-insertion vacuum-polarization channel count.
  What is not derived here is the physical coupling-map theorem that
  identifies that channel count as the vertex power in
  `alpha_s(v) := alpha_bare/u_0^2`.
- **B4 remains a scheme/scale bridge.** The lattice tadpole-improved
  coupling is not proved here to be the MSbar strong coupling at
  `mu = v`; the `v -> M_Z` corollary therefore stays standard
  bounded-infrastructure context.

Source-surface summary: this is bounded support only. It partially closes the
direct blocker by preserving the T1 arithmetic over B1-B4, the B3 abstract
algebraic identities, and the B3 vacuum-polarization two-insertion operator
count. The live blockers remain the B1 plaquette-value certificate, the B3
channel-selection/coupling-map theorem, and the B4 lattice-to-MSbar scheme and
scale theorem. No retained-grade proposal or status promotion is made here;
the independent audit lane remains the only authority for effective status.

## Why this is not a numerical match at a tuned scale

- **Zero-free-parameter closed form.** T1's output is
  `alpha_s(v) = 1 / (4 pi sqrt(<P>))` — a parameter-free function of
  the single boundary input `<P>`. There is no second knob: nothing in
  S2-S4 can be adjusted to move the output, and `<P>` itself is fixed
  upstream by the Wilson action at `beta = 6`, not by any fit to
  `alpha_s`.
- **Analytic sensitivity is declared, not hidden.** The exact
  sensitivity is `d alpha_s(v) / d<P> = -alpha_s(v) / (2 <P>)
  = -0.0870`, i.e. a `1%` shift in `<P>` moves `alpha_s(v)` by `0.5%`.
  The runner verifies this against a central finite difference. The
  agreement of C1's readout with the PDG band is therefore not
  tolerance-trivial; it is a genuine constraint on the boundary input `<P>`,
  and it is reported as exactly that — a constraint conditional on
  B1-B4 — not as a framework-native prediction.
- **The PDG comparator is quarantined.** PDG constants appear only in
  the terminal class-(D) section of the dedicated runner and in C1's
  standard-infrastructure threshold/scale inputs. T1's claim surface
  (S1-S4) contains no external comparator and no externally calibrated
  input scale: `v` enters only as the scale **label** of boundary input B4,
  not as a number that the arithmetic of S1-S4 consumes.

## Explicit non-claims

This note does **not** claim:

- a derivation, MC certification, or analytic closure of
  `<P> = 0.5934` (declared under the upstream reuse license, B1);
- a derivation of the lattice-to-MSbar scheme conversion or of the
  scale assignment `mu = v` (declared, B4);
- a derivation of the channel-selection step that identifies the
  staggered-Dirac gauge vacuum-polarization channel count as the vertex
  power entering the physical coupling definition
  `alpha_s(v) := alpha_bare/u_0^2` (declared, B3);
- a derivation of the staggered-Dirac realization gate or the
  link-exponential convention named by the operator-counting lemma;
- a framework-native derivation of the QCD beta function, the quark
  mass thresholds, or `M_Z` (C1 standard infrastructure, one hop away
  in the bridge note);
- a framework-native prediction `alpha_s(M_Z) = 0.1181` (C1 is a
  bounded corollary using the bridge row's bounded transfer-kernel
  scope);
- any audit outcome or status promotion (status authority is the
  independent audit lane only).

The honest ceiling for this row remains bounded: T1 is exact arithmetic
over declared boundary inputs, and B1, B3, and B4 are real open work
owned by the upstream plaquette and coupling-map lanes.

## Verification

Run:

```bash
python3 scripts/frontier_alpha_s_derived_bounded_chain.py
```

Expected result (deterministic, pure Python, runtime under one second):

```text
Breakdown: A=8 B=9 D=2
TOTAL: PASS=19 FAIL=0
```

The runner computes T1 forward from the declared boundary inputs B1-B4 (the
helper module `scripts/canonical_plaquette_surface.py` is consulted only
for tagged class-(B) consistency residuals), checks two independent
evaluation routes to `1e-16`, the exact-identity and sensitivity
residuals, and then runs a self-contained 2-loop SM RGE reimplementation
for C1 with its truncation envelope. PDG constants appear only in the
terminal class-(D) section. Every check is tagged [A]/[B]/[D].

## Changelog

- **2026-04-15.** Original note: canonical plaquette/`u_0` chain with
  headline `alpha_s(M_Z) = 0.1181`.
- **2026-05-01.** Scope amendment: author tier moved from
  retained-seeking to bounded; running bridge registered as a one-hop
  authority.
- **2026-05-09.** Informational bridge-support progress entry for the
  `rho_(p,q)(6)` coefficient-table delivery.
- **2026-06-10.** T1/C1 repair (this revision). Load-bearing claim
  restructured from a class-(B) cross-note transfer terminating in the
  running-bridge row into theorem T1 — the forward
  computation `alpha_s(v) = 1/(4 pi sqrt(<P>)) = 0.10330382` over the
  explicitly declared boundary inputs B1-B4 — with the `M_Z`
  readout quarantined as bounded corollary C1 (scoped to step S5;
  resolves by cascade without touching T1). Miscitation of the
  plaquette authority fixed (B1 reuse license); silent
  scheme/scale identification declared (B4); vertex power declared as
  structural boundary input (B3, coupling-map lane by file path only);
  dedicated runner
  `scripts/frontier_alpha_s_derived_bounded_chain.py` registered,
  replacing the shared `scripts/frontier_yt_zero_import_chain.py`
  registration (that shared runner is unchanged). Prior arithmetic
  verified and retained: `u_0 = 0.877681381`,
  `alpha_s(v) = 0.10330382`, 2-loop `-> 0.118067 ~ 0.1181`, envelope
  `~5e-4`.
- **2026-06-10.** B1 retirement-interface citation (follow-up). The B1
  admission paragraph now cites
  `docs/PLAQUETTE_VALUE_DERIVATION_PROGRAM_SPECIFICATION_AND_BRACKET_REDUCTION_NARROW_THEOREM_NOTE_2026-06-10.md`
  (follow-up reference) as the declared retirement interface
  for B1: precise referent `<P>* = 1 + f'(6)` with proven finite-size
  rate (S0/T1), bracket reduction to one certified three-point `ln Z_L`
  computation with proven budget (T2), and closure of the rival
  cluster-expansion route at `beta = 6` (T3). The admitted-reuse
  license text is unchanged; B1's status (admitted, not derived) is
  unchanged; runner untouched.
- **2026-06-11.** B3 algebraic half grounded (audit-requested partial
  repair of "supply one-hop authority for B3"). The
  narrow theorem
  [`ALPHA_S_TADPOLE_IMPROVEMENT_VERTEX_POWER_NARROW_THEOREM_NOTE_2026-05-10.md`](ALPHA_S_TADPOLE_IMPROVEMENT_VERTEX_POWER_NARROW_THEOREM_NOTE_2026-05-10.md)
  is wired as the one-hop markdown authority for the abstract
  algebraic equivalences T1 consumes (`alpha_LM = alpha_bare/u_0`,
  `alpha_s(v) = alpha_bare/u_0²`, vertex-power and geometric-mean
  identities on `R⁺ × R⁺`), strictly within its abstract scope. B1 (the
  plaquette value, retirement interface unchanged) and B4 (the
  scheme/scale bridge) remain declared open boundary inputs — those
  are real derivation programs owned upstream, not citation gaps.
- **2026-06-11.** B3 operator wording reconciled to the in-repo counting
  lemma. The load-bearing operator statement is now the
  staggered-Dirac gauge vacuum-polarization two-insertion count, with
  [`YT_VERTEX_POWER_OPERATOR_COUNTING_LEMMA_NOTE_2026-05-17.md`](YT_VERTEX_POWER_OPERATOR_COUNTING_LEMMA_NOTE_2026-05-17.md)
  wired as the one-hop markdown authority under its named assumptions
  and admission. The three-gluon-vertex wording is removed from the
  load-bearing statement; the channel-selection identification from the
  vacuum-polarization count to `alpha_s(v) := alpha_bare/u_0^2` remains
  declared in B3.
