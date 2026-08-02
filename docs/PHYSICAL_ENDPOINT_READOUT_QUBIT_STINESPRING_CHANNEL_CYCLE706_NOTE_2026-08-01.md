# Conditional qubit Stinespring model induced by supplied endpoint blocks — Cycle 706

Date: 2026-08-01

Claim type: bounded_theorem

Authority: none. Audit: unset. Constitutional effect: none. No new axiom or
primitive is proposed or adopted.

Type: bounded conditional theorem / model calculation. The accepted Qubit premise
supplies the local algebra `M_2(C)`; it does not supply the endpoint unitary, coupling,
K field, register/environment state, partial-trace operation, apparatus, or Record
identification used below.

Lane: the gravity K-endpoint readout lane. The unaudited
[Cycle 704 classical symplectic model](PHYSICAL_RECORD_REGISTER_SYMPLECTIC_DILATION_CYCLE704_NOTE_2026-08-01.md)
named a quantum Stinespring calculation as a possible successor while explicitly
disclaiming a framework-site unitary or physical apparatus. This note performs the
finite-dimensional algebraic calculation only: it defines a uniform site-register
mixture from supplied Cycle696 endpoint blocks, constructs its isometry, identifies its
Choi spectrum and Kraus pair, and measures finite frame behavior. It does not turn the
Cycle704 bookkeeping register or the Cycle700 projected output into a physical quantum
channel.

## 2. Setup

The input-producing algorithm is the audit-excluded Cycle696 compiler, used through its
module `physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py`:

    source edits -> divergence rho -> static linear response eps -> metric and coframe
    -> K field -> endpoint Hamiltonian H -> endpoint unitary U -> registered rows.

Declared constants of the join member used here: ETA = 1.0, T_ACT = 1.0, insertion
amplitude AMP = 0.20, endpoint coupling sign +1 and scale 1.0, a **single** activation
step (one application of U; no composition is claimed). Lattice sizes L = 3 (n = 27
sites) and L = 7 (n = 343 sites), open boundary. Sources are link-label edits on the
F17 six-ray decorated domain at the central anchor: `x5` (one x-axial edit of strength
5), `y5` (one y-axial edit of strength 5), and `x5y7` (both, strengths 5 and 7).

The Cycle700 evidence row motivating this experiment reads, verbatim:

```
| exact reversibility with conservation, deletion, sign, scale, and range mutations | PARTIAL | C4–C4b; no Stinespring or unitary dilation of the open-system readout channel is constructed |
```

This note does **not** answer that row. Cycle700's object is a real field-update followed
by a supplied projected relational readout. Here a different finite map is defined from
Cycle696 blocks by additionally supplying (i) an `n`-slot register Hilbert space, (ii)
the uniform pure register vector, (iii) a product injection with an arbitrary qubit
input, and (iv) a mathematical trace over the register. Those choices define

    Phi(E) = (1/n) sum_s R(theta_s) E R(theta_s)*

on `M_2(C)`. The retained
[Kraus–Choi normalization theorem](KRAUS_CHOI_REPRESENTATION_NORMALIZATION_RECONCILED_NARROW_THEOREM_NOTE_2026-06-05.md)
supplies the finite algebraic Choi/Kraus convention; it does not select this map or give
the trace a physical meaning.

Domain accounting is load-bearing. At `AMP=0.20`, the `x5` and `y5` sources and all
their tested frames have a positive-definite principal coframe. The stronger `x5y7`
source does not: every tested frame clips the coframe (5–6 sites at `L=3`, 24–28 at
`L=7`). Its rho/group rows remain valid upstream, but every downstream K/channel row is
reported only as `CONDITIONAL_ON_CLIP` and is excluded from the PASS/FAIL tally.

## 3. Results

### R1 — conditional endpoint blocks are rotations and the registered rows follow
(DERIVED ALGEBRA, MEASURED INPUT)

