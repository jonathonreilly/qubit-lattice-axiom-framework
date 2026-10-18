---
claim_id: contact_source_heisenberg_code_preparation_bounded_theorem_note_2026-10-18
claim_type: bounded_theorem
claim_scope: "For the supplied positive homogeneous nearest-neighbor Heisenberg Hamiltonian on actual Z3, the exactly-two-excitation representation around a common pure ray, and the stated translation/proper-cubic family of SU2-scalar eight-spin jumps: a bounded countable quantum-jump generator prepares a moving nodal code with positive first-click probability from an adjacent product seed; every installed jump annihilates every subsequent full-H target orbit; the complete channel includes all no-click and first-click outputs and passive references. The total rate is at most32gamma and a selected first-label probability is at least gamma*t/16 on the stated interval. The displayed normalized source/target mean energies are20j and24j. Instrument selection, reservoir realization, physical Record formation/admissibility/readout and an R-only state law remain open."
upstream_dependencies:
  - native_heisenberg_nodal_record_persistence_bounded_theorem_note_2026-10-18
runner: scripts/contact_source_heisenberg_code_preparation_2026_10_18.py
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: native_heisenberg_nodal_record_persistence_bounded_theorem_note_2026-10-18
target_blocker_text: "Supply an explicit preparation interface to the protected Heisenberg sector while keeping the physical instrument and Record-state interface separate."
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Review and verify this conditional preparation construction, then investigate the native event and Record-state interface."
conditional_surface_status: "Supplied homogeneous H, common pure background, exactly two excitations, eight-spin Markov jump family and rate; no physical Record identification."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Positive conditional preparation and subsequent full-H persistence theorem with an explicit complete-output channel."
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Contact-supported jumps prepare a moving Heisenberg code and cease automatically

**Date:** 2026-10-18
**Type:** bounded_theorem
**Status:** proposed_retained

Actual current surface status is conditional-support. This is an explicit
mathematical preparation process under supplied dynamics and a supplied jump
instrument. Formal retention belongs to the independent audit path.

An eight-spin scalar operator transfers an adjacent-pair source into a
correlated two-excitation state. The full homogeneous Heisenberg evolution
keeps that state free of adjacent-pair amplitude while its excitations move.
Every translated and rotated source is supported on adjacent pairs, so all
installed jumps become inactive after the first successful event. The
correlated input and a separate shutdown command are replaced by this
conditional preparation process. The instrument, its environment and rate,
and the initial aligned-background product seed remain supplied.

**Exact target theorem.** For every j>0 and gamma>0, the explicitly defined
translation/proper-cubic-covariant family of internally SU2-scalar eight-spin
jumps on the exactly-two-excitation Hilbert space over actual Z3 defines a
trace-preserving quantum channel with total instantaneous rate at most
32gamma, loads a full-H moving nodal target with selected first-label
probability at least gamma*t/16 for
`0<t<=1/[4(48j+16gamma)]` from an adjacent product seed, and preserves that
target's plane ray q for all later times with every subsequent jump rate zero,
including all no-click outcomes and passive references.

The statement concerns quantum preparation and persistence. Physical
Record admissibility, registration and readout are separate open bridges.
The physical application domain considered here begins with no prior Records.

Primary runner: `scripts/contact_source_heisenberg_code_preparation_2026_10_18.py`.
Its canonical cache is `logs/runner-cache/contact_source_heisenberg_code_preparation_2026_10_18.txt`;
its structured output is `outputs/contact_source_heisenberg_code_preparation_2026_10_18.json`.
These finite controls supplement the proofs below; they do not execute an
infinite lattice or infer all-time behavior from finitely many powers.

## 1. Supplied representation and imports

The common pure qubit ray q is denoted up; a perpendicular vector is denoted
down. Its phase is arbitrary. The Hilbert space used below is

    H_2 = l2({S subset Z3 : |S|=2}),

