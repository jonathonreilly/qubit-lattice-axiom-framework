# Quantum Stinespring dilation of the executed endpoint readout channel on M2(C) — Cycle 706

Date: 2026-08-01
Status: `unaudited`

Lane: the gravity K-endpoint readout lane. Cycle 704 built the *classical* symplectic
dilation of the executed readout channel and named the quantum Stinespring dilation on
M2(C) as its successor experiment; cycle 705 carried the endpoint-transport side of the
same chain. This note executes that named successor: it constructs an exact isometric
dilation of the qubit-level endpoint readout channel, identifies the dilated channel's
Choi spectrum and Kraus pair in closed form, and measures how the whole construction
transforms under the 24-frame cubic group.

## 2. Setup

The executed chain is the landed cycle-696 compiler, used verbatim through its own
module `physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py`:

    source edits -> divergence rho -> static linear response eps -> metric and coframe
    -> K field -> endpoint Hamiltonian H -> endpoint unitary U -> registered rows.

Declared constants of the join member used here: ETA = 1.0, T_ACT = 1.0, insertion
amplitude AMP = 0.20, endpoint coupling sign +1 and scale 1.0, a **single** activation
step (one application of U; no composition is claimed). Lattice sizes L = 3 (n = 27
sites) and L = 7 (n = 343 sites), open boundary. Sources are link-label edits on the
F17 six-ray decorated domain at the central anchor: `x5` (one x-axial edit of strength
5), `y5` (one y-axial edit of strength 5), and `x5y7` (both, strengths 5 and 7).

The cycle-700 evidence row this note answers reads, verbatim:

```
| exact reversibility with conservation, deletion, sign, scale, and range mutations | PARTIAL | C4–C4b; no Stinespring or unitary dilation of the open-system readout channel is constructed |
```

The object dilated here is the **qubit-level** readout channel on M2(C): the record
register carries n site slots, the endpoint unitary U acts block-diagonally on
(register) tensor (qubit), and the channel obtained by tracing out the register is a
completely positive trace-preserving map Phi : M2(C) -> M2(C). Everything below is a
finite-dimensional statement about that map and its dilation.

## 3. Results

### R1 — the endpoint unitary is an exact block rotation and the registered rows are its
two moments (DERIVED, MEASURED)

U carries no matter leakage at all: the largest modulus outside the 2x2 site blocks is
exactly 0.0 at both L = 3 and L = 7 (bit-exact zero, not a tolerance). Each block equals
the real rotation R(theta_s) = cos(theta_s) I - i sin(theta_s) X with theta_s = ETA
K(s), to 1.110e-16. The two registered rows are then not independent data: the excitation
row is sin^2(theta_s) and the quadrature row is -sin(2 theta_s), to 5.551e-17 and
1.110e-16. The field is genuinely non-constant — max |theta| = 3.339e-01 at L = 3 and
4.960e-01 at L = 7 — so these identities are not satisfied vacuously by a flat field.

### R2 — the executed readout channel has an exact Stinespring isometry (DERIVED)

Let omega be the flat register state and V = U (|omega> tensor I2), an explicit
2n-by-2 matrix. Then V is an isometry (V*V = I2 to 2.220e-16 at L = 3, 4.441e-16 at
L = 7), and tracing the register out of V E V* reproduces the site mixture

    Phi(E) = (1/n) sum_s R(theta_s) E R(theta_s)*

to 5.551e-16 (L = 3) and 6.106e-16 (L = 7), on a five-state probe set spanning M2(C).
The column-stacked superoperator built independently from the same rotations agrees with
Phi to 2.220e-16. So the open readout map of the executed chain *is* a register-traced
unitary dilation, constructed rather than assumed.

### R3 — the dilated channel has Kraus rank two, with a closed-form spectrum (DERIVED,
MEASURED)

The Choi matrix of Phi has eigenvalues summing to 2 (to 8.882e-16) with the third and
fourth eigenvalues at 3.227e-17 and below: the Kraus rank is **two**, not four. At
L = 3 the top pair is (1.953136, 4.686e-02), and their product equals 1 - rbar^2 to
3.331e-16, where rbar = |mean_s exp(2 i theta_s)| is the second circular moment of the
K field. The same product identity holds at L = 7 to 2.498e-16. Rebuilding the two
Kraus operators from the Choi eigenvectors reproduces the superoperator to 2.221e-16,
and both operators lie in span{I, X} to 2.00e-16. Phi is unital and trace preserving to
3.331e-16.

