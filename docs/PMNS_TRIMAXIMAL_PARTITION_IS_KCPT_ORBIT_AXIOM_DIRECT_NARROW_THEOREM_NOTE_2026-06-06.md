# PMNS Trimaximal Partition = the RECORD K/CPT-Orbit (Axiom-Direct) — Narrow Bridge Theorem

**Date:** 2026-06-06
**Claim type:** positive_theorem (narrow algebraic bridge; discharges a residual)
**Status:** unaudited candidate. Graph-visible only so the independent audit lane can
decide whether the candidate is retained.
**Primary runner:** [`scripts/trimaximal_partition_kcpt_orbit_runner.py`](../scripts/trimaximal_partition_kcpt_orbit_runner.py)
**Cached output:** [`logs/runner-cache/trimaximal_partition_kcpt_orbit_runner.txt`](../logs/runner-cache/trimaximal_partition_kcpt_orbit_runner.txt)

## Audit context

[`PMNS_TM2_TRIMAXIMAL_COLUMN_FROM_RECORD_CENTRAL_SECTOR_NARROW_THEOREM_NOTE_2026-06-05.md`](PMNS_TM2_TRIMAXIMAL_COLUMN_FROM_RECORD_CENTRAL_SECTOR_NARROW_THEOREM_NOTE_2026-06-05.md)
derives the PMNS trimaximal column as the corner overlap of the recorded `C_3`-singlet
central sector, "**modulo K-reality**" — citing
[`FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02.md`](FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02.md)
(`retained_bounded`) for the singlet⊕doublet partition.

That `retained_bounded` note labels **one** predicate "K-reality" but uses it for two
logically distinct jobs: (A) selecting the **2-block partition** (singlet⊕doublet) over
the 3-mode split, and (B) the **`δ=0` / `arg(b)=0` phase pin** (its "GAP A" is, by its
own wording, entirely about `arg(b)` / "the real axis" — the Brannen/chirality phase).
This note shows (A) is **axiom-direct** — it is the RECORD axiom's K/CPT-orbit clause,
not a posited K-real observable — so the trimaximal column is derived **modulo only the
retained `C_3` algebra**, and the genuine "K-reality" residual is (B), a *within-doublet*
phase that does not touch the singlet.

The framework's `2026-06-05` selector notes
[`RECORD_GENERATION_READOUT_TWO_SECTORS_2026-06-05.md`](RECORD_GENERATION_READOUT_TWO_SECTORS_2026-06-05.md)
and
[`GENERATION_RECORD_PARTITION_SELECTOR_2026-06-05.md`](GENERATION_RECORD_PARTITION_SELECTOR_2026-06-05.md)
(both `unaudited`) already state the partition is the K/CPT-orbit decomposition; this
note adds the class-A proof, the explicit separation from the `δ=0` phase, and the
discharge of the trimaximal column's caveat.

## Safe statement

The RECORD axiom (`MINIMAL_AXIOMS_2026-06-05`): *"the realized outcome is the `K`/CPT
orbit of the realized central sector."* On the retained 3-generation algebra
(`THREE_GENERATION_OBSERVABLE_THEOREM_NOTE`, `M_3(C)` with the `C_3[111]` cycle), the
central modes of the `C_3`-commutant are the trivial/singlet mode (real) and the two
faithful modes `ω, ω²`. Let `K` = the K/CPT conjugation (complex conjugation in the
character basis).

**Theorem.**

1. **K-orbit structure.** `K` exchanges the two faithful modes (`K P_ω K = P_{ω²}`) and
   fixes the singlet (`K P_0 K = P_0`).

2. **Partition = real Wedderburn, axiom-direct.** The K/CPT orbits of the central modes
   are exactly two — `{singlet}` and `{ω, ω²}` — giving the partition

   ```text
   P_0 = J/3            (singlet, rank 1, = |W><W|, W = (1,1,1)/sqrt(3))
   P_1 = P_ω + P_{ω²}   (doublet, rank 2, real)
   ```

   with `P_0 + P_1 = I`, `P_0 P_1 = 0`. This is the real Wedderburn decomposition
   `R[Z_3] = R ⊕ C`. It follows from the axiom's "outcome = K/CPT orbit" clause applied
   to the retained `C_3` central modes — **no posited K-real monitored observable is
   used.**

3. **The 3-mode split is K-broken.** Resolving `ω` from `ω²` (the 3-mode partition)
   strictly requires the **K-odd** operator `i(C − C²)` (`K X K = −X`, T-violating),
   which the record never supplies (the recorded outcome is a K-orbit). So the 2-block
   partition is the *only* record-compatible coarseness.

