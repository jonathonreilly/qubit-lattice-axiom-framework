---
claim_id: exact_microscopic_energy_at_a_star_birth_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Conditional mathematics of the explicitly supplied finite model and stated limits; numerical controls do not establish physical selection or extend the analytic quantifiers."
upstream_dependencies:
  - minimal_axioms
  - local_compensation_common_field_record_limit_bounded_theorem_note_2026-09-24
runner: scripts/exact_microscopic_energy_at_a_star_birth_2026_09_24.py
---

**Type:** bounded_theorem
**Status:** conditional mathematical result; unaudited.

The complete source argument and its selected companion proofs follow, with the narrow corrections documented in the combined review. Dated author-status statements, seals and numerical observations are historical provenance, not audit authority. Quantum spaces, Hamiltonians, instruments, preparations and resource assumptions are supplied mathematical premises. Fresh controls corroborate the proofs within their scope.

# Exact microscopic energy at an unchanged star birth

Author status: personal conditional construction, 2026-09-24. This author
packet precedes independent reconstruction. It establishes an exact fact
inside the supplied compensated Hamiltonian and formation instrument. It
does not identify heat, an autonomous reservoir, or a native physical law.

## 1. Why this is a different energy question

Earlier cube calculations concern the effective Hamiltonian `K D + delta H4`.
The finite-volume slow-density limit does not transfer expectations of the
microscopic Hamiltonian, whose scale is `delta epsilon^-4`. Here the initial
state is prepared in its exact low spectral cluster, so an initially large
bare-state energy cannot explain the result. The original microscopic jump
is retained. A four-site star is enough for an exact diagnostic; it has only
one possible birth and is not evidence for repeated formation.

## 2. Supplied model and complete physical sector

Take one A vertex 0 and three B leaves 1,2,3, with oriented edges `(0,b)`.
Use the same hard-core local states `q in {-1,0,+1}`, normalized integer-spin
link matrices `S^±/sqrt(S(S+1))`, outward transport `F`, and formation marks
`j_(0b),sigma` as the parent formation model. The transport moves the occupied
A charge to an empty B and changes `E_0b` by `-q_0`; the formation mark requires
both endpoints empty, creates charges `(sigma,-sigma)`, and changes `E_0b` by
`sigma`. Coherent marks are `j_(0b),+ + j_(0b),-`; resolved marks retain the two
outcomes. No rate or mark has been changed.

The Gauss law is `div E = q - 1_A`, hence on this tree

`E_0b = -q_b`, and `sum_x q_x = 1`.

There are four physical one-record states and twelve physical three-record
states. All fields are 0 or ±1, so these sectors are the same for every integer
`S >= 1`. Every allowed transport or formation step changes a field from 0 to
±1 or back. Its normalized spin coefficient is exactly one, including `S=1`.
Let `W=h_0` project onto an empty A vertex. On every active outward edge the
empty B implies `E_0b=0`. Consequently the finite-spin and rotor diagonal
outward-hop weights agree. The supplied local compensation, with the gate
being an empty product on this graph, is exactly

`C_S = F†F`.

This is a specialization of the previously supplied compensation, not a new
counterterm. In each fixed-number sector the dimensionless microscopic matrix
and the physical Hamiltonian are therefore

`h_epsilon = W - epsilon(F+F†) + epsilon² F†F`

`H_epsilon = delta epsilon^-4 h_epsilon`.

Since `WF=F`, `F†W=F†`, and `W²=W`,

`h_epsilon = (W-epsilon F)†(W-epsilon F)`.

The state-space and operator matrices are constructed directly in the companion
control, which also checks the Gauss law and every nonzero field increment.

## 3. Exact zero-energy preparation

Write `|A>` for the all-A-occupied state with `q_0=+1`, and `|b>` for the
state with the old + record on B leaf b. All are physical Gauss states with
the fields just specified. Since `F|A> = |1>+|2>+|3>`, the exact normalized
low-cluster state is

