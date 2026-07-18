# Finite-Diamond Sampled Lüders Invariant-Record Model

**Date:** 2026-07-14

**Type:** meta

**Authority:** none. This is an exact finite conditional construction used to
test substrate completeness. It is not the framework law, an axiom proposal,
an audit verdict, a continuum theorem, or a claim that the construction is
uniquely selected by the current foundation.

## Purpose

The July tournament identified a process plus sampled local instruments plus a
post-formation record-preserving operation family as the leading expressive
substrate architecture. This note constructs that architecture exactly on a
finite causal diamond so that its positive claims can be tested rather than
inferred from the word “instrument.”

Call the model **FD-SLIR**: finite-diamond sampled Lüders invariant record.

## Supplied Finite Model

Fix a finite event DAG `D` embedded in a finite subset of `Z^3`. Each event
`e` has:

- nearest-neighbour finite support `S_e`;
- one fresh outcome-record site `x_e`;
- a physically recorded setting `k_e`;
- a sharp local PVM `{P_(e,r)^k}`; and
- causal parents in `D`.

Overlapping event supports are causally ordered. Incomparable ready events have
disjoint supports. For finite `F`, the carrier is supplied as

```text
A_F = tensor_(x in F) M_2(C).
```

This construction uses the generated finite carrier theorem as motivation but
does not claim the four axioms already supply physical tensor composition or
all PVMs.

### Complete records and reconstructed branch state

A complete record configuration `C` contains immutable preparation/program
records `b`, recorded settings `k_e`, and past outcome records `r_e`. No
independent wavefunction is added to the finite model. Instead,

```text
B_C     = K_n U_n ... K_1 U_1,
sigma_C = B_C rho_b B_C^dagger,
w(C)    = Tr(sigma_C),
```

where `rho_b` is reconstructed from the preparation record and the `K_i,U_i`
are reconstructed from the recorded program, settings, and outcomes. This
makes “state is records” true *inside this declared model*. The construction
does not prove that the live framework's generic record configurations already
carry tomographically complete preparation/process information.

### Ready context and atomic law

A context `kappa` is a ready antichain of events plus its recorded settings.
Readiness means every causal parent and setting record exists, each `x_e` is
open, and the overlap-order condition holds.

For a ready antichain `A`, disjoint local projectors commute. With the supplied
between-event unitary `U_A`, define

```text
K_r^kappa       = product_(e in A) P_(e,r_e)^(k_e) U_A,
p(r | C,kappa)  = Tr(K_r sigma_C K_r^dagger) / Tr(sigma_C).
```

Exactly one tuple `r` is sampled from this normalized distribution. The next
record configuration appends `(x_e,k_e,r_e)` for every event in `A`. Sampling
is physical law content here, not a theorem of the nonselective channel.

The local PVM menu is algebraic availability. The supported record-forming
extensions are exactly the outcomes with positive `p`. These two notions are
kept distinct.

### Record contract

After outcome `r` is appended, every later admissible continuation on its
record carrier must preserve the selected record sector. In the strongest
two-sided form, for the record projector `Q_r`,

```text
Phi^*(Q_r) = Q_r.
```

Then every Kraus operator of `Phi` is block diagonal in
`Q_r + (I-Q_r)`, and distinct record sectors cannot reconnect. For a formation
law with inflow from an open sector, the weaker branch-relative condition

```text
(I-Q_r) K_i Q_r = 0
```

is sufficient to make the formed record absorbing on its future cone. The
model tests both and does not equate them.

## Exact Finite Quantum Control

The Bell diamond uses

```text
|Phi+> = (|00>+|11>)/sqrt(2),
A_0=Z, A_1=X,
B_0=(Z+X)/sqrt(2), B_1=(Z-X)/sqrt(2).
```

The paired runner checks exactly:

```text
E_00 = E_01 = E_10 =  1/sqrt(2),
E_11 =                  -1/sqrt(2),
CHSH = 2 sqrt(2),
```