4. **The trimaximal column is fixed by the partition alone.** The column is the
   singlet's corner overlap `|<corner_a|W>|² = 1/3`. `W` is the (real) singlet mode, so
   this is `1/3` independently of the entire doublet/mass structure — in particular
   independent of the within-doublet phase `δ = arg(b)`. Varying `δ` over `[0, 2π)`
   leaves `W` an eigenvector and the column unchanged.

5. **Discharge.** Therefore the PMNS trimaximal column is derived **modulo only the
   retained `C_3` algebra** (a `G1` input), with the coarseness (`G2`) supplied by the
   axiom's K-orbit clause. The "modulo K-reality" caveat conflated (A) the axiomatic
   partition with (B) the `δ=0` phase pin; (B) is a *within-doublet* residual (the
   Brannen/chirality phase) and is **irrelevant to the singlet's overlap**.

## Proof

(1)–(2): `K` is complex conjugation; `P_ω = |f_1><f_1|` with `f_1` the `k=1` DFT mode,
and `conj(f_1) = f_2` (the `k=2` mode), so `K P_ω K = P_{ω²}`; `f_0 = W` is real so
`K P_0 K = P_0`. The orbit sums `P_0`, `P_1 = P_ω + P_{ω²}` are the rank-1/rank-2 real
idempotents; `P_0 = (I + C + C²)/3 = J/3`. (3): `C + C² = J − I` is K-even and acts as
the scalar `−1` on `P_1` (cannot split it); `i(C − C²)` is K-odd with distinct
eigenvalues on `P_1`. (4): `W` is real and democratic, `|<e_a|W>|² = 1/3`; any operator
that commutes with `P_0` keeps `W` an eigenvector, and the runner confirms this for a
`δ`-parametrized family across `[0, 2π)`. (5) is the synthesis. The runner checks
(1)–(4) to `1e-9`/`1e-12`.

## Boundary

This note does **not**:

- **Re-derive the `C_3` central modes** — that is the retained input
  (`THREE_GENERATION_OBSERVABLE_THEOREM`, `G1`). What is added is that the *coarseness*
  (`G2`) is the axiom's K-orbit, not an admitted posit.
- **Derive the `K`/CPT conjugation** — it is named by the RECORD axiom (a fixed K/CPT is
  part of the readout context); identifying it with the physical CPT is the axiom's, not
  this note's.
- **Address the `δ=0` phase pin** — the genuine "K-reality"-labeled residual (the
  Brannen/`arg(b)`/chirality phase) is left exactly where it was; this note only shows it
  is *within the doublet* and does not enter the trimaximal column.
- **Touch the measure / Koide `r`** — the singlet/doublet *weight* is a separate
  registered datum (`G3`), unaffected here.

## Forbidden imports check

No new axiom or import. The only structures used are the RECORD axiom's verbatim
"outcome = K/CPT orbit" clause, the retained `C_3` central modes, and finite matrix
algebra (`C`, the DFT modes, `J`). The K/CPT conjugation is the axiom's; the `C_3`
algebra is retained. The note *removes* an apparent residual (the "modulo K-reality"
caveat) rather than adding structure.

## Runner check breakdown

Class A finite-dimensional algebra: the K-orbit action on the central modes; the
singlet⊕doublet real-Wedderburn idempotents (`P_0 = J/3`, `P_1` rank-2 real, complete
orthogonal); the K-even/K-odd separation (`C+C²` real vs `i(C−C²)` T-violating, the
latter being what a 3-mode split needs); the singlet overlap `= 1/3`; and its invariance
under the within-doublet phase `δ`. Expected `runner_check_breakdown = {A: N, B: 0,
C: 0, D: 0, total_pass: N}`.

## Honest auditor read

The runner is explicit class-A matrix algebra to `1e-12`. The load-bearing content is
elementary `C_3` real-representation theory: the K/CPT orbit of the faithful conjugate
pair is the real doublet, so the record-compatible partition is `R ⊕ C` with no posited
observable. The value is the *separation*: the retained einselection note's single
"K-reality" predicate covers both the (axiomatic) partition and the (residual) `δ=0`
phase; pulling them apart shows the PMNS trimaximal column rests only on the retained
`C_3` algebra, while the genuine residual (`δ=0`) is a within-doublet phase irrelevant to
it. The note does not derive `δ=0`, the K/CPT identification, or the Koide weight; it
discharges precisely the partition-coarseness caveat. Effective status remains
`unaudited` until the audit lane assigns one.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/trimaximal_partition_kcpt_orbit_runner.py
```
