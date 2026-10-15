---
title: Nearest-neighbor shared mediators for sampled interactions on one fixed pair
claim_id: nearest_neighbor_shared_mediator_programming_bounded_theorem_note_2026-10-15
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
artifact_role: theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: supports
conditional_surface_status: supplied finite nearest-neighbor coefficients and isolated vacuum auxiliaries for one fixed accessible pair on N_X=1
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: two separately checked positive finite-Hamiltonian constructions with explicit physical suppliers
audit_required_before_effective_retained: true
bare_retained_allowed: false
status: proposed_retained
canonical_parent_binding_complete: true
publication_pr: null
publication_status: canonical_source_for_regular_review
source_acceptance_status: checked_conditional_source
upstream_dependencies: ["finite_reservoir_boundary_clock_preparation_bounded_theorem_note_2026-10-15", "finite_local_clock_memory_resources_bounded_theorem_note_2026-10-15"]
runner: scripts/nearest_neighbor_shared_mediator_programming_2026_10_15.py
packet: .claude/science/physics-loops/toe-nearest-neighbor-shared-mediator-programming-20261015
next_trace_action: independent milestone review and cumulative stack validation; physical suppliers and full-program obligations remain open
---

Claim type: bounded_theorem

# Nearest-neighbor shared mediators for sampled interactions on one fixed pair

Two finite static constructions implement sampled interactions on the actual fixed pair
c=v0=(0,1,1), e=e(v0)=(0,2,1), while the original H=H0+K_X remains installed.
For arbitrary finite real samples, a finite horizon and positive error tolerance,
the displayed nearest-neighbor one-/two-qubit generator approximates the target
on the entire original N_X=1 sector, with every auxiliary and passive reference
retained at the same time. The coefficients, auxiliary vacuum, isolation and
precision are supplied resources; this is conditional finite-Hamiltonian mathematics.

The alternatives are separately proved and checked. The single-port construction
does not depend mathematically on correctness of the two-copy theorem.

| Construction | Program covered on this pair | Physical ports | Penalty certificate and prices |
|---|---|---|---|
| Two matched shared graphs | One Pauli pair Pc Pe with arbitrary sampled f_j | Two fresh ports at each data/clock endpoint | Uniform L>=N_A/4 and exact norm(L)=2m; inverse responses can still make sources enormous |
| One designed graph per axis | Simultaneous X_cX_e, Y_cY_e, Z_cZ_e sampled sum; supplied identity term priced separately | One port per axis, three axes fit the literal pair | Full-space L>=g_min N_A with explicitly positive graph-dependent g_min; subdivision compensation and source costs can be enormous |

The full unchanged author arguments appear below as two exact byte intervals,
with their original provisional wording preserved as historical source.
The current source disposition comes from the separately attributed reviews
and root acceptance records, not from rewriting those bodies or counting PASS lines.
ACTUAL_BINDING.json records the observed canonical sources and stack. The dated
PUBLICATION_STATE.json preserves the earlier unexecuted draft state. Actual
primary/cache/graph/publication outcomes require their separate receipts;
none confers independently audited retained status.

## Self-contained original inventory and generator

Choose integers L_b>=8, n_old>=2, Q=3^r>=3, and q_c>=1. Put M=4q_c,
X_*=max(n_old-1,Q)+2 and Y_*=1-L_b. The fixed old chain is
D={q_l=(l,0,0):0<=l<n_old}. The original boundary apparatus C consists of

    v0=(0,1,1), v1=(-1,0,0),
    v_j=(0,1-j,-1), 2<=j<=L_b,
    a0=(-1,1,0), b0=(0,1,0), a0'=(-1,0,1), b0'=(0,0,1),
    a1=(-1,-1,0), b1=(0,-1,0), a1'=(-1,0,-1), b1'=(0,0,-1).

There are Q original memory factors for each C site. Their positions are
e(u)+k d(u), 0<=k<Q, with k=0 called E and the rest F:

| u | e(u) | d(u) |
|---|---|---|
| v0 | (0,2,1) | (1,0,0) |
| v1 | (-2,0,0) | (-1,0,0) |
| v_j, j>=2 | (1,1-j,-1) | (1,0,0) |
| a0 | (-2,1,0) | (-1,0,0) |
| b0 | (1,1,0) | (1,0,0) |
| a0' | (-2,0,1) | (-1,0,0) |
| b0' | (1,0,1) | (1,0,0) |
| a1 | (-2,-1,0) | (-1,0,0) |
| b1 | (1,-1,0) | (1,0,0) |
| a1' | (-2,0,-1) | (-1,0,0) |
| b1' | (1,0,-1) | (1,0,0) |

The original program clock X consists of the M distinct sites around the square
at z=3 with lower-left corner (X_*,Y_*,3) and side q_c. Enumerate it cyclically
along bottom/right/top/left; adjacent indices are ordinary lattice neighbors.
The complete original set O is D union C union E union F union X. There are no
additional occupied sites in this literal geometry contract. All O states may
be arbitrary, including every C/E/F occupation and correlation, subject only
to the program-clock condition N_X=1.

H0=K+H_app is the unchanged supplied finite onsite/ordinary-neighbor Hermitian
generator on D union C, extended to the original memory and program-clock
factors. K includes its actual scalar and any installed reserve. In this
literal setup E/F have stipulated zero free terms. No positivity, product-state
or commutation simplification of H0 is used by the mediator theorem.
For a supplied a_c>0 define n_j=|1><1| at x_j, sigma^+=|1><0| and

    b_j=[n_j+n_(j+1)+i(sigma_(j+1)^+sigma_j^-
                          -sigma_j^+sigma_(j+1)^-)]/(2a_c),
    K_X=sum_j b_j,     N_X=sum_j n_j,     H=H0+K_X.

Indices are cyclic. Each b_j has spectrum {0,0,1/a_c,1/a_c}; thus
||K_X||<=M/a_c and [H,N_X]=0. Supply a certified full-space bound ||H||<=h0,
for example a bound on ||H0|| plus M/a_c. The clock identity coefficient
M/(2a_c) and every H0 scalar remain present. The proof also applies to any
fixed finite H satisfying its stated full-space bound and conservation
hypothesis; the ordinary-neighbor locality conclusion uses the literal
onsite/NN original generator just specified. H need not commute with n_j,
Pc or Pe.

The [finite-reservoir note](FINITE_RESERVOIR_BOUNDARY_CLOCK_PREPARATION_BOUNDED_THEOREM_NOTE_2026-10-15.md),
SHA256 3560cefa1c9a9e8064a11d2fc683bedd0cab3109905df5bffecdbe1999ad15ad,
supplies the original C/neighbor coordinate premise. Its complete raw source
26220ec9 is unique at bytes [14549,41771).
The [finite-memory-resource note](FINITE_LOCAL_CLOCK_MEMORY_RESOURCES_BOUNDED_THEOREM_NOTE_2026-10-15.md),
SHA256 32e4ab4a49fd7d5529a4b69059e2fc9b5966ebc1e41f9e81f422326f5a2a90cd,
supplies the memory-ray coordinate premise; its complete biased-memory body
f38d4590 is unique at [25736,51476). These are the two direct canonical
geometry dependencies. Neither its readiness/compression theorem nor the
reservoir pulse theorem is used to supply a ready input here.

The raw autonomous source b7267664 records the origin of this inventory and
the program-clock formula; it is provenance only. The clock formula is stated
and checked above, and no autonomous preparation theorem is invoked. Routed
readiness, later preparation proposals and git ancestry supply no premise.
At the observed origin/main bbada1fe these two canonical files are absent;
the root-designated feature head 3e647b40 contains them. Actual cumulative
stack review or parent landing and fresh source binding are integration
obligations, not reasons to infer a new theorem dependency from PR ancestry.

## Targets, proof obligations and common complete-output estimate

For the two-copy alternative the target is H+sum_j f_j n_j Pc Pe. For the
single-port alternative it is H+sum_(i,j) f_(ij)n_j Pc_i Pe_i, with i=X,Y,Z.
An optional supplied real identity program sum_j u_j n_j has its separate
norm, scalar, moment and calibration prices. These are sampled programs on
this pair, not a synthesis of every scheduled preparation gate.

Each argument establishes its own matrix response, counterterms and physical
geometry. The following proof obligations are proved inside the corresponding
body: full-sector positive penalty/kernel, finite inverse, second-order
vacuum contraction on N_X=1, all compensation terms, global mixed-sector
corrector, and uniform bare-input Duhamel comparison. The literal original
geometry is the explicit imported premise above. No terminal lemma equivalent
to the target is assumed.

In either construction let R be the full reduced inverse of the penalty,
V its source, C=J*VRVJ=C0-W and A=H+C0. The actual generator is

    K_Delta=Delta L+sqrt(Delta)V+A,
    X1=RVJ, Y2=RVX1, Z=J-epsilon X1+epsilon^2Y2,
    epsilon=Delta^(-1/2).

The exact residual is

    K_Delta Z-ZH_tar =
      epsilon[X1 H_tar-A X1+VY2]
      +epsilon^2[A Y2-Y2 H_tar].

