---
title: "Fixed finite-chain energy histories with controlled coarse readout"
claim_id: finite_chain_energy_history_bounded_theorem_note_2026-10-14
status: conditional-support
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
artifact_role: theorem
assembly_status: publication_prepared_root_integration_acceptance_pending
canonical_parent_binding_complete: true
scientific_execution: none_in_publication_source_preparation
runner: scripts/finite_chain_energy_history_identity_2026_10_14.py
trace_class: upstream_support
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
reachability_to_target: supports
conditional_surface_status: supplied gapped spin model; fixed finite carrier and finite coarse history; matched controls, preparation access and explicit effective spectral/gate data
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: conditional finite-chain history and readout compilation theorem with explicit premises and preserved source-exposed analytic checks
next_trace_action: separate root review of exact publication package and driver before canonical execution
audit_required_before_effective_retained: true
bare_retained_allowed: false
upstream_dependencies:
  - concrete_gapped_chain_bounded_theorem_note_2026-10-12
  - local_even_continuum_bounded_theorem_note_2026-10-12
  - energy_adapted_refinement_bounded_theorem_note_2026-10-12
  - calibrated_energy_transfer_bounded_theorem_note_2026-10-13
  - multitime_kinetic_energy_bounded_theorem_note_2026-10-13
---

Claim type: bounded_theorem

For a fixed finite energy-measurement history on a fixed finite coordinate/particle input carrier, the supplied gapped spin model admits one finite open chain whose complete weighted output approximates the infinite-chain target to any prescribed positive tolerance. With the stated spectral data and gate access, finite coarse readout circuits preserve within-bin coherence and fit a separate compilation budget. The output includes every unnormalized postmeasurement block and arbitrary passive references. The model, state preparation, matched drives and gate resources remain supplied premises.

# Fixed finite-chain energy histories with controlled coarse readout

**Current status: conditional source accepted for publication preparation; separate canonical integration review remains pending.** The supplied finite-chain, apparatus, finite-particle single-readout and matched-drive cores have the exact root acceptances recorded below. The complete weighted history, its finite R/C/D binding, and the readout-compiled fixed-history application have exact conditional root acceptances. This assembly creates no retained status, audit verdict, native physical realization or empirical prediction.

The complete mathematical text of the nine proof bodies is preserved byte for byte. The only body rendering changes turn two historical absolute checkpoint links in H into inline-code aliases; their exact original and rendered text and complete diff are recorded in PUBLICATION_EDITS.json. Every full original body remains unchanged in the compressed archive. Their old status sentences, unresolved obligations and discovered false wording are historical records. The current scope comes from this wrapper together with the named corrections and exact later acceptance records. Source identity and extraction checks do not establish a mathematical theorem.

Publication context supplied by root: **PR9527, head `ce0919d81e1660ee8c93e53af5cba8c1e4b293e4`**. This integration parent is distinct from the scientific dependencies listed below; branch ancestry does not supply a mathematical premise. Publication preparation checked the five complete canonical body identities against this exact parent and the live checkout. The root ref-refresh receipt independently records the regular parent and unchanged main/instruction refs; neither source identity nor PR ancestry proves a mathematical premise.

## Model, preparation and comparison topology

Fix the supplied one-dimensional massive chain with `g>J>0`, open intervals `Lambda=[l,r]`, interior fields `g` and endpoint fields independently in `[g/2,g]`. Its actual finite energy is

    K_Lambda=Hspin_Lambda-E0_Lambda,
    Hspin_Lambda=-sum_x d_x Z_x-J sum_x X_x X_(x+1),
    E0_Lambda=-Tr|T_Lambda|,  T_Lambda=diag(d_x)-J S_Lambda.

The supplied finite even diagonalization and isometry `W_Lambda` identify this energy exactly with `dGamma(2|T_Lambda|)` on the finite-mode Fock range. They do not identify it with the target infinite energy at finite volume. The target is the existing positive-Fock free Hamiltonian `H=dGamma(2|gI-JS|)`, on the full Fock space, including odd sectors. The exterior `2g` modes in the common-carrier extension are bookkeeping and are not physically populated.

Use the common number weight `A=1+N`. For fixed `s>=0`, compare complete system/classical-record/passive-reference outputs in `||A^s X A^s||_1`. Weights act trivially on references and records. The sector bounds `cN<=H,Hhat_Lambda<=CN`, with `c=(g-J)/2` and `C=2(g+J)`, supply graph-domain equivalence. In particular `||(1+H)^s A^-s||<=max(1,C)^s` converts this to a common-target-energy weighted estimate. It does not assume that compiled readout gates conserve energy or particle number, or identify different own-energy weights.

An actual finite preparation must lie in `ran Gamma(Pi_Lambda)` before pulling it back by `W_Lambda*`; apparatus C1 makes this explicit. The supplied finite ground state and matched finite local-control preparations meet that condition. For quantitative finite-input statements, start with a fixed carrier `Q0=direct sum_(n<=n_*) wedge^n ell²(S0)` on a fixed finite site set, or an explicitly controlled approximation to such a carrier. Arbitrary subspaces of `Q0` are permitted for supported states, but their projections cannot silently be moved through `A^s`. Native preparation of every abstract carrier vector is not supplied.

Keep one endpoint convention at every volume and stage. The apparatus uses left-closed/right-open bins `[b_j,b_(j+1))`, with a finite positive boundary list and a final unbounded bin. The volume proof explicitly permits the corresponding strict cumulative projectors. Exact finite eigenvalues at boundaries are allowed. Retain the full coarse Lüders output, including within-bin coherence, unnormalized postmeasurement blocks, previous labels and every passive reference. The metric does not uniformly control normalized states on arbitrarily rare branches. A fine-energy archive followed by binning is a different instrument.

## Component statements and exact current status

| Component | Current scope | Disposition and controlling record |
|---|---|---|
| A: finite open chain, `13fd167e…` | Exact ground shift, finite positive-Fock/PVM representation, compatible even controls and weighted qualitative fixed-history comparison under matched input hypotheses | Supplied accepted core in root dispatch; complete exposed finite-chain review `6eeb9c54…` and supervisor disposition `b9b58be6…`; physical-range C1 is mandatory |
| B/C: phase-register instrument and finite local compiler, `6d534a7c…` / `aa834948…` | Coherent compute/copy-coarse/uncompute, fibre error identity, weighted full-output bound and conditional local product compilation | Relied apparatus predecessors, read with endpoint addendum D and later apparatus acceptance; no independent model-family or native apparatus claim |
| D: endpoint precision, `ba189d96…` | Correct union-of-strips membership, effective margin, fixed-input versus moving-family quantifiers | Full precision addendum and its exact controls preserved; overrides the identified older unrestricted endpoint sentences |
| E: finite-chain apparatus C1–C11, `9179660b…` | Explicit readout accuracy after a volume is selected, actual finite energy including controlled ground phase, all finite gate errors and weighted suffix factors | `archive/crash_recovery_01a13807/finite_apparatus_composition/ROOT_ACCEPTANCE.json`; original v1, v2, both complete correction diffs and reviews preserved |
| F: finite-particle single-readout volume modulus, `8fc3f325…` | Explicit input-strip bound and conservative `O(d^(-1/6))` full-instrument bound on fixed finite mode/particle carriers, reference stable | Separate source-exposed review `dfb86b77…` and `archive/continuation_20261014_023239/FINITE_PARTICLE_VOLUME_ACCEPTANCE.json`; not a kinetic-uniform result |
| G: matched physical drive D1–D9, `98f1033c…` | Actual matched finite/infinite even local-spin drive comparison on the number-invariant carrier `Q0`; explicit sufficient clearance and finite physical output carrier | Separate review `95abd8c2…` and `archive/continuation_20261014_023239/MATCHED_DRIVE_ACCEPTANCE.json`; one-sentence repair preserved |
| H: common-final-volume quantitative history, `c4310617…` | Complete weighted recursion; finite R/C/D binding gives a computable common physical volume for the stated fixed finite protocol | Separate review `55e79455…` and `archive/continuation_20261014_023239/HISTORY_COMPOSITION_ACCEPTANCE.json`; original status-only v1, complete delta, scalar source and streams preserved |
| I: readout-compiled fixed-history application, `7fe0df39…` | One common finite chain followed by finite readout compilation, with total complete weighted output error `E_vol+E_comp` under the stated data/access premises | Separate application review `d7e9671e…`, exact repair review `e86f1c19…` and `archive/continuation_20261014_023239/FIXED_HISTORY_APPLICATION_ACCEPTANCE.json`; original, current and full precision diff preserved |

Exact full hashes and original/archive paths are in ARCHIVE_MANIFEST.json and EXTRACTION_MANIFEST.json. Root acceptance is conditional source acceptance; formal retained status remains separate. The provisional auxiliary `driven_reachability` proof at `5911cc4c…` is an optional alternative disclosed in the matched-drive exposure record, not the publication core or a premise of G.

## What the quantitative ingredients provide

For one sharp readout on the stated carrier, F transfers the target input boundary-strip masses to finite-volume strip masses by spectral smoothing and localized functional calculus. Its finite-support Fourier estimate then gives the explicit `d^(-1/6)` envelope. The boundary buffer is consequential: half endpoint fields change an adjacent offdiagonal entry of `T* T`; polynomial equality holds only through degree `d-1` with the declared endpoint clearance. The separate exact path control rejects the next degree. No global energy-operator norm convergence is asserted, and escaping boundary modes remain in the archive.

For a fixed driven segment, G bounds the graph-operator difference by

    epsilon_drive(d)=exp(B_s)[P(d,T)D_s+Efree(d,T,n_*)],

and the weighted state error by `2 exp(B_s) epsilon_drive(d) M(rho)`. The endpoint-dependent factorization puts the free factor on the input side, so the restricted free estimate is applied to `Q0`, not to an unproved compact post-drive support. The actual finite output lies in its full finite Fock range; this is an approximating carrier for the infinite output. The repaired sentence is “need not have exact” finite support, preserving the zero-drive vacuum exception. Effective model/coefficient/budget data make its sufficient clearance computable. Arbitrary measurable L1 waveforms still need an executable schedule or effective L1 approximation data to compute or synthesize the drive.

The accepted history H keeps positive, possibly subnormalized auxiliary states on finite physical-coordinate carriers. At a readout, F supplies its complete relative weighted error by applying the number-intertwining instrument to `A^s sigma A^s`. At a drive, G supplies both the actual finite-chain comparison and a finite output carrier: choose an auxiliary finite interval, whose full finite Fock range contains the actual output. Number-commuting projections certify a small tail of the infinite output. The auxiliary states are never normalized or used as physical resets.

For `r` fixed operations, let `a_j` and `q_j` bound actual and target weighted amplification, `D_j=max(1,a_j,q_j)`, and `K_r=product D_j`. With initial weighted error `e0`, initial mass bound `M0`, comparison allowances `epsilon_j` and intermediate surrogate allowances `tau_i`, H proves

    e_r <= K_r e0 + M0 K_r [sum_j epsilon_j/D_j
                          +2 sum_(i<r)(r-i)tau_i/D_i].

The explicit allocations in H then choose finitely many auxiliary carriers and comparison clearances. Their interval hull gives one physical interval; every larger admissible interval, with allowed endpoint fields, meets the same certified error bound. Every physical operation uses that single final interval. Only proof witnesses use intermediate intervals. The statement is uniform over the fixed input carrier and moment bound, including arbitrary passive references and earlier records; it is not uniform over the entire infinite-volume finite-energy ball. Exact matched preparation sets `e0=0`; varying approximate preparation requires its own effective eventual comparison.

The accepted application I then compiles the readouts on that selected common chain while retaining the supplied exact matched drives. For `m>0` readouts, put `Ddrive=product_drives exp(2B_(s,j))`. Total graph-isometry tolerances

    0<zeta_j<=min(1,E_comp/(3m M0 Ddrive 4^m))

suffice. Each readout has weighted channel defect at most `(2+zeta_j)zeta_j` and moment amplification at most `(1+zeta_j)^2`. The telescope uses ideal earlier operations and compiled later operations, charging every future readout factor and the single product `Ddrive`. Its total defect is at most `E_comp`; for `m=0` that defect is zero. Adding the finite-volume history error yields `E_vol+E_comp` in the same complete weighted output norm. The total `zeta_j` is distinct from the apparatus internal product allowance `zeta_L`: use `a_L=zeta_L=zeta_j/3` and `gamma_L<=zeta_j/(3Wcost_L)`.

For this computable volume prescription, retain adequate effective model bounds and a certified positive gap; effective bin-boundary data and positive position/separation margins sufficient to verify `delta_d<=min_j(b_j/C)/6`; a computable graph exponent; and certified finite support, coefficient, duration and control-budget data. Algebraic model/bin data with order tests suffice. A certificate-based alternative must supply these volume-bound data separately from the finite spectral-separation and threshold data needed by the circuit compiler. Those scalar certificates choose a sufficient volume and tolerances; evaluating or synthesizing general driven outputs still requires effective waveforms.

## Finite apparatus prescription and mandatory corrections

At each selected finite volume, E chooses a positive certified separation from every spectral energy strictly below each bin boundary. Exact equality belongs to the target bin's closed side. The classifier thresholds move; the target bins do not. With threshold uncertainty `kappa`, the effective phase margin is `r=delta-kappa`; the sufficient resolution condition uses `M r/(4R)`, not the nominal `M delta/(4R)` alone.

For several boundaries, an atom can lie in a higher boundary's bad strip. All internal boundary atoms are outside the union of open strips exactly when `2delta<=d_min`; equality is allowed. The original error bound already charges such strip mass, and the fixed-input limit survives. D preserves the close-boundary counterexample, the fixed-state lost-margin witness, and the moving-family witness. None is promoted to a universal negative theorem or a no-go gate PASS.

The finite compiler keeps the controlled scalar ground-energy phase, signed controlled local terms, specified clean auxiliary registers, bus routing, ancillary precision, clock and drift/drive management, coarse dephasing and declared traces as supplied resources. It uses fresh fine registers at interventions; approximate clearing does not give a free exact reset. The weighted apparatus error is

    eps_L=a_L+zeta_L+Wcost_L gamma_L,
    ||A^s(Phi_L-Lambda_L)(rho)A^s||_1
        <=(2+eps_L)eps_L Tr(A^(2s)rho).

The same certified `Wcost_L>=(1+L)^s` is used in every error budget, including `gamma_L<=u_L/(3Wcost_L)`. For certified rational upper bounds `U_j>=x_j`, the executable substeps are `n_j=max(1,ceil(U_j))`, with `sum n_j<=q+sum U_j`. The smaller exact-ceiling count is restricted to the exact C7 prescription. These v2→v3 repairs are part of the current scope, with the earlier erroneous alternative retained only as history.

A finite-resource existence statement for specified real data is distinct from a computable recipe. E's sufficient algorithmic data are algebraic spectral/model/boundary data with order tests, or a supplied certified finite separation/label table; rational tolerances; and a computable graph exponent or supplied integer upper bound. Logical gate counts exclude an autonomous clock, complete geometry-dependent routing, pulse duration, heat and reset work. No efficiency or total physical energy ledger follows.

## Direct scientific dependencies and provenance

The actual relied canonical bodies are archived in full at their scientific source identities. They are not inferred from PR ancestry:

<!-- BEGIN CANONICAL PARENT BINDING -->
| Canonical source | Relied scope | SHA-256 |
|---|---|---|
| [Supplied gapped spin chain and full-spin Fock representation](CONCRETE_GAPPED_CHAIN_BOUNDED_THEOREM_NOTE_2026-10-12.md) | Supplied gapped chain, compatible even JW and actual full-spin positive-energy representation | `2311c445bffc809d3387089c0feb48892f15f535d889121664dabe49fa146b05` |
| [Field normalization and positive polarization](LOCAL_EVEN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-10-12.md) | Field normalization/signs, positive polarization, finite even words | `b5a8394a9d8c17bb9559597a68b061ad3872201ebf9793bd5c9f10b15ac2c6aa` |
| [Exact energy-adapted infinite-chain embedding](ENERGY_ADAPTED_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md) | Existing exact infinite-chain common-energy/Fock embedding | `e8b34ef49f7e3d5c289584b8f662da40a05912794bcf1b4cb8e05e6c903bbc88` |
| [Actual Fock-domain and spectral-measure interface](CALIBRATED_ENERGY_TRANSFER_BOUNDED_THEOREM_NOTE_2026-10-13.md) | Actual Fock-domain/PVM and supplied-input interface used by A/F | `2cc7bfa7f5c6406391c52b2f6610b31ba309730edf2f324c4847d4cb98004f8b` |
| [Specified finite coarse energy-measurement protocol](MULTITIME_KINETIC_ENERGY_BOUNDED_THEOREM_NOTE_2026-10-13.md) | Upstream specified coarse-instrument/common-energy protocol conventions used by B; no kinetic-limit proof imported by this assembly | `afd18eda5af99d9e18d366ea88856d6331bef69aa3c18740083a8c32101915ed` |

<!-- END CANONICAL PARENT BINDING -->

The first four bodies were pinned by A at `ccbeddd0c04b70ee2b6c5f1cffeeeefa23df2989`. B originally pinned the fifth at `e8d5b7b99c9faab65f71eb5ff353b60e2b609608` and recorded byte identity on refreshing to ccbeddd0. The package preserves those exact snapshots and exposure receipts. Their complete live and parent bodies match these identities during publication preparation; root must recheck them before integration. The existing infinite energy-adapted embedding is retained as prior work and is not described as absent.

B and C are separate contributing proofs: C was sealed before B findings were read and is self-contained. E relies on both. The full new proof bodies and relevant reviews were read as recorded in READ_COVERAGE.json. Prior accepted readings were reused only at unchanged hashes. The archive preserves analytical counterexamples, disjoint finite controls, complete retained streams and reported execution failures; none was rerun for this assembly. Earlier numerical success is neither a proof of all volumes nor an independent audit. The source checker imports or executes none of those scientific scripts.

## Readiness limits

This package does not derive the supplied model, ground-state selection, controls, input preparation, Born probabilities, durable records, native readout, autonomous timing, three-dimensional placement, interacting channels or empirical rates. It gives no uniform result as the gap closes, observation count grows, bins move, or kinetic time scales jointly. Fixed-input, effective-data and any all-larger-volume quantifiers must remain attached to the exact statement that proves them.

No Git, PR, canonical driver, repository surface, audit, axiom or editable prompt was changed. All checking here is deterministic source bookkeeping with **zero mathematical predicates**. Root owns final mathematical acceptance, canonical integration and publication decisions. The final source freeze records the exact assembled candidate and accepted inputs; it adds no mathematical acceptance.

Review-loop integration: current canonical parent hashes above reflect previously reviewed publication-wrapper repairs on main a3ccb945b1543e31361f1c6fefd2cc7ab7d31d5f. Original complete parent snapshots and mappings remain archived. Mathematical bodies are unchanged; historical acceptance and pending labels are provenance, not audit authority.



<!-- BEGIN SOURCE A sha256=13fd167efa195fd672fa37e5f3562059bdd76ad373686ef88cde65a02cdfcb10 -->

## Source A: Finite open chain

Original: `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261013_213733/finite_open_chain_independent/CANDIDATE.md`. Complete immutable body follows.

---
title: Finite open-chain ground preparations and coarse free-energy histories
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
trace_class: upstream_support
reachability_to_target: supports
conditional_surface_status: supplied massive transverse Ising chain, specified open boundaries, matched even controls, coarse energy bins and stated input/preparation class
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: original conditional finite-volume proof candidate with finite independent implementation checks; root comparison and independent review remain separate
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# Finite open-chain ground preparations and coarse free-energy histories

This is an independent candidate derivation after a neutral plan was sealed.
No root finite-volume formulas or active coarse-instrument derivation was read.
The existing infinite-chain energy-adapted embedding is prior art. The result
below concerns the additional finite-open-volume bridge. It uses changed,
state-adapted Hilbert embeddings, not convergence of finite ground vectors
under an identity-on-CAR embedding into a preselected product vacuum.

## 1. Exact contract and parent bindings

Fix g>J>0. Let Lambda=[l,r] run through finite intervals with l tending to
minus infinity and r tending to plus infinity. Its number of sites is L.
For L>=2, define the actual finite spin Hamiltonian

    Hspin_Lambda = -sum_(x in Lambda) d_x Z_x
                  -J sum_(x,x+1 in Lambda) X_x X_(x+1).       (F1)

Every interior d_x is g. Either endpoint may be any supplied value in
[g/2,g], independently and even varying with Lambda. This includes both:

- the usual open Ising Hamiltonian, all d_x=g;
- the literal sum of the parent's bond densities
  h_x=-J X_x X_(x+1)-(g/2)(Z_x+Z_(x+1)), whose two endpoint fields are g/2.

Those Hamiltonians are not identified at finite volume. The literal empty
bond sum on one site has no simple ground state and is not included; any
exhaustion eventually has L>=2. No periodic wrap or boundary parity twist
is added. The infinite model always has bulk field g and the parent state.

The actual finite energy to be read is

    K_Lambda = Hspin_Lambda - E0_Lambda I,
    E0_Lambda = min spec(Hspin_Lambda).                       (F2)

The scalar shift is derived below, not dropped. Its finite chosen ground
state is the unique ground state constructed below. The target is the
parent's full spin-GNS free energy H=dGamma(E), with
E(k)=2 sqrt(g^2+J^2-2gJ cos k). It is full Fock energy; no even-only Hilbert
space or doubled even-sector gap is substituted.

The source revision is ccbeddd0c04b70ee2b6c5f1cffeeeefa23df2989. Exact parents:

| Parent | SHA-256 | Relied-on scope |
|---|---|---|
| CONCRETE_GAPPED_CHAIN_BOUNDED_THEOREM_NOTE_2026-10-12.md | 2311c445bffc809d3387089c0feb48892f15f535d889121664dabe49fa146b05 | Contract and complete sections 5-6: compatible even JW, actual full-spin GNS construction, positive free Hamiltonian |
| LOCAL_EVEN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-10-12.md | b5a8394a9d8c17bb9559597a68b061ad3872201ebf9793bd5c9f10b15ac2c6aa | Complete unchanged prior read: coefficient signs, normalization, positive-polarization Fock carrier, finite even spin words |
| ENERGY_ADAPTED_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md | e8b34ef49f7e3d5c289584b8f662da40a05912794bcf1b4cb8e05e6c903bbc88 | Complete unchanged prior read: existing exact infinite lattice/continuum state and energy embedding |
| CALIBRATED_ENERGY_TRANSFER_BOUNDED_THEOREM_NOTE_2026-10-13.md | 1f71af03465e71a57bcbe0f7713759ab51ff36df02736bf8be5d9e798d9f725e | Complete graph core 1 and actual-input interface core 4, especially 1262-1300: Fock domains/PVMs and supplied initialization |

These are conditional mathematical inputs, not new physical axioms. The
minimal axiom memo and approved primitive registry do not select this model,
ground state, energy readout or preparation controls. Here all are explicit
supplied mathematical conditions. No retained-status conclusion is made.

For each fixed protocol use finitely many bounded selfadjoint even local
spin polynomials, supported in one fixed finite set, and the same real
measurable L1 controls on finitely many finite time intervals. Their support
may depend on another already fixed parameter, such as lattice spacing, but
is fixed during this volume limit. Between these driven segments one may
read a fixed finite or countable partition of R_+ into intervals. Endpoints
are fixed positive real numbers; the vacuum point 0 is assigned consistently
and may also be a singleton bin. A final unbounded tail bin is permitted.
All outcomes and unnormalized postmeasurement states are retained.

## 2. Finite diagonalization without a vacuum implementability assumption

Use the finite open-chain Jordan-Wigner Majoranas a_x,b_x with left endpoint
l. Then Z_x=-i a_x b_x and X_x X_(x+1)=-i b_x a_(x+1). Thus

    Hspin_Lambda = i sum_(x,y in Lambda) a_x T_(Lambda;x,y) b_y,
    T_Lambda = diag(d_x)-J S_Lambda,                         (F3)

where (S_Lambda f)_x=f_(x-1), with zero outside the interval. Order the
coefficient pair as all a components followed by all b components. The
Hermitian signed coefficient matrix is

    D_Lambda = [ 0, 2i T_Lambda; -2i T_Lambda^*, 0 ].         (F4)

This agrees with the parent's coefficient clock exp(+itD), not its field
column clock. Transpose and adjoint agree on the real matrices here.

T_Lambda is real invertible and has positive determinant product_x d_x.
Write its real polar decomposition T_Lambda=V_Lambda |T_Lambda|. Then
V_Lambda is orthogonal with determinant +1. Set

    O_Lambda=diag(V_Lambda^*, I),
    e_Lambda=2|T_Lambda|,
    C0=[0,iI;-iI,0].

Direct multiplication gives

    O_Lambda D_Lambda O_Lambda^* = e_Lambda C0.             (F5)

The factors on the right commute. O_Lambda is a real coefficient isometry
in SO(2L), so finite Majorana plane rotations implement it by an even
unitary C_Lambda on the full 2^L-dimensional spin/Fock Hilbert space. This
uses only finite Clifford matrices; no infinite-volume implementation is
assumed.

In the usual Fock realization gamma_0(f_1,f_2)=a^*(f_1+i f_2)+a(f_1+i f_2),
C_Lambda sends the actual field gamma(f) to gamma_0(O_Lambda f). Since
|T_Lambda| is real symmetric, the creation-creation and annihilation-
annihilation terms cancel in i a^t |T_Lambda| b. Therefore

    C_Lambda Hspin_Lambda C_Lambda^*
       = dGamma(e_Lambda)-Tr|T_Lambda| I.                  (F6)

This proves, rather than assumes,

    E0_Lambda=-Tr|T_Lambda|,
    C_Lambda K_Lambda C_Lambda^*=dGamma(e_Lambda),
    phi_Lambda=C_Lambda^* Omega.                           (F7)

The ground state is simple because e_Lambda>0. Its parity is even because
C_Lambda is even and the product vacuum has even parity. The comparison
uses the full finite spin space, including odd excitation sectors.

A volume-independent lower bound also covers the literal density cutoff.
For x>=y, the lower-triangular inverse has entries

    (T_Lambda^-1)_(x,y)=J^(x-y)/(d_y d_(y+1)...d_x),

and is zero for x<y. At most two d's differ from g, and each g/d<=2. Hence

    |(T_Lambda^-1)_(x,y)| <= (4/g)(J/g)^(x-y),
    ||T_Lambda^-1|| <= 4/(g-J),
    (g-J)/2 <= e_Lambda <= 2(g+J).                        (F8)

The norm estimate follows from the row and column sums and the elementary
Schur bound. For full onsite fields the sharper lower bound is 2(g-J),
from ||(gI-JS_Lambda)f||>=(g-J)||f||. F8 is sufficient for both choices.

## 3. A common positive-Fock carrier with distinct actual energies

