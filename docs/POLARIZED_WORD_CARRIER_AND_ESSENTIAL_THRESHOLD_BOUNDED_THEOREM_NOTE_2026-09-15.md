---
claim_id: polarized_word_carrier_and_essential_threshold_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
runner: scripts/polarized_word_check_2026_09_15.py
upstream_dependencies: ["docs/NATIVE_RK_CHARGE_STABILITY_NOTE_2026-09-08.md", "docs/NATIVE_LOW_CHARGE_U1_DICTIONARY_NOTE_2026-09-08.md", "docs/NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md"]
claim_scope: "Bounded conditional polarized word representation and essential floor; supplied hypotheses and limit order retained in full proofs."
---

# Polarized word representation and essential floor

**Type:** bounded_theorem

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
trace_class: upstream_support
reachability_to_target: supports
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Scope and actual premises

The complete mathematical arguments below retain their supplied model, representation, parameters and limit quantifiers. Original dates, personal-review statements and recorded numerical outcomes are historical provenance, not current cache or independent-review claims. This package does not certify five independent exclusion routes. Full-field, native-phase, kinetic-interpretation and joint-limit targets remain open wherever the proofs say so.

Actual mathematical dependencies:

- [NATIVE_RK_CHARGE_STABILITY_NOTE_2026-09-08](NATIVE_RK_CHARGE_STABILITY_NOTE_2026-09-08.md).
- [NATIVE_LOW_CHARGE_U1_DICTIONARY_NOTE_2026-09-08](NATIVE_LOW_CHARGE_U1_DICTIONARY_NOTE_2026-09-08.md).
- [NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08](NATIVE_DYNAMICAL_CYCLE_FERMION_Z2_DICTIONARY_NOTE_2026-09-08.md).

<a id="owned-argument-1"></a>
## Owned argument 1: BLOCK9_POLARIZED_CHARGED_SECTOR_AND_FLAT_THRESHOLD

Original source identity: `BLOCK9_POLARIZED_CHARGED_SECTOR_AND_FLAT_THRESHOLD.md`. The original is also preserved byte-exact in the recovery manifest. Historical block names inside this complete argument refer to the ownership mapping, not to separate proof files.

### An exact polarized charged sector and its spectral threshold

Personal derivation, 2026-09-15. PROVISIONAL; personal derivation and bounded checks completed.
No independent scientific review or retained-status decision.
The same supplied native low-charge Hamiltonian is examined in a specified
infinite-volume boundary representation. This is not the periodic ground
state, a selected physical vacuum, or a new axiom. All statements concern
finite electric-edge changes from the fully polarized background.

The proposed result is stronger than a support count: this whole charged
Hilbert space has an exact word representation. Its spectral infimum is
2U-4sqrt(3)|t| at every translation momentum, for each fixed uniform
J>=0. The threshold is not an eigenvalue in a momentum fiber. Thus a
positive pair-creation energy and actual charge motion do not, by themselves,
identify an ordinary massive lowest particle band in this representation.

#### 1. The boundary representation and complete configuration classification

On Z^3 use positive-coordinate edges and

    E_(v,a)=epsilon_v(2n_(v,a)-1),  div E=2Q.

The reference electric field E^0_(v,a)=+1 has zero charge. Its corresponding
edge bits are n^0_(v,a)=(1+epsilon_v)/2. Consider configurations differing
from E^0 on only finitely many edges, with exactly Q_m=-1, Q_p=+1 and
all other charges zero. If chi_e indicates the flipped edges, then

    E=1-2chi,  div chi=delta_m-delta_p.              (1)

All chi edges carry their positive-coordinate direction. This directed
graph is acyclic because the height v_1+v_2+v_3 strictly increases along
each edge. A finite nonnegative integral flow with one unit source and
one unit sink on an acyclic graph consists of a single directed path.
For a direct proof, start at a minimal-height used vertex. Conservation
makes it m, and its outflow is one. Each subsequent nonterminal vertex
has one incoming unit and hence exactly one outgoing unit. The path ends
at p. A leftover finite balanced acyclic component would have a source,
which is impossible. This also excludes branches and extra closed loops.

Thus every configuration in this entire D=2 boundary sector is uniquely

    (m,w),  m in Z^3,  w=(i_1,...,i_n),
    i_j in {1,2,3},  n>=1,
    p=m+sum_j e_(i_j).                              (2)

