---
claim_type: bounded_theorem
target_claim_type: bounded_theorem
actual_current_surface_status: conditional-support
trace_class: upstream_support
target_claim_id: thermal_resonance_halt_bounded_theorem_note_2026-10-17
target_blocker_text: "The exact emitter uses supplied complex hopping; a real replacement needs an explicit product-seed preparation and complete-output handoff."
source_of_blocker_text: user_goal
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Check the portable execution and publication surfaces; pursue native pure-seed and real-controller supply, thermal preparation for this doubled apparatus, and complete capture/reset/reuse."
conditional_surface_status: "Exact supplied positive real ordinary-NN qubit apparatus, exact pure product seed, real C1 classical setup controls, nominal coupling family, and inherited complete-output resonance theorem."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "An explicit finite controlled preparation of the useful rail sector and its complete autonomous-output composition, with physical scalar, old aging, positive loads and finite horizon retained."
audit_required_before_effective_retained: true
bare_retained_allowed: false
source_science_acceptance_complete: true
canonical_execution: separately_recorded
publication: separately_recorded
---

# Real local preparation followed by autonomous output

Status: proposed_retained

**Current mathematical scope:** conditional support. The source construction and
its selective reviews are root-qualified. Canonical reproduction, source
transport review and publication decisions belong to their separate actual
records; none is implied by this draft or the historical PASS strings.

Can the supplied complex emitter hopping be replaced by real positive local
terms without supplying a chiral input? For this exact device, two real clock
rails plus a five-unit controlled preparation give a conditional construction.
The initial ancillary state is one excited physical emitter and vacuum
elsewhere. Nine positive isolation blocks and five positive pulse terms on eight
existing sites prepare the useful rail sector. Every added control is real and
C1, starts at zero, and returns to zero at time five. Subsequent runtime is
fully autonomous. This reduces the complex static-coupling permission to an
explicit real preparation/control permission; it does not derive those controls
or the pure seed from physical axioms.

**Runner:** [real_control_autonomous_output_2026_10_17.py](../scripts/real_control_autonomous_output_2026_10_17.py).
The inherited runtime is the [thermal/resonance theorem](THERMAL_RESONANCE_HALT_BOUNDED_THEOREM_NOTE_2026-10-17.md)
on the intended parent PR9666 at `67108090f68ed9b2bc62eee23701b2d3d71dce4a`.
That source remains conditional, with its own exact-ladder dependencies and
retained-audit boundary. Its single-rail thermal preparation is not a thermal
supply theorem for the new doubled apparatus.

## Exact claim and complete comparison

Fix one actual `kappa in [1e-12,1e-8]`, sigma=1e-6,L=12 and the exact nominal
ladder coefficients in the preserved proofs. Define `c=cos(2k0)`, `s=sin(2k0)`,
`d=1+c+s`, `E0=2J(1-cos k0)`, with the inherited rational center. The old pair
and operation remain literal:

\[
 K=2I+Z_1Z_2,\qquad
 W=\frac{(9+12i)I+(-16+12i)X_1X_2}{25}.
\]

Let E_e0 insert the supplied product ancillary seed, U_setup be the complete
five-unit propagator, and H_R,M the positive real finite runtime Hamiltonian.
Choose the finite device before setup with `T=kappa^-2`, `M=ceil(50T)` clock
sites per rail. The theorem is the complete operator bound

\[
 \left\|e^{-itH_{R,M}}U_{\rm setup}E_{e0}
 -\zeta e^{-i(\Phi+c_Rt)}\mathcal B^R_{\kappa,t}
        e^{-i(t+5)K}W\right\|<0.00483202,
 \qquad T\le t\le2T,
\]

where

\[
 c_R=2\nu+2\kappa d,\quad c_{\rm seed}=E_0+c_R,\quad
 r=4J+3\kappa d,\quad \Phi=5c_{\rm seed}+4r+3\pi/4.
\]

The actual common outgoing profile uses the inherited `f_kappa rho_kappa`, with
its fixed common zeta and rail state `xi+=(e0-i e1)/sqrt(2)`. Both source qubits
and emitters are empty in the ideal outgoing state. The finite apparatus is
embedded in the same infinite comparison space used by the source theorem;
there is no new truncation/renormalization of its ideal waveform. All clock,
rail, emitter, source, old and arbitrary passive-reference outputs remain.
Only `[W,K]=0` rearranges the ideal comparator; the true interacting dynamics
need not commute with K. Runtime t begins after release and the old age is t+5.
The phase includes the actual doubled-device scalar c_R, not the single-rail
scalar, and E0 is not added again as an independent runtime phase.

The complete unhalved trace distance is below 0.00966404 for arbitrary old/
reference density matrices on that finite window. The infinite apparatus has
operator error below 0.00383202 for every t>=T. These are distinct statements:
a fixed finite device is not asserted to work for all future times. There is
no exact-W or arbitrary-accuracy limit, and no calibration/joint/noise box is
silently composed with this exact family.

## Mechanism, costs and the unchanged counterexample

The realifier uses the standard complex/conjugate direct-sum mechanism with
an explicit ordinary nearest-neighbor embedding for this sparse Hamiltonian.
It leaves the old qubits unencoded. Real positive hopping cells have full-qubit
spectrum 0,0,2|h|,2|h|; their vacancy/onsite constants are retained. The two
opposite cross signs are necessary. The useful chiral rail sector intertwines
with the given complex source, not with a fitted old-dependent replacement.

A physical e0 product seed alone places equal weight in two conserved sectors.
For that **unchanged runtime and unprepared seed**, the preserved original proof
exhibits a gate branch and an identity branch, and a common-output separation
above 0.53 for the infinite late-time problem and above 0.52 on its finite window.
Those bounds use **the original slower T=10^6/kappa²**, with its corresponding
M=ceil(50T). They are not failure bounds at the new resonance onset, nor a
universal no-go for real Hamiltonians or other preparations. The counterexample
and live alternative mechanisms are preserved in full rather than erased by the
new positive construction.

The successful setup changes that preparation explicitly. Eight positive edge
complements and one onsite pin isolate the three-position core e0,m,e1. Three
unit pulse windows of areas pi/4,pi/2,pi/2, between two unit ramps, produce xi+
with the displayed common phase. The exact full old/core identity and exit
Gram 2I give total supported ramp error at most sqrt(2)kappa. Leaked components
are propagated by the full subsequent unitaries; they are not assumed to stay
in the core and are not discarded. Real Hamiltonian coefficients do not force
their evolving states to remain real.

The device uses 2M+6 qubits and 2M+28 positive runtime blocks excluding K.
Setup adds fourteen term channels and no qubits or old/source controls. The
added old-site loads stay below two; the separate old edge has norm three.
Source-A/B loads are 27.936224853155858 and 22.228906875353305. The extra control
norm sum is below 9, supplied incident slew below 20, and modeled work magnitude
below 33. Full identity coefficients, positive block norm sums, seed-supported
phase and signed work have separate formulas in the proof. They do not account
for controller heat, fabrication or reset. At kappa=1e-8, T=1e16 Hamiltonian
units and the device has 10^18+6 qubits. These are sufficient bounds, not seconds,
optimal costs or practical performance.

## Dependencies, evidence and open permissions

| Obligation | Support and remaining condition |
|---|---|
| Real local cells, scalar, sectors and literal-old geometry | First preserved proof and its selective analytical review; exact supplied coefficients/edges |
| Core isolation, signed pulse product, exit Gram and two ramp estimates | Second preserved proof and separate analytical review; pure seed and exact real C1 controls supplied |
| Common full spectral profile, localized coordinates, point-spectrum allowance and finite horizon | Inherited nominal resonance theorem on the parent; no inherited scientific checker replay here |
| Complete composition, phase and old aging | Source operator/trace derivations and root qualification; no output discarded |
| Native preparation, thermal delivery for this doubled device, controller and practical costs | Open physical supply obligations, not additional framework axioms |

The [root qualification](../outputs/real_control_autonomous_output_2026_10_17_inputs/frozen_sources/real_control_root_review/QUALIFICATION.md.txt) and
[acceptance](../outputs/real_control_autonomous_output_2026_10_17_inputs/frozen_sources/real_control_root_review/ACCEPTANCE.json) retain the two separate reviews, their analytical
freeze chronology, full failures and exact evidence identities. Both reviewers
froze their new analytical bodies before seeing the respective new author
program/output. They had substantial inherited source/authorship exposure and
used the same selected model. This is selective checking, not blind review of
all dependencies or model diversity. The source bodies' historical pending
labels remain provenance and are superseded only by those separate decisions.

The portable primary mechanically transplants the two author corroboration
programs. Realifier arithmetic uses at most 6x6 matrices and a 46-vertex graph;
preparation uses at most 4x4 dense matrices, symbolic kappa and sparse M16/M17
fixtures with twelve old/core columns each. The original preparation attempt
failed before science on isolated-Python SymPy import; its repaired launch ran
the identical mathematical checker. Both attempts and all streams remain.
No huge-clock dynamics, Gibbs evolution, parameter grid, old spectral replay or
independent theorem review is performed by the primary.

