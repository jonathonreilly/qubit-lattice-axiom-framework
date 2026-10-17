---
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
trace_class: upstream_support
target_claim_id: two_body_autonomous_halt_bounded_theorem_note_2026-10-17
target_blocker_text: "The supplied incoming clock packet in the positive two-body reflection theorem still needs a small old-independent product-ready source with complete emitted and returned outputs controlled."
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Review the canonical wrapper and portable checkers, execute their declared checks and positive-case mutations, and complete focused milestone checks; shared integrated-main landing gates remain later obligations."
conditional_surface_status: "Exact supplied positive two-body ladder and square-loop emitter, coherent complex hopping phase, one excited emitter in product with a clean clock/source vacuum and arbitrary old/reference input. Fixed accuracy at fixed parameters; infinite blank clock for all future times, or a specified finite clock and time horizon."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "A complete-output operator estimate is proved for an explicit supplied time-independent Hamiltonian and product seed. The Hamiltonian, vacuum, excitation and coherent loop phase are conditional resources; no native realization or arbitrary-accuracy family is derived."
source_science_acceptance_complete: true
wrapper_root_approval: accepted_source_bound_portability_review
canonical_execution: see_paired_execution_evidence_and_canonical_cache
publication: regular_review_proposal
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

# A product-seed emitter for autonomous two-body reflection

**Claim type:** `bounded_theorem`. **Status:** `proposed_retained`.
This is a publication draft of qualified conditional mathematics. Source
qualification, review of this wrapper, canonical execution, publication and an
independent retained audit are separate actions.

An added emitter qubit, prepared in its excited state beside a supplied empty
clock and source vacuum, supplies the common incoming scattering envelope for
the [positive two-body reflection theorem](TWO_BODY_AUTONOMOUS_HALT_BOUNDED_THEOREM_NOTE_2026-10-17.md).
The resulting time-independent model has complete isometry error below 0.004
for every time $t\ge 10^{36}$ on an infinite clock. This estimate retains the
emitter, both source qubits, the complete clock, literal old-system evolution
and arbitrary passive references. It includes prompt emission, all returns,
closed channels and any seed bound-state component. It does not infer a gate
time from a resonance linewidth.

The first installed proof gave the sufficient onset $10^{72}$. A separate
weighted-integral refinement gives $10^{36}$ for exactly the same apparatus,
seed, common spectral envelope and output comparator. Both proof bodies remain
unchanged below. The refinement changes a bound, not the physical construction.

The installed qualification (`outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_root_review/QUALIFICATION.md.txt`)
and its decision (`outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_root_review/ACCEPTANCE.json`) accept
the installed theorem for conditional provisional reuse. The later
weighted qualification (`outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_root_qualification/QUALIFICATION.md.txt`)
and its decision (`outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_root_qualification/ACCEPTANCE.json`)
bind the weighted proof to that exact qualified dependency. Earlier pending
labels in the frozen sources and reports describe their historical state;
they are not rewritten by this wrapper.

**Primary runner:** [scripts/product_seed_emitter_2026_10_17.py](../scripts/product_seed_emitter_2026_10_17.py)
directly imports six calculation functions from three local helpers. The
adaptation has [root portability acceptance](../.claude/science/physics-loops/toe-product-seed-emitter-20261017/ROOT_PORTABILITY_ACCEPTANCE.json).
Actual runs, failed attempts and mutation outcomes are distinguished in the
[execution record](../.claude/science/physics-loops/toe-product-seed-emitter-20261017/EXECUTION_STATUS.md).
The canonical envelope is one shared 120-second CPU cap and 120-second
external wall cap. Original source limits remain historical metadata. The
[pre-run plan](../.claude/science/physics-loops/toe-product-seed-emitter-20261017/PRE_RUN_PLAN.md)
and [adaptation map](../.claude/science/physics-loops/toe-product-seed-emitter-20261017/SOURCE_ADAPTATION.json)
identify the exact boundaries, input mapping and intended checks.
No historical stdout is presented as a canonical cache. The explicit local
destination map is in the source inventory (`outputs/product_seed_emitter_2026_10_17_inputs/SOURCE_INVENTORY.json`).

## 1. Exact statement and resources

Use the fixed exact coefficients of the parent ladder, including

\[
J=0.030021107107032,\qquad \nu=1.459892813020969,
\quad K=2I+Z_1Z_2,
\]
\[
W=\frac{(9+12i)I+(-16+12i)X_1X_2}{25},\qquad
\omega_+=\frac{-7+24i}{25},\quad \omega_-=1.
\]

Every decimal specifying the apparatus here is exact. The complete rational
parameter table remains in the preserved
point certificate (`outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_certificate/inputs/two_body_interval_bridge__inputs__rational_point_certificate.json`).
Times use the parent's declared Hamiltonian units; no conversion to physical
seconds is derived here.
Write $\iota x=x\otimes\Omega$, $\Omega=|00\rangle_{AB}$, and

\[
H_g=h_0\otimes I+B+P_0\otimes V_A+P_1\otimes V_B,
\quad h_0=2JI-J(S+S^*),\quad B\iota=\iota K.
\]

The old/source space has dimension 16. Parity $X_1X_2$ reduces it into two
eight-dimensional sectors. The contact matrices generally mix the old
energies 1 and 3; no commutation of $K$ with the interacting Hamiltonian is
assumed.

Fix

\[
q_0=4.510351185997098,\quad k_0=2\arctan(1/q_0),\quad
E(k)=2J(1-\cos k),\quad E_0=E(k_0),\quad \phi=2k_0,
\]
\[
L=12,\qquad \kappa=10^{-12},\qquad \sigma=10^{-6},\qquad
I=[k_0-\sigma,k_0+\sigma].
\]

The half-line clock is bent through
$c_L=(L,2,0),c_{L+1}=(L+1,2,0),c_{L+2}=(L+1,3,0),
c_{L+3}=(L+2,3,0)$, with emitter $e=(L,3,0)$. Its two new
nearest-neighbor bonds complete one square. On the one-head sector let
$V=|L\rangle-e^{i\phi}|L+2\rangle$, acting as the identity internally, and

\[
\widetilde H=\begin{pmatrix}H_g&\kappa V\\\kappa V^*&B+E_0\end{pmatrix},
\qquad H_{\rm phys}=\widetilde H+(\nu+2\kappa)I.
\tag{1}
\]

This sector is invariant under the full-qubit positive construction. The actual
ready isometry is

\[
\mathcal E x=(|1\rangle_e\otimes|\text{all clock zero}\rangle)
                 \otimes\iota x.
\tag{2}
\]

The emitter excitation and the clock/source vacuum are supplied product
resources, independently of the old input. The seed has no two-site phase
preparation. Its coherent phase resource is instead in the static square-loop
Hamiltonian. No drive is applied after the initial time. A passive reference
may be arbitrarily entangled with the old input.

There is one common normalized envelope $f$ and one unit scalar function
$\rho$, defined in section 3 from these actual fixed apparatus parameters.
On clock sites $n\ge0$, define

\[
b_t(n)=\frac1{\sqrt{2\pi}}\int_I
       f(k)\rho(k)e^{ikn-iE(k)t}\,dk,
\qquad \beta_t=b_t/\|b_t\|,
\tag{3}
\]

with emitter unoccupied. For the fixed scalar $\zeta$ in section 3, the ideal
complete-output isometry is

\[
\mathcal U_{\rm id}(t)x=
 \zeta e^{-i(\nu+2\kappa)t}\,
 \beta_t\otimes\iota e^{-itK}W x.
\tag{4}
\]

**Conditional theorem.** For the supplied apparatus and seed (1)–(2),

\[
\|e^{-itH_{\rm phys}}\mathcal E-\mathcal U_{\rm id}(t)\|<0.004
\qquad\text{for every }t\ge10^{36}.
\tag{5}
\]

The norm is the operator norm on the entire old input space, not a
column-by-column estimate with adjustable phases. Tensoring both isometries
with the identity of any passive reference preserves (5). The corresponding
complete, unhalved trace-norm error is below 0.008, including mixed inputs by
purification and contraction. The old factor ages for the whole elapsed time
from the product seed, including emission and propagation. The physical scalar
in (4) is retained even though density matrices alone would hide it.

For the actual finite compression to clock sites $0,\ldots,M-1$, together
with the emitter and the prescribed far-end diagonal, choose

\[
M=5\times10^{37},\qquad T_{\rm obs}=2\times10^{36}.
\]

After embedding its output in the infinite output space, the finite device
has complete isometry error below 0.005, and unhalved trace error below 0.01,
only for $10^{36}\le t\le2\times10^{36}$. The comparator remains the
normalized half-line packet (3), not a postselected finite projection. $M$
counts clock sites; the emitter, old pair and source pair are additional.
No fixed finite device is assigned the all-future claim (5).

## 2. Full-qubit local blocks and physical permissions

For $j=L,L+2$, with $t_L=\kappa$ and
$t_{L+2}=-\kappa e^{i\phi}$, add

\[
Q_{ej}=\kappa(n_e+n_j)+t_j a_j^\dagger a_e+
                  \overline{t_j}a_e^\dagger a_j,
\]
\[
(E_0-2\kappa)n_e,\qquad\kappa(I-n_L),\qquad
\kappa(I-n_{L+2}).
\tag{6}
\]

Each $Q_{ej}$ is positive on the full two-qubit space and has norm
$2\kappa$; $E_0>2\kappa$. Their sum gives the desired hoppings and
emitter energy, together with exactly $2\kappa I$. The vacancy terms in
(6) cannot be removed from the physical accounting. The added incident
positive-block norm sums are $E_0+2\kappa$ at the emitter and
$3\kappa$ at each new clock attachment. Old and source loads are unchanged.
The inherited added old-site loads are below 2; the source and boundary clock
loads are not all below 2, and the old edge of norm 3 is additional.

The complete local construction (`outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/autonomous_emitter_route/ROUTE.md.txt`),
its independent local review (`outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_independent_review/REPORT.md.txt`)
and qualification (`outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_root_qualification/QUALIFICATION.md.txt`)
are preserved, including the full positive-cell proof and the failed
single-point-emitter shortcut. The latter is a specific local counterexample,
not a general impossibility result. The exact loop phases in (6) require
complex XY/cross-quadrature couplings. Native supply of these couplings, a
clean vacuum, the excited emitter and the exact ladder coefficients has not
been derived from framework premises. No irreversible one-way sink, exact
chirality over a band, or Markovian exponential decay is assumed.

## 3. Common envelope, reflection phase and complete state accounting

The preserved installed proof (`outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_certificate/CANDIDATE.md.txt`)
uses the original certified band gap $9/50$, closed-root bound $1/7$,
physical matching inverse bound 166, and velocity lower bound
$v=1/40<E'(k)$, with $|E''(k)|\le E_2=2J$.
The generic bridge V2 (`outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_certificate/inputs/finite_channel_wavepacket_bridge__THEOREM_V2.md.txt`)
uses a certified velocity lower bound and a curvature upper bound; neither is
misidentified as an attained extremum.

The retarded tail kernel is

\[
R_g(n,m)=AQ^{|n-m|}+Q^{n-1}TQ^{m-1},\qquad
A=[J(Q-Q^{-1})]^{-1},\quad T=(M_{16}^{-1})_{11}-A.
\tag{7}
\]

Here $Q$ includes the open root and every decaying closed root in the
selected parity sector; $T$ need not commute with $Q$. With

\[
X=Q^{L-1}(I-e^{-i\phi}Q^2),\quad
Y=Q^{L-1}(I-e^{i\phi}Q^2),\quad
\Sigma_f=A(2I-2\cos\phi\,Q^2),
\]

the actual matching matrix on physical unknowns $(x_0,x_1,y_e)$ is

\[
M_{\rm aug}=
\begin{pmatrix}
M_{16}&-\kappa E_1Y\\
-\kappa XE_1^* &(\lambda-E_0)I-B-\kappa^2(\Sigma_f-XAY)
\end{pmatrix}.
\tag{8}
\]

It has dimension 24 per parity. Its emitter Schur complement contains
$\Sigma_g=\Sigma_f+XTY$, in that order. It is not the earlier generic
bridge's different 24-coordinate matching convention. No old norm bound is
transferred merely because these dimensions agree.