The path is monotone in each coordinate; its edges are exactly the flipped
edges. The three letters encode existing physical edges, not an added
three-state site degree of freedom.

#### 2. Native phases and the exact word Hamiltonian

A positive charge can append any letter at the right end, or delete the
last letter when n>=2. A negative charge can prepend any letter i at the
left while m changes to m-e_i, or delete the first letter i while m changes
to m+e_i, again only when n>=2. These are all legal hops. The n=1 row
has six choices; every longer row has eight.

The native D=2 sign frame can be used without an infinite filled-fermion
product. The word graph is connected: a temporary prepended letter permits
deleting an old word and appending any new word without reaching length zero,
then removing the temporary letter restores the anchor. A one-letter word
of type i translates its anchor by +/-e_i through one extension and one
opposite-end deletion. These operations reach all anchors and words.
Any finite closed path of these configurations and any involved
operator stars embed inside a sufficiently large even periodic cube,
away from its boundary. The finite native signed-hole theorem makes its
hopping sign product equal to (-1)^(number of hops). Hence the phase
obtained along a path from a fixed reference configuration is independent
of that path. In this diagonal frame all hops are -1. The same finite
embedding makes every alternating ring flip +1 in this frame. This is a
local phase-cocycle argument, not an undefined infinite CAR product.

A flippable geometric face intersects the monotone path in exactly two
consecutive steps of different coordinate types. Its flip interchanges
those two letters. Conversely every adjacent unequal pair gives that
face. A face away from the path is unflippable in E^0; one changed edge
cannot make it alternating. Monotonicity rules out other intersections.

The Hilbert space and ring operator are therefore exactly

    H_pol = l2(Z^3) tensor F_+,
    F_+ = direct_sum_(n>=1) (C^3)^(tensor n),
    K_n = sum_(j=1)^(n-1) (I-Swap_(j,j+1)).         (3)

Equal neighboring letters give a zero summand, as required by the gate.
K is positive and preserves m,n. Define right and left letter creation
R_i,L_i on F_+ and let S_-i translate the anchor m by -e_i. Their adjoints
annihilate length-one words rather than enter an absent vacuum. Put

    R=sum_i R_i,   L=sum_i S_-i tensor L_i,
    A=R+R^*+L+L^*,
    H=2U+J K-lambda A,  lambda=|t|>0.              (4)

The standard bipartite sign change handles negative t. Equation (4) is
an exact unitary representation of the specified boundary sector.
Finite-word vectors form a dense form core. K is a direct sum of finite
positive matrices and H is its self-adjoint bounded-hopping perturbation.
The reference background has no flippable faces, so no infinite background
ring-energy subtraction has been hidden.

#### 3. Exact spectral floor and absence of a threshold eigenvector

Orthogonality of the first/last-letter ranges gives

    R^*R=L^*L=3I,   ||R||=||L||=sqrt(3).

Consequently ||A||<=4sqrt(3), and

    H>=E_pol I,  E_pol=2U-4sqrt(3)lambda.           (5)

Writing V_R=R/sqrt(3) and V_L=L/sqrt(3), the stronger form identity is

    H-E_pol = J K
       +lambda sqrt(3)[(I-V_R)^*(I-V_R)
                        +(I-V_L)^*(I-V_L)].        (6)

Each V raises word length by one and is an isometry. It has no nonzero
fixed vector: the length-one component of a fixed vector vanishes, then
induction gives every component zero. Thus (6) has trivial kernel, even
when J=0. The threshold cannot be an l2 eigenvalue.

To see that (5) is sharp before resolving momentum, use
u=(1,1,1)/sqrt(3). Each u^(tensor n) is killed by K_n. Take sine weights
on lengths1,...,N and an anchor vector uniform on [-M,M]^3. Its hopping
expectation is

    2sqrt(3)[1+2M/(2M+1)] cos(pi/(N+1)).            (7)

Both N and M tending to infinity give 4sqrt(3). This proves inf spec H=E_pol.
It also works for arbitrary nonnegative spatial ring coefficients, since
every individual ring term annihilates the uniform word vector at fixed
anchor and length. Momentum statements below use uniform J.

#### 4. Momentum fibers and an exact J=0 reducing subspace