U carries no matter leakage at all: the largest modulus outside the 2x2 site blocks is
exactly 0.0 at both L = 3 and L = 7 (bit-exact zero, not a tolerance). Each block equals
the rotation `R(theta_s) = cos(theta_s) I - i sin(theta_s) X`, with
`theta_s = ETA K(s)`, at the numerical floor. The two registered rows are then not
independent data: the excitation row is `sin^2(theta_s)` and the quadrature row is
`-sin(2 theta_s)` at both sizes. Nonconstancy is tested by range and standard deviation,
not by the maximum: the `x5` angle ranges are about `0.602` at `L=3` and `0.986` at
`L=7`.

### R2 — the supplied uniform-mixture model has a Stinespring isometry
(DERIVED, CONDITIONAL)

Let omega be the **supplied** flat register state and V = U (|omega> tensor I2), an explicit
2n-by-2 matrix. Then V is an isometry (V*V = I2 to 2.220e-16 at L = 3, 4.441e-16 at
L = 7), and tracing the register out of V E V* reproduces the site mixture

    Phi(E) = (1/n) sum_s R(theta_s) E R(theta_s)*

to 5.551e-16 (L = 3) and 6.106e-16 (L = 7), on a five-state probe set spanning M2(C).
The column-stacked superoperator built independently from the same rotations agrees with
Phi at the numerical floor. This proves the dilation of the declared finite map. It does
not derive a register preparation, physical environment, discard operation, apparatus,
or Record-writing instrument.

### R3 — the conditional channel has rank two on the x5 fixtures, with a closed-form
spectrum (DERIVED, MEASURED)

With the unnormalized Choi convention, write

    m_2 = mean_s exp(2 i theta_s).

Direct matrix-unit expansion gives the complete spectrum
`(1+|m_2|, 1-|m_2|, 0, 0)`. It is positive because `|m_2|<=1`, has trace 2,
and has rank at most two. Rank is exactly two iff `|m_2|<1`; angle nonconstancy alone
would not suffice because angles differing by pi have the same `exp(2i theta)`. The
runner therefore gates the complete expected spectrum, the minimum eigenvalue, both
tail eigenvalues, and a positive lower bound on the second eigenvalue. On `x5`, the top
pair is approximately `(1.953136, 0.046864)` at `L=3` and
`(1.950210, 0.049790)` at `L=7`, so both model fixtures have rank exactly two. The
extracted Kraus pair rebuilds the map, lies in `span{I,X}`, and the map is unital and
trace preserving.

Rank-one anchor (rejector). Applying cycle-696's own **deletion** mutation — every ray
link label set to zero — gives rho bit-exactly zero, hence K = 0 to 7.772e-16, a Choi
matrix whose second eigenvalue is 1.740e-31, and a channel equal to the identity to
1.075e-31. The gate discriminates: the *undeleted* six-ray decorated state is not that
anchor (its Choi second eigenvalue is 1.701e-02), so rank one is a property of the
deleted-source state and not an artefact of the test.

### R4 — the one-step uniform traced map sees two real components of one moment
(DERIVED, SCOPED)

Writing cbar = mean_s cos(2 theta_s) and sbar = mean_s sin(2 theta_s), the superoperator
is exactly

    S = ((1+cbar)/2) I(x)I + ((1-cbar)/2) X(x)X - i (sbar/2) (I(x)X - X(x)I)

to 3.331e-16. Both moments are directly readable off the registered rows: cbar equals
1 - 2 (mean excitation) to 1.110e-16 and sbar equals minus the mean quadrature exactly.
The scope this fixes is sharp for this declared map, and a twin-field rejector demonstrates it: moving a pair
of sites onto the same two-moment locus changes the channel by exactly 0.0 while moving
individual site angles by 2.170e-01 and the quadrature row by 4.089e-01. Thus this
single-step, uniform-register, fixed-X, register-traced map is determined by the real
and imaginary parts of the **second circular moment**. Register-resolved readout,
nonuniform weights, noncommuting axes, retained-register multi-step evolution, and
initial correlations are outside this statement and can reveal other information.