For each incident energy $\lambda_j=b_j+E(k)$, the installed certificate
separates one resonant emitter coordinate from all seven other coordinates.
It proves $\|D_q^{-1}\|<6$, $\operatorname{Im}d_s>19\kappa^2$,
$\|D_e^{-1}\|<1/(18\kappa^2)$ and
$\|M_{\rm aug}^{-1}\|<1/(17\kappa^2)$ uniformly over the band.
This is an analytic interval certificate, not a grid of inverses. Together
the two sectors retain all sixteen internal directions.

Define the shared form factors and denominator

\[
g_+=e^{-ikL}(1-e^{i\phi-2ik}),\quad
g_-=e^{ikL}(1-e^{i\phi+2ik}),\quad
D_f=E(k)-E_0-\kappa^2(\Sigma_f)_{jj},
\]
\[
y_{\rm ref}=\frac{\kappa\overline{g_-}}{D_f},\quad
N^2=\frac1{2\pi}\int_I\chi^2|y_{\rm ref}|^2dk,\quad
f=\frac{\chi\overline{y_{\rm ref}}}{\sqrt{2\pi}\,N}.
\tag{9}
\]

The real cutoff $\chi$ equals one on the central half-band and decreases
linearly to zero at the two endpoints. The scalar reference spectral measure,
including the velocity Jacobian $dE=E'(k)dk$, gives $N>0.99$ and
$\|f\|_2=1$. It includes any reference spectral mass outside the band.
No global scattering-completeness assumption is needed.

The same $f$ serves every old-energy/parity column. Its exact scattering
packet $\Gamma_t$ is an isometry by the past-limit normalization argument.
The full two-by-two seed overlap matrix within each parity yields

\[
\|\mathcal E-\Gamma_0\|^2
=\|2I-\mathcal E^*\Gamma_0-\Gamma_0^*\mathcal E\|
<(0.003)^2.
\tag{10}
\]

Off-diagonal entries and coherent old superpositions are retained. The initial
state is (2); the function $f$ is a mathematical description of its common
scattering envelope, not an additional externally prepared packet.

There are no installed bound states in the selected energy bands, by (8).
The initial seed's full point-spectral amplitude outside those bands is bounded
by $2\kappa/(v\sigma)=1/12500$. It is already covered by (10), never set
to zero, postselected away, or charged a second time.

For $v_g=E'(k)$, let

\[
t_-=1-\frac{i\kappa^2|g_-|^2}{v_gD_f},\quad
\tau=t_-/|t_-|,\quad r_0(k)=-e^{2ik},\quad \rho=r_0\tau.
\tag{11}
\]

The installed optical bound keeps $|t_-|>1/2$. The gate's original site-1
reflection $\alpha$, in its designated $(s,p)=(-1,-1)$ column, supplies
the fixed scalar

\[
\zeta=-e^{-4ik_0}\alpha.
\tag{12}
\]

The conversion is $r_{\rm abs}=e^{-2ik}r_{\rm site1}$; the free values are
$-e^{2ik}$ and $-e^{4ik}$, respectively. Thus $\alpha$ alone is not
the target scalar. The physical vacancy scalar in (4) is a further, separate
factor. The exact central fit retains its strictly positive residual ceiling

\[
\max_j|R_{{\rm aug},j}(k)-\zeta\omega_j\rho(k)|
\le1.76\times10^{-13}+702\sigma+\epsilon_{\rm phase}
<0.000714,
\quad \epsilon_{\rm phase}<11\times10^{-6}.
\tag{13}
\]

The exact installed resolvent includes all feedback through the emitter and
all closed coordinates. This comparison does not discard a returning pass.
The common phase in (11) belongs to the actual output clock state and is not
chosen separately by column. There is no assertion of stability to varying
apparatus parameters or of a nominal waveform under calibration errors.

Actual old aging follows from the column relation

\[
e^{-it\widetilde H}\Gamma_0
=\Gamma_t e^{-it\operatorname{diag}(b_j)}.
\tag{14}
\]

It does not move $e^{-itK}$ through the interacting Hamiltonian. The
localized correction includes every emitter coordinate, source excitation,
finite interaction-site amplitude and decaying closed-channel tail.

## 4. Initial and weighted escape proofs

The common complete error decomposition is

\[
\|e^{-itH_{\rm phys}}\mathcal E-\mathcal U_{\rm id}(t)\|
\le0.003+0.000714+
\frac{A_0+B_0}{\sqrt{\pi vt}}+
\frac{D}{\sqrt{2\pi}\,vt},
\tag{15}
\]

when $vt\ge1$ and $B_0/\sqrt{\pi vt}\le1/2$. The last condition also
ensures the positive-real normalization in (3) is well defined. Incoming,
outgoing-normalization and full localized errors are all present. $D$
pays the square-sum factor for two potentially nonorthogonal columns per
parity; the parities themselves are orthogonal. Open outgoing vacuum columns
use the maximum in (13), not an unnecessary dimension factor.

The installed source first bounded derivatives separately, obtaining
$A_0=B_0=3\times10^{30}$, $D=8\times10^{42}$. This proves (15) is
below 0.004 for every $t\ge10^{72}$. That proof and its finite consequence
are preserved as a distinct result.

The weighted proof (`outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_candidate/CANDIDATE.md.txt`)
keeps products together inside integration by parts. For $U=1/|D_f|$,
$\operatorname{Im}D_f\ge19\kappa^2$,
$|D_f'|<61/1000$ and
$(\operatorname{Re}D_f)'\ge v-560\kappa^2>v/2$ give

\[
\int_I U\,dk<\kappa^{-1},\qquad
\int_I U^2dk<17\kappa^{-2},\qquad
\int_I U^3dk<\tfrac12\kappa^{-4}.
\tag{16}
\]

These estimates follow from a monotone substitution and exact whole-line
denominator integrals; no narrow-resonance quadrature is used. The complete
localized term $C_j$ satisfies

\[
\|C_j\|<32+12\kappa U,\qquad
\|C_j'\|<2701+131\kappa U+2\kappa U^2.
\]

Consequently the weighted integrals of
$|f'|\|C_j\|+|f|\|C_j'\|+(E_2/v)|f|\|C_j\|$, together with the
weighted phase derivative, give

\[
A_0=3/\kappa,\qquad B_0=23/\kappa,\qquad D=3/\kappa^2.
\tag{17}
\]

All complementary emitter coordinates remain in the block inverse used here.
The installed regularity bounds still justify normalization and integration
by parts; the weighted refinement changes only the final bounds. At

\[
T=10^{36},\quad
\epsilon_{\rm escape}\le\frac{52000027}{540000000000},\quad
\epsilon_{\rm complete}\le\frac{2057560027}{540000000000}<0.004.
\tag{18}
\]

The error terms in (15) decrease for later times. This proves the all-future
claim on the infinite blank clock, with no estimate of the minimal actual
completion time.

For a finite compression, the first omitted clock site is exactly
$d_M=M-L-1$ graph hops from the emitter seed through $c_{L+2}$. The
other attachment route is two hops longer. The certified centered spectral
radius 19 gives

\[
\|e^{-itH_{\rm fin}}\mathcal E-e^{-itH_{\rm phys}}\mathcal E\|
\le\frac{4e^{-d_M+19t\sinh 1}}{1-e^{-1}}.
\tag{19}
\]

The finite output in (19) is understood in the infinite-space embedding.
For $M=5\times10^{37}$, $t\le2\times10^{36}$, this cost is below
0.001. Adding it to (18) gives
$2597560027/540000000000<0.005$. The two proven resource statements are:

| Proof | Infinite-clock sufficient onset | Finite clock sites | Finite comparison interval |
|---|---:|---:|---|
| Initial installed derivative bounds | $10^{72}$ | $5\times10^{73}$ | $[10^{72},2\times10^{72}]$ |
| Weighted escape refinement | $10^{36}$ | $5\times10^{37}$ | $[10^{36},2\times10^{36}]$ |

Each row gives complete error below 0.004 on the infinite clock for all later
times, and below 0.005 only on the displayed finite-device interval. No clock
of either enormous size was allocated or evolved in the supporting programs.

## 5. Evidence and independence limits

The source inventory (`outputs/product_seed_emitter_2026_10_17_inputs/SOURCE_INVENTORY.md`) names every author and independent
program, exact input contract, actual run receipt and output. Their complete
frozen trees are included, with all bytes hashed in
SOURCE_INVENTORY.json (`outputs/product_seed_emitter_2026_10_17_inputs/SOURCE_INVENTORY.json`). Only copying, hashing, source/AST comparison, resolver bookkeeping and
syntax checks were performed while preparing this adaptation.

The installed author program used exact rational uniform bounds and a distinct
16-dimensional scalar tail-elimination calculation. Its twelve 90-digit
physical on-shell diagnostics used at most a 24-dimensional matrix. They are
diagnostics, not the interval proof. Its single recorded run took about
2.565 seconds under a 30 CPU/60 wall second envelope.

The installed independent report (`outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/emitter_installed_review/REPORT.md.txt`)
used a separately constructed 14-dimensional two-channel outgoing graph with
noncommuting contact matrices and non-real loop phase. It tested tail gluing,
the actual augmented Schur matrix, source form factors, closed emitter
response and flux; wrong matrix order, lower sign, density Jacobian and
diagonal-only overlap have explicit discriminators. Separate rational
ceilings cover the physical interval inequalities. One actual independent
run took about 0.881 seconds under 45 CPU/60 wall seconds. It did not replay
author code or independently rederive the inherited stationary ladder fit.

The weighted author program performed scalar rational checks in about
0.055 seconds under 5 CPU/10 wall seconds. The
weighted independent report (`outputs/product_seed_emitter_2026_10_17_inputs/frozen_sources/weighted_emitter_escape_review/REPORT.md.txt`)
checked the denominator antiderivatives, cutoff, a full non-Hermitian
one-plus-seven inverse, coefficientwise product bounds, normalization budgets
and hop distance. Its largest matrix was eight-dimensional. One actual run
took about 10.889 seconds under 45 CPU/60 wall seconds. It did not rerun the
physical installed inverse or seed-overlap proof; those are explicitly bound
to the separately qualified installed theorem.

These are source-exposed checks using the same model and effort. The installed
reviewer authored earlier stationary ladder work; the weighted reviewer had
prior local emitter and generic-packet exposure. Root authored the weighted
refinement and read its separate review. The current wrapper's drafter
authored the local and installed emitter sources and earlier bridge work.
None of these roles constitutes blind discovery, model diversity, a
proof-assistant proof or an independent retained audit. Re-executing their
programs canonically will establish reproducibility of those programs, not a
new independent derivation.

## 6. Imports, remaining assumptions and publication boundary

| Input | Role in this theorem | Provenance | Bridge still open |
|---|---|---|---|
| Exact old $K$, prescribed $W$, fixed fitted ladder coefficients and source vacuum identity | Defines the conditional plant and logical target | Parent theorem, exact point and interval certificates | Native derivation and supply of the apparatus; no arbitrary-accuracy fit family |
| Complex loop phase, emitter energy, positive local blocks and exact conservation structure | Defines the emitter and invariant one-head sector | Complete local construction and installed certificate | Native implementation, precision and structural robustness |
| One excited emitter with clean clock/source vacuum | Actual old-independent ready product | Explicit supplied state (2) | Native preparation, entropy/resource supply and reset/reuse |
| Infinite blank tail, or specified finite compression | All-future theorem, or finite-horizon consequence | Half-line model and graph-distance proof | Physical supply of the apparatus; no finite-device permanence claim |
| Continuous unitary Hamiltonian evolution and passive reference convention | Mathematical evolution and complete-output norm | Same supplied model as the parent theorem | Physical realization and any framework-to-apparatus bridge |
| Mathematical generic bridge and exact local/interval bounds | Proof machinery | Complete pinned sources and separate qualifications | Independent retained status remains for the audit path |

These are named conditional inputs, not new adopted physical axioms or
framework primitives. No empirical observation is used as a claimed derived
prediction. The fixed central residual ceiling $1.76\times10^{-13}$ is
preserved; the theorem proves a fixed error at the stated parameters.
Calibration tolerances and composition with a structural ladder coefficient
box are outside this packet. Scheduling this milestone after the structural
box does not compose their parameter claims.