all local marginals are `1/2`, every context normalizes, and Alice/Bob update
order is immaterial because the local projectors commute. This is a finite
quantum sampled process, not a classical local hidden-variable append model.

## Two Real Reductions

### Sharp rank-one repeatability fixes the branch update

For a sharp rank-one outcome projector `P`, require the branch CP map to have
effect `P` and output support in `P`. Every branch Kraus operator is then
proportional to `P`; trace/effect normalization makes their squared
coefficients sum to one. Hence

```text
I_P(rho) = P rho P.
```

The Lüders update need not be a separate atom after sharpness, effect, and
exact repeatability are supplied. Those hypotheses remain physical content.

### Orthogonal Hilbert refinement fixes norm-square form

Let an unnormalized branch-vector weight be `W(v)=f(||v||)`. Unitary
invariance removes direction. If replacing `v` by `m` untouched orthogonal
branches `v/sqrt(m)` is physically equivalent after forgetting the refinement,
and weights add over those branches, then

```text
f(r) = m f(r/sqrt(m)).
```

With continuity and `f(1)=1`, the power solution is `f(r)=r^2`. The runner
checks that the equal-split condition uniquely selects exponent `q=2` within
`r^q`.

This is a genuine reduction of weight *form*, not a derivation from the four
axioms. It consumes generated Hilbert composition, physical ancilla/refinement
equivalence, event-weight additivity, continuity, and the link from weights to
sample frequencies. Record readout additivity is not probability additivity.

## Exact Nonuniqueness Controls

The construction also tests routes that do not select FD-SLIR:

1. One dephasing channel has both a projective record instrument and a
   random-unitary phase-token instrument with the same minimal Kraus count.
2. Two primitive bit-symmetric Markov kernels have the same unique stationary
   law and different correlations, so unique ergodicity does not select the
   atomic law.
3. One pre-boundary law admits final `P_0` and `P_1` boundary completions that
   select opposite histories.
4. `Phi+` and `Phi-` have the same local marginals and `ZZ` data but different
   future `XX` laws; a relational preparation record is necessary in that
   finite family.
5. All 16 deterministic local Bell response tables obey `|CHSH|=2`, so a
   measurement-independent classical record mixture cannot reproduce the
   model's quantum control.

## Ten-Field Closure Inside The Conditional Model

| field | FD-SLIR status |
|---|---|
| `DOMAIN` | supplied finite generated carrier and event DAG |
| `STATE` | record configuration, with branch state reconstructed by definition |
| `CONTEXT` | supplied recorded ready antichain/PVM settings |
| `ATOMIC_LAW` | supplied sampled Lüders kernel |
| `CONTINUATION` | derived transitive append closure |
| `AVAILABILITY` | PVM menu plus derived positive-weight supported extensions |
| `CONCURRENCY` | disjoint commutation; overlaps ordered by the supplied DAG |
| `RECORD` | supplied fresh outcome site and preservation scope; nonreconnection derived |
| `ACTUALITY` | one sampled tuple, explicitly supplied |
| `STATISTICS` | one-shot trace law supplied; cylinders and repeated-trial theorem derived under declared independent preparation |

The table is closure of a **supplied finite law**, not derivation of that law.

## TOE Boundary

FD-SLIR does not supply or prove:

- the exact physical full-lattice process or its unique selection;
- quasilocality of an action-to-transfer logarithm;
- a continuum interacting Lorentz/CPT limit;
- indefinitely renewed records in a bounded finite patch;
- universal clock calibration, lapse response, or formation-rate equality;
- a stress-energy/source definition and nonlinear metric backreaction;
- Standard Model matter, chirality, species, masses, or couplings; or
- that preparation/program/process information is already present in the live
  framework's generic records.

Its value is sharper: it proves that the proposed architecture is internally
coherent, quantum/Bell capable, and exact on a finite diamond, while making the
remaining physical atoms visible.

## Verification

Run:

```bash
python3 scripts/finite_diamond_sampled_luders_invariant_record_probe_2026_07_14.py
```

The runner's PASS total contains related controls and is not an independent
evidence count.