### R5 — algebraic angle negation gives the adjoint, by pre/post Z conjugation
(DERIVED)

`S(-theta)` equals `S*`, and `S*=(Z tensor Z) S (Z tensor Z)` at the numerical
floor. Equivalently, the adjoint map is obtained by Z-conjugating both its input and
output. The runner mutates the angle list directly; it does not execute or derive a
physical source-sign reversal through the upstream chain.

### R6 — rho permutes; valid single-axis channels sign-classify; the two-axis branch is
clipped (UPSTREAM DERIVED, DOWNSTREAM MEASURED, SCOPED)

For every one of the 24 cubic frames and each of the three sources, the frame-pulled
divergence equals the site-permuted divergence in **float bit-equality** (24/24 for each
of `x5`, `y5`, `x5y7` at L = 3; 48/48 across `x5` and `x5y7` at L = 7). Non-vacuity: the
L = 3 `x5` divergence has 7 nonzero entries with peak 8.500e-01.

For the domain-valid single-axis sources, the downstream K field sorts into sign classes
read off the frame's signed permutation row. For `x5`, 12 frames preserve the axis sign
and give the same uniform-mixture channel; 12 negate it and give the adjoint channel.
The wrong branch is separated by an order-one numerical floor. The same classification
holds for `y5` at `L=3`, and the `x5` result is reproduced at `L=7`.

For `x5y7`, the **upstream signed-permutation classification** is still an exact group
fact: 6 coherent-plus, 6 coherent-minus, and 12 mixed frames. But its downstream theta
multisets and channel moments are computed from Cycle696's clipped continuation because
the principal coframe does not exist on any of these cases. The runner prints those
values with `CONDITIONAL_ON_CLIP`; they are diagnostics, not theorem gates or physical
coframe claims.

Pointwise invariance is strictly smaller than multiset invariance, and the note is
explicit about which. The set of frames fixing rho pointwise is exactly the divergence
stabilizer: `{20,21,22,23}` for `x5` at both sizes, `{3,10,14,23}` for `y5` at
`L=3`, and the identity `{23}` for `x5y7` at both sizes. For the valid single-axis
cases, the pointwise K-field stabilizer agrees with the rho stabilizer. For `x5y7`, only
the rho stabilizer is a gate; agreement of the clipped field's zero-deviation set is a
conditional diagnostic. The valid `x5` contrast is measured: its four stabilizer frames
move no site angle, the other eight sign-preserving frames move sites while preserving
the map, and the twelve negating frames move sites while producing the adjoint map.

## 4. Verification

Runner: `physical_endpoint_readout_qubit_stinespring_channel_cycle706_2026_08_01.py`.
73 gates pass with zero failures. Twelve downstream `x5y7` diagnostics are emitted as
`CONDITIONAL_ON_CLIP` and are excluded from that tally. The receipt records claim type,
authority, audit state, scope, the conditional-row count, and a timer whose scope starts
before Cycle696 import and ends before the receipt write. Wall time is about 4–5 seconds
on the review host.

Headline gates: matter leakage is bit-exact zero at both sizes; isometry,
register-trace, superoperator, Choi-spectrum, Kraus rebuild, and adjoint residuals are at
their declared numerical floors; the second Choi eigenvalue exceeds `0.046` at both
sizes; the twin field moves sites by `0.217` while preserving the map; and the rho frame
permutation law closes 24/24 and 48/48. Numerical-floor details are printed as stable
tolerance buckets so the cold transcript does not encode hash-order roundoff.

Every identity gate is paired with something that would fail if the implemented object
were wrong: the nonconstancy range/standard-deviation floor against a flat-field vacuity,
the wrong-branch floor (>= 0.05) against a sign-blind multiset test, the twin-field move
floors against a channel test that could not distinguish fields, the six-ray-is-not-the-
vacuum gate against the rank-one anchor, and support/peak floors on rho against the
integer-truncation failure mode. Complete Choi-spectrum and minimum-eigenvalue gates
reject a non-CP/tail-sign failure, and a direct second-eigenvalue floor rejects accidental
rank one. No scalar prefactor is fitted anywhere; every quantity is recomputed from the
Cycle696 machinery rather than read back from a cache.