`|psi_epsilon> = (|A> + epsilon(|1>+|2>+|3>))/sqrt(1+3epsilon²)`.

It is annihilated by `W-epsilon F`, and therefore has exactly zero microscopic
energy and energy variance. It is also the positive-overlap low-cluster
isometry applied to `|A>`. It approaches `|A>` in norm as epsilon tends to zero.
This preparation is an explicit premise. In contrast, the undressed `|A>` has
energy `3delta/epsilon²`, is annihilated by all formation marks, and has initial
dissipative energy derivative zero. The two preparations must not be conflated.

## 4. Actual resolved birth and microscopic spectral weight

Choose the edge `(0,1)` and mark `sigma=+1`. Only `|2>` and `|3>` in the prepared
state can jump. Define physical states `v_2` and `v_3` with A charge +1, B1 charge
-1, and the old + record on B2 or B3 respectively. Then

`j_+ |psi_epsilon> = epsilon (|v_2>+|v_3>)/sqrt(1+3epsilon²)`.

The intensity under the unchanged jump `sqrt(kappa)/epsilon j_+` is

`r_+ = 2kappa/(1+3epsilon²)`.

The normalized actual output is `|v_+> = (|v_2>+|v_3>)/sqrt(2)`, independent of
epsilon. Both outward hops of its A record lead to the same full-B state.
Thus `||F v_+||²=2` and, since `W v_+=0`,

`<H_epsilon>_(v_+) = 2delta/epsilon²`.

For the opposite resolved sign the A record is -1, B1 is +1, and the old record
is still +1. Hopping the A record into the remaining vacancy produces distinct
full-B charge states for the two paths. The normalized output `v_-` consequently
has `||F v_-||²=1`, giving

`r_- = 2kappa/(1+3epsilon²)`,

`<H_epsilon>_(v_-) = delta/epsilon²`.

These are energies of the full microscopic Hamiltonian, not expectations of W.
Both actual outputs have bare W probability exactly zero. The relevant high
spectral cluster is rotated relative to W.

Indeed, in the twelve-dimensional N=3 space, `F F†=3W`. Direct block
multiplication gives the exact spectral identity

`h_epsilon² = (1+3epsilon²) h_epsilon`.

Its trace is `3(1+3epsilon²)`. Its spectrum is therefore zero with multiplicity
nine and `1+3epsilon²` with multiplicity three. The physical high energy and
its spectral projector are

`E_hi = delta epsilon^-4 (1+3epsilon²)`,

`P_hi = h_epsilon/(1+3epsilon²)`.

For an output with `c=||F v||²`, the exact spectral weight, mean and variance are

`p_hi = c epsilon²/(1+3epsilon²)`,

`mean(H_epsilon) = c delta/epsilon²`,

`Var(H_epsilon) = c delta² epsilon^-6 [1+(3-c)epsilon²]`.

Here `c=2` for the + resolved mark and `c=1` for the - resolved mark. The high
spectral weight vanishes even while the mean and variance diverge. The projector
is idempotent and orthogonal; the identities above involve the complete
physical spectrum, without a spectral truncation or a numerical tolerance.

## 5. Coherent instrument and total energy balance

For the coherent edge mark, the two resolved output vectors occupy orthogonal
A-charge sectors and each has squared norm two before normalization. Their F
images are also orthogonal, since the position of the unique negative B charge
differs. The coherent normalized output thus has

`c=3/2`, `r_coh=4kappa/(1+3epsilon²)`,

`mean(H_epsilon)=3delta/(2epsilon²)`.

The same spectral probability and variance formulas apply with `c=3/2`.
This is not a claim that coherent and resolved conditional states agree.

Sum the gain over all three edges, with either the six resolved marks or the
three coherent marks. The input energy is zero and `H_epsilon psi_epsilon=0`,
so the entire anticommutator contribution to the energy derivative vanishes.
The Hamiltonian contribution vanishes identically. The full GKLS energy
balance at this dressed input is exactly

