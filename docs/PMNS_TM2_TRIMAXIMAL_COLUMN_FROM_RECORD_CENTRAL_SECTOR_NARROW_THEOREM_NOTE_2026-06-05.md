# PMNS TM2 Trimaximal Column = the Recorded C3-Singlet Central Sector — Narrow Bridge Theorem

**Date:** 2026-06-05
**Claim type:** positive_theorem (narrow bridge + axiom-derivability map)
**Status:** unaudited candidate. Graph-visible only so the independent audit lane
can decide whether the candidate is retained.
**Primary runner:** [`scripts/pmns_tm2_trimaximal_from_record_central_sector_runner.py`](../scripts/pmns_tm2_trimaximal_from_record_central_sector_runner.py)
**Cached output:** [`logs/runner-cache/pmns_tm2_trimaximal_from_record_central_sector_runner.txt`](../logs/runner-cache/pmns_tm2_trimaximal_from_record_central_sector_runner.txt)

## Corrigendum (2026-09-30)

Source-scope correction. Status fields above are unchanged; effective status
stays with the independent audit lane. Checks are same-family (Claude Sonnet
5.5), not an independent referee.

**`theta_12` is not free.** The Boundary lists `theta_13` and `theta_12` (the
solar angle) as free within-doublet data "matched to experiment". That holds
for the doublet block alone, not for the PMNS pattern. With the recorded
singlet `W` as the second PMNS column and `U_e = I`,
`|U_e2|^2 = s12^2 c13^2 = 1/3`, so `s12^2 = 1/(3 c13^2)` is fixed by `s13^2`.
The TM2 pattern has one free parameter, not two.

**Data.** That sum rule gives `s12^2 = 0.3409` at `s13^2 = 0.0222` and is at
least `1/3` for every `s13^2`. The NuFIT-6.1 3-sigma range for `s12^2` the
repository already quotes
(`PMNS_DCP_FORECAST_STANDING_DEGRADES_UNDER_NUFIT6_BOUNDED_NOTE_2026-06-08.md`,
line 28) is [0.2893, 0.3295]. The TM2 form is outside it at every `s13^2`, and
a trimaximal electron-row entry `1/3` is outside the image of the quoted
rectangle at every mass position (`nu_1`, `nu_2`, `nu_3`). arXiv:2512.03809
(Ding, Li, Lu, Petcov; the statement is in the body text, not the abstract)
reports the TM2-type patterns disagree with the first JUNO `sin^2 theta_12`
measurement at the 3.6 sigma level. The "Verdict: repo-native, modulo the
`K`-reality predicate" says where the algebra comes from; it is not agreement
with data, and this note does not supply a viable PMNS matrix.

**`theta_13` free holds for the dephasing `D` alone.** Item 3 of the Theorem is
unchanged for `D`. It does not survive adding the `mu`-`tau` residual as the
unitary invariance `[M_nu, P_23] = 0` that the sibling magic-residual note
pairs with this column: a `V_4`-invariant `M_nu` has `theta_13 = 0` (see the
Corrigendum in
`PMNS_TM2_MAGIC_RESIDUAL_DYNAMICAL_GENERATOR_NARROW_THEOREM_NOTE_2026-06-05.md`).

**What stands.** The algebra and the runner checks: `D(M)` has `W` as an
eigenvector for every pre-record `M`; `P_0 = J/3`; the corner overlaps `1/3`;
the `K`-reality 2-block statement. Not standing: any reading of the TM2 form as
a viable description of the measured PMNS matrix.

**TM1.** TM1 (first column `xi = (2,-1,-1)/sqrt6`) is a different literature
pattern; the same paper finds it inside the JUNO 3-sigma range. This repository
does not supply it: the record dephasing fixes `W` as a column, not `xi`. The
2026-08-05 historic intake of the April sum-rule note
(`docs/historic_intake/HISTORIC_KOIDE_PMNS_SUM_RULES_NOTE_2026_04_21_INTAKE_NOTE_2026-08-05.md`,
audit unset) lists TM1 as not fitting its NuFIT-based comparator (0.684 against
2/3) and TM2 as not fitting (0.294 against 1/3); that note does not use the
JUNO measurement. Nothing here adopts TM1 as a framework result.