## 5. Boundary and honest read

What is established is a finite-dimensional theorem conditional on the declared model
inputs. The resulting `Phi` is a CPTP map on `M_2(C)` with an explicit isometry and,
for the valid `x5` fixtures, Kraus rank two. It is **not** identified with a physical or
Cycle700 readout channel.

Supplied rather than derived: the Cycle696 source/K algorithm and its response
normalization; `AMP`, `ETA`, `T_ACT`, coupling sign and scale; the fixed-X block
Hamiltonian; the site register; its uniform state; product preparation; one activation;
and the decision to trace the register. Open: derivation or audit-retirement of those
inputs, a framework-site apparatus/environment and physical trace, a Record-writing
instrument, composition over multiple activations, and a physical source/sign law.

Three corrections to the working assumptions are worth recording. First, the six-ray
decorated domain with no edits is **not** source-free: its own anchor and port structure
carries divergence on 7 sites with peak 5.100e-01 at the ports and a Choi second
eigenvalue of 1.701e-02, so it cannot serve as the rank-one anchor. The deletion mutation, which is
Cycle696's own vocabulary, makes rho bit-exact zero and gives the identity channel to
tolerance; that is the anchor gate, while the undeleted state is the counter-case. Second, the
pointwise-invariant frame set here is the divergence stabilizer quartet, *not* the
body-diagonal six-frame list [1, 4, 9, 15, 18, 23] that the cycle-700 endpoint row
selects. Those two sets are different objects measured at different points in the chain,
and this note claims only the smaller one; frames 1, 4 and 9 are in fact sign-negating
for `x5`, which is exactly why they fall outside the pointwise-invariant set. The
coherent-minus branch is measured, not derived: the negation survives the nonlinear
metric and coframe stage to 1e-11, but no argument here explains why the principal square
root commutes with the sign flip. Third, `x5y7` lies outside the principal-coframe domain
at the declared amplitude; its downstream rows are clipped diagnostics and carry no PASS
credit.

## 6. Named next routes

Each of these opens a path rather than closing one.

1. **Derive the coherent-minus negation through the nonlinear chain.** The measured
   1e-11 agreement across 12 frames asks for a branch-tracking argument on the principal
   symmetric square root in the coframe stage. A proof there would upgrade R6's minus
   branch from MEASURED to DERIVED.
2. **Multi-step site-register composition.** With m > 1 activations, does the family
   {Phi_m} form a semigroup, and is the two-moment scope of R4 stable under composition
   or does composition reveal higher circular moments? The single-step dilation built
   here is the natural starting point.
3. **Restore a lawful two-axis domain before classifying it.** Reduce no parameter merely
   to buy a pass. Instead derive a domain-valid two-axis fixture or a coframe theorem,
   freeze it independently, and only then revisit the `x5y7` downstream classification.

## 7. Citations

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Retained Kraus–Choi normalization theorem](KRAUS_CHOI_REPRESENTATION_NORMALIZATION_RECONCILED_NARROW_THEOREM_NOTE_2026-06-05.md)
- [Cycle 700 operational source-response readout chain](PHYSICAL_OPERATIONAL_SOURCE_RESPONSE_READOUT_CHAIN_CYCLE700_NOTE_2026-07-25.md)
- [Cycle 704 classical symplectic model](PHYSICAL_RECORD_REGISTER_SYMPLECTIC_DILATION_CYCLE704_NOTE_2026-08-01.md)
- [Cycle 696 joined compiler tournament](work_history/repo/review_feedback/PHYSICAL_OPEN_COFRAME_K_ENDPOINT_JOINED_COMPILER_TOURNAMENT_NOTE_2026-07-23.md)