R in Y2 includes all two-excitation sectors, including different graphs or
different noncommuting axes. VY2 includes three-excitation outputs. No H/K
commutator is dropped. For the body's full-space constants v,a,b,g, set
x=v/g,y=v^2/g^2 and

    F1=2x+T[(a+b)x+v y],   F2=2y+T(a+b)y,
    E_Delta=F1/sqrt(Delta)+F2/Delta.

Two bare endpoint terms and full-unitary Duhamel give
||exp(-itK_Delta)J-J exp(-itH_tar)||<=E_Delta for 0<=t<=T.
A finite Delta suffices for any positive nominal tolerance. Complete
mixed-output unhalved trace error is at most min(2,2E_Delta), including
arbitrary passive references. Auxiliaries start in vacuum and remain in the
comparison output; no tracing or postselection supplies the estimate.

The two-copy graph lemma allows abstract M>=1 when its certificate is supplied;
its literal square realization here has M=4q_c>=4. Zero samples are admitted.
The single-port source chooses Lambda strictly above its transported real
amplitudes, including the zero-sample case. The supplied finite horizon can
be zero. No statement is made here for arbitrary program-clock sectors,
additional occupied sites or arbitrary reset pairs. The strongest outstanding
extension is a complete NN realization of the entire fixed-site program,
with every pair and retained auxiliary output, under its actual shared
geometry and resource assumptions. That extension is not needed for the
bounded pair theorem and is not asserted.

## Separately attributed review qualifications

The two-copy source review a17942e0 and root acceptance 4808bc61 check a
feedback-variable response derivation, L>=N_A/4, exact ||L||=2m, and the full
number-sector residual. Publication must retain its four extra old–fresh
adjacencies: (-1,1,1) to (-1,1,0) and (-1,0,1); (-2,2,0) to (-2,1,0);
and (-2,0,-2) to (-2,0,-1). They are undeclared interactions whose absence
or full-norm error is supplied. Declared degree checks do not establish isolation.

The single-port source review 081d9eb9 and root acceptance 374139d5 independently
check the core through symmetric/antisymmetric modes and a completed inverse
source quadratic form. Its r/a cross response is -Pe/240 and its r and a
diagonals are c0-Pe/240, c0=961/960. Both odd terms, -q^2 Pe/240 and
-Lambda^2 Pe/240, require the installed counterterm. A constant transported
complex modulus removes clock-dependent odd shifts with two coefficients on
one physical edge. Whole-qubit positivity follows from a lowering-operator
quadratic form, not from free-particle statistics.

For simultaneous axes, positive operator inequalities add even though Pe_i
do not commute. Component inverses apply only on their actual one-component
excitation sectors; mixed sectors require the inverse of the sum. The review's
zero-target imaginary-source witness has a strictly negative Hermitian part
in a two-component coefficient of Q0VX, so the second corrector is essential.
These checks and their source exposure are in the unchanged archived reports.
The newer proof does not assume the two-copy conclusion.

For either construction define the complete omitted-edge set as every lattice
NN pair in O union A touching a fresh site, minus all declared edges.
This includes fresh–old, same-component and intercomponent pairs, not just
separated-graph cross talk. Each actual residual E_uv needs a full-Hilbert-space
bound after physical Delta scaling. With zeta_iso=sum||E_uv||, the trace budget
adds 2T zeta_iso and a positive reserve needs an additional scalar zeta_iso.
This also covers number-breaking faults. Onsite/original-term errors are
separate, and extra occupied factors require an enlarged inventory.

The single-port final source proves |E_iso|<=4m_total-3M-12 by incidence
counting. Its later saved-coordinate analysis found 35 omitted edges in one
fixture (18 fresh–old, 11 same-component, 6 intercomponent), including own-tail/
outer-cycle chords. That retrospective result is distinct from the predeclared
159 predicates and is not a universal count. Its raw output and the correction
of an overly narrow “bookkeeping” label remain preserved.

## Scalar, energy and precision contract

All onsite Schur compensations and clock counterterms are installed. The
two-copy scalar is scalar(H)+m Delta+s0+sum s_j/2. The three-axis scalar is
scalar(H)+(Delta/2)sum Tr B_i+S0+sum S_j/2. The one-port Pe fields are
traceless operators, not removable scalars; two-copy opposite Pe-only fields
cancel only when both complete detunings are included.

The bodies price whole-space norms, optional positive reserves and their
actual phase/mean/norm effects. Bare-input means use H+C0. Variances retain
Var_rho(H+C0) and the full source-flip term; H/C0 covariances are not replaced
by independent variances. Leakage probability tending to zero does not by
itself establish energetic reset or repeated auxiliary reuse.

Each source edge, each independently calibrated quadrature, onsite shift,
subdivision/root compensation, detuning, scalar and reserve is charged.
Small Green responses and the single-port Schur construction can make these
finite costs and required precision enormous. No polynomial, optimal or
common-strength-cap result is proposed.

A complete Hamiltonian residual zeta adds at most 2T zeta in trace norm;
joint preparation error adds once; terminal time error has the body's
full-norm allowance at the actual elapsed time. Full-space rather than
one-particle calibration is necessary for faults that leave the ideal sector.
Fixed nonzero external error floors do not vanish when Delta grows.

## Evidence, imports and publication state

| Item | Role and provenance | Present status |
|---|---|---|
| Fixed H0, clock and site inventory | Explicit finite Hamiltonian/geometry inputs above | Supplied; no native identification or old-site relocation |
| Vacuum auxiliaries, signed coefficients, phases and isolation | Engineering inputs in each exact proof | Supplied with precision and norm prices; no new axiom adopted |
| Two-copy proof | Exact 24,905-byte source 0f885e0c | Separately checked and root accepted conditional source |
| Single-port proof | Exact 28,846-byte source d4ed04f7 | Separately checked and root accepted conditional source |
| Selected author fixtures | One exact finite one-particle/geometry diagnostic for each alternative | Evidence at their selected inputs; not full-space dynamics or proof of the parameter family |
| Distinct reviews | Same selected model/family, source exposed; no new scientific run | Analytic checks, not blind/model-diverse or audit-ratified independence |
| Source-only primary | Exact source/interval/provenance integrity only | Actual binding is recorded; execution outcomes are in FINAL_VERIFICATION and PUBLICATION_EVIDENCE |

The two-copy fixture used L_b=8,Q=3,n_old=2,M=4, 74 original and 66 fresh
sites, with 54 declared predicates and actual launch/execution streams.
The single-port fixture used the same old parameters and 121 fresh sites
(43/35/43), with 159 declared predicates. Its source/input hashes and
self-recorded times are available; the recovered preexecution source and
POST_RUN_RECEIPT were assembled retrospectively. No contemporaneous
independent launch/exit receipt is manufactured for that run. Neither reviewer
nor root replayed either scientific program. The single-port review also
happened to record 159 metadata predicates; that is unrelated bookkeeping,
not another scientific experiment. Complete exact files and limitations are
in the compact packet; earlier archives are not recursively bundled.

The preserved specific failed source choices, omitted-term mutants, clock-sector
examples and saturated-v1 neighbor inventory are witnesses for those specified
attempts. This publication makes no universal no-go or route-exhaustion claim.
The positive conditional theorem and its declared domain are the claim.

The intended downstream consumer is the local program interface of a finite
clock-driven preparation. This result supplies a checked pair-level building
block; it does not supply waveform manufacture, every pair, clock/memory
initialization, routed readiness, physical energy identification or a native
autonomous device. The approved framework primitives retain their registered
roles; none is adopted here as a hidden coefficient, state or control supplier.

## Review record and hard integration conditions

Both complete proof bodies below are untouched. Historical relative paths,
provisional language and planned-check text are resolved through BODY_MAP.json
and SOURCE_MANIFEST.json in the packet; they do not override this dated
qualification. Root source acceptances are 4808bc61000184199bbe1d505e2d0ce25e1fab610b995f15c477eac3ec38a0d4
and 374139d56c7217ab52c59b1f94fcec8808fc29a1753fadc2428bf39de1009ec4.
Neither is an audit outcome.

The proposed primary reads archived scientific evidence only as integrity data:
it imports or runs no scientific helper. AUDIT_INPUT_PATHS includes all exact
package-local inputs and the two canonical geometry notes. It must not
print source-integrity success while the canonical binding flag is false.
The historical draft was only syntax-checked and source-checked. Its null
outcome fields remain unchanged as dated history. Actual canonical checks
are recorded separately in FINAL_VERIFICATION and PUBLICATION_EVIDENCE;
neither source integrity nor a focused checker is a scientific audit. No
helper-runner registry change is proposed.

Canonical integration verifies the actual source/parent bytes, complete body
intervals, primary cache, source-integrity mutations and the two intended
geometry edges, with actual outcomes in the publication evidence record.
The deterministic citation manifest accompanies the new node. Full pipeline,
strict audit lint and cumulative changed-evidence validation on an integrated
current-main candidate remain shared landing obligations, alongside cumulative
stack review or parent landing. Formal retained status belongs to independent
audit. No audit verdict, physical axiom or editable prompt is changed.



## Two matched shared graphs: complete historical proof

<!-- BEGIN EXACT two_copy BODY -->
# Two shared graphs for one sampled Pauli pair

