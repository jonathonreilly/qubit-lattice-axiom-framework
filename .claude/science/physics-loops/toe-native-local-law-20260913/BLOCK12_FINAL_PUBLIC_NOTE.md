---
claim_id: charged_finite_link_local_dynamics_and_phase_bridge_bounded_theorem_note_2026-09-13
claim_type: bounded_theorem
claim_scope: "For a supplied bounded even-CAR gauge Hamiltonian, exact Gauss-preserving finite integer links approximate finite-time local rotor dynamics with explicit flux-tail and Hamiltonian-cutoff bounds. The displayed mixed four-orbital carrier preserves ordinary time reversal but has an exact complex three-slice fermion-weight witness; a finite phase-basis electric heat kernel also need not be entrywise positive. These are specified representation statements, not a no-go for a charged Coulomb phase, a fixed-cutoff infrared theorem, a native fermion encoding or an axiom update."
upstream_dependencies:
  - native_edge_record_matter_instrument_and_energy_ledger_bounded_theorem_note_2026-09-05
runner: scripts/charged_finite_link_local_dynamics_and_phase_bridge_2026_09_13.py
---

# Finite charged links: controlled local dynamics and the remaining phase argument

**Date:** 2026-09-13
**Type:** bounded_theorem
**Status:** proposed_retained

## Result and supplied premises

A specified finite integer-flux cutoff preserves the charged Gauss law and
ordinary time reversal exactly. Its local real-time dynamics approximates
that of the untruncated rotor with a derived error bound, for initial states
with bounded electric flux. For fixed time, local observable and accuracy,
the cutoff can be chosen independently of total spatial volume.

This addresses a finite-link realization obligation for a supplied Hamiltonian.
A thermodynamic charged photon phase remains a separate question. Two exact
matrix calculations sharpen that question: neither the finite phase-basis
heat kernel nor ordinary time reversal automatically supplies pointwise
positive Euclidean weights in the displayed representations. Other phase
proofs and other representations remain live.

~~~yaml
actual_current_surface_status: conditional-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact Gauss algebra and finite-time truncation bounds with explicit representation-specific Euclidean weight discriminators."
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "Realize a controlled finite-link charged Hamiltonian and identify the additional argument required for its quantum photon phase."
source_of_blocker_text: user_goal
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Control a specified fixed-cutoff charged ground-state phase or construct a different admissible phase bridge."
conditional_surface_status: conditional-support
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
~~~

The [minimal framework memo](MINIMAL_AXIOMS_2026-06-29.md) is the ontology
reference. The [edge matter construction](NATIVE_EDGE_RECORD_MATTER_INSTRUMENT_AND_ENERGY_LEDGER_BOUNDED_THEOREM_NOTE_2026-09-05.md)
identifies a conditional even-CAR comparison. The
[current integer-link note](THE_FERMION_ON_COMPACT_U1_LINKS_THE_INTEGER_FLUX_SELECTS_THE_STAGGERED_GAUSS_LAW_AND_JOINS_THE_MAXWELL_GERM_BOUNDED_THEOREM_NOTE_2026-09-03.md)
already distinguishes exact finite gauge algebra from a quantum Maxwell phase.
Here the CAR representation, graph, local Hamiltonian, continuous time and
couplings are supplied. No unmerged band theorem is required: all hopping
matrices used in the finite-link and determinant results are redeclared below.
No primitive, axiom, state preparation law or audit verdict is added.

