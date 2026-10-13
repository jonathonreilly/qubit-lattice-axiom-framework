---
title: "Actual potential graph regularity and localized endpoint applicability"
claim_id: effective_potential_graph_local_endpoint_bounded_theorem_note_2026-10-13
status: conditional-support
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
artifact_role: theorem
assembly_status: publication_prepared_root_review_and_runtime_pending
runner: scripts/effective_potential_graph_local_endpoint_identity_2026_10_13.py
scientific_execution: none_in_publication_preparation
trace_class: upstream_support
reachability_to_target: supports
target_claim_id: null
target_blocker_text: null
source_of_blocker_text: frontier_question
conditional_surface_status: "Supplied one-dimensional carrier, smooth finite inputs and the exact moment, commutator, variation and state hypotheses of the preserved cores; all provisional parents remain conditional."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Ordinarily accepted conditional source argument, preserved without core edits; source integrity is not analytic verification."
audit_required_before_effective_retained: true
bare_retained_allowed: false
next_trace_action: "Root review of the exact publication wrappers and tooling, followed by separately recorded prepare and verify; cumulative review and independent retained audit remain later obligations."
source_assembly: prepared_energy_source_assembly
upstream_dependencies:
  - explicit_effective_potential_bounded_theorem_note_2026-10-13
  - corrected_dispersion_bounded_theorem_note_2026-10-13
  - moment_sensitive_corrected_dynamics_bounded_theorem_note_2026-10-13
  - current_preserving_refinement_bounded_theorem_note_2026-10-12
  - local_even_continuum_bounded_theorem_note_2026-10-12
---

# Actual potential graph regularity and localized endpoint applicability

Claim type: bounded_theorem

Claim status: conditional-support; source assembly accepted, publication review and runtime pending.

## Source integration and scope

This candidate collects two original root compositions and the complete
source-exposed check that tested them. The three bodies are reproduced in their
original order of role: graph regularity, localized stationary endpoints, then
adversarial checking. Their titles, historical pending fields and exposure claims
remain literal source text. The collected note is not a new independent proof.

The conditional scope is the actual fixed finite effective-potential coefficients,
real even-CAR domains and commutators, uniform smooth-cutoff estimates, and the
localized endpoint application on the supplied physical/full-low carriers.
Constants retain fixed-order and fixed-input dependence. Exact local support is
asserted for the cut-off potential; the original coefficients have the stated
tails. The same-kinetic potential comparison does not establish finite-speed
propagation of the kinetic dynamics or exact locality of its full evolution.

The separate accepted precision reads G5's integer k as a nonnegative integer.
The N=0 tail is valid but cannot meet the displayed endpoint choice when a>=2;
the N=1 choice is available for J=0. These are the archived check's precisions,
not edits to either original composition.

## Direct proposed dependencies

- [explicit_effective_potential_bounded_theorem_note_2026-10-13](EXPLICIT_EFFECTIVE_POTENTIAL_BOUNDED_THEOREM_NOTE_2026-10-13.md): actual finite-order coefficient construction and compression conventions.
- [corrected_dispersion_bounded_theorem_note_2026-10-13](CORRECTED_DISPERSION_BOUNDED_THEOREM_NOTE_2026-10-13.md): global corrected kinetic multiplication domains and growth.
- [moment_sensitive_corrected_dynamics_bounded_theorem_note_2026-10-13](MOMENT_SENSITIVE_CORRECTED_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-10-13.md): stationary initial-moment/density comparison in the endpoint composition.
- [current_preserving_refinement_bounded_theorem_note_2026-10-12](CURRENT_PRESERVING_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md): actual carrier and real-field normalization.
- [local_even_continuum_bounded_theorem_note_2026-10-12](LOCAL_EVEN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-10-12.md): even-CAR normalization and local algebra conventions.

These direct support edges propose no retained-status change. The three
corrected-dynamics parent notes are installed on the exact parent head
bd831ffb14c7d7f12bf1b8165596a0db85f838ef, regular PR 9511.
The publication driver must recheck those bytes before installation.
Same-packet premises are carried below; existing carrier parents retain
their status. Branch lineage is separate from mathematical dependence.

## Exact historical core begins

Each mapped core segment below is copied byte-for-byte from its selected
source. The two labeled interludes are new wrappers, not part of those cores.
Original historical statuses are not the status of this assembly.

# Graph regularity of explicit and smoothly localized effective potentials

Root composition candidate, 2026-10-13. This is an ordinary derivation
joining separately checked premises. No focused independent check of this
composition, new scientific execution or retained audit has occurred.
The fourth-moment comparison correctly left its particular T_j application
outside the sources it had read. Its generic single-multiplier argument is
not, by itself, the full actual coefficient argument below.

Exact parents: potential600/8f1e13d1 and its comparison496/47d94f2b;
spatial626/62227375 and comparison328/f9f91957; corrected kinetic1049/402cbc03
and comparison449/a89c8915; fourth867/34bf78f5 and comparison505/4bc61a1a.
Full SHA-256 bindings are in the accompanying seal. All orders, positive
mass parameters, interval and input-polynomial complexity are fixed.

## 1. The actual coefficients preserve Schwartz regularity

The actual fixed-order coefficient has the Fourier representation

    (T_j f)^hat(p)=sum_(k=0)^floor(j/2)
                         R_(j,k)(p) partial_p^k fhat(p).       (G1)

The independently checked coefficient/pole result places R_(j,k) in the
matrix ring C[p,(m²+v²p²)^(-1)]. Its poles are away from the real line,
and each derivative of R_(j,k) is smooth with polynomial growth on that
line. For smooth compact f, fhat and all of its derivatives are Schwartz.
For each pair of nonnegative integers a,b, the product rule expresses
p^a partial_p^b[R_(j,k) partial_p^k fhat] as a finite sum of derivatives
of R_(j,k), polynomial factors and higher derivatives of fhat. Every term
is rapidly decreasing, because fhat has arbitrary polynomial decay.
Thus T_j f is Schwartz. The checked reflection-reality relation makes
it a real coefficient vector when f is real.

This proof retains all transported momentum derivatives in G1. In
particular T_2 includes a p³ partial_p fhat term, so T_j is not being
identified with a single Fourier multiplier. No L2-boundedness of T_j
on arbitrary rough inputs is asserted.

## 2. Uniform free-commutator bounds at fixed correction orders

For fixed kinetic order n and 0<c<=c0, the full-low positive corrected
one-particle energy obeys the previously checked bound

    e_c^[n](p)<=C_(n,c0,m,v) <p>^(2n+1).                       (G2)

It follows that every fixed h=T_j f has a uniformly bounded differentiated
field coefficient ||e_c^[n] h||_2. The absolute value of the real free
coefficient generator is this energy multiplier; the positive-polarization
CAR flow and its normalization are those of the exact canonical parents.