Status: provisional author conditional theorem. The analytic shared-graph response below is proposed with a complete finite-time proof. A paired ordinary-nearest-neighbor graph certificate is an explicit hypothesis of the general result. Section7 constructs it uniformly for the actual v0 reset pair; section8 shows why it fails at the saturated v1 head. No source acceptance, independent check, retained audit, full-SWAP implementation, or multi-axis composition follows from this note.

## 1. Exact target and geometry premise

Let O be the unchanged finite original qubit inventory, including every data, dirty, work, and clock factor. For M>=1, clock sites x_j, 0<=j<M, are distinct from data sites c,e. Let P_c,P_e be nonidentity Hermitian Pauli operators on those two distinct sites. Let H=H0+K_X be the supplied full original Hermitian generator, including all its actual scalars, with [H,N_X]=0 and certified ||H||<=h0. In particular H need not commute with P_c, P_e, or n_j. The target is

    H_tar=H+W,       W=sum_j f_j n_j P_c P_e,       f_j real.

The admitted original domain is the full N_X=1 subspace, tensor arbitrary data and passive reference. This includes the supplied chi_k clock input but is stronger than that one prepared state. No old site moves and H is an identical summand at its original strength.

Supply a finite connected simple graph G=(V,E), |V|=m, max degree d<=6, with distinct labelled vertices a,b,a_0,...,a_(M-1). Supply two injective embeddings iota_+,iota_-:V -> Z^3 such that:

1. All 2m images are fresh sites, disjoint from O and from one another.
2. Each edge of G embeds as an ordinary lattice nearest-neighbor edge in both copies.
3. iota_±(a_j) is adjacent to the actual fixed x_j, iota_±(a) to c, and iota_±(b) to e.
4. Each labelled port therefore has graph degree at most five; all actual incidences must be certified, including any accidental adjacency to old sites. Only declared interactions are installed; absence or bounded error of other couplings is supplied.

The two embeddings need not be related by a geometric reflection. Their abstract adjacency matrices and installed coefficients are identical. This is a certificate to check, not an asserted general routing theorem. It replaces M separate cells at each data site by two ports per site. Failure to supply the certificate does not establish impossibility of a different implementation.

Use X_u,Z_u for fresh Pauli matrices, n_u=(I-Z_u)/2, and S_uv=(X_u X_v+Y_u Y_v)/2. Let r=1/12, h_d=1/4, and choose a finite positive q. For clarity units are chosen so these penalty parameters are dimensionless; q and the source amplitudes carry the same square-root-energy units if Delta is dimensional. Set

    L=sum_(epsilon=±)[ sum_(u in V) n_(u,epsilon)
                         -r sum_(uv in E) S_(u,epsilon;v,epsilon)]
          +h_d P_e (n_(b,+)-n_(b,-)),
    V_src=sum_j t_j n_j (X_(a_j,+)+X_(a_j,-))
                +q P_c (X_(a,+)-X_(a,-)).                (1)

All new nonidentity interactions are onsite or two-qubit ordinary NN under the certificate. The displayed P_e onsite fields in expanding its number operators cancel between the two copies. They may not be discarded one copy at a time.

## 2. Full auxiliary gap and one-particle inverse

For a complete two-qubit pair, -n_u-n_v <= S_uv <= n_u+n_v, including the doubly occupied state. Hence, with N_A the total fresh occupation,

    L >= (1-r d-h_d) N_A >= N_A/4.                       (2)

This inequality holds on the complete original and auxiliary Hilbert space. The only zero vectors have the full auxiliary vacuum Omega; every original vector is allowed there. With J0 appending Omega, P0=J0 J0*, Q0=I-P0,

    ker L=ran J0,      R=Q0 (L|Q0)^(-1) Q0,     ||R||<=4. (3)

Both copy occupations commute with L, as do N_X and each n_j. The full R is used throughout. With holes n^h_u=1-n_u, the same inequality applied to the hole expression shows L<=2m I: the two upper scalar contributions m+h_d P_e and m-h_d P_e sum to2m. Full occupation realizes this value. Thus ||L||=2m exactly. This upper bound also does not assume anything about the original state.

Let A_G be the ordinary real adjacency matrix and B=I-r A_G. Since ||r A_G||<=rd<=1/2,

    G0=B^(-1)=sum_(k>=0) (r A_G)^k,
    ||G0||<=2,     G0_uv>0 for all u,v in connected G.    (4)

Positivity of each entry follows from nonnegative walks and at least one finite path; no continuum or thermodynamic limit enters. Put u_v=(G0)_(v b), z=(G0)_(bb), and

    G_+=(B+h_d |b><b|)^(-1),
    G_-=(B-h_d |b><b|)^(-1).

Here h_d z<=1/2, so every denominator below is strictly positive. Direct rank-one multiplication verifies

    G_±=G0 ∓ [h_d/(1±h_d z)] u u^T,
    G_++G_-=2G0 + [2h_d^2 z/(1-h_d^2 z^2)] u u^T,
    G_+-G_-=-[2h_d/(1-h_d^2 z^2)] u u^T.              (5)

No general inverse theorem is imported: multiplying the first line by B±h_d|b><b| gives I using B u=|b> and u_b=z. When P_e has sign s, the one-particle matrix in the plus copy is B+s h_d|b><b| and in the minus copy is B-s h_d|b><b|. The sum of these inverses is independent of P_e; their difference is P_e(G_+-G_-). Resolving P_e here is legitimate because the two one-particle contractions involve only that commuting data involution. It is not a claim that H commutes with P_e.

Define exact finite constants

    alpha_j=(G_++G_-)_(a_j a_j)>0,
    beta=(G_++G_-)_(aa)>0,
    delta_j=(G_+-G_-)_(a_j a)
            =-2h_d (G0)_(a_j b)(G0)_(ba)/(1-h_d^2 z^2)<0,
    t_j=-f_j/(2q delta_j),
    s_j=t_j^2 alpha_j,        s0=q^2 beta,
    C0=s0 I+sum_j s_j n_j.                               (6)

The source coefficients can be arbitrarily large for long graph distances. No polynomial-overhead, finite common cap, or optimality claim is made. For a supplied finite graph, G0 and delta_j are computable; with rational r,h_d they are rational and delta_j is explicitly nonzero. Choosing q rational and computable f_j gives effective t_j without a sign or zero oracle. The case all f_j=0 may instead omit the whole apparatus.

## 3. Complete second-order contraction and its admitted domain

The full vacuum contraction C=J0* V_src R V_src J0 contains no cross-copy vacuum returns: a flip in one copy cannot remove an excitation in the other. Within a shared copy, all clock ports communicate through its actual inverse. Keeping all such contractions gives

    C = s0 I + sum_(j,k) t_j t_k n_j n_k
                    (G_++G_-)_(a_j a_k)
               +2q sum_j t_j delta_j n_j P_c P_e.       (7)

The unwanted term n_j P_c cancels exactly because the Pc source changes sign between copies, while the symmetric inverse is common. Clock-source squares have no Pe term because the inverse sum is independent of Pe. The Pc-source square is s0 I because Pc^2=I. This establishes the full operator identity, not just a selected data sign calculation.

On N_X=1, n_j n_k=0 for j!=k and n_j^2=n_j. Consequently

    C|_(N_X=1) = C0-W,          (H+C0)-C=H_tar.          (8)

On N_X>=2 there are additional generally nonzero clock-clock terms

    sum_(j!=k) t_j t_k n_j n_k (G_++G_-)_(a_j a_k).

They are retained in (7), not hidden in a full-domain theorem. The exact apparatus below preserves N_X, so (8) suffices on the admitted input. An implementation error that leaks N_X requires a full-space error allowance and is not certified by (8).

This is not a truncation of interacting virtual paths to one excitation. (7) only evaluates the second-order vacuum return. The global second corrector and full evolution below retain all higher auxiliary sectors.

## 4. Static generator and full-output same-time estimate

Install the actual static full-space operator

    K_Delta=Delta L+sqrt(Delta)V_src+A,
    A=(H+C0) tensor I_A,      Delta>0.                  (9)

C0 is installed. Its clock onsite terms are not part of the original K_X and are not erased as a phase; they cancel the explicitly calculated virtual shifts. H0+K_X remains unchanged as a summand.

Let J be J0 restricted to the admitted N_X=1 original domain. Set

    X1=R V_src J,        Y2=R V_src X1,
    Z=J-epsilon X1+epsilon^2 Y2,     epsilon=Delta^(-1/2).

L and R preserve auxiliary number, V_src changes it by one, and A acts only on the original factors. X1 has auxiliary number one, Y2 number two, and J*V_src Y2=0 by parity. Y2 includes actual two-particle returns within a shared graph and between the two copies; these are not replaced by products of one-particle inverses. Noncommutation of H with any data Pauli, n_j, or L is allowed.

The identities LX1=V_src J, LY2=Q0 V_src X1, and P0 V_src X1=J(C0-W) imply by direct multiplication

    K_Delta Z-Z H_tar
       =epsilon [X1 H_tar-A X1+V_src Y2]
            +epsilon^2[A Y2-Y2 H_tar].                 (10)