Root has accepted the helper portability changes; the linked execution record
and paired publication checks state which actual cached runs, scientific
mutations and focused checks are complete. The [runner cache](../logs/runner-cache/product_seed_emitter_2026_10_17.txt)
binds the current primary and declared inputs when fresh. Full pipeline,
strict audit lint and changed-evidence checks belong to the
shared exact integrated-current-main landing candidate under conformance
section12; they are not per-PR entry gates.
Native hardware, practical timing, selected classical Record formation,
noise robustness and reset/reuse are not consequences of this theorem. No
editable prompts, physical axioms or audit verdicts change in this proposal.

## 7. Complete unchanged proof bodies

The following literal Markdown transcripts preserve the full local emitter
route, installed theorem and weighted refinement. Their original frontmatter,
pending labels, provenance paths and links are historical text. The active
wrapper and the separate qualification decisions above state the current
scope. Each body is also available as an unchanged standalone source file.
The byte map (`outputs/product_seed_emitter_2026_10_17_inputs/EMBEDDED_SOURCE_MAP.json`) records offsets, lengths and SHA256
hashes for extracting all three bodies. These transcripts are part of the
proof packet, not summaries substituted for the original arguments.

### Unchanged source: `autonomous_emitter_route/ROUTE.md`

<!-- BEGIN UNCHANGED SOURCE: autonomous_emitter_route/ROUTE.md; bytes=27328; sha256=f03626e591cddc3448bee72148edbee4717ae64af3a6543d4b5c184e7ef9f0a1 -->
~~~~markdown
---
claim_type: exploratory_conditional_route
actual_current_surface_status: unaccepted-author-work
independent_review: not-performed
native_preparation_claim: false
---
# A two-contact product-seed emitter: exact local checks and an open installed-system certificate

## Outcome and scope

A one-qubit excited seed with two phase-controlled attachments to a bent
clock path survives the first directional and return-scattering tests. The
attachments fit on one square plaquette of the cubic lattice. Their full-qubit
positive realization, scalar reserve, central interference zero, and uniform
free-lead return bounds are explicit below. These are author derivations and
an exact bounded algebra check, not an independently checked autonomous gate.

The outstanding issue is substantive: the emitter and installed old/source
gate form one coherent scattering system. No finite emission-completion time,
small in-band bound-state weight, or complete seed-to-gate isometry error has
been certified for that system. Weak coupling by itself does not supply those
facts. Section 7 gives a finite matching and overlap contract whose verification
would imply a complete-output result without assuming exponential decay or
discarding any source. No numerical dynamics or optimization was run.

The simpler one-point weak emitter is a failed shortcut in the free-lead
comparison: its two emitted branches have equal weight, and at its resonant
energy it completely reflects a returned wave, independently of how weak the
coupling is. This does not exclude other emitter designs or boundary-assisted
preparation. The two-contact route is the single alternative examined here.

## 1. Prior work used and the target retained

The preparation inventory and `PREPARATION_NEXT_DECISION.md` were read first.
The canonical wrapper of the installed-bus preparation note and the complete
controlling local-sine qualification were then read. Those constructions use
externally timed complements, swaps, rotations, or phase-locked quadratures.
They do not establish this static emitter. The bounded keyword scan of the
five inventory notes found no treatment of the directional-emission mechanism;
that scan is not a novelty or exhaustive prior-art claim. Exact source hashes
and read coverage are in `SOURCE_MANIFEST.json`.

The target contracts are the frozen `two_body_interval_bridge/CANDIDATE.md`
(SHA256 `b386126649516e533da29182a6cf9eac2da314538ae9b072a2262d7c5c78ed45`)
and the controlling `finite_channel_wavepacket_bridge/THEOREM_V2.md`
(SHA256 `db1a25ee639337a99800f8b8c27dbf366861a6707116f559029697c9f8aaf0e3`).
Their conditional model, rather than a hardware interpretation, is used.
In particular, with the emitter absent,

    Hg = h0 tensor I + I tensor B + P0 tensor VA + P1 tensor VB,
    h0 = 2J I - J(S+S*),       B iota = iota K,
    K = 2I+Z1 Z2,             iota x=x tensor Omega,
    Omega=|00>_AB,            Hphysical=Hg+nu I.               (1)

The exact decimals are J=0.030021107107032 and
nu=1.459892813020969. The old/source dimension is sixteen, split into two
eight-dimensional parity blocks. For each old-energy incident channel the
other seven channels in its block are closed on |k-k0|<=10^-3, with gap
at least 0.18 and closed-root magnitude at most 1/7. Here

    q0=4.510351185997098,    k0=2 arctan(1/q0),
    z0=exp(ik0)=(q0^2-1+2i q0)/(q0^2+1),
    E(k)=2J(1-cos k),       E0=E(k0).                       (2)

The old target W and the one common scalar zeta stay those of the frozen
candidate. In absolute-site normalization r0(k)=-exp(2ik), and its original
gate has

    |r_j(k)-zeta omega_j r0(k)| <= 1.76*10^-13+702 sigma
                  for |k-k0|<=sigma<=10^-3.                (3)

The nonzero central ceiling is retained. No arbitrary-accuracy family is
inferred. The emitter may change the common spectral envelope and phase;
it has not been shown to create the particular parabolic finite vector in
the candidate. The generic bridge permits other common W^(1,1)_0 packets,
but their actual norms, derivatives, preparation error, and output phase
must be certified anew. The candidate's T=10^13 resource example cannot be
reused as an emission time.

## 2. One extra qubit, a square loop, and the full-qubit price

Fix an integer L>=3. Keep the gate end of the clock and bend the distant
path through

    c_L=(L,2,0),       c_(L+1)=(L+1,2,0),
    c_(L+2)=(L+1,3,0), c_(L+3)=(L+2,3,0),
    e=(L,3,0).                                               (4)

The remaining ray continues to the right. The emitter e is adjacent to c_L
and c_(L+2), so the two new bonds and two intervening clock bonds make a
square, not a forbidden nearest-neighbor triangle. This presumes available
vacant sites for the bend; it preserves the abstract path Hamiltonian h0.
It does not shorten the long clock or supply its vacuum.

Let kappa>0, 2kappa<=E0, and put phi=2k0. On the one-head graph consisting
of the clock path and e, the desired new terms, before a common scalar, are

    E0 |e><e| tensor I
      + kappa[(|L>-exp(i phi)|L+2>)<e|+h.c.] tensor I.      (5)

The old/source B acts also when the head is at e. In the physical qubits
that is automatic: B is an installed old/source term, independent of clock
occupation. Source-contact terms are still controlled only by n_c0,n_c1.

Write a=|0><1| and n=a^dagger a. For j=L,L+2 choose
t_L=kappa and t_(L+2)=-kappa exp(i phi), and use the positive blocks

    Q_ej=kappa(n_e+n_j)+t_j a_j^dagger a_e+conj(t_j)a_e^dagger a_j,
    (E0-2kappa)n_e,       kappa(I-n_L),       kappa(I-n_(L+2)). (6)

Each Q_ej has spectrum {0,2kappa} on its full two-qubit space. On the full
qubit space, summing (6) gives exactly

    E0 n_e + sum_(j=L,L+2)(t_j a_j^dagger a_e+h.c.) + 2kappa I.

Its one-head restriction is (5) plus 2kappa I. Total emitter-plus-clock
head number is conserved. The complete one-head Hamiltonian is therefore

    Htilde_physical=Htilde+(nu+2kappa)I,
    Htilde = Hg on the clock, B+E0 on e, with (5)'s hopping. (7)

In particular the physical scalar exp[-i(nu+2kappa)t] cannot be dropped.
The added positive-block incident norm sums are E0+2kappa at e and 3kappa
at each attachment clock site. Old and source incident loads are unchanged.
The old-cap 2 from the stationary witness still does not cap its source or
boundary-clock sites. This new cell neither changes that fact nor assumes
an all-site cap. Its coefficients are static, hence have zero runtime slew;
installation and precision remain assumptions.

The coupling phase is a physical permission. For t=|t|exp(i theta),

    t a_j^dagger a_e+conj(t)a_e^dagger a_j
      = |t|[cos(theta)(X_j X_e+Y_j Y_e)
             +sin(theta)(Y_j X_e-X_j Y_e)]/2.               (8)

The nontrivial phase around this loop cannot generally be removed while
keeping all four hoppings real. Native permission for these static
phase-dependent XY/cross-quadrature couplings is not established. No drive,
synthetic flux implementation, or irreversible sink is assumed implicitly.

The proposed ready state is

    |1>_e tensor |all clock zero> tensor Omega_AB tensor x_old,R. (9)

It is old-independent and is a one-qubit excited product seed, not an
initially entangled or phase-engineered two-site seed. It still assumes a
supplied clean clock/source vacuum, the excited emitter, and the coherent
static phase reference encoded in (6). It does not derive any of those
readiness resources from the framework.

## 3. Exact directional and return calculation on a uniform lead

This section concerns a full infinite uniform lead, with no gate or internal
closed channels. It is a local diagnostic, not an approximation already
certified for (7). Denote its operator on l2(Z) by
h_Z=2J I-J(S_Z+S_Z^*). Translation by L only changes unit phases, so set
L=0 when evaluating magnitudes. Define

    vvec=|0>-exp(i phi)|2>,
    g_+(k)=1-exp(i phi)exp(-2ik),
    g_-(k)=1-exp(i phi)exp(2ik),     vg(k)=2J sin k.        (10)

A mode exp(ikn) travels right; exp(-ikn) travels left toward the gate.
The plus form factor controls both rightward emission and excitation of
the emitter by a right-moving return. At the chosen center,

    g_+(k0)=0,       |g_-(k0)|=2 sin(2k0)>0.              (11)

This is one exact interference zero, not exact chirality on an interval.
On |k-k0|<=sigma with sigma<sin(2k0), the elementary Lipschitz estimates are

    a=|g_+(k)|<=2sigma,
    b=|g_-(k)|>=2sin(2k0)-2sigma,
    a/b<=eta:=sigma/[sin(2k0)-sigma].                     (12)

These bounds use no decay law. The exact retarded lead Green function is

    <n|(E(k)+i0-h_Z)^-1|m>=-i exp(ik|n-m|)/vg(k),
    Sigma(k)=<vvec|(E(k)+i0-h_Z)^-1|vvec>
            =-i[2-2cos(phi)exp(2ik)]/vg(k),
    D(k)=E(k)-E0-kappa^2 Sigma(k),
    -Im Sigma(k)=(a^2+b^2)/(2vg(k)).                       (13)

The first formula follows by solving the second-order recurrence and its
unit delta jump at n=m; it fixes the retarded sign. Feshbach elimination
of the single emitter then gives, in momentum-direction channel order,

    S(k)=I-i kappa^2 [g_+,g_-]^T [conj(g_+),conj(g_-)]
                                  /[vg(k)D(k)].          (14)

Equation (13) makes S^*S=I exactly. For a right-moving return, let t_+ be
the diagonal entry and r_+ the amplitude reflected back toward the gate.
The imaginary part of D, including at resonance, gives the uniform bounds

    |r_+| <= 2ab/(a^2+b^2) <= 2eta,
    |t_+-1| <= 2a^2/(a^2+b^2) <= 2eta^2.                 (15)

In particular t_+(k0)=1 and r_+(k0)=0 for every kappa>0. The opposite
transmission t_- can carry a substantial common phase. It must remain in
the eventual clock state. Lossless two-port unitarity also gives
|t_+|=|t_-| and equal reflection magnitudes. This is not an isolator.

The emitter resolvent is G_ee=1/D. Its absolutely continuous spectral
density on this band follows from -Im G_ee/pi. Resolving the two outgoing
radiation directions in the same resolvent jump gives the weights

    dmu_e^+/dE=kappa^2 a^2/[2pi vg |D|^2],
    dmu_e^-/dE=kappa^2 b^2/[2pi vg |D|^2].                (16)

Equivalently these are the squared stationary outgoing amplitudes obtained
from the same rank-one resolvent; no flat-density or Markov replacement is
made. Thus, within this band, the wrong-direction continuum fraction is
at most eta^2/(1+eta^2)<=eta^2. Equation (16) does not assert that emission
has finished at any finite time. Since b is bounded away from zero, D has
strictly positive imaginary part here, so this free-lead emitter has no
seed point-spectral weight in the band. Outside it, bound states are allowed.
The installed gate in (7) requires its own analysis.