The preparation check named `ramp_error_and_complete_trace_ceiling` contains a
historical first comparison of 2*kappa_max to itself plus slack. **That clause is
budget arithmetic, not an independent validation of the ramp theorem.** It is
transported unchanged and labeled in the report. The ramp support is the
separately frozen Gram/Duhamel derivation and the substantive Gram/profile
identities. Neither its historical passing flag nor a new canonical replay
increases that support or warrants an inflated independent-check count.

Pure product seed/vacuum delivery, selected real signed cells, exact pulse areas,
timing and the existing enormous clock remain supplied. Autonomous preparation,
thermal/cooling realization of this doubled device, native controller supply,
complete capture/reset/reuse and physical Hamiltonian/energy/Record identification
remain open. The realification architecture and its state-encoding issue are
prior art, credited in the first proof; no broad novelty or new literature
priority claim is added by this publication wrapper.

## Review record and reproduction boundary

The [source map](../outputs/real_control_autonomous_output_2026_10_17_inputs/SOURCE_MAP.json)
resolves every preserved historical label to repository bytes. The
[transport ledger](../outputs/real_control_autonomous_output_2026_10_17_inputs/TRANSPORT_EDIT_LEDGER.json)
accounts for every executable path/cap/report adaptation. The complete source
bodies follow below; any Markdown destination changes have a reversible ledger,
and raw originals remain exact. New stored historical text with trailing
whitespace uses lossless gzip, with stored/raw identities stated separately.

The [reproduction plan](../outputs/real_control_autonomous_output_2026_10_17_inputs/REPRODUCTION_PLAN.json)
and [preparation status](../outputs/real_control_autonomous_output_2026_10_17_inputs/PUBLICATION_STATUS.json)
are frozen drafting history. Later [transport decision](../.claude/science/physics-loops/toe-real-control-autonomous-output-20261017/ROOT_PORTABILITY_ACCEPTANCE.json)
and [execution status](../.claude/science/physics-loops/toe-real-control-autonomous-output-20261017/EXECUTION_STATUS.md)
remain outside calculation inputs, avoiding a self-referential cache. This draft
performs no scientific/mutation run and asserts no successful canonical cache.

The source/proposal boundary is conditional support with `proposed_retained`
referral; only the independent audit path may ratify status. Root still owns
portable-source review, actual bounded execution and discriminating faults,
cache binding, focused publication checks and later integrated-current-main
conformance. The original narrow counterexample is preserved with its explicit
N1-N8 scope limits; no general-no-go or broad five-route PASS is claimed. No
shared graph/manifest, axiom, prompt, audit record, Git branch or PR is changed
by this drafting assignment.


<!-- BEGIN PRESERVED SOURCE: real_coupling_halt_route/ROUTE.md -->

## Preserved source: Real local apparatus and unprepared-seed counterexample

---
claim_type: exploratory_worked_failure
actual_current_surface_status: unqualified-author-candidate
independent_review: pending
general_real_coupling_no_go: false
native_phase_permission_closed: false
physical_axiom_changes: none
---
# A local realification and its complete gate/bypass output

The standard realification of the installed emitter can be implemented here
using two clock rails, real coefficients, positive ordinary-nearest-neighbor
two-qubit terms, and the literal old qubits. An explicit cubic embedding and
the full scalar and load costs are given below. It does **not** solve the
product-seed halt target. Its allowed seed, one excited physical emitter and
otherwise blank auxiliary qubits, has equal weights in two conserved conjugate
sectors. At late times one sector performs the target gate and the other emits
the identity operation. Both outputs are retained.

Conditional on the qualified exact-ladder family premises listed in section 1,
this construction's complete output has operator distance **greater than 0.53**
from every old-independent ancillary waveform times the target gate, for every
`t >= T=10^6/kappa^2` on the infinite graph. For two rails of
`M=ceil(50T)` sites it has distance **greater than 0.52** throughout `[T,2T]`,
under the stated embedding into the infinite output space. These are failure
bounds for this particular construction and preparation, not a prohibition on
all real Hamiltonians, other seeds, or earlier transient times.

Realification is established prior art, not a new architecture. The concrete
result of this attempt is the physical two-body realization and the quantitative
complete-output falsifier for applying that architecture to this exact emitter.
This is author work with one bounded exact corroboration, awaiting a separate
decisive check. It requests no audit status or publication.

## 1. Exact dependencies, target and prior exposure

Keep the literal old pair and gate

    K = 2I + Z1 Z2,
    W = [(9+12i)I + (-16+12i)X1 X2]/25.

For P=X1X2, the two gate eigenvalues are

    omega_plus=(-7+24i)/25,  omega_minus=1.                 (1)

In particular W is not scalar. Both parity sectors have a real old eigenvector
with K energy one: `( |01> +/- |10> )/sqrt(2)`. They will be a falsifier that
does not conflate different old aging phases.

`SOURCE_MANIFEST.json` records sixteen byte-preserved inputs and read coverage.
The controlling source is `inputs/family.md`, SHA256
`9bcf538e7efb2285e1e9e8b67da8c3f29a308b0baa9004eec1dd4787393fa9ac`.
Its separate root acceptance is
`a48c7f35251ccca1eeda6c022de50a0e93c7f0889b44a4d75c46f0853bf3a325`,
and qualification is
`27a4008d6588fef9f0a5ac1d231d71240c12468db93d50a36ac2ee02f6ab7814`.
Historical provisional labels in that unchanged body are not edited. The
qualification permits conditional reuse; it is not retained audit.

The exact installed, generic, moment, interval and local-emitter arguments
are reused by their pinned snapshots. Their complete relevant arguments had
already been authored or checked by this agent during this campaign. The
complete family argument and qualification were read, and all mathematical
sections used here were refreshed. This is substantial source exposure by the
same model, not blind or model-diverse review. No old scientific checker was
replayed. The newer resonance-family packet under separate review is not a
premise. Calibration and joint static boxes are excluded.

The parent supplied repository baseline is PR9665 head
`0e3993770a7a2dd872018f9dd3c76c2d9a624db9`. Current local workflow and relevant
wrapper bytes were read and hashed; there was no Git or remote freshness
operation. The primitive registry and realized-state primitive were read.
No registered primitive is treated as a missing axiom, and no primitive is
credited with supplying the specific blank/chiral state or Hamiltonian.

For clarity, the exact inherited apparatus is reproduced. Write `n=(I-Z)/2`,
`a=|0><1|`, source vacuum `Omega=|00>_AB`, and `iota x=x tensor Omega`:

    C = DeltaA nA + DeltaB nB
        + hAB(nA+nB-aA^dagger aB-aB^dagger aA) + u nA nB,
    G = gA nA(I+X1)+gB nB(I+X2),  B=K+C+G,
    VA=lambdaA(I+XA)+mu0 I, VB=lambdaB(I+XB)-nu I,
    Hg=h0 tensor I+B+P0 tensor VA+P1 tensor VB,
    h0=2J I-J(S+S*), E(k)=2J(1-cos k),
    V=|L>-exp(i phi)|L+2>,
    Hplus=[[Hg,kappa V],[kappa V*,B+E0]].                  (2)

All decimals below are exact, as in the inherited family:

| Coefficient | Value | Coefficient | Value |
|---|---:|---|---:|
| J | 0.030021107107032 | gA | 0.996878563816670 |
| gB | 0.599319315560298 | hAB | 3.999349697888060 |
| lambdaA | 3.801781381581202 | lambdaB | 2.575033765788497 |
| DeltaA | 2.192035527016003 | DeltaB | 2.186826508897014 |
| u | 0.544607276405587 | mu0 | 0.321494607058201 |
| nu | 1.459892813020969 | q0 | 4.510351185997098 |

Set `k0=2 arctan(1/q0)`, `phi=2k0`, `E0=E(k0)`, `L=12`,
`sigma=10^-6` and `10^-12 <= kappa <= 10^-8`. In particular `B iota=iota K`
exactly, but K is not assumed to commute with the contact dynamics. The original
physical operator is `Hplus+(nu+2kappa)I`. Its real seed is `E x=|e> iota x`.

Here are the precise inherited estimates needed, with the same actual common
envelope f and absolute-site convention as the family:

    Gamma_t e_j=(1/sqrt(2pi)) integral_I f(k) Phi_j(k) e^(-itE(k)) dk,
    Phi_j(k,n)=[e^(-ikn)+R_j(k)e^(ikn)]u_j+C_j(k,n),
    exp(-itHplus)Gamma_0=Gamma_t exp(-it Db),
    Gamma_t*Gamma_t=I, ||E-Gamma_0||<0.003,
    ||f||2=1, f in H1_0(I), |R_j|=1,
    kappa^2 ||f'||2<1/100, |R_j'|<1000/kappa^2,
    ||localized packet||<3/[sqrt(2pi)kappa^2 v |t|],
    v=1/40<E', |E''|<=2J, 2J/v<5/2.                     (3)

The localized estimate includes both old energies in each parity, all seven
complementary emitter coordinates in that parity, the entire finite core and
all closed tails. It follows from the Hilbert-valued product bound in family
(49)-(50); its integration-by-parts proof works for both signs of t and after
entrywise conjugation. The seed bound includes any point spectrum and any
component outside the compared scattering range. No such component is removed.