Let h=ell^2(Z), Pi_Lambda its coordinate projection and i_Lambda the finite
inclusion. Put

    T=gI-JS on h,
    That_Lambda=i_Lambda T_Lambda i_Lambda^*+g(1-Pi_Lambda),
    e=2|T|,
    ehat_Lambda=2|That_Lambda|
                =i_Lambda e_Lambda i_Lambda^*+2g(1-Pi_Lambda). (F9)

The outside 2g modes are comparison bookkeeping only. They are never added
to the physical finite chain or populated in its embedded states.

Both That_Lambda and its adjoint agree with T and T^* eventually on each
finitely supported test vector. They are uniformly bounded, and F8 gives
uniformly bounded inverses. Thus That_Lambda and their adjoints converge
strongly. Products converge strongly under uniform bounds. Polynomial
approximation on one fixed compact positive spectral interval then gives

    ehat_Lambda -> e strongly,
    Vhat_Lambda=That_Lambda |That_Lambda|^-1 -> V=T|T|^-1
       strongly together with adjoints,
    Ohat_Lambda=diag(Vhat_Lambda^*,I) -> O=diag(V^*,I)
       strongly together with adjoints.                    (F10)

The inverse-square-root argument uses the positive lower bound in F8.
It is not asserted at g=J, or uniformly as g-J tends to zero.

On F=F_-(h), let N be particle number, A=1+N, and define

    Hhat_Lambda=dGamma(ehat_Lambda),  H=dGamma(e).

For c=(g-J)/2 and C=2(g+J),

    cN <= Hhat_Lambda,H <= CN.                             (F11)

Consequently Dom((1+Hhat_Lambda)^s)=Dom(A^s)=Dom((1+H)^s)
for every fixed real s>=0, with equivalence constants independent of Lambda.
This follows sector by sector: on the n-particle sector the energy lies
between cn and Cn. No noncommuting power-order inequality is needed.

Let P_Lambda^F=Gamma(Pi_Lambda), the finite-mode Fock projection, and

    W_Lambda=Gamma(i_Lambda) C_Lambda.

It is an isometry from the actual finite spin Hilbert space into F, with
range P_Lambda^F F, and

    W_Lambda phi_Lambda=Omega,
    Hhat_Lambda W_Lambda=W_Lambda K_Lambda,
    1_B(Hhat_Lambda)W_Lambda=W_Lambda 1_B(K_Lambda)           (F12)

for every Borel B. Its range reduces Hhat_Lambda. These statements are
exact at each volume. They do not say H W_Lambda=W_Lambda K_Lambda.
The two energies are distinct before taking the volume limit.

For an actual even spin polynomial supported inside Lambda, use its compatible
even JW expression and replace each real coefficient f by Ohat_Lambda f.
The resulting operator V_Lambda in F acts with identity on outside modes,
preserves P_Lambda^F F, and agrees there with W_Lambda Vspin W_Lambda^*.
It is a unital CAR representative, not a zero-complement compression.
The target is the same expression with O f. F10 and field norm continuity
give norm convergence V_Lambda -> V for every fixed local polynomial.
Odd bilateral spin observables are not identified by this construction.

The target is precisely the parent's positive representation up to a fixed
one-particle unitary. More explicitly, nu z=(z,-iz)/sqrt(2) maps h onto the
positive C0 eigenspace. j=O^* nu maps h unitarily onto the positive spectral
subspace of the actual D and obeys D j=j e. Also
sqrt(2) j^* f=(O f)_1+i(O f)_2. Thus Gamma(j) gives exactly the parent's
positive-polarization fields, covariance and H. This is an explicit changed
observable representation; it neither asks nor proves that O is implementable
in a previously fixed infinite product-vacuum representation.

## 4. Number-weighted controls and strong evolution limits

For s>=0, creation and annihilation change particle number by one. On their
particle-sector cores,

    ||A^s a^*(z) A^-s|| <= 2^s ||z||,
    ||A^s a(z) A^-s|| <= ||z||,
    ||A^s gamma_0(f) A^-s|| <= (2^s+1)||f||.               (F13)

The first bound is ((n+2)/(n+1))^s<=2^s; the second is
(n/(n+1))^s<=1. Summing orthogonal sectors and then using closedness proves
the domain preservation and bounded extensions. Products give a bound
(2^s+1)^d product||f_j|| for a word of degree d. Finite coefficient sums
give an explicit number M_s(V). The same estimate bounds a telescoped
word difference by its coefficient-vector differences. It applies to all
real s, without differentiating an unbounded commutator formally.

Each ehat_Lambda and e is bounded on h, uniformly in Lambda. F10 implies
exp(it ehat_Lambda)z -> exp(it e)z uniformly on each compact t interval,
by polynomial/exponential-series approximation and uniform operator bounds.
The free Fock groups converge strongly uniformly on compact t intervals:
prove this on each fixed particle sector using tensor products and finite
sums, then approximate an arbitrary Fock vector by finitely many sectors.
All these groups commute with A.

The interaction-picture fields for V_Lambda are therefore norm convergent,
uniformly on compact time intervals. F13 and its telescoped version show
that this remains operator-norm convergence after conjugation by A^s.
For a matched finite family and real locally L1 functions u_l(t), the
interaction-picture generators have integrable graph-norm envelopes
sum_l |u_l(t)| M_s(V_l). Dyson iteration on Dom(A^s), followed by Hilbert-
space uniqueness, gives the same unitary evolution and domain preservation.
For each segment,

    ||A^s U_Lambda(t,r) A^-s||,
    ||A^s U(t,r) A^-s||
       <= exp(integral_r^t sum_l |u_l(v)| M_s(V_l) dv)=C_s, (F14)

using the appropriate absolute integral for reversed times. More accurate
polynomial bounds may be available from the parents, but are not needed.
Dominated Dyson differences give graph-operator-norm convergence of the
interaction-picture propagators. Restoring the free groups gives

    A^s U_Lambda(t,r) A^-s -> A^s U(t,r) A^-s strongly,     (F15)

uniformly for endpoints in a fixed compact time set. This is strong, not
operator-norm, convergence of the full propagators. Finite actual states
remain in P_Lambda^F F under their actual controls.

## 5. Coarse spectral projections and the full instrument

On the n-particle sector Hhat_Lambda is a sum of n uniformly bounded
one-particle operators, so it converges strongly to H on that sector.
Continuous bounded functions converge strongly there by polynomial
approximation on a common spectral interval.

For n>=1, H has no point spectrum. In Fourier variables it is multiplication
by sum_(j=1)^n E(k_j). For any fixed k_2,...,k_n and any real lambda, the
level set E(k_1)=lambda-sum_(j>=2)E(k_j) has Lebesgue measure zero:
J>0 and g>J make E nonconstant, with only finitely many points at a level.
Fubini proves the sum level set has measure zero, also on the antisymmetric
subspace. The vacuum is the sole zero-energy vector. This is why the
strict J>0 premise and explicit treatment of the vacuum matter here.

Approximate each interval indicator from above and below by bounded
continuous functions, whose discrepancy is supported in small neighborhoods
of its endpoints. Target spectral measures give these neighborhoods vanishing
mass at every positive endpoint. The continuous-functional-calculus limit
then proves strong convergence of the interval projections. The vacuum
component is exact at every Lambda and uses the same bin assignment. A
finite-particle truncation and the projection norm bound extend the result
to full Fock space. Thus for every bin B_z in the stated partition,

    P_(Lambda,z)=1_(B_z)(Hhat_Lambda) -> P_z=1_(B_z)(H)
       strongly.                                          (F16)

A bin unbounded above follows by subtraction or the same finite-sector
argument. A singleton vacuum bin is exact. Finite-volume eigenvalues may
sit on a bin boundary; only target boundary mass enters this proof.

Define the isometries to a countable label space

    J_Lambda psi = sum_z |z> tensor P_(Lambda,z) psi,
    J psi        = sum_z |z> tensor P_z psi.                (F17)

They converge strongly even for countably many outcomes. Indeed their
norms on psi equal ||psi||. A finite set of target components captures its
norm to arbitrary accuracy; the remaining inner-product tail is bounded
by ||psi|| times the target tail norm, by Cauchy-Schwarz. F16 handles the
finite part, giving <J_Lambda psi,J psi> -> ||psi||^2.
All P_(Lambda,z),P_z commute with N. Therefore J_Lambda,J also commute
with A^s in the input/output sense and are exact weighted contractions.

The coarse Lueders instruments are

    M_Lambda(rho)=sum_z |z><z| tensor P_(Lambda,z) rho P_(Lambda,z),
    M(rho)       =sum_z |z><z| tensor P_z rho P_z.           (F18)

This is F17 followed by dephasing only the displayed outcome register.
No finer energy register was measured and discarded. Within-bin coherence
and the full unnormalized quantum output are retained.

For any passive reference R and any fixed normal joint density rho with
Tr[rho(A^(2s) tensor I_R)]<infinity, set X=(A^s tensor I_R)rho^(1/2),
a Hilbert-Schmidt operator. Uniform bounded strong convergence remains
strong after tensoring with I_R and implies
||(J_Lambda-J) tensor I_R X||_HS ->0 by finite-rank approximation.
The inequality

    ||XX^*-YY^*||_1 <= (||X||_HS+||Y||_HS)||X-Y||_HS        (F19)

therefore proves convergence of the full instruments in weighted trace
norm. Register dephasing is a trace-norm contraction and commutes with the
weight. The same argument handles varying rho_Lambda if

    ||(A^s tensor I_R)(rho_Lambda-rho)(A^s tensor I_R)||_1 ->0. (F20)

For its difference term, M_Lambda is exactly contractive in this norm.
This theorem concerns fixed coarse bins. No comparison of unbinned atomic
finite-volume laws with a continuum energy-density law is asserted.

## 6. Finite histories, passive references and the precise topology

Alternate finitely many driven segments F14 and readouts F18. Retain every
outcome string and the final unnormalized joint quantum state. A fixed
finite feedback tree is allowed; countable outcomes with a fixed finite
control family and uniform finite budgets are handled by the same finite-
component approximation. The reference is passive throughout.

Write rho_(Lambda,h) and rho_h for the final record blocks. For every s>=0
and inputs satisfying F20 and its finite-moment premise,

    sum_h ||(A^s tensor I_R)(rho_(Lambda,h)-rho_h)
                              (A^s tensor I_R)||_1 ->0.    (F21)

Proof: at a driven stage the weighted trace-norm amplification is at most
C_s^2 by F14. For a fixed target input, F15 and F19 prove weighted output
convergence. At a measurement stage F18 is weighted contractive and its
fixed-input error tends to zero by F17-F19. Insert and subtract the target
input at each stage. Induction over the fixed finite number of stages gives
F21. Old outcome registers simply enlarge the passive factor for a readout;
block-diagonal feedback controls satisfy the same uniform graph bounds.
The target state has the required moment at each stage by F14. No normalized
rare-history conditional state is compared.

The convergence is uniform on fixed compact time-parameter sets for a fixed
protocol: the strong convergences above are uniform on compact target-vector
orbits; finite-rank Hilbert-Schmidt approximation and finite record-tail
approximation retain that uniformity. L1 controls are fixed or have explicitly
matched convergent interaction-picture data; arbitrary volume-varying controls
are not silently included.

Two useful energy formulations follow without extra moments. Put
B=(1+H)^s A^-s and B_Lambda=(1+Hhat_Lambda)^s A^-s. They are uniformly bounded
by F11. On each particle sector their strong convergence follows from
continuous functional calculus; finite-sector approximation proves
B_Lambda -> B strongly on full Fock space, with adjoints. Consequently F21
implies both the common-H weighted comparison and the own-energy comparison

    sum_h || ((1+H)^s tensor I_R)(rho_(Lambda,h)-rho_h)
                                  ((1+H)^s tensor I_R) ||_1 ->0,

    sum_h || ((1+Hhat_Lambda)^s tensor I_R)rho_(Lambda,h)
                                      ((1+Hhat_Lambda)^s tensor I_R)
             -((1+H)^s tensor I_R)rho_h((1+H)^s tensor I_R) ||_1 ->0. (F22)

For the second, first use F21 and the uniform B_Lambda bound, then apply
strong bounded multiplication to the trace-class weighted target output.
For a countable record register this is one trace-class operator on its
direct-sum Hilbert space; no unjustified exchange of an infinite sum occurs.

The chosen ground preparations satisfy F20 exactly: W_Lambda phi_Lambda=Omega.
Tensoring with any fixed reference state preserves that fact. There is also
an explicitly complete, nontrivial reference-uniform version. Let a fixed
finite-dimensional input space Q feed a matched preparation isometry
S_Lambda:Q->F tensor Q' with

    ||(A^s tensor I) S_Lambda-(A^s tensor I)S|| ->0.         (F23)

Examples include vacuum preparation with a fixed finite auxiliary system
and finitely many matched even local control/preparation operations; allow
bounded matrix coefficients on that finite auxiliary system. F13-F15 apply
unchanged. For the vacuum initial map this convergence is immediate, and
for the finite preparation it follows on a finite basis of Q.

Purify each Lueders instrument by copying its label to an environment before
tracing it out. Composing these isometries and the controlled unitaries gives
history Stinespring maps Z_Lambda,Z on Q. Their weighted versions converge
strongly: after moving the weights through each measurement factor, every
factor is either F17 or the uniformly bounded graph operator F15. Products
of finitely many such factors converge strongly. For feedback, use the
direct sum over old records; approximation by finitely many components and
the uniform graph bound prove the same fact. Restriction to a finite basis
of Q makes this weighted convergence operator-norm convergence. The maps
have a uniform bound
C_prod, the product of the segment graph bounds and preparation bound. For
any reference R and any density sigma on Q tensor R,

    || weighted [Phi_Lambda tensor id_R - Phi tensor id_R](sigma) ||_1
      <= (||Z_Lambda,s||+||Z_s||)||Z_Lambda,s-Z_s|| ->0.      (F24)

F19 and operator-ideal inequalities prove this bound; tracing environments
and dephasing records are contractions. It is independent of the dimension
of R and the input sigma. This is a weighted diamond-type comparison from
the fixed finite input Q. It is not a uniform comparison on every state
in an infinite-volume energy ball. The general F21 statement is pointwise
in the matched joint input and explicitly says so.

## 7. A finite preparation and its price

The polar construction gives a concrete preparation once local coherent
Z_x and X_x X_(x+1) control access is supplied. This access is a protocol
condition, not a consequence of the framework axioms or autonomous Hspin.
The input resource is L qubits initialized in the Z=+1 product state.
Preparation of that pure product input is supplied, not derived from
arbitrary mixed inputs by unitary evolution. No dissipative or ground-state-
selection mechanism is assumed.

Any O_Lambda in SO(2L) admits at most

    G_L=L(2L-1)                                           (F25)

adjacent-coordinate plane rotations. To see the count, eliminate each
column below its diagonal using successive adjacent-row Givens rotations
from the bottom upward. There are at most (2L)(2L-1)/2 eliminations. Positive
pivots and determinant +1 leave the identity, so reversing the rotations
recovers O_Lambda without an extra reflection. Angles can be chosen in
[-pi,pi]. This proves a finite constructive decomposition, not an efficient
many-body spectral diagonalization assumption.

In the interleaved Majorana order a_1,b_1,a_2,b_2,..., adjacent bilinears
have spin forms i a_x b_x=-Z_x and i b_x a_(x+1)=-X_x X_(x+1).
A plane rotation of angle theta is implemented by a pulse generated by
one such norm-one Hermitian bilinear, with integrated magnitude |theta|/2.
The inverse ordered circuit C_Lambda^* prepares phi_Lambda from every Z=+1.
With available pulse magnitude kappa>0, a serial duration bound is

    t_prep <= pi G_L/(2 kappa).                           (F26)

If the actual drift Hspin cannot simply be switched off, apply the explicit
cancelling local controls -Hspin during the pulses. There are L onsite and
L-1 bond controls, each of range at most one. Their summed absolute control
budget plus the rotation pulses is bounded by

    B_prep <= [gL+J(L-1)] pi G_L/(2 kappa) + pi G_L/2.      (F27)

Peak coefficients are at most g+kappa on sites and J+kappa on bonds.
The ground-energy shift contributes only a scalar phase during cancellation.
This prices O(L^2) serial pulses and an O((g+J)L^3/kappa+L^2) sufficient
control budget, not a uniform preparation cost as L increases. Computing
and accurately implementing the polar matrix and Givens angles are real
resources. No certified classical bit-complexity bound or native availability
of the cancellation controls is supplied by this theorem.
This preprocessing circuit depends on volume. F21 does not compare its
entire trajectory to a fixed infinite-volume preparation protocol; its
endpoint is handled by the exact F7 identification and the F28 error bound.

If each ideal pulse differs from the implemented one by operator norm
eta_j, product telescoping bounds the state trace-norm preparation error
by 2 sum_j eta_j. The finite-mode range has N<=L. Therefore the initial
number-weighted error is at most

    2(1+L)^(2s) sum_j eta_j.                              (F28)

The subsequent full history multiplies this error by at most C_prod^2.
This bound includes a passive reference because the gate operator-norm
bound is unchanged on tensoring with its identity. For angle errors
Delta theta_j, eta_j<=|Delta theta_j|/2 is sufficient.
For own finite energy use additionally the fixed factor from F11. All
intermediate finite-system energies are at most 2(g+J)L, so their qth
moments are bounded by [2(g+J)L]^q for q>0; this is a finite-resource bound,
not a small preparation-energy assertion.

## 8. What the volume theorem supplies to a kinetic comparison

At fixed lattice spacing a, use the supplied g_a,J_a from Local Even.
The infinite-chain positive carrier here is explicitly unitarily identified
with that parent carrier. Compose W_Lambda with that identification and the
existing energy-adapted Fock isometry I_a. The latter exactly preserves
free energy, its PVM and the supplied vacuum. Thus F21-F22 provide a
finite-open-volume approximation to the actual infinite-chain part of a
common-continuum-H history comparison. They do not replace the separate
calibrated-input or kinetic error estimates.

For any sequence of already fixed finite protocols indexed by h>0, each
with a positive gap and finitely many readouts and finite time/control
resources, and any positive tolerance eta_h, the theorem permits choosing
an eventual volume Lambda_h making its full weighted error <=eta_h. In
particular one may prescribe eta_h=o(h) if that is the later composition's
requirement. This is a diagonal existence choice. It supplies neither an
explicit volume-versus-h formula nor a uniform kinetic-window rate, and
F25-F28 do not turn an unquantified required volume into an efficient
preparation algorithm. A computable volume modulus with bin-boundary and
long-time resource control remains a separate quantitative task.

## 9. Checks, alternative route and review limits

The independent finite implementation checks are in check_finite_open.py
and FINITE_CHECKS.json. Direct Pauli-spin matrices are compared with an
independent singular-value construction, including both endpoint choices,
ground shifts, all many-body levels, ground covariance, parity and polar
field signs. The diagnostic also retains a passive qubit in two complete
coarse-readout histories. Its larger finite comparator is explicitly not
the infinite-chain theorem. No monotonic convergence or asymptotic rate is
inferred from those few finite volumes.

The first implementation checked 30 finite parameter/boundary cases. Its
maximum identity residual was 6.936869916919956e-14, against the recorded
2e-10 diagnostic tolerance. Sign and endpoint mutants give visible defects;
fine measurement followed by classical binning changes the full quantum
output by trace norm approximately one despite identical coarse probabilities.

check_preparation.py separately constructs the spin Hamiltonian by bit flips,
uses an eigen-square-root polar computation rather than the first SVD path,
and explicitly compiles adjacent Majorana rotations. It checked 30 cases,
including mixed endpoint fields. Its maximum residual was
3.6806494236518905e-14 against 5e-10. Reversing the circuit order produces a
ground-vector residual 1.3963300785434987. An angle-error test satisfies both
the unweighted and F28 weighted bounds; the full values are preserved in
PREPARATION_CHECKS.json. The two processes used about 134 MB and 62 MB peak
RSS respectively, sequentially; runtimes were about 1.39 s and 0.085 s.

Finite floating-point agreement cannot prove F10, the spectral-continuity
argument or F21-F24. Their proofs above are the analytic evidence. This
author's checks are distinct implementations, not a second independent
reviewer or retained audit.

The direct local-spin-dynamics route supplies local observable limits but
by itself has no control of the global coarse energy PVM or its postmeasurement
state. It is not counted as completion of the instrument obligation. The
positive-polarization route adds the actual finite scalar shift, common
positive-Fock carriers, uniform number domains and spectral-boundary argument
that the local route alone lacks.

Remaining scope: fixed supplied one-dimensional free massive model; exact
coarse Lueders readout as the comparison object; specified matched preparation
and controls; finite histories. A finite apparatus compiler for that readout,
physical readout selection, arbitrary unbounded adaptive protocols, a
uniform infinite-input energy-constrained diamond norm, a shrinking-gap
limit and a quantitative kinetic-volume law are not established here.
FINAL_FREEZE.json seals the full candidate and check evidence before the
first mathematical finding is sent to root. Root comparison, independent
final-source review and any later formal audit remain separate.

<!-- END SOURCE A -->


<!-- BEGIN SOURCE B sha256=6d534a7c409c1af1e1bb34199a1d35977ca1c5393f4bbe165bd301fe501dbdfe -->

## Source B: Coherent phase-register instrument

Original: `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261013_213733/coarse_energy_instrument_independent/REPORT.md`. Complete immutable body follows.

# A finite phase-register module for the full coarse energy instrument

Type: bounded_theorem. Actual current surface: conditional-support.
Trace: upstream_support; partially supplies the apparatus comparison interface.
Independent audit: not performed; required before any formal retained status.
No physical axiom, microscopic identification, occurrence rule or probability
derivation is asserted.

This report is an independent derivation after the plan seal in PLAN_SEAL.json.
The parent disclosed the generic compute/copy-coarse/uncompute route before the
seal. No parent proof or constants were read. The standard route and the
coarse/fine discriminator are prior art; this is same-family analytic
corroboration and an explicit quantitative module, not a novelty certification.

## 1. Statement of the result and its physical scope

Let H be a supplied nonnegative selfadjoint operator, possibly unbounded. From
coherently controlled exp(±itH), a finite blank work register, finite ancillary
gates and a supplied classical-pointer restriction, construct a completely
positive trace-preserving classical-label/system instrument Φ. Its target is

    Λ(ρ) = Σ_z |z><z| ⊗ P_z ρ P_z,
    P_z = 1_[b_z,b_(z+1))(H),
    0=b_0 < b_1 < ... < b_(k-1) < b_k=∞.                 (1)

All maps are tensored with the identity on an arbitrary passive reference.
The last bin is unbounded. This report uses the displayed left-closed endpoint
convention; section 4 explains the other endpoint choices.

For every fixed positive trace-class input ρ with finite first energy, the
constructed Φ approaches Λ in both trace norm and the energy form trace norm

    ||X||_(1,G) = ||G X G||_1,   G=(I+H/e_*)^(1/2),       (2)

where e_*>0 is a fixed mathematical energy unit. The identities on reference
and pointer spaces are implicit. This is the form domain D(H^(1/2)), not the
operator domain D(H). The quantitative bound is (17) below.

The simplest unshifted phase-grid classifier requires a boundary-mass term.
A one-sided displacement of the *classifier thresholds*, with the target bins
held fixed, puts each boundary atom on the correct side. This gives convergence
for every fixed finite-first-energy input, even if it has boundary atoms. Its
error still includes the explicit one-sided strip weights in (14). No bound
uniform over arbitrary mean-bounded moving input families follows.

The full labelled instrument, including within-bin coherences, is compared.
Keeping a fine-energy archive and coarsening its label is a different instrument, with an
explicit three-energy discriminator in section 9. The finite-history bound
in section 6 preserves the supplied intervening evolution and requires its
stated energy-form bounds. It controls final unnormalized labelled energy
measures and first moments, and normalized W1 only with positive success mass.

This is a **global controlled-energy-oracle module**. No spatial realization,
native nearest-neighbor law, actual-spin/continuum common-H embedding,
autonomous preparation, reset, clock, selected Record or physical permanence
has been derived. Section 10 prices the supplied resources and names the
remaining implementation obligations.

## 2. Premises, conventions and source use

Work in units ℏ=1. H and its zero are fixed. All dimensionful formulas retain
e_* in (2); numerical fixtures set e_*=1. The choice of a mathematical unit
does not supply a physical calibration or a derived dimensionless value.
The Hilbert spaces may be separable and infinite dimensional. The passive
reference is arbitrary and never controlled by the apparatus.

Supplied resources:

1. Controlled exp(+itH) and exp(-itH) for the requested finite times, including
   their phase relative to the identity control branch.
2. Blank qubit registers; coherent Hadamard, Fourier and Boolean label gates.
3. A known energy/time scale for the controls and known finite bin boundaries.
4. A classical output convention: dephase the pointer in its specified basis
   and discard the work register. This is an instrument definition.
5. For histories, the original specified propagators, and the additional form
   estimates (20) wherever an energy-weighted conclusion is claimed.

These are conditional mathematical apparatus premises, not new accepted
framework primitives. The source registry was read; the module uses none of
its three approved primitives to assert control, a clock, dynamics, reset or
measurement actuality.

The pinned common-H source is the supplied multi-time note at CW head
e8d5b7b99c9faab65f71eb5ff353b60e2b609608. The exact read ranges and SHA-256
identities are in SOURCES.json. Its sections 6 and 8 and Core B define the
finite coarse spectral Lüders protocol, common H0 and intervening evolution.
They do not establish an apparatus, general post-collapse first-moment
control or an actual-spin representation of H0. No kinetic-limit proof from
that note is reused here.
The final source refresh found CW at ccbeddd0c04b70ee2b6c5f1cffeeeefa23df2989;
every supplied file snapshotted for this task, including that note, was
still byte-identical. This derivation remains bound to the frozen e8d5b7
instrument premises and does not claim review of unrelated changes at
the later head. The exact refresh receipt is preserved.

Cycle279, read through its exact pointer and archive sections, already gives
U=Q⊗I+P⊗X and distinguishes within-fibre coherence from a fine archive.
The supplied arXiv:1310.3047v2 PDF text, pp. 5–7, describes the finite-dimensional
QPE controlled powers, Fourier readout and Dirichlet-kernel outcome law.
Only those displayed parts were read. Universal controllization, its finite
refresh analysis, and a claim for unbounded H were not adopted. The
unbounded-H extension and estimates below are derived by bounded spectral
calculus, not inferred from that finite-dimensional statement.

## 3. Exact finite apparatus and its complete branch maps

Choose an energy cutoff R>0, period L=4R, a power-of-two clock dimension
M=2^m, and a finite label register B of dimension at least k. A is the
M-dimensional work register. Let F have entries

    F_(q,y) = M^(-1/2) exp(2πiqy/M).

If a qubit register has unused pointer basis states beyond k, the exact
circuit never populates them. For an imperfect implementation one may
dephase the entire register and map every unused value to a declared
valid label, such as 0. This fixed classical postprocessing preserves a
k-outcome CPTP comparison and cannot increase the error; it acts trivially
on the ideal output.