where |S> has down spins at the two sites in S and q at every other site.
This is the two-excitation sector of the finite-excitation representation
about q, with ordinary qubit tensor composition. q is supplied state data,
not a preferred internal direction in the law. Statements for another q
are obtained by the corresponding local algebra rotation; no infinite-volume
total-spin operator is required.

| Input | Role | Provenance | Open physical bridge |
|---|---|---|---|
| Qubit tensor representation about common q and the exactly-two-excitation domain | Defines states, sectors and complete outputs | Supplied model, also used in the persistence source | Native state assignment and preparation of this family |
| Homogeneous positive Heisenberg interaction with j>0 | Supplies autonomous full spin evolution | The explicitly displayed model below | Selection and physical calibration of H |
| Eight-site source/target and scalar multiplicity transfer | Supplies the jump operator | Constructed in sections3–4 | Microscopic origin of the joint coupling |
| All translations and all24 proper cubic rotations with common gamma>0 | Supplies event channels and rates | Declared label/rate convention | Physical rate and event implementation |
| Markov reservoir and chosen quantum-jump output interpretation | Supplies the CP process and conditional event law | Explicit conditional mathematical model | Reservoir preparation, energy supply and realized-event bridge |
| Coordinate-exterior persistence construction | Supplies the invariant target mechanism | Same-proposal persistence theorem, specialized and proved again in section5 | Preparation is addressed here; physical identification remains separate |

The
[native Heisenberg persistence source](NATIVE_HEISENBERG_NODAL_RECORD_PERSISTENCE_BOUNDED_THEOREM_NOTE_2026-10-18.md)
is a declared same-proposal dependency for the code interface and model
conventions. It is not treated as retained authority. All load-bearing n=2
identities needed here are proved below so the preparation argument can be
read without an external research packet. The construction uses elementary
finite-dimensional spin representation theory and bounded-operator evolution;
no external physical model or empirical number is imported as a derivation.

The framework premises are described in
`docs/MINIMAL_AXIOMS_2026-06-29.md` and the primitive registry. Their role here
is the physical claim boundary. The three approved primitives retain their
registered grants; this construction neither changes them nor infers an
instrument, initial state or time/rate rule from them. No axiom or primitive
is proposed by this note.

## 2. Full actual-Z3 Heisenberg Hamiltonian

Supply the positive interaction

    H = 2j sum_(nearest-neighbor edges e) (I-SWAP_e), j>0.       (1)

On H_2 its precise operator definition is the configuration-graph Laplacian:
for S={a,b}, let c(S)=1 when a and b are nearest neighbors, and0 otherwise.
Then

    (Hf)(S)=2j[12-2c(S)]f(S)
           -2j sum_(allowed one-site NN moves S->T) f(T).      (2)

An allowed move changes one occupied site to an adjacent unoccupied site.
There are12-2c(S) such moves. A bond with two equal spins contributes zero;
a bond with one down spin gives2j times the diagonal-minus-exchange action.
This derives (2) from the actual bonds, without a projected persistence
Hamiltonian or subtraction of a divergent vacuum energy.

The configuration graph has degree at most12. Its adjacency and degree
operators each have norm at most12, so H extends from finite-support vectors
to a bounded selfadjoint operator on H_2 with `0<=H<=48j I`. Positivity follows
from the edge quadratic form `2j sum_{unordered S~T}|f(S)-f(T)|²`.
Its domain is all H_2, and `U_t=exp(-itH)` exists for every real t. Every
neighbor in Z3 is retained; no finite box or periodic truncation is used.

Write C for the diagonal projection onto adjacent-pair configurations.
Under the normalized symmetric ordered-pair embedding, (2) is the free
two-particle cubic Laplacian compressed to distinct positions, with the
additional diagonal term `-4j C`. That term and the forbidden occupied-site
moves are included throughout the proof.

## 3. Eight-site source and target

Let

    B={ (x,y,0) : x in{-2,-1,1,2}, y in{0,1} }.