For normalized `g in H1_0(I)`, the inherited position estimate gives the
unwanted half-line norm

    ||g'||2/(v t)+2J sigma/v,  t>0,                       (4)

for the incoming wave on `n>=0` and the outgoing wave on `n<0`. It is an
upper bound with a spread allowance, not a claim of a nonzero physical tail.
Exact packet normalization in (3) uses the separate decaying past-limit
argument, not this allowance. The forward family conclusion is

    ||exp(-itHplus)E
       - zeta beta_plus(t) tensor iota exp(-itK)W||<0.004,
    t>=T=10^6/kappa^2.                                  (5)

Here beta_plus is the actual normalized half-line Fourier wave of `f rho`,
and the fixed unit-modulus scalar `zeta=-exp(-4ik0)alpha` is inherited. Equation
(5) has removed only the known original physical scalar. No phase is fitted
separately to an old column.

## 2. Realification without encoding the old pair

All old/source matrices in (2) are real. Write `Hplus=A+iD`, where A is real
symmetric and D is real antisymmetric in the clock/emitter and real internal
basis. Only the two-contact hopping phase contributes to D. Double the
clock/emitter position label into rails q=0,1, while leaving the old/source
qubits literal. With the logical rail matrix

    Jf=[[0,-1],[1,0]],
    xi_plus=(|0>-i|1>)/sqrt(2),
    xi_minus=(|0>+i|1>)/sqrt(2),
    HRtilde=A tensor I + D tensor Jf,                    (6)

HRtilde is real symmetric and commutes with Jf. Its restrictions are Hplus
on xi_plus and `Hminus=conjugate(Hplus)` on xi_minus. The old Hilbert space
has not been real-encoded, conjugated or measured; (6) is a complex-linear
unitary block decomposition valid for arbitrary complex old/reference input.
The flag is a logical description of two physical head positions, not a free
physical qubit with unexplained controlled hoppings.

Put `c=cos(phi)>0`, `s=sin(phi)>0`, `d=1+c+s<3`. The hoppings, in row-clock,
column-emitter convention, are precisely

| Bond | Real hopping |
|---|---:|
| e0--c_(L,0), e1--c_(L,1) | +kappa |
| e0--c_(L+2,0), e1--c_(L+2,1) | -kappa c |
| e1--c_(L+2,0) | +kappa s |
| e0--c_(L+2,1) | -kappa s |

The two opposite cross signs matter. The exact six-dimensional check retains
the nonzero intertwining defect obtained by reversing the first cross sign.
Every bulk clock edge has hopping -J on its own rail. Source A is coupled
to both c_(0,q), source B to both c_(1,q), with their original coefficients.
The single old/source operator B is not duplicated.

## 3. Positive full-qubit terms, exact scalar and ordinary NN embedding

For every installed real hopping h between physical qubits u,v use

    Q_uv=|h|(n_u+n_v)+h(a_u^dagger a_v+a_v^dagger a_u).   (7)

Its full four-dimensional spectrum is `0,0,2|h|,2|h|`, so it is positive
with norm `2|h|`. In addition to the six cells above, use for each q

    (E0-kappa d)n_(e,q),
    kappa(I-n_(L,q)),
    kappa(c+s)(I-n_(L+2,q)).                            (8)

The exact rational center gives `E0>3*10^-8`, hence all emitter onsite
coefficients are positive throughout the declared interval. The sum of
(7)-(8) is the desired real emitter hopping plus the two emitter energies,
and **2 kappa d I**. This is an identity on the entire qubit space: occupation
coefficients cancel individually, not merely after setting head number to one.

On each rail use the ordinary positive clock bonds and `J n_(0,q)`;
use `lambdaA n_(0,q)(I+XA)+mu0 n_(0,q)` and
`lambdaB n_(1,q)(I+XB)+nu(I-n_(1,q))`. The two copies of the last vacancy
term give **2 nu I**, not nu I. Thus on the invariant one-head sector the
actual physical operator is exactly

    HRphysical=HRtilde+cR I,
    cR=2nu+2kappa(1+c+s).                               (9)

It differs from the original branch's physical scalar by
`nu+2kappa(c+s)`. Both the mean energy and the comparator phase retain (9).
All remaining C and G terms in (2) are positive two-qubit or onsite blocks
with real coefficients, and K is the unchanged positive old edge. The
full-qubit Hamiltonian conserves total clock/emitter head number. Equality
with (6) is claimed in its invariant one-head sector, not as an unrestricted
many-head realification. On the infinite graph the finite-number clock
restrictions are bounded selfadjoint positive operators; their orthogonal
direct sum, with the finitely many bounded contacts and internal terms,
defines the vacuum finite-excitation representation used here.

An explicit Z^3 embedding shows that no diagonal edges or three-body flag
controls were hidden. Put

    old1=(0,0,0), old2=(1,0,0), A=(0,1,0), B=(1,1,0),
    e0=(8,2,1), e1=(9,3,1).

Rail 0 has

    c0=(0,1,1), c1=(1,1,1), c2=(1,1,2), c3=(1,1,3),
    c_n=(n-2,1,3)                    for 4<=n<=10,
    c11=(8,1,2), c12=(8,1,1), c13=(9,1,1), c14=(9,2,1),
    c_n=(n-5,2,1)                    for n>=15.

Rail 1 has

    c_n=(n,1,-1)                     for 0<=n<=9,
    c10=(9,2,-1), c11=(9,3,-1), c12=(9,3,0),
    c13=(8,3,0), c14=(8,3,1),
    c_n=(8,n-11,1)                   for n>=15.           (10)

Every consecutive clock pair, each of the six emitter bonds, the old/source
square edges and all four clock/source contacts has Manhattan length one.
Coordinates are distinct. For the tails, rail 0 has x>=10,y=2,z=1, while
rail 1 has x=8,y>=4,z=1; neither intersects the core or the other tail.
Incidental nearest neighbors carry no extra interaction. A supplied device
may select which allowed edges are installed. This is not a derivation of
its fabrication or state supply from the framework axioms.

## 4. Product seed, resource costs and the forbidden shortcut

The allowed physical seed excites only e0. Every other clock/emitter qubit
and both source qubits are zero, in product with the arbitrary old/reference
state. In the logical rail description,

    |e,0> = (|e>xi_plus+|e>xi_minus)/sqrt(2).             (11)

Each conserved sector has weight one half. The same weights hold for any
normalized real rail vector at the emitter, since a real vector's expectation
of the antisymmetric Jf vanishes. This additional observation does not claim
that every such superposition is a physical product state.

Selecting only the successful sector would require the physical seed
`(|1_e0 0_e1>-i|0_e0 1_e1>)/sqrt(2)`. It is an entangled one-head state with
a prescribed relative complex phase, not the allowed one-qubit product seed.
If it were supplied, (6) would reduce exactly to the original branch; that
would move the open phase/preparation resource into the input. No autonomous
preparer for it is constructed here. Conservation of Jf prevents this HR
itself from changing (11)'s sector weights. This does not forbid another real
preparation Hamiltonian from doing so before an appropriate handoff; that is
a separate unproved architecture.

For a finite clock of M sites per rail, the device uses `2M+6` qubits: two
rails, two emitters, two old qubits and two source qubits. Its one-head
Hilbert dimension is `16(2M+2)`; the unrestricted qubit space has dimension
`2^(2M+6)`. Sector decomposition reuses both original 24-dimensional matching
blocks per parity; no new 48-dimensional numerical inverse is inferred from
the small corroboration below. Its positive-block incident norm sums are

| Site | Incident norm sum |
|---|---:|
| old1, added | 1.993757127633340 |
| old2, added | 1.198638631120596 |
| old edge, separate | 3 |
| A | 27.936224853155858 |
| B | 22.228906875353305 |
| either c0 | 8.015120691541701 |
| either c1 | 6.730044773026091 |
| ordinary clock | 4J=0.120084428428128 |
| either c12 | 4J+3kappa |
| either c14 | 4J+3kappa(c+s) |
| either emitter | E0+kappa d |
| finite far end | 3J |

In particular duplicating the source contacts increases A's load by
`2lambdaA=7.603562763162404` and B's by `2lambdaB=5.150067531576994`.
There is no all-site cap two. The full seed moment identities are

    ER* HRphysical ER=K+(E0+cR)I,
    ER* HRphysical^2 ER=[K+(E0+cR)I]^2+2kappa^2 I.        (12)

Indeed the three outgoing hoppings from e0 have squared sum
`kappa^2[1+c^2+s^2]=2kappa^2`, and `B iota=iota K`. Thus the modeled seed
variance is `Var(K)+2kappa^2`. These are not preparation, cooling or total
fabrication costs. Real coefficients, exact ladder values, clean blank
qubits and the excited product seed all remain supplied physical resources.
The fixed rational q0 gives exact rational c and s. No finite coefficient
precision or additional realifier calibration box is certified; the only
parameter interval here is the inherited kappa interval with the displayed
exact relations between its six hoppings.

## 5. The conjugate branch emits an identity output

