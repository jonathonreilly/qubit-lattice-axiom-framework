# Fock excitation bookkeeping, modular boundary, and local deviation current — Cycle 229

**Date:** 2026-07-17

**Type:** bounded_theorem

**Status:** exact finite conditional construction and bounded discriminator;
audit unset

**Authority:** none

**Constitutional effect:** none

**Packaging:** draft parking branch and draft PR #5389 only

Companion runner:

```text
scripts/fock_modular_boundary_current_cycle229_2026_07_17.py
```

This note and runner change no foundation, axiom, Qualification, primitive,
registry, policy, audit, or queue surface.

## Result up front

Cycle 229 executes the finite spectral-kinematic core of the strongest
Cycle-228 particle-hole alternative rather than assuming that the whole route
works. For each sampled generic six-mode momentum block of the supplied
proper-cubic family, the runner constructs an **eigenmode-diagonal finite CAR
representation and free Fock lift**, supplies a blockwise negative-phase
occupation, and applies the **particle-hole** reinterpretation. Every
occupation relative to that supplied blockwise sea has the nonnegative
additive unwrapped coordinate

```text
E_exc = sum_j |theta_j| q_j >= 0,
```

and its relative one-step phase is exactly `exp(i E_exc)`. The construction
retains the supplied scalar rest calibration and composes spectrally over two
sampled momentum blocks. This is an exact finite spectral-bookkeeping partial
closure of the Cycle-228 sign and carrier-multiplicity workstreams. It is not a
full finite-torus sea, a spatially constructed many-body QCA, an interacting
Fock law, or an onsite-qubit compiler for three-dimensional fermions.

It is not yet physical energy. The sea depends on the chosen quasienergy zero.
A phase that is projective in one fixed particle-number sector becomes
`exp(i delta N)` on full Fock space; it is observable only if cross-number
coherence or another number reference is admitted. Under number
superselection, the original phase freedom remains. Positive excitation
energy is not yet physical energy.

The current proper-cubic family has the same **quasienergy-circle seam
kinematics** as the discrete-time **modular boundary** identified by Gupta and
Short. Around its Cycle-228 numerically located transverse `U=-1` root, the
tested shrinking-offset sequence supplies a filled mode moving toward
`theta=-pi` and an empty mode moving toward `theta=+pi`; their unwrapped
branch-coordinate difference moves toward `2pi` while their relative one-step
phase moves toward `1`. Conditional on an exact `U=-1` crossing, that limiting
seam identity is algebraic. This is the conjugate-orientation modular alias
described below. The runner does not promote the numerical root to an exact
fixture theorem, identify a physical energy sign, reproduce
Gupta and Short's downhill direction, establish Dirac particle/antiparticle
spinors, or derive pair creation, an interaction matrix element, a decay rate,
or instability. At one sampled momentum block, selected mode pairs restricted
to `|theta|<pi/2` do not wrap; that is a kinematic sample, not an invariant
sector or a derived spectral gap.

A separate exact gain is the **local deviation continuity** equation. For the
chosen-reference Cycle-228 vector `chi=(I-exp(-i alpha)U)Psi`, coin output flux
obeys a nearest-neighbor discrete divergence law. That is a local conserved
norm current for the reference-relative deviation coordinate, not a local
current for `E_exc` and not stress-energy.

The outcome is therefore:

- particle-hole/Fock structure can close finite positivity and unwrapped
  additivity after a sea and branch are supplied;
- it does not select the sea, phase zero, number reference, or interaction;
- the named complete fixture has a directly executed finite-precision
  modular-zone witness;
- the local deviation current survives, while a local positive Fock-energy
  current remains open.

The fixture-specific outputs are the sampled six-band occupation ledger, the
change of sea rank and ledger under a supplied phase-reference shift, the
`U=-1` seam with a paired `U=+1` control, the exact `U=+/-1` endpoint branch
ambiguity, 64-state finite-Fock covariance for three sampled blocks over all 24
proper-cubic frames, and the separate one-particle deviation-norm continuity
identity. None is an explicit
modular-edge interaction calculation. A genuinely stronger result would
require a declared local proper-cubic interaction and a nonzero transition
matrix element or rate, a symmetry theorem forcing it to vanish, or a derived
local spectral pull-back that avoids the seam.