Write |a,b> for a two-down basis vector in its eight-spin tensor space.
Let `u_i(x)=delta_(x,i)-delta_(x,-i)` for i=1,2 and define

    w({a,b}) = [u_1(a_x)u_2(b_x)-u_2(a_x)u_1(b_x)]
               [delta_(a_y,0)delta_(b_y,1)
                -delta_(a_y,1)delta_(b_y,0)],
    psi = (1/sqrt(8)) sum_(unordered {a,b} subset B) w({a,b})|a,b>.  (3)

Both bracket factors change sign under exchanging a,b, so w is well-defined
on unordered pairs. Its support consists of eight configurations with
coefficients +/-1. Thus psi has norm1. Each support pair has distinct x
and distinct y coordinates, so it is neither a collision nor an adjacent
pair, and neither site has x=0.

For the positive-x plaquette set

    A=(1,0,0), Bp=(2,0,0), D=(1,1,0), E=(2,1,0),
    chi=(|A,Bp>-|Bp,E>+|E,D>-|D,A>)/2.                       (4)

The four configurations are distinct nearest-neighbor pairs, so chi has
norm1 and is orthogonal to psi.

Let S_z=(1/2)sum_(a in B)sigma_z,a and let S_+ remove a down spin. Both states
have S_z eigenvalue2. At each plaquette vertex the two source coefficients
in S_+chi cancel, giving S_+chi=0. For psi, fix the remaining occupied site
and sum over the removed site. Each odd orbital u_i has zero sum, so that
sum vanishes, giving S_+psi=0. Consequently chi and psi are highest weights
of two orthogonal copies of spin2 in the eight-spin representation.

For k=0,...,4 define

    n_k=k!4!/(4-k)!,
    chi_k=S_-^k chi/sqrt(n_k),
    psi_k=S_-^k psi/sqrt(n_k).                               (5)

The angular-momentum commutators give squared lowering norms
`n_k=1,4,24,144,576`; lowering once more gives zero. Each sequence is an
orthonormal spin2 basis with magnetization2-k. Cross inner products vanish:
different magnetizations are orthogonal, and at equal k the raising/lowering
identity reduces the inner product to n_k<chi,psi>=0.

## 4. Local scalar operator and covariant event family

On the full eight-spin Hilbert space define the partial isometry

    V=sum_(k=0)^4 |psi_k><chi_k|,
    P_chi=V†V=sum_k |chi_k><chi_k|.                          (6)

It is zero on the orthogonal complement of the source multiplet. The matching
ladder coefficients prove `[V,S_z]=[V,S_+]=[V,S_-]=0` on the full space.
The complement is invariant under these spin generators, so this is a full
operator identity, not just an identity on the input states. It follows that
V commutes with the same SU2 rotation on every block spin. Its norm is1,
`VV†=sum_k |psi_k><psi_k|`, and it annihilates the target multiplet.
This scalar completion uses internal spin multiplicity rather than a supplied
measurement of q.

For each `lambda=(c,R)` with c in Z3 and R one of the24 proper cubic rotations,
install the translated/rotated copy V_lambda on `c+R B`. The labels are all
retained, including labels with duplicate source effects; gamma is the common
rate per indexed label. The family is translation/proper-cubic covariant.
Each individual member is internally SU2 scalar. The same physical operators
therefore apply to the globally rotated common-background seed families.

The block is disconnected across its x=0 plane. Its maximum graph distance
from its designated center is3 and its Manhattan diameter is5. These are
finite-support eight-spin joint couplings, not a nearest-neighbor or
single-star event implementation. Their microscopic realization is supplied.

In H_2 every lowered source chi_k with k>=1 is inaccessible, since it has
at least three down spins inside the block. A nonzero highest-weight source
component contains both global excitations inside that block, so its exterior
is the aligned vacuum. The restriction is therefore exactly

    V_lambda=|psi_lambda><chi_lambda|  on H_2.                (7)