`d <H_epsilon>/dt |_(t=0) = 18 kappa delta / [epsilon²(1+3epsilon²)]`.

This is a finite positive number for every fixed epsilon. It is not an all-time
heating statement. Energy change here is generated by the supplied open-system
instrument; no external work source or reservoir energy has been modeled.

## 6. Relation to the effective description and limits

For this graph there is no grade-two hole sector: `Z=0`. The compensation has
`C0=M=F†F` on P and `C1=0` on the empty-A space. Hence the corrected general
formula gives `H4C=M²-{M,M}/2=0`. On P, the physical active-edge electric
operator D is zero because all its active edges have zero field. The target
Hamiltonian `K D + delta H4` is therefore exactly zero throughout the physical
P space. The same target formation B is `jF P` and has the output amplitudes
used above.

Under the joint scaling `epsilon² S(S+1)=delta/K`, with positive fixed K and
delta, the exact conditional microscopic energy is `c K S(S+1)` whereas the
target energy is zero. This scaling does not change any star matrix element.
The high spectral probability tends to zero. The density approximation and
the failure of energy-moment identification are thus compatible.

The graph has no independent cycle flux and only one possible formation. The
result establishes this energy-accounting distinction for an actual original
instrument mark in a supplied, exactly soluble physical sector. It neither
proves a cube asymptotic nor gives a no-go for autonomous dilations. It does not
say that the microscopic model is ill-defined: at fixed S and epsilon all
spaces and energies here are finite. It identifies a missing energy component
that a physical closed-system interpretation must explicitly account for.

## 7. Evidence and remaining obligations

`exact_star_energy.py` constructs all 16 physical states, their exact matrices,
the dressed zero-energy input, both instruments, and the full spectral
projector using symbolic epsilon. `EXACT_STAR_ENERGY_RESULTS.json` records the
bases, F matrices, physical outputs and exact formulas. Its source is personal
author evidence, not independent confirmation. The first development run used
a structural rather than symbolic trace equality; that non-scientific assertion
failure and its correction are preserved in `DEVELOPMENT_FAILURES.md`.

Independent reconstruction should rebuild the physical sector, compensation,
full spectrum and actual jump outputs from the model definitions before reading
this note. General graph leakage coefficients, stability under the proposed
electric completion, and energy-conserving reservoir constructions remain open.


## Landing scope and No-Go Discipline Gate

- **N1 — Domain:** the specified graph, sector, input, observable and order of limits.
- **N2 — Alternatives:** other models, initial states, instruments and resource scalings remain possible.
- **N3 — Imports:** supplied quantum and probability structures are mathematical assumptions, not new repository axioms.
- **N4 — Dependencies:** companion results retain their hypotheses; no retained grade is imported.
- **N5 — Evidence:** exact finite controls and fresh numerical diagnostics corroborate the argument; floating computations are not interval enclosures.
- **N6 — Resolution:** density convergence, energy convergence, initial power, finite time and volume limits are distinct statements.
- **N7 — Remaining work:** native selection, physical implementation and empirical identification remain separate obligations.
- **N8 — Authority:** no audit verdict or retained-grade promotion is applied.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository premise boundary; it does not derive the supplied model.
- [local_compensation_common_field_record_limit_bounded_theorem_note_2026-09-24](LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md): conditional companion source within its stated hypotheses.

## Source and verification

Source PR #8923, frozen head `191ad04ad48d64c55d31c34521caec68444bfa64`. Original source dispositions and recovery branches are recorded in the combined receipt. Review uses the same primary session without subagents; no separate fix reviewer or formal audit is claimed.

```bash
python3 scripts/exact_microscopic_energy_at_a_star_birth_2026_09_24.py
```

Fresh controls execute in a temporary directory. Full scientific stdout and generated JSON are included in the authenticated result. Historical diagnostics and deferred source remain recoverable from the original branch.