Write a finite formally selfadjoint even polynomial as a sum of ordered
words with real coefficient inputs h_(a,k) and scalar coefficients z_a(c).
If sup_(0<c<=c0)|z_a(c)| is finite, field norm equality and the Leibniz
rule give uniform finite bounds

    K_* = sum_a sup_c|z_a(c)| product_k ||h_(a,k)||_2,
    L_* = sum_a sup_c|z_a(c)| sum_k sup_c||e_c^[n]h_(a,k)||_2
                                  product_(l!=k)||h_(a,l)||_2. (G3)

For the selfadjoint half-sum convention, count both adjoint partners
with their literal half weights; there is no missing factor two. A
degree-zero word contributes no differentiated term. Norm differentiability
of each real-field free orbit gives a norm derivative of the polynomial.
The generator criterion then gives its domain-preserving bounded
commutator with F_c=dGamma(e_c^[n]), precisely the premise in the
fourth-moment theorem. No commutator is inferred from norm approximation
of the potential alone.

The actual finite polynomial V^[N](c) has a fixed finite collection of
inputs T_j f and coefficients equal to fixed weights times c^j, 0<=j<=N.
G1 and the bound c^j<=c0^j therefore prove G3 for that exact family,
uniformly in c, at fixed n,N. This fills the previously named application
premise once the actual coefficient source is included. It does not
re-prove its potential remainder or any dynamics theorem.

## 3. A smooth local cutoff keeps this resource uniform in its radius

Fix I=[a,b] containing all original supports and a width w0>0. Choose
real smooth chi_R, R>=0, equal to one on I_R, between zero and one,
and supported in I_(R+w0), so for every fixed k

    sup_R ||partial_x^k chi_R||_infinity <= D_k < infinity.    (G4)

Such a family is obtained by multiplying fixed smooth transition functions
at the two endpoints translated by +/-R. Their product derivatives have
uniform bounds even when the transitions overlap. The width w0 stays fixed.

For every integer k, the ordinary product rule gives

    ||chi_R h||_(H^k) <= C_k sum_(l=0)^k
                        ||partial_x^l h||_2,                 (G5)

uniformly in R, with constants determined by G4. Consequently G2 bounds
||e_c^[n](chi_R T_j f)|| uniformly in c and R. Multiplication by chi_R
also contracts the L2 norm and preserves reality. Applying G3 to the
already checked local polynomial V_R^[N](c) proves uniform K_* and L_*
for this entire smooth-cutoff family. Its finite evenness, formal
selfadjointness and time-zero support are inherited from the checked
spatial construction.

This allows a radius R=R(c) growing as log(1/c), or any other nonnegative
radius, without losing the uniform first commutator solely through the
radius. A sharp characteristic cutoff does not satisfy G4; it cannot be
substituted into this domain statement using only its L2 approximation
bound. No assertion is made about a shrinking transition width.

For a finite collection of real BV time coefficients multiplying these
fixed operators, both potential and free-commutator total variations are
bounded by the sums of each coefficient's variation times K_* and L_*.
Here R(c) is fixed during each time protocol. A genuinely time-varying
cutoff radius or moving interval needs a separate variation/domain check.

## 4. Conditional endpoint composition

Let actual initial states have uniform fourth free moments and let the
effective initial low state be their low partial trace. The checked
commuting free orders pass that initial moment to F_c. G3, or G3--G5 for
the smooth local family, supplies the missing effective commutator premise
for fourth-moment propagation. Under the fixed stationary, finite-switching
or BV resources of the fourth-moment theorem, both sides therefore have
uniform fourth-column bounds Q_c,Q_0 and second-column bounds S_c,S_0.
Constructive ramp/pulse resources can be used only with their own stated
operator and density-comparison hypotheses.