Use a real Bell basis for the old input, so Db and the vacuum channel vectors
u_j are real. Because E and Db are real, conjugating the backwards version
of (3) gives, for every t,

    ||exp(-itHminus)E - conjugate(Gamma_-t) exp(-itDb)||
       = ||E-Gamma_0|| <0.003.                          (13)

This is an operator identity/bound, not an anti-linear operation performed
on an input. Entrywise conjugating the intertwining matrix produces a
complex-linear matrix from arbitrary old coefficients to the output. Passive
references remain arbitrary.

The open part of `conjugate(Gamma_-t)` in column j is

    (1/sqrt(2pi)) integral_I
      [conjugate(f)e^(ikn)
        +conjugate(f) conjugate(R_j)e^(-ikn)] e^(-itE) dk.
                                                               (14)

The first term is the same outgoing identity wave for every old column.
The second is an unwanted incoming wave. Unlike the forward output, no W
is present in the leading term. Define

    b_minus(t,n)=(1/sqrt(2pi)) integral_I conjugate(f)
                                   e^(ikn-itE) dk,
    beta_minus(t)=b_minus(t)/||b_minus(t)|| on n>=0.      (15)

Since `|R_j|=1`, the product weak derivative obeys

    ||(conjugate(f)conjugate(R_j))'||2
       <=||f'||2+sup|R_j'| <1001/kappa^2.               (16)

The incoming old-vacuum columns are orthogonal, so (4) and (16) use their
maximum, not an unjustified square sum reduction. For the complete localized
columns the within-parity square sum in (3) is retained. It applies equally
to the integrand `conjugate(f C_j)` at positive t. Finally the negative tail
of (15) is bounded with `||f'||2`; normalizing its retained half-line part
costs at most that tail bound. The zero endpoint trace is preserved under
conjugation and multiplication by R_j.

At `t>=T=10^6/kappa^2`, these four complete errors are bounded by

    seed:             0.003,
    incoming:         1001/(kappa^2 v t)+(5/2)sigma,
    normalization:    (1/100)/(kappa^2 v t)+(5/2)sigma,
    localized:        (3/2)/(kappa^2 v t),               (17)

where `sqrt(2pi)>2` and `2J/v<5/2` were used only for upward rounding.
The normalization tail is below one half, so beta_minus is defined. The
sum at T is exactly `215527/5000000=0.0431054<0.044`; time-dependent terms
decrease later. We have proved the new reverse-branch consequence

    ||exp(-itHminus)E
          -beta_minus(t) tensor iota exp(-itK)||<0.044.  (18)

This bound includes all complementary emitter/source coordinates, closed tails,
and seed point-spectrum error. It assumes neither decay law nor absence of
out-of-band point spectrum. It does not introduce a separate old-dependent
spectral fit. The physical scalar in the combined device will be (9).

## 6. A complete-output lower bound

Define normalized ancillary states, including source vacuum and empty emitters,

    a_t = zeta xi_plus beta_plus(t) tensor Omega,
    b_t = xi_minus beta_minus(t) tensor Omega.

They are orthogonal because their rail sectors are orthogonal, even though
their actual clock profiles need not agree. After taking out the common
physical scalar `exp(-it cR)` and literal old evolution `exp(-itK)`, the
device's output is within

    epsilon_R=sqrt[(0.004^2+0.044^2)/2]=sqrt(61)/250<0.032

of the isometry

    Vout x=(a_t tensor W x+b_t tensor x)/sqrt(2).         (19)

Orthogonality of the flag sectors justifies the squared combination of the
two branch errors; it does not discard either branch. For any proposed
common normalized ancillary vector eta_t, apply W* on the old output and
test the two real old vectors in (1). Their actual ancillary vectors in
(19) become

    eta_minus=(a_t+b_t)/sqrt(2),
    eta_plus=(a_t+conjugate(omega_plus)b_t)/sqrt(2).

Their separation is

    ||eta_plus-eta_minus||=|omega_plus-1|/sqrt(2)
                         =8/(5sqrt(2)).                (20)

The triangle inequality forces at least one of the two distances to eta_t
to be at least half of (20). It even holds for an unnormalized eta_t or an
eta_t outside the span of a_t,b_t. Consequently

    inf_(||eta||=1) ||exp(-itHRphysical) ER
      -exp(-it cR) eta tensor exp(-itK)W||
       >=4/(5sqrt(2))-epsilon_R >0.53,  t>=T.           (21)

For a rational check, `4/(5sqrt(2))>9/16` and `epsilon_R<8/250`, whose
difference is `1061/2000=0.5305`. The comparator in (21) allows **any**
common ancillary waveform, including emitter/source support; it is broader
than the requested empty-emitter, vacuum-source outgoing clock comparator.
A phase common to the old inputs is absorbed in eta. Separate per-old-input
phases are not permitted. No output is traced out, projected, measured,
postselected or stopped externally. Tensoring a passive reference does not
alter the operator bound. This is an isometry obstruction; it is not a claim
that every individual input has a large reduced-old-state error.

## 7. Finite clock, actual distance and horizon

The one-head spectrum of HRtilde is the union of those of Hplus and its
conjugate. Hence the inherited radius 19 about `2J+10.5` applies unchanged;
cR shifts only its center. Keep sites 0,...,M-1 on both rails and add
`J n_(M-1,q)` at each far end. This is the exact compression, not an absorber.
From e0, the first omitted sites c_(M,q) are both at head-graph distance

    dM=M-13.                                            (22)

Each rail has a direct e0--c14,q edge, and no edge reaches a larger clock
index. The two rails and onsite internal mixing cannot shorten (22).
Polynomials of degree below dM agree on the whole seed subspace. The known
Chebyshev coefficient estimate therefore gives

    ||embedded finite evolution-infinite evolution||
       <=4 exp[-dM+19t sinh(1)]/[1-exp(-1)].             (23)

At `M=ceil(50T)`, `Tobs=2T`, the buffer beyond exponent -9 is at least
`(22/5)T-22>0`; `sinh(1)<6/5` was retained. The remaining bound is

    (32/5)(3/8)^9=19683/20971520<0.001.                 (24)

Thus the embedded finite complete output remains at distance greater than
`0.5305-0.001=0.5295>0.52` from every common ancillary waveform times W
on `[T,2T]`. The same full scalar and old aging appear. At kappa=10^-8,
T=10^22 and M=5*10^23 per rail; at kappa=10^-12, T=10^30. These enormous
costs are a horizon for this worked failure, not a successful gate resource
estimate or an optimal time. No fixed finite device is analyzed for all
future times, and no resonance-scale improvement is assumed.

## 8. Other real routes and the exact remaining obligation

An initial real-contact shortcut explains why simply deleting the local loop
phase is not justified. For any finite set of real scalar contact weights v_n,
the two free-lead form factors are conjugates,

    g_+(k)=sum_n v_n exp(-ikn),
    g_-(k)=conjugate(g_+(k)),  |g_+|=|g_-|.             (25)

This loses the installed emitter's directional interference zero and does not
inherit its small-bypass proof. Equation (25) is not a proof that a redesigned
real emitter with gate feedback cannot work; it is the precise failure of that
particular free-lead substitution.

A second restricted compiler idea also has an exact boundary. If a finite
real symmetric Hamiltonian is split into P/Q coordinates and real energy E
is outside the eliminated Q spectrum, its Schur Hamiltonian is

    H_eff(E)=H_PP+H_PQ(E-H_QQ)^(-1)H_QP,                 (26)

which is real symmetric. Such a closed ancillary elimination cannot produce
a nonreal scalar loop hopping in the same physical basis. For an open
ancillary channel the retarded self-energy can be complex, but every new
output and its feedback must then be accounted for. Equation (26) does not
rule out encodings or real multiport gate architectures.

For a possible redesigned one-open-channel real emitter there is a useful
production-phase condition. If its real-energy matching problem is unique,
its unit-incoming column has `Phi=R conjugate(Phi)` by time reversal and
`|R|=1`. A real local seed therefore has overlap `y=R conjugate(y)`. The
outgoing spectral coefficient of that seed is proportional to y. If two old
columns have a common nonzero outgoing profile times omega_j, their reflection
ratio must satisfy

    R_j/R_l=(omega_j/omega_l)^2                         (27)

on that common profile's support, as well as common magnitudes and controlled
localized components. This elementary conditional identity is derived here;
no uniqueness or common-profile claim for a new apparatus is supplied. It
suggests a different target for a real reflection design instead of assuming
that the old W scattering certificate is sufficient for emission.

The following remain genuinely different live routes, not failed searches:

| Route | Required new result; present status |
|---|---|
| Real multiport transmission gate with a local product source | Realize the literal old two-qubit operation, retain reflected/rejected ports and all delay errors, and prove one common complete output. Not attempted here. |
| Real one-port emitter designed using (27) | Certify the required squared reflection ratio and common seed spectral magnitude with all closed coordinates. Not constructed here. |
| An autonomous real preparer feeding a single useful chiral sector | Break the conserved-Jf restriction during preparation and prove the full product-seed handoff, with local positive costs and no clock-age reset. Active preparation work is separate and was not inspected or appropriated. |
| An encoded real history/quantum-walk computer | Known real universal architectures exist, but an encoding, decoder, old-aging identity and unpostselected full halt bound for these literal qubits are missing. No impossibility asserted. |
| A different multi-excitation or conditional latch | Avoid this one-head conserved-sector decomposition and prove full seed and output control with two-body NN terms. Not attempted. |
| The existing real boundary-reflection apparatus | It already performs W with a supplied incoming packet and positive three-body boundary. Replacing both those permissions with the requested product-seed/two-body supply is the live bridge; it is not supplied by this failure result. |