Let J be any fixed unitary with J|0>=M^(-1/2)Σ_q|q>; the register circuit below
uses m Hadamards. On a spectral fibre of H of energy E define

    D(E)_(q,q) = exp(2πiq(E+R)/L),
    W(E) = F* D(E) J,
    α_y(E) = <y|W(E)|0>
           = M^(-1) Σ_(q=0)^(M-1)
                        exp(2πiq((E+R)/L-y/M)).          (3)

The offset R is a known ancillary phase reference. It does not change the
specified system energy zero. For L=4R this is the ancillary phase
exp(iπq/2), implementable by S and Z on its two lowest binary bits.

Define a deterministic label function g on the finite grid. Initially one
may take g(y) to be the target bin containing

    e_y = Ly/M-R,

with every negative e_y assigned to the first bin. The endpoint-safe choice
is specified in section 4. Let Q_z=Σ_(y:g(y)=z)|y><y| and let C_g coherently
add/XOR g(y) into the blank label register. The isometry on system input is

    V = W(H)* C_g W(H) ( |0>_A |0>_B ).                 (4)

Here W(H) is defined entrywise by bounded spectral calculus. Every entry is
a finite linear combination of bounded exp(itH), so the unitary is defined
on the full Hilbert space without imposing D(H). It commutes with every
spectral projection of H.

The fibre output and branch amplitudes are

    β_E = Σ_z W(E)* Q_z α(E) ⊗ |z>,
    k_(a,z)(E) = <a|W(E)* Q_z W(E)|0>.                  (5)

After discarding A and dephasing B, the actual branches are exactly

    Φ_z(ρ) = Σ_(a=0)^(M-1) k_(a,z)(H) ρ k_(a,z)(H)*.   (6)

This identifies their action on off-diagonal energy blocks, not only
outcome probabilities. Indeed

    q_z(E) := Σ_a |k_(a,z)(E)|²
            = ||Q_z α(E)||²,
    k_(0,z)(E)=q_z(E),   Σ_z q_z(E)=1.                  (7)

Consequently (6) is CP and trace preserving after summing z. Its
nonselective system map preserves *every* spectral energy distribution and,
by monotone truncation, its finite first energy. This exact conservation
at an intervention does not identify its branch maps, nor prevent different
later energy laws after a noncommuting intervening propagator.

For a separate finite-matrix check, its branch Schur kernel is

    Γ_z(E,E') = <W(E')*Q_z α(E'), W(E)*Q_z α(E)>
      = Σ_(y,y':g(y)=g(y')=z)
          conjugate(α_(y')(E')) α_y(E)
          M^(-1)Σ_q exp[2πiq((E'-E)/L+(y-y')/M)].        (8)

An energy-block ρ_(E,E') is multiplied by Γ_z(E,E'). This expression follows
from W(E')W(E)*=F* diag_q[exp(2πiq(E'-E)/L)] F; the offsets cancel.
It is independent of which J prepares the uniform vector. Section 9 checks
(8) against a direct circuit that never uses this simplified kernel.

The ideal dilation is V0=Σ_z P_z⊗|0>_A|z>_B. Put z(E) for the exact target
bin and define the probability of a wrong grid label

    p(E)=1-q_(z(E))(E).

The crucial *amplitude* identity, including the uncomputed register, is

    <0,z(E)|β_E> = 1-p(E),
    ||β_E-|0,z(E)>||² = 2p(E).                         (9)

Its proof is simply <0|W(E)*Q_(z(E))W(E)|0>=q_(z(E))(E),
which is real and nonnegative. An arbitrary passive reference does not
alter this fibre identity.

The work register is not generally exactly blank: its nonzero-population
probability at energy E is 1-Σ_z q_z(E)² ≤ 2p(E). Thus an approximate
uncompute does not authorize cost-free reuse of an exactly blank A.

## 4. Quantitative phase tails, aliases and endpoint assignment

For θ=(E+R)/L modulo 1 and circular distance
d_y=dist_(R/Z)(θ,y/M), (3) gives, away from d_y=0,

    |α_y(E)|²
      = sin²(πM(θ-y/M)) / [M² sin²(π(θ-y/M))]
      ≤ 1/(4M² d_y²).                                 (10)

The removable value at a phase-grid point is defined by the finite sum (3).
For a phase radius r/L, h=Mr/L>0, sum separately over the two circular
directions. In either direction the retained scaled distances are
a,a+1,... with a≥h. Truncating at the antipode only decreases the sum.
An antipodal double count is harmless. Therefore

    Σ_(d_y≥r/L) |α_y(E)|²
       ≤ β(h):=min{1, (h^(-1)+h^(-2))/2}.              (11)

The last inequality uses
Σ_(n≥0)(h+n)^(-2) ≤ h^(-2)+∫_0^∞(h+x)^(-2)dx.
For h≥1, β(h)≤1/h. This elementary proof supplies the constants;
no asymptotic QPE convergence claim is being used as a substitute.

For E∈[0,R] the shifted phase lies in [1/4,1/2]. If 0<r<R and a grid point
is circularly within r/L, it cannot have wrapped around an end of [0,L).
Consequently |e_y-E|<r as real energies. This is the cutoff/alias guarantee.
E>R is not asserted to be identifiable, and is charged to the input tail.

**Unshifted classifier.** If g bins e_y at the original b_j and
E∈[0,R] is farther than r from every positive boundary, then a phase error
smaller than r/L yields the correct label. Hence p(E)≤β(Mr/L) off the
closed strips [b_j-r,b_j+r] and the cutoff tail. Boundary atoms may retain
order-one error; section 8 gives an exact example.

**Endpoint-safe classifier, with the same fixed target (1).** Choose

    0<δ<min{R,b_1/2},     g_δ(y)=#{j:e_y≥b_j-δ}.        (12)

For k=1 there are no boundaries and the instrument is the identity;
the b_1 condition is then omitted. All classifier boundaries are shifted
by the same δ, so their order is preserved. Put

    D_δ = ⋃_(j=1)^(k-1) (b_j-2δ,b_j).                 (13)

If E∈[0,R]\D_δ and |e_y-E|<δ, the label in (12) equals z(E).
To check each threshold: E≥b_j implies e_y>b_j-δ, while
E≤b_j-2δ implies e_y<b_j-δ. These exhaust the allowed energies outside
the indicated open strip. In particular, E=b_j is on the correct side;
no boundary atom is put into the bad set. Endpoint equality at b_j-2δ
is also safe because the good estimation error is strict.

For any nonnegative weight w and the input spectral measure
μ_ρ(A)=tr[(1_A(H)⊗I_ref)ρ], define

    M_w=∫w(E)dμ_ρ(E),
    B_w(δ,R)=∫_([0,R]∩D_δ) w(E)dμ_ρ(E),
    T_w(R)=∫_(R,∞) w(E)dμ_ρ(E),
    P_w=∫w(E)p(E)dμ_ρ(E).

Then the explicit estimate is

    P_w ≤ β(Mδ/(4R)) M_w + B_w(δ,R) + T_w(R).          (14)

It can be sharpened by multiplying the good-set mass instead of M_w.
The displayed bound is convenient and always sufficient. For the
unshifted classifier replace D_δ by the closed two-sided boundary strips.

The thresholds need only finite precision. If the actually encoded
thresholds are b_j-δ+ε_j with |ε_j|≤κ<δ and remain ordered, the same
D_δ is valid with good radius r=δ-κ in (11) and (14). The two threshold
inequalities just proved acquire ±κ and still hold. When errors differ by
j, their ordering can be ensured by κ below half the minimum original
boundary spacing. A certified finite lookup table is an alternative.

For the opposite endpoint convention, shift the classifier threshold to
b_j+δ and charge (b_j,b_j+2δ); then E=b_j is correctly assigned to the
left bin. Mixed conventions use the corresponding sign at each boundary,
with δ small enough to preserve their order. This construction does not
change the target P_z or replace sharp bins by fuzzy target effects.

## 5. Full-reference and energy-form estimates

For w=1, or w(E)=1+E/e_*, let G_w=w(H)^(1/2). For a purification ψ of a
positive trace-class ρ, bounded spectral calculus and (9) give exactly

    ||G_w(V-V0)ψ||²=2P_w,   ||G_w Vψ||²=||G_w V0ψ||²=M_w. (15)

Here the unbounded G_w is applied only on its form domain. This is justified
by first using its bounded spectral truncations and then monotone
convergence. V and V0 commute with the spectral truncations; finite M_w
gives the domain and limit. Nothing is differentiated in an unspecified
unbounded domain.

For vectors x,y, the elementary identity
|x><x|-|y><y|=|x-y><x|+|y><x-y| and the rank-one trace norm give

    || |x><x|-|y><y| ||_1 ≤ (||x||+||y||)||x-y||.

Apply this to G_w Vψ and G_w V0ψ. Partial trace of the purification/work
register and pointer dephasing contract the trace norm of a Hermitian
operator. They commute with G_w. Thus

    ||(Φ⊗id_ref)(ρ)-(Λ⊗id_ref)(ρ)||_(1,G_w)
                   ≤ 2 sqrt(2 M_w P_w).               (16)

For mixed ρ the same proof uses any purification, or Hilbert-Schmidt
vectorization of sqrt(ρ). Its spectral measure is the same μ_ρ.
For arbitrary finite trace the formula is homogeneous; ρ=0 is immediate.
Using (14) yields the promised quantitative full-instrument bound

    error_(1,G_w)
       ≤ 2 sqrt{2 M_w [β(Mδ/(4R))M_w+B_w(δ,R)+T_w(R)]}. (17)

For normalized inputs, (16) with w=1 bounds the completely reference-stable
state error by 2 sqrt(2∫p dμ). It is not an unrestricted diamond-norm
convergence statement. Taking suprema is justified only over families for
which the right-hand terms have the stated uniform controls.

For every fixed finite-first-energy ρ, T_(1+E/e_*)(R)→0 as R→∞.
Moreover D_δ decreases to the empty set as δ↓0, because its boundary
endpoints were excluded on purpose. Continuity from above of the finite
weighted measure proves B_w(δ,R)→0, uniformly in R after replacing [0,R]
by [0,∞). Thus any resources satisfying

    R_n→∞,  δ_n→0,  M_n δ_n/(4R_n)→∞                 (18)

with the restrictions in (12) give error→0 in both norms for this fixed ρ.
For example, after choosing fixed energy units, R_n proportional to n,
δ_n proportional to 1/n, and M_n a power of two at least n^3 suffice.
This gives no input-independent rate for the first two terms: finite first
energy supplies a tail limit, not its rate.

The unshifted classifier has the same conclusion if μ_ρ({b_j})=0 for
every boundary (or if the residual boundary-atom error is otherwise
controlled). The biased construction shows that failure of the unshifted
case is a route-specific endpoint problem, not a universal obstruction to
approximating the spectral instrument.

This endpoint-safe apparatus approximation does **not** remove the
positive-atomic-endpoint restriction from the supplied kinetic-limit
theorem. Its pre-intervention states vary with the kinetic parameter,
and convergence to a limiting boundary atom can leave order-one mass in
the shrinking one-sided strip. We approximate the specified H instrument
for each fixed input; we do not identify the limiting probability of a
kinetic bin whose endpoint lies on the auxiliary limiting spectrum.
Any joint limit must price the actual strip/tail weights and form constants.

In addition to trace and weighted trace estimates, (15) is a direct
form-graph vector estimate. On
Q_good=1_([0,R]\D_δ)(H), exact commutation with H also gives

    ||G(V-V0)Q_good G^(-1)|| ≤ sqrt(2β(Mδ/L)).

The full-space graph-to-graph operator norm has the same unsuppressed
spectral supremum as V-V0, since these maps commute with G. It need not
converge: the alias example below makes p(E)=1 at suitable high energies.
Thus the claimed graph convergence is on fixed form-domain vectors and
finite-first-energy inputs, with uniform control only on the qualified
spectral set or families whose weighted bad-set masses are controlled.
An analogous D(H) graph estimate would need
∫E²dμ_ρ finite; finite first energy alone does not even put a purified
vector in D(H). There is no hidden second-moment assumption in (16)–(18).

## 6. Fixed finite histories and final energy laws

Let n be fixed. At each slot j use a finite-bin target Λ_j and a finite
apparatus Φ_j of the kind above, with fresh A_j and B_j. The original
specified system propagators U_1,...,U_n act before the respective slots;
an optional U_(n+1) follows the last slot. The maps never act on the passive
reference, and there is no feedback or adaptive change of times/bins.
Retain all classical labels.

For unweighted trace norm, no energy assumption on the propagators is
needed. Telescoping the complete channel product, with approximate future
maps and exact past maps, bounds the final error by

    Δ_1 ≤ Σ_(j=1)^n 2 sqrt(2 tr(ρ_j) P_(1,j)),         (19)

where ρ_j is the exact protocol's state just before slot j, including
previous labels as part of the passive reference. For normalized
nonselective histories tr(ρ_j)=1. The relevant boundary/tail weights are
therefore those of these exact pre-intervention states. Formula (19)
does not require a maximum over an exponentially large history tree.

For energy-weighted passage we use a separate sufficient premise. Suppose

    U_j* G² U_j ≤ c_j G² as closed quadratic forms,
    equivalently ||G U_j G^(-1)||² ≤ c_j <∞.            (20)

G^(-1) is bounded. The form inequality includes preservation of D(G).
No claim that an arbitrary unitary has this property is made. A verified
work estimate U_j*HU_j≤H+C_j I would suffice with
c_j=1+C_j/e_* for C_j≥0. Obtaining that estimate for a driven model requires
its own domain/commutator/work justification; merely naming bounded V or
unitarity is insufficient.

Every ideal or exact-oracle apparatus instrument commutes with G and
preserves its weighted trace on positive inputs. More generally it
contracts ||.||_(1,G) on Hermitian inputs: conjugation by G turns it into
the same CPTP map on G X G. Meanwhile the map U_j(.)U_j* has weighted
trace-norm bound c_j, since it becomes A_j(.)A_j* with
A_j=G U_j G^(-1). This establishes the following telescoping inequality:

    Δ_G ≤ Σ_(j=1)^n [Π_(l=j+1)^(n+1)c_l]
                         2 sqrt(2 M_(G,j) P_(G,j)),   (21)

where M_(G,j)=tr(G²ρ_j) and P_(G,j)=tr(G²p_j(H)ρ_j).
The future propagator product includes the optional final propagator;
an absent final one has c_(n+1)=1. Each ρ_j is positive with finite M_(G,j),
because ideal interventions preserve energy and (20) propagates the
form domain. Bounds M_(G,j)≤(Π_(l≤j)c_l)tr(G²ρ_0) are available, though
the actual state weights in (14) can be sharper.

Proof details of telescoping: expand the difference of the composed full
labelled maps into one replacement at a time. In the jth summand apply
(16) to ρ_j, then use the weighted contraction of all future apparatus
maps and the c_l bounds of future propagators. Previous classical labels
are spectators. Sum the Hermitian trace norms. This uses no trace cycling
of an unbounded H and no normalized conditional state inside the proof.

For fixed input, fixed target histories and fixed propagators satisfying
(20), all n exact states ρ_j are fixed finite-first-energy states.
Apply (18) at each slot. The finite sum in (21) tends to zero. If a kinetic,
continuum or volume parameter also varies, the conclusion needs control
of the corresponding c_j, weighted tails and moving strip weights at
the actual joint scaling. Mean bounds alone do not supply that uniformity.
No growing-n, dense monitoring, feedback or moving-target theorem is proved.

Take any fixed selection A of the classical histories and then measure the
final energy. Let μ_A and μ'_A be the exact and apparatus unnormalized
positive energy measures. Trace-norm contraction under classical selection
and spectral measurement gives

    ∫(1+E/e_*) |dμ'_A-dμ_A| ≤ Δ_G.                    (22)

To justify the weighted version directly, test the signed difference
against bounded f with |f|≤1: its weighted integral is
tr[f(H)G X_A G], bounded by ||G X_A G||_1. Supremizing gives (22).
Thus success masses, unnormalized first moments, and these weighted
energy measures are controlled.

For p=μ_A([0,∞))>0 and p'=μ'_A([0,∞))>0, with finite first moment
E_A=∫E dμ_A, Kantorovich duality on the half-line (f(0)=0, |f(E)|≤E)
gives the explicit safe bound

    W1(μ'_A/p', μ_A/p)
      ≤ [e_* Δ_G]/p' + [Δ_G E_A]/(p'p).               (23)

Consequently positive limiting success mass and bounded conditional first
moment transfer an existing conditional W1 limit once Δ_G→0.
If p tends to zero, (23) displays the missing relative-error requirement;
there is no rare-postselection uniformity claim.

## 7. Finite implementation precision

Two errors must be distinguished.

**Ancillary gate errors and timing errors that remain functions of H.**
Assume the actual ancillary gates are unitary and act only on the finite
registers; the actual oracle timing gates still have the displayed H.
If the sum of operator-norm errors of the finite ancillary gates is η,
finite-product telescoping gives at most η for the whole unitary. If the
oracle times have errors Δt_s, let Θ=Σ_s|Δt_s|, counting forward and inverse
calls. On a fixed E fibre each controlled phase error is at most E|Δt_s|,
so the fibre isometry difference is bounded by

    d(E) ≤ min{2, η+EΘ}.                              (24)

For any cutoff Q>0, its weighted squared vector error on ρ is bounded by

    ∫w(E)d(E)²dμ_ρ(E)
       ≤ (η+QΘ)² M_w + 4 T_w(Q).                      (25)

The corresponding instrument error is at most 2 sqrt(M_w) times the square
root of (25), by the same rank-one proof as (16). Add it to (17).
The threshold-precision error κ has already been charged by replacing
δ with δ-κ in the phase-tail factor. It is not hidden in η.

Equation (25) needs only finite first energy for w=1+E/e_* and gives
pointwise convergence as η,Θ→0 after controlling the tail. A rate for the
weighted term cannot be extracted from a mean bound alone. If only an
unweighted error is desired, min{4,(EΘ)²}≤2EΘ provides a first-moment
timing estimate as well. Approximate gates under (24) still commute with H,
so their nonselective maps preserve energy and the history estimate applies.

**Generic simulator or control errors.** An operator-norm approximation to
an oracle or to a finite instrument need not commute with H and provides
no analogous energy-weighted control for unbounded H. One needs a graph
bound on the implementation error and on later evolution, or another
explicit uniform energy-tail estimate. The counterexample in section 8
prevents promoting ordinary diamond/operator-norm accuracy to (25).
This is a key unresolved requirement for a spatial simulator that is
accurate only in an ordinary norm.

## 8. Exact failure controls and the limits they diagnose

These are explicit counterexamples to *stronger omitted-hypothesis claims*,
not a universal no-go for apparatus realization.

### 8.1 Keeping a fine archive changes the instrument

Let H=diag(1,2,5), with bins [0,3) and [3,∞). The coarse branch on the first
bin preserves (|1>+|2>)/sqrt(2). A fine-energy archive followed by classical
binning instead gives

    ρ -> Σ_(i:E_i in bin z) |i><i| ρ |i><i|.           (26)

Its first conditional output on that input has purity 1/2 rather than 1;
the full instrument trace-norm difference is 1. Both histograms are (1,0).
On ψ=(|1,0>+|2,1>+|5,0>)/sqrt(3), with passive reference basis 0,1,
the branch probabilities are (2/3,1/3) for both instruments, but the first
coarse branch retains the off-diagonal |1,0><2,1|/3. Equation (26) erases it.
The complete output trace norm difference is 2/3. In the w=1+E norm it
is 2sqrt(6)/3. A later Hadamard mixing just energies 1 and 2 converts
the first within-bin superposition to the energy-1 vector under the coarse
instrument, while the fine archive gives equal diagonal weights and mean
3/2. Thus even equal immediate energy laws do not identify later behavior.

### 8.2 A fixed boundary atom defeats the unshifted classifier

Choose R=8,L=32,b=8/3 and a one-dimensional state with energy E=b, assigned
to the right bin by [b,∞). Its phase is 1/3. For every M=2^m the point
y=floor(M/3) lies strictly below the boundary and is labelled incorrectly.
Let a be the fractional part of M/3; a=1/3 or 2/3. From (10),

    p(E) ≥ sin²(πa)/[M² sin²(πa/M)]
         ≥ sin²(πa)/(π²a²)
         ≥ 27/(16π²)>0.                               (27)

Hence the full classical output error is at least 27/(8π²).
This refutes boundary-free convergence of that unshifted construction.
The one-sided classifier in (12) escapes it: E=b is a good point and
p(E)≤β(Mδ/L), which vanishes if Mδ/L→∞.

### 8.3 Phase aliases require a cutoff or tail term

At L=32, E=1 and E=33 have identical W(E), β_E and labels for every M.
The target bins [0,3),[3,∞) distinguish them. A state concentrated at
E=33 can therefore be classified as the low-energy state; no all-spectrum
operator-norm or unrestricted diamond convergence follows from this
finite-period construction.

Even mean-bounded families defeat uniform energy-weighted convergence.
Set e_*=1 for this example. Take one fixed H with nonnegative integer spectrum, integer R_n→∞,
L_n=4R_n, and M_n a power of two at least 4. Set

    ρ_n=(1-1/L_n)|0><0|+(1/L_n)|L_n><L_n|.             (28)

Then tr(Hρ_n)=1, but the second energy aliases zero exactly. For a fixed
positive boundary smaller than L_n and an endpoint-safe classifier with
δ below half that boundary, the approximate apparatus puts both components
in the first label, while the target labels the second component high.
The ordinary full-labelled error is 2/L_n, but its G-weighted error is
2(1+L_n)/L_n→2. The weighted tail in (14) detects precisely this.
The nonselective single-step energy law remains equal; the differing
joint label/energy law is the comparison object.

### 8.4 Small ordinary control error can carry finite or divergent energy

On a fixed H with H|0>=0 and H|n>=n²|n>, let T_n rotate |0> and |n>
by θ_n=1/n and be the identity elsewhere. Then
||T_n-I||≤1/n, while the energy of T_n|0> is
n² sin²(1/n)→1. The ordinary state error tends to zero, but the weighted
trace error does not. With energies n^4 the output energy diverges.
This applies to an ideal instrument followed by such a small control error.
It does not contradict (25): T_n does not commute with H and is not a
controlled timing/ancillary error covered there.
Even a uniform bound on the *form norm of T_n itself* would not repair
the missing error estimate. At e_*=1 its two-dimensional conjugated block is
[[cosθ_n,-sinθ_n/sqrt(1+n²)],
 [sqrt(1+n²)sinθ_n,cosθ_n]], whose norm is at most 1+sqrt(2).
Hence T_n satisfies a uniform bound of the form (20), but its
form-weighted discrepancy from the identity still does not vanish.

### 8.5 First energy does not supply the operator graph or arbitrary history

For H|n>=n|n>, a pure vector with probabilities proportional to n^(-5/2)
has finite first energy and infinite second energy, so it is not in D(H).
For the same H, a normalized vector with probabilities proportional to
n^(-2) has infinite first energy. A unitary can map the zero-energy vector
to that vector, so H≥0 plus arbitrary unitary evolution does not preserve
finite first energy. These examples identify the exact role of (20);
they do not assert failure of the specified CAR propagators.

## 9. Deterministic finite controls

The calculation script and complete outputs are kept beside this report.
The pre-execution control specification is CONTROL_PLAN.md.

The direct implementation applies a tensor Hadamard preparation, diagonal
controlled phases, inverse DFT, coherent coarse XOR, DFT, inverse controlled
phases and inverse Hadamards to system/reference/work/pointer amplitudes.
It then traces the work register and dephases the pointer. It does not use
the reduced kernel (8). A second implementation evaluates the closed
Dirichlet formula for its finite exponential sums and applies the resulting
kernel to system energy blocks.

Controls include exact-grid H=diag(1,2,5), off-grid energies, complex
system/reference amplitudes, the uncomputed work amplitudes, branch
coherences, trace preservation, exact spectral-energy preservation,
the full weighted bound (16), the boundary-atom and alias fixtures, and a
small non-energy-preserving rotation. These finite computations can reveal
phase, indexing, normalization or coherence errors. They cannot certify
the unbounded-domain argument, general spectral calculus, the history
proof, source kinetic limits, physical locality or a common-H embedding.

The first execution completed all declared numerical assertions, with no
execution failure or changed numerical tolerance. The exact-grid instrument
trace error was 1.50e-15; the coarse/fine entangled error was
0.6666666666666669 and its weighted error 1.6329931618554525. The maximum
direct-circuit/analytic-kernel entry discrepancy on the off-grid complex
reference tests was 4.65e-15. The off-grid instrument errors were not
monotone in M (approximately 0.0513, 0.0705, 0.0850, 0.0141 for
M=32,64,128,256); no monotonic-convergence claim is made.

The sampled dyadic boundary tests used even m and retained wrong-label
weights near 0.767 for the unshifted boundary atom at large M. The displaced
threshold weights reached 0.00332 at M=16384 with the declared decreasing
δ, consistent with the proved bounds; this finite sequence does not prove
the limit. The timing test's weighted difference was 0.0001855, below
its sufficient bound. The noncommuting rotation at n=512 had ordinary
state error 0.00391, energy 0.999999 and weighted error 2.23607, confirming
the distinction being tested.

Complete values, input amplitudes and the exact branch matrices are in
CONTROL_RESULTS.json; EXECUTION_RECEIPT.json and EXECUTION_LOG.txt bind
the actual command, source and output. Before execution, the mean-one
family control was corrected from a coherent purification to the mixed
system state actually specified in (28). That pre-run correction is
recorded in PRE_EXECUTION_SEAL.json; no failed run was erased.

## 10. Resource accounting and remaining physical obligations

For M=2^m, implement W with m Hadamards, m controlled oracle powers at
times 2^j(2π/L), and one inverse QFT. Its inverse requires one QFT,
m inverse oracle powers, and m Hadamards. Thus one intervention costs

    2m controlled energy-evolution calls,
    total absolute oracle evolution time 4π(M-1)/L,
    maximum single-call time πM/L.                    (29)

Forward and inverse time count separately. This assumes one variable-time
controlled oracle call per power; an oracle offering only a fixed base step
instead needs 2(M-1) step uses. For h=Mδ/L≥1, (11) permits error control
with p(E)≤L/(Mδ) on the good set, so the elementary construction has
oracle time proportional to 1/(δ times the desired good-set probability
error). A trace-state error target squares that probability tolerance
through (16). This is an explicit sufficient cost, not an optimality claim.

Space includes m work qubits and ℓ=ceil(log2 k) pointer qubits per
intervention, plus Boolean-computation scratch. A completely explicit
nonoptimal label table can be implemented by iterating over its M inputs,
negating the zero control bits and applying an m-controlled NOT to each
1 bit of g(y). For m≥2 one such gate decomposes into 2m-3 Toffolis with
m-2 clean scratch qubits, which are uncomputed after each use. This gives
at most Mℓ(2m-3) Toffolis and 2Mm X gates; m=1 is direct CNOT.
Comparators at the k-1 ordered thresholds can improve this table cost,
but that optimization is not needed or claimed here.