Fourier transform the anchor with convention sum_m exp(-ik.m)f(m).
Then

    A(k)=sqrt(3)[R_u+R_u^*+L_v+L_v^*],
    v=v(k)=(exp(i k_1),exp(i k_2),exp(i k_3))/sqrt(3),
    H(k)=2U+J K-lambda A(k).                        (8)

Here R_u appends the unit vector u and L_v prepends v. The phase-correct
translation is the signed-frame anchor shift, conjugated back by the native
diagonal phase. No naive uncorrected Pauli permutation is presumed.

Choose a unit w perpendicular to both u and v; it exists in C^3 even
when they are linearly independent. The vectors

    v^(tensor r) tensor w tensor u^(tensor s),
    r,s>=0,                                       (9)

are orthonormal. Different total lengths are orthogonal; at equal length,
different r put w against a v or u factor and have zero overlap. The four
operators in (8) raise/lower r and s as unilateral shifts. At an endpoint,
annihilation gives zero because w is perpendicular to the corresponding
boundary vector. Thus (9) is a reducing subspace for A(k), unitarily
equivalent to sqrt(3) times the sum of two half-line adjacency operators.

Their sine transforms give spectrum [-4sqrt(3),4sqrt(3)]. Combined with
the norm bound, this is the entire spectrum of A(k), for every k, at J=0.
This subspace need not reduce K; the next argument is required for J>0.

#### 5. A slow word texture proves the same threshold for every fixed J

Use the same u,v,w and define a unit curve z:[0,1]->C^3 by

    z(s)=cos(pi s)v+sin(pi s)w,                    0<=s<=1/2,
    z(s)=cos(pi(s-1/2))w+sin(pi(s-1/2))u,          1/2<=s<=1.

This curve is continuous and piecewise smooth, with

    z(0)=v, z(1)=u, ||z'(s)||=pi,
    <z(s),z'(s)>=0 almost everywhere.              (10)

The last identity retains the complex phase, not just the projective
direction. It is crucial for coherent left/right creation. Orthogonality
to w makes it true on both segments for arbitrary complex u,v.
For all s,t, integration of (10) gives

    |<z(s),z(t)>-1|<=pi^2 |s-t|^2/2.               (11)

Indeed replace z(s) by z(s)-z(r) inside the integral of <z(s),z'(r)>;
the norm is bounded by pi^2|r-s|. This remains valid across the corner.

For n>=1 put

    xi_n = tensor_(j=1)^n z(j/(n+1)).              (12)

Its norm is one. The swap expectation is the squared modulus of adjacent
factor overlap, so

    <xi_n,K_n xi_n>
       =sum_(j=1)^(n-1)[1-|<z_j,z_(j+1)>|^2]
       <=pi^2/n.                                  (13)

The two creation overlaps obey the complex bounds

    |<xi_(n+1),L_v xi_n>-1| <=pi^2/[2(n+1)],
    |<xi_(n+1),R_u xi_n>-1| <=pi^2/[2(n+1)].        (14)

To verify (14), each paired old/new parameter differs by at most1/(n+2),
including the one endpoint factor. There are n+1 factors. Apply (11)
and telescope the product using the modulus-at-most-one property of every
factor. The sum of squared parameter changes is at most1/(n+1).

Take nonnegative normalized sine coefficients b_n on n=N,...,2N, with
sum_n b_n b_(n+1)=cos(pi/(N+2)), and set Xi_N=sum_n b_n xi_n. For N>=5,

    <Xi_N,(H(k)-E_pol)Xi_N>
      <= J pi^2/N
       +4sqrt(3)lambda {1-[1-pi^2/(2(N+1))]cos(pi/(N+2))}.           (15)

Both terms tend to zero at fixed J,lambda, uniformly in k. This proves

    inf spec H(k)=2U-4sqrt(3)lambda for EVERY k.     (16)

The isometry argument (6) works in each fiber and excludes a threshold
eigenvector. Xi_N tends weakly to zero because its word lengths tend to
infinity. Positivity and (15), or the finite-rank spectral-projection
criterion, show the threshold lies in essential spectrum. No infinite
matrix truncation is used to establish (16).

#### 6. Physical scope and comparison with periodic ground energies

For U>2sqrt(3)lambda this boundary sector has positive pair energy above
the zero-energy polarized neutral reference, despite its flat momentum
threshold. There is no isolated lowest massive pair band at that threshold
in these fibers. Other spectral structures or states are not classified.
If U>4lambda, the general native stability inequality also makes the neutral
reference a ground state against all allowed charge sectors.
Long strings in (15) carry the low-energy momentum; their length grows
without bound, so a fixed-length approximation would miss this mechanism.