Physical energy remains unselected. No axiom conclusion follows.

## Exact finite construction

Write the supplied one-particle block as

```text
U = V diag(exp(i theta_j)) V^dagger,
```

and let the eigenmode operators `a_j` satisfy

```text
{a_i,a_j^dagger}=delta_ij,
{a_i,a_j}=0.
```

The finite free-Fock update is

```text
Gamma(U)|n_1...n_6>
  = exp(i sum_j theta_j n_j)|n_1...n_6>.
```

**Phase convention.** Here `U|j>=exp(i theta_j)|j>` and the supplied blockwise
sea fills `theta_j<0`. Gupta and Short instead write
`U|j>=exp(-i E_j delta t)|j>` and fill `E_j<0`, so their filled branch
corresponds to `theta_j>0`. Cycle 229 therefore executes the same
quasienergy-circle seam identity in the conjugate orientation; it does not
reproduce their filled-energy assignment, energetic direction, or
internal-spinor coupling argument. Applying the same construction to
`U^dagger` sends `theta -> -theta` and gives their negative-energy orientation
with the same `|theta|` ledger and `+/-pi` alias.

Choose the sea occupation `n_j^sea=1` for `theta_j<0` and zero otherwise, with
`E_sea=sum_{theta_j<0} theta_j`. For positive modes define the particle
annihilator `p_j=a_j`; for negative modes define the hole annihilator
`h_j=a_j^dagger`. Both annihilate the supplied sea. Their excitation creators
gain phase `exp(i|theta_j|)`. Equivalently, take `q_j=n_j` on positive modes
and `q_j=1-n_j` on negative modes. Then

```text
Gamma(U)_n / Gamma(U)_sea
  = exp(i sum_j |theta_j| q_j).
```

The reference-relative generator is therefore

```text
H_exc = sum_{theta_j>0} theta_j a_j^dagger a_j
      + sum_{theta_j<0} (-theta_j) a_j a_j^dagger >= 0,
U_rel = exp(-i E_sea) Gamma(U) = exp(i H_exc).
```

The runner exhausts all 64 occupations at three generic complex family points
and all 4096 occupations of two combined momentum blocks. For a fixed branch
and sea, the zero is unique whenever no `theta=0` mode occurs. At `theta=pi`,
each explicit `+pi/-pi` and filling convention still has its own unique zero,
but `U` does not select among those conventions. The runner also checks the
particle/hole CAR, sea annihilation, excitation phase law, occupation
conservation, and exact free-sea eigenstate property.

At generic momentum with `beta=0`, this fixture instead has two exact `U=+1`
modes and two exact `U=-1` modes. The zero modes give `2^2=4` zero-coordinate
states. Assigning both endpoint phases `+pi` or both `-pi` produces the same
free Fock phases and the same multiset of nonnegative coordinates, but different
sea occupations and complementary endpoint ledgers. Thus the free update does
not select the endpoint sea convention.

For the fixed free `Gamma(U)`, every mode occupation is conserved and the
supplied sea is an exact eigenstate. It is therefore exactly stable in this
free model. The `U=-1` alias removes only a possible kinematic protection
against a subsequently supplied interaction; interacting stability, a
transition amplitude, and decay remain open.

For a general six-mode matrix `A`, the runner also constructs the full exterior
lift

```text
Gamma(A)_{I,J}=det A[I,J]  when |I|=|J|,
Gamma(A)_{I,J}=0           otherwise,
```

and verifies the 64-state covariance identity over all 24 proper-cubic frames.
The displayed Jordan-Wigner matrices remain a finite spectral-mode proof
device. They establish an abstract number-preserving fermionic lift of the
finite one-particle blocks; they are not an explicit spatially local onsite-
qubit QCA compiler or finite onsite-qubit realization in three dimensions.
The live free spatial-CAR candidate `Gamma(S)Gamma(C)` is not executed here;
the full finite-torus sea/projector, an onsite-qubit encoding with locality, and
an interacting local Fock law remain open constructions rather than inferred
obstructions.