Two exact QFT circuits cost O(m²) controlled phase gates and O(m) swaps,
in addition to the 2m Hadamards. Their non-Clifford angle precision must
be supplied or synthesized and charged to η in (24); an exact finite
dimension is not an exact finite universal-gate compilation certificate.
The offset phase uses the S/Z gates noted after (3). The finite threshold
comparisons must be certified to κ<δ, or their actual additional
misclassification must be added explicitly.

For n fixed interventions one may reserve n fresh m-qubit work registers
and nℓ pointer qubits, with reusable exactly cleared scratch. Alternatively
one must explicitly reset each work register using further prepared
resources. Because the work output is only approximately blank, its
reset cannot be assumed exact at zero cost. Stored history labels also
consume space; reading/dephasing/discarding them is a supplied operation.
There is no thermodynamic erasure-work calculation in this report.

Durations in (29) are apparatus operations, not automatically instantaneous
insertions into the original physical-time evolution. Implementing the
abstract protocol at the source's observation times requires a control
schedule that gives the specified net oracle action while the original
drive is paused, canceled or otherwise accounted for. If that drive
continues and does not commute with H, equations (3)–(7) need a new error
analysis. Clock synchronization, time reversal/control phases and the
extra elapsed time remain supplied and must be priced in a realization.

The global controlled Hamiltonian effectively contains a control projector
coupled to H. Even if a finite-volume H_spin is a sum of bounded local
terms, coupling one control to all those terms is not a nearest-neighbor
implementation. A local construction must supply routing/distributed
controls, geometry, control preparation and clearing, gate support,
interaction strengths and wall-clock error estimates. A bounded finite
Hamiltonian can convert ordinary norm errors to weighted errors at a
cost depending on 1+||H_spin||/e_*; that factor may diverge with volume.
Such a compiler does not provide a continuum graph estimate by itself.

For the actual-spin/continuum question one must identify the physical
Hamiltonian and its zero, construct the embedding or comparison map, and
control the spectral instrument and the intervening dynamics in the
required weighted topology. Equal energy means, similar spectra, an
isometry alone or a local-algebra encoding is insufficient. The source
note explicitly requires the same selfadjoint H0 and projectors for its
conditional transfer; this report does not discharge that identification.

There is no pressure to change the axioms. Conditional global-oracle
accuracy, a local bounded-H compiler and a native common-H realization
are different obligations. The result here establishes the first
mathematical implication with its stated resources.

## 11. Disposition, recovery and next scientific decision

The strongest proved statement is the complete-reference form-trace
estimate (17), its endpoint-safe convergence (18), and the finite-history
transfer (21) under explicit form bounds. The negative controls refute
specific stronger shortcuts while preserving the endpoint-biased route
and possible future local implementations.

The next consequential check is an independent review of (9), the one-sided
endpoint classifier argument, and the weighted telescoping in (21), followed
by a spatial implementation with its own common-H and graph-error contract.
The present worker has not reviewed a parent candidate or tested the
specified CAR domain/commutator bounds anew.

All writes are confined to this assigned folder. No canonical source,
Git metadata, audit authority, axiom, prompt or other chat was changed.
Editable prompt files changed: none. Full sources, plan seal, controls,
results and the final content seal provide the recovery path.

## 12. No-go discipline scope record

Negative-packet status: **FAIL / partial-narrowing**, not a universal-no-go
packet PASS. N1's five-failed-family schema is not met, and N8 is a bounded
source search rather than an exhaustive historical closure review. The
positive conditional theorem above stands on its proof. The negative
statements are confined to the explicit omitted-hypothesis counterexamples,
with viable stronger-premise routes kept open. No claim that all physical
realizations fail is submitted.

**N1 — actual approach families.** Three relevant mathematical families are
identified, without manufacturing five closed routes: (a) a finite
controlled-phase register, ATTEMPTED here and successful at the stated
scope after coherent uncompute and endpoint assignment; (b) a direct exact
spectral-pointer dilation, READ AS PRIOR ART in Cycle279, which supplies an
exact instrument if the projector gate is supplied; (c) spatial synthesis
of a bounded local H, NOT ATTEMPTED by this worker, with a graph/common-H
transfer obligation. Fine archival is a control within (a)/(b), not an
additional independent family. No failed-family exhaustiveness is claimed.

**N2 — conditional obligations.** Let L denote spatial implementation,
G denote error control in the target H form norm for that implementation,
and I denote actual-spin/continuum common-H identification. No independent
wall count is asserted.

| Pair | Does the first discharge the second? | Does the second discharge the first? |
|---|---|---|
| L, G | Unresolved for the target implementation; locality alone is not the supplied weighted estimate | Not established; a norm estimate specifies no geometry |
| L, I | Unresolved; a local compiler has no identified continuum map here | Not established; an embedding is not a control schedule |
| G, I | Not established; the estimate can refer to a supplied H | Not established; an exact identification supplies no implementation error bound |

The graph-accuracy demand is part of implementing this *weighted*
instrument target, not a separately counted extra no-go. Clock, register,
reset and gate costs belong to L's construction contract rather than an
inflated number of independent walls.

**N3 — hidden-premise scan.** The specified phrase scan of the analytic
body before this scope record found only the procedural word “canonical”
in the no-edits statement; it supplies no scientific premise. Additional
occurrences in this scope record refer to workflow certificates and also
carry no scientific premise. Re-reading checked the actual
load-bearing assumptions: nonnegative selfadjoint H, supplied controlled
positive/negative evolution, blank finite registers, pointer restriction,
known scales/thresholds, finite first energy for the weighted conclusion,
and the explicit history form bounds. The off-diagonal branch kernels and
energy commutation were proved rather than supplied silently. A numerical
gate approximation that breaks that commutation is excluded explicitly.

**N4 — residual matching.** Cycle279's coarse/fine archive proof is a
matching prior witness only for the within-fibre distinction (26).
It is not evidence for the phase error, first-energy topology, finite
history estimate or locality gap. The QPE pages are positive finite
algorithmic prior art, not a no-go witness. No prior audit label or
unread theorem is used to support the counterexamples.

**N5 — resolution.** Per energy element: (9) is an analytic fibre identity,
and finite matrices test the three-energy and boundary examples. Per site:
no physical site interaction was implemented. Per mode: the finite
phase-register computation was exercised, with no general CAR-mode
realization claimed. Per block: (21) proves a fixed finite history
implication; its unbounded/domain proof was analytic, not numerically
certified. Lattice wide: no thermodynamic or native-lattice experiment,
simulation or theorem was performed. These are scope statements, not a
canonical runner's N5 execution certificate; no PR/audit packet is being
submitted by this delegated worker.

**N6 — live partial-closure routes.** The biased threshold in (12) already
closes the fixed boundary-atom failure of the unshifted route without
changing target bins or physical axioms. Increasing the phase period and
paying first-energy tails removes pointwise alias error. H-commuting timing
and ancillary errors satisfy the weighted estimate without a second
moment. A local compiler with an independently controlled graph error and
an actual common-H comparison remains a live realization route. Approved
unit/kinetic-form/realized-state primitives are not reclassified as walls.

**N7 — steelman.** A hostile reader would correctly reject any conclusion
that a finite apparatus cannot realize the coarse instrument: the supplied
Cycle279 projector pointer is already exact, and the present positive
construction handles even fixed boundary atoms. A spatial bounded-H
compiler or a different continuous-variable detector could close more of
the physical target. The actionable remaining demand is its exact
geometry/control construction and a weighted common-H instrument estimate
through the intended limit. None of the small counterexamples closes that
route, and no search failure supplies evidence that it is impossible.

**N8 — historical echo limits.** PRIOR_SCOPE_SEARCH.json binds three
read-only searches of local origin/main at
583c699e859b64ff01c8bc92d1c04bdfe9994509; complete outputs are retained.
They returned four coarse/archive textual hits, nine mostly unrelated
phase/alias hits and no hit for the narrow weighted-instrument expression.
The substantive historical comparison actually read remains the supplied
Cycle279 source. The additional hits have not been used as theorem or
retirement evidence. This limited search supports no exhaustive novelty
or wall-closure conclusion.

<!-- END SOURCE B -->


<!-- BEGIN SOURCE C sha256=aa8349482e636744d001946cf2531d83f12d79847e3d025c35d657f4d6d093a8 -->

## Source C: Finite local instrument compiler

Original: `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261013_213733/coarse_energy_instrument_root/DERIVATION.md`. Complete immutable body follows.

# Coarse energy instruments from finite coherent phase registers

Root proposed conditional derivation. No independent target findings have been
received. This is an intermediate apparatus module and a finite local-spin
compiler, not a derivation of a native physical model or an audit verdict.
Standard phase estimation, pointer dilation, coherent uncomputation and product
formulas are prior machinery. The claim being checked is their quantitative
composition with this repository's finite-first-energy protocol requirements.

## 1. Supplied model and the full instrument

Let H>=0 be self-adjoint on a separable Hilbert space, G=1+H and S=G^(1/2).
Fix finitely many internal boundaries 0<b_1<...<b_(q-1)<infinity and the
half-open interval partition I_0=[0,b_1), ..., I_(q-1)=[b_(q-1),infinity).
Write z(E) for the bin containing E and P_z=1_(I_z)(H). The ideal instrument is

    L(rho) = sum_z P_z rho P_z tensor |z><z|.

Its coherent dilation W is W psi=sum_z P_z psi tensor |0>_F tensor |z>_Z.
The fine register F in this expression is blank. A passive reference is allowed
throughout; all operators on the reference are identities. Initial rho is
positive trace class, possibly subnormalized, with M_rho=Tr(G rho)<infinity.
Energy here is the supplied H, not an unidentified physical observable.

## 2. A finite unitary construction

Take M=2^m, a period Lambda>0 and tau=2*pi/Lambda. The fine register has M
basis states. Its Fourier transform has entries exp(2*pi*i*y*n/M)/sqrt(M).
Let B be the tensor product of m Hadamards. Define

    D = sum_(n=0)^(M-1) exp(i*n*tau*H) tensor |n><n|,
    Q = (1 tensor F_M^*) D (1 tensor B).

These are bounded unitaries even for unbounded H, by spectral calculus. For a
spectral energy E, Q_E|0> has amplitudes

    a_y(E) = M^(-1) sum_(n=0)^(M-1)
                 exp(2*pi*i*n*(E/Lambda-y/M)).                    (2.1)

Choose the signed representative s_y in [-Lambda/2,Lambda/2) of Lambda*y/M,
and set e_y=max(0,s_y). Let C XOR the r=ceil(log_2 q)-bit representation of
z(e_y) into the coarse register, controlled by y. Empty extra coarse codes
are unused. For q=1 one may omit the coarse register and the entire readout.
The implemented isometry, including its residual fine workspace, is

    V psi = Q^* C Q (psi tensor |0>_F tensor |0>_Z).             (2.2)

The implemented instrument A traces F and dephases Z. It does not measure or
archive y before uncomputation. In general F is not exactly blank afterwards;
it must be kept or discarded and a fresh blank F supplied at the next readout.

Every factor commutes with spectral projections of H on the system. Thus V
and W intertwine every bounded spectral function and G or S on its domain:

    (S tensor 1)V=VS,  (S tensor 1)W=WS.                       (2.3)

In particular both dilations preserve the system energy distribution when
the readout is nonselective. This is a statement about system energy in the
supplied model, not total apparatus energy conservation.

## 3. Exact error identity and phase resolution

For each E, apply the unitary Q_E to both terms of V_E-W_E. The difference
becomes C(Q_E|0> tensor |0>)-Q_E|0> tensor |z(E)>. Fine labels y are orthogonal;
for a wrong coarse label the two coarse basis vectors have squared distance2.
Consequently

    ||V_E-W_E||^2 = 2 p(E),
    p(E)=sum_{y:z(e_y)!=z(E)} |a_y(E)|^2.                      (3.1)

There is no factor equal to the number of energies or coarse bins. In
particular fine energies within one coarse bin can retain their coherence.

For circular phase distance d_y in [0,1/2] from E/Lambda to y/M, the geometric
sum gives |a_y(E)|<=1/(M |sin(pi*d_y)|)<=1/(2*M*d_y) when d_y>0.
Fix delta>0, K>=0, Lambda>2(K+delta), and a=M*delta/Lambda>1. For 0<=E<=K
at distance greater than delta from every internal boundary, any circular
estimate within delta in energy has a signed representative within delta
of E. Clamping a negative estimate to zero cannot increase its distance from
E. Such an estimate has the correct bin. Hence wrong labels require
d_y>=delta/Lambda.

The scaled signed distances x=M*d_y lie on the two rays of a unit-spaced
shifted integer lattice, with absolute value at least a. On each ray their
inverse-square sum is at most 1/a^2+integral_a^infinity x^(-2)dx, which is at
most 1/(a-1). The finite circular set is a subset of these two rays; a tie at
the antipode can only reduce its cardinality. Therefore

    p(E) <= eta := min(1, 1/[2(a-1)])                         (3.2)

on the good energy set. The exact-grid case follows directly from (2.1).
For all other E use p(E)<=1. This loose bound is sufficient; no optimal
phase-estimation constant is claimed.

## 4. Trace norm, reference systems and energy weights

Let mu_rho(B)=Tr(rho 1_B(H)), including the identity on any passive reference.
Let mu_G,rho(B)=Tr(G rho 1_B(H)) and B_delta be the delta-neighborhood of the
finite internal boundary set, intersected with [0,infinity). Define

    t_K = mu_G,rho((K,infinity)),
    b_delta = mu_G,rho(B_delta),
    R = eta M_rho + b_delta + t_K.

Equation(3.1), spectral calculus and Hilbert-Schmidt integration give

    ||(S tensor 1)(V-W)rho^(1/2)||_2^2
       = 2 integral (1+E)p(E) dmu_rho(E) <= 2R.               (4.1)

For any two Hilbert-Schmidt operators X,Y,
||XX^*-YY^*||_1 <= (||X||_2+||Y||_2)||X-Y||_2, by expanding the
difference into (X-Y)X^*+Y(X^*-Y^*). Set X=(S tensor 1)V rho^(1/2)
and Y=(S tensor 1)W rho^(1/2). Equation(2.3) gives both norms sqrt(M_rho).
Taking the partial trace of F and dephasing Z are trace-norm contractions on
Hermitian trace-class operators and commute with the system weighting. Thus

    ||(S tensor 1)(A-L)(rho)(S tensor 1)||_1
       <= 2 sqrt(2 M_rho R).                                (4.2)

All identities are justified first by bounded energy cutoffs, or equivalently
by the trace-class input S rho S and the bounded intertwining maps V and W;
then monotone/Hilbert-Schmidt convergence removes the cutoff. No second
moment, density of spectral eigenvectors or finite-rank energy cutoff is used.
The same proof is unchanged with an arbitrary passive reference and with
previous classical history registers retained. This is an energy-constrained
reference-stable bound, not an unconstrained diamond-norm assertion.

Dropping S gives the analogous unweighted estimate with Tr(rho), ordinary
boundary mass and ordinary cutoff mass. The weighted bound also bounds the
trace-norm error, each branch probability error and each branch first-energy
error, since ||S^(-1)||<=1 and ||H G^(-1)||<=1. For a fixed state, t_K->0 as
K->infinity. If mu_rho has no atom at each internal boundary, b_delta->0 as
delta decreases to zero: these boundaries are finite energies, so the weight
is locally bounded. Hence choosing K->infinity, delta->0,
Lambda>2(K+delta), and M*delta/Lambda->infinity proves convergence in(4.2).
No explicit rate for the state's tail or boundary mass has been assumed.

## 5. Families and finite histories

For a parameter family rho_alpha the sufficient uniform/joint conditions are

    sup_alpha M_rho_alpha < infinity,
    lim_(K->infinity) limsup_(alpha->limit) t_(alpha,K)=0,
    lim_(delta->0) limsup_(alpha->limit) b_(alpha,delta)=0.     (5.1)

Any K_alpha->infinity and delta_alpha->0 then make those terms vanish,
by monotonicity and comparison to fixed K and delta. Take the phase
resolution eta_alpha->0 as well. Uniform conclusions on a whole resource
set replace limsup_alpha by its supremum. Bounded first moments alone do
not imply the tail condition. Boundary regularity of a weak limiting energy
law implies the last condition at the finitely many finite boundaries, with
the weight bounded on their neighborhoods.

For a fixed n readouts, place supplied unitary drives U_j between them.
Assume ||S U_j S^(-1)||<=L_j with the stated common energy. The weighted
conjugate of a drive is X -> B_j X B_j^*, of trace-norm norm at most L_j^2.
Both ideal and phase-register readouts have weighted conjugates that are
trace-preserving CP maps, by(2.3); their norm on Hermitian inputs is at most1.

Telescoping the channel products with an ideal prefix and actual suffix
therefore bounds the weighted error of the entire classical-history/system
output by the sum, over j, of the single-readout bound(4.2) evaluated at the
ideal pre-readout state sigma_j, multiplied by the product of L_k^2 for all
subsequent drives. Prior classical records are passive references at that
step. There is no demand to reset correlated fine registers: allocate a fresh
one at every readout. The graph and tail hypotheses are those of the ideal
pre-readout family, whose conditional branches are summed as positive
subnormalized states; finite n and finitely many bins keep that sum finite.

The repository's accepted energy-tail theorem can supply the joint tail
condition for those states only when its actual two-sided G graph bounds and
fixed finite protocol premises hold. Its finite-history weak-law premise
can supply boundary regularity only at boundaries regular for the relevant
pre-readout limiting marginal. These are explicit applications, not facts
obtained from the register construction. Conditional branch conclusions
require a limiting branch probability bounded away from zero. The present
proof compares instruments; combining it with an ideal weak-law/first-moment
limit transfers that limit, and hence W1 when the respective probability
measures have the required weak convergence and moment convergence.

## 6. Decisive controls and limits of the claim

Fine archive: take distinct exact phase-grid energies E_0,E_1 in the same
bin, an energy E_2 outside, and (|E_0>+|E_1>)/sqrt(2). The correct ideal
coarse branch leaves this pure superposition unchanged. Measuring/retaining
a fine energy label and forgetting it dephases that superposition, with
trace-norm error1. The Bell-correlated version with a passive reference has
the same error. Equation(2.2) restores the blank fine register for those
exact-grid inputs and preserves this coherence. A coarse pointer alone is
therefore insufficient evidence of the full intended instrument.

Boundary atom: choose a boundary b=1, period Lambda=3, and the exact energy
E=1, assigned to the upper bin. For dyadic M, M/3 has fractional part r=1/3
or2/3. The closest lower grid point has wrong label, and its probability is
sin^2(pi*r)/(M^2 sin^2(pi*r/M)) >= 27/(16*pi^2). Thus this construction need
not converge on boundary atoms. This is a counterexample to a regularity-free
claim, not necessity of regularity for every possible apparatus or sequence.

Phase alias: energies0 and Lambda have identical Q_E. If their desired bins
differ, a fixed period cannot distinguish them, for any M. The growing
cutoff/period hypothesis removes this obstruction on the controlled family.

Weak-only control: states(1-1/N)|0><0|+(1/N)|N><N| converge in trace norm to
vacuum, yet their first energies stay1. This violates uniform first-energy
tails, so an unweighted instrument estimate cannot replace(4.2).

## 7. Explicit ideal-oracle resource accounting

Binary control implements D with m controlled evolutions exp(i*t_j*H),
t_j=tau*2^j. Q^* requires their inverses in the reversed circuit. Total
absolute oracle evolution time is2*tau*(M-1); the longest query is
tau*M/2. Both signs and controlled access to the actual H are supplied
resources. There are two Fourier transforms and2m Hadamards in V.

A finite exact lookup is available without assuming a black-box bin gate.
For each y, temporarily flip fine bits whose target pattern is zero,
compute their AND into m-1 clean scratch bits by an explicit Toffoli chain,
CNOT that AND into each coarse bit of z(e_y), uncompute the chain, and undo
the pattern flips. This costs at most M[2(m-1) Toffolis+r CNOTs+2m X gates]
for m>=2, with m-1 scratch bits. Scratch returns exactly blank. This bound
is intentionally coarse. The assumed condition M*delta/Lambda>1 together
with Lambda>2*delta ensures M>=4. Boundaries determine a finite lookup table;
their mathematical specification and exact gate-angle access are inputs.

Each readout uses m fine bits plus r output bits and the reusable lookup
scratch. A finite history reserves n fresh fine registers and n coarse
records, or supplies a priced reset mechanism. This derivation supplies
no free erasure, finite-temperature preparation theorem, autonomous clock,
permanent macroscopic record or resource bound uniform as accuracy grows.

## 8. Conditional local compiler for a bounded finite spin Hamiltonian

This section changes to a FINITE supplied system. Let

    H_N=c*1+sum_(l=1)^L h_l >=0,
    B_N=|c|+sum_l ||h_l||,
    C_N=sum_(l<k)||[h_l,h_k]||.

Each h_l has a specified bounded-arity, bounded-range support in a finite
connected geometry. Assume individually switchable signed local term gates,
local controlled versions of them with one nearby auxiliary bit, and a
connected auxiliary bus with a bit near every term. Also assume local
auxiliary one-, two- and three-bit gates. These are explicit control and
geometry hypotheses. H_N is not identified with the preceding unbounded H.

For two bounded self-adjoint terms A,B, Duhamel comparison of
exp(i*t*(A+B)) and exp(i*t*A)exp(i*t*B) bounds their difference by
t^2||[A,B]||/2: differentiate the product in the joint interaction picture,
write the conjugation difference of B as the integral of the conjugated
commutator, and use unitary invariance of norm. Induction over the terms
and telescoping r substeps then gives

    ||exp(i*t*sum_l h_l) - (prod_l exp(i*t*h_l/r))^r||
        <= t^2 C_N/(2r).                                    (8.1)

The scalar c phase is implemented exactly on the controlling bit. A
controlled operator has the same error as its active block. If the j-th
query uses r_j substeps, the error of the Q circuit is at most
sum_j t_j^2 C_N/(2r_j). Choose the inverse approximate Q circuit exactly as
the inverse gate list; then the full V circuit error is at most twice this
sum. No cancellation of its noncommuting term errors is assumed.

Writing S_N=sqrt(1+H_N), ||S_N|| ||S_N^(-1)||<=sqrt(1+B_N).
An unweighted isometry error u therefore gives graph-half error

    d = ||(S_N tensor 1)(V_tilde-V) S_N^(-1)||
      <= sqrt(1+B_N)*u.                                     (8.2)

The ideal V graph-half norm is1. The actual graph-half norm is at most1+d,
so the weighted output error on rho is at most(2+d)d M_rho, by the same
Hilbert-Schmidt factorization as in section4. Its weighted CP-map norm is
at most(1+d)^2, available in the finite-history telescope. The compiled
apparatus can change system energy; exact energy preservation is asserted
only for the ideal oracle circuit. For a desired d<=zeta>0 it suffices to use

    r_j=max(1,ceil(m*C_N*t_j^2*sqrt(1+B_N)/zeta)).             (8.3)

If C_N=0 the local product is exact. Otherwise each query contributes at
most zeta/[2m sqrt(1+B_N)] to the Q error. The term-gate count for Q and its
inverse is2L sum_j r_j, with

    sum_j r_j <= m + m*C_N*sqrt(1+B_N)*tau^2*(M^2-1)/(3zeta).

To implement a controlled product locally, fan out the computational basis
of its fine control bit along a spanning tree of the bus using CNOTs, apply
each local term controlled by its nearby bus bit, and reverse the fanout.
This is a coherent GHZ control encoding, not cloning an arbitrary state.
The term gates never change bus bits. In both control branches the inverse
fanout restores the bus exactly, even when the fine control was entangled
with the system. With V_bus bus vertices including the controlling root,
each query uses2(V_bus-1) fanout/unfanout CNOTs. Q and its inverse use
4m(V_bus-1) such gates. Depth depends on the spanning-tree height and the
specified term schedule; no finite-speed independent-of-size claim is made.

The auxiliary QFT and lookup gates also require routing if their operands
are not adjacent. They can be routed by explicit swaps on a connected
finite auxiliary graph, applying the gate on an adjacent patch and undoing
the permutation. Such a compilation has finite size-dependent overhead;
an exact routed count requires the chosen graph and is an open implementation
deliverable. The quoted logical gate counts exclude this routing overhead.
No global gate is declared local merely by writing it in a circuit.

This compiler requires additional spatial sites, blank pure auxiliaries,
signed switching, gate precision and an externally supplied timing schedule.
It prices oracle replacement and logical controls, but does not furnish a
closed autonomous energy ledger. A native single-qubit-per-site theory must
supply a compatible enlarged geometry and all those physical resources.
As N and continuum resolution change, B_N,C_N, bus size and required gate
precision can diverge. Equations(8.1)-(8.3) expose that cost rather than
asserting uniformity. A calibrated identification of finite H_N, its prepared
state and these instruments with the common continuum H remains unproved;
the existing even-algebra embedding alone is insufficient for it.

## 9. Proposed scope

Sections1–5 propose a finite-first-energy approximation of the full coarse
instrument, stable with a passive reference and composable on fixed finite
histories under explicit tail, boundary and graph assumptions. Section8
proposes a conditional local finite-system implementation with stated
size/accuracy costs. Neither establishes the actual continuum physical
energy instrument, autonomous apparatus, native symmetries, interacting
channel selection or empirical validity. These remain named constructive
obligations. Independent derivation, decisive controls and review are pending.

<!-- END SOURCE C -->


<!-- BEGIN SOURCE D sha256=ba189d9680af226772af6a3a0e23103b67d5f99443c0b76a05427bbd5b372890 -->

## Source D: Endpoint precision addendum

Original: `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261013_213733/crash_recovery_01a13807/endpoint_precision/PRECISION_ADDENDUM.md`. Complete immutable body follows.

# Precision addendum: one-sided coarse energy endpoint assignment

Status: completed bounded recovery note, supported by the proof and checks below; not an audit verdict. Sealed source files remain unchanged.

## Contract and pinned sources

Target: adjudicate finite-resolution endpoint membership and the effective-margin convergence condition for the saved one-sided classifier. Preserve the fixed-input/moving-family distinction, the supplied-oracle scope, and existing common-H identification. No physical premise, publication package, prompt, worktree, or Git state is changed.

Instruction source snapshots supplied by supervisor: main `583c699e859b64ff01c8bc92d1c04bdfe9994509`; ai/execution `3a4b2c66a1ead7a1c48b4359627e968f681e3c39`. No fetch performed because this dispatch prohibits Git-state changes. Applicable AGENTS, science workflow, freshness and workhorse instructions were read. Model and reasoning effort inherited without override.

All science paths below are relative to `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261013_213733`. SHA-256 identities recorded before analysis:

| Source | SHA-256 |
|---|---|
| `coarse_energy_instrument_independent/REPORT.md` | `6d534a7c409c1af1e1bb34199a1d35977ca1c5393f4bbe165bd301fe501dbdfe` |
| `coarse_energy_endpoint_review/REVIEW.md` | `f3a37f50b99de2c8d8dd402cbf89d616619348f63fbcd5fed257589e77101b62` |
| `coarse_energy_endpoint_review/decisive_controls.py` | `1a68906e0efa580e4906686cc9bb06a7d288e59783e0e113a26e9110b1fabcad` |
| `coarse_energy_endpoint_review/decisive_run01/RECEIPT.json` | `fda0e82f3156628fe76d6f56dbc671ab4dc753e2d84334d7a721dbf6ee7451cb` |
| `coarse_energy_instrument_root/DERIVATION.md` | `aa8349482e636744d001946cf2531d83f12d79847e3d025c35d657f4d6d093a8` |

## 1. Result and exact scope

The unrestricted finite-resolution assertion at `REPORT.md:249`, “no boundary atom is put into the bad set,” is false. Its proof establishes the correct decision at each atom's own threshold; it does not exclude that atom from a higher boundary's strip. The bad-strip estimate (14) already charges such atoms. The fixed-input convergence result survives.

Write the internal boundaries as `b_1 < ... < b_m`, with `m=k-1`, and keep the report's fixed target bins `[b_i,b_(i+1))`. For `m>=2`, let

```text
d_min = min_(1<=i<m) (b_(i+1)-b_i).
```

Use `d_min=+infinity` when there are zero or one internal boundaries. The exact condition that **all internal boundary energies lie outside the union** `D_delta = union_j (b_j-2delta,b_j)` is

```text
2 delta <= d_min.                                             (A1)
```

Equality is allowed. The prior review's strict inequality is sufficient but stronger than needed. Condition (A1) is not needed for (14), nor is it an additional hypothesis needed at every index for the fixed-input limit. It holds eventually when the finite boundary list is fixed and `delta_n -> 0`. To apply the phase-tail bound at an individual atom, that atom must also lie in `[0,R]`; an atom above `R` is charged to the tail.

With encoded threshold errors `|epsilon_j|<=kappa<delta`, the relevant good radius is

```text
r = delta-kappa > 0,
h_eff = M r/(4R).                                            (A2)
```

The sufficient resolution limit is `h_eff,n -> infinity`. The nominal limit `M_n delta_n/(4R_n) -> infinity` plus `kappa_n<delta_n` is insufficient. Divergence of `h_eff` is a sufficient resource condition for the displayed estimate, not a necessary condition for every individual apparatus/input sequence; exact grid alignment and the one-bin identity give elementary exceptions to any necessity claim.

## 2. Exact original and replacement wording

These are proposed replacements in this addendum. No replacement has been applied to the sealed report.

### 2.1 Finite endpoint paragraph, REPORT.md:245–250

Exact original:

> If E∈[0,R]\D_δ and |e_y-E|<δ, the label in (12) equals z(E).
> To check each threshold: E≥b_j implies e_y>b_j-δ, while
> E≤b_j-2δ implies e_y<b_j-δ. These exhaust the allowed energies outside
> the indicated open strip. In particular, E=b_j is on the correct side;
> no boundary atom is put into the bad set. Endpoint equality at b_j-2δ
> is also safe because the good estimation error is strict.

Replacement:

> If E∈[0,R]\D_δ and |e_y-E|<δ, the label in (12) equals z(E). For each threshold j, E≥b_j implies e_y>b_j−δ, while E≤b_j−2δ implies e_y<b_j−δ. Thus all threshold indicators agree outside the union of the open strips. At E=b_i, the indicator of its own threshold and every lower threshold is correct. The atom lies outside D_δ exactly when i is the last internal boundary or b_(i+1)−b_i≥2δ. Hence every internal boundary atom lies outside D_δ exactly when 2δ≤d_min, where d_min is the smallest adjacent internal-boundary gap and is taken as infinity if there are fewer than two internal boundaries. Boundary atoms in another boundary's strip remain charged to B_w; atoms above R remain charged to T_w. Equality E=b_j−2δ is safe for threshold j because |e_y−E|<δ is strict; safety for the full label still requires exclusion from every strip. For any fixed finite boundary list, all its atoms leave D_δ eventually as δ tends to zero.

This also qualifies the original lower-endpoint sentence. For the same close-boundary fixture below, `E=b_2-2delta=7/8` is the lower endpoint of the second strip but lies in the first strip. On the exact grid its target label is 0 and shifted label is 1. This is the same individual-strip versus union distinction, not a separate failure of the error bound.

### 2.2 Overview, REPORT.md:39–44

Exact original:

> The simplest unshifted phase-grid classifier requires a boundary-mass term.
> A one-sided displacement of the *classifier thresholds*, with the target bins
> held fixed, puts each boundary atom on the correct side. This gives convergence
> for every fixed finite-first-energy input, even if it has boundary atoms. Its
> error still includes the explicit one-sided strip weights in (14). No bound
> uniform over arbitrary mean-bounded moving input families follows.

Replacement:

> The simplest unshifted phase-grid classifier requires a boundary-mass term. A one-sided displacement of the classifier thresholds, with the target bins held fixed, protects each boundary atom against its own threshold. For a fixed finite boundary list, sufficiently small displacement also separates every atom from the other thresholds' bad strips. Together with the effective phase-resolution condition below, this gives convergence for every fixed finite-first-energy input, including inputs with boundary atoms. At finite resolution the bound retains all one-sided strip weights in (14). No bound uniform over arbitrary mean-bounded moving input families follows.

### 2.3 Explicit precision limit, REPORT.md:323–327

Exact original:

> by [0,∞). Thus any resources satisfying
>
>     R_n→∞,  δ_n→0,  M_n δ_n/(4R_n)→∞                 (18)
>
> with the restrictions in (12) give error→0 in both norms for this fixed ρ.

Replacement:

> by [0,∞). For exactly encoded thresholds, any resources satisfying R_n→∞, δ_n→0 and M_nδ_n/(4R_n)→∞, with the restrictions in (12), give error→0 in both norms for this fixed ρ. More generally, suppose the encoded thresholds b_j−δ_n+ε_(j,n) remain ordered, |ε_(j,n)|≤κ_n<δ_n, and M_n is a power of two. Put r_n=δ_n−κ_n. The sufficient resource conditions are
>
>     R_n→∞,  δ_n→0,  M_n r_n/(4R_n)→∞,
>     0≤κ_n<δ_n<min{R_n,b_1/2}.                       (18-precision)
>
> Use β(M_nr_n/(4R_n)) in (14), (17) and the good-set graph estimate. The bad strips remain D_(δ_n), with width 2δ_n. The conditions are vacuous for the one-bin identity instrument. For varying inputs or protocols, the corresponding strip/tail weights, total weighted masses and history propagation factors must also make the displayed error bounds vanish.

The finite-precision paragraph at lines 268–273 and the reminder in section 7 already identify `delta-kappa` correctly. The replacement makes that substitution explicit in the asymptotic statement. No timing-error formula is changed. For example, `kappa_n<=a delta_n` for a fixed `a<1` makes the nominal resolution limit sufficient because `r_n>=(1-a)delta_n`.

## 3. Proof of the finite condition and unchanged bound

At a boundary energy `E=b_i`, membership in `D_delta` means that for some `j`,

```text
b_j-2delta < b_i < b_j.
```

Only `j>i` can satisfy this. If such a `j` exists, the next boundary already satisfies `b_(i+1)-b_i<2delta`. Conversely that strict inequality puts `b_i` in the next strip. Thus

```text
b_i not in D_delta
    iff i=m or b_(i+1)-b_i >= 2delta.                         (A3)
```

Taking all internal boundaries gives (A1). This is an exact criterion for membership in the chosen bad set. It is not an iff criterion for actual error at a particular finite grid. For instance, with exact threshold encoding and a perfectly estimated `b_i`, the label is correct exactly when `i=m` or `delta < b_(i+1)-b_i`. In the range `delta < gap < 2delta`, the exact estimate is correct even though the theorem conservatively charges the atom to the strip. At `delta=gap`, threshold equality uses `>=` and mislabels the atom upward.

For finite precision, set `t_j=b_j-delta+epsilon_j`, `|epsilon_j|<=kappa<delta`, and `r=delta-kappa`. If `|e-E|<r`, then

```text
E >= b_j:
    e > E-r >= b_j-delta+kappa >= t_j;
E <= b_j-2delta:
    e < E+r <= b_j-delta-kappa <= t_j.                       (A4)
```

The strict estimate inequality makes both endpoint equalities safe for that threshold. Outside `D_delta`, every indicator agrees with its target indicator. This argument allows all the stated threshold errors, not merely one selected sign. To see the geometry directly, the least possible label over all such errors and estimates is `#{j:b_j<=E}`, and the greatest possible label is `#{j:b_j<E+2delta}`. Their difference counts precisely the boundaries with `E<b_j<E+2delta`. The two extremal error choices are common shifts by `+kappa` and `-kappa`, so they preserve threshold order. Consequently exclusion from `D_delta` is also exact for this worst-case guarantee over real estimates and admissible threshold errors. A particular phase grid may give a better result.

Because `r<=delta<R`, the report's cutoff argument identifies a circular phase error smaller than `r/(4R)` with an ordinary energy error smaller than `r` on `[0,R]`. Its elementary Dirichlet tail bound then gives `p(E)<=beta(h_eff)` on that good set. Elsewhere use `p(E)<=1`. With the report's notation, for either `w=1` or `w(E)=1+E/e_*`,

```text
P_w <= beta(h_eff) M_w + B_w(delta,R) + T_w(R),
error_(1,G_w) <= 2 sqrt(2 M_w P_w),
G_w = sqrt(w(H)).                                           (A5)
```

The second inequality follows from the unchanged fibre identity `||beta_E-|0,z(E)>||^2=2p(E)`, weighted spectral integration and the rank-one/Hilbert–Schmidt trace-norm estimate. The finite classifier change alters `p`, not that identity or the reference-system argument. There is no new second-moment assumption and no need to place boundary atoms outside all strips to make (A5) valid.

## 4. Direct counterexample and the equality case

Use the prior review's proposed fixture, independently checked here:

```text
b_1=1, b_2=9/8, delta=1/8, R=2, L=8, M=1024, E=1.
```

The restrictions in (12) hold. The phase is `theta=(E+R)/L=3/8`, exactly at `y=384`. Orthogonality of the finite roots-of-unity sum makes the phase outcome a point mass there. The encoded thresholds are `7/8` and `1`, so the label is 2. The target label of `[1,9/8)` is 1. Therefore `p(E)=1`, the full classical-label/system trace error is 2, and its `w=1+E` weighted error is 4. The atom lies in the second strip `(7/8,9/8)`. Here `h=16` and `beta(h)=17/512`; (A5) remains valid because `B_1=1` and `B_(1+E)=2`.

Keeping the same phase grid but setting `delta=1/16` gives `2delta=b_2-b_1`. Both strips exclude `E=1`, the thresholds become `15/16` and `17/16`, and its exact label is 1. This checks that equality in (A1) is allowed. The direct finite-sum computation gives wrong probability `1.0` for the first fixture and about `3.07e-27` for the equality fixture; the exact values 1 and 0 follow from the geometric-sum proof, not from rounding those numbers.

## 5. Fixed-input and family quantifiers

Fix a supplied nonnegative selfadjoint `H`, a finite list of target boundaries and `e_*>0`. For every fixed positive trace-class input `rho` on the system and any passive reference, assume `M_(1+E/e_*)<infinity`. For every resource sequence satisfying (18-precision), the instrument error tends to zero in ordinary and energy-form trace norm. Here the circuit has the stated threshold errors and otherwise uses the exact supplied oracle and ancillary operations. Additional gate, timing or simulator errors still require their separate bounds in the source. Write `mu_(w,rho)(A)=integral_A w(E) dmu_rho(E)` for the weighted spectral measure.

Indeed, for each fixed energy `E`, no member of the finite boundary list lies strictly between `E` and `E+2delta` once `delta` is small enough. Hence `1_(D_delta)(E)->0`, including at all boundary energies. Since the weighted spectral measure is finite, continuity from above (or dominated convergence for a nonmonotone sequence `delta_n->0`) gives

```text
mu_(w,rho)(D_(delta_n)) -> 0,
B_w(delta_n,R_n) <= mu_(w,rho)(D_(delta_n)) -> 0.
```

Its tail `T_w(R_n)` also vanishes. The effective-resolution limit makes `beta(h_eff,n)->0`. Equation (A5) proves the conclusion. A single valid resource sequence thus works pointwise for every fixed input of this class; finite first energy supplies no universal rate for the strip and tail limits.

For a moving input `rho_n`, apply (A5) at the actual parameters. A precise sufficient condition is

```text
M_(w,n) [ beta(h_eff,n) M_(w,n)
          + B_(w,n)(delta_n,R_n) + T_(w,n)(R_n) ] -> 0.       (A6)
```

If `sup_n M_(w,n)<infinity`, it suffices that `h_eff,n->infinity` and both actual bad-strip and tail weights tend to zero. Bounded weighted mass alone does not imply either uniform integrability of the energy tails or disappearance of moving strip mass. For a uniform statement on a class of inputs, corresponding sufficient conditions are bounded `sup_rho M_w`, vanishing `sup_rho mu_(w,rho)(D_delta)` as `delta->0`, and vanishing `sup_rho T_w(R)` as `R->infinity`. These are sufficient hypotheses for this bound, not asserted necessary conditions for every instrument family.

A separate moving-family witness sets `e_*=1` and uses a single bounded diagonal `H` with eigenvalues `1` and `E_n=1-2^(-n-1)` for integers `n>=2`. Let `rho_n` be the pure state at `E_n`, and choose

```text
R_n=2^n, delta_n=2^(-n), M_n=2^(3n+2), kappa_n=0.
```

Then `h_n=2^n->infinity`. Both `E_n` and 1 are exact phase-grid energies. With the sole boundary `b=1`, `E_n=1-delta_n/2` is below the target boundary but above the shifted threshold `1-delta_n`, so its wrong label probability is exactly 1. Its weighted strip mass is `1+E_n->2`, its weighted tail is zero, and its full weighted error tends to 4. The input first energies are uniformly bounded, and its energy measures converge weakly to the boundary atom. The fixed state at energy 1 is correctly labeled in this example. Thus the failure concerns a preselected joint scaling for a moving family; it does not refute the fixed-input theorem or rule out family-adapted resource choices.

For a fixed finite history, the same correction is made at each slot. Fixed ideal pre-intervention states have finite first energy under the source's stated form bounds, so the finite telescoping sum still tends to zero. With a varying external parameter, the actual per-slot terms and propagation factors in (21) must make that sum vanish. This addendum does not supply an infinite-history, moving-target, or positive-atomic-endpoint kinetic theorem.

## 6. A fresh fixed-state precision control

To check the effective-margin requirement without replaying the review's one-third-grid fixture, keep `E=b=1` and use, for `n>=2`,

```text
M_n = 2^(3n+2),
a_n = 2^(2n)+1/2,
R_n = M_n/(4a_n),  L_n=4R_n,
delta_n = 2^(-n),
r_n = L_n/M_n^2,
kappa_n = delta_n-r_n,  epsilon_n=+kappa_n.
```

These are finite admissible parameters, with `R_n~2^n->infinity`, `delta_n->0`, and nominal resolution

```text
M_n delta_n/L_n = 2^n + 2^(-n-1) -> infinity.
```

However, `h_eff,n=M_n r_n/L_n=1/M_n->0`. The actual threshold is `1-r_n`. The phase-grid coordinate at energy 1 is `M_n/4+a_n`, whose fractional part is exactly `1/2`. Its nearest lower grid point has energy `1-L_n/(2M_n)`, which is below `1-r_n` since `M_n>2`. That outcome has the wrong label. From the finite geometric sum its probability is

```text
1 / [M_n^2 sin^2(pi/(2M_n))] >= 4/pi^2 > 0.40528.            (A7)
```

Thus the fixed input retains a nonzero labeling error although the nominal resource limits and `kappa_n<delta_n` hold. Here the boundary atom is outside `D_(delta_n)` and below `R_n`, so neither a strip nor a tail term explains the error; the lost effective margin does. The valid effective beta equals 1 and makes no convergence promise. Direct finite sums at `M=256,2048,16384` give this one wrong outcome probabilities `0.4052898208706713`, `0.40528481404222017`, and `0.4052847358111145`, respectively. The general lower bound (A7), not these samples, establishes the persistent error.

## 7. Actual checks, provenance and limits

The five named initial sources were read, including the full report and its complete endpoint, weighted-error and history arguments, the root derivation, prior review, review control source and receipt. An initial display truncation was repaired by reading the omitted ranges; no truncated display is treated as complete coverage. The local science workflow was also checked byte-identical to its pinned main version. The older root derivation uses the unshifted classifier with its own boundary-mass premise; this addendum does not replace that construction.

New evidence is confined to this directory:

- `independent_check.py` — stdlib-only exact interval arithmetic and direct finite Fourier sums; imports neither author nor reviewer code.
- `run01/stdout.json` — full computed values and source hashes.
- `run01/stderr.txt` — empty actual stderr.
- `run01/RECEIPT.json` — actual command, runtime, timestamps, return code and hashes.

The recorded command is `/opt/homebrew/opt/python@3.13/bin/python3.13 independent_check.py`, run in this directory with `PYTHONDONTWRITEBYTECODE=1`. The sole run completed with exit code 0 at `2026-10-14T01:48:31.000171+00:00`; elapsed time was about 0.512 seconds. The source SHA-256 is `148bdfe77b9d800490c3211ae7c8164034ddd72c214f76a563a5dbd8fafc4d09`; stdout SHA-256 is `076f2fce8c10a152bb457dc463b1cd2cc1bc24e3fad0939be34c97f7e107b1f1`. The full absolute command appears in the receipt.

The run checked 1,485 finite fixtures by an exact interval sweep, including 21,327 interval cells/endpoints, 1,470 boundary-membership comparisons and 113 cases with `2delta=gap`. It computed the entire 1,024-outcome probability vector by direct finite sums for the close-boundary control. The precision test computed one coefficient at each stated finite dimension. Large `M` values in the moving-family certificate are rational resource/grid calculations; no enormous register or full circuit was allocated. Incorrect closed-strip endpoints, the weaker proposed condition `delta<=gap`, and the nominal-margin probability bound were explicitly rejected by calculated discrepancies. A changed expected source hash was rejected without modifying any source file.

The written argument proves the general finite membership condition and the conditional convergence implication. Finite enumeration and floating Fourier sums are controls of that argument, not proofs of all real parameters, unbounded spectral calculus, or a physical realization. The phase-sum trigonometric lower bound is analytic. No Lean formalization was attempted. This was one inherited-model worker context, exposed to the prior review and its original close-boundary example. Its separate interval and direct-sum implementation is not a blind derivation or an independent retained audit. The previous review's receipt was inspected as historical evidence; its runner was not rerun and its complete output stream was not recertified here.

No new consequential defect in the scoped endpoint bound was found. The lower-endpoint wording requires the same union qualification described in section 2.1. Broader common-H, kinetic, compiler and physical-realization results were not re-reviewed. The existing infinite common-H identification is preserved and is not relabeled as absent by this addendum. An identification of H and an implementation with its controlled oracle, register, preparation and graph-error resources remain distinct assertions. This precision correction supplies no new physical realization, physical axiom, broad impossibility claim, N-gate result or audit status.

## 8. Final recovery checkpoint and next decision

Completed: exact finite bad-set criterion, proposed replacement text, finite-precision convergence condition, fixed/moving quantifiers, proof and explicit counterexamples, disjoint finite check with complete streams. All five sealed source hashes matched before and after the run. Source changes detected: none.

Supervisor handoff: inspect this addendum and the exact proposed wording before carrying it into any publication candidate. The sealed originals, publication packages and worktree were not edited. No Git writes, commits, pushes, merges, external application writes or audit actions were performed. Editable prompt files changed: **none**. This addendum is the current checkpoint; no further mathematical task is pending in this bounded dispatch.

<!-- END SOURCE D -->


<!-- BEGIN SOURCE E sha256=9179660b1c247a99c6e3abc03203fb1bf125d70226c0d8c6b5257b696fc09118 -->

## Source E: Finite-chain apparatus corrected v3

Original: `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261013_213733/crash_recovery_01a13807/finite_apparatus_composition/DERIVATION.md`. Complete immutable body follows.

# Conditional finite-chain apparatus composition

Status: positive conditional research theorem. A separate source-exposed review
supports C1–C11; this revision makes the reviewed notation and effective-data
clarifications explicit. No retained audit or native physical realization is
claimed. The reviewed original and receipt are preserved in history/.

This note connects the supplied finite-chain comparison to the supplied local
compiler. It gives an explicit finite readout accuracy prescription at each
chosen volume. It does not supply the volume needed to approximate the infinite
chain, or an efficient algorithm, autonomous apparatus, or framework-derived
state/control/readout law.

## 1. Sources, exposure and premises

All paths in this section are relative to
`/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261013_213733`.

- `finite_open_chain_independent/CANDIDATE.md`, SHA-256
  `13fd167efa195fd672fa37e5f3562059bdd76ad373686ef88cde65a02cdfcb10`,
  complete 565-line argument read. This supplies the conditional open-chain
  Fock identification, preparation, and fixed-protocol volume comparison.
- `coarse_energy_instrument_independent/REPORT.md`, SHA-256
  `6d534a7c409c1af1e1bb34199a1d35977ca1c5393f4bbe165bd301fe501dbdfe`,
  complete 820-line argument read. Use its actual controlled-energy circuit,
  fibre identity, phase tail, and weighted Hilbert--Schmidt argument, with the
  endpoint precision correction below. Its own no-go scope is not promoted.
- `coarse_energy_instrument_root/DERIVATION.md`, SHA-256
  `aa8349482e636744d001946cf2531d83f12d79847e3d025c35d657f4d6d093a8`,
  complete argument read, especially the finite local compiler in section 8.
- Complete exposed reviews read: `local_instrument_compiler_review/REVIEW.md`,
  `coarse_energy_endpoint_review/REVIEW.md`, and the new
  `crash_recovery_01a13807/finite_chain_review/REPORT.md` and
  `crash_recovery_01a13807/endpoint_precision/PRECISION_ADDENDUM.md`.
  Exact identities are recorded in the sibling source receipt. Some initial
  displays truncated; their missing ranges were subsequently read in full.

The already existing infinite-chain energy-adapted/Fock map is an upstream
conditional input, not a new result here. The science/planning revisions used
are main `583c699e859b64ff01c8bc92d1c04bdfe9994509` and instructions
`3a4b2c66a1ead7a1c48b4359627e968f681e3c39`; the pinned scientific parent is
`ccbeddd0c04b70ee2b6c5f1cffeeeefa23df2989`. This is an exposed composition of
read arguments, with no claim of a blind derivation or independent model family.

Fix g>J>0. For an interval of L>=2 spins use exactly the candidate's

    Hspin_L = -sum_x d_x Z_x - J sum_(x=1)^(L-1) X_x X_(x+1),
    g/2 <= d_1,d_L <= g,    d_x=g in the interior,
    K_L = Hspin_L + c_L I >= 0,    c_L = Tr |T_L|,
    T_L = diag(d_x) - J S_L,    e_L=2|T_L|.

The endpoints and energy zero are part of the model and cannot be silently
changed. The candidate's even unitary C_L identifies K_L with dGamma(e_L).
Let W_L=Gamma(i_L)C_L be its isometry into F(l2(Z)); its range is
F(Pi_L l2(Z)). Write A=1+N and A_L=1+N_L in that carrier. All weights below
act trivially on apparatus registers, classical records, and references.

Supplied apparatus premises: finitely many fresh pure auxiliary qubits;
signed switchable local controlled term gates; local ancillary gates with
stated norm precision; a finite connected bus/auxiliary geometry permitting
their routing; a controlled scalar phase; a clock and schedule that account
for the system drift and any drive during the readout; coarse-register
dephasing and discarding of declared ancillary systems. No reset of an unknown
or approximately blank register is assumed. These remain physical premises.

When the finite-input statement F23 of the candidate is used as an actual
finite-chain preparation, impose explicitly

    ran S_L subset ran Gamma(Pi_L) tensor Q'.                (C1)

This ensures W_L^* converts the prepared carrier state into a finite physical
state. F23 as an abstract comparison on the common infinite carrier does not
itself ensure (C1). The candidate's vacuum and finite local-control examples
do satisfy (C1); its concrete ground-preparation proof requires no repair.

## 2. A finite spectrum prescription that includes boundary atoms

Fix a finite partition with internal boundaries 0<b_1<...<b_m; the bins are
left closed and right open, with the last extending to infinity. The m=0
readout is the identity and needs no phase circuit. Otherwise let

    B_L = c_L + sum_x d_x + J(L-1) <= 2L(g+J),
    Spec_L = spectrum(K_L) subset [0,B_L],
    Delta_L = min { b_j-E : E in Spec_L, E<b_j, 1<=j<=m }.

The displayed minimum is positive: the finite set is nonempty because 0 is
in Spec_L and b_1>0. Let d_min be the smallest adjacent internal-boundary
spacing, or infinity if m=1. Select finite certified numbers satisfying

    R_L > B_L,
    0 < delta_L < min(R_L,b_1/2,Delta_L/2,d_min/2),
    0 <= kappa_L <= delta_L/2.                               (C2)

The condition involving infinity is omitted. One may use any certified lower
bound for Delta_L instead of computing its exact value. Choose ordered encoded
thresholds t_j=b_j-delta_L+epsilon_j, |epsilon_j|<=kappa_L. They are strictly
ordered since a gap changes by at most 2kappa_L<=delta_L<d_min/2.

The phase circuit of the independent report uses period P_L=4R_L and grid
e_y=P_L y/M-R_L for M=2^q. Classify by the number of thresholds t_j<=e_y.
This changes the classifier, not the target spectral bins. The one-sided bad
strips D_delta=union_j(b_j-2delta_L,b_j) contain no point of Spec_L: every
energy below b_j is separated by at least Delta_L>2delta_L. An energy exactly
at a boundary is handled by that threshold's closed-side convention; the
same separation argument excludes it from every higher boundary's strip.
There is also no spectral tail above R_L.

Put r_L=delta_L-kappa_L>=delta_L/2. The endpoint correction proves, for each
E in Spec_L,

    p_L(E) <= beta(M r_L/P_L),
    beta(h) = min(1,(h^-1+h^-2)/2) <= 1/h for h>=1.          (C3)

Here p_L(E) is the wrong-label probability of the coherent phase classifier.
Given any desired 0<a_L<=1, choose a power of two M>=4 with

    M r_L/P_L >= 2/a_L^2.                                  (C4)