Finite-time gauge truncation and cutoff-independent propagation have close
established precedent in [Tong et al.](https://arxiv.org/pdf/2110.06942),
Appendices D and I. The contribution is their explicit bounded-shift
specialization to this charged carrier, together with the phase discriminators.
The general truncation mechanism is not claimed as a new discovery.

## Hamiltonian and finite physical space

Take a>0, g>0 and r>=0. On a finite cubic graph with distinct endpoints for each link, use four CAR
orbitals per cell and an integer rotor on each oriented link. Write

```text
H=H_on + sum_alpha(V_alpha+V_alpha^dagger) + sum_l k_l E_l^2,
G_x=div(E)_x-(N_x-2).
```

Each V_alpha is a bounded hopping or plaquette term, shifts each participating
link by s_alpha,l in {-1,+1}, and commutes with the other electric operators.
A link is not repeated inside one plaquette term. k_l>0. Onsite matter terms
are bounded and number preserving. The standard choices are
V_l=(r/a)c_x^dagger T_i U_l c_y and V_p=-b_p W_p, with b_p>0.
For the carrier below the onsite operator is (r/a) sum_x c_x^dagger h_on c_x;
h_on denotes its dimensionless four-by-four matrix.
The Hamiltonian is self-adjoint on the domain of its positive electric part:
the remaining finite-volume interaction is bounded.

For an integer S>=0 and P_S=product_l 1_{|E_l|<=S}, H_S=P_S H P_S restricted to its range is a
finite matrix. The compressed U_S=P_S U P_S obeys [E_S,U_S]=U_S exactly.
U_S^dagger U_S=I-|S><S| and U_S U_S^dagger=I-|-S><-S|. Thus every G_x
commutes with H_S. Occupying two orbitals at every cell with all E_l=0 proves
that the physical subspace is nonempty. A finite Gauss-projected Gibbs state
exists. A link uses ceil(log2(2S+1)) encoding qubits, with unused codewords
excluded or locally penalized; an even-CAR matter representation is still a
separate condition, not removed by this link encoding.

For the mixed carrier below, the antiunitary T=(tau_x on each cell) K in the
real occupation/flux basis preserves H and all G_x. A gauge-invariant state
has <U_l>=0 for distinct endpoints, by averaging exp(i alpha_x G_x). That
identity is compatible with a charged phase; the gauge-invariant bilocal
c_x^dagger W_gamma c_y carries the required dressing. A free Slater determinant
tensored with a link vacuum is not asserted to be its physical ground state.

No finite-dimensional *unitary* U satisfies [E,U]=U, because conjugation would
give U^dagger E U=E+I and a contradictory trace. Hard truncation escapes via
nonunitarity at its endpoints. This algebraic observation does not exclude
finite-spin Coulomb phases, including the existing ice route.

## One-link exponential estimate

Let J_l=sum_{alpha:s_alpha,l!=0} ||V_alpha||. Regroup the terms as
H=R_l+B_l+B_l^dagger, [R_l,E_l]=0, [E_l,B_l]=B_l, ||B_l||<=J_l.
On a finite larger cutoff K, for lambda>0,

```text
exp(lambda E_l) H_K exp(-lambda E_l)
 =R_l+exp(lambda) B_l+exp(-lambda) B_l^dagger.
```

The norm of its anti-Hermitian part (H_lambda-H_lambda^dagger)/(2i) is at
most 2 J_l sinh(lambda). Differentiating the squared norm of weighted
Schrodinger evolution and applying Gronwall therefore gives

```text
||exp(lambda E_l) exp(-it H_K) exp(-lambda E_l)||
 <=exp(2 J_l |t| sinh(lambda)).                              (A)
```

For any real thresholds L>=M and either sign epsilon=+1 or -1,

```text
||1_{epsilon E_l>=L} exp(-it H_K) 1_{epsilon E_l<=M}||
 <=exp[-lambda(L-M)+2 J_l |t| sinh(lambda)].                 (B)
```

This is an operator norm bound, so arbitrary matter/link entanglement in the
initial low-flux subspace is allowed. Both one-sided bounds hold with the same
J_l. The combined |E_l| tail costs at most sqrt(2) times the right side when
the initial support is |E_l|<=M, by the commuting-projector union bound (the output tails are orthogonal when L>0).

For the full rotor, pass K to infinity. The electric part commutes with all
cutoffs. In its interaction-picture Dyson series every bounded compressed
interaction converges strongly, termwise, and the series has a common
exponential norm bound at fixed volume/time. Consequently the evolutions on
finite-support initial vectors converge strongly, and so do the bounded
spectral projections appearing in (B). The uniform finite-K inequality passes
to all initial vectors by density. This avoids treating exp(lambda E_l) as a
bounded operator on the full rotor space. The same proof directly gives (B)
for any finite H_S, with constants independent of S and total volume.

## Hamiltonian truncation error with explicit factors

Let I_S embed the truncated space and P_M be the all-link cutoff M<=S. With
U(t)=exp(-itH), U_S(t)=exp(-itH_S), Duhamel gives

```text
[U(t)-I_S U_S(t) I_S^dagger] P_M
 =-i integral_0^t U(t-s) (I-P_S) H P_S U_S(s) P_M ds.         (C)
```

For one V_alpha, crossing the boundary requires at least one of its shifted
links to start at the outward endpoint E_l=s_alpha,l S. A union of these
commuting endpoint projectors is bounded in vector norm by the sum of their
norms. Thus each V_alpha and its adjoint contribute at most

```text
||V_alpha|| sum_{l in alpha} [||1_{E_l=S} U_S(s)P_M||
                              +||1_{E_l=-S} U_S(s)P_M||].
```

Overcounting a plaquette that reaches several endpoints only enlarges this
upper bound. Inserting (B) into (C) yields the explicit safe estimate

```text
D_S(t):=||[U(t)-I_S U_S(t) I_S^dagger] P_M||
 <=2 |t| sum_l J_l exp[-lambda(S-M)+2 J_l |t|sinh(lambda)].   (D)
```

It may always be capped by 2. If J_l<=J and there are N links,
D_S(t)<=2 N J |t| exp[-lambda(S-M)+2 J |t|sinh(lambda)].
For lambda=1 and nonzero Jt, the sufficient choice

```text
S>=M+2 J |t|sinh(1)+log(2 N J |t|/epsilon)
```

rounded upward and constrained S>=M gives D_S<=epsilon. For zero coupling or
time the error is exactly zero. The sharper one-sided tail exponent, if
d=S-M>2J|t|, is optimized at lambda=arcosh[d/(2J|t|)], giving
-d arcosh[d/(2J|t|)]+sqrt(d^2-(2J|t|)^2). This optimization is optional;
it does not turn the sufficient growth into a necessary lower bound.

For a density matrix supported in P_M and any bounded observable A, comparing
A to its compression in the truncated evolution costs at most
2 ||A|| D_S(t) in expectation. The factor two follows from the two cross
terms in the difference of normalized evolved vector expectations and extends
to mixtures; no additional assumption on entanglement is needed.

## Local observables and spatial volume

Treat matter cells and link rotors as sites of a bounded-degree incidence
graph. H_on and E_l^2 are onsite. All other terms have bounded support size,
range and norm, uniformly in the flux cutoff. Their interaction picture under
the onsite part preserves these properties. The usual nested-commutator
Lieb-Robinson argument applies to bounded *even* observables: disjoint even
CAR algebras commute, and onsite evolution preserves parity and support.
This is also the hypothesis mechanism in Tong et al., Appendix I, Lemma 13.

For a local bounded even A with support X, let B_R contain its R-neighborhood
and let H_B retain only terms completely inside B_R. There are constants
C_X,v,nu>0 independent of S and ambient volume with

```text
||A_H(t)-A_HB(t)|| <= C_X ||A|| exp(v|t|-nu R).               (E)
```

The same bound holds for the compressed theory. Constants absorb the fixed
support cardinality/range and boundary polynomial factors. For an initial
state with all fluxes supported in |E_l|<=M, its reduced state in B_R has the
same support condition. Apply (D) in B_R and (E) on both sides to obtain

```text
|<A_H(t)>-<A_HS(t)>|
 <=2 C_X ||A|| exp(v|t|-nu R)
   +4 ||A|| |t| sum_{l in B_R} J_l
           exp[-lambda(S-M)+2 J_l |t|sinh(lambda)].           (F)
```

Compression of A is understood. The spatial restriction need not preserve
all boundary Gauss constraints: the comparison is made in the ambient
Hilbert space where the norm bound holds, then restricted to physical initial
states. No artificial product state or independently factorized physical
Hilbert space is assumed. At fixed time, local support and precision, choose
R and then S using (F); both choices are independent of ambient volume.

This result controls a sequence of finite-time local approximations to rotor
dynamics. It does not control an infinite-time limit at fixed S, prove a
thermodynamic ground-state photon pole, provide a gapped-path stability theorem,
or prepare the requisite charged state. An energy-based low-flux hypothesis
can replace exact support only with its own quantitative tail estimate.

## Explicit carrier and supplied common bare metric

Let s=sin b,c=cos b, 0<b<pi/2, 1/2<zeta<1, 0<mu^2<1-zeta^2. Define

```text
h_on=(2+zeta) sigma3+mu tau_x(s sigma1+c sigma3),
C_x=-s sigma1-c sigma3, S_x=tau_z(c sigma1-s sigma3),
C_y=C_z=-sigma3, S_y=sigma2, S_z=0, T_i=(C_i-i S_i)/2.
```

These are the explicitly aligned four-orbital carrier coefficients; the
present finite-link theorem requires only their boundedness and symmetry,
not an unmerged band theorem. tau_x T_i^* tau_x=T_i and the corresponding
onsite identity hold. Each T_i has nuclear norm 2: x,y singular values
(1,1,0,0), z singular values (1/2,1/2,1/2,1/2). Hence
||c_x^dagger T_i c_y||<=2 by singular-value decomposition and the CAR norm
bound on each normalized creation/annihilation operator.

For supplied positive diagonal D, physical coordinates y_i=a n_i/D_i, and
w_i=det(D)/D_i^2, choose

```text
H_E=(g^2/(2a)) sum_{links axis i} w_i E_l^2,
H_B=-(1/(2g^2 a)) sum_{plaquettes normal i} w_i(W_p+W_p^dagger).
```

The small-angle quadratic expansion of the untruncated rotor classical symbol
has unit photon speed in y. A finite compressed U_S is not being identified
with a unit-modulus classical angle. Indeed
link angle theta_i=(a/D_i) A_i, cell volume a^3/detD, and canonical electric
momentum Pi_i=detD E_i/(a^2 D_i) transform H_E to integral(g^2/2)Pi^2 and the
quadratic H_B to integral B^2/(2g^2), up to its constant. This is a bare
classical expansion, not a quantum phase derivation. With matter prefactor
r/a, a selected D matching its four free-node metric gives matter speed r;
equality of bare photon and matter speeds requires the supplied r=1.

For an axis-i link in the cubic bulk, four plaquettes meet it, two of normal
j and two of normal k. Thus a valid local flux-growth constant is

```text
J_i <= [2r+(w_j+w_k)/g^2]/a.                                (G)
```

This makes the coupling/spacing dependence of (D)-(F) explicit. In particular,
the construction does not assert a cutoff uniform in a continuum limit a->0
or in arbitrarily weak g. The local link count still grows with R, but not
with an ambient torus already larger than that neighborhood.

## Two exact discriminators for a naive positive Euclidean bridge

These statements concern specified representations before any proof of a
quantum phase. A negative transfer-matrix entry is an amplitude, not a negative
physical probability. An unprojected fixed-background fermion weight is not
the full Gauss-projected partition function.

First put S=2 and use the five orthonormal discrete phase states of one link.
For H_E=E^2/2 the off-diagonal heat kernel at phase separation 4pi/5 is

```text
K_2(2;tau)=[1+2 exp(-tau/2)cos(4pi/5)
             +2 exp(-2tau)cos(8pi/5)]/5.
```

K_2(2;0)=0 and K_2'(2;0)=(5-3sqrt(5))/20<0. Therefore this exact finite-link
electric transfer matrix has a negative off-diagonal phase-basis entry for
sufficiently small positive tau. At tau=.02 the entry is about -0.00162675043.
The infinite-rotor heat kernel is positive by its Poisson/Gaussian expression;
one cannot simply transfer that pointwise property to this finite phase grid.
The pure-gauge model has a different live representation: in the flux basis,
negative real plaquette hopping yields nonnegative Euclidean worldline weights.
No basis-independent obstruction is claimed.

Second use just one open y-directed edge of the actual four-orbital model and
three successive background link phases 0,pi/2,pi. The one-particle Hamiltonian
h(phi) is eight-dimensional, with h_on at each endpoint and off-diagonal
T_y exp(i phi). Write

```text
W(delta)=det[I+exp(-delta h(pi)) exp(-delta h(pi/2)) exp(-delta h(0))].
```

This is the usual grand-canonical number-conserving fermionic trace for that
specified history, before Gauss projection or temporal-link integration.
In a basis diagonalizing tau_x it factorizes into two four-dimensional
problems. Their onsite matrices are A_eta sigma1+B_eta sigma3, where
A_eta=eta m1, B_eta=B0+eta m3, B0=2+zeta. The common hopping is
T_y=[[-1,-1],[1,1]]/2. Let w(A,B;delta) denote the determinant of one block.
Direct matrix multiplication of the convergent power series at delta=0 gives

```text
log w = 4 log 2 + (18 A^2+18 B^2+1)delta^2/4
        +i A delta^3
        -(162 A^4+324 A^2 B^2-110 A^2+162 B^4-28 B^2+1)delta^4/96
        -i A(7 A^2+7 B^2-1)delta^5/4 + O(delta^6).            (H)
```

For completeness, these coefficients are finite algebra, with no spectral
assumption: form P(delta)=exp(-delta h_3)exp(-delta h_2)exp(-delta h_1),
P_n=(-1)^n sum_{a+b+c=n}h_3^a h_2^b h_1^c/(a!b!c!), and use

```text
[delta^n](log w-4log2)
 =sum_{r=1}^n (-1)^(r+1)/(r 2^r)
   sum_{n1+...+nr=n; nj>=1} Tr(P_n1 ... P_nr).              (I)
```

The displayed four-by-four block matrices and (I) are a reproducible exact
certificate for (H), not a floating-point phase fit. Adding eta=+/- cancels
the cubic terms but leaves

```text
Im log W(delta)=-7 B0 m1 m3 delta^5+O(delta^6).              (J)
```

For the aligned carrier m1=mu sin b, m3=mu cos b. In its stated open parameter
range this coefficient is nonzero. An explicit rational fixture has
sin b=4/5, cos b=3/5, zeta=3/5, mu=1/5; then the coefficient is -1092/3125.
At delta=.4 its phase is approximately -0.00048223703. The nonzero Taylor
coefficient itself proves that sufficiently small nonzero steps have complex
weights. No phase threshold or numerical scan defines this conclusion.

Every single-slice exponential is positive definite. A single factor gives
a positive det(I+P), as do two factors since their product is similar to a
positive definite Hermitian matrix. Three factors need not do so. Ordinary
T^2=+1 maps this background history to its sign-reversed history and gives
W[-phi]=conjugate(W[phi]); it supplies pairing, not pointwise positivity of
this particular background integrand. A Gauss projection, a different field
representation, extra matter pairing, or a determinant estimate may alter the
proof route. This calculation rules out only an automatic positivity inference
from ordinary time reversal for the displayed time-sliced representation.

## Precise remaining phase task and literature scope

[Tong, Albert, McClean, Preskill and Su](https://arxiv.org/pdf/2110.06942), establish a much
broader truncation framework. Here Appendix D, Theorem 6 and its proof, and
Appendix I, Lemma 13 and its proof were read. The bounded-shift argument above
is a direct specialization with explicit constants. Their isolated-eigenstate
results require a spectral isolation condition; they cannot be read as a
volume-uniform gapless ground-state theorem. No priority is claimed for
polylogarithmic-precision flux truncation or cutoff-independent propagation.

[Hermele, Fisher and Balents](https://arxiv.org/pdf/cond-mat/0305401), sections III A-C and IV A
were read for the phase mechanism. The effective Coulomb description and its
monopole corrections concern a phase with gapped spinons and monopoles.
Replacing the gapped electric sector by this gapless charged quartet requires
an additional argument; a small-angle Maxwell expansion alone does not supply
it. Their finite-spin route remains constructive evidence against a universal
finite-local-dimension obstruction. The current-main cubic-ice notes retain
exact component facts and distinguish them from the imported adjacent-phase
argument. They are not treated as a theorem already including this quartet.

The next terminal obligation is concrete: for a specified fixed finite S,
couplings and thermodynamic sequence, construct physical ground states and
control gauge-invariant long-distance correlations or spectral response well
enough to establish the massless transverse gauge sector together with the
charged matter phase, excluding confinement or symmetry-breaking masses in
the claimed region. The common renormalized metric needs its own protection
or attraction argument in that actual phase. These are unresolved proof tasks,
not mutually independent axiomatic walls, and no new axiom is forced here.

## No-Go Discipline Gate

The delivered disposition is a positive bounded construction and a partial
phase attempt with named untested routes. The two negative representation
statements have exact witnesses. They are not a universal phase no-go, and
no route-count or unknown implication is used as evidence for one.

**N1 — Actual route families.** These materially different objects and
terminal obligations were examined; successes and live alternatives are kept.

| Route and object | Work and disposition | Marker |
|---|---|---|
| Finite unitary electric shift algebra | The trace proof closes the simultaneous exact commutator/unitarity requirement in finite dimension. Hard compression escapes it. | ATTEMPTED |
| Hard-cutoff Hamiltonian dynamics | The weighted norm and Duhamel derivation control the local finite-time error. It succeeds at that task; fixed-cutoff ground-state control is unproved. | ATTEMPTED |
| Classical quadratic coordinate/metric matching | The canonical coordinate substitution gives the displayed positive bare Maxwell quadratic form. It does not by itself construct a quantum state or phase. | ATTEMPTED |
| Electric phase-basis transfer measure | The exact five-state heat-kernel derivative disproves pointwise positivity for that representation and time-step regime. Flux-basis worldlines remain a constructive escape. | ATTEMPTED |
| Charged determinant measure and antiunitary pairing | The exact three-slice coefficient disproves automatic pointwise positivity from the displayed T. Pairing, Gauss projection and alternative representations remain available. | ATTEMPTED |
| Fixed-spin ice and monopole effective theory | The cited finite-spin phase literature and current-main comparison were read for the charged-gap assumption. Their gapped-charge phase is a live comparison, not an exclusion of gapless charged matter. | ATTEMPTED, hypothesis review only |

No row invokes a prior retained result that rules out the full target. These
are six actual formulations of intermediate obligations, not six failed
exhaustive searches of the admissible theory space. Untested terminal routes
include a charged constructive RG argument, determinant bounds compatible
with monopole control, and a direct Hamiltonian phase argument at fixed S.

**N2 — Relations among remaining tasks.** Let F mean the proved finite-time
low-flux approximation, P the unresolved charged thermodynamic phase, and C
the unresolved common renormalized cone in that phase. No independent wall
count is asserted.

| Pair | Forward implication | Reverse implication | Disposition |
|---|---|---|---|
| F, P | Not established; the limits and state hypotheses differ | A phase statement alone need not include a quantitative cutoff estimate | No independence theorem; separate proof tasks |
| P, C | Not established; the phase may allow metric contrasts | C formulated for that actual charged phase includes its existence | Treat C as a stronger phase target, not an additional independent wall |
| F, C | Not established | Quantitative cutoff bounds are not part of the cone assertion | Relation unresolved beyond the stated scope |

The finite-unitarity trace result, phase-kernel sign and determinant phase
are distinct exact representation facts. They are not added together to
inflate an axiom deficit.

**N3 — Hidden-premise scan.** The graph, four CAR orbitals, Hamiltonian time,
a,g,r, positive weights, bounded shifts, distinct plaquette links, initial
low-flux support and chosen D are explicit supplied conditions. The locality
step states the even-algebra, finite-range and bounded-degree hypotheses.
"Background" denotes specified link histories or charge N-2; it is not a
formed physical state. The "standard" norm argument is written out through
its support and parity mechanism. Neither the classical coordinate change
nor a finite Gibbs state imports a thermodynamic ground state. Numerical
fixtures are declared tests of the finite matrices, not extra premises in
the analytic inequalities.

**N4 — Residual matching.** The current integer-link note is cited only for
the distinction between finite gauge algebra and a quantum phase. Its code
parity and staggered filling results are not transferred to this four-orbital
N-2 background. Tong et al. address low-quantum-number finite-time truncation
and the onsite-independent propagation bound, matching those comparison
residuals. Hermele et al. address an effective Coulomb phase with gapped
electric charges; that differs from the gapless charged quartet target and
is explicitly not counted as its proof. No prior no-go is a witness against
the full target.

**N5 — Resolution audit.** Per element: the exact finite link commutator,
unitarity defects and phase kernel are tested. Per site: two-cell charged
Gauss sectors and T are tested. Per mode: finite link/environment leakage
norms are tested; no thermodynamic photon mode is certified. Per block:
simultaneous boundary crossings and the exact determinant coefficients are
tested. Lattice wide: the local-volume independence follows from the stated
analytic norm/locality argument; no thermodynamic phase computation is run.
The primary stdout records all five classes with these limits. The kernel
and determinant counterexamples refer to the stated representations; they
are never broadened to all bases, all physical states or all formulations.

**N6 — Partial closure and conventions.** The link encoding and low-flux
approximation retire a concrete finite-time realization obligation under
explicit imports. Bare coordinate/metric matching is a convention plus a
selected coupling choice, and is not presented as new dynamics. The exact
Gauss law and finite Gibbs state are useful partial construction. A phase
requires a physical long-distance statement; no notation change is offered
as its proof. No claim that a new axiom is required is made, and no approved
primitive is relabeled as an unresolved axiom.

**N7 — Steelman against a universal negative.** A critic can keep one large
but fixed finite link, work directly in the Hamiltonian formulation, and
control weak compact-gauge fluctuations with the gapless charged determinant
rather than demand positivity in this particular phase basis. Finite-spin
Coulomb phases already make a universal finite-dimension objection untenable
as a search strategy; the referenced Hermele construction is the concrete
counter-route. The terminal task is a thermodynamic ground-state/correlation
estimate that survives the charged sector and excludes the relevant ordering
or confinement instability. The present norm theorem supports finite-time
approximations but does not complete that task. This live route is why the
phase attempt remains partial.

**N8 — Cross-cycle echo.** Current-main integer-link and cubic-ice notes were
read for the same finite-matrix-to-photon jump. Their corrected scopes keep
exact algebra and finite component facts while separating the imported
phase. The hard-cutoff proof here addresses finite-time approximation; it
does not silently promote those old phase comparisons. A scoped search of
NO_GO_LEDGER.md and REVIEW_AND_LEARNING.md for finite-link/photon/truncation
phase wording found no additional matching ledger in this checkout. That
search result is a retrieval limit, not an exhaustion certificate. The known
finite-spin escape is explicitly retained.

No universal no-go packet PASS is claimed. The narrow algebraic and
representation statements stand on their displayed proofs and witnesses;
the charged phase is recorded as an unfinished research route.

## Reproduction and verification limits

Run `python3 scripts/charged_finite_link_local_dynamics_and_phase_bridge_2026_09_13.py`.
The primary independently builds occupation-basis CAR matrices, finite gauge
links, entangled-environment leakage fixtures and simultaneous-boundary
examples. Exact rational trace-series coefficients are challenged by separate
high-precision matrix exponentials. These author checks can catch formula
errors; their count does not establish a thermodynamic phase or independent
scientific acceptance.

The proof uses arbitrary finite volume and then spatial locality for a local
observable. It does not exchange a->0, S->infinity, t->infinity and the
thermodynamic limit without control. It does not infer a fixed-S phase from
an S chosen for each finite time. Independent source review and the formal
retained-grade audit remain pending.