This exact residual keeps the original clock hopping and every H0 commutator. No transformation, cancellation, relocation, or attenuation of H is used.

For full-space bounds take

    v=2(sum_j |t_j|+q),       a=h0+s0+sum_j s_j,
    b=h0+sum_j |f_j|,         x=4v,        y=16v^2,
    F1=2x+T[(a+b)x+v y],
    F2=2y+T(a+b)y.                                         (11)

Then ||V_src||<=v, ||A||<=a, ||H_tar||<=b, ||X1||<=x, ||Y2||<=y. Finite-dimensional unitary Duhamel applied to Z exp(-itH_tar), followed by both bare endpoint differences, gives uniformly 0<=t<=T

    ||exp(-it K_Delta) J-J exp(-itH_tar)||
        <=F1/sqrt(Delta)+F2/Delta=:E_Delta.              (12)

For requested eta>0, Delta>=max(Delta_ref,(2F1/eta)^2,2F2/eta) is sufficient, where Delta_ref is any fixed positive reference choice. T=0 causes no difficulty, although the bound is not sharp there. The lift Z need not be an isometry and is not physically prepared. The physical auxiliaries start in the product vacuum and are retained as vacuum in the comparator. Both sides evolve for the same actual time t.

Tensoring any passive reference preserves (12). For every admitted mixed original/reference input and appended vacuum, the complete output trace norm error is at most min(2,2E_Delta). No original factor, clock, auxiliary, or reference is traced away. In particular the independent chi_k preparation of the autonomous source is admitted. A supplied subsequent CPTP map contracts the trace bound; normalized selected outcomes need a separate estimate.

## 5. Full scalar, positivity and resource ledger

The exact full normalized Pauli scalar is

    scalar(K_Delta)=scalar(H)+m Delta+s0+(1/2)sum_j s_j. (13)

Each of the 2m auxiliary number terms contributes Delta/2. Hopping and sources are traceless. The opposite Pe detunings have zero total scalar and cancel their Pe-only fields. The clock counterterms supply the displayed scalar even though, on N_X=1, their actual mean is sum_j s_j p_j. Scalar coefficients are not the same as prepared means.

A full-space norm bound is

    B_full=h0+s0+sum_j s_j+2m Delta+sqrt(Delta)v.        (14)

An installed reserve R_pos=h0+sqrt(Delta)v makes K_Delta+R_pos I nonnegative on every original/auxiliary sector. It adds R_pos to (13), the actual mean and B_full, not the variance; the comparison in (12) then carries the exact phase exp(-it R_pos). No positivity follows from L alone for a signed total generator. An additional full-space perturbation norm zeta requires an additional reserve zeta for this certificate.

The added graph has 2m fresh qubits, 2|E| auxiliary edges, 2M clock-source edges, two Pc-source edges and two Pe-detuning edges. Each old addressed site uses two distinct fresh nearest neighbors, independent of M. Counts are for declared supports before any vanishing term is omitted. Every auxiliary incidence is its graph degree plus its declared external port, at most six under the certificate. H's existing graph and strengths remain present. Coupling strength is not bounded merely by bounded degree.

Whole-term norm loads, before assigning global scalar reserves, are: 2sqrt(Delta)|t_j|+s_j on old clock x_j; 2sqrt(Delta)q on c; 2Delta h_d on e; and at fresh u in either copy, Delta[1+r deg_G(u)+h_d 1_(u=b)]+sqrt(Delta)[q 1_(u=a)+sum_j |t_j|1_(u=a_j)]. The scalar s0 and any reserve are assigned to one specified fresh site and fully charged there. This whole-term inventory uses n_j X_(a_j), Pc X_a and Pe n_b as the declared two-qubit blocks. Expanding into separate Pauli occurrences redistributes one-body accounting but cannot reduce an asserted cap without an explicit convention.

For any admitted initial original density rho, put A0=H+C0 and p_j=Tr(rho n_j). Orthogonal single-auxiliary flips give

    mean(K_Delta)=Tr(rho A0),
    Var(K_Delta)=Var_rho(A0)+2Delta[q^2+sum_j t_j^2 p_j]. (15)

Every H/C0 and clock/data covariance remains inside Var_rho(A0); no independence of original inputs is assumed. Small auxiliary return error does not refund these actual energy/precision resources. Equation (12) gives nonvacuum probability <=E_Delta^2, but only the coarse penalty expectation bound 2m Delta E_Delta^2, which need not vanish as Delta grows.

A joint preparation trace error eta_p adds once. A full implemented Hamiltonian error E_actual(t) adds 2 integral_0^T||E_actual(t)||dt in trace norm. For phase-sensitive terminal-time uncertainty use (B_full+R_pos)|delta t| in operator norm, or twice this in trace norm, plus the error integral over the actual interval. Sector-only calibration does not control arbitrary leakage. For the displayed normalized whole-term blocks, there are 2m+2|E|+3M+5 added coefficient occurrences before omitting zeros, plus one if a reserve is installed. Uniform absolute coefficient errors <=xi therefore give the conservative full-space bound (2m+2|E|+3M+5)xi, with original-H error and reserve error added separately. Appending this one-Pauli-pair simulator to a compatible existing prepared-map comparison costs at most 2E_Delta in complete output trace norm. This statement alone does not implement the whole noncommuting SWAP or compression program.

## 6. Application to other pairs and program composition

For any other addressed pair, this conditional theorem requires an actual paired-graph coordinate certificate before application. A finite coordinate/edge list with collision, unit-distance, degree, and graph-isomorphism checks would discharge that placement hypothesis for a finite instance; a uniform routing argument is needed for a symbolic family. The certificate is a combinatorial statement, not the global quantum simulation theorem restated in different words. Section7 supplies a uniform certificate for the literal v0 reset pair. Section8 exhibits a different literal pair where this certificate cannot apply at all.

The paired graphs may have length and strengths growing rapidly. Existing four-auxiliary unit-cube cells do not supply this certificate. Conversely, their M-dependent incidence restriction does not rule out the shared construction. The full-SWAP/multi-axis problem additionally requires compatible simultaneous networks and a new incidence analysis; independent one-pair layouts cannot simply be superimposed at saturated old sites. The full local-interface question therefore remains open even if the positive pilot theorem is independently confirmed.

## 7. Explicit matched NN graphs for the v0 reset-pair pilot

There is a constructive positive case on the literal original layout. Choose the fixed pair

    c=v0=(0,1,1),       e=e(v0)=(0,2,1),

with arbitrary chosen nonidentity Pauli P_c,P_e. Let L_b>=8, Q=3^(r_mem) with integer r_mem>=1, n_old>=2, x_max=max(n_old-1,Q), X_*=x_max+2 and Y_*=1-L_b. Keep every original C site, memory ray, old chain, and clock site exactly as in the autonomous source. No additional occupied spectator site beyond this literal list is assumed; an enlarged inventory requires new collision checks. Let M be its supplied positive multiple of four, and put q_c=M/4. The clock is the square perimeter at height z=3 with lower-left corner (X_*,Y_*,3).

Take one copy of the same square perimeter at z=4 and one at z=2. Their vertices directly above/below every original x_j are the respective a_(j,+),a_(j,-), and their edges are the same cycle in the same order. Let a_(j*,±) be the lower-left corner in each cycle. Define

    a_+=(0,1,2),      b_+=(0,2,2),
    a_-=(-1,1,1),     b_-=(-1,2,1).

Thus a_± is a fresh neighbor of c, b_± a fresh neighbor of e, and a_±--b_± is an ordinary NN edge. Add a path from b_+ to the upper-cycle root with the successive integer line segments

    (0,2,2) -> (0,2,4) -> (0,Y_*-6,4)
              -> (X_*,Y_*-6,4) -> (X_*,Y_*,4),          (16)

and a path from b_- to the lower-cycle root with segments

    (-1,2,1) -> (-2,2,1) -> (-2,2,-2)
              -> (-2,Y_*-2,-2) -> (X_*,Y_*-2,-2)
              -> (X_*,Y_*-2,2) -> (X_*,Y_*,2).          (17)

Every segment is filled with its unit lattice steps, with shared endpoints counted once. Both path lengths are exactly

    ell_path=X_*+16-Y_*.

For (16), the lengths are 2, 8-Y_*, X_*, and 6. For (17), they are 1,3,4-Y_*,X_*+2,4,2. The paths have no repeated vertex, meet their own square only at the declared root, and avoid the added a leaf except at the b endpoint's edge. They therefore define identical abstract graphs: the M-cycle, one length-ell_path path attached at j*, and a single a leaf attached to b. Matching graph vertices is by cycle label and by distance along the path, not by geometric reflection.

The paths/copies avoid one another. The upper path after its initial vertical leg has z=4, with its horizontal bridge strictly at y<Y_* and x between0 andX_*. Its initial z=2..4 segment has x=0,y=2. The lower path uses x=-2,y=2 for its initial downward leg, then z=-2, and its final upward leg has x=X_*,y=Y_*-2 and stops at z=2. Its final y approach stays below the clock square until the root. None of these intersections is an upper-copy vertex. The lower cycle has x>=X_*,y>=Y_*,z=2, so it misses the upper path's x=0 initial leg and y<Y_* bridges. The two a leaves lie outside every path; each b vertex occurs only as its own path's initial endpoint. These four data-port vertices are distinct from one another.