Then the exact compute/copy-coarse/uncompute isometry V_L and ideal coarse
isometry J_L satisfy ||V_L-J_L||<=a_L, by the fibre identity
||V_L(E)-J_L(E)||^2=2p_L(E). Each oracle entry is a function of K_L and hence
commutes with N_L in the diagonalized finite representation. Therefore for
every real s>=0 the same bound holds in the number graph norm:

    ||(A_L^s tensor I)(V_L-J_L)A_L^-s|| <= a_L.             (C5)

Neither fine energy measurement followed by binning nor retaining a fine
archive may replace this coherent circuit. Their postmeasurement states
can differ even when the bin probabilities agree.

The prescription is finite for each L and any fixed real supplied spectrum.
Its *computability* requires more. One sufficient version assumes g,J,d_x and
the b_j are specified real algebraic numbers, with exact algebraic arithmetic
and order tests. The finite spin matrix then has algebraic eigenvalues;
subtracting its algebraic ground energy gives Spec_L. Comparing finitely
many algebraic numbers computes a positive rational lower bound for Delta_L,
including exact equality cases. Rational R_L, delta_L and encoded thresholds
can then be certified, and the finite label table can be evaluated exactly.
This argument may enumerate 2^L energies and has no efficiency claim. Arbitrary
unspecified real parameters do not supply an effective spectral-separation
oracle. The alternative premise is simply a certified finite separation/table.

For a fully executable resource prescription, take rational accuracy tolerances
and a computable exponent s, and choose a certified rational amplification
bound Wcost_L>=(1+L)^s. Alternatively, a supplied integer S>=s permits the
exact choice Wcost_L=(1+L)^S. Use the same chosen bound throughout the
compiler and gate-error budgets below. For the nonnegative quantity x_j
inside the ceiling in (C7), choose a certified nonnegative rational upper
bound U_j>=x_j and set n_j=max(1,ceil(U_j)). Its separate count bound is
stated below; exact equality testing for the ceiling of a general computable
real is unnecessary. Approximate every prescribed gate to its allocated
share of the finite norm-error budget.
These effective-data conditions concern an algorithmic version; they do not
change the finite-resource existence proof for the stated supplied real data.

## 3. Replacing the global oracle by local gates

There are D_L=2L-1 non-scalar Pauli terms h_l in K_L. Their exact pairwise
commutator sum is

    Ccomm_L = sum_(l<k)||[h_l,h_k]||
        = 2J sum_(x=1)^(L-1)(d_x+d_(x+1))
        <= 4gJ(L-1).                                      (C6)

All onsite terms commute with each other; all XX bonds commute with each
other; only the two onsite incidences of each bond contribute 2Jd_x.
The scalar cost Ccomm_L is distinct from the diagonalizing unitary C_L.

Let tau=2pi/P_L, t_j=tau 2^j, j=0,...,q-1. The reviewed controlled product
formula approximates each query with error <=t_j^2 Ccomm_L/(2n_j). Scalar
c_L phases are included. The inverse query circuit is the literal adjoint
of the approximate forward circuit. Thus its full isometry error is at most
sum_j t_j^2 Ccomm_L/n_j. Choose Wcost_L>=(1+L)^s and use that same value
everywhere below; the minimal theoretical choice is (1+L)^s. Given zeta_L>0,
the exact prescription is

    n_j=max(1,ceil(q Ccomm_L t_j^2 Wcost_L/zeta_L)).           (C7)

If Ccomm_L=0 the product is exact and n_j=1 suffices. Otherwise telescoping
and ||A_L^s||<=Wcost_L, ||A_L^-s||<=1 imply

    ||(A_L^s tensor I)(Vproduct_L-V_L)A_L^-s|| <= zeta_L.     (C8)

Let gamma_L be the sum of norm errors of the *entire* implemented finite
circuit relative to this intended product circuit: count ancillary Fourier,
lookup, controlled scalar, bus, routing and term gates in both directions.
An independently implemented approximate inverse is permitted only when its
errors relative to the prescribed adjoint list are included in gamma_L.
The further graph error is <=Wcost_L gamma_L. Consequently

    eps_L=a_L+zeta_L+Wcost_L gamma_L,
    ||A_L^s(Vactual_L-J_L)A_L^-s|| <= eps_L,
    ||A_L^s Vactual_L A_L^-s|| <= 1+eps_L.                 (C9)

All isometries include the same initialized auxiliary spaces; a clean ideal
bus is padded into J_L. Faulty bus clearing is covered only insofar as the
actual total circuit has the stated norm error. No energy conservation is
claimed for the compiled circuit.

For a positive input rho on finite chain plus arbitrary passive reference,
write M_L(rho)=Tr[(A_L^(2s) tensor I)rho]. Hilbert--Schmidt factorization and
||XX*-YY*||_1<=(||X||_2+||Y||_2)||X-Y||_2 give the full CQ instrument bound

    ||(A_L^s tensor I)[Phi_L(rho)-Lambda_L(rho)]
                          (A_L^s tensor I)||_1
       <= (2+eps_L)eps_L M_L(rho).                        (C10)

Common partial traces and coarse dephasing contract the Hermitian trace
norm and commute with the weight. The implemented channel's weighted
Hermitian trace norm is at most (1+eps_L)^2. The estimate is uniform over
all reference systems and all finite-chain inputs with bounded M_L.
Finite dimension is crucial in the Wcost_L conversion; it is explicitly
paid as L grows.

If the binary label register has unused codes, compare on the same padded
record space, with zero ideal probability there. A fixed classical map can
assign unused codes to a declared valid label without increasing the error.
Any future feedback protocol must specify the action on those codes; (C11)
only uses the fixed intervening drives already stated.

For the exact (C7) prescription, an explicit logical resource upper bound is

    2q controlled queries; total |oracle time|=2tau(M-1);
    2D_L sum_j n_j controlled local term gates;
    sum_j n_j <= q + q Ccomm_L Wcost_L tau^2(M^2-1)/(3zeta_L);
    4q(Vbus-1) bus fanout/unfanout CNOTs;
    M[2(q-1) Toffolis + ell CNOTs + 2q X gates]
        for the literal finite lookup, ell=ceil(log2(m+1));
    two Fourier transforms, 2q Hadamards, controlled scalar/offset phases.

For the effective rational-upper-bound prescription, replace only the
displayed substep inequality by sum_j n_j<=q+sum_j U_j. This follows from
max(1,ceil(U_j))<=1+U_j for U_j>=0. The actual controlled local term count
is still 2D_L sum_j n_j, and (C8) still follows because n_j>=x_j. Arbitrary
conservative rounding does not inherit the smaller exact-(C7) count bound.

Lookup uses q-1 clean scratch bits. Readout dephasing may be represented by
ell additional fresh environment bits, ell copy CNOTs and environment trace.
Alternatively dephasing is an explicitly supplied primitive. Fine registers
and records are fresh at each intervention. The bus and Boolean scratch
are reusable only after their specified uncomputation. These logical counts
exclude the geometry-dependent routing of auxiliary gates, physical pulse
times, heat/reset work and clock resources; they are not a full energy ledger.

## 4. Composition with the finite-volume comparison

At fixed g,J, s and fixed finite protocol, import only the actual theorem
scope of the finite-chain candidate: matched inputs obey weighted trace
convergence, satisfy (C1) when physically prepared, and the supplied finitely
many even local drives have uniform A^s graph bounds. Ideal finite-chain
coarse histories then converge in weighted trace to the infinite target.

Replace readout j by the compiled channel above with error eps_(L,j).
Let sigma_(L,j) be the *ideal finite-chain* state just before readout j,
retaining earlier records, let M_(L,j)=Tr A^(2s)sigma_(L,j), and let
ell_(L,k)=||A^s U_(L,k) A^-s|| for the intervening drive from readout k to
k+1. A final drive has its own identical suffix factor if present. Channel
telescoping, ideal past and implemented future, gives

    weighted error of actual versus ideal finite histories
    <= sum_(j=1)^n (2+eps_(L,j))eps_(L,j) M_(L,j)
          product_(k=j+1)^n (1+eps_(L,k))^2
          product_(k=j)^(n-1) ell_(L,k)^2.                 (C11)

Use the common output carrier W_L, tensored with record and reference
identities. The candidate bounds M_(L,j) and ell_(L,k) uniformly in L for
its fixed protocol and matched input. Thus choosing max_j eps_(L,j)->0
makes (C11) tend to zero. Triangle inequality with its ideal volume limit
proves convergence of the implemented finite histories to the supplied
infinite coarse histories in the same weighted full-output topology.

At s=1/2, finite first number is equivalent to finite first energy using
the uniform positive gap and upper one-particle bound. This is an operator
comparison on particle sectors; no noncommutative power-monotonicity is
being assumed. The native spatial continuum map remains the existing
energy-adapted map with its own supplied hypotheses, not a locality theorem
for that map. No uniformity in shrinking a, shrinking gap, growing number of
interventions, kinetic time or all infinite-volume energy-bounded inputs is
obtained from this fixed-parameter theorem.

One simple accuracy schedule is a_L=zeta_L=u_L/3 and
gamma_L<=u_L/(3 Wcost_L), for any 0<u_L<=1 tending to zero; (C4), (C7) and
the finite supplied gate precision make eps_L<=u_L. This prices apparatus
accuracy *after a volume is selected*. The infinite-to-finite volume error
is still the separate quantitative obligation. At each fixed kinetic
parameter one may choose a volume and then apparatus resources, but no
computable joint kinetic rate follows from that diagonal existence alone.

## 5. Verification obligations and nonclaims

The complete original C1–C11 argument received the separate source-exposed
review at ../finite_apparatus_composition_review/REPORT.md. No consequential
mathematical error was found. This revision renames the compiler allowance
zeta_L so it cannot be confused with the right endpoint field d_L, names the
commutator scalar Ccomm_L consistently, and states the effective-data and
unused-code qualifications. A narrow revision review then identified two
accounting gaps in the effective-data alternative: arbitrary upper rounding
need not satisfy the exact-ceiling resource count, and an enlarged Wcost_L
must also be used in the final gate-error budget. Both are corrected above,
with the separate rational-upper-bound count and a consistent Wcost_L budget.
The original exact C1–C11 bounds and physical model are unchanged. The original
and intermediate revisions, including the review that found these gaps,
remain preserved.

That review performed one disjoint two-spin full-circuit check, with exact
boundary eigenvalues and a maximally entangled passive reference. The full
weighted CQ error was approximately 0.01516 against the sufficient bound 3.12.
Omitting the controlled ground shift produced approximately 3.91329 and was
detected. The floating isometry residual was about 1.06e-8 at a 1e-5 diagnostic
tolerance. Full code, output and receipt are preserved beside the report.
These finite results check a consequential calibration failure; the analytic
argument, not the numerical fixture, supplies C1–C11. No supervisor rerun,
Lean formalization, native experiment or retained audit is claimed here.

All resource assumptions remain explicit. The construction neither derives
the supplied one-dimensional model from the framework, nor selects its
state, controls, Born probabilities, durable records, autonomous timing,
three-dimensional placement, interacting channels or empirical parameters.
It makes no universal negative claim about alternative realizations.
No original source, axiom, audit authority, editable prompt or Git state is
changed by this note. Packaging into a source milestone is a later decision.

<!-- END SOURCE E -->


<!-- BEGIN SOURCE F sha256=8fc3f3255db941288993e13afa6cef9b35d52804595fc26b75bcb7b841b72dea -->

## Source F: Finite-particle one-readout volume modulus

Original: `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261013_213733/crash_recovery_01a13807/finite_volume_modulus/DERIVATION.md`. Complete immutable body follows.

# A computable volume modulus for one coarse-energy Lüders readout

Provisional conditional theorem and source-exposed analytic derivation. The proof below is new work in this bounded task; it has not received independent acceptance or a formal audit. It concerns one readout on fixed finite mode/particle support. It does not establish the driven kinetic protocol, an apparatus implementation, or an infinite-input energy-constrained diamond estimate.

The result is an explicit boundary-strip-dependent bound for the complete recorded quantum instrument, stable under every passive reference. In the stated finite-support class, a conservative fully explicit specialization tends to zero as the distance to the open boundary to the power -1/6. The exponent and constants are not claimed optimal.

## 1. Exact sources, exposure, and supplied interface

The full 565-line finite-chain candidate was read at SHA-256
`13fd167efa195fd672fa37e5f3562059bdd76ad373686ef88cde65a02cdfcb10`:
`/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261013_213733/finite_open_chain_independent/CANDIDATE.md`.
Its F3–F12 positive-Fock representation, exact ground shift, and actual finite-energy PVM identity are supplied inputs. F16–F24 provide the qualitative predecessor, not a quantitative estimate used as proof here. The complete recovery review was also read; its source hash is inserted at the end. In particular, its escaping boundary modes and finite physical-range qualification are preserved.

Scientific parents are pinned at `ccbeddd0c04b70ee2b6c5f1cffeeeefa23df2989`. The exact infinite-chain common-energy embedding already exists. Its source passages read here were ENERGY_ADAPTED_REFINEMENT lines 1–215, especially E6–E11, and CALIBRATED_ENERGY_TRANSFER lines 1240–1320, especially the actual Fock-domain and PVM interface in section 5. Their complete-file hashes are recorded below. No new reading or certification of the rest of these parents, their external theorems, or all scientific ancestors is claimed. The finite-spin diagonalization is not rebuilt here.

The operating instructions are the already read main `583c699e859b64ff01c8bc92d1c04bdfe9994509` SCIENCE_WORKFLOW/workhorse sources and planning AGENTS `3a4b2c66a1ead7a1c48b4359627e968f681e3c39`, reused at unchanged identities. The inherited model and effort were retained. The initial combined source display was truncated; bounded follow-up reads completed the candidate. No prior finite-volume modulus proof was supplied or read. No other agent, numerical runner, Git/PR action, source edit, audit/status change, physical axiom, or prompt edit was used. Only this assigned output file was written.

## 2. Quantified input and actual finite readout

Fix g>J>0. On h=ell²(Z), let S be the right shift and

    T=gI-JS,       e=2(T* T)^(1/2),       H=dGamma(e),
    C=2(g+J),      h0=H/C.

On a finite interval Lambda=[l,r], use the candidate's open matrix

    T_Lambda=diag(d_x)-J S_Lambda,

where interior fields equal g and each endpoint field lies in [g/2,g]. Endpoints may vary with Lambda. Thus the estimate covers both full onsite fields and the literal half-endpoint bond-density cutoff, without equating their finite spectra. Extend it to h by

    That_Lambda=i_Lambda T_Lambda i_Lambda*+g(I-Pi_Lambda),
    ehat_Lambda=2(That_Lambda* That_Lambda)^(1/2),
    Hhat_Lambda=dGamma(ehat_Lambda),  hLambda=Hhat_Lambda/C.

The exterior modes are bookkeeping and are not populated. The source's exact isometry W_Lambda maps the actual spin energy K_Lambda=Hspin_Lambda-E0_Lambda to Hhat_Lambda on its reducing finite-mode Fock range, and intertwines every Borel spectral projection. This is the actual finite-energy readout, not a replacement by H before the limit.

Let S0 be a fixed nonempty finite set of sites, M=|S0|, and let the fixed input space Q be a subspace of

    direct sum from n=0 to n_* of wedge^n ell²(S0),   1<=n_*<=M.

Write P_Q for its orthogonal projection. Superpositions of particle sectors are allowed. Choose Lambda containing S0 and set

    d=min(min(S0)-l, r-max(S0)) >= 1.

Thus d is the clearance in lattice steps from every populated input mode to either endpoint. It is not the distance to the support of the matrix perturbation. The proof reserves the conservative inner interval [l+2,r-2] and uses polynomial degrees only through d-1; the adjacent half-field offdiagonal change is included in that buffer. Q lies in the actual finite physical range Gamma(Pi_Lambda)F for every such Lambda. The matched actual input is the pullback by W_Lambda*, including any passive reference. This explicitly supplies the finite-range condition highlighted by the recovery review. It does not claim that arbitrary local-spin preparations produce this exact Q.

Fix m>=1 positive bin boundaries 0<b_1<...<b_m<infinity and one fixed convention for assigning boundary eigenvalues. For definiteness use cumulative projectors

    L_j=1_(-infinity,b_j](H),
    L_Lambda,j=1_(-infinity,b_j](Hhat_Lambda).

Differences of consecutive cumulatives, with endpoints 0 and I, form the m+1 coarse bins. If the supplied apparatus instead uses left-closed/right-open bins [b_j,b_(j+1)), replace every cumulative above by 1_(-infinity,b_j), at both finite and infinite volume. Every estimate below is unchanged: equality at b_j remains inside the charged boundary strip. The endpoint convention is fixed across the comparison; this is not permission to swap finite instruments. A separately recorded singleton vacuum is also allowed: it is identical at every volume and contributes zero to the difference. The proof allows finite-volume atoms exactly on b_j. Put beta_j=b_j/C.

For a density rho on Q tensor an arbitrary passive reference R, the compared outputs are

    M_Lambda(rho)=sum_z |z><z| tensor
         (P_Lambda,z tensor I_R) rho (P_Lambda,z tensor I_R),
    M(rho)=sum_z |z><z| tensor
         (P_z tensor I_R) rho (P_z tensor I_R).

All unnormalized blocks and the complete postmeasurement system/reference are retained. This is the coarse Lüders instrument itself; it is not fine-energy measurement followed by forgetting a label.

## 3. Explicit locality constants

Set

    mu=(g-J)^2/[16(g+J)^2],
    r0=1-mu,        rho0=(1+r0)/2,
    q=r0/rho0<1,   kappa=-log q>0,
    v=sqrt(1+rho0), K=2 n_*/[pi(1-q)].                 (1)

These deliberately conservative constants are uniform over the allowed endpoint fields. For full onsite fields one may improve mu, but no such improvement is used.

For an auxiliary Fourier cutoff tau>0 define

    xi(d,tau)=min{1, K q^d [exp(v tau)-1]}.           (2)

This tau is a functional-calculus parameter. It is not a physical readout duration or a drive time.

To prove (2), first normalize the one-particle squares:

    A=T* T/(g+J)^2,       A_Lambda=That_Lambda* That_Lambda/(g+J)^2,
    X=I-A,               X_Lambda=I-A_Lambda.

The inverse-entry formula of the triangular T_Lambda gives

    |(T_Lambda^-1)_(x,y)| <= (4/g)(J/g)^(x-y), x>=y,
    ||T_Lambda^-1|| <=4/(g-J).

The same bound covers the exterior gI. Also ||That_Lambda||,||T||<=g+J. Therefore both A and A_Lambda have spectra in [mu,1], and X,X_Lambda have spectra in [0,r0]. This is where the fixed positive gap enters; no assertion is uniform as g-J tends to zero.

Both square operators are tridiagonal. The finite block has diagonal d_x²+J² except for the last entry d_r², and offdiagonal -J d_(x+1). In particular a half-field right endpoint changes the (r-1,r) and (r,r-1) entries as well as the endpoint diagonal; those entries cannot be treated as bulk. The difference X_Lambda-X annihilates every vector supported in the conservative interval [l+2,r-2], at distance at least two from the endpoints. Nearest-neighbor support propagation then gives, for every k=0,...,d-1,

    X_Lambda^k P_S0 = X^k P_S0.                      (3)

Indeed in the telescoping identity for kth powers, X^j P_S0 has support at distance at least d-j>=2 whenever the difference operator occurs. The degree-zero case is exact even when d=1.

On |z|=rho0, the principal square root is analytic and has modulus at most v. Cauchy's coefficient estimate applied to

    G_t(z)=exp(it sqrt(1-z))-1

gives |coefficient_k G_t| <= |t|v exp(v|t|) rho0^(-k). Truncate at degree d-1 and use (3). Each spectral tail is bounded by a geometric series, so

    ||[exp(it ehat_Lambda/C)-exp(it e/C)]P_S0||
       <= 2 v |t| exp(v|t|) q^d/(1-q).              (4)

The subtraction of 1 in G_t matters: it supplies the factor |t| needed at the origin in the later integral. This proof uses no global operator-norm convergence of finite energies.

On the n-particle sector the free group is the nth exterior tensor power. Tensor-product telescoping costs at most n times (4) on wedge^n ell²(S0); other tensor factors are unitary. Direct-sum orthogonality costs at most n_* rather than a sum over sectors. Consequently

    ||[exp(it hLambda)-exp(it h0)]P_Q||
       <= 2 n_* v |t| exp(v|t|) q^d/(1-q).          (5)

All subsequent functional calculus may be performed on the common invariant subspace N<=n_*. Both normalized energies are bounded there by n_*, so no unbounded-operator integral or domain interchange is required.

## 4. Spectral smoothing and finite-volume strip control

Use the integrated Fejér kernel

    F_tau(x)=1/2+(1/pi) integral_0^tau
                    (1-t/tau) sin(tx)/t dt.          (6)

Its derivative is

    F_tau'(x)=[1-cos(tau x)]/[pi tau x²],

with the continuous value tau/(2pi) at zero. The derivative is nonnegative, its integral is one, and F_tau(-infinity)=0, F_tau(infinity)=1. Hence 0<=F_tau<=1. For x>=delta>0,

    1-F_tau(x)=F_tau(-x)<=a,
    a=2/(pi tau delta).                              (7)

The bound follows by integrating 2/(pi tau x²). No smooth density assumption has entered.

For any real u, (5) and the sine/exponential identity give

    ||[F_tau(u-hLambda)-F_tau(u-h0)]P_Q||
       <= (1/(2pi)) integral_0^tau (1-t/tau)/t
            [ ||[exp(it hLambda)-exp(it h0)]P_Q||
             +||[exp(-it hLambda)-exp(-it h0)]P_Q|| ] dt
       <= K q^d [exp(v tau)-1].                     (8)

Equation (5) gives the same common majorant for both signs of t; it does not assert that the two restricted operator norms are equal. The factor 1/2 in sine cancels the two copies of that majorant. The additional cap one in (2) is valid because both functions are positive contractions. The same estimate holds for F_tau(hLambda-u)-F_tau(h0-u).

For each boundary define its actual target-input strip mass

    B_j(delta)=||P_Q 1_{|h0-beta_j|<=delta} P_Q||.    (9)

This is the required input dependence. It is not replaced by an assumption that the finite-volume spectrum misses the boundary.

Fix delta>0 with a<1/2. To bound the finite-volume strip, use

    G_j(x)=F_tau(x-beta_j+2delta)
                        -F_tau(x-beta_j-2delta).

This scalar function lies in [0,1]. On |x-beta_j|<=delta it is at least 1-2a. Outside |x-beta_j|<=3delta it is at most a. Therefore spectral calculus and (8) imply

    B_Lambda,j(delta)
      :=||P_Q 1_{|hLambda-beta_j|<=delta}P_Q||
      <= Btilde_j
      :=min{1, [B_j(3delta)+a+2xi(d,tau)]/(1-2a)}.    (10)

To see the operator estimate explicitly, the scalar inequality gives the finite strip projection <=G_j(hLambda)/(1-2a). After compressing to Q, the difference from G_j(h0) has norm at most 2xi; the target compressed G_j is bounded by B_j(3delta)+a. No application of locality to L_j Q, whose vectors need not be finitely supported, is made.

For f_j(x)=F_tau(beta_j-x), the cumulative indicator and f_j differ by at most a away from the delta strip and by at most one inside it. Thus

    ||[L_Lambda,j-f_j(hLambda)]P_Q||
                      <=sqrt(Btilde_j+a²),
    ||[L_j-f_j(h0)]P_Q||<=sqrt(B_j(delta)+a²).

Inserting the smoothed comparison gives the computable boundary-dependent estimate

    ||(L_Lambda,j-L_j)P_Q|| <= theta_j,
    theta_j=min{1, sqrt(Btilde_j+a²)+xi(d,tau)
                                      +sqrt(B_j(delta)+a²)}. (11)

The cap one uses the norm bound for a difference of orthogonal projections. Equations (9)–(11) are valid with the exact input strip masses even before specializing to finite Fourier support. They tolerate arbitrary finite spectral degeneracies and boundary eigenvalues.

## 5. Full instrument and arbitrary reference

Let the coherent record isometries be

    J_Lambda psi=sum_z |z> tensor P_Lambda,z psi,
    J psi=sum_z |z> tensor P_z psi.

Put D_j=L_Lambda,j-L_j and D_0=D_(m+1)=0. Every bin difference is D_j-D_(j-1), up to indexing. Hence for psi in Q,

    ||(J_Lambda-J)psi||²
      =sum_z ||(P_Lambda,z-P_z)psi||²
      <=4 sum_(j=1)^m ||D_j psi||².

It follows that

    ||(J_Lambda-J)P_Q||<=2 [sum_j theta_j²]^(1/2).    (12)

For every trace-class input X on Q tensor R, insert and subtract one cross term in J_Lambda X J_Lambda* - J X J*. The two isometries have norm one, and tensoring a bounded operator with I_R leaves its norm unchanged. The trace ideal inequality gives an upper bound 2||(J_Lambda-J)P_Q|| ||X||_1. Dephasing the displayed finite record register is completely trace-norm contractive. Therefore

    ||M_Lambda(rho)-M(rho)||_1
       <= Delta(d;tau,delta)
       :=min{2, 4 [sum_(j=1)^m theta_j²]^(1/2)}.     (13)

This holds uniformly over all normalized rho on Q tensor every passive R. The same derivation gives the diamond norm between the two channels whose input is Q, with this bound. It does not replace Q by all infinite-volume states below an energy cap.

The entire postmeasurement state is controlled: within-bin coherences, cross-system/reference correlations, and outcome probabilities are all included. Since readout preserves particle number, both outputs remain in N<=n_*. For s>=0, a number-weighted trace error with weight (1+N)^s on each output side is therefore at most (1+n_*)^(2s) Delta. A common-H weight (1+H)^s costs at most (1+C n_*)^(2s). No own-energy weighted comparison between different output weights is asserted here.

## 6. A fully explicit strip bound for the stated Q

No extra density regularity is needed for the fixed finite-mode input class. Under the unitary Fourier transform to L²([-pi,pi],dk/(2pi)), the normalized one-particle dispersion is

    eps(k)=sqrt(g²+J²-2gJ cos k)/(g+J),
    (g-J)/(g+J)<=eps(k)<=1.

For any real u and delta>0, write the clipped energy window endpoints as y_-<=y_+ within this band. If nonempty, y_+-y_-<=2delta. On k in [0,pi], eps is increasing. The corresponding cosine coordinates differ by

    |cos(k_+)-cos(k_-)|
      = (g+J)²(y_+²-y_-²)/(2gJ)
      <=2(g+J)² delta/(gJ).

For 0<=k_-<=k_+<=pi, the elementary cosine identity gives

    |cos(k_+)-cos(k_-)| >=2 sin²((k_+-k_-)/2).

Using arcsin(t)<=pi t/2 on [0,1] therefore gives the normalized torus measure bound

    measure{ k: |eps(k)-u|<=delta }
       <=min{1, gamma sqrt(delta)},
    gamma=(g+J)/sqrt(gJ).                            (14)

This retains the possible square-root band-edge singularity. No uniformly bounded density of states has been assumed.

