# DM PMNS finite seeded chamber-candidate diagnostic

**Date:** 2026-04-20
**Lane:** DM A-BCC / open import `I11`
**Type:** open_gate
**Status:** finite supplied-model numerical support; exact roots and completeness open
**Status authority:** independent audit lane only; no audit verdict is set here.
**Primary runner:** `scripts/frontier_dm_pmns_chamber_spectral_completeness_theorem_2026_04_20.py`

## Construction and supplied premises

The runner explicitly supplies `H_BASE`, `T_M`, `T_D`, `T_Q` and the Hermitian matrix family `H(m,delta,q)=H_BASE+m*T_M+delta*T_D+q*T_Q`. It supplies the angle target `(0.307,0.0218,0.545)` and row-label permutations. Ascending numerical eigendecomposition produces the observable residuals. The chamber cut `q+delta>=sqrt(8/3)` is stipulated in this diagnostic; it is not a derived physical selection law.

Two ordered-eigenvalue parameterizations use `(lambda1,log(lambda2-lambda1),log(lambda3-lambda2))`. Their supplied reduced equations and rational reconstruction formulas are evaluated numerically. Exceptional denominators, exact-root existence, equivalence on a complete domain and global exhaustion are not proved here. The unchanged solver checks are finite numerical diagnostics, not interval arithmetic.

## Exact execution scope

For each reduced branch the runner uses four named seed spectra plus 500 pseudorandom seeds. For `(2,1,0)`, RNG seed 20260420 draws lambda1 in [-10,5], gap12 in [.05,50], gap23 in [.05,5000]. For `(2,0,1)`, seed 20260421 uses lambda1 in [-10,10] and the same gap intervals. It calls SciPy `root(method="hybr",tol=1e-13)`, requires solver success and residual infinity norm at most 1e-9, and deduplicates eigenvalue triples within 1e-6. A search-start box is not a proven bound on roots or solver iterates.

The additional direct chamber search starts from the three named chamber candidates and 250 random starts per each of six permutations, RNG seed 20260420. Its coordinates draw m in [-5,35], delta in [-2,25], and positive slack in [1e-3,50]; q is reconstructed as `sqrt(8/3)-delta+exp(log_slack)`. The existing seeded and random solver tolerances, residual filters, 1e-6 deduplication and 1e-9 chamber allowance are unchanged. Exceptions and unsuccessful solves are skipped as before; this behavior cannot exclude unlocated solutions.

The checks compare the returned finite candidate lists and their supplied target residuals/chamber margins with named points. No PASS line establishes exact existence, uniqueness, an interval box, a complete bank or a physical PMNS source. Former literal-True boundary narration is unscored.

## Named points and counterexamples retained

The supplied chart coordinates `(m,delta,q)` include:

| Name | Row labels | Supplied point |
|---|---|---|
| Basin1 | `(2,1,0)` | `(0.657061342210,0.933806343759,0.715042329587)` |
| Basin2 | `(2,1,0)` | `(28.006188289565,20.721831213931,5.011599458305)` |
| BasinN | `(2,1,0)` | `(0.501997247472,0.853543345404,0.425916455114)` |
| BasinP | `(2,1,0)` | `(1.037883050950,1.433018557503,-1.329548075477)` |
| BasinX | `(2,0,1)` | `(21.128263668694,12.680028023619,2.089234805861)` |

The original runner retains all full-precision points, including the three other `(2,0,1)` seed spectra. BasinN and BasinP have negative supplied chamber margins (approximately -.3535 and -1.5295); they are retained counterexamples to identifying the whole supplied candidate list with its chamber subset. Basin1/2/X have positive floating margins. Signs at displayed decimals or located candidates are not interval-certified signs of exact roots.

## Unconfirmed contextual routes and open obligations

The [Krawczyk companion](DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_KRAWCZYK_CERTIFICATE_NOTE_2026-05-16.md) and [asymptotic source note](DM_PMNS_ASYMPTOTIC_SOURCE_NO_GO_NOTE_2026-04-20.md) are historical/contextual proposed routes. Their local-box or infinity-tail conclusions are not imported as discharged premises of this owner. This runner does not execute or certify those arguments. The [active-half-plane](DM_NEUTRINO_SOURCE_SURFACE_ACTIVE_HALF_PLANE_THEOREM_NOTE_2026-04-16.md) and [affine-family](DM_NEUTRINO_SOURCE_SURFACE_ACTIVE_AFFINE_POINT_SELECTION_BOUNDARY_NOTE_2026-04-16.md) notes provide context for the explicitly supplied formulas; no physical provenance is inferred from their titles.

Exact-root/enclosure certification, other branches, denominator coverage, infinity-tail exclusion, global completeness and physical selection all remain open. `I11` is not closed. The complete stronger note, runner and cache remain recoverable at `f00d5860eff9d8b6fdab9d5c3f2fc1d2fab63409` and in the repair evidence. Their claims and old PASS counts are historical, not current authority.

## Reproduction

Run `PYTHONPATH=scripts python3 scripts/frontier_dm_pmns_chamber_spectral_completeness_theorem_2026_04_20.py` with the declared 300-second bound. The canonical cache records the actual finite result and any failures; no expected result is substituted for execution.
