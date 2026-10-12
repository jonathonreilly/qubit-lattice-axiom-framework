---
claim_id: finite_energy_sector_selection_bounded_theorem_note_2026-10-12
claim_type: bounded_theorem
claim_scope: "Supplied free-chain Fock representation with a uniform actual positive-energy expectation bound: high-excitation concentration and normalized trace-distance bound, even square-root sharpness and an explicit vacuum correlation counterexample."
upstream_dependencies:
  - current_preserving_refinement_bounded_theorem_note_2026-10-12
  - concrete_gapped_chain_bounded_theorem_note_2026-10-12
  - local_even_continuum_bounded_theorem_note_2026-10-12
runner: scripts/finite_energy_sector_selection_identity_2026_10_12.py
artifact_role: theorem
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: partially_closes
target_claim_id: null
target_blocker_text: "Determine what a uniform actual-energy expectation bound controls in the supplied two-branch limit."
source_of_blocker_text: frontier_question
next_trace_action: "Keep the present concentration theorem conditional; separately control observable energy transfer and remaining low-sector limits before any continuum-correlation claim."
conditional_surface_status: "Chosen model, state, normal Fock representation and imposed uniform energy bound; Current parent remains an open proposal."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Positive conditional concentration theorem with sharpness and explicit limits; ordinary proof review supplies no framework selector or retained audit."
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

**Type:** bounded_theorem

Status: conditional-support

Primary runner: [source identity and reconstruction only](../scripts/finite_energy_sector_selection_identity_2026_10_12.py).
Its output checks named bytes only. It executes zero mathematical predicates,
scientific mutations or formal proofs and supplies no N5 certificate or packet PASS.

**Publication review record:** The complete 238-line final source and focused
review were accepted at the earlier campaign deadline; publication was deferred.
The reviewer performed a source-exposed focused check in a separate context of
the same selected model and effort, reusing previously checked parent passages.
Root is a coauthor, supplied the post-freeze vacuum counterexample and compared
a separately sealed reconstruction. This is neither blinded nor model-diverse
review. Original pending-review language below records author chronology.


# Finite actual energy suppresses high-branch excitations

**Conditional author lemma, 2026-10-12.** In the common state-preserving
Fock embedding of the supplied current-preserving construction, a uniform
bound M on the expectation of the actual positive Hamiltonian implies
high-excitation probability at most M/sqrt(m^2+2v^2/c^2). The state is
within that probability's square root in trace distance of a normal state
with no high excitations. This is concentration near a subspace; it neither
forces convergence to a particular low state nor collapses the high
observable algebra in C*-norm.

## 1. Scope, sources and chronology

The plan and exact source identities were frozen before this proof in
finite_energy_sector_selection/PLAN_FREEZE.json, at 15:48:25 UTC.
The current source is CURRENT_PRESERVING_REFINEMENT_PROBE.md, SHA-256
`1104de3922002720beecb7eb2bd106b64025aea0afb1e11b8f86750dfb59e30d`;
the actual positive full-spin GNS Hamiltonian is from
CONCRETE_GAPPED_CHAIN_PROBE.md, SHA-256
`0aebc2ded245d9bc9ecae364db0d1a042f9642771ed788794dafd73fb7f621bd`,
C20-C22 and C28. The covariance/Fourier/even-CAR convention is from
LOCAL_EVEN_CONTINUUM_PROBE.md, SHA-256
`7be1a72e2b59c5c61b68ead6d663e8d4e179b21e2497243a2859a4082ea7813b`.
Complete snapshots and hashes are in the new evidence directory. Necessary
positive-energy passages were refreshed; unchanged prior source coverage is
reused. No new root reconstruction has been read. Root independently studies
this shared target, so this is author work, not blinded independent review.

The previously read instruction snapshot 72a7cf00... and its byte identity
for the thirteen applicable files at 34ab62523138756eded9bdcc8a35fd2ff61f926f
are reused. Existing current/energy packets, repository files, prompts,
axioms and audit status are unchanged. No scientific executable or numerical
experiment is needed or asserted.

## 2. Common Fock space and the actual energy bound