All original nonclock sites lie in z=-1,0,1. Their full literal positions, beyond that box bound, matter for the four new data-neighbor sites and the initial lower-path vertices. The five negative-x memory rays have x<=-2 and transverse (y,z) among (0,0),(1,0),(0,1),(-1,0),(0,-1). All other memory rays have x>=1, except the v0 ray with x>=0,y=2,z=1. Thus no memory occupies x=-1, or x=-2,y=2. This excludes a_-=(-1,1,1), b_-=(-1,2,1) and the downward segment x=-2,y=2 from every memory ray. All original C sites have x=-1 or0, so the downward segment also avoids C. The original C list has only a0'=(-1,0,1), b0'=(0,0,1), and v0=(0,1,1) at z=1; these do not collide. The old chain has y=z=0. The remaining lower path is at z=-2 or at y<Y_*, and the upper path at z>=2, so they avoid all nonclock originals. The original clock is z=3 and x>=X_*,y>=Y_*; the upper initial vertical segment is at x=0 and the lower final vertical segment is at y=Y_*-2. Both avoid it. No unchanged old site is used as transit or assumed clean.

This proves the certificate of section1 for every displayed finite L_b,Q,n_old,M in the source family, for this one specified pair. There are

    m=M+ell_path+1 vertices per copy,       |E|=m,
    2m fresh auxiliaries in total.

The abstract maximum graph degree is3, attained only at the chosen cycle root. Including its original clock-source edge gives degree4. Other cycle ports have total degree3; b has degree3 including its data detuning; a has degree2 including its data source; nonport path sites have degree2. At the original x_j,c,e exactly two extra NN edges are used. The coarse general r=1/12,h_d=1/4 constants above apply unchanged; the actual degree gives a stronger gap but is not needed for the claimed estimate.

Thus sections1–5 plus this construction give a complete proposed ordinary-NN two-qubit prepared-map theorem for any real sampled program sum_j f_j n_j P_(v0)P_(e(v0)), while preserving all fixed original sites and H0+K_X. Because the supplied original H0+K_X already has ordinary-NN two-qubit/onsite support, this explicit pilot makes the complete Hamiltonian ordinary NN. It is a single-pair pilot within the original layout, not the entire autonomous preparation program.

## 8. Preserved failure for another literal reset pair

The same construction does not extend automatically to every original data site. In the literal layout,

    v1=(-1,0,0)

has the six occupied neighbors

    q0=(0,0,0),    e(v1)=(-2,0,0),
    a0=(-1,1,0),  a1=(-1,-1,0),
    a0'=(-1,0,1), a1'=(-1,0,-1).

All are original factors whose arbitrary inputs must be retained. Hence v1 has zero fresh nearest neighbors, while the certificate in section1 needs two at each data role. Reversing Pc/Pe does not repair this incidence failure. This is an exact failure of this certificate on that pair; it does not rule out other encodings, use of occupied transit with a new proof, different global networks, or a revised admissible preparation/layout contract. In particular, it is not a general no-go for ordinary-NN autonomous implementation. Any proposed general routing lemma for this certificate must therefore restrict its data sites to adequate accessible vacancies. A complete implementation on the unchanged layout needs a different mechanism at saturated sites.

The full multi-axis SWAP program also cannot be certified by applying the single-pair result independently three times: that spends six fresh ports per old data site, before existing neighbors, and needs a new global compatibility analysis. The two-copy pilot resolves the M-dependent incidence issue for the stated pair but leaves the axis and saturated-site issues explicit.

## 9. Evidence, attribution and current disposition

The exact autonomous target and fixed original geometry come from the frozen b726766403bf6f4b0080172d046cf773facad028eed538d7473417683b931bb7 derivation, with freeze39d2efbbbe60bbf4fb47d569398d84666779e5de9f689739cb76129bdcacbffc. Its complete argument was read. The full simultaneous multi-port proof f02e80d2c69be61819c9fc43a8a3125cc1432f895c01b93a5e7081ec2b4d8755 was read as the closest supplied two-path/global-residual method, including its placement, mixed-sector and scalar restrictions. The present proof does not assert that its per-cell certificate is met. The root route note3033aa58 was prior exposure, not proof. The finite-range mediator source's sections1–3 already expose clock-source cross contractions, clock onsite counterterms and the one-clock cancellation; its data-word port is generally three-body for a two-site Pauli word. Those mechanisms are credited as prior method, not rediscovered as globally novel. The additional proposed ingredient here is the two-copy local detuning/source construction with the literal fixed-pair NN placement. No complete literature or repository novelty claim is made.

One exact, predeclared finite diagnostic was executed once. At L_b=8,Q=3,n_old=2,M=4 it checked74 original sites and66 fresh sites, both33-vertex graphs, their28-edge tails, every declared NN edge/port, and exact responses from independently inverted33-by33 rational matrices. The two-clock response and omitted-mirror/clock-counterterm mutations were preserved. Full logs, the exact program, input, pre-execution source and hashes are under runs/selected_01. It did not form the full2^66 auxiliary matrix or numerically check evolution, the full-sector gap, the global residual, or the symbolic parameter family. Those remain complete analytic author arguments here, not independent computational evidence. The diagnostic's54 Boolean predicates are bookkeeping of its finite coverage, not54 independent confirmations.

This candidate is source-exposed author discovery. No independent reviewer or formal audit has examined it in this task. It uses supplied finite Hamiltonians, isolation, clean auxiliary preparation, fixed geometry, coefficient access and accuracy resources. These conditions are not derived from the minimal axioms or supplied by a new primitive. No physical axiom or primitive, original Hamiltonian, model setting, editable instruction, canonical repository, Git state, PR or audit record was changed. All artifacts stay in the one authorized candidate directory.

Actual current surface status: conditional-support. Target claim type: bounded_theorem. Trace class: upstream_support to the ordinary-NN autonomous program interface. Reachability: partially_closes, specifically the fixed v0 single-Pauli-pair sampled program. Bare retained allowed: false. Independent audit required before any retained claim: true. The next scientific decision is an independent check of this exact final argument, followed by a distinct mechanism for multiple axes and saturated original sites if the pilot survives.

<!-- END EXACT two_copy BODY -->


## One port per axis: complete historical proof

<!-- BEGIN EXACT single_port BODY -->
# One physical port per axis from a designed inverse and two source quadratures

Status: proposed conditional bounded theorem, source-exposed author discovery. No independent review or audit is claimed. The target is a sampled one-pair program on the admitted one-excitation clock sector, retaining every original, auxiliary and passive-reference factor over the same physical time. The construction below also supplies three disjoint NN components for the X/Y/Z sum on the actual fixed v0,e(v0) pair. It does not implement all pairs of the autonomous preparation word or resolve the saturated v1 site.

## 1. Domain, imports and the failed real-source version

Keep the literal original chain, C apparatus, all E/F memory rays and the fixed clock square of the autonomous derivation b726766403bf6f4b0080172d046cf773facad028eed538d7473417683b931bb7. Their exact source snapshots are in SOURCE_MANIFEST.json. Let H=H0+K_X, with its full scalar and certified ||H||<=h0, and [H,N_X]=0. No commutation with a data Pauli or n_j is assumed. All original inputs and passive references are arbitrary on N_X=1. Supply only fresh auxiliary product vacuum, isolation of unlisted interactions, finite coefficient access and the stated precision. No old site, state or term of H is moved, replaced, attenuated or assumed clean.

For one nonidentity Pauli P_c at c and P_e at a distinct e, the target is

    H_tar=H+sum_(j=0)^(M-1) f_j n_j P_c P_e,     f_j real.

Root exposed the unchecked matrix suggestion below. Its numerical values, and the earlier two-copy candidate, are not accepted premises: the needed identities and full-sector argument are proved here. Generic inverse-response, Schur-complement and global-residual methods are attributed to the supplied earlier mediator family. No complete novelty claim is made.

On abstract core terminals (r,a,b), put

    G=[[1,-1/960,1/8],[-1/960,1,1/8],[1/8,1/8,1]],
    D=G^(-1),       h_d=1/4,       c0=961/960.

The off-diagonal absolute row sums of G are at most1/4, so 3I/4<=G<=5I/4 and 4I/5<=D<=4I/3. Direct cofactors give

    det G=892769/921600,
    D_rr=D_aa=907200/892769,
    D_bb=921599/892769,
    D_ra=15360/892769,
    D_rb=D_ab=-115320/892769.                         (1)

For s=±1, D_s=D+s h_d|b><b|>=11I/20. Multiplying the rank-one identity verifies

    D_s^(-1)=G-[s h_d/(1+s h_d)] G|b><b|G,
    (D_s^(-1))_ra=-s/240,
    (D_s^(-1))_rr=(D_s^(-1))_aa=c0-s/240.             (2)

In particular the root cross-entry suggestion is correct, but both diagonal entries retain an odd part. A real clock source with transported amplitude x_j and a real q Pc source at a would give the desired cross term when x_j=120 f_j/q, while leaving -(x_j^2/240)n_j Pe. With general unequal f_j^2, this is not removable by an onsite clock scalar and a single onsite Pe field. This is a failure of that real-source ansatz, not a no-go for one-port mediators.

