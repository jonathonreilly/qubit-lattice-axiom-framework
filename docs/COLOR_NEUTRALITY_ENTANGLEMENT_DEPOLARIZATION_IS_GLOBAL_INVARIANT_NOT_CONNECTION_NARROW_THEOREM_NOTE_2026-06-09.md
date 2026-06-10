# Color-Neutrality Entanglement Depolarization Is a Global-Invariance Consequence, Not a Connection — Narrow Theorem Note

**Date:** 2026-06-09
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Script:** `scripts/frontier_color_neutrality_entanglement_depolarization_2026_06_09.py`
**Cache:** `logs/runner-cache/frontier_color_neutrality_entanglement_depolarization_2026_06_09.txt`
**Status authority:** source-note proposal only; the independent audit lane sets
the effective status. This note does not set or predict an audit outcome.

## Context — the relocated ADM-2 depolarization input

The gauge-link / color-einselection campaign has reduced the second
attractor-measure premise (ADM-2) to a single matter observable: does the
dynamics drive the single-carrier color density `rho_color` to the color-blind
ensemble `I3/3`? (Necessary direction:
`MATTER_COLOR_DEPOLARIZATION_NECESSARY_FOR_GAUGE_LINK_AD_INVARIANCE_NARROW_THEOREM_NOTE_2026-06-09`,
source proposal.) Two mechanisms for that depolarization were mapped, each gated:

- the depolarizing **twirl** — the channel `M -> E_sing(M) = (Tr M / N_c) I`
  applied to the color **operator**
  (`COLOR_DEPOLARIZATION_SINGLE_FRAME_DEPHASING_INSUFFICIENCY_AND_MULTIFRAME_EXHIBIT_NARROW_THEOREM_NOTE_2026-06-09`,
  source proposal; and the channel-vs-partition reading of
  [`FIERZ_SINGLET_CHANNEL_SELECTOR_IS_WEIGHT_NOT_PARTITION_NARROW_NO_GO_NOTE_2026-06-08`](FIERZ_SINGLET_CHANNEL_SELECTOR_IS_WEIGHT_NOT_PARTITION_NARROW_NO_GO_NOTE_2026-06-08.md),
  source proposal) — which requires a multi-frame / multi-instrument averaging
  admission Record does not supply;