For comparison, a single real point attachment has a=b=1. Reflection
symmetry gives equal left/right outgoing weights. At E=E0 its uniform-lead
self-energy is -i/vg, so t=0 and r=-1 exactly, for every kappa>0. Weakening
that contact does not repair either the bypass branch or resonant return
reflection. The particular two-contact zero (11) removes these two free-lead
defects without postselecting an emission direction.

## 4. A numerical scale check, and a bound that already survives the gate

Choose only for this diagnostic

    sigma=10^-6,        kappa=10^-12,       v=1/40.        (17)

The exact rational z0 fixes sin(2k0) without trigonometric roundoff. The
code checks the following strict rational ceilings, not floating enclosures:

| Free-lead quantity on the entire packet band | Certified ceiling |
|---|---:|
| eta in (12) | <1.31*10^-6 |
| Return-reflection amplitude | <2.62*10^-6 |
| Return-transmission amplitude difference from 1 | <3.44*10^-12 |
| In-band wrong-direction continuum fraction | <1.72*10^-12 |

There is also an exact installed-system energy-concentration estimate.
Let u_j=iota e_j, B u_j=b_j u_j, and Eseed e_j=|e> tensor u_j. With
c_j=b_j+E0+nu+2kappa, direct application of the full physical Hamiltonian is

    (Htilde_physical-c_j)Eseed e_j
       =kappa(|L>-exp(i phi)|L+2>) tensor u_j,
    ||(Htilde_physical-c_j)Eseed e_j||^2=2kappa^2.         (18)

The old/source interaction need not commute with K for (18): all gate
contacts vanish on the initially empty clock, and B u_j=b_j u_j is exact.
The spectral theorem therefore bounds the norm outside the total-energy
interval b_j+nu+2kappa+E([k0-sigma,k0+sigma]) by

    sqrt(2)kappa/dE <= sqrt(2)kappa/(v sigma) <6*10^-5.    (19)

Here E is increasing and E'>=v on the band. This includes out-of-band
point spectrum; it does not exclude in-band point spectrum or source
entanglement. The two parity blocks remain reducing after adding (5).
There are two old-energy columns per parity block, so the safe operator
bound for the map of discarded column parts is

    sqrt(2)*sqrt(2)kappa/(v sigma)=8*10^-5,                (20)

not the single-column ceiling. Within a parity block the discarded parts
are not assumed orthogonal. Every old/reference input is covered by the
operator bound. Small energy spread is not a certificate that the old
gate has run once, that the emitter has emptied, or that the output is
an old-independent clock packet.

The numbers (17)-(20) are not an emission-time or apparatus-size example.
No exponential decay rate is used to convert them into one.

## 5. Returning waves and the actual unresolved composition

Even in a scalar single-channel reduction one must keep repeated gate
visits. With propagation phases absorbed into R_G, |R_G|=1, the exact
stationary series for a two-port emitter to the right of a reflecting gate is

    R_total=r_- + t_+ R_G (1-r_+ R_G)^-1 t_-.             (21)

The inverse is a convergent geometric series if |r_+|<=r_*<1. Visits after
the first have total amplitude at most r_*/(1-r_*); the prompt reflected
branch r_- is also present. They can implement extra old gates and cannot
be absorbed into an unexamined common clock phase. For example, (15) gives
the scalar bound

    |R_total-R_G t_-|
       <=r_*+2eta^2+r_*/(1-r_*).                          (22)

Replacing t_- by its unit-modulus phase costs at most r_*^2, since
1-|t_-|<=|r_+|^2. Equations (21)-(22) are exact for the scalar two-port
composition with the stated factors; they have not been proved to describe
all channels of (7). In particular the initial emitter's radiation is not
an external incident wave independent of subsequent feedback.

In (7) the couplings act as identity on the *whole* old/source space. A
source-vacuum projector inserted on those bonds would be a different
interaction with a new many-body permission. The actual returning field
can contain closed-channel tails and transient source excitation, which
couple to the additional internal states of the emitter sector. A large L
suppresses closed tails but does not remove the open propagating feedback.
Moreover increasing L changes travel time and derivatives of propagation
phases. It cannot be declared harmless without a joint bound.

There is a compact exact starting point. For lambda in an incident band
let V=|v_L> tensor I, v_L=|L>-exp(i phi)|L+2>. The finite emitter resolvent
is governed by the 16-dimensional matrix (eight in each parity block)

    D_e(lambda)=(lambda-E0)I-B
                 -kappa^2 V^*(lambda+i0-Hg)^-1 V.         (23)

For the original gate's unit-incoming column phi_j^g(k), the emitter
component of the augmented scattering solution is exactly

    y_ej(k)=kappa D_e(lambda_j(k))^-1 V^*phi_j^g(k),
    lambda_j(k)=b_j+E(k).                                 (24)

The gate's certified finite matching and closed roots can evaluate (23)
without a long finite-time simulation. But its inverse is a new certificate:
at kappa=0 the open emitter coordinate is resonant, so the old matching
inverse bound 366 cannot be carried over by a naive small-perturbation
argument. The resonant coordinate must be treated separately, with its
optical imaginary part and coupling to the other internal coordinates.

For clarity, the already-certified original gate gives the genuine partial
bound, valid for L>=3,

    V^*phi_j^g(k)
      =[conj(g_-(k))+r_j(k)conj(g_+(k))]u_j + d_closed,j(k),
    ||d_closed,j(k)|| <=16*(50/49)*7^(-(L-2)).             (25)

The g's here include the translation phases exp(+-ikL). Equation (25)
uses its closed coefficient norm <=16, |q_l|<=1/7, and
q_l^(L-2)(1-exp(-i phi)q_l^2) for each tail. A sufficient derivative bound is

    ||d_closed,j'|| <=[700*(50/49)+16/(84)]*7^(-(L-2))
                 +[16*(L-2)*(50/49)/24]*7^(-(L-3)).        (26)

The last term in the first bracket is 16*2*(1/7)*(1/24).
This is a bound on the background driving vector, not on the inverse in
(23), the completed emission, or all delayed returns. It does not supply
the missing complete-output certificate.

## 6. The sufficient certificate must concern the actual initial seed

An adequate future certificate must do more than show nonsingular stationary
matrices on a momentum grid. It must establish, on a common interval I,

1. Exact selfadjoint full-qubit coefficients, conserved total head number,
   the stated vacuum-input identity, and the same reducing parity blocks.
   The additional loop phase and readiness resources must be allowed.
2. Uniform invertibility and derivative bounds for the *augmented* finite
   matching problem, such as a rigorously controlled Schur treatment of
   (23). Include every internal old/source direction and both attachments.
3. A common complex spectral envelope f and common unit-modulus phase
   rho(k), with finite W^(1,1) and C^1 bounds as specified below. They must
   approximate the actual one-qubit seed and the actual full reflection
   columns in operator norm. The different old energies cannot each be
   assigned a separate fitted envelope or scalar phase.
4. Quantitative late-time escape constants for the interaction region,
   closed tails and emitter. These give a finite onset time directly;
   an assumed Markov lifetime does not substitute for them.

The following implication makes these requirements testable. It is an
extension of the frozen bridge's proof to a finite attached graph, stated
here as a new conditional author lemma, not as a reviewed theorem already
satisfied by this emitter.

## 7. Conditional complete-output implication, with a seed-overlap test

Use Htilde without its common scalar. Suppose its unit-incoming scattering
columns Phi_j(k) have the same energies lambda_j(k)=b_j+E(k), exactly one
propagating channel in each selected block, and satisfy

    Phi_j(k,n)=[exp(-ikn)+R_j(k)exp(ikn)]u_j+C_j(k,n),
    Phi_j(k,e)=C_j(k,e).                                  (27)

The localized vector C_j includes the whole finite core 0,...,L+2, the
emitter, and every closed tail. Assume uniformly C^1 Hilbert-space bounds
||C_j||<=C0_j, ||C_j'||<=C1_j, |R_j'|<=L_Rj. These follow from an actual
uniform inverse bound on the finite matching matrix, not merely its point
invertibility. The current identity gives |R_j|=1.

Choose one f in W^(1,1)_0(I), ||f||2=1, and define

    Gamma_t e_j=(1/sqrt(2pi)) integral_I f(k)Phi_j(k)exp[-iE(k)t] dk.
    F0=||f||1, F1=||f'||1, 0<v<=min_I E', E2>=max_I |E''|. (28)

These are certified lower/upper velocity bounds as in controlling V2.
The bridge's past-limit argument applies unchanged: the incident wave is
normalized on the full line, its excluded half-line tends to zero in the
distant past, and the reflected and localized terms tend to zero by
integration by parts. The emitter is included in the localized term.
Selfadjoint evolution then proves

    Gamma_t^*Gamma_t=I,
    exp(-it Htilde)Gamma_0=Gamma_t exp(-it Db),
    Db=diag(b_j).                                         (29)

No scattering completeness or commutation of K through the interaction is
needed. Exact packet columns are orthogonal to normal bound eigenvectors
by the same weak-past-limit argument.

The finite matrix that tests the *physical seed* is

    A=Eseed^* Gamma_0,
    A_lj=(1/sqrt(2pi)) integral_I f(k)<u_l,Phi_j(k,e)> dk,
    ||Eseed-Gamma_0||^2=||2I-A-A^*||.                      (30)

Both maps in (30) are isometries, which proves the identity. Thus a rigorous
upper bound ||2I-A-A^*||<=eta_seed^2 is sufficient. Interval quadrature
with controlled tails and an operator bound, rather than separate column
phases or diagonal overlaps alone, can certify it. The parities may reduce
the matrix to two 2-by-2 blocks. This overlap requirement has not been
checked. It captures out-of-band weight, possible bound states, incomplete
emission preparation and old-dependent spectral shape in one actual norm.

Suppose also that a single rho in C^1(I), |rho|=1, |rho'|<=L_rho, obeys

    max_j sup_I |R_j(k)-zeta omega_j rho(k)|<=Delta_aug.    (31)

The physical gate's fixed zeta is retained; emitter propagation and its
common spectral phase belong in rho or f. If (31) is obtained by comparison
to the old gate plus an emitter correction, Delta_aug must include the
original ceiling (3). No independent per-column scalar choice is allowed.
Define

    A0=F1+(E2/v)F0,
    B0=F1+(L_rho+E2/v)F0,
    D_j=F1 C0_j+F0 C1_j+(E2/v)F0 C0_j,
    D=max_parity sqrt(sum_(j in parity) D_j^2),
    b_t(n)=(1/sqrt(2pi)) integral_I f(k)rho(k)exp[ikn-iE(k)t] dk,
    beta_t=b_t/||b_t|| on n>=0, with emitter unoccupied.  (32)

The negative-site restriction of the full-line b_t has norm at most
B0/sqrt(pi v t); the unwanted incoming wave on n>=0 has norm at most
A0/sqrt(pi v t). The localized operator has norm at most
D/[sqrt(2pi)v t]. These follow by precisely the integration-by-parts
estimates in the bridge, applied also to f rho. The within-parity square
sum is required because localized error columns need not be orthogonal.
The open output columns are orthogonal, and use the maximum in (31).

For vt>=1 and B0/sqrt(pi v t)<=1/2, beta_t is well-defined. Full-line
Parseval gives ||b_t||^2=1-||b_t on n<0||^2, so normalizing it costs at
most B0/sqrt(pi v t). Combining (29)-(32) yields, for every t>=T satisfying
these inequalities,

    ||exp(-it Htilde_physical)Eseed-Uideal(t)||
       <=eta_seed+Delta_aug+(A0+B0)/sqrt(pi v t)
                                  +D/[sqrt(2pi)v t],
    Uideal(t)x=zeta exp[-i(nu+2kappa)t]
                  beta_t tensor iota exp(-itK)W x.        (33)

All emitter, clock, source, old and passive-reference outputs remain in
this comparison. Old evolution is measured from the initial product seed:
t is the entire physical time, including emission and flight. There is no
reset of its age at an arbitrarily chosen collision time. Tensoring a
reference preserves (33); complete unhalved trace distance is at most
twice its right side. The infinite-apparatus bound-state amplitude is at
most eta_seed, already counted in (33), and is not discarded separately.