## 2. The NN one-particle matrix and full-sector positivity

We give an explicit way to implement D through a subdivided cycle, then attach a clock network only at r. Let a physical auxiliary cycle contain three distinct terminals r,a,b. Its three arcs between consecutive terminals have disjoint internal vertices. A direct length-one arc ij receives hopping coefficient D_ij. If an arc ij has k>=1 internal vertices, place the positive path matrix T_arc=I-A_path/12 on its internal vertices. Let g_arc=(T_arc^(-1))_(1k)>0. Connect i to its first vertex with coefficient1 and j to its last vertex with coefficient -D_ij/g_arc. All these couplings are real, possibly signed. Eliminating this internal path gives cross response D_ij because minus the endpoint product times g_arc is D_ij. Its diagonal shifts are retained below. For k=1, both endpoint couplings meet the same internal vertex; they remain different physical edges.

Let a connected clock transport graph have maximum degree3, matrix T_clk=I-A_clk/12, distinct clock-source vertices u_j, and a vertex u_* adjacent to the physical core r. Its physical edges and clock-source edges must all be NN. Install coupling -w between u_* and r, with w=1/12. Define

    tau=T_clk^(-1),       beta_j=w tau_(u_j,u_*)>0,
    gamma_j=tau_(u_j,u_j)>0.                           (3)

The Neumann walk expansion proves strict positivity because the graph is connected and ||A_clk/12||<=1/4. No inverse zero-test is used.

Collect every arc-internal vertex and every transport vertex into a space E, disjoint from the three core terminals. Let T be the direct sum of all their path/transport matrices, and Q the real E-by3 matrix of endpoint couplings just specified. It includes the entry -w from u_* to r. Then T>=3I/4 and the installed full one-particle matrix is

    B=[[T,Q],[Q^T,D+Q^T T^(-1)Q]].                    (4)

The lower block is an actual installation, including every diagonal compensation. On a subdivided arc ij, its off-diagonal is D_ij-D_ij=0; on a direct arc it is D_ij. Thus all remaining off-diagonal entries have declared NN edges. The apparent dense formula in (4) introduces no additional core chord. Clock elimination changes only the r diagonal. The complete finite rational matrix is fixed before Delta is chosen.

For s=±1, let B_s=B+s h_d|b><b|. Completing the block square factors B_s as

    B_s=F^* diag(T,D_s) F,
    F=[[I,T^(-1)Q],[0,I]].                            (5)

Let Qabs=sum_(u,i)|Q_ui|, and take the conservative rational certificate

    g=(11/20)/[1+(4/3)Qabs]^2 >0.                     (6)

Since ||F^(-1)||<=1+||T^(-1)Q||<=1+(4/3)Qabs, (5) gives B_s>=g I. It is not necessary that the physical matrix be diagonally dominant; signed cycle hoppings are essential to the response.

For every fresh auxiliary site v write sigma_v^+=|1><0|, n_v=sigma_v^+sigma_v^-, and S_uv=sigma_u^+sigma_v^-+sigma_v^+sigma_u^-. Install on the complete qubit Hilbert space

    L=sum_v B_vv n_v+sum_(u<v) B_uv S_uv+h_d Pe n_b.   (7)

This has the exact one-particle matrix B_s at Pe sign s. More importantly, a positive matrix inequality implies the full-qubit inequality: if B_s-gI=R^*R, then

    L_s-g sum_v n_v
      =sum_alpha (sum_v R_(alpha v) sigma_v^-)^*
                  (sum_v R_(alpha v) sigma_v^-) >=0.   (8)

This identity uses no bosonic/fermionic commutation convention, excitation truncation or free-particle approximation. It proves L>=g N_A on every auxiliary sector. L annihilates exactly all original vectors tensored with auxiliary vacuum. A sufficient complete norm is

    ell_L=sum_v B_vv+sum_(u<v)|B_uv|+h_d.             (9)

All B_vv are positive by (5), and every n_v and S_uv has norm1. Pe commutes with all auxiliaries, so resolving Pe for (8) proves a joint operator inequality even if H does not commute with Pe.

The Pe n_b term expands as (Pe-Pe Z_b)/2. Its Pe-only field is physically present; unlike the mirror construction it does not cancel against another copy. The full operator (7), its onsite compensation and the counterterm below must be installed together.

## 3. Exact response and the quadrature repair

The block inverse of (4), verified by multiplication, has core block D_s^(-1). Because the transport component connects only at r with negative coupling -w,

    (B_s^(-1))_(u_j a)=beta_j(D_s^(-1))_ra=-s beta_j/240,
    (B_s^(-1))_(u_j u_j)=gamma_j+beta_j^2(c0-s/240),
    (B_s^(-1))_aa=c0-s/240.                           (10)

Arc subdivisions affect the core diagonal compensation and full gap, but not these blocks. Off-diagonal transport entries are tau_(u_j,u_k)+beta_j beta_k(c0-s/240).

Choose a positive real q and a finite supplied Lambda with Lambda>max_j|120 f_j/q|. For effective inputs a certified strictly larger bound suffices; no maximum equality decision is needed. Set

    x_j=120 f_j/q,
    z_j=[x_j+i sqrt(Lambda^2-x_j^2)]/beta_j,
    V=q Pc X_a+sum_j n_j[Re(z_j)X_(u_j)+Im(z_j)Y_(u_j)]. (11)

Here Y|0>=i|1>, so the created amplitude at u_j is exactly z_j. There is one fresh qubit and one physical clock edge per j. Its two Hermitian quadratures are two coefficients on that same edge, not two sites or two fresh neighbors. The combined bracket has norm |z_j|. Splitting into Pauli occurrences must charge both real coefficients when pricing separate calibration errors.

Let J0 append the auxiliary vacuum, P0=J0J0*, Q0=I-P0 and R=Q0(L|Q0)^(-1)Q0. R is the full reduced inverse, ||R||<=1/g. At second order only one auxiliary excitation is present, so (10) applies. Define

    s0=c0 q^2,
    s_j=|z_j|^2[gamma_j+c0 beta_j^2]
        =Lambda^2[gamma_j/beta_j^2+c0],
    d=(q^2+Lambda^2)/240,
    C0=s0 I+sum_j s_j n_j-d Pe.                       (12)

The full clock-space contraction is obtained by retaining every n_j n_k in the transport quadratic form, with coefficients z_j^* z_k(B_(Pe)^(-1))_(u_j,u_k), plus q^2(c0-Pe/240) and the clock/data cross term. It is Hermitian; off-diagonal clock pairs combine to twice their real parts. No cross-clock term is deleted on general clock inputs.

On the admitted N_X=1 subspace, n_j n_k=0 for j!=k. The Pc cross term is

    -[q beta_j Re(z_j)/120] n_j Pc Pe=-f_j n_j Pc Pe.

The two odd diagonal contributions are

    -q^2 Pe/240,
    -(1/240)sum_j |z_j|^2 beta_j^2 n_j Pe
        =-Lambda^2 Pe/240.                            (13)

The second equality uses both the constant transported modulus and sum_j n_j=1. Therefore, as an exact operator identity on that entire domain,

    C:=J0* V R V J0=C0-W,
    W=sum_j f_j n_j Pc Pe.                            (14)

There is no n_j Pc term, since the actual cross entry in (10) has zero even part. Both Pe shifts, including the Pc-source square, are canceled by installing the negative onsite field -d Pe in C0. It is not discarded, counted as a scalar, or presented as modification of the original H. On clock vacuum the installed field overcompensates by -Lambda^2 Pe/240, and multiple clock excitations have extra cross terms. Thus (14) is not a full-clock-domain theorem. The exact dynamics below preserve N_X; full-space error allowances handle imperfect leakage.

## 4. Complete bare-output dynamics and scalar/energy costs

Install the static full-space generator

    K_Delta=Delta L+sqrt(Delta)V+A,
    A=(H+C0) tensor I_A,      Delta>0.                (15)

Let J be J0 restricted to N_X=1 and define X1=RVJ, Y2=RVX1 and Z=J-epsilon X1+epsilon^2Y2, epsilon=Delta^(-1/2). L,R preserve total auxiliary number; V changes it by one. Hence X1 has number1, Y2 number2, and J*VY2=0 by parity. Neither Y2 nor the full interacting evolution is restricted to one particle. The identities LX1=VJ, LY2=Q0VX1 and P0VX1=J(C0-W) give by direct expansion

    K_Delta Z-Z H_tar
      =epsilon[X1 H_tar-A X1+VY2]
         +epsilon^2[A Y2-Y2 H_tar].                  (16)

Every noncommuting H0/K_X term remains in this identity. Z need not be an isometry and is not a supplied dressed preparation.

For a horizon T_fin>=0, use full-space bounds

    v=q+sum_j |z_j|,
    a=h0+s0+sum_j s_j+d,       b=h0+sum_j |f_j|,
    x=v/g,                    y=v^2/g^2,
    F1=2x+T_fin[(a+b)x+v y],
    F2=2y+T_fin(a+b)y.