For n>=1, fix k_2,...,k_n. A strip for sum_i eps(k_i) leaves a window of width 2delta for eps(k_1). Fubini and (14) therefore bound the product-torus measure of every n-particle energy strip by the same right side of (14).

For a normalized wavefunction in wedge^n ell²(S0), its Fourier values satisfy

    |psi_n(k_1,...,k_n)|² <= M^n/n!.                  (15)

Proof: use the orthonormal Slater basis with wavefunctions det(exp(-ik_i x_j))/sqrt(n!). Cauchy–Schwarz in the Slater coefficients bounds evaluation by the sum of squared basis values. Cauchy–Binet identifies that sum with det(A A*)/n!, where A_(i,x)=exp(-ik_i x), x in S0. The positive Gram matrix has every diagonal entry M; Hadamard's determinant inequality gives (15). For an unnormalized sector multiply by its squared norm.

Set

    K_S=max_(1<=n<=n_*) M^n/n!,       A_S=K_S gamma.   (16)

If 0<delta<min_j beta_j, the strip does not contain the vacuum. Orthogonality of the particle sectors and (14)–(15) imply, for the actual Q,

    B_j(delta)<=min{1, A_S sqrt(delta)}.              (17)

This estimate is uniform over every subspace Q in the specified finite mode/particle carrier. For a particular Q it can be very loose. Sharper values in (9) can be obtained from its finite matrix of spectral integrals of Slater trigonometric polynomials. Equations (14)–(17) already give a certified upper bound without relying on uncertified quadrature of a discontinuous indicator.

## 7. Explicit volume choice and conservative rate

For n_*=0 (vacuum input only), or a partition with no positive boundary, the instruments agree exactly. Otherwise use (1) and set

    tau_d=kappa d/(2v),
    delta_d=tau_d^(-2/3),
    a_d=(2/pi) tau_d^(-1/3),
    xibar_d=K exp(-kappa d/2).                        (18)

Take d large enough that

    tau_d>=64,
    delta_d<=min_j beta_j/6.                         (19)

The second condition keeps even the triple-width strips away from the vacuum. Now a_d<1/2, and (2) is bounded above by xibar_d. Insert

    B_j(delta_d)<=A_S tau_d^(-1/3),
    B_j(3delta_d)<=sqrt(3) A_S tau_d^(-1/3)

into (10)–(13). This is an explicit finite-volume modulus using only g,J, the support/cardinality and particle cutoff, the fixed boundaries, and d.

For an uncluttered explicit envelope, put

    D0=1-1/pi,
    B0=sqrt[(sqrt(3) A_S+2/pi)/D0+4/pi²]
                            +sqrt[A_S+4/pi²].

Under (19), 1-2a_d>=D0 and tau_d>=1. Elementary square-root subadditivity in (11) yields

    Delta(d) <= min{2, 4 sqrt(m) [
       B0 (2v/(kappa d))^(1/6)
       +sqrt(2K/D0) exp(-kappa d/4)
       +K exp(-kappa d/2) ]}.                        (20)

Thus the full reference-stable instrument error is

    O_(g,J,S0,n_*,m,boundaries)(d^(-1/6)).             (21)

This is a sufficient rate, not an optimal asymptotic claim. The constants can be extremely large near the closing gap, for small J, or for large input support/particle cutoff.

Given tolerance eta>0, choose an integer d satisfying (19) and enlarge it until the explicit right side of (20) is <=eta. Termination follows from the displayed formula. One valid interval is

    [min(S0)-d, max(S0)+d],
    number of sites = max(S0)-min(S0)+1+2d.           (22)

For numerical implementation, supplied real parameters need validated numerical enclosures and positive gap/boundary margins; rational interval overestimates may be substituted throughout. The formula itself does not provide an efficient bit-complexity theorem. It does provide a constructive modulus without an unknown compactness or strong-limit convergence rate.

## 8. One exact finite control and failed shortcuts

A two-dimensional control isolates the boundary-strip dependence. For b>0 and 0<eta<b, take

    A_eta=diag(b-eta,b+eta),
    B_eta=diag(b+eta,b-eta).

Their norm difference is 2eta. On input |0><0|, the two-bin readout at b produces opposite certain classical labels, so the full recorded outputs have trace distance exactly 2. The input's A_eta strip mass at width delta>=eta is one. This is consistent with (10)–(13), and shows concretely why smoothing cannot simply discard boundary mass. It is a varying two-level diagnostic, not a counterexample to the fixed-chain theorem or a general physical impossibility claim. No numerical control was run.

The following routes were not used as closure:

- Global norm convergence of Hhat_Lambda to H is unavailable; even the one-particle operators differ on the exterior. Boundary-localized eigenmodes can persist below the bulk band. The proof uses (3) only on the fixed input modes.
- Direct comparison of hard projectors from a small energy-operator error loses control at the bin boundaries. The explicit strip majorant (10) handles finite atoms rather than assuming them absent.
- Comparing only outcome probabilities or measuring fine energy and binning would not prove (13). The record isometry and its system output are compared before dephasing.
- A small ||(ehat_Lambda-e)P_S0|| alone does not justify applying a general Lipschitz function as an operator-Lipschitz map. The Cauchy polynomial/Fourier argument proves the needed functional calculus estimate directly.
- Strong convergence or a finite numerical sample alone gives no computable modulus. The quantitative locality and strip estimates are the additional steps here.

## 9. Remaining obligations and exact scope

The theorem assumes the actual finite/infinite positive-Fock identifications from the pinned candidate, exact coarse Lüders readout, fixed g>J>0, known finite-support matched inputs, and fixed finite positive boundaries. The proof introduces no physical premise beyond that supplied task. The existing infinite-chain common-energy isometry can be applied to both compared outputs; isometric conjugation preserves the trace-norm/reference bound and does not require rebuilding the embedding.

A full driven kinetic history is still outside this result. Earlier dynamics can create spatial tails and unbounded particle sectors; applying this bound then requires quantitatively truncating the reachable inputs and controlling that truncation through subsequent stages, along with the long-time and boundary-strip dependence. This derivation supplies none of those missing kinetic-uniform estimates. Growing record counts, moving boundaries, a closing gap, arbitrary energy-ball inputs, or an apparatus compiler are also unproved here. The allowed finite endpoint fields and their escaping edge states are included in this single-readout estimate.

The decisive new steps needing independent review are the localized analytic-functional-calculus bound (3)–(5), the finite-volume strip transfer (10), and the explicit Fock Fourier strip bound (14)–(17). The elementary two-isometry argument then transfers them to the complete quantum instrument. The supplied proof is provisional original mathematics, not evidence of independent acceptance. In particular, the planned target-excluded one-particle comparison has not been supplied to this derivation and remains a separate check. No Lean, canonical identity runner, scientific program, pipeline, or audit was executed.

Exact end-of-task source identity check:

- Candidate: `13fd167efa195fd672fa37e5f3562059bdd76ad373686ef88cde65a02cdfcb10`.
- Recovery review: `6eeb9c546b01ef54afb5ff0f972ea64a44832ce16c029a745e758d04df59cba6` at `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261013_213733/crash_recovery_01a13807/finite_chain_review/REPORT.md`.
- `docs/ENERGY_ADAPTED_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md` at pinned ccbeddd0: `e8b34ef49f7e3d5c289584b8f662da40a05912794bcf1b4cb8e05e6c903bbc88`.
- `docs/CALIBRATED_ENERGY_TRANSFER_BOUNDED_THEOREM_NOTE_2026-10-13.md` at pinned ccbeddd0: `1f71af03465e71a57bcbe0f7713759ab51ff36df02736bf8be5d9e798d9f725e`.
- Saved UTC: `2026-10-14T02:11:35.711937+00:00`.

<!-- END SOURCE F -->


<!-- BEGIN SOURCE G sha256=98f1033ce7f3898b7c71afb9e97d0caee9e02d09557ebc409898bee761e916c1 -->

## Source G: Actual matched driven-chain comparison

Original: `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261013_213733/continuation_20261014_023239/matched_drive_root/DERIVATION.md`. Complete immutable body follows.

# Proposed quantitative matched-drive comparison

Status: supervisor construction, unaccepted pending a separate check. This is
a conditional statement for the supplied massive one-dimensional chain and
matched bounded even local-spin controls. It is not native physical realization,
an efficient simulation, an audit verdict, or a kinetic-limit theorem.

## Sources and exposure

The finite-open-chain candidate at
../..//finite_open_chain_independent/CANDIDATE.md, SHA256
13fd167efa195fd672fa37e5f3562059bdd76ad373686ef88cde65a02cdfcb10,
was read completely in the preceding recovery turn. Its complete model/control
definitions and F8–F15 were refreshed for this construction. The common-carrier
finite/infinite identification, actual shifted finite spin energy, and even
local-spin CAR-polynomial representatives are supplied conditional premises.

The proposed single-readout modulus at
../../crash_recovery_01a13807/finite_volume_modulus/DERIVATION.md, SHA256
8fc3f3255db941288993e13afa6cef9b35d52804595fc26b75bcb7b841b72dea,
was previously read and checked by the supervisor and is under separate review.
Its complete locality construction was refreshed here. Only its elementary
square-matrix geometry and analytic free-propagator estimate are reused below;
neither its spectral strip theorem nor its d^(-1/6) conclusion proves this
drive statement. Prior instruction identities and source exposure are retained
in the sibling START.json. No worker's new driven-reachability or history
composition output was read before writing this construction.

## 1. Model and finite input

Fix g>J>0, c0=g+J and C=2c0. Use the actual open-chain matrices and extensions

    T=gI-JS,
    That_L=i_L T_L i_L* + g(I-Pi_L),
    e=2|T|, ehat_L=2|That_L|,
    H=dGamma(e), Hhat_L=dGamma(ehat_L), A=1+N.

Interior fields equal g; endpoint fields may lie anywhere in [g/2,g]. The
finite physical range is Gamma(Pi_L)F. The shifted finite spin Hamiltonian
intertwines exactly with Hhat_L on this range, as in F7/F12 of the candidate.
No assertion identifies it with H at finite volume. Outside modes are only
comparison bookkeeping and are never populated by a physical finite state.

For s>=0, put k_s=2^s+1. Let each fixed bounded selfadjoint even control have
a specified finite CAR-word representation

    V_a = sum_w c_aw product_(b=1)^(p_aw) gamma_0(O f_awb),
    O=diag(V*,I), V=T|T|^-1.

Every real two-component coefficient f=(f_1,f_2) has support in the same finite
set K. Its finite representative replaces O by Ohat_L=diag(Vhat_L*,I), with
the identical word order and coefficients. This is precisely the matched even
spin control in the source, not a compressed target control. Identity words
have p=0 and their difference is zero. Define the finite coefficient bounds

    M_sa=sum_w |c_aw| k_s^(p_aw) product_b ||f_awb||,
    D_sa=sum_w |c_aw| p_aw k_s^(p_aw) product_b ||f_awb||.

These are valid graph-norm and field-difference envelopes by F13. They need
not be optimal. Zero coefficient vectors cause no divisions by their norms.

Consider one segment [0,T0], T0>=0, with the same real L1 controls u_a(t) in
both models. Write

    B_s=int_0^T0 sum_a |u_a(t)| M_sa dt,
    D_s=int_0^T0 sum_a |u_a(t)| D_sa dt.

Known upper bounds may replace these integrals everywhere. The corresponding
driven propagators are U_L(T0,0) and U(T0,0). Both have A^s graph norm at most
exp(B_s). No differentiability of the controls is required.

Let Q be any subspace of sum_(n=0)^n_* wedge^n ell2(S0), with S0 a finite set
and 0<=n_*<=|S0|. Assume the chain interval contains S0 union K with clearance

    d=min(min(S0 union K)-l, r-max(S0 union K))>=2.

Empty/identity control sets can be omitted from this union. The vacuum-only
input case has n_*=0 and zero free-input error. Define the restricted relative
graph error

    E_L = ||A^s (U_L-U) P_Q A^(-s)||.

Q need not be invariant under either dynamics. The input projection P_Q need
not commute with A; this last displayed placement is intentional and will be
qualified in section 4 before using the estimate for arbitrary subspaces.

## 2. Explicit evolved-profile comparison

Use the uniform constants

    mu=(g-J)^2/[16(g+J)^2], r0=1-mu,
    rho=(1+r0)/2, q=r0/rho<1, v=sqrt(1+rho),
    X=I-T*T/c0^2, X_L=I-That_L*That_L/c0^2.

Both spectra lie in [0,r0]. The real-space squares are tridiagonal and their
difference annihilates vectors supported in [l+2,r-2]. Thus X_L^k f=X^k f
through degree d-1 for a coefficient supported at clearance d. In particular
the half-field right endpoint changes the adjacent offdiagonal entry too.
That_L* f_1=T* f_1 at clearance d>=2; this common vector has clearance at
least d-1, so the equality after an additional X power holds through d-2.

For |z|=rho, the analytic functions

    F_t(z)=exp(i C t sqrt(1-z)),
    G_t(z)=F_t(z)/sqrt(1-z)

have moduli at most exp(C v |t|) and
exp(C v |t|)/sqrt(1-rho), respectively. Cauchy's coefficient bound and a
geometric spectral tail, truncating at the degrees just stated, imply

    ||[exp(it ehat_L) Vhat_L* - exp(it e) V*] f_1||
      <= 2 exp(C v |t|) q^(d-1)
                      ||f_1|| / [(1-q)sqrt(1-rho)],       (D1)

    ||[exp(it ehat_L)-exp(it e)] f_2||
      <= 2 exp(C v |t|) q^d ||f_2||/(1-q).                (D2)

For D1 use V*=(1-X)^(-1/2)T*/c0, and its finite counterpart, with
||T*/c0||,||That_L*/c0||<=1. The polynomial portions agree on the common
T* f_1; each analytic tail is charged separately. D2 uses F_t directly.

The complex coefficient of the Majorana field is z_f=V* f_1+i f_2. Since
T and the polar unitary are real and V is unitary, ||z_f||=||f||; the same
holds at finite volume. Free evolution rotates this vector by exp(it e),
up to a common harmless sign convention for t. Therefore the difference
of matched evolved coefficient vectors for |t|<=T0 is at most

    P(d,T0) ||f||,
    P(d,T0)=2 exp(C v T0)
          [(1-rho)^(-1/2)+1] q^(d-1)/(1-q).              (D3)

Here ||f_1|| and ||f_2|| were each bounded by ||f|| and q^d<=q^(d-1).
This is deliberately conservative. Each unchanged factor in a telescoped
word still has coefficient norm ||f||, so the graph-norm difference of its
matched evolved control operators is bounded by P(d,T0) D_sa.

## 3. Put the final free factor on the input side

Write F(t)=exp(-itH). For a fixed segment endpoint T0, exact interaction-picture
algebra gives

    U(T0,0)=R_T0 F(T0),
    R_T0=time_ordered_exp[-i int_0^T0
                 F(T0-t) (sum_a u_a(t)V_a) F(t-T0) dt].   (D4)

Indeed the usual formula is U=F(T0) W with interaction generator
F(-t)V(t)F(t); conjugate the entire Dyson series by the constant F(T0).
Conjugation preserves time order. Use exactly the same identity for the
finite system. D4 is an endpoint-dependent factorization, not an assertion
that R_t solves an ordinary fixed-generator interaction equation as t varies.

Both R factors have graph norm <=exp(B_s). D3 bounds their generator
difference by an integrable envelope with integral <=P(d,T0)D_s. Duhamel
or Dyson telescoping in the A^s-conjugated bounded evolution gives

    ||A^s(R_L,T0-R_T0)A^(-s)||
         <= exp(B_s) P(d,T0) D_s.                        (D5)

Only one exp(B_s) is needed: the forward and backward portions in the
integral use complementary pieces of the same nonnegative control envelope.
No uniform full-Fock norm convergence of the free propagators is asserted.

For the finite spatial/particle carrier

    Q0=sum_(n=0)^n_* wedge^n ell2(S0),

the elementary free estimate, using F_t-1 in Cauchy's bound, is

    ||[F_L(T0)-F(T0)]P_Q0||
      <= Efree(d,T0,n_*)
      :=min(2, 2 n_* v C T0 exp(v C T0) q^d/(1-q)).        (D6)

One-particle polynomial equality through d-1 and tensor telescoping on
each exterior sector prove D6. Both free groups preserve particle number.
Q0 commutes with A, so D6 also holds with A^s and A^(-s) around the
displayed operator. This is a bound on a finite input carrier, not global
operator-norm convergence.

Subtract D4 in the order

    U_L-U=(R_L-R)F_L + R(F_L-F).

Combining D5 and D6 gives the central proposed estimate on Q0:

    ||A^s(U_L-U)P_Q0 A^(-s)||
       <= exp(B_s)[P(d,T0)D_s+Efree(d,T0,n_*)]
       =: epsilon_drive(d).                              (D7)

The final-free-factor placement is consequential: the finite-input free
estimate is applied before the driven factor. Applying D6 to W Q0 in the
usual U=F W form would require a separate reachability estimate that has
not been assumed.

## 4. Inputs, references, and a sufficient volume

D7 is stated on Q0, which commutes with A. Its consequence for any subspace
Q subset Q0 is the Hilbert--Schmidt estimate on actual inputs, not the claim
that an arbitrary P_Q commutes with A. For positive rho supported on Q0 tensor
an arbitrary reference, set M(rho)=Tr[(A^(2s) tensor I)rho]. Since
P_Q0 A^s sqrt(rho)=A^s sqrt(rho), D7 gives

    ||A^s(U_L-U)sqrt(rho)||_HS <= epsilon_drive sqrt(M(rho)).

The two propagated weighted Hilbert--Schmidt norms are at most
exp(B_s)sqrt(M(rho)). Consequently

    ||(A^s tensor I)[U_L rho U_L* - U rho U*](A^s tensor I)||_1
       <=2 exp(B_s) epsilon_drive(d) M(rho).              (D8)

This includes every passive reference and all sector coherences. The earlier
symbol E_L involving arbitrary P_Q is not needed; D7–D8 are the actual claim.
For s=0 they also give the corresponding finite-input channel diamond bound.

For an explicit sufficient clearance, define

    Kdrive=2 exp(B_s+C v T0)/(1-q)
          {[(1-rho)^(-1/2)+1]D_s+n_* v C T0}.

Then epsilon_drive(d)<=Kdrive q^(d-1). If Kdrive=0 the segment has no
comparison error. Otherwise any integer d>=2 satisfying

    d-1 >= log(Kdrive/eta)/(-log q)                        (D9)

ensures epsilon_drive<=eta. Certified upper rounding is allowed; no bound
on an arbitrarily enlarged rounded resource count is inferred. For a target
weighted state error eps and a known input moment M0, choose
eta<=eps/[2 exp(B_s) M0]. A carrier containing S0 union K with this clearance
has finite explicit size. The constants are not uniform as the gap shrinks,
the time/control budget grows, or the input carrier grows.

The actual finite U_L preserves Gamma(Pi_L)F. Its output from Q0 thus has
finite mode support L and at most |L| particles, even though the infinite
target need not have exact finite spatial/particle support after the drive. It is
a legitimate finite-dimensional reachable-output approximant. Its moment
is at most exp(2 B_s)M(rho), independently of the resulting volume.

This supplies a proposed route to reachable-state approximants without a
separate hard particle cutoff: use the entire finite Fock range as the next
auxiliary carrier, and explicitly pay its size in the next bound. That may
be extremely inefficient. A common-final-volume history theorem still needs
its own telescoping, input approximation and physical carrier argument.

## 5. Effective data and limits

D9 is a computable volume prescription when g,J,s,T0, the finite coefficient
data and suitable B_s,D_s bounds are specified effectively. Integer upper
bounds can replace noninteger graph exponents as in the apparatus note.
Arbitrary merely measurable supplied L1 controls do not by themselves give
an algorithm for synthesizing their finite evolution. That requires a
supplied executable control schedule or effective L1 approximation data and
its separately priced implementation error. D7–D8 as mathematical estimates
need only the stated L1 hypotheses and known bounds.

This note does not perform a numerical experiment, formalize the analysis,
derive the physical model or controls from the framework, price autonomous
clocks/heat/three-dimensional routing, or identify a kinetic joint limit.
No earlier source, audit state, Git branch, axiom or editable prompt changed.

<!-- END SOURCE G -->


<!-- BEGIN SOURCE H sha256=c431061736d32ede70f0ff4ee38f82520997106575d469ae374edb5e664f6612 -->

## Source H: Complete weighted quantitative history

Original: `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261013_213733/continuation_20261014_023239/history_composition/DERIVATION.md`. Complete immutable body follows.

# Finite histories through finite-dimensional approximants to target inputs

Status: conditional composition lemma, not a physical-realization or audit finding. The two supplied interfaces yield computable finite carriers and error certificates for approximants to reachable target inputs; evaluating the approximant state matrices is unnecessary and is not claimed. A computable volume for the actual complete protocol additionally needs a finite-input comparison modulus for each actual finite-chain drive. The distinction is explicit below.

## Source and exposure

The source is `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261013_213733/finite_open_chain_independent/CANDIDATE.md`, SHA-256 `13fd167efa195fd672fa37e5f3562059bdd76ad373686ef88cde65a02cdfcb10`. Sections 3–5 and the displayed first part of section 6 were already read in the preceding bounded task. The complete section 6, including F23–F24, was then read for this task, with the hash checked again. The relevant source is now covered completely. The main/ai-execution instruction revisions remain `583c699e859b64ff01c8bc92d1c04bdfe9994509` and `3a4b2c66a1ead7a1c48b4359627e968f681e3c39`; their previously read AGENTS, science workflow and workhorse instructions were reused.

The earlier independent one-particle volume proof is exposed to this worker but is **not** a proof of interface (R) below for many-particle inputs. This task assumes the stronger interface conditionally, exactly as requested. No quantitative many-particle theorem, new derivation of the infinite common-H identification, or native implementation is inferred. No other worker's current proof was requested or read for this task. Model and effort were inherited unchanged.

## 1. Spaces, weights and a physical-support condition

Work on the source's common Fock carrier `F=F_-(ell^2(Z))`, with number operator `N`, `A=1+N`, fixed `s>=0`, and `G=A^s`. For a system/record/reference operator define

```text
||X||_s = ||(G tensor I) X (G tensor I)||_1,
M_s(rho)=tr[(G^2 tensor I)rho] for rho>=0.
```

Every record and reference factor is unweighted. Use the finite physical-mode/particle projections

```text
Q(K,n)=Gamma(Pi_K) 1_{N<=n},   K a finite subset of Z.
```

These commute with `G` and have finite-dimensional range. In particular, if a physical interval `Lambda` contains `K`, their range is inside `Gamma(Pi_Lambda)F`. Their dimension is `sum_(p=0)^min(n,|K|) binom(|K|,p)`.

Here “finite-mode approximant” must mean such a finite physical-coordinate mode space, or come with a computable additional approximation into one. A finite-dimensional span of vectors with infinite spatial tails does not itself lie in any physical chain. If only that weaker range statement is supplied, a certified coordinate-tail approximation and its error are an additional required premise. The output-support issue is separate from finite rank.

Consider `r>=1` fixed operations `T_1,...,T_r`, each either a supplied driven unitary channel or a full coarse Lüders readout. Their actual common-chain counterparts are `T_(j,Lambda)` under the candidate's matched embeddings and common label convention. All comparisons retain the entire unnormalized quantum state and every record. Let `rho_j=T_j(rho_(j-1))` and `rho_(j,Lambda)=T_(j,Lambda)(rho_(j-1,Lambda))`. The zero-operation case is just the initial comparison.

Use the source's genuine full-carrier extensions of the actual operations, with the graph bounds below, rather than zero-complement compressions. This allows an actual extended map to be applied to a target state in the comparison proof even when that target has infinite spatial support. The actual physical state stays in `Gamma(Pi_Lambda)F`, which the source's matched finite controls and readouts preserve.

Initially take a normalized `rho_0` supported on `Q_0=Q(K_0,n_0)` in the system factor, with an arbitrary passive reference. A known bound `M_s(rho_0)<=M_0` is enough; one may use `M_0=(1+n_0)^(2s)`. Subnormalized inputs scale homogeneously, and zero input is immediate. An initial preparation error `e_0=||rho_(0,Lambda)-rho_0||_s` can be included. Preparation of this matched input is a supplied condition. A general initial infinite-mode input would need its own effective weighted approximation; finite moment alone gives no computable tail modulus.

## 2. Precise conditional interfaces

### (R) Readout comparison and finite physical output

For each readout, each `Q=Q(K,n)`, and each tolerance `epsilon>0`, there is a computable interval requirement `L_R(Q,epsilon)` such that, for every admissible physical interval `Lambda` containing it and `K`,

```text
||(M_Lambda-M) tensor id_R (sigma)||_s
     <= epsilon M_s(sigma)                                  (R)
```

for every positive `sigma` supported on `Q` and every reference. The same output labels and endpoint convention are used. The modulus is an **eventual bound for all larger allowed volumes**, not the discovery of one favorable volume. Where endpoint fields may vary, its stated quantifier must include those variations or the physical family must be fixed in advance.

For the exact free-energy readouts in F12 and F17–F18, both instruments intertwine `N` and hence `G`; they are weighted trace-norm contractions on Hermitian inputs. Also `M_Lambda` sends an input in `Q(K,n)`, for `K subset Lambda`, into `Q(Lambda,n)` in the system factor. These facts are needed here, and follow from the source's exact range and number-preservation identities. They are not consequences of probability agreement alone.

If supplied interface (i) is stated in ordinary full-CQ trace norm with an arbitrary passive reference, these identities give (R) with the same tolerance: apply it to `G sigma G`, which is positive and still supported on `Q`. If (i) is only uniform on unreferenced density operators, a safe computable promotion is available on finite `D=dim Q`: request ordinary tolerance `epsilon/(2D)`. Polarization bounds the image of an off-diagonal matrix unit by twice the unreferenced state bound, and a Schmidt decomposition gives `(sum_i sqrt(lambda_i))^2<=D`. Thus the complete bound costs at most `2D`. No dimension factor depends on the passive reference or the number of old records.

An approximate apparatus that does not intertwine number would instead require a weighted comparison and weighted amplification bound of its own. Ordinary-norm accuracy alone does not supply them.

### (C) Computable output compression for target drives

For a target segment `U_j`, assume a known graph bound

```text
||G U_j G^-1|| <= C_j.
```

On any given finite input space `Q`, interface (ii) must furnish a computable physical-coordinate mode/particle space `Q'`, and a uniform error certificate

```text
||G (I-Q') U_j Q G^-1|| <= eta.                             (C)
```

A supplied finite-output operator approximation `V:QF -> Q'F` with `||G(U_j-V)QG^-1||<=eta` suffices: apply the orthogonal projection `I-Q'`, which commutes with `G`. A finite set of basis-vector certificates can likewise be converted to an operator bound with its explicit finite-dimensional norm factor. Pointwise convergence with no effective error certificate is not (C). For volume selection the weaker interface stated in (C), returning only the carrier and certificate, is enough; it need not return entries of `V` or `U_j`.