For example, an escape term at most epsilon follows from the sufficient
finite condition

    T>=max{1/v, 4 B0^2/(pi v),
           4(A0+B0)^2/(pi v epsilon^2),
           2D/[sqrt(2pi)v epsilon]}.                      (34)

This is a finite-time formula *after* the constants and (30)-(31) are
certified. None of eta_seed, Delta_aug, C0_j, C1_j, L_rho for the installed
emitter has been bounded here. Consequently (34) is not yet a finite
resource example or a proof that the proposed emitter meets the target.

## 8. Finite apparatus and the next bounded decision

One finite-horizon consequence is available without a decay model. Keep
clock sites 0,...,M-1 with M>=L+3, retain e, and use the true compression
of (7), including the usual far-end clock diagonal J n_(M-1). From the
seed e the first omitted clock site c_M is exactly

    d_M=M-L-1

graph hops away, via e,c_(L+2),...,c_M. The other route is two hops longer.
Internal old/source matrices do not move head support. The frozen gate's
spectral radius bound 18 also contains the decoupled B+E0 emitter block
about the same center; the added off-diagonal norm is sqrt(2)kappa. Thus
rho_star=19 is sufficient for (17), with the common scalar shifting the
spectral center only. The bridge's polynomial/Chebyshev argument gives

    ||exp(-it Htilde_physical)Eseed
        -embed exp(-it Htilde_physical,M)Eseed||
      <=4 exp[-mu d_M+19t sinh(mu)]/[1-exp(-mu)]            (35)

for mu>0,t>=0. Given a separately certified T and an observation horizon
Tobs>=T, a chosen finite M can make (35) small on [T,Tobs]. A fixed finite
chain is not covered for all future times. Since the infinite-emitter
certificate (30)-(31) is still absent, no finite M is advertised as a
working autonomous gate size.

The next useful bounded decision is to fix one L,kappa,sigma and certify
(23), its derivatives, and the seed overlap (30), including all sixteen
internal directions. A scalar linewidth estimate or a long-time simulation
that omits the wrong branch, emitter, or closed source channels would not
settle that question. If the required loop phase is unavailable, this
particular one-qubit route lacks a physical permission. Surviving alternatives
include a separately supplied two-site phase-engineered seed or the already
known driven preparation routes, each with its different readiness costs.
They are not analyzed or declared successful here.

## 9. Evidence and literature limits

`emitter_algebra_check.py` performs one exact bounded check. Its largest
matrix is 16 by 16, covering all four plaquette qubits. It verifies the
positive-edge polynomial identity Q^2=2kappa Q, the scalar identity (6)-(7),
head conservation, the exact directional zero, the optical identity and
two-port unitarity, and the rational strict ceilings in section 4. Two
exact on-shell points test the scattering algebra; they are not an interval
grid. The band bounds come from (12)-(15), with exact rational comparisons.

The single execution exited 0 in approximately 1.124 seconds of wrapper wall time.
Caps were 10 CPU seconds and 30 wall seconds; no optimizer, finite-chain
simulation or search over designs was used. Python 3.13.5 and SymPy 1.14.0
performed exact rational arithmetic. Full stdout, stderr, actual script
and runtime identities are retained in `algebra.stdout`, `algebra.stderr`,
`EXECUTION.json` and `ALGEBRA_CERTIFICATE.json`. `display_only` fields are
rounded displays and are never used as rigorous enclosures. The check is
source-exposed author verification, not independent review.