Let h=h_low direct-sum h_high be the positive-polarization one-particle
space of the current construction. Each summand has one complex fiber over
the current coordinate p. The real coefficient maps J_c intertwine the
chosen polarizations; their restrictions J_c,+ are complex isometries on
positive-polarization spaces. Their exterior powers, with vacuum fixed,
therefore define isometries V_c=Gamma_-(J_c,+) into F=F_-(h).

This is a Hilbert-space/state representation embedding. Only the already
proved even-CAR/spin embeddings are asserted at the quasilocal algebra
level. It does not manufacture an odd-inclusive bilateral spin embedding.
Concrete C20-C22 supplies the full spin GNS Fock representation and actual
canonical Hamiltonian dGamma(E_c), with vacuum energy exactly zero and
positive one-particle energies. No divergent offset is subtracted here.

The image F_c=V_c F_(original,c) is the Fock space over both branch bands
|p|<1/c. On that closed subspace the actual transported Hamiltonian is

    H_c=dGamma(e_c,0 direct-sum e_c,1),
    e_c,1(p)^2=m^2+(2v^2/c^2)(1+sqrt(1-c^2p^2)),
    Lambda_c=sqrt(m^2+2v^2/c^2).                      (F1)

The high branch satisfies e_c,1>=Lambda_c over its *entire* band. The
infimum is approached at the critical endpoints; an endpoint eigenvector
is not required. This global lower bound is different from its stronger
fixed-compact-momentum asymptotic 2v/c+O(c).

Let N_high=dGamma(1_high) on F, let P=1_{N_high=0}, and Q=1-P. On F_c,

    H_c >= Lambda_c N_high >= Lambda_c Q              (F2)

as positive quadratic forms. On each finite particle sector this is the
pointwise sum of the one-particle inequalities; increasing particle-sector
and spectral truncations extend it to the form domains. In particular,
finite H_c expectation implies finite N_high expectation. This argument
uses positivity of the full Fock Hamiltonian, not the signed two-component
coefficient matrix D_c. The latter alone would not give F2.

For a density operator rho_c on F supported in F_c, define actual energy
by the extended positive expectation Tr(H_c^(1/2) rho_c H_c^(1/2)). Assume
it is at most a fixed finite M. Form/spectral approximation in F2 yields

    Tr(rho_c N_high) <= M/Lambda_c,
    delta_c:=Tr(rho_c Q) <= min(1,M/Lambda_c)
                         <= min(1,Mc/(sqrt(2)v)).     (F3)

No finite particle-number cutoff or pure-state assumption is made. More
generally, Tr(rho_c 1_{N_high>=k})<=M/(k Lambda_c) for integers k>=1.
For states supported in an actual energy spectral subspace [0,R] with
R<Lambda_c, F2 and the commuting branch number imply Q rho_c=0 exactly.
The normal-state assumption means a trace-class density in this supplied
representation; no assertion for arbitrary nonnormal states is inserted.

## 3. Normal-state and vector distance bounds

Use trace distance D(rho,sigma)=one half ||rho-sigma||_1. For all
sufficiently small c with M/Lambda_c<1, put

    p_c=Tr(P rho_c)=1-delta_c,
    sigma_c=P rho_c P/p_c.                            (F4)

It is a normal state supported in the no-high-excitation sector. Then

    D(rho_c,sigma_c)<=sqrt(delta_c)<=sqrt(M/Lambda_c),
    ||rho_c-sigma_c||_1<=2sqrt(M/Lambda_c).            (F5)

Proof with the normalization explicit: purify rho_c as a unit vector Psi
in F tensor an auxiliary Hilbert space; project and normalize it to
Phi=(P tensor 1)Psi/sqrt(p_c). Their overlap is sqrt(p_c), so their pure
density difference has trace norm 2sqrt(1-p_c), by its two-dimensional
eigenvalue calculation. Partial trace is contractive in trace norm on
self-adjoint trace-class operators: duality tests only operators A tensor
1 with ||A||<=1. The two partial traces are exactly rho_c and sigma_c.
This proves F5 without replacing the state by an unnormalized compression.
If p_c=1 the states coincide; p_c=0 precludes F4, but is excluded at the
stated sufficiently small spacings. At remaining spacings the trivial
distance bound one to any no-high state is available, without F4.