For analysis define the positive, possibly trace-decreasing map

```text
B_j(sigma)=Q' U_j sigma U_j* Q',   sigma supported on Q.
```

Then, also with any reference,

```text
M_s(B_j(sigma)) <= C_j^2 M_s(sigma),
||(B_j-T_j)(sigma)||_s <= 2 C_j eta M_s(sigma).              (11)
```

Indeed, weighted conjugation turns the two vector operators into `G U_j G^-1` and its output compression, each of norm at most `C_j`, with difference at most `eta` on `Q`. The Hilbert–Schmidt/rank-one trace estimate gives (11). This compression is an analysis device, not an extra physical measurement. It is never normalized. Selecting the spaces and all error bounds only needs the certificates, not exact computation of the surrogate state matrices.

### (D) Additional actual-drive comparison needed for a computable physical volume

Let the actual source segment be `U_(j,Lambda)` and suppose its uniform graph bound is

```text
||G U_(j,Lambda) G^-1|| <= Cbar_j.
```

The missing effective interface, unless already explicitly included in (ii), is a computable eventual modulus on every finite input space:

```text
||G (U_(j,Lambda)-U_j) Q G^-1|| <= nu
       for every Lambda containing L_D(j,Q,nu).             (D)
```

It implies the channel comparison

```text
||(T_(j,Lambda)-T_j) tensor id_R(sigma)||_s
     <= (Cbar_j+C_j) nu M_s(sigma),                         (12)
```

for all positive `sigma` supported on `Q`. The same factorization as in (11) proves this, with no input-reference dimension cost.

Interface (C) approximates the range of the target `U_j Q`. It does not compare the actual `U_(j,Lambda)` with `U_j`; these are different mathematical statements. In particular a nonunitary output compression or arbitrary finite matrix approximant is not automatically the actual matched finite-chain drive or an available physical replacement for it.

The candidate's F14 supplies uniform graph amplification, and F15 gives qualitative graph-strong convergence of the actual matched drives. On a fixed finite-dimensional `Q`, strong convergence implies graph-operator-norm convergence after restriction to `Q`, by a finite basis argument. Thus the source supplies qualitative existence for (D), but the exposed source does not give the computable modulus required in (D).

## 3. Constructing finite-dimensional reachable-input approximants

Only pre-operation target inputs need approximation. For `j=0,...,r-1` construct a positive surrogate `sigma_j` with system support in a known `Q_j=Q(K_j,n_j)`. Set `sigma_0=rho_0`. Denote its weighted mass upper bound by `m_j`, and its target approximation error by `b_j`:

```text
M_s(sigma_j)<=m_j,
||sigma_j-rho_j||_s<=b_j,
m_0=M_0, b_0=0.
```

For a drive at stage `j<r`, use (C), set `sigma_j=B_j(sigma_(j-1))`, and choose its certificate so that `2 C_j eta_j<=tau_j`. Then `Q_j` is the returned output space.

For a readout at stage `j<r`, choose an **auxiliary analysis volume** `lambda_j` satisfying (R) on `Q_(j-1)` with tolerance `tau_j`, and set

```text
sigma_j=M_(lambda_j)(sigma_(j-1)),
Q_j=Q(lambda_j,n_(j-1)).
```

This produces a finite-dimensional system output approximation even though the target sharp projection generally has infinite spatial tails. No independent post-readout localization theorem is needed beyond (R) and the finite physical output/number-preservation facts. All output records are retained as unweighted factors. The final operation does not need an output surrogate unless a further stage is to be appended.

Write

```text
q_j=C_j^2 for a drive, and q_j=1 for a readout.
```

Both cases give the explicit recursive bounds

```text
m_j <= q_j m_(j-1),
b_j <= q_j b_(j-1) + tau_j m_(j-1),       j<r.              (13)
```

The first inequality uses positivity and no renormalization. For the second, insert `T_j(sigma_(j-1))`, apply the target weighted amplification to the incoming discrepancy, and then the local surrogate estimate. This construction uses (R), (C) and the physical output-range facts. It does not yet establish that the actual complete finite-chain protocol follows the surrogates.

## 4. Actual finite-history error recursion

For each operation choose a finite-input comparison allowance `epsilon_j` on `Q_(j-1)`:

- at a readout, obtain it from (R);
- at a drive, require (D) with `nu_j<=epsilon_j/(Cbar_j+C_j)`.

Let `a_j=Cbar_j^2` for a drive and `a_j=1` for a readout. Define `e_j=||rho_(j,Lambda)-rho_j||_s`. For one fixed physical `Lambda` satisfying all the required comparison bounds,

```text
e_j <= a_j e_(j-1)
       +(a_j+q_j) b_(j-1)
       +epsilon_j m_(j-1).                                (14)
```

Proof: first insert `T_(j,Lambda)(rho_(j-1))`. Its incoming-error contribution is bounded by `a_j e_(j-1)`. In the remaining difference `(T_(j,Lambda)-T_j)(rho_(j-1))`, insert the supported surrogate `sigma_(j-1)`. The two maps amplify its target discrepancy by at most `a_j+q_j`, and their supported-input comparison costs `epsilon_j M_s(sigma_(j-1))`. This proves (14). Surrogates are used only to apply the finite-input modulus; the actual state may have arbitrarily complicated support inside the final physical chain.

Equations (13)–(14) are a computable recursion once the interfaces are supplied. They are valid for arbitrary passive reference systems and retain full old-record/system correlations. They do not replace old records by marginal probabilities and never normalize a rare branch.

For an explicit closed budget, use the larger constants

```text
D_j=max{1,a_j,q_j},
K_0=1, K_j=product_(ell=1)^j D_ell.
```

Then `m_j<=M_0 K_j`, and (13) yields

```text
b_j <= M_0 K_j sum_(i=1)^j tau_i/D_i.
```

Substitution in (14), dividing by `K_j` and summing, gives

```text
e_r <= K_r e_0 + M_0 K_r [
        sum_(j=1)^r epsilon_j/D_j
        +2 sum_(i=1)^(r-1) (r-i) tau_i/D_i ].              (15)
```

Thus an analysis truncation is charged every time it is used as an input approximation downstream; it is not silently treated as an exact reset. The bound is sufficient, not optimized. Direct evaluation of (13)–(14) can be sharper.

For a final allowance `E>0` and a known initial bound `e_0`, let `E_rem=E-K_r e_0>0`. For `r>=2`, one safe choice is

```text
epsilon_j/D_j <= E_rem/(2 r M_0 K_r),
tau_i/D_i <= E_rem/[2 r(r-1) M_0 K_r],  1<=i<r.           (16)
```

Because `2 sum_(i=1)^(r-1)(r-i)=r(r-1)`, the two sums in (15) each consume at most half the remaining allowance. For `r=1`, no surrogate output tolerance is needed; request `epsilon_1 M_0<=E-D_1 e_0`. If the supplied initial-error upper bound already consumes the allowance, this recipe has no remaining guaranteed budget; it does not prove that the actual error is large.

## 5. One common final physical volume

Construct all `Q_0,...,Q_(r-1)` sequentially using (13) and the chosen tolerances. This determines a finite list of physical mode sets, auxiliary readout volumes, and comparison requirements. Next obtain all final readout requirements from (R) and drive requirements from (D) on those fixed finite input spaces. Take a physical interval `Lambda_*` containing:

1. every `K_j` and each auxiliary interval used to define them;
2. every eventual readout comparison interval `L_R(Q_(j-1),epsilon_j)`;
3. every eventual drive comparison interval `L_D(j,Q_(j-1),nu_j)`;
4. the fixed control/preparation support required by the actual source protocol.

The hull of finitely many supplied finite intervals is a computable common choice when those interfaces are computable. Every admissible `Lambda` containing this hull then satisfies (14)–(16). All actual operations are performed as `T_(j,Lambda)` on **this same physical chain**. The state is never transferred between different physical volumes, and no surrogate compression is physically inserted.

This is a carrier-and-scalar calculation. Its inputs are the finite protocol, `Q_0`, `M_0`, the graph-constant upper bounds, the tolerance and initial-error budgets, and effective uniform (R), (C), (D) interfaces. First calculate (16), using the stated one-stage rule when `r=1`. At a drive request the next carrier from (C) with `eta_j=tau_j/(2C_j)`; at a readout request an auxiliary interval from (R) with tolerance `tau_j` and retain the known particle cutoff. Iterate scalar upper bounds (13), without evaluating `M_s(sigma_j)` or any matrix entry of `sigma_j`. Finally request the comparison intervals and take their hull. The same selected carriers and volume work for every input state and passive reference covered by the given `Q_0`, `M_0` and initial-error bound. Known finite feedback families use common carriers and worst-case constants as below; branch probabilities are not needed.

If the uniform interfaces and graph constants are certified functions of physical supports, durations and supplied numerical control-budget upper bounds, this prescription needs only those data, not an effective representation of the full control waveforms. This is a conditional statement about the supplied interfaces: a bound on the control budget alone does not by itself establish (C) or (D), and any additional data their algorithms require must still be supplied. The actual-drive modulus can be supplied separately after the reachable-carrier construction, provided its graph bound used to set the budgets is already known.

Computing or synthesizing driven outputs is a different task. The source assumes fixed real measurable `L1` controls (F14–F15); that assumption alone is not an effective integration or waveform description. To compute finite propagators or surrogate matrix entries one generally needs, in addition to computable finite generators, certified effective approximations to the controls, for example piecewise-constant approximations with a computable `L1` error bound. The corresponding time-ordered evolution error can then be charged separately. Even on a fixed two-dimensional space, the drives `u(t)=c` and `u(t)=-c` on the same interval have the same absolute control budget but generally produce different rotations under a nontrivial fixed generator. Thus carrier/error budgets do not determine the output matrix. Nothing in the present prescription compiles waveforms, evaluates those matrices, or proves physical access to the specified controls.

If the initial error allowance comes from a volume-dependent preparation, include its own eventual comparison requirement in this hull. Qualitative F23 alone is not a computable initial-error modulus. For an exactly matched finite-mode input there is no such extra initial comparison.

The auxiliary `lambda_j` are only mathematical witnesses producing supported approximants to target inputs. Their final mode supports are embedded in the common carrier and contained in `Lambda_*`; no identification of their finite Hamiltonians with the final chain Hamiltonian is asserted. The proof compares the actual operation at `Lambda_*` directly with the target operation using its own modulus on the surrogate input space.

It is essential that the moduli are eventual bounds. Errors need not decrease with every increase in volume. A set of separately successful volumes, with no guarantee for their common enlargement, does not justify the hull construction. If only a particular exhaustion is certified, choose one later member of that same exhaustion satisfying every eventual threshold rather than switching physical families.

## 6. Records, feedback and the limits of the inference

At a readout, all old records and the passive reference are spectators, so the complete finite-input modulus applies directly. A fixed finite feedback tree can be treated with branchwise drives. Use the maximum graph/comparison constants and a common finite output space containing the finitely many returned spaces at that stage. Weighted mass and trace errors add over unnormalized record blocks; no factor equal to the number of histories is needed when the bounds are relative to each block's weighted mass.

Countably many labels do not by themselves spoil the argument: the record space can be an arbitrary passive factor, and positive weighted masses add. With feedback drawn from a fixed finite family, the same common-space construction works. An unrestricted infinite family of history-dependent controls would require a **uniform computable** common output approximation and comparison modulus. Separate finite approximants for each branch need not have a finite common mode union. That stronger premise is not supplied by merely saying that the protocol has finitely many time slots.

The two given interfaces alone do not justify a computable actual-drive volume. As an abstract interface diagnostic, take a two-dimensional one-particle input space, target drive `U=I`, an identity readout, and a rotation `V` moving one basis state to the other. Target output compressibility and readout comparison are exact with graph constants 1. Finite implementations could equal `V` through an unspecified volume threshold and `I` thereafter. They still converge qualitatively and have the same graph bounds, while any volume formula based solely on those unchanged target-compression/readout data can fail before that threshold. This diagnostic is not asserted to arise from the source's matched Ising controls; it isolates information missing from those two quantitative interfaces. The actual matched source family has its own qualitative F15 theorem, whose quantitative refinement must supply (D).

Consequently the available conclusions are:

- With (R), (C) and the finite-output support facts: computable finite carriers and explicit error certificates (13) for supported approximants to the reachable target inputs, without computing those states.
- Adding only the source's qualitative actual-drive convergence: existence of a common sufficiently large physical volume for this fixed protocol, via finite-dimensional restriction and a finite intersection of eventual conditions. This is not yet a computable volume law from the exposed data.
- Adding the effective actual-drive interface (D): a computable common physical volume and the complete weighted history bound (14)–(16).

Nothing here proves interface (R) for many-particle inputs from the preceding one-particle proof, a native apparatus, unrestricted initial energy-ball uniformity, an efficient resource law, or joint kinetic/long-time uniformity. If a protocol or graph constants vary with another parameter, every approximation/comparison tolerance and amplification product must be controlled at that joint scaling. A finite-history lemma alone supplies no uniformity in that parameter.

## 7. Actual verification and scientific-source record

`check_recursion.py` uses exact rational arithmetic to iterate (13)–(14) and compare with the independently expanded expression (15). It checked 512 deterministic profiles of one through eight stages, including unequal target/actual amplification factors and nonzero initial errors. The bound held in each profile. For two through eight stages with equal worst-case amplifications, the allocation (16) gave exactly the assigned scalar budget `1/10`. Removing the coefficient two in (15) was rejected: a three-stage scalar recursion gave `3/50`, while the altered formula gave `3/100`. This tests the bookkeeping identity, not physical realizability or tightness of those worst-case scalar values.

The sole execution used `/opt/homebrew/opt/python@3.13/bin/python3.13 check_recursion.py` in this directory with `PYTHONDONTWRITEBYTECODE=1`. It exited zero with empty stderr at `2026-10-14T02:47:33.364388+00:00`, after about 0.079 seconds. Script SHA-256: `1c95fcff6c847c9c54693edcc6c9dd6873019650351a0ba3e6c7545570ed17a2`. Stdout SHA-256: `46bf1674f33014169247a03b4d2976d87fe0eb0b17ed6d13aabbfc28d3f7125e`. Complete command, environment, outputs and hashes are in `run01/RECEIPT.json`, `run01/stdout.json` and `run01/stderr.txt`. No failed run was discarded. The candidate source hash matched before and after execution. No physical channel simulation, many-particle modulus computation, or new actual-drive comparison was performed.

The proof and resource recursion are complete as a conditional lemma. A final precision check distinguished computable carrier/volume/error selection from computing or synthesizing driven outputs; it required no change to (13)–(16) or the arithmetic check. The concrete unresolved application obligation is a computable finite-input graph comparison for the actual matched driven finite chains, unless a separate supplied result already proves (D). Also verify that every output approximant has finite physical-coordinate mode support and that readout comparison is complete and weighted as above. A volume-dependent initial preparation needs its own effective comparison if an initial error is charged. Evaluating or synthesizing the actual driven outputs would require its own effective control data and implementation premises, which are not prerequisites for the abstract carrier prescription once the uniform certified interfaces are supplied. These are named application conditions, not new physical axioms.

This note is a scientific-source and verification record. The sole operational checkpoint is maintained in `STATE.yaml` (historical path: `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/worktree/.claude/science/physics-loops/toe-dynamics-bridge-20261009/STATE.yaml`) and `HANDOFF.md` (historical path: `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/worktree/.claude/science/physics-loops/toe-dynamics-bridge-20261009/HANDOFF.md`). No actual-source, Git, PR, audit, prompt, axiom or external-application change has been made. Editable prompt files changed: none. No many-particle premise is promoted by this document; the earlier one-particle proof remains narrower. Supervisor review of this exposed derivation and verification of the application interfaces remain distinct from formal retention.

<!-- END SOURCE H -->


<!-- BEGIN SOURCE I sha256=7fe0df39ecad4aafbbbbfeeae83d2e2372f6527afbaf04223d9ab43dd5ac99b1 -->

## Source I: Compiled fixed-history application

Original: `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/renewal_20261013_213733/continuation_20261014_023239/fixed_history_application/APPLICATION.md`. Complete immutable body follows.

# One common finite chain for a fixed driven energy-readout history

Status: proposed conditional corollary, pending separate check of this application. This is a scientific source record, not an operational checkpoint or retained audit verdict. The supervisor has read the component proofs and their stated reviews. The argument below makes the component interfaces explicit; it supplies no new physical axiom.

## A1. Exact sources and scope

The source root is `renewal_20261013_213733`. The following exact current bodies are used, including the complete proofs rather than their summaries:

| Component | Relative source | SHA-256 |
| --- | --- | --- |
| Finite spin/Fock chain and matched controls | `finite_open_chain_independent/CANDIDATE.md` | `13fd167efa195fd672fa37e5f3562059bdd76ad373686ef88cde65a02cdfcb10` |
| Finite coherent readout compiler, corrected v3 | `crash_recovery_01a13807/finite_apparatus_composition/DERIVATION.md` | `9179660b1c247a99c6e3abc03203fb1bf125d70226c0d8c6b5257b696fc09118` |
| Complete finite-input one-readout bound | `crash_recovery_01a13807/finite_volume_modulus/DERIVATION.md` | `8fc3f3255db941288993e13afa6cef9b35d52804595fc26b75bcb7b841b72dea` |
| Actual matched driven finite-chain bound | `continuation_20261014_023239/matched_drive_root/DERIVATION.md` | `98f1033ce7f3898b7c71afb9e97d0caee9e02d09557ebc409898bee761e916c1` |
| Abstract complete weighted history composition, status-only v2 | `continuation_20261014_023239/history_composition/DERIVATION.md` | `c431061736d32ede70f0ff4ee38f82520997106575d469ae374edb5e664f6612` |

Fix the supplied one-dimensional gapped chain with `g>J>0`, a weight `G=(1+N)^s`, `s>=0`, and a finite ordered protocol of matched even local drives and finite coarse energy readouts. Each readout has finitely many fixed positive interior boundaries, with left-closed bins and the same convention at finite and infinite volume. Use the `<` cumulative version of the readout proof. All times, controls, partitions and the gap are fixed for this statement.

Let the initial normalized positive state, including any passive reference and old classical records, be supported on `Q0=Q(K0,n0)`, where `K0` is a finite set of physical mode coordinates and `Q(K,n)=Gamma(Pi_K) 1_{N<=n}`. Supply a certified bound `M0 >= Tr(G rho0 G)` and actual finite-chain preparation of this state under the spin/Fock identification. The latter is the range and access premise in apparatus C1; a general mathematical input density matrix is not a preparation procedure.

For a computable prescription, retain all effective scalar hypotheses of the readout and drive bounds: a computable weight exponent; adequate effective bounds on the model parameters and a certified positive gap; effective bin-boundary data with certified positive position/separation margins sufficient to check the readout condition delta_d<=min_j(b_j/C)/6; and effective bounds on the finitely supported control coefficients/profiles, durations, and integrated control budgets. Algebraic model and boundary data with certified order tests suffice, while a certificate-based alternative must supply all these volume-bound data separately from the finite compiler separation/threshold data in A5. These data suffice for the volume and tolerance prescription. Evaluating or synthesizing arbitrary driven outputs would additionally require effective control waveforms. No such output computation is used in A2-A4. The local signed controls and their schedules remain supplied physical resources.

## A2. Readout interface R is complete and weighted

For a carrier `Q=Q(K,n)`, the finite-particle readout proof gives an explicit bound `Delta_Q(d)` for the full recorded postmeasurement channel, uniformly for normalized positive input states on `Q` and arbitrary passive references. Its constants depend on this finite carrier, the gap and the fixed partition. `Delta_Q(d)` tends to zero; its stated sufficient envelope is `O(d^(-1/6))`. The cutoff degree is `d-1`, not `d`. It holds for every larger admissible interval with at least the prescribed clearance.

Both the finite and target exact readout channels commute with particle number at every Kraus block. The carrier `Q` commutes with `G`. For any positive carrier-supported `sigma`, put `Y=G sigma G`; then `Y` is positive, has the same carrier and has trace `M(sigma)`. Intertwining `G` through the channels gives

`||(M_Lambda-M)(sigma)||_s = ||(M_Lambda-M)(Y)||_1 <= Delta_Q(d) M(sigma)`.

The passive reference and earlier record registers are included in this equality. Thus abstract interface R has exactly the same tolerance, without a dimension factor. The finite exact readout preserves `N` and maps this input into `Q(Lambda,n)`, a finite physical-coordinate carrier. The single-readout rate is used on the auxiliary carrier chosen at each stage; this assertion does not apply a fixed initial-carrier bound to a spread-out later state.

## A3. Actual drives provide both D and C

For each drive `j`, write `C_j=exp(B_{s,j})`; this bounds both target and matched finite graph propagators independently of volume. The matched-drive D7 bound supplies, for every carrier `Q(K,n)` and sufficiently large clearance around its support and all control supports,

`||G(U_{j,Lambda}-U_j) Q G^(-1)|| <= eta_j(d)`,

where `eta_j(d) <= K_j q^(d-1)`, `0<q<1`, with explicit finite constants from that proof. This is eventual for all larger admissible intervals, not just along a subsequence. The bound concerns the actual matched finite drive. D8 gives the corresponding complete channel difference at most `2 C_j eta_j(d) M(sigma)` on positive carrier-supported inputs. This proves abstract interface D with `Cbar_j=C_j`.

To supply C, choose one auxiliary finite interval `lambda` containing the input and control supports with `eta_j(d)<=eta`. The actual finite drive maps `Q(K,n)` into the finite Fock space over `lambda`. Put `Q'=Q(lambda,|lambda|)`, the full Fock carrier on that interval. Since `Q'` commutes with `G`,

`G(I-Q') U_j Q G^(-1) = G(I-Q')(U_j-U_{j,lambda}) Q G^(-1)`

has norm at most `eta`. The compression `Q' U_j sigma U_j* Q'` is a positive, trace-decreasing auxiliary state with moment at most `C_j^2 M(sigma)` and weighted error at most `2 C_j eta M(sigma)`. It is never normalized. No exact compact support of the infinite driven state is asserted. Nor is an arbitrary finite-rank projection silently assumed to commute with `G`.

This construction uses an actual finite-volume comparison certificate to select `Q'`; it does not require computing the target state, the compression matrix or the finite propagator matrix. The separate auxiliary Dyson-reachability source is unnecessary for this binding and is not promoted by it.

## A4. One physical volume and the full history

Apply the history lemma with `a_j=q_j=C_j^2` at drive stages and `a_j=q_j=1` at exact readout stages. Here `q_j` is the history amplification notation, distinct from the exponential locality ratio `q` in A3. With exact common initial preparation set `e0=0`. Choose its positive surrogate tolerances `tau_i` and comparison tolerances `epsilon_j` by equations (15)-(16) for a desired history budget `E_vol>0`.

Sequentially select the auxiliary carriers using A2 after readouts and A3 after drives. Then impose R/D comparison requirements on each of the finitely many carriers. Take one final interval `Lambda` containing all these carriers, control supports and required clearances. The all-larger-volume quantifiers ensure that this one interval satisfies every comparison. Every physical stage is performed on this same chain; the auxiliary intervals and compressions are proof witnesses, not physical resizing or discarded successful branches.

The lemma's scalar recursion yields weighted trace distance at most `E_vol` between the exact finite-chain history and the infinite target history, including every recorded outcome, its unnormalized postmeasurement block, older classical records and an arbitrary passive reference. The proof explicitly charges the discrepancy between later target inputs and their finite auxiliary carriers. No history probability-only metric is substituted.

This is a finite, computable volume prescription under the stated certified scalar data. Its recursive carrier sizes can be extremely large. It provides neither an efficient scaling claim nor a uniform bound as the gap closes, duration grows, the protocol length grows, or another continuum/kinetic parameter changes.

## A5. Compile the readouts after choosing the volume

Fix that final chain, of length `L`. Retain the supplied exact matched drives. To replace its exact energy readouts by finite logical circuits, impose the additional effective spectral and gate premises of apparatus C1-C10: algebraic chain and boundary data, or equivalent certified finite spectral-separation information; pure ancillary qubits; controlled signed local terms and required scalar ground-energy phase; coherent phase estimation, coarse copying and fine uncomputation; routing and terminal readout.

For each readout, choose the strict lower-side separation and biased phase precision exactly as in the corrected apparatus source, including its endpoint addendum. This avoids replacing the instrument by a fine spectral dephasing. Apparatus C8-C10 yields, for any selected `0<zeta_j<=1`, complete graph-isometry error at most `zeta_j`, complete weighted channel error at most `beta_j=(2+zeta_j)zeta_j`, and moment amplification at most `(1+zeta_j)^2`, all relative to input weighted mass. Certified rational upper-bound product-formula counts and the `Wcost` gate precision are those of v3; no smaller exact-ceiling count is asserted for approximate parameter data. Here `zeta_j` is the total isometry tolerance, distinct from the apparatus internal product-formula allowance: one valid v3 choice is `a_L=zeta_L=zeta_j/3` and `gamma_L<=zeta_j/(3 Wcost_L)`.

Here is one deliberately coarse finite history budget. Let `m` be the number of readouts and `D=product_drives C_j^2`. If `m=0`, there is no readout-compilation error. Otherwise choose every

`zeta_j <= min(1, E_comp / (3 m M0 D 4^m))`.

Use the ideal-past/compiled-future telescope from apparatus C11. The product of drive moment factors is bounded by `D`; all future compiled readout factors are bounded by `4^m`; and `beta_j<=3 zeta_j`. Therefore the sum of the `m` channel defects is bounded by

`3 m M0 D 4^m max_j zeta_j <= E_comp`.

All bounds are complete in the passive reference and prior records. Combining with A4 by the triangle inequality gives total weighted full-history error at most `E_vol+E_comp`. The common finite chain is chosen first; each finite spectral calculation and circuit precision is then charged on that chain. Finite computability of readout circuits does not imply a practical circuit size, clock time, heat cost, or native availability of these resources. Drives are supplied controls in this corollary, not circuit-synthesized from noncomputable waveforms.

## A6. Disposition and unresolved physical work

This corollary connects the supplied gapped-chain finite-volume theorem, actual matched-drive estimate, complete readout estimate and finite logical readout compiler. It does not establish the framework's physical identification, autonomous preparation/control/readout, a three-dimensional native local-qubit architecture, an interacting kinetic equation, or a central rate. Existing infinite-chain energy-adapted identification is used where supplied and is not newly derived here. A varying family of initial states needs its own computable weighted-tail or preparation-comparison certificate before A4 can be applied with an initial error.

Component analytic checks, finite numerical diagnostics, exact scalar controls and byte-identity checks have different scopes. Their existence is not a retained audit or a physical experiment. The operational campaign state remains solely in STATE.yaml and HANDOFF.md in the established checkpoint directory. Editable prompt files changed: none.

<!-- END SOURCE I -->
