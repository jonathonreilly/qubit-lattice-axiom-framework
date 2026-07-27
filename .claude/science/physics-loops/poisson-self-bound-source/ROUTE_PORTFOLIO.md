# Route Portfolio — poisson-self-bound-source (cycle 713)

## Target

`self_consistency_forces_poisson_note` claims that self-consistency selects the
unscreened Poisson operator. PR #5693 (cycle 712) established that the note's
conclusion is right but its evidence never tested a far field, because the
self-consistent construction cannot supply a localized source: with the
per-layer normalization the source is scale-locked to the box, and without it
the total mass diverges. The successor named there is a **source term that is
not the normalized propagator density**.

## Step-2 prior-art sweep (mandatory)

Searched commit: `9ce38a06db` (`git fetch origin main:refs/remotes/origin/main`,
2026-07-27).

Commands run:

```bash
git grep -l -iE "self.?bound|soliton|schr(o|ö)dinger.?newton|choquard" origin/main -- 'docs/*.md'
git grep -l -iE "(self.?consistent.*(ground state|eigen)|nonlinear eigen|hartree)" origin/main -- 'docs/*.md'
git grep -l -i "biharmonic" origin/main -- 'docs/*.md'
git ls-tree -r --name-only origin/main -- docs/ | grep -iE "SOURCE|LOCALIZ|SOLITON|BOUND_STATE"
git grep -l -iE "(box.?independen|lattice.?size.?independen|size.?independent.*(width|extent|radius))" origin/main -- 'docs/*.md'
git grep -l -iE "(asymptotically free|confining potential|kernel (decays|grows)|potential (depth )?(grows|scales) with (the )?box)" origin/main -- 'docs/*.md'
git grep -l -iE "hartree|frozen_star|self_focusing" origin/main -- 'docs/audit/data/ledger/'
```

### Matched hits and classification

| Hit | What it actually contains | Classification |
|---|---|---|
| `docs/FROZEN_STARS_RIGOROUS_NOTE.md` + `scripts/frontier_frozen_stars_rigorous.py` | Self-consistent Hartree ground state on an `L^3` lattice with an attractive self-potential; measures an RMS width; claims "Fermi stabilization is lattice-size independent" and "persists in full 3D". **Directly adjacent prior art — read in full.** Its self-potential is a hand-imposed `-G sum(rho/r)` direct Coulomb sum with `r[r<1]=1`, not a solve of `Op phi = rho`, so it cannot address operator selection at all. Its own 3D table (`L=6..14`, widths `2.52..5.08`) shows the width growing with the box without saturation, and its "What is needed next" section concedes "3D lattices with `L > 14` to fully converge the 3D width". Its stability test is `width < 1.5 -> COLLAPSED`, which any delocalized state passes. Row `frozen_stars_rigorous_note` is `criticality: leaf`, `verdict: null`, in-degree 0. | **Open after matched-hit review.** The eigenstate-density source construction is prior art and is cited, not reinvented. The operator-family question and the depth diagnostic are untouched by it. Its 3D lattice-size-independence claim is contradicted by its own table; row R1/R2 of this cycle measures that directly rather than asserting it. |
| `docs/MATTER_SELF_FOCUSING_NOTE.md` | Two-pass self-focusing propagator, `S = L(1 - f_ext - lambda*(density[i]+density[j])/2)`, explicitly "Schrodinger-Newton / Gross-Pitaevskii-style". Outcome negative: equivalence-principle deviation only falls 123% -> 44%, family portability collapses. Source is the propagator density — the same object cycle 712 ruled out. Row is `leaf`, `verdict: null`. | **Prior negative attempt on the propagator-density source.** Confirms the successor direction (leave the propagator density) rather than duplicating it. |
| `docs/POISSON_BACKREACTION_LIVE_THRESHOLD_PACKET_NOTE_2026-05-29.md`, `docs/BACKREACTION_NOTE.md`, `scripts/backreaction_poisson.py` | Self-gravity backreaction harness; `f_self(y) = G sum_x |psi(x)|^2/|y-x|`, again a hand-imposed `1/r` sum, on a propagated packet. Bounded-support threshold table only; the old `G_crit ~ 0.011` claim is explicitly not restored. | **Non-matching.** Single imposed kernel, no operator family, no extent-versus-box measurement. |
| `docs/BOUND_STATE_SELECTION_NOTE.md` | Lattice bound states in an **external** Coulomb potential; `d <= 3` stability. Not self-consistent. Carries its own `missing_bridge_theorem` finite-to-continuum blocker. | **Non-matching** (external potential, not a self-consistent source). |

No hit states, for any operator, that the self-consistent extent or the
self-consistent well depth is or is not independent of the box; and no hit
solves `Op phi = rho` for more than one operator. The statement this cycle
proposes is **open after the matched-hit review**.

## Routes considered

| # | Route | Verdict |
|---|---|---|
| R-a | Keep the propagator density, drop the per-layer normalization | Ruled out by prior: PR #5693 row U9 measured total mass diverging `4.19e6 -> 1.38e20`. |
| R-b | Prescribe a fixed external localized source | Already done — that IS cycle 712 (PR #5693). Not self-consistent, so it cannot answer the parent note's question. |
| R-c | **Eigenstate density of the self-consistent ground state** — `H = -t A + V`, `rho = |psi_0|^2`, `Op phi = s g rho`, `V = phi <= 0` | **Selected.** Source is not the propagator density; extent is set by the kinetic-versus-self-attraction balance rather than by a propagation length or a normalization convention. |
| R-d | Add a saturating nonlinearity to the source (`rho/(1+rho)`) | Rejected: introduces an undeduced constitutive law, i.e. a new premise, forbidden by the no-new-axiom/no-new-primitive rule. |
| R-e | Fermionic multi-particle Hartree (the frozen-stars shape) | Deferred: Pauli pressure adds a second stabilizing mechanism that confounds the operator comparison. Single particle isolates the kernel's contribution, which is the variable under test. |

## Source-sign normalization

The parent row's `notes_for_re_audit_if_any` asks to "normalize alternative-operator
source signs consistently". This cycle does so explicitly: for each operator the
source sign `s` is fixed once, by the sign of `sum(phi)` on the first iterate, so
that every operator produces a non-positive (attractive) well. No operator is
handed a repulsive self-potential and then scored as unphysical.