Equivalently, for every bounded observable A on F,

    |Tr(rho_c A)-Tr(sigma_c A)|
                       <=2||A||sqrt(M/Lambda_c).     (F6)

This includes represented even spin/CAR observables and is uniform over
their norm unit ball for each such state. P is a representation-level
spectral projection; no claim that P is quasilocal, or that F4 is a physical
preparation/selection operation, is needed.

For a unit vector psi_c of energy expectation at most M,

    ||Q psi_c||<=sqrt(M/Lambda_c),
    chi_c=P psi_c/||P psi_c||,
    ||psi_c-chi_c||^2=2(1-sqrt(1-delta_c))
                                  <=2delta_c.        (F7)

Here delta_c=||Q psi_c||^2 and the normalization is again used only when
nonzero. The distance to the subspace itself is sqrt(delta_c); the bound
to the normalized comparison vector is at most sqrt(2delta_c). The pure
density trace distance is exactly sqrt(delta_c). Thus occupation probability
is O(c), while the general vector/state norm estimates are O(sqrt(c)).

The square-root order cannot in general be replaced by O(c), even on even
observables. Choose two orthonormal fixed compact-current-support high
packets and their normalized two-particle vector phi. For small c it lies
in F_c, and h_c=<phi,H_c phi>=4v/c+O(c). For fixed M>0 set
eta_c=M/h_c and psi_c=sqrt(1-eta_c)Omega+sqrt(eta_c)phi, once eta_c<1.
Its actual energy expectation is M. Its no-high comparison state is the
vacuum, and its trace distance to that state is sqrt(eta_c)=Theta(sqrt(c)).
The even two-mode observable a*(u)a*(v) plus its adjoint, of norm one,
has expectation of magnitude 2sqrt(eta_c(1-eta_c)), up to an irrelevant
choice of phase of phi. This is an actual even-observable coherence
witness, not an odd-parity interference loophole.

## 4. Exact limits of the conclusion

There need not be a limiting low state. Along any sufficiently fine sequence,
alternate the vacuum and a fixed normalized compact-current-support
two-low-particle state. They have uniformly bounded actual energies because
e_c,0 converges uniformly on that compact support, are orthogonal, and
their density operators have trace distance one. Both already have delta=0.
Consequently F3-F7 do not imply vector or trace-norm convergence, uniqueness,
or a selected continuum vacuum. They assert distance to a fixed closed
sector tends to zero while the comparison state may vary inside it.

If rho_c does converge in trace norm to a density rho, then Tr(rho Q)=0
by F3 and boundedness of Q. Positivity gives rho=P rho P. Likewise any
norm-convergent vector sequence satisfying F7 has its limit in P F. These
are conditional implications, not compactness claims. Weak or weak-star
limits and their normality require separate hypotheses.

No uniform observable C*-norm reduction follows. For a fixed normalized
compact-current-support high packet u, the even number projection
n_u=a*(u)a(u) lies in every sufficiently fine band algebra and has norm
one, while P n_u P=0. Its full operator/C*-norm remains one. Its expectation
in the bounded-energy states is at most delta_c, since n_u<=Q. Thus even
uniform suppression of expectations over the energy-bounded state class
does not make the observable vanish in the unrestricted C*-norm. The full
doubled coefficient/equal-time algebra and the actual-time counterexample
of the current note remain intact.

The mathematical input selecting this approximation class is the imposed
uniform *actual positive-energy expectation bound*. It is not derived from
the framework axioms, the realized-state evaluation primitive, or the
current-preserving refinement alone. The model, chosen quasifree state,
normal representation and positive Hamiltonian remain the pinned supplied
premises. Subtracting the diverging high energy, replacing the Hamiltonian,
or admitting energies growing like 1/c changes the hypothesis: fixed high
packets then furnish the expected counterexample to F3 tending to zero.

This short lemma is conditional support. No interaction, higher-dimensional
claim, general physical selection rule, independent review result or audit
verdict follows. The next check is the positive-form inequality and the
normalized compression/trace-distance proof against these exact sources.

