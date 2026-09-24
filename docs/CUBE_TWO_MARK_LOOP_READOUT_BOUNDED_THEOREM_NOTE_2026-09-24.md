---
claim_id: cube_two_mark_loop_readout_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Conditional mathematics of the explicitly supplied finite model and stated limits; numerical diagnostics alone do not prove the analytic limits or select physical dynamics."
upstream_dependencies:
  - minimal_axioms
  - first_event_instrument_corollary_bounded_theorem_note_2026-09-24
runner: scripts/cube_two_mark_loop_readout_2026_09_24.py
---

**Type:** bounded_theorem
**Status:** conditional mathematical result; unaudited.

The source argument below comes from the frozen submission, with the narrow corrections identified in the combined review receipt. Dated author-status statements, seals and numerical observations are historical provenance, not audit authority. The Hamiltonians, quantum state spaces, instruments, backgrounds and preparations are supplied model assumptions. Fresh canonical controls are distinguished from archived diagnostics; no numerical scan substitutes for the displayed proofs.

# A field loop in two consecutive formation marks

Personally derived conditional operator identity, 2026-09-23; independent
reconstruction pending. This concerns the supplied unit-rotor effective
formation instrument. Intervening fast motion is treated separately, not
discarded as an approximation on a finite laboratory interval.

## 1. Cube and first mark

Label cube vertices by binary 0..7, join vertices differing in one bit,
orient every edge low to high, and put A={0,3,5,6}, B={1,2,4,7}.
Use hard-core q=0,+1,-1, Gauss div(E)+1_A-q=0, and unit translations
U_e|E_e>=|E_e+1>. A positive record moving along an oriented edge contributes
U_e^dagger; moving against it contributes U_e. Hopping T has a minus sign.
The effective resolved creation is B_(e,sigma)=-P j_(e,sigma) Pi1 T P,
where j creates sigma at the tail and -sigma at the head and includes U_e^sigma.
The all-A-plus/B-vacant initial charge state leaves five independent integer
cycle fields. All statements below act on their full normalizable Hilbert
space, with no angle-eigenstate preparation.

Choose a first resolved mark on 0->1 with charge sigma1 at 0. The old positive
record at 0 must first move to 2 or 4. The two resulting charge states are
orthogonal, and both coefficients have unit modulus. Thus B1^dagger B1=2I
on the initial field space. Its normalized output is B1/sqrt(2) applied to
the field state. If the first edge mark is coherent, sum sigma1=+1,-1 and
normalize by 2; the four charge/path states are orthogonal.

## 2. A second marked edge and its interference

Choose the second resolved mark on 6->7, with charge sigma2 at 6. There are
two paths to its same final charge word:

1. Old record 0->2, then old record 6->4.
2. Old record 0->4, then old record 6->2.

The pair-creation factors U_01^sigma1 U_67^sigma2 are the same on both paths.
Their old-hop factors are respectively

    V1=U_02^dagger U_46,
    V2=U_04^dagger U_26.

The relative link word is the oriented square

    W_square=V1^dagger V2
             =U_02 U_26 U_46^dagger U_04^dagger,        (1)

which circulates 0->2->6->4->0 and has zero divergence. It is a physical
unitary on the initial Gauss-law field space. The normalized two-mark
operator for a specified sigma2 consequently has Gram operator

    (B2 B1/sqrt(2))^dagger (B2 B1/sqrt(2))
       = I + (W_square+W_square^dagger)/2.              (2)

For a normalized field density rho, its instantaneous second marked rate is

    kappa [1+Re Tr(rho W_square)].                     (3)

For a coherent first mark, the sigma1 final charge words remain orthogonal,
so the same normalized identity holds. If the second mark is coherent, its
two sigma2 ranges are orthogonal and its rate is twice (3). No classical
mixture of the old-hop paths has been substituted for the actual instrument.

## 3. Total immediate hazard and normalizable controls