A nonzero first event produces the entire spin state psi_lambda with its
aligned exterior; no other spin factor is discarded. V conserves excitation
number. No extra classical flag or separately operated state-reset device
is added; the jump itself is a conditional rank-one transfer.

## 5. Exact full-H target evolution and nonstationary motion

For completeness, specialize the coordinate-exterior construction to (3).
Use normalized wedge products `(f wedge g)=(f tensor g-g tensor f)/sqrt(2)`.
With `f_i=u_i/sqrt(2)`, the normalized symmetric ordered-pair vector is

    F=(f_1 wedge f_2)(x_1,x_2)
      (delta_0 wedge delta_1)(y_1,y_2)
      delta_0(z_1)delta_0(z_2).                             (8)

It is symmetric under simultaneous exchange of the two positions, because
two exterior factors change sign. It vanishes at collisions. Multiplication
by sqrt(2) on each unordered distinct pair gives exactly psi in (3) and
preserves norm.

Evolve every one-dimensional orbital in (8) by `exp(-it 2j L_Z)`, with
`L_Z=2I-A_Z`. The resulting F_t solves the bounded free two-particle equation
with generator `2j(L_Z3^(1)+L_Z3^(2))` on the full ordered lattice.
The x and y exterior factors remain antisymmetric. The x orbitals remain odd,
since reflection commutes with L_Z. At every t:

- Equal x coordinates give zero x exterior factor; equal y coordinates give
  zero y exterior factor.
- A collision has equal x. An adjacent pair along x has equal y; an adjacent
  pair along y or z has equal x. Thus every collision and every contact
  amplitude is zero.
- A particle at x=0 has zero x-orbital amplitude.

At a distinct configuration, the free action's omitted hops land on
collisions and hence have zero amplitude. Its diagonal difference from H
is `4j C`, which also annihilates F_t. The unordered image of F_t consequently
solves the exact physical equation (2). Bounded-H uniqueness proves it is
`U_t psi` for all real t. In particular

    C U_t psi=0,
    N_v U_t psi=0 for every v with x_v=0,                   (9)

where N_v projects onto a down spin at v. Translations and proper rotations
commute with H and transport these identities to every target psi_lambda.
The protected plane is `c+R{x=0}` and includes the designated center c.
Every finite subset of that plane has pure product q reduced state and
factors from the remaining spins and any passive reference.

The target is nonstationary for j>0. All its initial z coordinates are0.
Moving one occupied site one step in the z direction produces a configuration
outside the initial support with coefficient `-2j` times its unique initial
coefficient; that coefficient is nonzero. No other initial configuration
contributes to that same output. Hence Hpsi has a nonzero component
orthogonal to the initial support, so psi is not an eigenvector. Its
nontrivial motion coexists with (9).

## 6. Bounded countable generator on the actual infinite lattice

On H_2 let

    Q_lambda = sum_(four source edges e for lambda) |e><e|,
    A=sum_lambda |chi_lambda><chi_lambda|.                  (10)

A fixed nearest-neighbor edge belongs to four elementary plaquettes: either
of two transverse coordinate directions and either side in that plane.
Each unoriented plaquette has eight proper-cubic-rotation/translation
realizations of the indexed source. Thus every edge occurs in exactly32
Q_lambda supports. A direct alternative count uses four source edges and
eight rotations that take each unoriented source direction into a chosen
unoriented coordinate direction, with one matching translation each.

Since `|chi_lambda><chi_lambda|<=Q_lambda`, finite partial sums give

    0<=A<=32 C<=32 I.                                     (11)

The sum exists as a strong monotone limit, independently of enumeration.
Equation (11) bounds positive effects; it is not an asserted equality
between the source-projector sum and a diagonal operator. No sharpness of
the operator-norm bound is claimed.

For positive trace-class rho, the positive series
`sum_lambda V_lambda rho V_lambda†` converges in trace norm, with trace at
most32 tr(rho). It extends to a bounded completely positive map, also after
tensoring with any passive reference identity. This is pointwise trace-norm
convergence, not uniform convergence of finite-center truncations on the
trace-class unit ball.