Rank-one anchor (rejector). Applying cycle-696's own **deletion** mutation — every ray
link label set to zero — gives rho bit-exactly zero, hence K = 0 to 7.772e-16, a Choi
matrix whose second eigenvalue is 1.740e-31, and a channel equal to the identity to
1.075e-31. The gate discriminates: the *undeleted* six-ray decorated state is not that
anchor (its Choi second eigenvalue is 1.701e-02), so rank one is a property of the
deleted-source state and not an artefact of the test.

### R4 — the channel sees only two moments of the K field (DERIVED, SCOPED)

Writing cbar = mean_s cos(2 theta_s) and sbar = mean_s sin(2 theta_s), the superoperator
is exactly

    S = ((1+cbar)/2) I(x)I + ((1-cbar)/2) X(x)X - i (sbar/2) (I(x)X - X(x)I)

to 3.331e-16. Both moments are directly readable off the registered rows: cbar equals
1 - 2 (mean excitation) to 1.110e-16 and sbar equals minus the mean quadrature exactly.
The scope this fixes is sharp, and a twin-field rejector demonstrates it: moving a pair
of sites onto the same two-moment locus changes the channel by exactly 0.0 while moving
individual site angles by 2.170e-01 and the quadrature row by 4.089e-01. The dilated
channel therefore cannot resolve the K field beyond its first two circular moments.

### R5 — negating the field implements the adjoint, by Z conjugation (DERIVED)

S(-theta) equals S* exactly (0.0), and S* equals (Z(x)Z) S (Z(x)Z) exactly (0.0). The
sign mutation of the source field is thus not merely "another channel": it is the
adjoint of the executed one, realised by a fixed local conjugation on the qubit.

### R6 — the frame law: rho permutes, the channel sign-classifies (DERIVED, MEASURED,
SCOPED)

For every one of the 24 cubic frames and each of the three sources, the frame-pulled
divergence equals the site-permuted divergence in **float bit-equality** (24/24 for each
of `x5`, `y5`, `x5y7` at L = 3; 48/48 across `x5` and `x5y7` at L = 7). Non-vacuity: the
L = 3 `x5` divergence has 7 nonzero entries with peak 8.500e-01.

Downstream of that permutation the K field sorts into sign classes read off the frame's
signed permutation row. For the single-axis source `x5`, 12 frames preserve the axis sign
and 12 negate it. The 12 sign-preserving frames leave the sorted theta multiset invariant
to 4.774e-15; the 12 negating frames map it to its own negation to 1.001e-11. The wrong
branch is firmly rejected: the smallest cross-branch deviation is 2.057e-01, four orders
above the coherent floors. For the two-axis source `x5y7` the classification is a
trichotomy — 6 coherent-plus, 6 coherent-minus, 12 mixed — with coherent floors 9.548e-15
and 9.670e-11 and every mixed frame breaking both branches by at least 1.873e-01. At the
moment level, coherent-plus frames preserve both moments (1.221e-15), coherent-minus
frames flip the odd moment (1.985e-11), and mixed frames break the moments by at least
1.075e-01. Every L = 3 sign-class floor is reproduced at L = 7 (3.819e-13, 3.077e-10,
9.687e-13, 5.474e-10, mixed break 3.018e-02).

Pointwise invariance is strictly smaller than multiset invariance, and the note is
explicit about which. The set of frames fixing rho pointwise is exactly the divergence
stabilizer: {20, 21, 22, 23} for `x5`, {3, 10, 14, 23} for `y5`, and the identity {23}
alone for `x5y7`, at both L = 3 and L = 7; and for each source the set of frames with
*exactly zero* sorted-multiset deviation coincides with that stabilizer. The contrast
is measured: the 4 stabilizer frames of `x5` move no site angle at all (0.0) and no
moment at all (0.0); the other 8 sign-preserving frames move site angles by at least
7.70e-02 while holding both moments to 9.714e-16; the 12 negating frames move site
angles by at least 5.560e-01 while flipping the odd moment to 2.900e-12.

## 4. Verification