**Evidence.** `scripts/pmns_tm2_scope_check_solar_angle_outside_nufit61_and_v4_commutant_forces_theta13_zero_2026_09_30.py`
(26 PASS, 0 FAIL).

## Audit context

The conditional TM2 lemmas
[`PMNS_TM2_RESIDUAL_CONSEQUENCE_BOUNDED_NOTE_2026-05-26.md`](PMNS_TM2_RESIDUAL_CONSEQUENCE_BOUNDED_NOTE_2026-05-26.md)
and
[`PMNS_TM2_MAGNITUDES_CONDITIONAL_BOUNDED_NOTE_2026-05-26.md`](PMNS_TM2_MAGNITUDES_CONDITIONAL_BOUNDED_NOTE_2026-05-26.md)
(`retained_bounded`) **assume** a trimaximal PMNS column `|U_x|^2 = 1/3` and do not
derive it. The sibling note
[`PMNS_TM2_MAGIC_RESIDUAL_DYNAMICAL_GENERATOR_NARROW_THEOREM_NOTE_2026-06-05.md`](PMNS_TM2_MAGIC_RESIDUAL_DYNAMICAL_GENERATOR_NARROW_THEOREM_NOTE_2026-06-05.md)
showed the trimaximal column would follow if the **pre-record** neutrino operator
`M_nu` preserved the democratic vector `W = (1,1,1)/sqrt(3)`, but the framework's
own DM-neutrino source operator **breaks** `W` (nonzero singlet-doublet slots), so
forcing the pre-record operator looked obstructed.

This note removes the obstruction by reading the column off the **record**, not the
pre-record operator. The framework's RECORD axiom states (`MINIMAL_AXIOMS_2026-06-05`):

> "Given a readout context with a finite central-sector decomposition and a fixed
> `K`/CPT conjugation, **the realized outcome is the `K`/CPT orbit of the realized
> central sector.**"