Supply the Markov quantum-jump generator

    G(rho)=-i[H,rho]+gamma sum_lambda V_lambda rho V_lambda†
                       -(gamma/2){A,rho}, gamma>0,        (12)
    M_t=exp[(-iH-gamma A/2)t],  t>=0.                      (13)

H and A are bounded on H_2. The instantaneous total jump rate is at most
32gamma, giving a convergent jump expansion and nonexplosion. M_t is a
contraction because

    d||M_t eta||²/dt=-gamma <M_t eta,A M_t eta><=0.          (14)

No commutation of A and H is assumed.

## 7. Automatic cessation after the first event

Each chi_mu is supported on adjacent-pair configurations. Equations (7) and
(9) therefore imply, for all labels lambda,mu and all real s,

    V_mu U_s psi_lambda=0,
    A U_s psi_lambda=0.                                   (15)

The second identity follows from the strong positive sum (10), or from
(11). Consequently U_s psi_lambda solves the no-click evolution equation
with its initial value, and bounded-generator uniqueness gives

    M_s psi_lambda=U_s psi_lambda, s>=0.                   (16)

Every later jump rate is exactly zero. Both the gain and loss dissipative
terms vanish on the post-first-event orbit, so its complete subsequent
spin evolution is the unchanged full H. All event channels remain installed;
there is no external cessation command and no stored registration flag.
The protected local rays in (9) persist along this entire future process.

Equations (15)–(16) use exactly two total excitations and the displayed
targets. Those are theorem hypotheses, not assumptions about arbitrary
matter states or pre-existing Records.

## 8. Complete channel and reservoir output, including references

For every density matrix rho on H_2 and finite T>=0 the full channel is

    Phi_T(rho)=M_T rho M_T†
      +gamma integral_0^T sum_lambda
          U_(T-s) V_lambda M_s rho M_s† V_lambda† U_(T-s)† ds. (17)

The first term is the unnormalized no-click branch. The integral includes
every first label and every first time. All histories with later clicks
have zero weight by (15), so (17) is the entire channel of (12).
The integral is well-defined in trace norm by (11). Each term is completely
positive. For positive rho, (14) gives

    d tr(M_s rho M_s†)/ds
       =-gamma sum_lambda tr(V_lambda M_s rho M_s† V_lambda†).

Unitary post-click propagation preserves each trace. Integrating proves
`tr Phi_T(rho)=tr rho`. This also supplies a direct conservative construction
of the bounded evolution. It keeps unsuccessful/no-click outcomes instead
of selecting only successful runs.

A reservoir output space can be taken as the direct sum of a no-click
sector and `L2([0,T] x labels)` click modes. The isometry on a vector eta
has no-click component M_T eta and click-component function

    (s,lambda) -> sqrt(gamma) U_(T-s) V_lambda M_s eta.      (18)

The norm identity above is the isometry identity. Exact times label a
continuous density; they are not normalizable Hilbert vectors. Tracing this
reservoir yields (17); retaining it keeps every branch output. The Markov
reservoir and a realized-trajectory interpretation remain supplied physical
inputs, rather than consequences of this dilation formula.

Tensor every operator in (17)–(18) with the identity on an arbitrary passive
reference. Complete positivity and the same trace identity prove the result
for mixed inputs and input/reference entanglement. A nonzero first branch
has the rank-one spin output psi_lambda and a conditioned reference state;
its spin/reference factorization discards no reference subsystem. Conditional
normalization is used only to describe nonzero branches, not to remove
zero-success or no-click outputs from the full channel.

## 9. Explicit positive loading from an adjacent product seed

Let eta=|e> for any nearest-neighbor pair e, with q at all other sites.
Choose any label lambda whose source contains e. Its source coefficient has
magnitude1/2, so

    |<chi_lambda,eta>|=1/2,
    gamma||V_lambda eta||²=gamma/4.                        (19)