## 5. Post-freeze correlation counterexample and exposure record

The analytic core above was frozen at 15:51:33 UTC, SHA-256
`50587a7c76b476c5e358873e1ab957923f6b27e7553bfcffec8e50c1c106142f`,
and remains unchanged in the evidence directory's frozen/ copy. Root then
read that core and authorized comparison to the complete root reconstruction,
SHA-256 `25e48e92474605ef3c67c6a9c90334bb192bd3a2f385951fca5c76578c783bf1`.
That post-freeze coauthor comparison agrees on the form, probability, trace
distance and vector bounds. It is not an independent review certificate.

Root also supplied the following important proposed scope counterexample;
its calculation is checked here. Bounded energy of the *initial state* does
not eliminate high dynamical correlations. Take the exact vacuum Omega,
which has actual energy zero at every spacing. Choose the fixed two compact
high packets u,v from section 3, with disjoint current supports, and the
even norm-one pair creator B=a*(u)a*(v). For all sufficiently small c this
is in the common embedded band algebra. Actual positive Fock evolution gives

    <Omega, B* alpha_c(t)(B) Omega>
      =<u wedge v, exp(itH_c)(u wedge v)>
      =exp(i4vt/c)+o(1)                               (F8)

for every fixed t. The error tends to zero because each high packet energy
is 2v/c+O(c) uniformly on its fixed compact support; unitarity and the
two-factor telescoping bound control the matrix element. At every fixed
t!=0 the two all-scale spacing sequences in Current C18 give different
limits. On c_n=c_0 2^-n, t=pi c_0/(6v) gives the same alternating cube-root
phases used there. These are even-observable vacuum correlations, despite
the initial state's energy being identically zero.

There is no conflict with F5-F6: for the vacuum rho_c=sigma_c already, and
F6 compares two states on the *same* bounded operator at a given c. It does
not control the spacing-dependent operator B*alpha_c(t)(B), nor make
compression multiplicative for operations leaving the sector. Here B Omega
has energy 4v/c+O(c), so the intermediate prepared excitation does not meet
the uniform bound. Extending the state concentration result to a restricted
family of measurements, interventions or dynamical correlators therefore
requires explicit additional control of their energy transfer and of the
remaining low-sector limits. No such additional physical rule or convergence
theorem is proved in this packet.


## Publication dependencies, interpretation and open obligations

The [current-preserving construction](CURRENT_PRESERVING_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md)
supplies the common chosen-state branch embedding and actual branch energies.
It landed as `open_gate`, with conditional support and N1/N5 obligations pending;
this note does not promote that parent. The [concrete-chain construction](CONCRETE_GAPPED_CHAIN_BOUNDED_THEOREM_NOTE_2026-10-12.md)
supplies the actual positive full-spin GNS Hamiltonian. The [local-even convention](LOCAL_EVEN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-10-12.md)
supplies the polarization, Fourier and even-CAR normalization. These are the three
direct scientific dependencies. Exact main-source hashes and the complete landing
diffs are preserved; the mathematical parent bodies were unchanged by those diffs.

The final review makes one scope distinction explicit: F6 also applies to bounded
spacing-dependent operators at the same spacing. It compares two states there;
it gives no comparison across spacings and therefore no correlation limit. The
zero-energy vacuum in F8 supplies the explicit dynamical counterexample. No
unique low-state convergence, unrestricted C*-norm collapse, compactness theorem,
continuum-correlation theorem or physical state-selection rule is inferred.

The author body and original core/appendix remain byte-exact. The complete author
manifest, focused review, root reconstruction/seal/coverage and main-parent refresh
are preserved in a deduplicated source archive with every original path retained.
Content deduplication adds no review independence. The packaging identity tool is
not a mathematical runner, Lean certificate or audit verdict.

The positive concentration theorem remains proposed conditional support. Its
counterexamples mark a partial narrowing; formal N1/N5 negative-packet readiness
remains pending, with no fabricated route families, controls or packet PASS.
A regular review PR, source/cache checks, combined current-main landing validation,
strict audit lint and formal retained audit are distinct steps. No editable prompt,
physical axiom or audit verdict is changed by this publication proposal.