Two bare endpoint differences and unitary Duhamel applied to (16) give, uniformly 0<=t<=T_fin,

    ||exp(-it K_Delta)J-J exp(-it H_tar)||
       <=F1/sqrt(Delta)+F2/Delta=:E_Delta.             (17)

Choosing Delta>=max(Delta_ref,(2F1/eta)^2,2F2/eta) suffices for any eta>0, with any fixed positive Delta_ref. The full auxiliary vacuum is retained in the comparator, and every original/passive-reference input is allowed on the admitted domain. Tensoring references preserves operator norm; complete mixed-output trace error is at most min(2,2E_Delta). No tracing, postselection, changed elapsed time or altered H is used.

The exact normalized full Pauli scalar and a complete norm bound are

    scalar(K_Delta)=scalar(H)+(Delta/2)Tr B+s0+(1/2)sum_j s_j,
    B_full=h0+s0+sum_j s_j+d+Delta ell_L+sqrt(Delta)v. (18)

The Pe counterterm is traceless, while auxiliary onsite compensation contributes through Tr B. Neither is dropped. The actual reserve

    R_pos=h0+d+sqrt(Delta)v                            (19)

makes K_Delta+R_pos I nonnegative on every original and auxiliary sector. It adds to the scalar, actual mean, full norm and comparator phase exp(-it R_pos). It does not change variance. This reserve is a sufficient price, not an optimized one.

For arbitrary admitted initial density rho, A0=H+C0 and p_j=Tr(rho n_j), orthogonal flips give

    mean(K_Delta)=Tr(rho A0),
    Var(K_Delta)=Var_rho(A0)+Delta[q^2+sum_j |z_j|^2 p_j]. (20)

All covariances remain inside Var(A0). Small auxiliary nonvacuum probability <=E_Delta^2 gives only the penalty-energy bound Delta ell_L E_Delta^2, not energetic return or reuse. The amplitudes and compensations can grow very rapidly with graph distance. There is no common-cap or efficiency theorem.

For a physical edge the clock-source load is sqrt(Delta)|z_j| in the combined-block convention, or sqrt(Delta)(|Re z_j|+|Im z_j|) when the two quadratures are charged separately. The Pc source adds sqrt(Delta)q at c, and Pe detuning plus counterterm add Delta h_d+d at e. Each fresh vertex v has load Delta[B_vv+sum_u|B_uv|+h_d 1_(v=b)], plus its source load if any. Clock onsite s_j is charged at x_j; global s0 and R_pos are assigned to a specified fresh site and charged there. H's original loads remain.

All displayed coefficients are computable from finite rational graph inverses and supplied computable f_j, with strictly positive certified denominators and the chosen positive radicand margin. If scalar/hopping/Pe/source-quadrature/counterterm coefficients have errors, sum their full operator norms; a bound zeta on the complete Hamiltonian error costs at most2 T_fin zeta in trace norm. The number of declared added coefficients per component is m+|E_B|+3M+4, counting the two clock quadratures separately, the Pc source, Pe detuning, M clock counterterms, global s0 and the Pe counterterm, before a reserve. A joint preparation trace error adds once. Terminal timing error costs at most2(B_full+R_pos)|delta t| in trace norm, together with calibration integration over the actual interval. Full-space perturbations of norm zeta require an additional reserve zeta for this positivity certificate.

## 5. Actual disjoint three-component geometry at v0,e(v0)

Set c=(0,1,1), e=(0,2,1), L_b>=8, Q_mem=3^(r_mem)>=3, n_old>=2, X_*=max(n_old-1,Q_mem)+2>=5 and Y_*=1-L_b<=-7. For an integer q_c>=1, the original M=4q_c clock is the square perimeter at z=3 from (X_*,Y_*,3) to (X_*+q_c,Y_*+q_c,3). No additional occupied sites beyond the literal source inventory are assumed. All line segments below contain their integer unit steps. No original factor is used as transit.

Component1 uses core terminals and internal vertex

    a1=(-1,1,1), b1=(-1,2,1), r1=(-2,1,1), d1=(-2,2,1)

in the square a1--b1--d1--r1--a1. Its transport graph is the original clock square shifted to z=2, with one attached tail from u1=(-3,1,1) through

    (-3,3,1), (-3,3,-2), (-3,Y_*-4,-2),
    (X_*,Y_*-4,-2), (X_*,Y_*-4,2), (X_*,Y_*,2).

The last point is the transport-cycle root; the first is adjacent to r1. The tail has length X_*+23-Y_*. Each original clock site couples to its shifted neighbor at z=2. The four core sites use the compiler of section2; only the b1--r1 arc is subdivided.

Component2 uses

    a2=(0,1,2), b2=(0,2,2), r2=(-1,1,2), d2=(-1,2,2)

in the square a2--b2--d2--r2--a2. Its transport graph is the clock square at z=4, with tail from u2=(-1,1,3) through

    (-1,3,3), (-1,3,5), (-1,Y_*-3,5),
    (X_*,Y_*-3,5), (X_*,Y_*,5), (X_*,Y_*,4).

This tail has length X_*+15-Y_*. Its start is adjacent to r2 and its end is the transport-cycle root. Clock source ports are the shifted sites at z=4.

Component3 uses a3=(1,1,1), b3=(0,3,1). Its core cycle is the union of two internally disjoint paths from a3 to b3:

    P: (1,1,1)->(1,1,2)->(1,3,2)->(0,3,2)->(0,3,1),
    Q: (1,1,1)->(2,1,1)->(2,1,3)->(2,4,3)
                    ->(0,4,3)->(0,4,1)->(0,3,1).

Their lengths are5 and11, so this is a16-vertex cycle. Choose r3=(2,4,3). Its three terminal arcs are compiled by section2; the core vertices other than r3,a3,b3 are auxiliary subdivision sites, with their full onsite compensation charged.

The third transport cycle is the outer square perimeter at z=3 with corners

    (X_*-1,Y_*-1,3), (X_*+q_c+1,Y_*-1,3),
    (X_*+q_c+1,Y_*+q_c+1,3), (X_*-1,Y_*+q_c+1,3).

It has M+8 vertices. Clock ports are the outward NN site along each clock edge, with each original corner assigned to its outgoing edge in the traversal bottom/right/top/left. Thus bottom uses y=Y_*-1, right uses x=X_*+q_c+1, top uses y=Y_*+q_c+1, left uses x=X_*-1. These M source ports are distinct and none is an outer-cycle corner. Attach a tail from u3=(3,4,3), adjacent to r3, through

    (3,Y_*-2,3), (X_*-1,Y_*-2,3), (X_*-1,Y_*-1,3).

Its length is X_*+3-Y_* and its end is the outer-cycle lower-left corner, which is not a clock-source port.

These three geometries are disjoint and fresh for all stated parameters. The core1 sites have z=1,x=-1 or-2,y=1 or2; negative-x old memory rays at x<=-2 have transverse (y,z) in {(0,0),(1,0),(0,1),(-1,0),(0,-1)}, so none meets them. No old memory occupies x=-1. The only old C sites at z=1 are (-1,0,1),(0,0,1),(0,1,1), so core1 is also disjoint from C. Core2 is at z=2. Core3's z=1 vertices lie at y=1 with x=1 or2, or y=3 or4 with x=0; the source's only positive-x memory at z=1 has y=0 or2, and no original nonclock site has y>=3. Its remaining sites have z=2 or3 and x<=2, outside both clock and other cores. Core3's listed z=2 points have x=1,2 or y>=3, while core2 has x=-1,0,y=1,2.

The component1 tail leaves through x=-3,y>=1,z=1, then descends at y=3 to z=-2, below all original sites; its final ascent is at y=Y_*-4, below both original box and every transport cycle, and stops at z=2. The component2 tail leaves at x=-1,z=3 to y=3, then uses z=5 until its final descent to z=4. These differ from the finite core3 coordinates and from each other. The component3 tail has x=3,z=3 until y=Y_*-2, then stays below its outer cycle until the root. Its transport cycle has x>=X_*-1>=4 and y>=Y_*-1; the other transport cycles lie at z=2 and4. The first two tails' portions near those x ranges are at z=-2 or5 or outside their cycles' lower y bounds. Thus no tail meets another graph. Each tail meets its own cycle exactly once. Original clock sites have z=3, x>=X_*, y>=Y_*; the new outer cycle is exterior and every new z=3 tail/core portion is either at x<=3 or y<Y_*. This excludes original-clock collisions. Unlisted nearest-neighbor interactions remain excluded or charged by the isolation premise, including adjacency between different components.

Each transport graph has maximum degree3. Its root is either a clock-source vertex (components1,2) or not a source (component3); fresh total degree is at most4. Each core terminal has two core-cycle edges and at most one external edge: r to transport, a to c, or b to e. At c the three used fresh neighbors are (-1,1,1),(0,1,2),(1,1,1), exactly its three available neighbors in the literal inventory. At e the used neighbors are (-1,2,1),(0,2,2),(0,3,1). At every clock site the used fresh neighbors are below, above and outward; together with its two old clock bonds this gives degree5. One component per axis therefore fits without sharing an auxiliary or spending a second port for a quadrature.

