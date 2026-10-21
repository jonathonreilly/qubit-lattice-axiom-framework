# Conditional time-dimension arithmetic and its supplied bridges

**Date:** 2026-05-08; source boundary corrected 2026-10-21
**Claim type:** bounded_theorem
**Proposal allowed:** false
**Status authority:** source-note proposal only; audit verdict and effective status belong to the independent audit lane.
**Primary runner:** [`frontier_dt1_time_dimension_proof_walk_lattice_independence.py`](../scripts/frontier_dt1_time_dimension_proof_walk_lattice_independence.py)

## Claim

This note checks a limited arithmetic implication, not a derivation of time or the full dependency-independence claim formerly attached to this filename. With supplied spatial dimension `d_s=3`, a supplied reconstruction requiring even total Clifford dimension, and a separately supplied clock cap `0 <= d_t <= 1`, the nonnegative integer `d_t` equals one. The anomaly traces below are separate consistency checks on supplied matter content. They do not establish either reconstruction or the clock cap.

The [current axiom memo](MINIMAL_AXIOMS_2026-06-29.md) supplies the spatial cubic lattice, not these dynamics or reconstruction conditions. The current [anomaly/time parent](ANOMALY_FORCES_TIME_THEOREM.md) explicitly names hypercharge identification P-HY, anomaly consistency P-ABJ, opposite-chirality completion P-COMP, reconstruction on an irreducible Dirac factor P-REC, and the one-axis condition B-AXIS. These are conditional inputs, not consequences of the rational sums.

## Exact arithmetic

For the supplied left-handed quark/lepton doublets with multiplicities `(6,2)`, hypercharges `(1/3,-1)` and fundamental index `1/2`,

```text
Tr[Y]_LH = 6/3 - 2 = 0,
Tr[Y^3]_LH = 6/27 - 2 = -16/9,
Tr[SU(3)^2 Y]_LH = (1/2)(2/3) = 1/3,
Tr[SU(2)^2 Y]_LH = (1/2)(3/3 - 1) = 0.
```

Supplying right-handed singlets with hypercharges `(4/3,-2/3,-2,0)` and multiplicities `(3,3,1,1)` cancels the linear, cubic and mixed-colour traces after chirality signs are included. This exhibits one completion, not its uniqueness or physical selection. The [anomaly trace catalog](LH_ANOMALY_TRACE_CATALOG_THEOREM_NOTE_2026-04-25.md) provides context; the runner recomputes these sums directly.

For nondegenerate Clifford generators in dimension `n>=1`, moving a generator past the other `n-1` factors gives

```text
omega gamma_mu = (-1)^(n-1) gamma_mu omega.
```

Thus the volume element anticommutes for even n and commutes for odd n. On the supplied volume-grading/irreducible reconstruction surface, n must be even; with `n=3+d_t`, `d_t` is odd. Combining odd nonnegative `d_t` with the separate cap `d_t<=1` gives `d_t=1`. This elementary implication is not a derivation of the cap.

Centrality alone does not exclude all gradings on doubled representations. For `n=3`, let `Gamma_j=diag(sigma_j,-sigma_j)` and `J=[[0,I],[I,0]]`. Then `J^2=I` and `{J,Gamma_j}=0` for every j, while the volume remains central. The [Clifford volume theorem](CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md) and the parent's explicit irreducible reconstruction restriction must not be silently extended to that doubled carrier.

## Dependency boundary

The arithmetic runner does not compute a Wilson action, kinetic operator, continuum reconstruction, time metric or transfer dynamics. It checks arithmetic and source metadata separately. Its lack of runtime lattice-action inputs does not establish that its upstream physical interpretation is independent of all lattice machinery.

In particular, the current [Kawamoto–Smit source](STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md) proves a local phase/scalarization theorem under supplied P-KIN and P-SD; it expressly withdrew the old no-rooting premise. Its actual kinetic and phase hypotheses cannot be erased by citing its output as a black box. This source note therefore withdraws the older full-chain assertion that the proof path has no staggered-phase or lattice-action dependency. No claim about the truth or failure of that entire upstream theorem is made here.

The [emergent-dynamics open gate](ONE_TIME_DIMENSION_DT1_REDUCES_TO_EMERGENT_DYNAMICS_GATE_OPEN_GATE_NOTE_2026-06-17.md) owns the missing time-dynamics bridge. The [staggered realization gate](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md) remains separate. No source in this note is promoted by the arithmetic or the metadata checks.

## Reproduction and recovery

```bash
python3 scripts/frontier_dt1_time_dimension_proof_walk_lattice_independence.py
```

The runner checks exact anomaly sums, the volume parity identity and the conditional finite filter. Finite enumeration is a diagnostic; the parity-and-cap argument above gives the quantified result. `METADATA` lines check source presence/text only and cannot prove physical premises. No observed parameter enters these arithmetic checks.

The original argument and dated May fix records remain recoverable at commit `f24d17d97d372df977476e4a69674577f31af575`. The stable filename is retained for existing consumers, but its former claim of full-chain lattice independence is withdrawn. Auxiliary historical text-guard verifiers may require separate scope maintenance; their success is not mathematical authority.