Runner: `physical_endpoint_readout_qubit_stinespring_channel_cycle706_2026_08_01.py`.
68 gates, all passing, in blocks C1 (block structure and registered rows, 5), C2
(Stinespring isometry, 3), C3 (Choi spectrum, Kraus pair, unitality, rank-one anchor,
10), C4 (two-moment registration and the twin-field rejector, 6), C5 (adjoint by Z
conjugation, 2), C6 (frame law at L = 3, 25), C7 (the same battery at L = 7, 17). Wall
time about 5 seconds.

Headline numbers: matter leakage exactly 0.0 at both sizes; isometry deviation 2.220e-16
(L = 3) and 4.441e-16 (L = 7); register-trace agreement 5.551e-16 and 6.106e-16; third
Choi eigenvalue 3.227e-17 and 1.826e-16; top-pair product identity 3.331e-16 and
2.498e-16; twin-field channel deviation exactly 0.0 against a 2.170e-01 site move;
adjoint identities exactly 0.0; frame permutation law 24/24 and 48/48 in float
bit-equality.

Every identity gate is paired with something that would fail if the implemented object
were wrong: the non-uniformity floor (max |theta| >= 0.3) against a flat-field vacuity,
the wrong-branch floor (>= 0.05) against a sign-blind multiset test, the twin-field move
floors against a channel test that could not distinguish fields, the six-ray-is-not-the-
vacuum gate against the rank-one anchor, and support/peak floors on rho against the
integer-truncation failure mode. No scalar prefactor is fitted anywhere; every quantity
is recomputed from the cycle-696 machinery rather than read back from a cache.

## 5. Boundary and honest read

What is established is finite-dimensional and local to one activation step. Phi is a
genuine CPTP map on M2(C) with an explicitly constructed isometric dilation and Kraus
rank two; the register-traced dilation is the executed readout channel, not a model of
it. What is *not* established: nothing here derives the K field itself, and nothing here
composes activations — the channel semigroup for m > 1 steps is untouched.

Two corrections to the working assumptions are worth recording. First, the six-ray
decorated domain with no edits is **not** source-free: its own anchor and port structure
carries divergence on 7 sites with peak 5.100e-01 at the ports and a Choi second
eigenvalue of 1.701e-02, so it cannot serve as the rank-one anchor. The deletion mutation, which is
cycle-696's own vocabulary, gives the exact vacuum instead, and that is what the anchor
gate uses; the undeleted state is kept as the discriminating counter-case. Second, the
pointwise-invariant frame set here is the divergence stabilizer quartet, *not* the
body-diagonal six-frame list [1, 4, 9, 15, 18, 23] that the cycle-700 endpoint row
selects. Those two sets are different objects measured at different points in the chain,
and this note claims only the smaller one; frames 1, 4 and 9 are in fact sign-negating
for `x5`, which is exactly why they fall outside the pointwise-invariant set. The
coherent-minus branch is measured, not derived: the negation survives the nonlinear
metric and coframe stage to 1e-11, but no argument here explains why the principal square
root commutes with the sign flip.

## 6. Named next routes

Each of these opens a path rather than closing one.

1. **Derive the coherent-minus negation through the nonlinear chain.** The measured
   1e-11 agreement across 12 frames asks for a branch-tracking argument on the principal
   symmetric square root in the coframe stage. A proof there would upgrade R6's minus
   branch from MEASURED to DERIVED.
2. **Multi-step record-register composition.** With m > 1 activations, does the family
   {Phi_m} form a semigroup, and is the two-moment scope of R4 stable under composition
   or does composition reveal higher circular moments? The single-step dilation built
   here is the natural starting point.
3. **General-source coherence classification.** R6 classifies one- and two-axis edit
   sets. An arbitrary edit set has no obvious signed-permutation-row invariant; finding
   the general classifier — or an obstruction to one — would extend the frame law beyond
   the axial family.

## 7. Citations

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Cycle 700 operational source-response readout chain](PHYSICAL_OPERATIONAL_SOURCE_RESPONSE_READOUT_CHAIN_CYCLE700_NOTE_2026-07-25.md)
- [Cycle 696 joined compiler tournament](work_history/repo/review_feedback/PHYSICAL_OPEN_COFRAME_K_ENDPOINT_JOINED_COMPILER_TOURNAMENT_NOTE_2026-07-23.md)