The fresh qubit counts are

    m1=M+X_*+27-Y_*,
    m2=M+X_*+19-Y_*,
    m3=M+X_*+27-Y_*,
    m_total=3M+3X_*+73-3Y_*.

Each component is a core cycle and a transport cycle joined by one edge; tails are part of the transport graph. Therefore |E_B,i|=m_i+1. Counts exclude the clock/data source and detuning edges, which are priced separately above.


### Complete isolation accounting

Freshness and disjointness do not mean that the occupied cubic-lattice adjacency graph equals the declared interaction graph. Let O be the complete literal original coordinate set and A the union of the fresh coordinates in section5. Let E_decl be the union of all declared auxiliary hopping edges and the c/a_i,e/b_i,clock/u_(ij) edges. Define the complete omitted-edge set, including edges within one component, by

    E_iso={{u,v}:u,v in O union A, |u-v|_1=1,
                     {u,v} intersects A, {u,v} not in E_decl}.       (22)

Every NN pair involving a fresh factor is either in E_decl or in E_iso. E_iso includes fresh–original, same-component fresh–fresh and intercomponent pairs; no geometric separation is substituted for isolation. Onsite faults and changes to the original–original H terms are priced separately as in section4. Additional occupied factors beyond O union A require an enlarged inventory and fault sum.

The nominal Hamiltonian sets every E_iso coupling to zero. For actual residual Hermitian interactions E_uv, with no commutation or number-conservation assumption, let

    zeta_iso=sum_({u,v} in E_iso) ||E_uv||.

Full-space Duhamel adds at most2 T_fin zeta_iso in trace norm, and a further installed scalar reserve zeta_iso preserves the whole-space positivity certificate. That reserve adds to the actual scalar/mean/norm and comparator phase. General scalar or onsite calibration errors are not erased by this edge accounting. A uniform edge-error bound nu gives zeta_iso<=|E_iso|nu. Since there are at most6m_total fresh incidences, |E_iso|<=6m_total is always a sufficient finite bound. Using the declared counts gives the sharper conservative bound |E_iso|<=4m_total-3M-12 for the three-component geometry. These are symbolic bounds, not the selected-fixture count.

Additional retrospective geometry analysis of the already saved selected-fixture coordinates found exactly35 omitted edges:18 fresh–original,11 same-component and6 intercomponent. ISOLATION_ADJACENCY_INVENTORY.json lists all177 NN pairs touching fresh factors within that recorded inventory, with142 declared and35 omitted; both classes are included explicitly. In particular the outer-cycle left edge has omitted neighbors on the x=3 tail when X_*=5. For that selected fixture, uniform residual-edge norm nu costs zeta_iso<=35nu. This enumeration was requested after the one inverse fixture and is not part of its predeclared159 checks or independent validation. No inverse or dynamics was rerun. The general theorem uses(22) and the complete norm sum, not a projection of the selected count onto other parameter choices.

## 6. Simultaneous X/Y/Z response with one global inverse

Take three components of section5, with Pc_i=X_c,Y_c,Z_c and Pe_i=X_e,Y_e,Z_e, supplied real f_(ij), positive q_i and Lambda_i>max_j|120 f_(ij)/q_i|. Each has its own computed B_i, beta_(ij), gamma_(ij), z_(ij), L_i,V_i,s0_i,s_(ij),d_i. Put

    L=sum_i L_i, V=sum_i V_i,
    S0=sum_i s0_i, S_j=sum_i s_(ij), Dsum=sum_i d_i,
    C0=S0 I+sum_j S_j n_j-sum_i d_i Pe_i,
    H_tar=H+sum_(i,j) f_(ij)n_j Pc_i Pe_i.             (21)

The L_i generally do not commute, since their Pe_i act on the same e. Nevertheless L_i>=g_i N_i is an operator inequality; summing gives L>=g_min N_total, with the entire original-space vacuum kernel and full reduced inverse norm at most1/g_min. Every individual auxiliary component number N_i commutes with every L_k. On a sector with only component i excited, every other L_k vanishes on the original space because its auxiliaries are vacuum. Hence the restriction of the global inverse is exactly that component's inverse. A source in another component cannot remove its excitation, so cross-component second-order vacuum contractions vanish. Adding (14) therefore gives C=C0-(H_tar-H) on N_X=1 without diagonalizing the three Pe_i simultaneously.

The second corrector Y2=RVRVJ retains actual sectors with two distinct components excited; their inverse is the inverse of the sum, not the sum/product of separate inverses. The global residual (16) is proved with this R exactly as before. Use

    g=g_min, ell_L=sum_i ell_L,i,
    v=sum_i[q_i+sum_j|z_(ij)|],
    a=h0+S0+sum_j S_j+Dsum,
    b=h0+sum_(i,j)|f_(ij)|

in (17). The full scalar is scalar(H)+(Delta/2)sum_i Tr B_i+S0+(1/2)sum_j S_j. The reserve h0+Dsum+sqrt(Delta)v makes the complete operator nonnegative. The initial variance is Var_rho(H+C0)+Delta sum_i[q_i^2+sum_j|z_(ij)|^2 p_j]. All original/auxiliary/reference outputs and the entire physical interval are retained. Noncommutation of the Pe-only counterterms with H or with each other is already included in A and the residual.

Consequently this proposed theorem covers the X/Y/Z sampled sum on the one fixed accessible pair. A supplied scalar sampled identity term U=sum_j u_j n_j can be installed directly as an original-clock onsite term in both target and generator. Set u_bound=sum_j|u_j|, add u_bound to a,b,B_full and the sufficient positive reserve, and add (1/2)sum_j u_j to the exact scalar. Replace A0 by H+C0+U in the mean and variance, and price these M additional coefficient errors. The residual proof is unchanged because U preserves N_X. This gives a conditional local implementation of a sampled SWAP logarithm for this pair when its three Pauli and scalar coefficients are supplied. It does not synthesize the whole preparation waveform, apply three axes to every scheduled pair, or make the v1 neighbor obstruction disappear.

## 7. Bounded theorem, preserved limits and actual evidence

Conditional theorem statement: under the literal finite original geometry and premises in sections1,5, finite computable coefficients f_(ij), a certified full norm for the unchanged H0+K_X with [H0+K_X,N_X]=0, fresh product-vacuum auxiliary qubits and priced isolation/coefficient access, the displayed static ordinary-NN two-qubit Hamiltonian gives, for every finite horizon and positive error target, a finite Delta with the complete prepared-map bound(17) for the X/Y/Z program(21) on N_X=1. One may omit two components for a single-Pauli-pair pilot. Every original site, H0/K_X term, passive reference and auxiliary output is retained at the same physical time. The full-space positive reserve and scalar are(18)-(19), with the explicit three-axis replacements in section6. This is an author-proposed conditional theorem pending independent review.

Real one-quadrature sources fail for arbitrary f_j through the explicit n_j Pe shift. Omitting the Pe counterterm fails even after fixing the transported modulus: both -q^2 Pe/240 and -Lambda^2 Pe/240 are present. Replacing the signed designed core by a generic positive-hopping graph does not preserve the zero even cross entry. Deleting charged root/subdivision diagonal shifts changes the core inverse. Applying the one-excitation contraction on all clock sectors fails. Independent per-axis one-particle inverses do not replace the mixed full-sector inverse in the dynamics.

All six neighbors of v1=(-1,0,0) remain original occupied factors q0,e(v1),a0,a1,a0',a1'. The present construction uses fresh ports and offers no implementation there. This is an explicit limitation of this construction, not a no-go for other mechanisms. Additional occupied sites, common strength caps, efficient resource scaling, physical initialization and control manufacture remain outside the result. The axis theorem is conditional finite-Hamiltonian mathematics, not derived native physics or retained status.

The one predeclared exact Fraction fixture ran once on 2026-10-15 at12:11:34-12:11:35 UTC. Its fixed input L_b=8,Q_mem=3,n_old=2,M=4 has74 original and121 fresh sites, with component sizes43,35,43. SELECTED_PLAN.md and PREEXEC_FREEZE.json seal the plan, rational phases, code and pre-execution argument. Direct Gauss-Jordan inversions of the complete physical one-particle matrices B_s, checked by exact multiplication, have zero response defect at both signs and every selected source. All159 declared checks passed, including mutual NN placement, degrees, both odd diagonal contributions and the six occupied neighbors of v1. The literal coordinate/edge inventories and every rational result are in EXACT_RESULT.json; EXECUTION.log records the single invocation outcome.

The declared mutants were detected: real sources gave unequal odd diagonal coefficients; omitting the full Pe counterterm left +Pe/120, omitting its Pc-source portion left +Pe/240; deleting root compensation changed the cross entry; clock vacuum left -Pe/240, and the selected two-clock state had nonzero extra response. The latter two findings preserve the admitted-domain limit. These are exact selected algebra/geometry checks, not independent scientific review. No full many-qubit matrix, arbitrary-H time evolution, parameter sweep or second inverse/dynamics execution was made. The symbolic geometry family, full-sector gap, noncommuting simultaneous-axis inverse and bare-output dynamics are analytic arguments above, rather than conclusions established by the fixture.

<!-- END EXACT single_port BODY -->