- the matter-unitary **primitivity** route — a primitive unistochastic
  `S_ij = |U_ij|^2` requires a generic SU(3) **link** `V != I3`, a presupposed
  **local** background connection (PR #3436, PR #3441 source proposals), which is
  circular for a campaign that seeks to *induce* the connection.

This note records a **third, distinct** mechanism on the color carrier and
places it on the obstruction surface: the **color-singlet entanglement** route.

## Statement

Work on the framework color structure of the retained
[`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md)
and [`CL3_COLOR_AUTOMORPHISM_THEOREM.md`](CL3_COLOR_AUTOMORPHISM_THEOREM.md)
(`N_c = 3`, fundamental `3`, conjugate `3bar`; the unique `q`-`qbar` color
singlet is the decoration
[`CL3_QUARK_ANTIQUARK_COLOR_SINGLET_THEOREM_NOTE_2026-05-02`](CL3_QUARK_ANTIQUARK_COLOR_SINGLET_THEOREM_NOTE_2026-05-02.md)).
Let a two-carrier joint color state `rho_AB` live on `C^3 (x) C^3bar`.

**(T1) Singlet marginal.** The unique color singlet
`|s> = (1/sqrt(N_c)) sum_i |i, ibar>` has reduced single-carrier color density

```text
rho_A = Tr_B |s><s| = I3 / N_c,        Tr(rho_A^2) - 1/N_c = 0.
```

**(T2) Schur (the load-bearing step).** Let `rho_AB` be invariant under the
**global** diagonal color action `g (x) g*` for every `g in SU(3)` — the **same**
`g` on both carriers (a global color rotation, *not* a per-edge link). Then

```text
rho_A = Tr_B rho_AB = I3 / N_c.
```

*Proof.* `rho_A` commutes with every `g in SU(3)` (partial trace intertwines the
global action). The fundamental `3` is irreducible, so by Schur its commutant is
the scalars; a unit-trace scalar is `I3 / N_c`. ∎ The pure singlet (T1) is the
special pure case; the maximally-mixed octet state `P8/8` and any invariant
mixture share the marginal (runner E2).

**(T3) Global, not local.** The required symmetry is one color rotation applied
identically to both carriers, `g (x) g*`. An independent **local** action
`g_x (x) h_y*` with `g_x != h_y` does **not** fix the singlet (runner E3). The
global symmetry is strictly **weaker** than the local connection `g_x V g_y^dag`
that the block-07 primitivity route consumes — a different point on the
obstruction surface.

**(T4) Schur no-go for a lone carrier.** The single fundamental `C^3` admits no
SU(3)-invariant pure state and no invariant projector other than `0` and `I3`
(commutant of an irrep = scalars). The depolarization is therefore
**irreducibly multi-carrier**: a single isolated color carrier cannot be
color-neutralized this way. The baryon `qqq` singlet
`(1/sqrt(6)) eps_ijk |ijk>` corroborates — every single-carrier marginal is
`I3/3` (runner E5).

## What this is NOT (mechanism separation)

- **Not the twirl.** `E_sing` averages an **operator**, `(1/9) sum_k W_k M W_k^dag
  = (Tr M / N_c) I` over the Heisenberg-Weyl 1-design (runner E6, exact). The
  entanglement route never averages `rho_A`; it reads the **marginal** of an
  invariance-constrained joint **state**. The two maps agree on an already-
  invariant `rho` only because that input is already `I3/3`. They carry distinct
  admissions.
- **Not the local-connection route.** The marginal is `I3/3` for every global
  `g` (frame-independent on the invariant joint state), whereas the block-07
  route depolarizes only with a generic local `V != I3` and is reducible
  (`S = I`, no depolarization) in the `V`-eigenframe (runner E7).
- **Not a within-sector weight assigned by fiat.** The `I3/3` here is the forced
  partial trace of an invariance-constrained joint state: a non-invariant joint
  state has a **polarized** marginal (runner E8). So nothing is assigned by fiat
  — staying on the right side of the
  [`FIERZ_SINGLET_CHANNEL_SELECTOR_IS_WEIGHT_NOT_PARTITION_NARROW_NO_GO_NOTE_2026-06-08`](FIERZ_SINGLET_CHANNEL_SELECTOR_IS_WEIGHT_NOT_PARTITION_NARROW_NO_GO_NOTE_2026-06-08.md)
  weight-leak demotion (the `I3/3` is a Schur consequence, not a chosen weight).

## Relocation (no hat discharged)

The route delivers the relocated-ADM-2 depolarization **conditionally** on the
joint matter state being **globally color-neutral** (a global SU(3)
singlet/invariant). The axioms do not derive that the matter dynamics produce a
color-neutral composite — that is global color confinement, and the confinement
corpus on main is `unaudited` and imports scale-setting
([`CONFINEMENT_STRING_TENSION_NOTE`](CONFINEMENT_STRING_TENSION_NOTE.md)). So
ADM-2 relocates onto: *does the dynamics / Record select a globally
color-neutral matter state?* This is the converse, register-clean direction of
the necessary condition of
`MATTER_COLOR_DEPOLARIZATION_NECESSARY_FOR_GAUGE_LINK_AD_INVARIANCE...`: there
the unpolarized `rho_color` is *necessary* for an Ad-invariant link measure;
here global color-neutrality is *sufficient* for the unpolarized `rho_color`,
fenced behind the named neutrality admission.

The four campaign hats are untouched: ADM-1 (frame/link selection), the R1 link
generator, the R2 link-measure delivery, and the blocking isometry. No `ST1`/`ST2`
ranking is made. The runner is class-A finite-dimensional linear algebra
(`PASS=22 FAIL=0`), all identities exact, no Monte-Carlo in the logic path.

## Honest boundary — what this does NOT do

- It is **conditional** on global color-neutrality, a named admission the axioms
  do not supply; it does not derive depolarization from the axioms.
- It needs `>= 2` color carriers (a composite); a lone carrier cannot depolarize
  (T4). The mechanism delivers the color density, not any link object: it
  **induces no link dynamics** and constructs no connection — it sidesteps the
  link for the density rather than resolving the block-07 circularity for the
  link.
- Global color-neutrality is weaker than, and does not supply, a local
  connection; it says nothing about ADM-1 or the R1 link generator.
- A non-neutral or single-carrier matter state has a polarized marginal — the
  route is not a blanket guarantee of depolarization.

## No-Go Discipline Gate

This section gates the negative legs: a lone fundamental carrier cannot be
neutralized by this Schur/entanglement mechanism, and global color-neutrality is
not a local connection or link-dynamics construction.

- **N1 alternative routes:** (1) pure `q qbar` singlet — ATTEMPTED, gives
  `I3/3` marginal (E1). (2) any globally invariant `3 ⊗ 3bar` mixed state —
  ATTEMPTED, gives `I3/3` by Schur (E2). (3) independent local action
  `g_x ⊗ h_y*` — ATTEMPTED, does not fix the singlet (E3). (4) lone
  fundamental carrier — ATTEMPTED, has no invariant pure state/projector beyond
  scalar operators (E4). (5) baryon singlet — ATTEMPTED, corroborates the
  multi-carrier route with `I3/3` one-carrier marginals (E5).
- **N2 wall independence:** the walls are global color-neutrality, a
  multi-carrier color state, and the retained color representation structure.
  None supplies local link dynamics, a record-selected neutral state, or a
  confinement derivation.
- **N3 hidden-wall scan:** "global", "same `g` on both carriers", "not local",
  and "named admission" are explicit. Schur's lemma and partial trace are
  finite-dimensional linear algebra; global color-neutrality is not hidden as a
  Record consequence.
- **N4 residual matching:** this note answers the color-density marginal
  residual only. It does not match or close block 07's local-link residual, the
  twirl/instrument averaging residual, or confinement dynamics.
- **N5 rhetoric audit:** "not a connection" means no per-edge local link
  `V` or link generator is constructed. It does not mean a future connection
  theorem is impossible or unnecessary for other hats.
- **N6 partial-closure scan:** a future retained confinement or
  record-selection theorem could supply the global-neutrality input. That would
  promote the route's premise; it would not change this note into an axiom or
  primitive and does not make an approved primitive a bounded-status source.
- **N7 steelman:** a hostile reviewer can argue that global color-neutrality
  merely moves the real physics into confinement. Response: correct; this note
  explicitly relocates ADM-2 onto the neutral-state selection problem and does
  not claim to solve it.
- **N8 cross-cycle echo:** this mirrors the recent color-depolarization repairs:
  density depolarization can arise from several mechanisms, but each mechanism
  has its own named admission. This note keeps the global-invariance route
  separate from twirl averaging and local-link primitivity.

## No new imports

`N_c = 3`, the fundamental/conjugate reps, the Fierz singlet, Schur's lemma, and
the partial trace are all standard finite-dimensional linear algebra carried by
the retained color structure and the cited decorations. No PDG value, no
empirical fit, no new axiom, no new primitive, and no literature comparator is
load-bearing. The confinement corpus is cited only to state that global
color-neutrality is *not* delivered there from the axioms (relocation target),
not consumed as an input.

## Dependencies

- [GRAPH_FIRST_SU3_INTEGRATION_NOTE.md](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md) —
  retained SU(3) carrier structure.
- [CL3_COLOR_AUTOMORPHISM_THEOREM.md](CL3_COLOR_AUTOMORPHISM_THEOREM.md) —
  retained algebraic color automorphism structure.
- [CL3_QUARK_ANTIQUARK_COLOR_SINGLET_THEOREM_NOTE_2026-05-02.md](CL3_QUARK_ANTIQUARK_COLOR_SINGLET_THEOREM_NOTE_2026-05-02.md) —
  decoration-level q-qbar singlet source.
- [FIERZ_SINGLET_CHANNEL_SELECTOR_IS_WEIGHT_NOT_PARTITION_NARROW_NO_GO_NOTE_2026-06-08.md](FIERZ_SINGLET_CHANNEL_SELECTOR_IS_WEIGHT_NOT_PARTITION_NARROW_NO_GO_NOTE_2026-06-08.md) —
  weight-leak boundary and mechanism-separation context.
- [CONFINEMENT_STRING_TENSION_NOTE.md](CONFINEMENT_STRING_TENSION_NOTE.md) —
  cited only as a non-delivery boundary for global color-neutrality.