If a separate theorem supplies actual-to-exact-compression density error
alpha_exact on |t|<=T_c, same-kinetic bounded Duhamel and the checked
potential estimates give, for the corresponding smoothly localized target,

    alpha_loc <= min(2, alpha_exact
                 +2T_c[C c^(N+1)+C' c² exp(-nu R(c))]),       (G6)

with fixed 0<nu<m/v. For time-dependent controls use their uniform norm
remainder, or its actual time integral. This assertion still requires a
density theorem valid for those controls; the moment theorem alone does
not provide it.

The fourth-moment endpoint formulas then apply with alpha_loc:

    W2 <= kappa_c Q_c+sqrt(Q_c+Q_0)(alpha_loc/2)^(1/4),
    ||Gamma_c-Gamma_0||_1 <=2kappa_c(1+S_c)Q_c
       +sqrt(alpha_loc)*sqrt((1+2S_c+Q_c)²+(1+2S_0+Q_0)²).     (G7)

Gamma is the positive shifted graph density defined through Hilbert--Schmidt
columns, not a normalized state. kappa_c=c/(2v)+1/Lambda_c. All readouts
refer to the actual free energy and continuum H0; the target may evolve
under F_c plus its chosen bounded potential. G7 permits convergence when
c->0 and alpha_loc->0 at uniform displayed resources. It supplies neither
unscaled-current convergence nor a detector realization or causal theorem.

The new content is the exact G1 regularity link and its radius-uniform
smooth local extension. The claims are conditional compositions of explicit
premises, with source-exposed focused checking still required before treating
this particular combined application as independently checked. All original
notes, comparisons and freezes remain unchanged.


## Second exact historical core: localized endpoint root

The first composition ends above. The following separate endpoint composition
is reproduced without mathematical or historical-status edits.

# Moment-sensitive local effective dynamics and energy endpoints

Root composition candidate, 2026-10-13. The stationary moment theorem is
separately derived and root-read; the graph-regularity application remains
a root candidate awaiting a focused check. This note makes that dependency
explicit. It supplies no retained audit, microscopic realization, formal
analytic verification or new physical axiom.

Use the exact supplied physical carrier and placements of the corrected
kinetic theorem. Fix J>=0, a=2J+2, q=2J+3, positive m,v and a finite
smooth even interaction V_c with ||V_c||<=K and all free commutators
through q-1 uniformly bounded. Let C bound ||[H_c,V_c]|| in the typed
norm-flow sense. Fix the initial actual normal densities with

    ||H_c rho_c^(1/2)||_HS <= S,
    ||H_c^2 rho_c^(1/2)||_HS <= Q.                       (E1)

Q is the square root of the fourth free-energy moment. A first-energy cap
alone does not provide E1. Let tau_c be the initial unconditional low
partial density, with no postselection or assumed fixed-state convergence.

## 1. Supply the interacting fourth moment without a form-power shortcut

Put B_c=1+H_c+V_c+K>=1 and L=1+2K. The typed first commutator gives
D(B_c^2)=D(H_c^2). On that domain, literal noncommutative multiplication
gives

    B_c^2 = H_c^2+2(V_c+K+1)H_c
                      +[H_c,V_c]+(V_c+K+1)^2.

Attach the Hilbert--Schmidt moment column using closedness or bounded
spectral cutoffs of H_c. The resulting uniform resource is

    ||B_c^2 rho_c^(1/2)||_HS <= Q+2LS+C+L^2 =: M.         (E2)

Consequently Tr rho_c B_c^4<=M^2, with the trace interpreted spectrally.
This is an operator identity with a bounded commutator, not a fourth power
of a noncommuting form inequality. The scalar reference energy is one,
the same convention as the root moment note.

The checked moment-sensitive theorem at spectral order s=4 therefore
gives, for the exact compressed potential W_c and fixed order J,

    alpha_exact(T_c)
      <= C_1[c^2+(T_c c^a)^(2/q)].                       (E3)

The coefficient C_1 depends on the fixed resources, including M and the
typed commutators; it is uniform in c, time and states satisfying E1.
Since q>=3 there is no saturation ambiguity in 2/q. Equation E3 is a
convergence statement when T_c c^a tends to zero. The finite-resource
bound, including its cap by two, remains the one in its source.

## 2. Explicit time-zero local potentials on the same windows

Choose a fixed potential truncation N with N+1>=a. Use the explicit
potential and spatial-tail theorems with a real smooth fixed-width cutoff,
not a characteristic cutoff. For any fixed 0<nu<m/v, they give

    ||W_c-V_R^[N](c)|| <= C_2 c^(N+1)+C_3 c^2 exp(-nu R).

For N=0 or 1 the coefficient tails in question vanish; the bound is still
valid with C_3=0. Orders and inputs remain fixed throughout. Choose

    R(c)=R_0+gamma log(1/c),  R_0>=0,
    gamma>=max(a-2,0)/nu,  0<c<=1,
    epsilon_c=(1+T_c)c^a ->0.                            (E4)

Bounded Duhamel compares the same corrected kinetic generator plus W_c
with that generator plus V_R^[N](c), at density cost at most twice time
times the displayed potential norm. Its two costs are O(epsilon_c).
Also c^2<=epsilon_c^(2/q) for sufficiently small c, because epsilon_c>=c^a
and 2a/q<2. Hence the full unconditional density comparison obeys

    alpha_loc(T_c)=O(epsilon_c^(2/q)).                    (E5)

The endpoint choice of gamma in E4 is allowed because the tail theorem
uses a fixed nu strictly below m/v, absorbing its finite polynomial tail.
No endpoint exponential rate nu=m/v without the polynomial is substituted.
No moving cutoff during a time protocol occurs: R(c) is fixed in time.

## 3. Fourth-moment endpoints with the regularity dependency displayed

The initial low density has the needed free moments by the commuting
physical-band free orders F_c^[J]<=H_(L,c) and the positive partial trace.
The explicit graph-regularity root composition proves, conditionally on
its checked coefficient premises, that V_R^[N](c) has a uniformly bounded
first commutator with F_c^[J] even for the radii E4. It retains momentum
derivatives in T_j and uses the smooth cutoff derivative bounds. This
particular composition still awaits a focused source-exposed check.

With that premise, the stationary fourth-moment theorem supplies uniform
second- and fourth-moment column bounds for actual and effective states.
Apply its already checked readout inequalities to E5, with
kappa_c=c/(2v)+1/Lambda_c=O(c). They give

    W2(actual free-energy law, target H0 law)
                           =O(c+epsilon_c^(1/(2q))),
    ||Gamma_actual-Gamma_target||_1
                           =O(c+epsilon_c^(1/q)).        (E6)

Gamma is the positive shifted graph density constructed from the column
(1+H)rho^(1/2), not a normalized state. The analogous homogeneous graph
formula follows from its own source inequality. The named energies remain
H_c and H0; the effective generator is F_c^[J]+V_R^[N](c).

These are sufficient upper rates. The density phase controls do not prove
sharpness of E6: a free relative phase can change coherences while leaving
energy-law probabilities unchanged. Nor do generic energy-law or graph
state-family counterexamples establish realizability by a fixed pulse or
by this particular pair of dynamics. No endpoint optimality is asserted.

The result concerns a spatially local potential with logarithmically growing
support radius, at each fixed time-zero comparison. The corrected kinetic
operator is generally nonlocal. Neither a finite propagation cone nor a
fixed-interval local effective Hamiltonian follows from E4--E6.

## Sources and remaining checks

The seal binds: moment-sensitive731/8361667a; corrected kinetic1049/402cbc03
and449/a89c8915; potential600/8f1e13d1 and496/47d94f2b; spatial626/62227375
and328/f9f91957; fourth867/34bf78f5 and505/4bc61a1a; root graph154/4282b727.
All complete proof bodies were previously read at these identities. The
new work is E2 and the explicit parameter/resource composition E3--E6.
Independent-before-root derivation and source-exposed checking are distinct.
No program was used to certify these analytic implications. Preserve the
root graph dependency, the stricter E1 resource, and all counterexamples.


## Third exact historical core: source-exposed crosscheck

The second composition ends above. The following complete check examined both
roots after exposure. It is not an independent pre-exposure derivation.

# Source-exposed check of graph regularity and moment-local energy endpoints

This ordinary mathematical check supports both named root compositions under
their stated fixed-data, domain, moment and protocol hypotheses. In particular,
the actual differential coefficient maps preserve Schwartz regularity, smooth
localization has a radius-uniform free commutator, and the stationary
fourth-moment conversion gives the displayed density and energy-endpoint rates.
No load-bearing formula repair is required. Graph G5 needs the wording
precision **nonnegative integer k** in place of “integer k.”

This is a source-exposed comparison, not an independent-before-root derivation.
It does not assign root acceptance, formal verification, model diversity,
retained status or a global negative-packet verdict. The root notes and their
seals retain their original historical statuses. No input mathematical or
publication source was edited; this comparison and its evidence are separate artifacts.

## 1. Sources, actual reading and chronology

Let R denote `/Users/jonreilly/Documents/Codex/research_runs/toe_leap_20261009/resume_20261012`.
Except for the last two canonical parents, the following paths are relative
to R. The labels are local references in this note, not new claim identifiers.

| Label | Exact source | Lines | SHA-256 |
|---|---|---:|---|
| G | EFFECTIVE_POTENTIAL_GRAPH_REGULARITY_ROOT_COMPOSITION.md | 154 | `4282b72723f572ca518742fca1eb5918c8ac39d02dc7178e18802ef34d5e9389` |
| E | MOMENT_LOCAL_ENDPOINT_ROOT_COMPOSITION.md | 126 | `7ab78b9db65646dacd073622f183857af82cb979231dce25b122e5e2c5a3246b` |
| M | MOMENT_SENSITIVE_DYNAMICS_INDEPENDENT.md | 731 | `8361667a12e01be16c40b01a3fc6aff14512fb1fed6f29ccdd9cac2e4c408c09` |
| F | FOURTH_MOMENT_ENDPOINT_INDEPENDENT.md | 867 | `34bf78f52b8928dacece75750ad8a881f4fe1b59f49dc943ced7bd9ed5b6dd38` |
| FC | FOURTH_MOMENT_ENDPOINT_CROSSCHECK.md | 505 | `4bc61a1a3c7289e04051a2d59b8d05601045490a0bf78168a1cdec3fa8968060` |
| I | CORRECTED_DISPERSION_INDEPENDENT.md | 1049 | `402cbc03585ac1cf0fc32facfc18b889de09a2fc9b3bb1449dfda47beb813c0d` |
| IC | CORRECTED_DISPERSION_CROSSCHECK.md | 449 | `a89c8915a2f1207aaee8fbef7273494126445d4e26fbda625d418f0557a83cb6` |
| P | EFFECTIVE_POTENTIAL_INDEPENDENT.md | 600 | `8f1e13d1ca4c42bbf4e5483c4035cacf28fd2bc82ee4b470776409e7753323be` |
| PC | EFFECTIVE_POTENTIAL_CROSSCHECK.md | 496 | `47d94f2b67f97b1180d2b32a1445d2afda9b3ce8322ec5a278c47d486d872160` |
| S | EFFECTIVE_POTENTIAL_SPATIAL_INDEPENDENT.md | 626 | `622273759a10a8d69eb05d01363dddca23fcdfb4f0aa9ab7c994e98c45ae76fe` |
| SC | EFFECTIVE_POTENTIAL_SPATIAL_CROSSCHECK.md | 328 | `f9f919573dfe48c433f3b366fe7659add901330e5511f8970f615dde1a6226eb` |
| Current | ../correlation_worktree/docs/CURRENT_PRESERVING_REFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-12.md | 601 | `763082a6faa8bea3f6be74ddc7ee81bf288c00740085804e62f701a1576283ff` |
| Local | ../correlation_worktree/docs/LOCAL_EVEN_CONTINUUM_BOUNDED_THEOREM_NOTE_2026-10-12.md | 731 | `b5a8394a9d8c17bb9559597a68b061ad3872201ebf9793bd5c9f10b15ac2c6aa` |

The complete G seal has SHA-256
`1d1a0d04d47f2ed1efa1d1fc28c57b4d52918b89419867d9e349e73b207fe11f`;
the complete E seal has SHA-256
`1a2199f3721efa2d96f88e33efa8fea9f06d19df578f402abbe4f49588d08d51`.
Their source and parent bindings agree with these exact bytes. This identity
agreement supplies provenance, not proof of an analytic assertion.

G, E, both seals, M, F, FC, I and IC were read completely for this task.
P, PC, S, SC, Current and Local have actual earlier complete-read coverage
at the same identities; that coverage is reused, with the relevant coefficient,
compression, spatial, real-CAR and domain premises refreshed here. No claim of
a new complete read of those six is made. The earlier publication-preparation
task's mechanical reuse of root acceptance is not substituted for a mathematical
read. `READ_COVERAGE.json` records the actual complete ranges and refresh ranges.

The neutral plan was sealed at 2026-10-13T03:07:21.749699+00:00 before opening
G and E, with prior spatial/effective-potential exposure already disclosed.
Its SHA-256 is
`3304eb1516644c96824a43198065e699b2e36e4555735895a09b307866a5a674`.
This ordering does not make an explicitly source-exposed comparison blind.
The predecessor/recovery exposure and transport history of S remain in its
unchanged source and evidence; no independence status is upgraded here.

The applicable instructions remain the previously read pinned procedures
(main `516cb69d8487ff04f8a48e065d3dcbe71d7dd237`, ai/execution
`3a4b2c66a1ead7a1c48b4359627e968f681e3c39`), subject to this bounded task.
No Git refresh is claimed. Root BV/history, active nonautonomous work, new
unpublished preparation candidates and campaign checkpoint were excluded.
References to excluded works inside allowed sources were not followed.

## 2. Actual coefficient maps and the corrected kinetic domain

Fix m,v>0, a fixed finite polynomial with fixed real compact smooth inputs,
fixed potential order N and fixed kinetic order n. None of these quantities
varies with c or the localization radius. Put alpha_*=m/v. P (4), (10) and
S (S1)--(S4) give the actual coefficient representation

    (T_j f)^hat(p) = sum_(k=0)^floor(j/2) R_(j,k)(p) partial_p^k fhat(p),
    R_(j,k) = [c^j] M(c,p)(q(c,p)-p)^k/k!,
    q(c,p)=arcsin(cp)/c.                                      (C1)

Coefficient extraction in C1 is at c=0 for fixed real p. It is not a Taylor
expansion over the singular moving band edge. Explicitly, with t=arcsin(cp),
w=sqrt(1-c^2p^2) and B=I/2+sigma_z/4, the parent formula is

    A(c,p)=2 sqrt(1+alpha_*^2 c^2/4)/(1+w),
    d(c,p)=atan((p/alpha_*)A(c,p))-atan(p/alpha_*),
    M(c,p)=w^(-1/2) sinc(t/2) exp(itB) exp(-i d(c,p)sigma_z/2).

The pole proof expands the
frame germ on each sigma_z component s=+/-1 as

    (1+[p/(p-i alpha_*)]delta)^(-s/4)
    (1+[p/(p+i alpha_*)]delta)^( s/4),
    delta=A(c,p)-1=O(c^2).

Every fixed even c coefficient of delta is polynomial in p, as are the
coefficients of the remaining cell factors and q-p. A term with l frame
denominator factors and k transported derivatives starts at order 2(l+k).
Thus R_(j,k) lies in the matrix ring C[p,(m^2+v^2p^2)^(-1)] and each of its
two possible finite poles has order at most floor(j/2)-k. In particular,
there are no real poles. All real-axis derivatives have polynomial growth.

For f in C_c^infinity, fhat is Schwartz. Every seminorm of
R_(j,k) partial_p^k fhat is finite by the product rule: a fixed polynomial
growth factor is absorbed by the arbitrarily rapid decay of the corresponding
higher derivative of fhat. The finite sum in C1 and Fourier inversion therefore
give T_j f in Schwartz space. The exact identities
M(c,-p)=conjugate(M(c,p)) and q(c,-p)=-q(c,p) preserve Fourier reflection
reality; their coefficients show that T_j f is real when f is real.

This checks G1 as a differential representation. In particular P (8) is

    (T_2 f)^hat = [p^2 C-i kappa(p) sigma_z/2] fhat
                          +(p^3/6) partial_p fhat,
    C=5I/96-sigma_z/8,
    kappa(p)=mp(m^2+2v^2p^2)/(8v(m^2+v^2p^2)).                (C2)

The final term cannot be dropped. FC's section 4 established a conditional
regularity implication for an unspecified single Fourier multiplier and
explicitly left application to the actual T_j unverified. C1, with all its
derivatives retained, supplies the missing application here. It does not
retroactively make FC a read of P or assert that T_j is bounded on bare L2.

The full-low kinetic symbol in I (25) is

    e_c^[n](p)=E(p) sum_(l=0)^n d_l(u(p)) c^(2l) p^(2l),
    E(p)=sqrt(m^2+v^2p^2),  u(p)=v^2p^2/E(p)^2 in [0,1].     (C3)

The d_l are fixed polynomials nonnegative on [0,1], with d_0=1. Their maxima
on that interval, c<=c0 and E<=C<p> give

    E(p)<=e_c^[n](p)<=C_(n,c0,m,v)<p>^(2n+1).                 (C4)

The upper bound is global on the real axis. It follows from the finite
coefficient formula, not from extending a physical-band remainder estimate.
F_c=dGamma(e_c^[n]) is the positive selfadjoint Fock multiplication operator
on its maximal direct-sum domain. Outside the physical band there is no
assertion D(F_c)=D(H0) or F_c<=H_(L,c). Those statements are unnecessary.

## 3. Literal CAR flow, constants and smooth local approximants

Let P_+ be the supplied low polarization. On the real coefficient space,

    gamma(h)=a^*(sqrt(2)P_+h)+a(sqrt(2)P_+h),
    {gamma(h),gamma(k)}=2(h,k)_R I,
    gamma(h)^2=||h||_2^2 I,  ||gamma(h)||=||h||_2.             (C5)

Local L18 and Current's real isometry conventions fix this normalization.
The signed coefficient generator for F_c is
d_c=e_c^[n] D/E, where D(p)=-vp sigma_x-m sigma_y, D^2=E^2 I. It preserves
the polarization and anticommutes with position conjugation. Therefore
exp(it d_c) preserves real coefficient vectors, |d_c|=e_c^[n], and the
Fock implementation gives

    exp(it F_c) gamma(h) exp(-it F_c)=gamma(exp(it d_c)h).

For real h in D(e_c^[n]), the norm derivative at zero is
gamma(i d_c h), with norm ||e_c^[n]h||_2. The vector i d_c h is real;
we have not treated the real-linear field map as complex-linear.

For an ordered even word U_a=product_k gamma(h_(a,k)), apply the ordinary
Leibniz rule to this norm-differentiable orbit, without reordering its slots.
The free generator is even. No graded Leibniz sign or additional covariance
factor enters this derivative. A finite formally selfadjoint polynomial
V(c)=sum_a z_a(c) U_a consequently obeys

    ||V(c)|| <= K_* := sum_a sup_c|z_a(c)| product_k ||h_(a,k)||,
    ||[F_c,V(c)]|| <= L_* := sum_a sup_c|z_a(c)| sum_k
           sup_c||e_c^[n]h_(a,k)|| product_(l!=k)||h_(a,l)||. (C6)

For (U+U*)/2 include both partners with their literal weights 1/2. Their
two norm bounds then sum to the original word bound, not twice it. Empty
words have zero differentiated sum. No division by a slot norm is involved,
so zero slots cause no exception. For the actual V^[N](c), the h's are the
fixed finite collection T_j f and the scalar weights are fixed numbers
times c^l. C1 and C4 make all C6 resources finite uniformly for 0<c<=c0.

The actual lattice commutator assumptions are also supplied by the fixed
smooth class, rather than by a band-edge guess. I's exact cell intertwining
includes every alias and gives, for each nonnegative integer r,

    || |D_c|^r C_c f||_2<=||E^r f||_2.

Here the periodic cell-energy multiplier is
sqrt(m^2+4v^2 sin^2(ck/2)/c^2)<=E(k), and C_c is a contraction. The actual
real-field flow therefore bounds the r-th commutator of a polynomial by

    ||ad_(H_c)^r(V_c)|| <= sum_a |z_a| sum_(r_1+...+r_d=r)
                    [r!/(r_1! ... r_d!)] product_k ||E^(r_k)f_(a,k)||.

Literal half weights again give the same bound for formal symmetrization.
These supply finite uniform kappa_r for each required positive r<=q-1;
take kappa_0=K as in section 5. The norm-flow generator argument below supplies
the typed domains; a bare formal core calculation would not suffice.

Here C6 is a typed commutator statement. If the derivative of the orbit of
V is D_V, then, for psi in D(F_c),

    exp(it F_c)V psi = [exp(it F_c)V exp(-it F_c)] exp(it F_c)psi

has a strong derivative at zero equal to D_V psi+iV F_c psi. The generator
criterion proves V psi in D(F_c) and i[F_c,V]psi=D_V psi. Thus V preserves
D(F_c), and the commutator has the bounded extension used in F2. A mere
operator-norm approximation of V would not prove this domain statement.

An explicit cutoff family also verifies all radius quantifiers. For I=[a,b],
fix w0>0 and a real smooth eta with 0<=eta<=1, eta=0 on (-infinity,0],
eta=1 on [1,infinity). Set

    chi_R(x)=eta((x-a+R+w0)/w0) eta((b+R+w0-x)/w0), R>=0.     (C7)

It equals one on I_R=[a-R,b+R] and is supported in I_(R+w0). For every
nonnegative integer k,

    sup_R||partial_x^k chi_R||_infinity
      <= w0^(-k) sum_(l=0)^k binom(k,l)
                       ||eta^(l)||_infinity ||eta^(k-l)||_infinity.

Thus Leibniz' rule bounds ||chi_R h||_(H^k) by a constant times
sum_(l=0)^k||partial_x^l h||_2, independently of R. Take k=2n+1 in C4.
This proves the uniform differentiated-field bound for chi_R T_j f.
G5's “every integer k” is interpreted as nonnegative integer k; its finite
sum and this proof concern precisely those k. No negative Sobolev assertion
is needed.

Apply this cutoff after T_j, preserving each original word order and formal
adjoint partner, in every coefficient of V^[N](c). The resulting V_R^[N](c)
is bounded, selfadjoint and even, belongs to A_even(I_(R+w0)), and satisfies
C6 uniformly in c and R. Locality refers to support of the real coefficient
before polarization; P_+h itself need not have that support. Selfadjointness
uses formal adjunction, not a CAR identity accidental to the original inputs.
The finite c degree and number of slots stay fixed. A growing R(c), including
the logarithmic choice below, does not consume this commutator resource.

The width w0 is fixed. Shrinking-width or sharp cutoffs are not covered by
these derivative bounds. Indeed P (28)--(29) give a nonzero exponential
exterior tail for T_2 f when f is a nonzero nonnegative bump in one component.
A sharp cutoff at a finite exterior point then creates a jump, so its
coefficient is not H1. Since e_c^[n]>=E, that coefficient need not be in the
differentiated-field domain. Its L2 field and bounded-potential Duhamel
approximation still make sense. This example rejects the attempted inference
from L2 approximation to the graph premise; it does not say every polynomial
word must fail, since CAR or coefficient cancellations can remove a term.

For finitely many fixed operators from this family and scalar BV coefficients
in time, the potential and commutator variations are bounded by the sums of
coefficient variations times their C6 bounds. This checks G's conditional BV
resource statement when R(c) is fixed during each protocol. A time-varying
radius/interval, uncontrolled total variation, or a density theorem for such
controls is an additional problem, not a consequence of C7.

## 4. Initial moments, shifted moments and later full-low propagation

For a positive trace-one actual density rho_c, write

    S=||H_c rho_c^(1/2)||_HS,
    Q=||H_c^2 rho_c^(1/2)||_HS.

The root assumes uniform upper bounds on these quantities. Q^2 is the
fourth free-energy moment; Q is not that moment. In a spectral decomposition
of rho_c, finite Q means every occupied vector lies in D(H_c^2), with the
square-summable weighted H_c^2 columns. Closedness gives the full moment
column. No occupied-vector D(H_c^4) assertion or unbounded trace cycle is used.

Let ||V_c||<=K, V_c=V_c*, V_c D(H_c) subset D(H_c), and let the bounded
extension of [H_c,V_c] have norm at most C. Put

    A_c=V_c+(K+1)I,  L=1+2K,  B_c=H_c+A_c=1+H_c+V_c+K.

B_c>=1, ||A_c||<=L, and D(B_c)=D(H_c). Moreover
D(B_c^2)=D(H_c^2): one direction uses that A_c preserves D(H_c), and the
other subtracts A_c psi from B_c psi. On this common square domain,

    B_c^2=H_c^2+2A_c H_c+[H_c,V_c]+A_c^2.                    (C8)

This is literal multiplication, including its commutator order and sign.
Multiply the domain-valid columns of rho_c^(1/2), first with a finite-rank
right cutoff if needed, and take their Hilbert--Schmidt norm. Closedness
and convergence of the columns give

    ||B_c^2 rho_c^(1/2)||_HS <= Q+2LS+C+L^2 =: M,
    Tr rho_c B_c^4 <= M^2.                                  (C9)

This is exactly E2. The argument does not raise a noncommuting form inequality
to the fourth power. The scalar reference energy is one as in E; restoring
another fixed unit rescales all terms consistently.

Let tau_c be the unconditional initial low partial density. On the actual
physical range the free Fock multipliers strongly commute and obey

    H0<=F_c^[J]<=H_(L,c)<=H_c,

where the first inequality also holds globally on full low Fock space.
The physical support of tau_c and bounded tests min((F_c^[J])^l,B), l=2,4,
followed by increasing B, give

    Tr tau_c (F_c^[J])^2<=S^2,
    Tr tau_c (F_c^[J])^4<=Q^2.                              (C10)

The partial-trace identities are applied to bounded tests before the limit.
All powers here are powers of commuting multiplication operators, so this
step is different from the noncommuting shift conversion C8.

After replacing the exact compression by V_R^[N], the target need not stay
in the physical band. Use the full selfadjoint F_c^[J] and its C6 commutator
on that full carrier. F's stationary domain identities for H+V then give,
uniformly for every real time,

    S_c(t)<=S+2K,
    Q_c(t)<=Q+4KS+2C+4K^2,
    S_0(t)<=S+2K_*,
    Q_0(t)<=Q+4K_*S+2L_*+4K_*^2.                            (C11)

In the last two bounds first propagate the F_c^[J] columns from C10, then
use globally commuting H0<=F_c^[J]. S_0,Q_0 are H0 readout resources, not
moments of the interacting target generator. The interacting spectral
moments are conserved; the free moments are uniformly bounded, not claimed
conserved. No physical-band estimate is reapplied to the evolved localized
target. These are the precise resources needed by E and the stationary
instance of G. G's switching/BV instances instead require F's stated uniform
switching or variation resources and their own density comparison.

## 5. Literal substitution into the moment-sensitive density theorem

Fix J>=0 and write a=2J+2, q=2J+3=a+1. In M use its kinetic index r=q,
moment order s=4 and energy reference mu=1. The shift S_c in M is then
exactly B_c in C8, and its cap is M_4=M^2 from C9. Its interpolation
parameters are k=2, eta=1, theta=2/q<1 and N_4=M. The required actual
commutators are through max(q-1,1)=q-1, exactly those assumed in E.

For explicit constants let C_l be M9's graph recurrence with C_0=1,
a_0=max(K,1) and kappa_j bounding ad_(H_c)^j(V_c), kappa_0=K. With
Lambda_c=sqrt(m^2+2v^2/c^2), beta_c=||Q_hi V_c P_hi||<=K and
L_J=1/(2v^a), put

    d_(q,c)=C_q[L_J c^a+beta_c Lambda_c^(-q)],
    h=min(1,M C_2 Lambda_c^(-2)),
    l(T)=min(2,2^(1-2/q) M [T d_(q,c)]^(2/q)).               (C12)

P_hi projects to high vacuum and Q_hi=1-P_hi; they are not spectral
projections of the interacting generator. M's bounded right-weight
interpolation and normal-state column argument give the actual finite bound

    alpha_exact(T)<=min(2,2 sqrt(h^2+l(T)^2)+h^2).            (C13)

The effective initial density in C13 is the full tau_c, not its normalized
high-vacuum corner. Its additional discarded positive partial density costs
at most h^2. Orthogonal low and high columns give the square root in C13.
No postselection or fixed-target-state convergence is assumed.

Since Lambda_c^(-q)=O(c^q), q=a+1 and all C_l are uniform fixed resources,
d_(q,c)=O(c^a). Hence h=O(c^2) and l(T)<=C(Tc^a)^(2/q). C13 gives

    alpha_exact(T_c)<=C_1[c^2+(T_c c^a)^(2/q)],              (C14)

with the separate finite cap by two retained in C13. This checks E3,
including its M versus M^2 convention and exponent. In particular the
root does not confuse the initial free fourth moment with a fourth moment
of a time-dependent instantaneous interacting generator. Conservation of
the shifted interacting moment in M is stationary. C14 is not a theorem
for arbitrary switching or BV controls.

## 6. Exact compression, localization and the time-radius choice

W_c is the exact high-vacuum compression, extended unitally to full low Fock
space. In the low-first grading the actual field is

    gamma(ell,h)=gamma_L(ell) tensor I+Z_L tensor gamma_H(h).

P (23)--(26) retains every even high subset, its parity crossing sign and
the upper-triangle covariance 2<h_i,P_0 h_j>. Empty subsets, scalar terms
and lower-degree contractions all remain in the exact operator. Fixed smooth
inputs make the nonempty high contractions smaller than every fixed power;
they are not asserted identically zero at finite c. P's full-low norm bound is

    ||W_c-V^[N](c)||<=C_N c^(N+1).                           (C15)

For the fixed-width smooth cutoff, S/SC's ordered CAR telescoping gives, for
N>=2 and D=floor(N/2)-1,

    ||V^[N](c)-V_R^[N](c)||
       <=C_N' c^2(1+R)^D exp(-alpha_* R)
       <=C_(N,nu)' c^2 exp(-nu R), 0<nu<alpha_*.             (C16)

The constants are independent of c,R at fixed data and fixed nu. The c^2
factor arises because T0 and T1 are supported in I: any changed slot has
order at least two. For N=0,1 the spatial difference is exactly zero.
The final inequality absorbs the finite polynomial tail into alpha_*-nu;
it would not follow with nu=alpha_* after discarding that polynomial.
Smearing or CAR cancellations may improve or remove this upper bound, and
no lower bound for every coefficient or word is asserted.

Compare on full low Fock space F_c^[J]+W_c and F_c^[J]+V_R^[N](c), using
the identical selfadjoint kinetic operator and domain in both. Bounded
selfadjoint perturbation gives both generators domain D(F_c^[J]). Strong
Duhamel on that domain, extended by density, bounds their unitary difference
by |t| times C15+C16. Trace-ideal telescoping doubles this for a normal density.
Together with C13 it proves G6:

    alpha_loc(T_c)<=min(2,alpha_exact(T_c)
            +2T_c[C_N c^(N+1)+C_(N,nu)' c^2 exp(-nu R(c))]). (C17)

This Duhamel step itself requires bounded potentials, not their commutator
regularity. The latter was needed separately for C11. The potential can
leave the band because C17 uses the full-low operator; no zero-energy
extension of an actual lattice Hamiltonian is introduced.

Take fixed N with N+1>=a, 0<c<=min(c0,1), R0>=0 and fixed

    R(c)=R0+gamma log(1/c),  gamma>=(a-2)/nu,
    epsilon_c=(1+T_c)c^a ->0.                               (C18)

Here a>=2, so the displayed lower bound on gamma is nonnegative. The root's
max(a-2,0) notation is equivalent. The logarithm uses the fixed spacing
reference implicit in c<=1. For T_c>=0,

    T_c c^(N+1)<=epsilon_c,
    T_c c^2 exp(-nu R(c))
      =exp(-nu R0) T_c c^(2+nu gamma)<=epsilon_c,
    (T_c c^a)^(2/q)<=epsilon_c^(2/q).

Also epsilon_c>=c^a and 2a/q=2-2/q<2, hence c^2<=epsilon_c^(2/q).
For sufficiently small c, epsilon_c<1 and epsilon_c<=epsilon_c^(2/q).
Thus every term of C17 is bounded by a fixed multiple of epsilon_c^(2/q):

    alpha_loc(T_c)=O(epsilon_c^(2/q)).                       (C19)

Equality in gamma's lower bound is permitted because nu<alpha_* was fixed
before C18. A sharp alpha_* rate with its polynomial discarded would not
justify the same endpoint reasoning. At J=0 one can take N=1, with zero
spatial tail and a fixed radius. The root's N=0 tail statement is true as
a general coefficient fact, although N=0 does not meet N+1>=a in this
particular composition. At J=1 one may take N=3 and gamma>=2/nu.

Every radius is fixed during the corresponding time evolution. Constants
are not uniform in J,N, unrestricted input seminorms, polynomial complexity,
shrinking width or nu tending to alpha_*. The window condition is the stated
T_c=o(c^(-a)) as c tends to zero. The freedom to localize a bounded potential
on still larger windows, considered alone, does not remove C14's separate
actual-to-exact-compression time restriction.

## 7. Energy laws and full graph-weight endpoints

Place the actual density by the specified isometric Fock map iota_c and the
target by tensoring its low density with the high vacuum. These are normal
trace-one densities on the common carrier and their trace distance is bounded
by alpha_loc. Let L0=H0 tensor I on that whole carrier. On the actual physical
range, H_c and L0 strongly commute, and F's bridge is

    0<=H_c-L0<=kappa_c H_c^2,  L0<=H_c,
    kappa_c=c/(2v)+1/Lambda_c=O(c).                           (C20)

H_c in C20 acts on the placed actual range; it has not been assigned a
fictitious action on the orthogonal complement. The target readout is H0,
even though its generator is F_c^[J]+V_R^[N]. Use C11 to bound the time
dependent column resources by fixed S_c,Q_c,S_0,Q_0 below.

The commuting spectral coupling in C20 bounds the actual H_c law's W2
distance to the L0 law in its placed density by kappa_c Q_c. The total
variation distance of that L0 law from the target H0 law is at most
t=alpha_loc/2. Remove the common part of the two laws. Their residual
positive measures have equal mass at most t; coupling them and using
nonnegative energies gives cost at most

    integral x^2 dmu_res + integral y^2 dnu_res
                 <=(Q_c+Q_0)sqrt(t).

The last step is Cauchy--Schwarz against each dominating probability law
with its fourth moment. Taking the square root of this cost and adding the
native bridge proves the exact first inequality in G7:

    W2<=kappa_c Q_c+sqrt(Q_c+Q_0)(alpha_loc/2)^(1/4).          (C21)

For graph weights define positive trace-class operators by columns:

    Xi_c=iota_c(H_c rho_c^(1/2))(H_c rho_c^(1/2))*iota_c*,
    Gamma_c=iota_c((1+H_c)rho_c^(1/2))((1+H_c)rho_c^(1/2))*iota_c*,

with analogous target H0 columns tensored with high vacuum. These operators
are not normalized states. The common-weight trace interpolation used in F
has the following finite-cutoff form for a positive bounded invertible weight A:

    ||A Delta A||_1 <= ||Delta||_1^(1/2)
                                      ||A^2 Delta A^2||_1^(1/2).

It follows by applying three-lines and trace duality to A^(2z) Delta A^(2z),
whose imaginary boundary factors are unitary. With Delta the difference of
two densities, the upper boundary is bounded by the sum of their A^4 moments.
Regularize positive spectral cutoffs of L0, or of 1+L0, and then pass to the
limit by Hilbert--Schmidt convergence of the moment columns. This explains
the particular unbounded substitution needed here without assuming that
the densities share an eigenbasis or that an unbounded trace is cyclic.

C20 bounds the actual native column difference by kappa_c Q_c. Combining
the product inequality ||XX*-YY*||_1<=(||X||_2+||Y||_2)||X-Y||_2 with the
common-weight step gives

    ||Xi_c-Xi_0||_1 <=2kappa_c S_c Q_c
                              +sqrt(alpha_loc)sqrt(Q_c^2+Q_0^2),
    ||Gamma_c-Gamma_0||_1 <=2kappa_c(1+S_c)Q_c
       +sqrt(alpha_loc)sqrt((1+2S_c+Q_c)^2+(1+2S_0+Q_0)^2).  (C22)

For the shifted formula, 1+2S+Q bounds the HS norm of the squared graph
weight column, while 1+S bounds the unsquared column. This checks all
constants in G7, with the common fixed energy unit understood. A bounded
coefficient inserted between graph weights additionally needs its own
coefficient comparison if the actual and target coefficients differ.

Uniform C11, C19 and kappa_c=O(c) now give, uniformly on [-T_c,T_c],

    W2=O(c+epsilon_c^(1/(2q))),
    ||Gamma_c-Gamma_0||_1=O(c+epsilon_c^(1/q)),
    ||Xi_c-Xi_0||_1=O(c+epsilon_c^(1/q)).                     (C23)

These are exactly E6 and its stated homogeneous companion. As checks on the
indices, J=0 gives density power 2/3, W2 power 1/6 and graph power 1/3 in
epsilon; J=1 gives 2/5, 1/10 and 1/5. No optimality claim is inferred from
these sufficient bounds.

## 8. Adversarial disposition and obligations

| Root argument | Actual finding and necessary boundary |
|---|---|
| G1, lines 18--37 | Actual differential coefficient representation, pole ring, Schwartz preservation and reality checked; no multiplier-only replacement or bare-L2 operator bound. |
| G2--G3, lines 41--74 | Full-line kinetic growth and real-field norm differentiation give the stated constants and typed first commutator; literal adjoint half weights retained. |
| G4--G5, lines 78--111 | Fixed-width smooth cutoff gives uniform resources for every R>=0; k means nonnegative integer. BV statement is conditional on fixed-in-time R and bounded variation resources. |
| G6, lines 115--135 | Initial moment transfer, full-low propagation and same-kinetic Duhamel compose; a separate density theorem for the actual protocol remains necessary. |
| G7, lines 137--148 | W2 and shifted graph constants agree with the column definitions and actual/target energies; no normalized graph-state or detector inference. |
| E1--E3, lines 9--51 | Typed square-domain identity supplies cap M_4=M^2; s=4 substitution in M gives the exact exponent with commutators through q-1. |
| E4--E5, lines 55--79 | Both potential costs are O(epsilon), their absorption is valid, and endpoint gamma is allowed only with fixed nu<m/v. |
| E6, lines 83--115 | Full-low first commutator and stationary fourth moments justify all displayed rates; the target may leave the physical band. |

The following stronger routes remain invalid or unproved, as already delimited
by the sources and made concrete above:

- Bounded V or small operator-norm potential error alone does not give its
  free commutator or fourth-moment propagation. F's bounded rank-two even
  counterexample is outside the regular fixed smooth CAR class and remains
  a control against that proposed strengthening.
- A sharp local CAR approximation supplies the bounded Duhamel comparison,
  but its L2 estimate cannot substitute for the smooth-cutoff graph estimate.
  Nonzero coefficient tails can also cancel in an entire CAR word.
- A noncommuting inequality such as B_c<=H_c+constant cannot be raised to
  its fourth power to obtain C9. The typed identity C8 supplies that step.
- Physical-band comparability and initial moment transfer do not imply that
  the local target stays in the band. Its later H0 resource uses global
  H0<=F_c and the full-low propagation theorem instead.
- Stationary conservation in M does not prove the density estimate for
  switching/BV protocols. G keeps that density theorem conditional. The
  mere availability of a bounded-variation moment theorem does not fill it.
- Density relative-phase controls do not prove optimal W2 rates: a free
  relative phase can alter coherence without changing the energy law.
  F's generic state-family endpoint examples do not establish realization
  by a fixed pulse or sharpness for this particular pair of dynamics.
- Uniform fourth moments are a sufficient resource, not a necessary one.
  F's weaker squared-energy-tail controls and counterexamples remain valid.
  No convergence of fourth moments is inferred from their uniform bounds.
- Only the time-zero bounded potential is spatially localized. The corrected
  kinetic multiplier need not have finite propagation. Growing support,
  energy endpoints and same-kinetic Duhamel do not establish a causal cone,
  a fixed-interval full Hamiltonian, unscaled-current convergence or an
  identified selfadjoint detector.

The new analytic work is the source-exposed checking of C1--C23 and their
domains, constants and quantifiers. No scientific numerical, symbolic or
formal program was executed. Bookkeeping checks of copied bytes, parent
bindings and final membership are separate evidence and contain no mathematical
acceptance predicate. Navigation outputs that were truncated were not counted
as completed source reading; full source reads and untruncated focused refreshes
are recorded separately. No transport failure or failed scientific execution
occurred in this assignment.

Only this note and `effective_potential_graph_endpoint_crosscheck/` were
written. Original scientific sources, root seals, earlier spatial freezes,
the publication-preparation package, canonical repository, Git/PR/cache/audit
state and editable prompts were untouched. No platform instruction was changed,
no delegation or other-chat message was sent, and the selected model/effort
was retained. The campaign deadline remains 2026-10-13T16:42:30Z.

The source-specific application gap named in FC is filled for the actual
fixed finite smooth potential and the fixed-width smooth local family. Root
review of this final comparison remains outstanding; retained/formal/model-
diverse review, any publication action, N1/N5 packet obligations and additional
protocol/preparation/detector/causal claims are not performed by this artifact.
Its final freeze binds exact source snapshots, honest reading coverage,
the precision record, progress chronology and this complete mathematical note.


## End of exact historical core; assembly evidence

The selected source bytes, original freezes, complete accepted comparisons,
precisions, exposure records and failure records are preserved in the bounded
source archive. `SOURCE_IDENTITIES.json` resolves every selected source alias
to its exact content-addressed archive path. `BODY_COPY_MANIFEST.json` and
`LINE_PIECE_MAP.json` give byte intervals and line ranges; complete assembly
and new-file diffs are separate from the empty core-change diffs.

Selected core identities:

- `EFFECTIVE_POTENTIAL_GRAPH_REGULARITY_ROOT_COMPOSITION.md`: `4282b72723f572ca518742fca1eb5918c8ac39d02dc7178e18802ef34d5e9389`.
- `MOMENT_LOCAL_ENDPOINT_ROOT_COMPOSITION.md`: `7ab78b9db65646dacd073622f183857af82cb979231dce25b122e5e2c5a3246b`.
- `EFFECTIVE_POTENTIAL_GRAPH_ENDPOINT_CROSSCHECK.md`: `41fdd517ab0e3a492acf04688f9633eb5f873f4265ea591bf88b3a46bbf0227a`.

Exact ordinary acceptance/comparison/precision records:

- `EFFECTIVE_POTENTIAL_GRAPH_ENDPOINT_ROOT_ACCEPTANCE.json`: `91e59c40a122d16d3d5175c2eef225084f029a1ad4bdd9732e07da487263843b`.
- `effective_potential_graph_endpoint_crosscheck/PRECISION_RECORD.json`: `77c78b18dd8bcc1eed1d4de01e48764a0f8ec84d5a3dbada4005eff40b0278b8`.

This new wrapper neither repairs an original mathematical body nor relabels
a historical source-exposed comparison as independent work. Historical pending,
false and limited-coverage fields stay unchanged in their original files.
The later exact acceptance is recorded alongside them, never inserted into
those files. All scopes and precisions remain attached to their exact sources.

`DEPENDENCY_REGISTRY.json` distinguishes direct canonical or same-packet
support, archived provisional premises, method/context ancestry and mere branch
lineage. `PROVENANCE_CLOSURE.json` closes the member lists of seven named freezes;
references inside those lists do not imply recursive proof or archive closure.
No finite-history, observable687 or new all-time result belongs to this note.

Root accepted the exact source assembly at its separate source review.
This publication projection changes wrappers only; the original package
and all its pending, false, failure and exposure records remain literal
archived bytes. The [source recovery and scope](../.claude/science/physics-loops/toe-prepared-energy-20261013/SOURCE_RECOVERY.md)
binds every immediate member of the accepted source freeze.
The [identity-only runner](../scripts/effective_potential_graph_local_endpoint_identity_2026_10_13.py) verifies source bytes,
maps and reconstruction. It executes zero mathematical predicates and
supplies no analytic, formal, model-diverse, retained-audit or no-go status.
Publication preparation may test it only in a temporary noncanonical
root. Such scratch results are separate from later canonical execution.
The [block handoff](../.claude/science/physics-loops/toe-prepared-energy-20261013/HANDOFF.md) and
[review history](../.claude/science/physics-loops/toe-prepared-energy-20261013/REVIEW_HISTORY.md) distinguish
source preparation from root-owned installation, caches, graph and
staged compatibility checks. New publication review and those checks
remain pending in this frozen source projection. N1/N5 remain pending
where applicable. Editable prompt files changed: none.