## Number-sector phase condition

For a one-particle update, `U` and `exp(i delta)U` define the same projective
channel. Their Fock lifts obey

```text
Gamma(exp(i delta)U) = exp(i delta N) Gamma(U).
```

Within a fixed-`N` sector the difference is again one global phase. Across
different number sectors it is not. Thus the Fock lift does not automatically
solve the phase-reference residual: it converts it into a question about
number superselection, vacuum coherence, and physical reference systems. The
runner also shows that shifting the reference can change which modes are
filled and changes the positive excitation ledger.

Before any mode crosses the chosen zero or branch seam, the runner verifies the
stronger exact response

```text
H_exc(delta) = H_exc + delta (N-N_sea),
U_rel(delta) = exp(i delta (N-N_sea)) U_rel.
```

This `delta` denotes the Fock rephasing `U -> exp(i delta)U`. It is the negative
of the Cycle-228 deviation-current reference convention
`U_alpha=exp(-i alpha)U`; the two signs must not be conflated.

At a crossing, the principal-branch sea prescription changes occupation and
this same-sector identity no longer supplies a continuation rule.

## The executed modular-zone boundary

At the Cycle-228 numerically located `beta=-0.3` diagonal `U=-1` root, the
center eigenvalue residual is below `10^-12` and three offsets
`10^-2,10^-3,10^-4` give phases consistent with the conditional limit

```text
theta_- -> -pi,
theta_+ -> +pi,
E_pair = theta_+ - theta_- -> 2pi,
Arg exp(i E_pair) -> 0.
```

At the nearby numerically located `U=+1` root, the tested unwrapped and wrapped
costs both move toward zero normally. This paired finite-precision control
isolates the seam behavior from an ordinary positive/negative crossing. It does
not certify either fixture root symbolically.

Gupta and Short, “The Dirac Vacuum in Discrete Spacetime,” *Quantum* 9, 1845
(2025), <https://doi.org/10.22331/q-2025-09-03-1845>, construct the free
1+1-dimensional fermionic QCA/Fock setting, derive perturbative conservation of
quasienergy modulo `2pi/delta t`, identify the second filled/empty boundary at
`E=+/-pi/delta t`, and argue that an interaction-mediated edge-pair channel can
be energetically downhill. They analyze the analogous boundary in a
3+1-dimensional Dirac-walk extension. They do not calculate a matrix element or
decay rate for a specified interaction, so the paper establishes a potential
instability channel, not vacuum decay. Their amended-walk theorem removes
energy-releasing pair creation kinematically in its stated mass range under the
modular criterion; it
does not prove full interacting-vacuum stability, and the amendment introduces
doubling. Cycle 229 instantiates only the convention-qualified seam-wrapping
identity on this repository's proper-cubic fixture. Global novelty has not been
established.