For the full competing-channel process let `M=48j+16gamma`.
Equations (2), (11) and contractivity give

    ||M_s-I|| <= integral_0^s ||(-iH-gamma A/2)M_u||du
              <= M s.

For `0<=s<=1/(4M)` this implies

    |<chi_lambda,M_s eta>|>=1/2-Ms>=1/4.

Integrating that first-label density yields the promised exact sufficient
bound

    Pr(first click has label lambda and time<=t)
       >= gamma t/16,  0<t<=1/[4(48j+16gamma)].             (20)

The no-click evolution already includes all other installed channels, so
(20) is a first-event bound in the complete law, not a single-channel
approximation. Under the specified label convention the initial total rate
is exactly `32(gamma/4)=8gamma`. The theorem asserts positive capture
probability on the stated finite interval; the eventual no-click mass is
not evaluated. Deduplicating channel labels would change the rate convention
and requires changing these constants accordingly.

## 10. Modeled energy and reservoir accounting

Each configuration in chi has one occupied nearest-neighbor edge, so (2)
has diagonal20j there. A single hop cannot connect two distinct source edges
in the square: such edges either are disjoint or their nonshared endpoints
are not adjacent. Thus there are no internal off-diagonal contributions and

    <chi,Hchi>=20j.                                      (21)

Every configuration in psi has no adjacent pair, hence diagonal24j. A
z hop leaves its support; a y hop gives equal y; an x hop either leaves the
allowed x set or makes both absolute x coordinates equal. None is another
configuration in the eight-term target support. Therefore

    <psi,Hpsi>=24j.                                      (22)

The normalized source-to-target transfer in (6) changes mean modeled system
energy by+4j. The supplied reservoir must account for that transfer. This
is a state-specific mean-energy statement, not a universal per-event work
formula for arbitrary coherent pre-click states or a claim of passive
relaxation. A microscopic bath energy/work implementation remains open.

## 11. Proof obligations, boundaries and physical interpretation

The proof graph is acyclic:

| Obligation | Discharge | Used by |
|---|---|---|
| Actual-Z3 full two-excitation H and its bounded selfadjoint realization | Section2, graph-Laplacian derivation and degree bound | Sections5–10 |
| Source/target normalization and spin2 highest weights | Section3, coefficient and raising sums | Section4 |
| Full eight-spin scalar partial isometry and n=2 rank-one restriction | Section4, ladder identities and excitation count | Sections6–9 |
| Full-H all-time contact and plane zeros, with nonstationary motion | Section5, separable ordered evolution and exact interaction correction | Section7 |
| Countable effect/jump convergence and rate bound | Section6,32-fold incidence and positive trace bound | Sections7–9 |
| All-label darkness and no-click equality | Section7, contact support plus bounded evolution uniqueness | Section8 |
| Complete CP/reference channel and trace preservation | Section8, explicit outputs and norm derivative | Theorem |
| Positive selected first-label bound | Section9, contraction estimate and seed overlap | Theorem |
| Displayed source/target energy means | Section10, full configuration-H action | Energy statement |

Every mathematical obligation in the stated conditional theorem is discharged
here; the earlier persistence source supplies the named code interface and
contains its broader finite-n setting. No external research-file receipt is
a mathematical premise of this proof.

The theorem covers arbitrary q, every translated/rotated target, normal
mixed states on H_2, arbitrary passive references, zero-probability labels,
all finite T>=0 and all real times for target unitary persistence. At T=0,
Phi_0 is the identity. The gamma=0 specialization is pure H evolution with
zero loading rate and is outside the positive-loading assertion. At j=0 the
same source/target and channel formulas have a static target; nonstationary
motion is asserted for j>0. No ratio formula divides by zero because the
main theorem assumes j,gamma>0. If a first-label amplitude is zero, that
branch has zero weight and is not conditionally normalized.