So the physical observable is which **central sector** is recorded; inter-sector and
within-sector coherence are not part of the outcome ("A record supplies no ...
within-sector data"). For the 3-generation `C_3` algebra the central decomposition is
**singlet** (`W`, the `C_3`-trivial mode) `(+)` **doublet** (2-dim). The trimaximal
column is then the corner (flavor) overlap of the recorded singlet sector, and the
pre-record `W`-breaking is simply **not recorded**.

## Safe statement

On the `hw=1` triplet `V_1` with `W = (1,1,1)/sqrt(3)`, let `P_0 = |W><W| = J/3` (the
`C_3`-singlet central-sector projector) and `P_1 = I - P_0` (the doublet sector). Let
the **record map** (RECORD outcome structure on operators) be the dephasing channel

```text
D(M) = P_0 M P_0 + P_1 M P_1.
```

**Theorem.**

1. **(Trimaximal column = recorded singlet overlap.)** The corner (flavor) overlaps of
   the singlet sector are `|<corner_a|W>|^2 = 1/3` for `a = 1,2,3`. Hence whenever the
   neutrino is recorded in the singlet central sector, its observable column is exactly
   trimaximal — independent of any pre-record operator.

2. **(Pre-record `W`-breaking is not recorded.)** For an arbitrary pre-record Hermitian
   `M_nu` (which may have `||P_0 M_nu P_1|| != 0`, i.e. break `W`), the recorded operator
   `D(M_nu)` has `W` as an eigenvector and yields an exact trimaximal PMNS column (with
   `U_e = I`). The pre-record singlet-doublet coherence is dropped by `D`.

3. **(`theta_13` is record-blind / free.)** `D` does not touch the within-doublet block
   `P_1 M_nu P_1`; the doublet eigenvectors (hence `theta_13`, `theta_12`) are set by the
   pre-record within-sector data, which the RECORD axiom explicitly does not record. So
   the recorded pattern is **TM2** (one trimaximal column + free `theta_13`), not the
   TM3 over-prediction.

4. **(`K`-reality selects the 2-block partition.)** A `K`-real `C_3`-invariant monitored
   observable lies in `span_R{I, C + C^2}`, and `C + C^2 = J - I` has spectrum
   `{2, -1, -1}` — the singlet is isolated, the doublet **degenerate**, so `K`-real
   monitoring resolves exactly the singlet `(+)` doublet partition. Splitting the doublet
   into the 3-mode partition strictly requires the `K`-odd `i(C - C^2)`.

5. **(Monitored observable is the native double-shift coupling.)** `C + C^dagger = J - I`
   is the retained_bounded native second-order double-shift corner coupling, whose
   eigenbasis is the magic-reflection partition `S = 2P_0 - I` of the sibling note. The
   same native object `J - I` plays a dual role: its **time evolution** generates the
   magic `S` (dynamical generator note), and its **record** gives the central-sector
   partition (this note).

## Proof

(1) `W` has equal-magnitude components `1/sqrt(3)`, so `|<e_a|W>|^2 = 1/3`. (2)-(3)
`D(M) = P_0 M P_0 + P_1 M P_1` is block-diagonal in `span{W} (+) doublet`, so `W` is an
eigenvector of `D(M)`; with `U_e = I` the corresponding PMNS column is `W`, magnitudes
`1/3`. The doublet block `P_1 M P_1` is preserved verbatim, so its eigenvectors and the
implied `theta_13` are unconstrained by `D`. (4) `eig(C + C^2) = {2 Re(omega^k)} =
{2, -1, -1}`; `C + C^2` acts as the scalar `-1` on the doublet (degenerate), so a
`K`-real `C_3`-invariant observable cannot split it; `i(C - C^2)` has distinct eigenvalues
on the doublet. (5) `I + C + C^2 = J` gives `C + C^2 = J - I`; `S = 2P_0 - I` commutes
with `P_0, P_1`. The runner checks all of (1)-(5) plus robustness across 200 random
pre-record operators, to `1e-9`/`1e-12`.

## Axiom-derivability map (is this repo-native?)

This is the load-bearing question: does the result follow from `{LATTICE, QUANTUM,
RECORD}`, or need a new axiom? Piece by piece:

| Load-bearing piece | Status | Supplied by |
|---|---|---|
| (a) observable = recorded central sector; inter-/within-sector coherence not recorded | **directly in the RECORD axiom** (outcome structure) | `MINIMAL_AXIOMS_2026-06-05` (`meta`). The *dynamical* "how dephasing happens" is explicitly disclaimed. |
| (b) `M_3(C)` + `C_3` generation structure on the 3 corners | **derived / retained** | `THREE_GENERATION_OBSERVABLE_THEOREM_NOTE` (`retained`), LATTICE+QUANTUM-native |
| (c) singlet `(+)` doublet isotypic split; singlet `= W`; corner overlap `= 1/3` | **derived / verified algebra** | `C_3` rep theory; `P_0 = J/3` (this runner) |
| (d) which sub-algebra is monitored -> the 2-block (not 3-mode) partition | **modulo the named `K`-reality predicate** | `FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02` (`retained_bounded`) |
| (e) a *dynamical* decoherence derivation forcing the singlet sector | **open** (not needed for the column) | record-formation notes are `unaudited`, conditional on a quantum-Darwinism bridge |

**Verdict: repo-native, modulo the `K`-reality predicate. No new axiom is required for
the trimaximal column.** The "observable = recorded central sector, coherences not
recorded" content is the RECORD axiom's outcome structure verbatim; the `C_3`
decomposition and the `1/3` overlap are derived/retained. The single residual that gates
"the singlet is a coherent recorded sector" is `K`-reality, an already-tracked admitted
predicate (the same `delta=0` / transpose-symmetry / chirality pin; `retained_bounded`
[`KOIDE_EMERGENT_TIME_ETA_CONJUGATION_PARITY_BOUNDED_NOTE_2026-05-30.md`](KOIDE_EMERGENT_TIME_ETA_CONJUGATION_PARITY_BOUNDED_NOTE_2026-05-30.md)
shows the emergent-time mechanism is conjugation-even and so does not by itself deliver
it).

## Boundary

This note does **not**:

- **Derive the `K`-reality predicate.** It is an admitted residual (the standing
  `delta=0` / chirality pin), shared with the charged-lepton readout. The column rides on
  it (it is what makes the singlet a coherent recorded sector).
- **Give the within-doublet observables (`theta_13`, `theta_12`, the solar angle).** These
  are within-sector data the RECORD axiom does not record; here they are free and matched
  to experiment, not derived. (This is the reframe working as intended: match the record,
  do not force pre-record values.)
- **Give the `r = 1/2` doublet/singlet weight (Koide `Q = 2/3`).** That is a separate,
  harder gap (block-counting vs Born/dimension weighting); the trimaximal `1/3` column is
  a pointer-*state* fact and is independent of it. The retained Born/tracial measure
  weights blocks by dimension (`-> r = 1`); the column does not depend on resolving this.
- **Supply a dynamical decoherence derivation.** The note uses the RECORD axiom's outcome
  structure (recorded = central sector), not a process argument; a Darwinism-style
  dynamical derivation is open and `unaudited`.
- **Establish the neutrino-specific readout context.** That the neutrino is recorded in
  the `C_3` central decomposition is the natural extension of the retained_bounded
  generation einselection; neutrino-specific monitoring is not separately established.

## Forbidden imports check

No new axiom or imported structure is asserted. The result uses only `{LATTICE, QUANTUM,
RECORD}` plus retained `C_3` structure: the record map `D` is the RECORD axiom's outcome
identity (recorded = central sector) realized on operators; `P_0 = J/3`, `C`, `J - I` are
finite matrices on the existing `hw=1` carrier; `J - I` is the retained_bounded native
double-shift coupling. The one residual, `K`-reality, is a **pre-existing** admitted
predicate (not introduced here), explicitly named and shared with the charged-lepton pin.
No new axiom, no new import.

## Runner check breakdown

Class A finite-dimensional algebra only: the record/dephasing channel `D` and its
idempotence, `P_0 = J/3` and the `1/3` corner overlaps, the pre-record-`W`-breaking ->
recorded-trimaximal-column washout (single case + 200 random pre-record operators),
`theta_13`-free within-doublet, the `K`-reality 2-block-vs-3-mode selection
(`C + C^2` degenerate doublet vs `i(C - C^2)` split), and the `J - I` / magic-`S`
partition link. Expected `runner_check_breakdown = {A: N, B: 0, C: 0, D: 0,
total_pass: N}` where `N` is the printed `PASS` count in the cache.

## Honest auditor read

The runner is explicit class A matrix algebra, checked to `1e-9`/`1e-12`, with a 200-case
robustness sweep. The positive content — trimaximal column = recorded singlet sector,
pre-record `W`-breaking not recorded, `theta_13` record-blind — is exact and follows from
the RECORD axiom's outcome structure plus the retained `C_3` decomposition. The
derivability map states honestly what is axiom-direct (the outcome structure), what is
derived/retained (the `C_3` decomposition and `1/3`), what is modulo a named admitted
predicate (`K`-reality, the standing `delta=0`/chirality pin), and what is open and not
needed here (a dynamical decoherence derivation; the `r = 1/2` weight; the neutrino
readout context). The note does not close TM2 end to end; it derives the **trimaximal
column** as repo-native modulo `K`-reality and locates every residual. Effective status
remains `unaudited` until the independent audit lane assigns one.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/pmns_tm2_trimaximal_from_record_central_sector_runner.py
```