The free CAR/Fock lift and particle-hole reinterpretation are also prior
machinery, not Cycle-229 novelty. Direct precedents include Bisio, D'Ariano, and
Tosini, *Annals of Physics* 354, 244–264 (2015),
<https://doi.org/10.1016/j.aop.2014.12.016>, for a one-dimensional linear
free-field QCA; Mlodinow and Brun, *Physical Review A* 102, 042211 (2020),
<https://doi.org/10.1103/PhysRevA.102.042211>, for a local one-dimensional
qubit/Fock construction and sea proposal; and Mlodinow and Brun, *Physical
Review A* 103, 052203 (2021),
<https://doi.org/10.1103/PhysRevA.103.052203>, for a free three-dimensional
antisymmetric multiparticle construction, with interactions left open.
Explicit interacting gauge-QCA constructions also exist in 1+1 dimensions
(Arrighi, Bény, and Farrelly, 2020,
<https://doi.org/10.1007/s11128-019-2555-4>) and 3+1 dimensions (Eon et al.,
2023, <https://doi.org/10.22331/q-2023-11-08-1179>), but they neither select
this fixture's sea nor compute its modular-edge transition. Brun and Mlodinow,
*Entropy* 27, 492 (2025), <https://doi.org/10.3390/e27050492>, calculate
nonzero local-interaction coupling and finite-range suppression for a different
one-dimensional negative-energy/locality mechanism; that is not the
Gupta–Short modular-edge calculation.

## Exact local deviation continuity

Let

```text
chi_t = (I-exp(-i alpha)U) Psi_t,
a_t(x,d) = [C chi_t(x)]_d,
F_d(x,t) = |a_t(x,d)|^2,
rho(x,t) = sum_d |chi_t(x,d)|^2.
```

Because the coin is onsite unitary and stream `d` moves one edge `D_d`,

```text
rho(x,t+1)-rho(x,t)
  = sum_d [F_d(x-D_d,t)-F_d(x,t)].
```

The runner verifies this on generic complex states at `beta=0`, `beta=-0.3`,
and a nonzero phase reference. It is a local conserved norm current for a
derived deviation vector. It does not establish that `rho` is normalized as a
probability state, that `rho` is energy, that `F_d` is an energy flux, or that
either sources gravity.

## Cross-lane effect

### O — operational quantum

The eigenmode CAR/Fock construction supplies explicit occupation alternatives
and exact nonnegative reference-relative excitation bookkeeping. It does not
supply a spatial local many-body compiler, preparation, record instrument,
occurrence law, physical archive redundancy, or Born frequency.

### T — time

The number-sector identity states precisely when one-step global phase can
become relational. No clock or permitted cross-number reference is derived.
The modular alias shows that the one-step eigenphase alone cannot recover
unwrapped phase winding or a physical energy lift.

### I — matter

One selected particle excitation retains the supplied rest calibration, and
finite reference-relative excitation coordinates add across momentum blocks.
The construction is free and one-particle-derived; binding energy, interacting
Fock dynamics, species generation, and the mass spectrum remain open.

### G — gravity

There is now an exact local current for reference-relative deviation and a
nonnegative spectral Fock ledger. They are not the same object. Phase zero,
source reciprocity, momentum/stress, active field backreaction, and nonlinear
geometry remain missing.

### B — boundary/history

An explicit history or clock could carry phase winding across the modular
boundary, but none is built. A restricted central quasienergy sector or an
amended local law could also avoid the alias. Boundary selection remains open.

## No-go discipline gate

No claim that Fock lifting fails generally, that the current law is unstable,
or that new axiom content is required is shipped. Only the finite construction
and named-fixture modular alias are retained.

**N1–N8 status:** **PASS for the narrow bounded claim.** The broad no-go fails
because amended-law, interaction-suppression, winding-history, spatial-compiler,
and alternative-source routes remain live; that stronger claim is not shipped.

### N1 — alternative routes

The claim under attack is only: *for the declared phase convention, an exact
`U=-1` branch crossing has the algebraic modular seam identity; on the named
`beta=-0.3` fixture, the Cycle-228 numerically located root has a sub-`10^-12`
center residual and the tested `10^-2,10^-3,10^-4` sequence converges toward
that conditional identity.* Six distinct attacks were executed:

| attack route | honesty marker | disposition and evidence |
|---|---|---|
| numerical-root or finite-offset overclaim | **ATTEMPTED** | the center residual and three offsets are measured in `modular_boundary_controls`; they support convergence but do not constitute a symbolic root proof, so the fixture claim remains numerical |
| every positive/negative crossing behaves this way | **ATTEMPTED** | the paired `U=+1` crossing has ordinary small wrapped and unwrapped differences |
| the sea/branch is uniquely fixed by the free update | **ATTEMPTED** | the exact `beta=0` `+pi/-pi` endpoint conventions have identical free Fock phases but different seas in `branch_endpoint_controls` |
| phase-reference choice is physically irrelevant on Fock space | **ATTEMPTED** | the `delta=0.4` shift changes sea rank and the ledger, while the small no-crossing shift obeys the exact `N-N_sea` law |
| the result is a direction-basis presentation artifact | **ATTEMPTED** | the complete 64-state finite Fock blocks satisfy covariance over all 24 proper-cubic frames in `covariance_and_complex_controls` |
| wrapping is unavoidable for all selected pairs | **ATTEMPTED** | selected `|theta|<pi/2` mode pairs at one momentum block do not wrap; no invariant restricted sector is inferred |

The first two attacks leave the algebraic conditional identity and the scoped
numerical fixture witness standing; they do not upgrade the root to an exact
fixture theorem. The next four force its reference-, branch-, frame-, and
sample-resolution qualifiers. An
amended or gapped law, a winding history, a spatial many-body compiler, a
specified interaction form factor, and a different local energy/source current
remain unexecuted here and therefore defeat every broader no-go.

### N2 — wall-independence

Cycle 229 does not count every failed interpretation as a new physics atom. The
new residuals collapse to six workstreams, none promoted to an axiom wall:

- `C_ref`: select or derive the physical phase zero, cut, and sea;
- `C_num`: determine whether a cross-number reference is physical or number
  superselection is exact;
- `C_wrap`: store winding or derive an invariant sector/amended law that avoids
  the seam;
- `C_int`: specify a local interaction and determine its seam matrix element or
  suppression theorem;
- `C_local`: construct the spatial many-body CAR/QCA realization; and
- `C_source`: identify a local positive energy, momentum/stress, and reciprocal
  source response.

The complete directional audit is:

| pair | left closes right? | right closes left? | independent? |
|---|---|---|---|
| `C_ref`, `C_num` | no: a sea does not provide cross-number coherence | no: superselection does not select a sea | yes |
| `C_ref`, `C_wrap` | no: a chosen cut still wraps | no: winding storage need not select the physical zero | yes |
| `C_ref`, `C_int` | no: a sea does not choose an interaction | no: an interaction need not choose the sea | yes |
| `C_ref`, `C_local` | no | no: a compiler does not select phase zero | yes |
| `C_ref`, `C_source` | no | no: a `K`-type source could retain phase freedom | yes |
| `C_num`, `C_wrap` | no | no | yes |
| `C_num`, `C_int` | no | no | yes |
| `C_num`, `C_local` | no | no | yes |
| `C_num`, `C_source` | no | no | yes |
| `C_wrap`, `C_int` | no: avoiding a seam does not specify dynamics | no: an interaction does not store winding | yes |
| `C_wrap`, `C_local` | no | no | yes |
| `C_wrap`, `C_source` | no | no | yes |
| `C_int`, `C_local` | no: an abstract Fock interaction is not an onsite compiler | no: a compiler need not interact | yes |
| `C_int`, `C_source` | no: an interaction does not identify stress/source | no: a source map need not give the interaction | yes |
| `C_local`, `C_source` | no | no: a current does not compile fermions spatially | yes |

These workstreams are alternatives and interfaces, not a claim that all six
must become axioms. Cycle 229 partially addresses Cycle-228 `R_sign` and the
carrier-multiplicity slice of `R_comp`; it leaves `R_phase`, modular winding,
selection, and stress/source content open.

### N3 — hidden-wall scan

The load-bearing supplied inputs are explicit: one-particle `U`, eigenmode
decomposition, phase representative and branch, blockwise sea occupation,
finite sampled momentum blocks, free CAR/Fock kinematics, and the conditional
comparison of number sectors. No spatial Fock locality, interacting law,
vacuum selection, preparation, occurrence, probability, clock, physical energy,
or source map is smuggled in.

The trigger-phrase scan classifies “rather than assuming that the whole route
works” as non-load-bearing rhetoric, “supplied” as an explicit condition, and
the cited prior-work descriptions as attribution. No occurrence of “by
construction,” “as is standard,” “the framework provides,” “naturally,”
“obviously,” “standard QFT,” or an appeal to a registered/canonical object is
used to discharge a scientific step. “Energetically downhill” appears only in
the convention-qualified Gupta–Short attribution; it is not inferred for this
fixture. “Canonical anticommutation relations” is the tested algebra's name,
not an authority or registry appeal.

### N4 — residual matching

Only exact residual matches are used as predecessor support:

| cited witness | predecessor residual | Cycle-229 residual or closure | match? | use |
|---|---|---|---|---|
| `docs/work_history/repo/review_feedback/LOCAL_GENERATOR_SOURCE_TOURNAMENT_CYCLE228_NOTE_2026-07-17.md:124` | positive-frequency/Fock lift left live | finite spectral particle-hole ledger executed | yes | partial closure only |
| same file `:602` | `R_phase`: projective channel does not select phase reference | sea rank and ledger remain reference-dependent | yes | inherited open residual |
| same file `:607` | `R_comp`: carrier multiplicity | exact ledger over two sampled momentum blocks | yes | finite spectral slice closed |
| same file `:607` | `R_comp`: winding | `U=-1` branch difference wraps modulo `2pi` | yes | named-fixture residual remains |
| `docs/work_history/repo/review_feedback/ARCHIVE_CARRIER_SOURCE_LEDGER_CYCLE227_NOTE_2026-07-17.md:168` | genuine multiparticle additivity needs a Fock/direct-sum construction | free finite two-block Fock additivity | yes | partial closure, not spatial/interacting composition |
| same file `:185` | clock/rate must calibrate quasienergy to physical energy | no physical energy interpretation selected | yes | prevents an energy rename |
| same file `:197` | universal gravity needs a local stress-energy-like source | deviation-norm current is not the Fock ledger or source | yes | source residual retained |
| `docs/work_history/repo/review_feedback/COMMON_MATTER_FIELD_COIN_FAMILY_CYCLE219_NOTE_2026-07-16.md:124` | vacuum-relative rest reading is supplied fixture content | no predecessor wall is claimed closed | no | context only; dropped as a witness |

External mechanisms are attribution boundaries, not repo no-go witnesses:

| source | mechanism | match? | use |
|---|---|---|---|
| Gupta and Short 2025 | modular Dirac-sea boundary in discrete time | yes | known seam mechanism instantiated in the named fixture's conjugate orientation; fixture-specific execution, not independent global novelty |
| Brun and Mlodinow 2025 | finite-range suppression of a different local negative-energy production channel | no | steelman against instability drift, not evidence for this seam transition |

### N5 — resolution

| resolution | actually tested | not established |
|---|---|---|
| per mode | eigenmode CAR, particle/hole phase law, exact `0/pi` endpoint census | selected physical sea or energy sign |
| per six-mode block | all 64 occupations at three generic points | full finite-torus sea or interacting block |
| two sampled blocks | all 4096 additive reference-relative coordinates | infinite-volume domains or interacting composition |
| selected seam pair | sub-`10^-12` numerical root residuals and three shrinking offsets at `U=+/-1` | symbolic fixture root, transition amplitude, decay, or stability |
| selected central pairs | one momentum block avoids one-pair wrapping | invariant window, protected sector, or gap |
| proper-cubic frames | full 64-state finite-Fock covariance for sampled blocks | spatial fermionic locality, boosts, or Lorentz closure |
| one-particle packet | exact local deviation-norm continuity | local positive Fock-energy/stress current |
| lattice-wide many body | not tested | spatial CAR compiler and interacting QCA |
| records and clocks | not tested | formation, occurrence, frequency, winding carrier |

Accordingly, “not physical energy” means only “not selected as physical energy
by this finite construction.” It is not a universal statement that no physical
energy lift exists. Likewise, “not a local Fock-energy current” is restricted to
the separately tested one-particle deviation current; no lattice-wide negative
current theorem is claimed.

### N6 — primitive and reframe

Calling `E_exc` energy would hide the supplied sea and reference. Treating the
modular alias as an instability would add an interaction claim. Treating full
Fock number phase as observable would add cross-number coherence.

The required registry check was run against
`docs/audit/data/axiom_premise_nodes.json` and the three approved primitive
source notes:

| approved primitive | exact grant | relevance here |
|---|---|---|
| `docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md` | units conversion only | cannot choose a dimensionless phase cut, sea, or interaction |
| `docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md` | structural kinetic-form isotropy `c_t=c_s` only | cannot supply dynamics, phase, selector, vacuum, or energy map |
| `docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md` | pointwise evaluation at a supplied law-admissible realized state | cannot select the state, sea, measure, weighting, or state-contingent value |

These primitives remain approved premise nodes and are not counted as walls.
None is used to supply the missing interpretation. The honest partial-closure
path is: state the phase/sea as a named condition, prove the bounded theorem,
then try to retire that condition through a local history, spectral amendment,
or interaction theorem. Renaming `E_exc` a reference-relative excitation
coordinate is a terminology correction, not new physics. A fixed-number
superselection rule, amended QCA, or selected vacuum would still require its
own derivation or explicit conditional statement. No new-axiom claim is made.

### N7 — steelman

The strongest hostile alternative is a locally generated gapped or amended QCA
whose selected vacuum and particle-hole split avoid the modular seam, or whose
autonomous history stores winding. Gupta and Short construct a spectral
amendment that removes energy-releasing pair creation in its stated mass range
under their modular
criterion, while leaving explicit interacting amplitudes and full vacuum
stability open and introducing doubling. Even if a seam remains, Brun and
Mlodinow show in a different one-dimensional mechanism that finite-range local
interaction form factors can exponentially suppress negative-energy production.
A symmetry-forced zero matrix element could do more. These routes block every
inference from the present alias to physical instability.

A second hostile route couples gravity to local `K`, an action-derived current,
or another conserved operator with nonlinear emergent energy calibration,
bypassing a local `|Arg U|` Hamiltonian. Cycle 229 does not test or eliminate
that route either.

### N8 — cross-cycle echo

The repository scan found the following structurally similar earlier
expectations and retirement mechanisms:

| predecessor expectation or wall | retired? | mechanism | applicability here |
|---|---|---|---|
| Cycle 204 nonlinear clock map may align rest and inertia | no | route remains conditional | could provide a physical phase/energy lift |
| Cycle 219 global scalar phase freedom | no | no physical reference selected | inherited directly as `C_ref` |
| Cycle 227 genuine multiparticle additivity requires Fock/direct-sum structure | partial | exact free two-block exterior lift | closes finite spectral multiplicity only |
| Cycle 227 quasienergy-to-energy calibration is open | no | none | excitation coordinate is not renamed energy |
| Cycle 228 positive-frequency/Fock route may repair sign | partial | supplied sea plus particle/hole reinterpretation | finite generic blocks only |
| Cycle 228 carrier multiplicity and winding are bundled in `R_comp` | partial | Fock occupations carry multiplicity; `U=-1` exposes lost winding | winding/history remains open |
| Cycle 228 direct local current route | partial | deviation norm has exact continuity | not a positive Fock-energy/stress current |
| expectation that a filled sea automatically removes phase wrapping | yes, for the named numerical fixture witness only | numerically located `U=-1` root with shrinking-offset and `U=+1` controls | does not apply to amended laws, derived invariant sectors, or a symbolic fixture theorem |

No earlier convention-only retirement supplies the missing physical sea,
interaction, spatial compiler, or source. The mechanisms that could still
retire those residuals—history winding, a spectral amendment, symmetry or
finite-range suppression, and an action/current construction—remain explicit
next routes rather than axiom content.

## Falsification and next discriminators

This cycle does not yet give the supplied common law an empirical killer, but
it identifies concrete theory-level falsifiers. A derived symmetry-allowed
local proper-cubic interaction with an unsuppressed seam matrix element, loss
of the intended source ledger, or an actual vacuum transition would falsify a
claim that the present free completion is physically stable. Conversely, a
derived symmetry zero, spectral gap/amendment, or finite-range suppression
would protect it. Failure of every live spatial-CAR or local onsite-qubit
realization would challenge compatibility with the Qubit foundation; a local
compiler would remove that concern. These are future probes, not present
findings.

## Scope boundary

This is not a selected vacuum, Hamiltonian, interacting QFT, stress-energy
tensor, gravity theory, record-formation law, Born derivation, or empirical
prediction. The common family, phase representative, CAR/Fock lift, sea, and
spectral branch remain supplied. It is also not a proof of fermionic-algebra
locality for the lifted spatial update or a finite onsite-qubit realization in
three dimensions. The only spatial locality result executed here is the
separate one-particle deviation-norm continuity equation. No axiom conclusion
follows.

## Verification

```text
python3 scripts/fock_modular_boundary_current_cycle229_2026_07_17.py
```

Predecessor coexistence is checked separately before parking.