A narrow primary-literature search was used for the mechanism and its
known limitations. Chen et al., [Nonreciprocal and chiral single-photon
scattering for giant atoms](https://arxiv.org/abs/2203.00823v2), distinguish
local coupling phases from nonreciprocal transmission: their two-level
model also needs external dissipation for the latter. No dissipative
isolator result is imported here. Li and Shen, [Non-Markovian dynamics
with a giant atom coupled to a semi-infinite photonic waveguide](https://arxiv.org/html/2404.07890v1),
analyze reflected-field reabsorption and bound states. Their waveguide
calculation linearizes dispersion and extends its momentum integral;
its delay equation is not a theorem for this finite-band lattice. The
present Green-function and norm calculations were derived directly for
the stated lattice model. Neither source supplies the missing installed
old/source certificate or native couplings. Search scope is recorded in
`LITERATURE_NOTES.md`.

All writes are confined to this route directory. No original source,
repository, Git state, prompt, axiom, checkpoint or audit record changed.
~~~~
<!-- END UNCHANGED SOURCE: autonomous_emitter_route/ROUTE.md -->

### Unchanged source: `emitter_installed_certificate/CANDIDATE.md`

<!-- BEGIN UNCHANGED SOURCE: emitter_installed_certificate/CANDIDATE.md; bytes=30796; sha256=4361797e3896c5301d899d57824991dc2fd9263c7f4947fb87ddceabdef0a8ee -->
~~~~markdown
---
claim_type: conditional_author_theorem
actual_current_surface_status: new-author-work-awaiting-independent-review
native_preparation_claim: false
retained_audit_claim: false
---
# A uniform installed-emitter Schur certificate and a common product-seed envelope

The exact capped ladder with one added emitter does admit a uniform installed-system certificate at L=12, coupling kappa=10^-12, and momentum half-width sigma=10^-6. The resonant coordinate must be separated from the other seven emitter coordinates in each parity block. Its optical denominator stays bounded below even though a perturbation of the old matching inverse alone cannot establish this. Every one of the sixteen old/source directions is retained.

The resulting common envelope approximates the actual one-qubit product seed with isometry error below 0.003. The installed reflection columns share one phase with error below 0.000714, including the original positive central residual ceiling 1.76*10^-13. Explicit, deliberately loose derivative bounds give a complete-output isometry error below 0.004 for every t>=10^72 on the infinite clock. This huge sufficient time comes from integration by parts, not a linewidth or an assumed decay law. A finite horizon consequence is stated below.

This is a new source-exposed author derivation. Its analytic inequalities and bounded algebra checks have passed, but the installed-system argument has not received an independent review. The construction assumes a supplied clean clock/source vacuum, a supplied excited emitter, and the static complex loop couplings described below. It establishes neither native preparation of these resources nor a practical size or time. The frozen exploratory route is unchanged.

## 1. Exact dependencies and model

The controlling source copies are in `inputs/`; full identities and original paths are in `SOURCE_MANIFEST.json`.

| Source | SHA256 |
|---|---|
| `autonomous_emitter_route/ROUTE.md` | `f03626e591cddc3448bee72148edbee4717ae64af3a6543d4b5c184e7ef9f0a1` |
| Its `FREEZE.json` | `f5278acb3899cb2749009031c5cff5fd24f72a05d539aa0f3957c6a500af04db` |
| `two_body_interval_bridge/CANDIDATE.md` | `b386126649516e533da29182a6cf9eac2da314538ae9b072a2262d7c5c78ed45` |
| Its `CERTIFICATE.json` | `a98e272fa5d65e6177670ce2dfb52498ed942b8bd9996a0b9b16838d4e0c2251` |
| Its input `rational_point_certificate.json` | `6f057d8a580217d29a09d7683462f5b35b71de093e75c8d07a12283cde33593f` |
| `finite_channel_wavepacket_bridge/THEOREM_V2.md` | `db1a25ee639337a99800f8b8c27dbf366861a6707116f559029697c9f8aaf0e3` |

The earlier packet theorem is used with its certified velocity lower bound and curvature upper bound, as specified in V2. The extension to a finite attached graph and the seed-overlap identity are equations (27)-(33) of the frozen emitter route. Those local formulas have separately been checked and provisionally qualified by root; that does not constitute an independent check of the new bounds here.

Use the exact old/source operator and positive physical blocks of the frozen ladder:

    Hg = h0 tensor I + B + P0 tensor VA + P1 tensor VB,
    h0 = 2J I-J(S+S*),   K=2I+Z1 Z2,
    B=K+C+G,    B iota=iota K,    iota x=x tensor Omega,
    Omega=|00>_AB,       Hphysical=Hg+nu I.                (1)

Here J=0.030021107107032 and nu=1.459892813020969 are exact. All other exact ladder coefficients are the pinned certificate's `exact_parameters`; no fit is changed. The old space has dimension four, the old/source space dimension sixteen, and P=X1X2 gives two reducing parity blocks of dimension eight. In either block the two source-vacuum old eigenvalues are 1 and 3. The contact interaction can mix these energies; no commutation of K with the full Hamiltonian is assumed.

Set

    q0=4.510351185997098,   k0=2 arctan(1/q0),  z0=exp(ik0),
    E(k)=2J(1-cos k),      E0=E(k0),            phi=2k0,
    L=12,   kappa=1/10^12,  sigma=1/10^6,
    I=[k0-sigma,k0+sigma].                                (2)

The rational values used in all comparisons are

    Re z0=4835816955256357129429116105401/
          5335816955256357129429116105401,
    Im z0=2255175592998549000000000000000/
          5335816955256357129429116105401,
    E0=30021107107032000000000000000/
          5335816955256357129429116105401.

Thus exp(i phi)=z0^2 is exact too. On the larger frozen band |k-k0|<=10^-3 the original certificate supplies

    closed-band gap g=9/50,   |q_closed|<=r=1/7,
    |q_closed'|<=1/24,       ||M16^-1||2<166,
    ||M16'||2<=2J/(1-r^2),  |r_j'|<=700,
    ||alpha_closed,j||<=16, ||alpha_closed,j'||<=700,
    ||C_g,j||<=31,          ||C_g,j'||<=2700.              (3)

There is exactly one propagating channel at lambda_j(k)=b_j+E(k) in each selected parity block, with b_j in {1,3}. The supplied gap applies to every other channel band. These bounds concern the full physical matrices, not rounded eigenvectors. Also

    0<v=1/40<E'(k),   |E''(k)|<=E2=2J,   E2/v<5/2.       (4)

The new head graph is the half-line plus one emitter e. Bend the path at the four sites

    c_L=(L,2,0), c_(L+1)=(L+1,2,0),
    c_(L+2)=(L+1,3,0), c_(L+3)=(L+2,3,0), e=(L,3,0).

The new two bonds complete a square. On the one-head sector define V=|L>-exp(i phi)|L+2>, tensored with the identity on all internal directions, and

    Htilde = [[Hg, kappa V], [kappa V*, B+E0]],
    Htilde_physical=Htilde+(nu+2kappa)I.                  (5)

The explicit full-qubit positive realization is retained from the route. For j=L,L+2, t_L=kappa and t_(L+2)=-kappa exp(i phi), use

    Q_ej=kappa(n_e+n_j)+t_j a_j^dagger a_e+conj(t_j)a_e^dagger a_j,
    (E0-2kappa)n_e,    kappa(I-n_L),    kappa(I-n_(L+2)).  (6)

Each Q_ej has norm 2kappa and is positive; E0>2kappa. The sum is exactly E0 n_e plus the two desired hoppings plus 2kappa I. It conserves total emitter-plus-clock head number. Its added incident positive-block norm sums are E0+2kappa at e and 3kappa at either clock attachment. Old/source loads are unchanged. The original added old loads are below 2, but its source and boundary-clock loads are not all below 2. The existing old edge is additional. No all-site cap 2 is claimed.

Complex XY/cross-quadrature bonds with this nontrivial loop phase are an explicit extra physical permission. They are not replaced by real native hopping. The initial ready isometry is exactly

    Eseed x=|1>_e tensor |all clock zero> tensor Omega tensor x. (7)

This is an old-independent one-qubit excited product seed. The clock/source vacuum, excitation, exact coefficients and their static phase relation are supplied assumptions. No external drive is applied after t=0, and no output is absorbed into a one-way sink.

## 2. Exact retarded matching, with the resonant coordinate visible

Fix a parity and incident old energy. All norms in this section are Euclidean operator norms in orthonormal physical coordinates. Let Pj=|u_j><u_j| on the eight-dimensional internal block and Pc=I-Pj. Let

    Q=z Pj+sum_closed q_l P_l,    z=exp(ik),
    A=[J(Q-Q^-1)]^-1,    A Pj=(-i/vg)Pj,   vg=2J sin k.

The fixed spectral projections of B are used only to define matrix functions; the proof does not require certified numerical eigenvectors. Closed channels satisfy ||Pc A||<=1/g by the full-line resolvent gap. Differentiation gives ||A||<=40, ||A'||<=100, using 2J/v^2<100 and 2J/g^2<100.

With M16 in the frozen physical convention, set

    R=M16^-1,   R11=E1* R E1,   T=R11-A,
    M16=[[lambda-2J-B-VA, JI], [JI, -JQ^-1-VB]],         (8)

where E1 embeds the internal coordinates at clock site 1. Then

    ||T||<=206,   ||T'||<2000,
    ||R'||<=166^2*2J/(1-r^2)<1710.                       (9)

The Dirichlet-tail recurrence and its unit delta jump give, for n,m>=2,

    Rg(n,m)=A Q^|n-m|+Q^(n-1) T Q^(m-1),
    Rg=(lambda+i0-Hg)^-1.                               (10)

For example the Dirichlet kernel has the first term minus Q^(n-1) A Q^(m-1); gluing sites 0,1 back adds Q^(n-1)R11 Q^(m-1). This fixes both signs without a scattering-completeness assumption. Define

    X=Q^(L-1)(I-exp(-i phi)Q^2),
    Y=Q^(L-1)(I-exp(+i phi)Q^2),
    Sigma_f=A[2I-2cos(phi)Q^2].

Consequently the full installed self-energy and emitter denominator are exactly

    Sigma_g=V*Rg V=Sigma_f+XTY,
    D_e=(lambda-E0)I-B-kappa^2 Sigma_g.                  (11)

Eliminating only the tail, not the emitter, gives the following actual physical matching matrix on (x0,x1,y_e):

    Maug = [[M16,                  -kappa E1 Y],
            [-kappa X E1*, (lambda-E0)I-B
                               -kappa^2(Sigma_f-XAY)]]. (12)

It has dimension 24 per parity, equivalent to a direct sum of two 24-dimensional blocks on the whole internal space. Its Schur complement is (11). The old bridge also used a matrix of dimension 24, but in a different unknown convention. Its bound 366 is not a bound for (12). No norm conversion between those unrelated unknown lists is used. Instead (12) has its own physical-coordinate norm bound below.

The open amplitudes

    g_plus=z^(-L)(1-exp(i phi)z^-2),
    g_minus=z^L(1-exp(i phi)z^2),
    a=|g_plus|,  b=|g_minus|,
    a_max=2sigma, b_min=2sin(2k0)-2sigma, b_max=2,
    eta=a_max/b_min                                      (13)

satisfy a/b<=eta. In particular a(k0)=0 and b_min>3/2. One has

    |X_open|=a, |Y_open|=b,
    ||Pc X||,||Pc Y||<=delta=(1+r^2)r^(L-1)
                            =50/96889010407,
    ||X||<=a_max, ||Y||<=2, ||X'||,||Y'||<=2L=24.         (14)

The inequality delta<a_max is explicitly checked. Differentiating the open power and closed spectral powers proves the last bound.

A sharper identity than ||T||<=206 is decisive:

    T_jj=(-i/vg) z^2 r_j.                               (15)

Indeed the original absolute-site incoming RHS is (i vg/z)E1u_j, so its site-1 component is (i vg/z)(R11)_jj=z^-1+r_j z. Rearranging gives R11_jj=(-i/vg)(1+r_j z^2), hence (15). Conserved flux gives |r_j|=1. This step keeps the entire gate/source interaction inside its actual reflection coefficient.

## 3. Uniform Schur inverse, closed directions, and bound states

Let Dq=Pc D_e Pc on its seven-dimensional range. Since E0 lies in [0,4J], the closed-band gap in (3) implies

    dist(lambda-E0, spectrum(B|Pc))>=g.

The closed self-energy obeys

    ||Pc Sigma_g Pc||<=Sqq=2(1+r^2)/g+delta^2*206,
    g-kappa^2 Sqq>1/6,       ||Dq^-1||<6.                (16)

This controls all seven coordinates, including the other vacuum old energy, without replacing them by a scalar spectator. The off-diagonal self-energies satisfy

    ||Pj Sigma_g Pc||<=sPQ=a_max*206*delta,
    ||Pc Sigma_g Pj||<=sQP=delta*206*b_max.               (17)

The free resonant denominator and its optical imaginary part are

    Df=E(k)-E0-kappa^2 (Sigma_f)_jj,
    Im Df=kappa^2(a^2+b^2)/(2vg)
          >=kappa^2 gamma0,
    gamma0=b_min^2/(4J)>19.549...>19.                    (18)

The only resonant scalar left after eliminating Pc is

    ds=Df-kappa^2 X_jj T_jj Y_jj
          -kappa^4 (Sigma_g)_jc Dq^-1 (Sigma_g)_cj.     (19)

By (15), the first subtracted term has magnitude kappa^2 ab/vg, at most 2eta Im Df. The second has magnitude at most kappa^4 sPQ*6*sQP. Thus, with

    xi_c=kappa^4 sPQ*6*sQP/(kappa^2 gamma0),
    xi=2eta+xi_c,

both |ds-Df|<=xi |Df| and

    Im ds >=kappa^2 gamma0(1-xi)>19 kappa^2             (20)

hold uniformly. The second assertion follows by comparing the first correction directly to Im Df, not by confusing a relative modulus bound with an imaginary-part bound. The exact rational check gives xi approximately 2.6106713073*10^-6.

The block triangular inverse factorization now gives

    ||D_e^-1|| <= (1+kappa^2 sPQ*6)(1+kappa^2 sQP*6)
                        /(19 kappa^2)+6
                 <1/(18 kappa^2),
    ||Maug^-1|| <=(1+166 kappa b_max)(1+166 kappa a_max)
                           /(18 kappa^2)
                  <1/(17 kappa^2).                      (21)

Here 166<1/(18 kappa^2), so the latter factorization controls the original block too. All norm comparisons are exact rational inequalities. Equivalently the smallest singular value of the precise matrix (12) exceeds 17 kappa^2. In particular this is a uniform interval bound, not a grid of nonsingular points.

An eigenvector at any selected-band energy would have zero open tail and a decaying closed tail. It would therefore solve the homogeneous outgoing matching equations (12). Invertibility forces its contact/emitter coordinates, and then its whole tail, to vanish. There are no installed bound states in either selected old-energy band in either parity. Outside those bands bound states are allowed.

For the physical product seed, exact application of (5) gives

    ||(Htilde_physical-b_j-E0-nu-2kappa)Eseed e_j||^2
          =2kappa^2.

The spectral theorem and (4) bound each column's amplitude outside its band by sqrt(2)kappa/(v sigma). There are two potentially nonorthogonal columns per parity, so the safe operator bound is 2kappa/(v sigma)=8*10^-5. Since no point eigenvalue lies in these bands, this also bounds the full point-spectral amplitude of the seed. It is not set to zero or postselected away. The overlap error below already covers it.

## 4. One common seed profile and the full operator overlap

Let Phi_j^g be the original unit-incoming stationary column. Direct substitution in the certified tail gives

    w_j=V*Phi_j^g=[conj(g_minus)+r_j conj(g_plus)]u_j+w_cj,
    ||w_cj||<=w_c=16(1+r^2)r^(L-2)=800/13841287201,
    ||w_cj'|| <=[700(1+r^2)+32r/24]r^(L-2)
                     +16(L-2)(1+r^2)r^(L-3)/24.         (22)

The augmented column is exactly

    y_j=kappa D_e^-1 w_j,
    Phi_j|clock=Phi_j^g+kappa Rg V y_j,
    Phi_j(e)=y_j.                                       (23)

Define the common scalar profile

    yref(k)=kappa conj(g_minus(k))/Df(k).                (24)

It is independent of j: all four columns have the same E(k), E0 and free form factor after their actual old energy b_j has been subtracted. Solving the two Schur rows, rather than declaring separate column phases, yields

    |(y_j)_j/yref-1|<=eta_p,
    eta_p=[eta+kappa^2 sPQ*6*w_c/b_min+xi]/(1-xi)
             <4*10^-6,
    ||Pc y_j||<=6 kappa w_c
               +6 kappa^2 delta*206*b_max*(1+eta_p)|yref|. (25)

The exact stored eta_p is approximately 3.9160171843*10^-6. None of the other emitter coordinates has been projected away in (25).

For normalization use the scalar full-line two-contact emitter, only as an exactly calculable reference spectral measure. Its emitter resolvent is 1/Df and its two continuum weights, in dk, are

    kappa^2 a^2/(2pi |Df|^2),
    kappa^2 b^2/(2pi |Df|^2)=|yref|^2/(2pi).             (26)

The retarded jump of 1/Df gives their sum. On the selected band its denominator has positive imaginary part and a smooth boundary value, so scalar Stieltjes inversion gives an absolutely continuous measure there. Its total spectral measure is one, including any outside-band point masses. No global scattering completeness or Markov law is imposed.

Set h=sigma/2. On |k-k0|<=h, the wrong-direction weight fraction is at most [h/(sin(2k0)-h)]^2. The reference seed variance is exactly 2kappa^2; therefore its spectral mass outside this inner energy band is at most 2kappa^2/(vh)^2. Choose the common real cutoff chi equal to one on |k-k0|<=h, linear down to zero on each remaining half-band, and zero outside I. Define

    N^2=(1/(2pi)) integral_I chi^2 |yref|^2 dk,
    f(k)=chi(k) conj(yref(k))/(sqrt(2pi) N),
    delta_m=2kappa^2/(vh)^2+[h/(sin(2k0)-h)]^2.           (27)

It follows rigorously that

    1>=N^2>=1-delta_m,   delta_m<13*10^-9,   N>0.99,
    ||f||2=1,   f in W^(1,1)_0(I),
    Aref=(1/(2pi N)) integral_I chi |yref|^2 dk in [N,1]. (28)

The lower Aref bound uses chi>=chi^2; the upper is Cauchy-Schwarz and the total mass bound from (26). No narrow-resonance quadrature is used.

Use this same f in every column and set

    Gamma_t e_j=(1/sqrt(2pi)) integral_I
                     f(k) Phi_j(k) exp[-iE(k)t] dk,
    Aseed=Eseed* Gamma_0.                                (29)

The regularity bounds in section 6 and the past-limit normalization proof of the pinned bridge show that Gamma_t is an exact isometry. Specifically the incident full-line packet is normalized, its excluded half tends to zero in the past, and reflected/localized parts tend to zero. Selfadjoint evolution then preserves the limiting inner products. This proof includes the emitter as a localized coordinate and does not require the scattering columns to span the whole Hilbert space.

Equation (25) bounds each diagonal entry of Aseed-Aref I by eta_p. Each off-diagonal entry inside a parity block is bounded by

    epsilon_off=6 kappa w_c
                  +6 kappa^2 delta*206*b_max*(1+eta_p)
                 <10^-18.                               (30)

Here ||f||1/sqrt(2pi)<=1 and integral |f yref|/sqrt(2pi)=Aref<=1 were used. Entries between parities vanish exactly. For a 2 by 2 block, the diagonal part has norm at most eta_p and the off-diagonal part norm at most epsilon_off. Consequently

    ||Aseed-Aref I||<=eta_p+epsilon_off,
    ||Eseed-Gamma_0||^2=||2I-Aseed-Aseed*||
         <=2(delta_m+eta_p+epsilon_off)
          <(3/1000)^2.                                  (31)

The exact squared ceiling before the last rounding is approximately 7.8576352206*10^-6. This is the requested full operator overlap test, not a diagonal-only or columnwise phase test. It covers arbitrary old states and passive references. The f in (27) describes the seed's common mathematical scattering envelope; an external apparatus is not asked to synthesize that packet. The physical readiness premise remains the supplied product state (7).

## 5. Complete reflection, returns, and the single common scalar

For n>=L+2, equation (10) gives

    (Rg V)(n)=Q^(n-L-2) Dtail,
    Dtail=A(Q^2-exp(i phi)I)+Q^(L+1)TY,
    brow=z^(-L-2) Pj Dtail,
    R_aug,j=r_j+kappa brow y_j.                          (32)

Selfadjoint current conservation for (5), including the complex loop bonds, gives |R_aug,j|=1. There is one open channel, closed tails carry no asymptotic flux, and there is no absorber.

The open coordinate of brow is exactly (-i/vg)(g_plus+r_j g_minus), by (15). Let

    t_minus=1+kappa^2(-i/vg)b^2/Df,
    tau=t_minus/|t_minus|.                              (33)

The free two-port optical identity gives |t_minus|^2=1-|r_free|^2, with |r_free|<=2eta. Thus |t_minus|>1/2 and replacing it by tau costs at most 4eta^2. Substituting (24)-(25) into (32) gives the explicit full-system estimate

    |R_aug,j-r_j t_minus|
       <=2eta+2(1+eta)eta_p+epsilon_closed,
    epsilon_closed=6 kappa^2*206*delta*w_c
          +6 kappa^2 delta^2*206^2*b_max*(1+eta_p)*(4J/b_min).

The first term is the prompt emitter-reflected amplitude. The second controls the actual change of the resonant coordinate, including repeated open feedback. The last term is the complete closed-coordinate contribution. They follow from the exact resolvent (23), so no returning pass is dropped from a path sum. In the second term of epsilon_closed one uses |yref|<=2vg/(kappa b) and vg<=2J. Hence

    |R_aug,j-r_j tau|<=epsilon_phase
       =2eta+2(1+eta)eta_p+epsilon_closed+4eta^2
          <11*10^-6.                                    (34)

Retain precisely the old target

    W=((9+12i)I+(-16+12i)X1X2)/25,
    omega_+=(-7+24i)/25, omega_-=1,
    zeta=-exp(-4ik0) alpha,
    r0(k)=-exp(2ik),     rho(k)=r0(k) tau(k).             (35)

Here alpha is the exact unit reflection of the frozen (s=-1,p=-1) witness in its site-1 normalization. Multiplying that stationary column by exp(-ik) converts to absolute-site normalization and r_abs=exp(-2ik)r_site1. Thus zeta in (35), not alpha alone, is the fixed target scalar. This is the same scalar as the frozen interval theorem. Its physical vacancy scalar remains separate.

The original comparison and (34) now imply on the entire I

    max_j |R_aug,j-zeta omega_j rho|
        <=1.76*10^-13+702 sigma+epsilon_phase
          <714/10^6.                                    (36)

One rho and one f serve all four channels. No old-dependent phase fitting, exact chirality on an interval, arbitrary exact calibration or irreversible sink is used.

## 6. Explicit regularity and complete localized tails

This section supplies conservative constants so that the seed-overlap and late-time claims have checked hypotheses. Differentiating (11)-(14) gives

    ||Sigma_g'||<11000,   ||D_e'||<0.061,
    ||Maug'||<0.063,
    ||w_j||<3, ||w_j'||<30,
    ||y_j||<=1/kappa, ||y_j'||<=1/kappa^3.                (37)

For example ||Sigma_f'||<=4*100+4*40=560; the XTY derivative is bounded by 24*206*2+a_max*2000*2+a_max*206*24. The inverse derivative is -D_e^-1 D_e' D_e^-1. Its substitution with (21) verifies the last two generous bounds in (37).

Let Kloc map an emitter-coordinate vector y to Rg V y minus its outgoing open wave on every clock site, including sites 0 and 1. On sites 0,1 the unsubtracted stack is R E1Y, with norm <=332 and derivative <7404. On each site 2 through L+1 it has norm <=492 and derivative <16000. The outgoing coefficient obeys

    ||Dtail||<=492, ||Dtail'||<=14580,
    ||brow||<=492,  ||brow'||<=21468.                    (38)

For n>=L+2 the subtracted expression is exactly the closed tail Q^(n-L-2)Pc Dtail. Its norm and derivative sums use

    sum_(m>=0) r^(2m)=1/(1-r^2),
    sum_(m>=1) m^2 r^(2m-2)=(1+r^2)/(1-r^2)^3.

Their square roots are below 1.011 and 1.05. Adding the finitely many earlier coordinates by the triangle inequality yields

    ||Kloc||<20000,       ||Kloc'||<10^6.                (39)

For clarity, the actual positive upper expressions checked are

    K0<=332+2*492+L*(492+492)+492*1.011,
    K1<=7404+492+2*21468
          +L*[16000+(L+1)*492+21468]
          +14580*1.011+492*(1/24)*1.05.

The augmented localized correction is C_g,j+kappa Kloc y_j on the clock and y_j on the emitter. Thus its full Hilbert-space bounds, retaining all source outputs and every closed tail, are

    ||C_aug,j||<=31+(1+20000 kappa)/kappa <C0=2*10^12,
    ||C_aug,j'||<=2700+kappa*10^6/kappa
                         +(1+20000 kappa)/kappa^3
                      <C1=2*10^36,
    |R_aug,j'|<700+kappa[21468/kappa+492/kappa^3]
                 <1000/kappa^2.                         (40)

The scalar Df has derivative magnitude below 0.061. From (24), |yref|<=1/kappa and |yref'|<=1/kappa^3. Since ||chi'||1=2 and sqrt(2pi)N>2, (27) gives

    F0=||f||1<1/500,
    F1=||f'||1<=1/kappa+sigma/kappa^3<2*10^30.            (41)

Differentiating (33) bounds

    |t_minus'|<=720/19+160*0.061/(19^2 kappa^2)<1/kappa^2,
    |rho'|<=2+4/kappa^2<5/kappa^2=:Lrho.                 (42)

The first inequality uses ||A_open'||<=100, b<=2 and |(b^2)'|<=8. All coefficients are C^1 on the compact band; the cutoff is Lipschitz with zero endpoint trace. Equations (37)-(42) are consequently sufficient for the bridge's Hilbert-valued integration by parts.

## 7. Conditional complete-output result, actual aging, and a finite horizon

Let b_t(n)=(1/sqrt(2pi)) integral_I f(k)rho(k) exp[ikn-iE(k)t] dk on n>=0 and let beta_t=b_t/||b_t||, embedded with emitter unoccupied. Define

    Uideal(t)x=zeta exp[-i(nu+2kappa)t]
                   beta_t tensor iota exp(-itK)W x.      (43)

The complete-output estimate concerns the full graph, old system, both source qubits, and an arbitrary passive reference. The source is compared to its actual vacuum in the ideal state; it is not traced out to claim success. The old factor uses the entire elapsed time from the seed at t=0, including emission and flight. It follows from the exact column intertwining

    exp(-it Htilde)Gamma_0=Gamma_t exp(-it diag(b_j)),

not from an invalid commutation of K through the interacting Hamiltonian.

Set the conservative packet constants

    A0=B0=3*10^30,
    Dj=F1*C0+F0*C1+(5/2)F0*C0<5*10^42,
    D=8*10^42>sqrt(2) max_j Dj.                          (44)

There are two localized error columns per parity; (44) pays their square-sum factor, with no assumption that they are orthogonal. Distinct parities are orthogonal. Open outgoing vacuum columns are orthogonal and use the maximum in (36).

The exact isometry normalization and integration-by-parts estimates of the pinned bridge and route give, whenever vt>=1 and B0/sqrt(pi vt)<=1/2,

    ||exp(-it Htilde_physical)Eseed-Uideal(t)||
       <=0.003+0.000714+(A0+B0)/sqrt(pi vt)
                                    +D/(sqrt(2pi)vt).   (45)

This follows by applying unitary evolution to (31), then estimating the unwanted incoming half-line wave, the normalized outgoing wave, and the localized part in (29). The normalization cost is bounded by the negative-half-line norm of the full-line outgoing Fourier packet. The exact scattering packet is orthogonal to normal bound eigenvectors by the past-limit argument; any seed point amplitude is included in (31), with the sharper separate bound 8*10^-5 from section 3. It is not added twice or omitted.

For the declared finite sufficient onset

    T=10^72,

the exact inequalities (27*10^34)^2<3vT, pi>3, sqrt(2pi)>12/5 show that the final two terms in (45) are at most

    6*10^30/(27*10^34)+8*10^42/[(12/5)vT]
       =500000000000000000000003/22500000000000000000000000000.

The whole right side is at most

    84065000000000000000000003/22500000000000000000000000000
        <0.004                                             (46)

for every t>=T. Complete unhalved trace distance is therefore below 0.008. These costs are intentionally poor sufficient analytic bounds; there was no long-time dynamics simulation and no claim that T is close to the actual emission or gate time.

For a finite device retain clock sites 0,...,M-1 and e, using the actual compression of the same Hamiltonian and the far-end clock diagonal J n_(M-1). The radius 19 about the old certificate's spectral center contains both the decoupled clock and B+E0 emitter spectra plus the off-diagonal perturbation of norm sqrt(2)kappa. The physical common scalar changes that center only. From the seed e the first omitted clock site c_M is exactly

    dM=M-L-1

graph hops away, through c_(L+2). The other route is two hops longer. The polynomial/Chebyshev argument therefore bounds the embedded finite versus infinite evolution by

    4 exp[-dM+19t sinh(1)]/[1-exp(-1)].                   (47)

Choose integers

    Tobs=2*10^72,        M=5*10^73.

The checked strict inequality dM>19*Tobs*(6/5)+9, together with the inherited elementary bounds sinh(1)<6/5 and log[4/((1-exp(-1))*10^-3)]<9, makes (47) less than 0.001 throughout [T,Tobs]. Thus that embedded finite output has complete isometry error below 0.005 and unhalved trace error below 0.01 on this finite time interval. The comparator in (43) remains the normalized half-line output. This is a finite existence example, not a hardware resource proposal; no matrix of size M was created. No fixed finite device is claimed to satisfy (46) for all future times.

## 8. Bounded evidence, independence limits, and remaining obligations

`CAPS.json` was written before computation: 30 CPU seconds, 60 wall seconds, maximum executed dimension 48, three diagnostic momenta times four sectors, no optimizer and no time evolution. The actual largest executed matrix was 24. The one execution of `certify_installed_emitter.py` exited 0 in 2.565229 seconds of wrapper wall time (2.431585 seconds reported by the program). Python 3.13.5, SymPy 1.14.0 and mpmath 1.3.0 were used. `run01_execution.json` records the command, binary hash, source hash, environment and output hashes. The script's SHA256 is `950973354e69857ab19e40dbbf185ada46d1cda8a8a6c201c35fecf97a74623c`.

All uniform numerical ceilings are exact Fraction comparisons. In particular `display_float` entries in `CERTIFICATE.json` are rounded displays, not outward enclosures. The interval argument is (16)-(21), not a nonsingularity grid. The code additionally performs two distinct checks:

1. Exact finite elimination on the actual L=12 attachment geometry, using a scalar closed lead q=3/5, J=1, kappa=1/10 and non-real phase (3+4i)/5. Direct elimination of sites 2,...,14 in a 16-dimensional matrix with the exact outgoing Robin boundary gives (12) and its emitter Schur complement identically. This tests the signs and coordinate convention by a separate finite computation; it is not the physical interval proof.
2. Full physical matrices at k0 and k0+-10^-6 in all four (old-energy, parity) sectors, at 90 decimal digits. The code retains every closed channel, checks the augmented inverse against its Schur complement, verifies (15), evaluates the profile comparison and checks flux. The largest inverse residual was below 3*10^-81 and the largest observed relative profile error below 1.306*10^-6. These floating diagnostics are not substituted for rigorous enclosures. Full sixteen-dimensional B, its vacuum identity and its exact parity reductions are also checked symbolically.

Full stdout and stderr are preserved as `run01.stdout` and `run01.stderr`; the actual executed source is copied to `run01_script.py`. `CERTIFICATE.json` is the unchanged JSON stdout. No failed numerical run, discarded search candidate, optimizer, unreported retuning or alternative installation was used in this bounded step. The earlier one-point-emitter failure remains in the unchanged exploratory route.

The main independent-review targets are the noncommuting matrix tail gluing in (10)-(12), the resonant/open-closed Schur bounds, the common-envelope spectral-mass argument and the full operator overlap in (31), and the complete-localized regularity/normalization chain leading to (45). The distinct algebra calculation is a useful sign check but does not make this author's derivation independent of itself. The inherited model and reasoning effort were preserved; there was no delegation or model override.

Within this conditional mathematical model, the former installed inverse, common overlap and finite-time constant obligations now have explicit proposed certificates. Independent review of this new theorem remains required before accepting them. Physical permissions still open are the supplied clean vacuum and excited seed, exact static complex loop couplings and ladder coefficients, apparatus construction/precision, and any native interpretation or practical optimization. No uniform fit family, arbitrary accuracy below the fixed central ceiling, reset, reuse, selected classical Record, noise robustness, or global source/clock cap is inferred. The source qualification of earlier work does not grant these permissions.

All writes in this step are confined to `emitter_installed_certificate/`. The frozen route and original sources are unchanged. No repository, Git state, PR, prompt, axiom, audit or shared checkpoint was edited.
~~~~
<!-- END UNCHANGED SOURCE: emitter_installed_certificate/CANDIDATE.md -->

### Unchanged source: `weighted_emitter_escape_candidate/CANDIDATE.md`

<!-- BEGIN UNCHANGED SOURCE: weighted_emitter_escape_candidate/CANDIDATE.md; bytes=10962; sha256=a2e96d2947b1e0deef2417d4673ddc8afd54f7382236aee6913ba6cae98e32b5 -->
~~~~markdown
---
claim_type: proposed_bounded_theorem
actual_current_surface_status: unreviewed-author-work
independent_review: pending
---
# Weighted emitter integrals give a smaller sufficient escape time

This is a root-authored proposed refinement of the installed-emitter argument,
not a qualified result. Its complete installed-system dependency is
`emitter_installed_certificate/CANDIDATE.md`, SHA256
`4361797e3896c5301d899d57824991dc2fd9263c7f4947fb87ddceabdef0a8ee`.
That new theorem is itself undergoing a separate check. The original source
files are unchanged. This refinement keeps exactly the same Hamiltonian,
product seed, common spectral envelope, complete comparator and error
contract. Only the sufficient analytic escape time and associated finite
clock horizon are changed.

The proposed result is: under every premise and certified inequality of that
installed theorem, its complete isometry error is below 0.004 for every
t>=10^36 on the infinite clock. A finite clock with M=5*10^37 sites gives
error below 0.005 for 10^36<=t<=2*10^36 in the same output embedding.
These are sufficient mathematical bounds in the declared units, with no
large-clock evolution or practical resource claim. The earlier 10^72 bound
remains valid if its own theorem is accepted; this argument does not refute it.

## 1. Fixed premises and the integral that is actually needed

Use kappa=10^-12, sigma=10^-6, v=1/40, L=12 and the exact original ladder,
loop phase, emitter energy, vacuum and one-excited-emitter product input. Use
the same old K and W, the same physical scalar nu+2kappa and the same common
envelope and output phase from the installed source:

    Df=E(k)-E0-kappa^2 Sigma_f,jj(k),
    yref=kappa conjugate(g_minus)/Df,
    f=chi conjugate(yref)/(sqrt(2pi) N),
    rho=r0 t_minus/|t_minus|,
    t_minus=1-i kappa^2 |g_minus|^2/(vg Df).

Here chi is one on the central half of I and linear to zero at the two
endpoints of I=[k0-sigma,k0+sigma]. Its pointwise derivative is bounded by
2/sigma almost everywhere. The actual N and f are the source's normalized
ones, not a replacement fitted packet. In particular sqrt(2pi)N>2 and
F0=integral |f|<1/500 are inherited.

For a fixed old/parity column let C_j(k) be the complete localized correction
after subtracting its incoming and outgoing open waves on all clock sites.
It includes the emitter coordinate and every closed source tail. The direct
Hilbert-valued integration by parts uses

    D_j = integral_I [ |f'| ||C_j|| + |f| ||C_j'||
                                   +(E2/v)|f| ||C_j|| ] dk.       (1)

The old estimate F1 C0+F0 C1+(E2/v)F0 C0 is a sufficient upper bound for
(1). We instead keep the correlated denominators in these products. This
does not change the integration-by-parts identity or weaken its hypotheses.
Likewise the outgoing half-line estimate uses

    B0 = integral |f'| + integral |f| |rho'| +(E2/v)F0,          (2)

and the incoming estimate uses A0=integral |f'|+(E2/v)F0.
The proof of these estimates requires only the displayed integrability and
zero endpoint trace; it does not require taking a separate supremum of
rho' before integration. E2/v<5/2 remains the certified curvature ratio.

## 2. Uniform denominator integrals without resonance quadrature

Let U(k)=1/|Df(k)|. The installed inequalities supply

    Im Df >= 19 kappa^2,
    |Df'|<61/1000,
    |Sigma_f,jj'|<=560,
    E'(k)>v.

Writing x(k)=Re Df(k), we have

    x'(k)>=v-560 kappa^2>v/2.                              (3)

Thus x is strictly increasing, and dk<=2 dx/v for the change of variables.
This remains valid if its image does not contain zero. Extending the resulting
positive integrals to the full real line and using pi<4 gives

    I2 := integral_I U^2 dk
       <= (2/v) integral_R dx/[x^2+(19 kappa^2)^2]
        = 2pi/(19 v kappa^2) <17/kappa^2,
    I3 := integral_I U^3 dk
       <= (2/v) integral_R dx/[x^2+(19 kappa^2)^2]^(3/2)
        = 4/(361 v kappa^4) <1/(2 kappa^4).                (4)

Cauchy-Schwarz on the interval of length 2sigma gives

    I1 := integral_I U dk <=sqrt(2sigma I2)<1/kappa.        (5)

These are uniform analytic bounds, not numerical integration over a linewidth
too narrow for a grid. The only scalar conditions used are
560 kappa^2<v/2, 8/(19v)<17, 4/(361v)<1/2 and 34sigma<1.

## 3. Weighted packet and outgoing-phase derivatives

The inherited form factor satisfies |g_minus|<=2 and |g_minus'|<=26.
Set a1=2/sigma+13 and d=61/1000. Differentiating f almost everywhere gives

    |f| <= kappa U,
    |f'| <= kappa [a1 U+d U^2].                          (6)

For example the cutoff contribution is at most
kappa*(2/sigma)*U, because its form factor is at most two and the
normalizing denominator exceeds two. No cutoff derivative is omitted.
Consequently

    F1 := integral |f'| <=a1+17d/kappa<2/kappa.            (7)

To keep the phase derivative inside its integral, write
t_minus=1+kappa^2 n(k)/Df with n=-i |g_minus|^2/vg.
The inherited open-resolvent bounds give |n|<=160, |n'|<=720, so

    |t_minus'| <=kappa^2[720 U+160d U^2].

The source proves |t_minus|>1/2. Differentiating its unit phase therefore
gives the safe estimate |(t_minus/|t_minus|)'|<=4|t_minus'|.
Since |r0'|=2,

    integral |f| |rho'|
      <=2F0+4 kappa^3[720 I2+160d I3]
       <2/500+48960 kappa+(320d)/kappa.                  (8)

Using (7),(8) in (2), we can take

    A0=3/kappa,             B0=23/kappa.                 (9)

All four columns still use exactly the same f and rho. There is no separate
column phase adjustment or parameter-dependent substitution into W.

## 4. Weighted complete localized correction

The installed Schur analysis has one resonant scalar ds with
|ds-Df|<=xi |Df|, xi<1, and a closed emitter block inverse of norm below six.
Its off-diagonal coefficient bounds are sPQ and sQP as explicitly defined
in the source. The rank-one block inverse formula, keeping the closed inverse
as a separate summand, yields

    ||De^-1||
      <=6+[(1+6 kappa^2 sPQ)(1+6 kappa^2 sQP)/(1-xi)] U
       <6+2U.                                           (10)

This step is not an unproved replacement of the uniform inverse by a scalar:
it includes the seven complementary emitter coordinates in each parity.
The bracket is independently checked using the exact source expressions.
For y_j=kappa De^-1 w_j, the inherited ||w_j||<3, ||w_j'||<30 and
||De'||<d imply

    ||y_j|| <=kappa(18+6U),
    ||y_j'|| <=kappa[3d(6+2U)^2+30(6+2U)]
              <kappa(187+65U+U^2).                     (11)

The source's full localized representation is C_g,j+kappa Kloc y_j on
the clock and y_j on the emitter. Its checked bounds are

    ||C_g,j||<=31, ||C_g,j'||<=2700,
    ||Kloc||<20000, ||Kloc'||<10^6.

No derivative of the fixed internal basis is needed. From (11) and
1+20000 kappa<2,

    ||C_j|| <32+12 kappa U,
    ||C_j'|| <2701+131 kappa U+2 kappa U^2.              (12)

For the derivative, the constant leftovers obey
374 kappa+18*10^6*kappa^2<1, and the additional coefficient of U is
6*10^6*kappa^2<kappa. These explicit inequalities justify the rounding
in (12); the emitter derivative and all closed tails are counted.

Substituting (6),(12) in (1) and using E2/v<5/2 gives

    D_j <= kappa(32a1+2781) I1
       + [kappa^2(12a1+161)+32 kappa d] I2
       + kappa^2(12d+2) I3
       <236a1+5518+(544d)/kappa+(6d+1)/kappa^2
       <3/(2 kappa^2).                                 (13)

There are two potentially nonorthogonal localized columns in each parity.
Paying their square sum exactly as in the original proof, the safe grouped
constant is

    D=3/kappa^2 >sqrt(2) max_j D_j.                     (14)

Different parity subspaces remain orthogonal. This is a bound on the full
localized map, not an assumption that the two old-energy columns are
orthogonal in the interaction region.

## 5. Complete output and finite apparatus

Inherit the installed source's seed-isometry error below 0.003, common
reflection comparison below 0.000714, and complete comparator

    Uideal(t)x=zeta exp[-i(nu+2kappa)t]
                    beta_t tensor iota exp(-itK)W x,

where beta_t is the very same normalized outgoing half-line packet from
that source. The seed starts at t=0, so all old aging includes emission
and flight. The exact scattering-packet intertwining and seed overlap imply

    ||exp(-it Hphysical)Eseed-Uideal(t)||
      <0.003+0.000714+(A0+B0)/sqrt(pi v t)
                                  +D/(sqrt(2pi) v t).    (15)

With T=10^36, sqrt(pi v T)>27*10^16 and sqrt(2pi)>12/5,

    (A0+B0)/sqrt(pi v T)+D/(sqrt(2pi) v T)
      <[26/kappa]/[27*10^16]+[3/kappa^2]/[(12/5)v T].   (16)

The right side is below 0.000097, and the total is below 0.004. Moreover
vT>1 and B0/sqrt(pi vT)<1/2, so the outgoing normalization conditions
actually hold. Both remainder terms decrease for every later t. The full
unhalved trace-distance bound with a passive reference is twice (15), below
0.008. No seed bound-state amplitude is discarded or added twice: it is
already included in the unchanged seed-overlap norm.

The inherited spectral radius 19 and actual graph hop distance from emitter
to the first omitted site, dM=M-L-1, are unchanged. With Tobs=2*10^36 and
M=5*10^37, dM>19*Tobs*(6/5)+9. The same Chebyshev argument therefore gives
finite-device error below 0.001 on [T,Tobs], and complete embedded output
error below 0.005, with unhalved trace distance below 0.01. The far-end
diagonal correction and infinite-output comparison remain exactly as in
the source; this is not an all-future statement for a fixed finite device.

## 6. Evidence scope and next check

The new proof obligations are (3)-(5), replacement of separate supremum
bounds by the weighted integrals (1),(2), the full block inverse in (10),
and all product/rounding constants in (6)-(16). They require a distinct
analytical check. Exact scalar arithmetic can verify displayed comparisons,
but cannot by itself qualify the new weighted proof or its installed source.

The single recorded execution of `check_bounds.py` completed successfully
through `run_check.py`; the child source was hashed before execution. The
program and wrapper declared five CPU seconds and ten wall seconds before
that run. `EXECUTION.json`, full stdout/stderr and exact `BOUNDS.json` preserve
the actual evidence. The resulting complete-error upper expression is
approximately 0.0038102963462962962, a display only; its exact rational is
controlling. No failed scientific execution occurred in this bounded step.

No new interactions, new initial state, fit, numerical quadrature, parameter
search, dynamics simulation or physical permission are used. This note does
not compose with the separate ladder-coefficient or emitter-calibration
proposals. Native realization, vacuum/seed supply, exact structural symmetry,
static complex couplings, capture/reset/reuse and practical resource costs
remain separate physical obligations. No canonical publication or retained
status is approved by this author note.
~~~~
<!-- END UNCHANGED SOURCE: weighted_emitter_escape_candidate/CANDIDATE.md -->