Enumerating the other allowed second edges gives (2,3), (2,6), (3,7),
(4,5), (4,6), and (5,7). For each charge sign each has normalized squared
norm 1/2, with no alternative path to the same charge output. The second
edge (6,7) has the two interfering paths just described. All remaining
edges are blocked. Summing the twelve single-path signed marks and the two
signs on (6,7), for either first instrument and either second resolution,
gives the exact total hazard at the normalized first output:

    h(0)=kappa [8+2 Re Tr(rho W_square)].               (4)

This lies between 6 kappa and 10 kappa as an operator bound. A sharp integer
cycle-field state has <W_square>=0 and gives 8 kappa. The normalized field
states (|E0>+W_square|E0>)/sqrt(2) and
(|E0>-W_square|E0>)/sqrt(2), with E0 any allowed divergence-free integer field,
give <W_square>=+1/2 and -1/2, hence total hazards 9 kappa and 7 kappa.
They have finite support in the physical field basis. Extremal +/-1 loop
expectations would require nonnormalizable angle eigenstates; arbitrarily
close values can be approached by longer normalized wave packets.

The author check independently enumerates all one-hop-plus-creation paths
and their integer link shifts. Squaring the complete two-mark maps gives
exact Laurent coefficients: before first-output normalization the resolved
sum is 16I+2W_square+2W_square^dagger; the coherent first sum is twice that.
Each term is tested for Gauss invariance. Separately constructed finite
fiber jump matrices reproduce (4) at declared phases. These are exact path
coefficients plus floating controls, not evidence of a normalizable single
phase preparation.

## 4. What the identity does and does not show

The existing first-mark loss is a scalar on the field space; this particular
two-mark loss reads a gauge-invariant loop. Moving records and subsequent
formation can therefore carry field information in this supplied model.
The dependence is an instrument identity at zero intervening time. It is
not yet a finite-probability finite-time measurement protocol in the
epsilon->0 fast-motion regime. A window short compared with epsilon^2
suppresses motion but also makes a second event rare at fixed kappa.

The full no-event operator eta H2+delta H4-i Gamma/2 must be retained to
infer an ordinary-time waiting law. Initial author probes show phase-dependent
secular losses on the cube, but their finite fibers do not by themselves
establish a normalizable-state readout theorem. That averaging/preparation
bridge, the simultaneous finite-spin electric term, a large lattice limit,
and native model selection remain separate obligations. No empirical or
TOE claim follows from (1)-(4).


## Landing scope and No-Go Discipline Gate

- **N1 — Domain:** only the stated graph, sector, preparation, observation topology and order of limits.
- **N2 — Alternatives:** other laws, preparations, graphs and scaling paths are not excluded.
- **N3 — Imports:** supplied quantum and probability structures are mathematical assumptions, not repository axioms.
- **N4 — Dependencies:** companion arguments retain their explicit hypotheses and confer no audit grade.
- **N5 — Evidence:** exact finite controls and fresh numerical diagnostics corroborate proofs; floating computations are not interval enclosures. Archived diagnostic tables remain historical observations.
- **N6 — Resolution:** fixed-time, shrinking-time, fixed-index, growing-index and volume statements must not be interchanged.
- **N7 — Remaining work:** native model selection, physical implementation and empirical identification remain separate obligations.
- **N8 — Authority:** this source applies no audit verdict or retained grade.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository premise boundary; it does not derive the supplied quantum model.
- [first_event_instrument_corollary_bounded_theorem_note_2026-09-24](FIRST_EVENT_INSTRUMENT_COROLLARY_BOUNDED_THEOREM_NOTE_2026-09-24.md): conditional companion argument within its stated hypotheses.

## Source and verification

Source PR #8831, frozen head `b6eb31bedb3134dfacd8f4ab83cb7d96fc6dc953`. Complete original path dispositions and recovery branches are retained in the combined receipt. Review and affected-fix confirmation use the same primary session without subagents; no formal audit is claimed.

```bash
python3 scripts/cube_two_mark_loop_readout_2026_09_24.py
```

The runner executes selected controls in a fresh temporary directory and includes generated result JSON in its authenticated stdout. Source history and deferred diagnostics remain recoverable from the original branch.