The periodic finite-torus parent gives

    E2_periodic <=2U-(36/5)lambda
                <2U-4sqrt(3)lambda.                (17)

Thus the spectral infimum of this particular finite-excitation boundary
representation cannot be substituted for the periodic pair-energy infimum.
This is a distinction between thermodynamic constructions, not a theorem
about local weak limits of the delocalized finite-volume states. A vanishing
charge density can make local limits lose the charged excitation entirely.

The polarized boundary condition, the supplied Hamiltonian and the native
phase-correct translation all remain explicit. Neither this example nor
the periodic energy bounds select a physical vacuum. It provides a concrete
case where charge gap and motion coexist with a non-particle lowest spectral
threshold. It does not refute all vacua of this Hamiltonian, all choices of
law, or the framework axioms.


#### 7. Provenance, checks and negative-claim discipline

The conditional native inputs are the September8 RK charge stability,
global charge connectivity/exchange, low-charge U1 dictionary and dynamical
cycle fermion-Z2 dictionary notes in docs/. Their supplied Hamiltonian and
D=2 phase theorem are used explicitly; no selected-vacuum claim is inherited.
The complete word classification and the horizontal-texture bound above
are direct arguments on this carrier.

Wan and Tchernyshyov, [Quantum strings in quantum spin ice (2012)](https://arxiv.org/html/1201.5314v3),
already use strings specified by an endpoint and a word, endpoint hopping,
internal loop moves, and source-dependent spectral sectors. Their
checkerboard/pyrochlore perturbative Hamiltonians differ from the cubic
RK Hamiltonian here. No novelty is claimed for the string description.
Their result is not imported as a proof of (16).

The paired runner checks actual native Pauli phases on240 word configurations,
408 gated faces, three finite momentum matrices, and complex tensor
contractions through length256. These finite checks challenge the analytic
identities; they do not prove the infinite theorem by extrapolation.
The first radial expectation check lost precision in a BLAS dot product
at length7: error1.954e-13. A compensated scalar sum gives7.994e-15 with
the original1e-13 tolerance. The first runner, failure output and diagnosis
are preserved in review/block9_initial_radial_failure/. No tolerance or
analytic formula was weakened. A nonhorizontal phase curve is explicitly
rejected: its creation overlap stays a fixed distance from1.

See the N1-N8 scope review (`BLOCK9_ROUTE_AND_NO_GO_REVIEW.md`).
The only excluded object is an eigenvector at the stated sector's spectral
threshold. All-vacuum, all-law and axiom-level negative conclusions fail.

<a id="owned-argument-2"></a>
## Owned argument 2: BLOCK9_ROUTE_AND_NO_GO_REVIEW

Original source identity: `BLOCK9_ROUTE_AND_NO_GO_REVIEW.md`. The original is also preserved byte-exact in the recovery manifest. Historical block names inside this complete argument refer to the ownership mapping, not to separate proof files.

### Polarized-sector result: personal N1-N8 scope review

Read with the word-sector derivation (`BLOCK9_POLARIZED_CHARGED_SECTOR_AND_FLAT_THRESHOLD.md`).
The theorem excludes a threshold eigenvector for one explicit representation.
A broad claim that the framework cannot support particles is **FAIL**.
This is an author review, not independent validation or an audit verdict.

#### N1 — Real routes examined

| Route family | Actual work | Disposition |
|---|---|---|
| Directed electric-flow classification | Finite nonnegative unit flow on the height-acyclic cubic graph | ATTEMPTED: exact complete word carrier in this boundary sector |
| Operator lower bound | Sum of two creation-isometry defects plus positive rings | ATTEMPTED: rigorous floor and trivial threshold kernel |
| Fixed-momentum free reduction | Orthogonal marker between left/right strings, J=0 | ATTEMPTED: exact reducing two-half-line spectrum; not used for positive J |
| Positive-ring variational construction | Complex horizontal slow texture and sine length weights | ATTEMPTED: essential threshold for every fixed J and every momentum |
| Observable-selected spectroscopy | Identify that local source cyclic subspaces may miss parts of the spectrum | ATTEMPTED at formulation; exact response is the next task, and remains an escape from broad particle rhetoric |
| Periodic ground-state comparison | Reuse the explicit36/5 uniform-state energy bound | ATTEMPTED: periodic infimum is lower; boundary sector does not represent all thermodynamic choices |

No failed route is called closed by retained authority. Related lower-bound
and trial arguments are complementary proof components, not independent
physical walls. The route count does not prove an exhaustive physical no-go.

#### N2 — Dependence

The flat floor, long-string minimizing sequence and absence of a bottom
particle eigenvector concern one operator. They are not three walls.
Absence of an eigenvector follows directly from the isometry-defect identity;
flatness adds the explicit minimizing sequence. Neither fixes observable
spectral weight. Vacuum selection and the general full-source field problem
have no proved implication in either direction here; relation unresolved.
Independent axiom-wall count: zero.

#### N3 — Hidden assumptions

Background means the explicitly supplied all-positive electric reference,
not a selected vacuum. Finite excitation means finitely many changed edges.
Uniform nonnegative J is required for the momentum decomposition; the global
floor also holds for nonnegative spatial coefficients on their natural
positive form domain. lambda>0 is essential to the kernel argument.
The native phase convention is constructed by finite embeddings using the
provisional signed-hole parent; no infinite filled CAR product is assumed.
No physical time normalization or kinetic-isotropy closure is supplied.

#### N4 — Exact witness matching

| Input | Used residual | Match |
|---|---|---|
| Native D=2 signed-hole theorem | Finite closed hopping and ring phase cocycles | yes, every finite local configuration loop embeds in an even torus |
| Periodic36/5 energy bound | Comparison of spectral infima | yes, but only an energy comparison; not a local weak-limit theorem |
| Prior clock/foundation obstacles | None | not witnesses against this native sector |

No literature no-go is used as a substitute for the displayed proof.

#### N5 — Resolution audit

Per edge: actual bit flip and native phase checked, including all incident
stars. Per configuration: analytic classification covers all finite changes;
runner covers240 explicit states, not a full infinite census. Per mode:
the texture proof handles every k and fixed J; three k are matrix controls.
Per length: analytic inequalities hold for every n, numerical tensor controls
reach256. Per sector: trivial threshold kernel is proved only on F_+ and its
anchor product. Lattice-wide: no assertion about other vacuum representations,
periodic local limits, a full interacting field theory or axioms. The runner's
limits state these distinctions and no absence of all spectral poles is claimed.

#### N6 — Surviving partial closure

A cyclic subspace selected by a local pair source can have a different
spectral edge or internal eigenvalues. Periodic and nonpolarized neutral
states remain viable. Selecting a law/background and then deriving its
response is legitimate conditional science, not automatically an axiom
revision. Existing approved primitives have not been invalidated.

#### N7 — Strongest objection

A hostile reviewer should object that the polarized state is an extreme
boundary choice and that an essential threshold need not be visible to a
local measurement. Correct. The periodic variational inequality already
shows that this representation misses lower charged energies. The next
concrete obligation is to compute the cyclic spectral measure of an actual
local source, including its phase convention, and compare alternative
backgrounds. The note therefore makes no claim against all physical
particles or against the framework.

#### N8 — Prior comparison and novelty

The native parent notes establish gap bounds and finite connectivity, not
the complete polarized word representation with positive-ring slow textures.
The2012 quantum-string paper was read in full main text and appendices A-C
(HTML lines27-247); it already supplies related string and source-sector
ideas for different models. Standard shift spectra, flow decomposition and
variational spectral arguments are not claimed as new mathematics.
The delta is their explicit matching and horizontal texture in this supplied
native sector. No independent review has occurred.


## Canonical evidence and N1–N8 boundary

The route/proof appendices preserve the actual attempts, assumptions, residuals and surviving alternatives. Their components are not independent physical walls (N1/N2). Hypotheses and limits stay as written (N3/N4). N5 stdout distinguishes finite executed elements, sites, modes and blocks from unexecuted analytical limits. N6–N8 remain open to the positive routes and prior-result comparisons described above. No broad negative-certification PASS is asserted.

- [Program: polarized_word_check_2026_09_15](../scripts/polarized_word_check_2026_09_15.py); [current cache](../logs/runner-cache/polarized_word_check_2026_09_15.txt).

[Exact source recovery](work_history/review_loop/pr8159/README.md).