The useful next discriminating question is whether a concrete real multiport
or real squared-reflection emitter can meet the complete common-profile
condition without the second branch in (19). It is not whether a real
Hamiltonian can ever generate a complex unitary: even elementary real
Hamiltonians can do that under time evolution.

## 9. Prior work and narrow negative-claim discipline

Primary-literature search and exact read scope are in
`literature/SEARCH_NOTES.md`. Cubitt, Montanaro and Piddock,
[Universal Quantum Hamiltonians, v4, sections 7.1-7.2](https://arxiv.org/pdf/1701.05182v4),
already give the complex/conjugate direct-sum realification and explain the
state-encoding issue for dynamics. Its general ancillary-flag representation
does not automatically preserve geometric locality. This packet gives the
explicit two-rail embedding for the present sparse imaginary edge and derives
its particular literal-old output failure. No general realification novelty
is claimed.

Childs, [Universal computation by quantum walk, v1](https://arxiv.org/pdf/0806.1972v1),
uses real adjacency and permits a single-vertex initial state, with filtering
and encoded wires. Its construction is an important counterweight to a broad
real-coupling impossibility claim. The inspected success/output protocol does
not by itself provide this literal-old, complete unpostselected comparator.
The existing reflection note is likewise a real target-gate mechanism, with
different explicit input and locality permissions. No theorem from either
source is silently imported as the requested two-body product-seed closure.

The no-go discipline was read and applied to this **scoped worked failure**:

1. **N1 alternatives:** the three actual analytical tests are (6)-(24),
   the real-contact substitution (25), and closed elimination (26). Six live
   families are listed above. They are not mislabeled as five completed
   failed attempts. The broad packet-PASS threshold of five ruled-out routes
   is not met, and no such PASS or general no-go is requested.
2. **N2 wall independence:** equal conjugate weights, the bypass branch and
   the common-output separation are one dependent mechanism, not three
   independent physical walls. The closed-elimination statement is narrower
   and is not counted as a prohibition on all real hardware.
3. **N3 hidden walls:** supplied exact coefficients, selected NN edges,
   positive blocks, high source loads, blank vacuum and infinite tails are
   explicit. The alleged cure by a chiral seed is identified as a changed
   resource. No primitive or axiom is used to supply it.
4. **N4 residual matching:** the bound is an operator-isometry error to the
   exact W, allowing arbitrary common full ancillary states, actual cR and
   full old age. It is not a zero-flux, reduced-state or one-column proxy.
5. **N5 accounting:** per_element: positive cells (7)-(8); per_site: the
   full load table; per_mode: both flags, both old energies, every complementary
   source/emitter coordinate; per_block: full-qubit positivity and invariant
   one-head equality distinguished; lattice_wide: two infinite rails or the
   declared `2M+6` finite horizon. These are written research accounting,
   not a claimed canonical no-go-runner or PR-conformance certificate.
6. **N6 partial closure:** ordinary NN realification is achieved. Product-seed
   gate closure fails for this apparatus. The omitted permission is not
   promoted to a new physical axiom or a demonstrated universal necessity.
7. **N7 steelman:** real transmission and real squared-reflection architectures
   could make all emitted branches carry the same W; a real preparer could
   also break the current conserved-sector structure. This proof does not
   exclude them. Known real quantum-walk computation prevents a blanket
   inference from time reversal to computational impossibility.
8. **N8 cross-cycle echo:** the pre-existing free-lead bypass warning is credited
   in (25); the new work is the installed full-output reverse-branch bound,
   physical realification resource accounting, and explicit finite horizon.
   The reflection/emitter scattering strategy itself is prior work.

## 10. Actual computation and remaining verification limits

`PLAN.md` preceded scientific work. The saved `RESOURCE_PLAN.json` added the
bounded exact corroboration before it ran: CPU soft/hard 20 seconds, external
wall 30 seconds, at most two attempts, matrix dimension at most six, graph
at most 64 vertices. One attempt ran. It exited zero in 0.083587125 seconds
of launcher wall time, with 0.033349 user and 0.011494 system CPU seconds;
macOS child peak RSS was 22,921,216 bytes. No OS memory cap is claimed.

`run01/PRELAUNCH.json` was serialized, flushed, fsynced, closed and its directory
fsynced before subprocess creation. It binds the executed copy, checker,
launcher, plans, exact scalar inputs, all sixteen source snapshots and seven
selected runtime files. All 31 byte/generation bindings and sixteen original
source/snapshot pairs matched afterward. This is a real prelaunch record,
not a post-run reconstruction. Runtime bindings are selected files, not an
assertion of a complete transitive binary dependency inventory.

The new exact-Fraction checker imports no inherited scientific implementation.
Its largest matrix is six by six and its finite geometry prefix has 46
vertices. It checks contact signs and flag intertwining, the literal target,
positive-cell identities and full number/scalar coefficients, NN supports,
seed moments, source loads, the reverse budget and error separation. Its
wrong-sign countercase is retained as a nonzero exact defect. Complete stdout,
empty stderr, executed source and receipt are preserved. No optimizer, grid,
quadrature or time evolution ran, and no scientific execution failed.

The small core matrices are evaluated exactly at kappa=10^-8. Extension of
their identities to every declared kappa is analytical linear homogeneity;
onsite positivity and resource ceilings use the displayed monotone inequalities.
The output field `scientific_parameter_samples: 0` means no parameter-sampling
study was run; it must not be read as symbolic-kappa execution. The geometry's
infinite extension and its general distance are proved in (10),(22), not by
checking one prefix alone. The program does not independently prove the
operator-domain, packet or inherited certificate arguments. This packet is
source-exposed author verification, not independent review.

A read-only lookup initially used a nonexistent `.claude/skills/.../DISCOVERY.md`
path; the correct `docs/ai_methodology/skills/...` span was then read. Large
aggregated reads and the broad repository search were sometimes truncated;
needed mathematical spans were recovered separately. The full search text is
saved, and no exhaustive result or complete reading of every lexical hit is
claimed. There are no hidden failed scientific streams or overwritten attempts.

The remaining decisive review is the new reverse-time packet implication,
its full operator constants, physical scalar/embedding and the common-output
lower bound. No current task claims to have independently checked itself or
to have closed native real phase permission. All writes are confined to this
packet directory. No source, worktree, Git, checkpoint, prompt, physical axiom,
audit record or other chat was changed; no subagent or model override was used.


<!-- END PRESERVED SOURCE: real_coupling_halt_route/ROUTE.md -->


<!-- BEGIN PRESERVED SOURCE: real_coupling_preparation_candidate/CANDIDATE.md -->

## Preserved source: Real local preparation and autonomous-output composition

---
title: Finite real preparation of the useful chiral rail sector
status: proposed conditional theorem; separate review required
source_realifier_status: pending separate review
execution_status: see separate EXECUTION.md and actual receipts
scope: exact supplied two-rail apparatus and classical preparation controls
---

# A physical product seed, real local pulses, and autonomous release

There is a concrete candidate route using only real, positive onsite and
ordinary nearest-neighbor two-qubit preparation blocks. It starts from one
excited physical emitter and all other auxiliary qubits blank. Nine local
isolation blocks and five pulse blocks, supported on eight already present
sites, prepare the useful chiral emitter sector and turn off in five units
of Hamiltonian time. The operator seed error is at most `sqrt(2) kappa`,
uniformly in the clock length. The old Hamiltonian remains literally
`K=2I+Z1 Z2` throughout, including both ramps and all three pulses.

The route is conditional on the supplied apparatus, exact initial product
seed and specified real classical control functions. Its transfer to the
halt theorem is also conditional on the pending realifier result. It does
not supply a native controller, thermal delivery, cooling, a phase reference
without cost, autonomous setup, reset or reuse. No postselection, subsystem
discard, old encoding or externally stopped runtime is used. No new complex
static coupling is introduced. Exact pulse areas are an explicit control
permission; they are not inferred from the framework axioms.

For the exact coupling family `10^-12 <= kappa <= 10^-8`, the qualified
resonance bound transfers to complete operator error below `0.00483202`
on the finite window `[T,2T]` after release, where `T=kappa^-2` and each
rail has `M=ceil(50T)` sites. The corresponding unhalved trace distance,
including arbitrary passive references, is below `0.00966404`. These are
conditional sufficient bounds, not measured performance or practical costs.
At the upper coupling endpoint the apparatus still has
`1,000,000,000,000,000,006` physical qubits.

## 1. Sources, exposure and precise inherited premises

The source manifest is [SOURCE_MAP.json](../outputs/real_control_autonomous_output_2026_10_17_inputs/frozen_sources/real_coupling_preparation_candidate/SOURCE_MAP.json). It records exact
copied bytes, original historical paths and capture metadata. Relevant pins:

| Source | SHA256 |
|---|---|
| Realifier ROUTE | c1cf729c2639d682a66df72b880c529dbabfc1768935ae62d170538973ce2018 |
| Realifier FREEZE | 16fa2cbf13386826cd6939cc412f66c9224a89eaadd133b2163c5b3130e5829b |
| Exact coupling-family body | 9bcf538e7efb2285e1e9e8b67da8c3f29a308b0baa9004eec1dd4787393fa9ac |
| Family root acceptance | a48c7f35251ccca1eeda6c022de50a0e93c7f0889b44a4d75c46f0853bf3a325 |
| Resonance-family body | 401e5c2389ef99bd9980898ec118f2476e49dd627d3cf9f32deb812ffc5498f0 |
| Resonance-family root acceptance | bb280c96d290e28b42c45994cab3fe9871d671b0d20d39a36ae09d211ef98686 |
| Exact rational ladder parameters | a98e272fa5d65e6177670ce2dfb52498ed942b8bd9996a0b9b16838d4e0c2251 |
| Earlier product thermal preparation | b7ef6e98b16bcffb609cbf8a9cca2aee03d4bb20ac6295e99c744f488ad14227 |
| Earlier product preparation qualification | 5e4cc2c916d9240ec5bb0b2a84559ae38fd2b20959e63c52d6b3c0bda04a2d69 |

The realifier body and its freeze were read before developing this pulse
route. The author previously authored or reviewed parts of the family,
source certificate, packet bridge and product preparation chain, with the
same model. This is source-exposed author work, not blind or model-diverse
review. The earlier product preparation supplies context for positive
complements and supported Duhamel estimates; its Gibbs construction is not
used here. No realifier checker/output or root's separate unshared pulse
idea was read. The forbidden `real_phase_preparation_idea` directory was
not accessed. The first recorded source exposure in this packet is
`2026-10-17T04:49:01.176316+00:00`.

The owner supplied baseline is PR9665 head
`0e3993770a7a2dd872018f9dd3c76c2d9a624db9`. No Git/remote freshness operation
was performed here. Current workflow and governing discovery/status/delivery
instructions were read at their recorded unchanged revisions. No editable
prompt, axiom, registry, shared checkpoint, repository or audit file changed.

Use the exact inherited constants, with every listed decimal exact:

| Constant | Value | Constant | Value |
|---|---:|---|---:|
| J | .030021107107032 | gA | .996878563816670 |
| gB | .599319315560298 | hAB | 3.999349697888060 |
| u | .544607276405587 | lambdaA | 3.801781381581202 |
| lambdaB | 2.575033765788497 | DeltaA | 2.192035527016003 |
| DeltaB | 2.186826508897014 | mu0 | .321494607058201 |
| nu | 1.459892813020969 | q0 | 4.510351185997098 |

Write `n=(I-Z)/2`, `a=|0><1|`, `Omega=|00>_AB`,
`iota x=x tensor Omega`, `k0=2 arctan(1/q0)`, `phi=2k0`,
`c=cos(phi)>0`, `s=sin(phi)>0`, `d=1+c+s<3`,
`E(k)=2J(1-cos k)`, `E0=E(k0)`, `L=12`, `sigma=10^-6`.
Here `E0>3*10^-8`, so `E0-kappa d` and `E0-kappa` are positive over
the whole closed coupling interval. The exact rational `c,s,E0` are
calculated from the pinned rational `cos(k0),sin(k0)`; no decimal fit is
used to establish a sign.

The literal old target and source are

    K=2I+Z1 Z2,
    W=[(9+12i)I+(-16+12i)X1 X2]/25,
    C=DeltaA nA+DeltaB nB
      +hAB(nA+nB-aA^dagger aB-aB^dagger aA)+u nA nB,
    G=gA nA(I+X1)+gB nB(I+X2), B=K+C+G.               (1)

Both `W*W=I` and `[W,K]=0`, and `B iota=iota K` exactly. Commutation of
K with the full interacting runtime is neither assumed nor true in general.

The inherited complex branch is

    Hg=h0 tensor I+B+P0 tensor VA+P1 tensor VB,
    h0=2J I-J(S+S*), VA=lambdaA(I+XA)+mu0 I,
    VB=lambdaB(I+XB)-nu I,
    V=|12>-exp(i phi)|14>,
    Hplus=[[Hg,kappa V],[kappa V*,B+E0]].              (2)

The finite version adds the positive far-end onsite needed to compress
`h0`. These are statements about the complete old/source/clock one-head
space; each old/source fiber has dimension 16.

## 2. The unchanged real apparatus and its geometry

For any real hopping h on an installed edge uv define

    Q_uv(h)=|h|(n_u+n_v)+h(a_u^dagger a_v+a_v^dagger a_u).
    spec Q={0,0,2|h|,2|h|}.                          (3)

Thus Q and `2|h| I_uv-Q` are real positive two-qubit matrices, each with
norm `2|h|`. Identity extension to all other qubits is implicit; none of
these identities is silently omitted from the physical Hamiltonian.

There are two clock rails `c_(n,q)`, `0<=n<M`, `q=0,1`, and physical
emitters e0,e1. Keep the original C,G,K once, without duplicating the old
pair or its source. Install on each rail all `Q(-J)` clock bonds, endpoints
`J n_(0,q)` and `J n_(M-1,q)`, and the positive contact terms

    lambdaA n_(0,q)(I+XA), mu0 n_(0,q),
    lambdaB n_(1,q)(I+XB), nu(I-n_(1,q)).              (4)

The six emitter hopping cells (3), in row-clock/column-emitter convention,
have coefficients

    e0--c12,0 : +kappa,      e1--c12,1 : +kappa,
    e0--c14,0 : -kappa c,    e1--c14,1 : -kappa c,
    e1--c14,0 : +kappa s,    e0--c14,1 : -kappa s.      (5)

Also retain, for q=0,1,

    (E0-kappa d)n_eq,
    kappa(I-n_(12,q)), kappa(c+s)(I-n_(14,q)).        (6)

The sum of (5)-(6) is exactly its six hopping operators plus
`E0(n_e0+n_e1)+2kappa d I` on the whole qubit space. The two vacancy
contacts in (4) contribute `2nu I`. On the invariant one-head sector the
physical runtime therefore satisfies

    HR=HRtilde+cR I, cR=2nu+2kappa d,
    HRtilde=A tensor I_rail+D tensor Jf,
    Hplus=A+iD, Jf=[[0,-1],[1,0]].                    (7)

The physical chiral state

    xi+=(|0>-i|1>)/sqrt(2), Jf xi+=i xi+              (8)

reduces HR exactly to `Hplus+cR I`, for either infinite or compressed
finite rails. This invariant-sector identity is the realifier dependency
being reused conditionally. Its negative conclusion for the unprepared
physical seed does not apply once the sector is prepared by active controls.

All controls below use existing edges. Put `m=c_(14,0)`. The eight touched
sites have coordinates

    e0=(8,2,1), e1=(9,3,1), m=(9,2,1),
    c12,0=(8,1,1), c12,1=(9,3,0), c14,1=(8,3,1),
    c13,0=(9,1,1), c15,0=(10,2,1).                   (9)

Both e0--m and m--e1 are ordinary NN edges. Every edge in (5), plus
m--c13,0 and m--c15,0, has Manhattan distance one. The full two-rail
embedding, source contacts and old/source square are the exact coordinates
in the realifier section 3. In particular old1=(0,0,0), old2=(1,0,0),
A=(0,1,0), B=(1,1,0). There are no new qubits, diagonal edges, crossings
interpreted as interactions, or three-body terms. Require M>=16 so c15,0
is present. All proposed horizon sizes satisfy this.

## 3. Nine local positive blocks isolate a three-position core

Let F be the eight installed edges consisting of all six edges (5) and the
two clock bonds incident to m. On each such edge h is its actual signed
runtime hopping. Add the time-controlled positive operator

    R=sum_(uv in F) [2|h_uv| I_uv-Q_uv(h_uv)]
                        +(E0-kappa)n_m.             (10)

There are eight two-qubit complements and one positive onsite pin. They
are real and use neither an old nor a source site. R is a full-space
operator, not a subtraction made only after restricting a sector.

Let E_a map an arbitrary literal old vector into old tensor source vacuum
and the single head at a. The three-position core is the range of
`E_S=(E_e0,E_m,E_e1)`. Put

    cseed=E0+cR,
    r=4J+3kappa d,
    Ciso=cseed+r=E0+2nu+4J+5kappa d.                 (11)

Then the exact supported intertwining is

    (HR+R) E_S = E_S [K tensor I_3+Ciso I].          (12)

Proof: the six emitter hoppings and both clock hoppings leaving m cancel
as full operators. The sum of their complement constants is
`Sb=4J+4kappa d`. In the one-head representation before adding those
constants, the emitter diagonal E0 loses kappa d. The m diagonal 2J loses
`2J+kappa(c+s)` and gains `E0-kappa`, also giving `E0-kappa d`.
Every core diagonal is therefore `cR+Sb+E0-kappa d=Ciso`. Source terms
vanish on Omega and no core head is at a source contact. Only literal K
acts on the old vector. This proves invariance as well as equality of the
three scalars, for every M>=16. The far endpoint at c15,0 when M=16 has
no effect because its head amplitude is zero in this core.

For either physical emitter the stronger supported identities are

    HR E_eq = E_eq(K+cseed I)+kappa Vq,
    R E_eq = r E_eq-kappa Vq,                       (13)
    V0=E_c12,0-c E_m-s E_c14,1,
    V1=E_c12,1+s E_m-c E_c14,1,
    (V0,V1)*(V0,V1)=2I_old tensor I_rail.            (14)

The cross term is `-cs+sc=0`, and each diagonal is `1+c^2+s^2=2`.
Thus V is a scaled isometry with Gram `2I`, not a unit isometry. For
every normalized rail vector z, `||Vz||=sqrt(2)`, simultaneously for
all old inputs and passive references. This is what makes the ramp error
independent of M. A bound using the extensive full-space norm of HR is
unnecessary and would miss this useful local property.

Omitting the pin in (10) fails: the m diagonal differs from either emitter
diagonal by `-(E0-kappa)`. This is a real obstruction to the simpler
eight-complement pulse calculation, not a no-go for other controls.

## 4. An explicit five-unit, finite-slew real schedule

All added controls are zero at the initial time and after time 5. The
installed HR remains literal at every time. Let

    q(x)=30x^2(1-x)^2, 0<=x<=1,
    u_up(x)=3x^2-2x^3, u_down(x)=1-u_up(x).          (15)

The pulse profile has integral 1, maximum 15/8, zero values and first
derivatives at both endpoints, and `max|q'|=10sqrt(3)/3`.
The ramps have integral 1/2 and maximum derivative magnitude 3/2.
Extension by the adjacent constant values makes all control coefficients
continuously differentiable. No ideal instantaneous quench is used.

During `[0,1]` use `H=HR+u_up(t)R`.
During `[1,4]` keep R fully on and apply the following three disjoint
unit-window pulses, with x the local time in that window:

| Window | Positive blocks added | Weight |
|---|---|---|
| [1,2] | `n_e0+n_m+hop(e0,m)` and `n_e1` | `w1=(pi/4)q(x)` on both |
| [2,3] | `n_m+n_e1-hop(m,e1)` and `n_e0` | `w2=(pi/2)q(x)` on both |
| [3,4] | `n_e1` | `w3=(pi/2)q(x)` |

Here `hop=a_u^dagger a_v+a_v^dagger a_u`. Each pair block is Q(+1)
or Q(-1); all weights are nonnegative real. The spectator onsite in the
first two windows is necessary for the common core phase below. During
`[4,5]` remove R using `H=HR+u_down(t-4)R`, with no pulse present.
After time 5 every new control and its first derivative is exactly zero;
only HR governs the subsequent evolution.

In core basis `(e0,m,e1)`, the three pulse generators are

    P1=I_3+X_(e0,m), P2=I_3-X_(m,e1), P3=|e1><e1|. (16)

The off-pair spectator entries of X are zero. On the exact invariant core
(12), the old factor and Ciso commute with these head operations. The
explicit pulse product gives

    exp[-i(pi/2)P3] exp[-i(pi/2)P2] exp[-i(pi/4)P1]|e0>
       =exp(-3pi i/4)(|e0>-i|e1>)/sqrt(2).          (17)

Indeed the first exchange creates `(e0-i m)/sqrt(2)` with common phase
`exp(-i pi/4)`. The negative second exchange sends m to `+i e1`, with
common phase `exp(-i pi/2)`, producing `(e0+e1)/sqrt(2)`. The final
positive onsite pulse multiplies e1 by `-i`. Reversing the sign of the
second exchange instead selects the orthogonal chirality; the sign is
load-bearing. No pulse generator is complex, although its real-time
unitary need not preserve real vectors.

## 5. Supported ramps, exact old aging and the complete seed bound

For any fixed normalized rail vector z and ramp u(t), the comparison
isometry

    A_z(t)=exp{-i integral_0^t[cseed+r u(v)]dv}
                            E_z exp(-itK)           (18)

has initial value E_z. Equations (13)-(14) imply the exact residual

    [H(t)A_z(t)-i dA_z(t)/dt]
       =kappa[1-u(t)] exp{-i integral[cseed+r u]}
                                      V_z exp(-itK).

Variation of constants and unitarity, without a bound on ||HR||, give

    ||U_u(t)E_z-A_z(t)||
       <=sqrt(2) kappa integral_0^t |1-u(v)|dv.       (19)

This is an operator norm statement on all old columns. It remains true
after tensoring any reference identity. For both unit ramps the integral
is 1/2, so each ramp costs `kappa/sqrt(2)`. The first actual ramp's
error is propagated through the later exact unitaries; the pulse calculation
is used only for the ideal comparison state. No claim that the leaked
part stays in the three-position core is needed.

Let Usetup be the actual full five-unit propagator. Let

    Echi=(E_e0-i E_e1)/sqrt(2),
    Phi=5cseed+4r+3pi/4.                             (20)

The ramps contribute `2cseed+r`, the three flat-core windows contribute
`3Ciso`, and the pulse common phase is `3pi/4`. Combining (17)-(19),

    ||Usetup E_e0-exp(-iPhi)Echi exp(-i5K)||
                         <=sqrt(2)kappa.             (21)

Every old energy has the same scalar Phi. The old aging is exactly five
units of K on the ideal branch, not a preparation-time reset or an
unproved commutation through the true dynamics. The error includes any
old/source entanglement and any clock/emitter leakage produced during
the ramps. No trace over those systems occurs.

If exact pulse areas or ramps are perturbed, a finite control tolerance
can be stated without redoing scattering: for actual added control
`A(t)+DeltaA(t)`, Duhamel adds `integral_0^5 ||DeltaA(t)||dt` to (21).
For errors supported on these finitely many blocks this bound remains
independent of M. Positivity/reality and slew must still be separately
maintained by an admissible perturbation; arbitrary perturbations are not
asserted to preserve the hardware class. No such tolerance is silently
included in the numerical error quoted above.

## 6. Transfer into the unchanged autonomous runtime

The new preparation theorem needs only this inherited runtime implication:
for the exact complex seed E and some complete common output isometry B_t,

    ||exp(-itHplus,M)E-zeta B_t exp(-itK)W||<epsilon_M(t). (22)

All embeddings into the common infinite comparison space are understood
as in the family/resonance statements. In particular the finite output
is compared with the same normalized infinite-half-line packet, not a
new finite truncation or renormalization.

The qualified resonance family provides (22) with
`epsilon_infinite(t)<.003832` for every `t>=T=kappa^-2` and
`epsilon_M(t)<.004832` on `[T,2T]` for `M=ceil(50T)`.
Its comparator uses the one actual normalized function

    b_t(n)=(1/sqrt(2pi)) integral_I
                     f_kappa(k)rho_kappa(k)exp[ikn-iE(k)t]dk,
    beta_kappa,t=b_t/||b_t||_(n>=0),
    zeta=-exp(-4ik0)alpha, |alpha|=1.                (23)

Here alpha is the exact inherited site-one reflection witness in channel
`s=-1,p=-1`; it is not rounded or fitted anew. One f_kappa rho_kappa is
shared by all four old columns, whose total scattering energies differ
with the old energies 1 and 3. The inherited spectral-mass, old-energy
channel, closed-tail, bound-state, derivative, normalization and finite
distance arguments are reused by their pinned identities and scope.
The nonzero central target residual `<1.76*10^-13` remains charged in
their reflection budget. This packet does not rerun or independently
reprove those scattering certificates.

Map B_t into the physical two-rail apparatus with fixed rail factor xi+,
empty e0/e1 and source vacuum, calling the result `B_t^R`. This map is an
isometry and retains every rail, emitter and source qubit. Equation (7)
transfers (22) with the extra phase `exp(-icR t)`. Compose it with (21)
and use `[W,K]=0` only on the ideal comparator to obtain

    ||exp(-itHR,M)Usetup E_e0
       -zeta exp[-i(Phi+cR t)] B_t^R exp[-i(t+5)K]W||
                  < epsilon_M(t)+sqrt(2)kappa.        (24)

This gives `<.00483202` for the stated finite window and `<.00383202`
for the infinite apparatus at all t>=T. The preparation and runtime
limits are conditional on (7) and the inherited exact-ladder runtime
premises. The parent realifier was frozen before the newer resonance
acceptance, so using the latter is an explicit new interface composition,
not a claim that the older realifier already contained its improved onset.
Alternatively its original family bound `<.004` infinite and `<.005`
finite transfers by exactly the same algebra, at its larger onset
`10^6/kappa^2` and clock size `ceil(50*10^6/kappa^2)`.

For any density matrix of the old pair and an arbitrary passive reference,
two isometries at operator distance eta induce unhalved trace distance
at most 2eta: expand `U rho U*-V rho V*` into two terms and use
`||AXB||_1<=||A||||X||_1||B||`. Tensoring a reference leaves the
operator distance unchanged. Thus the complete finite bound is
`<.00966404`. It includes the rail coherence as an output, even though
that coherence is independent of the old input in the ideal branch.

The delivered seed is an exact pure product across the old/reference
system and all ancillary sites, with only e0 occupied. An exact pure
auxiliary marginal would force the same factorization for any extension.
No finite-temperature claim is made. An independently supplied initial
state within unhalved trace distance delta of this product would simply
add delta by unitary invariance; deriving such delta from a Gibbs device
or a correlated delivery model is a separate obligation. It is not
provided by the preparation schedule here.

Total elapsed physical time is `5+t`. Relabeling t as time since release
does not reset the old pair or clock. No finite clock is asserted to work
forever; after release no control is used to stop or catch its evolution.
The static/coupling/calibration boxes outside this exact family are excluded.
No arbitrary-accuracy or exact-W limit follows from these fixed bounds.

## 7. Counts, incident loads and finite slew

For M sites per rail, the unchanged apparatus contains `2M+6` qubits,
one-head dimension `16(2M+2)`, and full dimension `2^(2M+6)`.
No such exponentially sized matrix is used in the argument or corroboration.
There are `2M+28` positive runtime blocks excluding K: `2M+12`
two-qubit blocks and 16 onsite blocks. Preparation adds 14 channels:
the nine in (10), two pair pulses, two spectator onsite pulses and one
onsite phase pulse. Counting separate time profiles separately gives
`2M+42` blocks excluding K; some onsite hardware can be shared but no
such economy is assumed. They use eight existing sites and eight existing
edges, and only e0--m--e1 participates in nontrivial pulse transfer.

The sum of the nine isolation block norms is

    Aiso=4J+4kappa d+E0-kappa <1/7.                  (25)

Its incident additions are `2kappa d` at either emitter;
`4J+2kappa(c+s)+E0-kappa` at m; `2kappa(c+s)` at c14,1;
`2kappa` at either c12; and `2J` at c13,0 and c15,0.
No old/source/boundary contact is altered. Each of those norms is an
actual full positive block norm; a scalar subtraction is never used to
discount an incident load.

The following are peak incident sums during the whole setup. Separate
pulse windows are maximized, not incorrectly added as if simultaneous:

| Site | Peak sum, excluding K at the old sites |
|---|---|
| old1 | 1.993757127633340 |
| old2 | 1.198638631120596 |
| A | 27.936224853155858 |
| B | 22.228906875353305 |
| either c0 | 8.015120691541701 |
| either c1 | 6.730044773026091 |
| m=c14,0 | `8J+E0+5kappa(c+s)-kappa+15pi/8` |
| e0 | `E0+3kappa d+15pi/16` |
| e1 | `E0+3kappa d+15pi/8` |
| c14,1 | `4J+5kappa(c+s)` |
| either c12 | `4J+5kappa` |
| c13,0 | `6J` |
| c15,0 | `6J`, or `5J` if M=16 |
| other interior clock site | `4J` |
| an untouched finite far end | `3J` |

The old edge has separate norm 3 and is unchanged. The original added
old-site cap two therefore holds through preparation as well as runtime;
there is no claim of a cap two at source/contact sites. The largest
source load remains below 28. The peak total norm sum of just the added
controls is bounded by `Aiso+45pi/16<9`.

For a site, define the control slew load as the sum of `||dA_b/dt||`
over incident added blocks b. During either ramp it is at most
`(3/2)Aiso<3/14`. During the pulses its largest value is
`10pi sqrt(3)/3<20`, from either of the active pair sites in the second
window. The onsite spectator has a smaller value. Thus a supplied
incident slew allowance 20 suffices, with finite strengths specified above.
The bound is independent of M and kappa in the stated interval.

At kappa=10^-8, T=10^16 and M=5*10^17, so the onset from initial
delivery is `5+10^16`, the compared window ends at `5+2*10^16`, and
the device has `10^18+6` qubits. These are Hamiltonian units, not seconds.
The five-unit setup reduces a static phase permission; it does not remove
the enormous existing runtime resource requirement.

## 8. Identity coefficients, energy and classical work

Full-space identity coefficients and supported scalar energies differ.
For the full Pauli expansion on the finite device, including K, the
coefficient of the global identity in HR is exactly

    alpha_R=2+(DeltaA+DeltaB+gA+gB)/2+hAB+u/4
              +2JM+lambdaA+lambdaB+mu0+nu+E0+2kappa d. (26)

Its positive block norm sum excluding K is

    S_M=DeltaA+DeltaB+2hAB+u+2(gA+gB)+4JM
            +4(lambdaA+lambdaB)+2mu0+2nu+2E0+4kappa d. (27)

These extensive quantities are not replaced by the much smaller seed
energy. For R the full-space identity coefficient is

    alpha_iso=2J+2kappa d+(E0-kappa)/2.               (28)

Pulse windows one and two add identity coefficient `3w_j/2`; window
three adds `w3/2`. Since R is ramped with total area four, the exact
integrated full-space identity coefficient during setup is

    5alpha_R+4alpha_iso+11pi/8.                      (29)

By contrast, the actual supported phase outside old K in (21) is Phi,
because nonidentity operators have nonzero action on the seed/core. The
identity part `2I` of old K remains inside `exp(-i5K)`; it is not omitted
or counted again in Phi. Equation (24) likewise keeps `cR t` and the
old aging separately. Equations (26)-(29) explicitly retain all positive
complement and vacancy constants even when an involved head site is empty.

For an arbitrary old/reference input, the initial physical mean runtime
energy is `Tr(K rho_old)+cseed`. For the ideal flat-core state during
pulses the mean base energy is `Tr(K rho_old)+Ciso`; pulse contributions
must additionally be included while their weights are nonzero. Those
ideal statements are not substituted for the actual ramped state's work.

Let A(t) be the entire added control and rho(t) the actual unitary state.
In a finite apparatus, its classical work, with the same Hamiltonian
energy units, obeys the exact identity

    Wsetup=integral_0^5 Tr[rho(t) dA(t)/dt]dt
          =Tr[HR rho(5)]-Tr[HR rho(0)],              (30)

because A(0)=A(5)=0. The onset ramp has nonnegative work at most Aiso;
the final ramp has nonpositive work of magnitude at most Aiso. Each
ideal isolated pulse has zero net work, but the actual leaked component
need not, so no zero actual pulse work is claimed. Independently of that
component and of M,

    |Wsetup| <= integral_0^5 ||dA/dt||dt
       <=2Aiso+6 max(w1)+6 max(w2)+2 max(w3)
        =2Aiso+165pi/16 <33.                        (31)

The pair-plus-spectator pulse has full-space norm at most 3w, yielding
the factors six for a smooth rise and fall. The bound uses actual full
block norms, not a one-head projection. It does not calculate the
controller's fabrication, heat, phase reference or reset cost. Those
remain supplied classical-control resources outside this conditional
unitary device model. Every modeled qubit and passive reference remains
in the complete output.

## 9. What is new, what is tested, and what remains conditional

The new load-bearing claims are the nine-block core identity (12),
supported Gram identity (14), explicit positive pulse product (17),
two length-independent ramp estimates (19)-(21), complete interface
composition (24), and finite resources/scalars/work (25)-(31).
The ordinary real positive cells and the exact two-rail decomposition
come from the pending realifier, with the new local algebra independently
reconstructed here. The spectral and finite-horizon claims retain the
qualified exact-ladder family/resonance premises. Neither another PASS
line nor this source-exposed author's calculation makes the whole chain
independent or retained.

The bounded checker is independently written for this route. It uses
exact rational/symbolic kappa algebra, at most 4x4 dense matrices, and
sparse Pauli action on twelve core basis columns for each M=16 and 17.
It checks the full local positive cells, pulse signs and scalar phase,
runtime/isolation identity coefficients, norm counts and incident loads,
and exact supported seed/core actions. It also checks that omitting the
pin destroys the flat core and that reversing the second exchange selects
the wrong chirality. These are corroborating discriminators, not an
optimizer, grid proof, huge-clock dynamics or inherited checker replay.
The all-M proof is the symbolic edge/diagonal cancellation in section 3,
and the all-time error proof is the operator Duhamel estimate, not the two
finite fixtures. Actual execution and any failures are recorded separately
in [EXECUTION.md](../outputs/real_control_autonomous_output_2026_10_17_inputs/frozen_sources/real_coupling_preparation_candidate/EXECUTION.md.txt), with genuine prelaunch source/runtime
bindings and complete streams; see [RESOURCE_PLAN.json](../outputs/real_control_autonomous_output_2026_10_17_inputs/frozen_sources/real_coupling_preparation_candidate/RESOURCE_PLAN.json).

Before claiming this as a checked conditional theorem, separate review
should verify the supported scalar cancellation, signs and spectator phases,
all-M release error, literal old aging, complete output and realifier-to-
resonance interface. If those checks pass, the reduction obtained is from
complex installed hopping to real installed hopping plus finite supplied
real preparation controls. The missing native preparation/controller
supplier, exact pure seed delivery and enormous finite apparatus remain
explicit permissions. There is no claim of an autonomous real preparer,
thermal supply theorem, no-go for other real devices, arbitrary-accuracy
closure or physical identification of the framework.


<!-- END PRESERVED SOURCE: real_coupling_preparation_candidate/CANDIDATE.md -->