The physical initial domain has no prior Records. Arbitrary pre-existing
Record configurations, extra injected excitations, finite-density states,
repeated Record accumulation, almost-sure capture, and physical microscopic
nearest-neighbor implementation are not conclusions of this theorem. The
source and target use the same lattice spins, but their joint coupling and
reservoir remain supplied. This note publishes a positive conditional
construction; it does not classify all formation mechanisms or establish
an exclusion theorem.

The strongest open physical task is to derive a native event/state interface
that supplies an instrument with these probabilities and connects its state
and outputs to admissible physical Records. In this calculation the
pre-click quantum state and elapsed time are prediction inputs. No
assignment of that quantum state from Record configuration alone is derived.
The conditional loading theorem is not presented as completion or
near-completion of that stronger task. A pure protected site does not by
itself encode whether it was registered or how it is read.

## 12. Source provenance and verification record

The construction was developed at current-main source snapshot
`584755767deb8dfb670f07211d8446873fd0999b` and worktree HEAD
`688e7b02a3dabd6254193992e1f18da2532e683d`. The initial multiplicity-transfer
idea and the contact-only source repair were collaborative. The frozen
research author source was `LOCAL_AUTONOMOUS_FORMATION_STRETCH.md`, SHA256
`14cba858a08de56cf4502cb3d70aab81c968a49ef8152fc4a7feac607036dc5d`.

The separate `CONTACT_PUMP_INDEPENDENT.md` was written before its author read
the full frozen construction; `CONTACT_PUMP_COMPARISON.md` then compared the
complete source. The source/target idea and proposed quantitative values were
shared in the neutral brief, so this is a separately reconstructed proof and
implementation check, not hypothesis-blind discovery. Both used OpenAI
Astra/medium. It is same-family checking, not a different-vendor referee or
formal audit. `CONTACT_PUMP_DISPOSITION.md` records the source's accepted
conditional research scope. These filenames are provenance, not required
external input paths or evidence of a canonical primary execution.

The independent argument reconstructed the full spin2 intertwiner, the
actual-Z3 contact correction and all-time target evolution, and the bounded
countable CP process. Source-level author and checker controls used different
implementations of the configuration Hamiltonian; finite generator powers
corroborate concrete amplitudes, while the all-time claim rests on section5.
The assembled primary imports `scripts/contact_source_heisenberg_controls.py`.
It constructs the full256-dimensional local spin matrices with exact SymPy
arithmetic, compares the configuration Hamiltonian with a separately written
crossing-bond action, and checks actual-Z3 finite-support powers0 through6.
It also counts the source incidences for each of the three coordinate-edge
orientations, computes the source/target energy means, and applies the scalar
operator to the specified product seed. These are finite controls of the
stated formulas, not replacements for the countable-sum and all-time proofs.

Seven explicit in-memory changes exercise the same fail-closed checks:
source scaling, omitted lowest multiplet component, reversed hopping sign,
added target contact amplitude, a removed rotation, omitted contact diagonal
energy, and substitution of a zero-overlap seed. A mutation result is accepted
only when its intended check family rejects the modified construction. The
structured output retains every failed check; mutation coverage is finite.
The helper reads no files. The primary reads its declared helper and both
source notes for integrity and writes the one declared structured output;
it uses no external scientific dataset.

Reproduce using the repository's canonical envelope:

```bash
python3 - <<'PY_RUN'
import sys
sys.path.insert(0, "scripts")
from runner_cache import execute_and_write_cache
execute_and_write_cache("scripts/contact_source_heisenberg_code_preparation_2026_10_18.py", 180)
PY_RUN
```

The source, helper and primary are content-bound by that envelope. The
publication snapshot's `REVIEW_HISTORY.md` records actual execution, mutation,
source-review and conformance results; no formal audit verdict is implied.
This note adds a preparation theorem without changing the existing
persistence theorem. Its proof is self-contained, with the linked persistence
source retaining the broader finite-excitation context.
