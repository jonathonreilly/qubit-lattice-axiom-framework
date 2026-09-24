---
claim_id: homogeneous_field_star_penalty_for_mobile_records_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Conditional mathematics of the explicitly supplied finite model and stated ordered limits; historical numerical tables are author observations, with fresh controls separately identified below."
upstream_dependencies:
  - minimal_axioms
  - hardcore_record_motion_generates_gauge_rings_bounded_theorem_note_2026-09-24
  - uniform_record_density_with_live_formation_bounded_theorem_note_2026-09-24
runner: scripts/homogeneous_field_star_penalty_for_mobile_records_2026_09_24.py
---

**Type:** bounded_theorem
**Status:** conditional mathematical construction; unaudited.

The complete source argument below is preserved from the frozen submission. Its dated author-status statements and historical execution tables describe that submission, not an independent audit verdict. Quantum laws, enlarged site/link memories, Hamiltonians, instruments, backgrounds and preparations are supplied mathematical model assumptions. They are not new repository axioms or framework primitives. Fresh execution of the canonical runner checks the stated finite controls; finite tests alone do not establish the general proofs or limits.

# A homogeneous field-star penalty for mobile records

Date: 2026-09-22. Status: conditional construction and mean-density theorem,
with exact finite controls; independent reconstruction pending. This removes
one explicitly alternating Hamiltonian coefficient from the preceding model.
It does not derive the enlarged field/matter space, the quantum law, or the
selected external Gauss-charge sector from the minimal axioms.

## 1. The same local Hamiltonian at every vertex

Use the same finite periodic d-dimensional cubic lattice, spin-half link
fields E, hard-core record states 0,+,-, and gauge-preserving nearest-neighbor
hopping T as in `HARDCORE_RECORD_MOTION_GENERATES_GAUGE_RINGS_BOUNDED_THEOREM_NOTE_2026-09-24.md`. The side
lengths are even and at least six when only elementary plaquettes are counted
as four-cycles. Replace the explicit sublattice penalty by

    H_star = Delta R + t T,
    R = (1/2) sum_x (div_x E)^2,             Delta>0.       (1)

Every vertex has the same field-star term. The local terms overlap but
commute, because they are functions of the electric fields. Equation (1) is
translation invariant and covariant under the proper cubic rotations when
the oriented fields transform with their orientations. It is also invariant
under simultaneous field and record charge conjugation. The chosen state
and sector need not share those symmetries.

The homogeneous conserved generators are g_x=div_x E-q_x. Select the sector

    g_x=-n_x^0,           n_x^0=1_A(x),                    (2)

and prepare one plus record at every A vertex, none at B, and an ice field.
Equivalently, (2) is the old zero-Gauss constraint with a static alternating
compensating background. Writing that background as sector eigenvalues does
not remove its physical premise cost. In particular the zero sector g_x=0
on a torus would force total record charge zero, whereas this construction
has total charge V/2. No spontaneous selection of (2) is established here.

For the closed initial number sector N=N0=V/2, all records remain plus and

    R = N_B = H_A,

where H_A counts empty A sites. Thus (1) restricted to that entire sector is
exactly the preceding Delta N_B+tT Hamiltonian, not merely its perturbative
approximation. Its closed fourth-order ring coefficient and scalar shift
therefore carry over unchanged:

    H_eff = scalar - J sum_p (W_p+W_p^dagger)
                    + O_V(t^6/Delta^5),
    J=2t^4/Delta^3.                                      (3)

The same finite-volume dressing and first-birth estimates apply: the earlier
proof only used the fixed-number closed reference evolution and allowed any
number-preserving Hamiltonian extension after a birth. Its global trace-norm
bound remains volume dependent. No large-volume field convergence is inferred
from this exact sector identification.

The field-star term is additional local interaction structure, involving all
2d links at a vertex. It is not an on-site term in the original possibility
qubit algebra. The scales Delta and t remain supplied and unbounded along
the fixed-J scaling below.

## 2. Exact bookkeeping with continuing formation

Keep the uniform pair-formation rate beta>0 on every vacant edge and the same
spin-half, gauge-preserving pair maps. Both coherent signs and charge-resolved
refinements are allowed here; all have loss

    Gamma=beta sum_e P_(vacant endpoints).

Let M count minus records, equivalently the number of pair births since the
specified initial state. Total charge is N0, so N=N0+2M. Let N_(A,-) count
minus records on A and K=H_A+N_B. The Gauss constraint gives the exact
diagonal identities, throughout every reachable number sector,

    R = K/2+2 N_(A,-) = H_A+M+2 N_(A,-),
    R>=M,       R>=K/2,       H_A<=K/2.                  (4)

At a vacant A-B edge, an A-plus/B-minus birth leaves R unchanged; an
A-minus/B-plus birth increases R by two. Coherent superposition of the two
maps gives the same adjoint action on R: the two charge images are orthogonal.
There is a useful sharper bound from Gauss itself. An empty A vertex has
div E=-1. Among its 2d outward fields, exactly d-1 are positive and d+1 are
negative. Only a positive outward field permits the energy-raising A-minus
birth. Some of its neighboring B sites may be occupied. Therefore

    0 <= D_birth^dag(R) <= 2 beta(d-1) H_A
                         <= 2 beta(d-1) R.              (5)

This uses periodic bulk degree 2d and the sector (2); it is not a statement
about arbitrary boundary charges. For d=1 the energy-raising branch vanishes.
The total intensity also satisfies Gamma<=2d beta H_A<=2d beta R.

## 3. A bound uniform in the number of sites

Write b_e for the sum of the allowed A-to-B single-record hops on edge e,
so T=-sum_e(b_e+b_e^dagger). The exact local adjoint identity from the
preceding density calculation is still valid:

    D_birth^dag(b_e)=-(beta/2)c_e b_e,                   (6)

where c_e counts vacant other endpoints of edges sharing one endpoint with
e; 0<=c_e<=4d-2 and c_e commutes with b_e. The same-edge contribution is zero,
the disjoint contribution cancels, and each shared endpoint contributes its
other vacancy projector. It holds for each of the three stated refinements.

There are dV edges. Since b_e b_e^dagger is bounded by the projector onto an
empty A endpoint and occupied B endpoint,

    sum_e <b_e b_e^dagger> <= 2d <H_A> <= d<K> <= 2d<R>.

Cauchy-Schwarz for the positive state, followed by the scalar sum inequality,
gives, with C_d=d(4d-2) and r=<R>,

    |<T>| <= 2d sqrt(2Vr),
    |<D_birth^dag(T)>| <= C_d beta sqrt(2Vr).             (7)

These are density estimates, not operator-norm estimates proportional to V
inserted into a small-system perturbation condition. They allow mixed states
and do not presume sparsity of individual quantum trajectories.

Let E(tau)=<H_star>, initially zero. Hamiltonian evolution conserves this
energy, while the supplied formation apparatus can change it. Equations
(5)-(7), with epsilon=|t|/Delta, imply

    E'(tau)/(Delta V)
       <= 2(d-1) beta r/V + sqrt(2) C_d beta epsilon sqrt(r/V),
    r/V <= E/(Delta V)+2sqrt(2)d epsilon sqrt(r/V).

Put u=r/V. Applying Young's inequality only to the last, instantaneous
square-root term yields the integral comparison

    u(tau) <= 8d^2 epsilon^2
           + 4(d-1) beta integral_0^tau u(s) ds
           + 2sqrt(2) C_d beta epsilon integral_0^tau sqrt(u(s)) ds. (8)

For epsilon>0 compare with the equality solution y=epsilon^2 z^2, starting
at y(0)=8d^2 epsilon^2. The right-hand side is increasing in y and is locally
Lipschitz away from zero; that positive equality solution bounds the continuous
nonnegative u by the usual first-crossing integral comparison. Its equation
for z is linear:

    z'=2(d-1) beta z+sqrt(2) C_d beta,       z(0)=2sqrt(2)d.

Consequently, for every finite volume and every finite tau>=0,

    <R(tau)>/V <= epsilon^2 z_d(tau)^2,
    expected_births(tau)/V=<M(tau)>/V <= epsilon^2 z_d(tau)^2,       (9)

where

    z_d(tau)=sqrt(2){[2d+C_d/(2(d-1))]exp[2(d-1)beta tau]
                             -C_d/(2(d-1))},             d>1,
    z_1(tau)=2sqrt(2)(1+beta tau).                         d=1.     (10)

For epsilon=0 the initial state stays in R=M=0 and (9) follows directly.
The bounds can be very loose, especially for d>1 or long times. They do not
certify a useful practical density at an arbitrarily chosen finite scale.

Holding J,beta fixed and taking t=(J Delta^3/2)^(1/4) gives
epsilon^2=sqrt[J/(2Delta)]. Thus additional record density and star-defect
density tend to zero at each fixed finite time, uniformly over the finite
periodic volumes in this family. The result survives arbitrary initial ice
superpositions in the selected sector. It controls spatial averages; it is
not a volume-uniform approximation to local field evolution, a concentration
bound, a thermodynamic photon theorem, or an indefinite survival statement.

## 4. Energy costs remain explicit

The absence of an alternating Hamiltonian coefficient does not provide a
cost-free formation apparatus. In the exact four-site control the full
zero-Gauss sector has nine states. Its seven original-number states have
precisely the old penalties; its two filled four-record states have energy
Delta under (1), rather than 2Delta under the former Delta N_B extension.
They have no permitted hop. For any normalized low eigenvector of energy
E_low in the original-number sector,

    formation_power = (Delta-E_low) formation_rate.     (11)

This identity follows directly by applying the adjoint dissipator to H_star
and is checked against the full finite matrices. The bare R birth change is
zero on this square, but the full energy increase is not zero: formation
destroys the negative hopping coherence. A bare diagonal ledger alone would
miss that energy exchange.

In the bulk, immediately after one allowed hop, R=1. Of the 2d-1 vacant
neighbor edges, d produce a target with R=1 and d-1 a target with R=3. Their
mean bare target star energy is Delta(4d-3)/(2d-1). This count is checked for
every allowed first hop in six ice configurations on 6x6 and 6x6x6 tori. It
is not an exact many-body energy-cost formula once hopping coherence and
later events matter.

The runner also checks the local identities on complete 18-, 108- and
324-dimensional tensor products and integrates the complete nine-state
Lindblad equation at four values of Delta and three times. Both charge
refinements and the two coherent signs are included in the exact identities.
Those small computations check the algebra; the argument (4)-(10) supplies
the volume-uniform density bound.

## 5. Remaining premises and next physical question

This construction replaces the explicitly alternating pinning Hamiltonian by
a homogeneous field-star interaction while retaining the same fixed-number
ring physics and a controlled finite-time density of newly formed records.
The selected period-two Gauss-charge sector and checkerboard preparation
remain essential inputs. Their origin, the placement of field qubits, the
birth apparatus energy, the quantum amplitude/statistics rule and the scale
limit still need a physical derivation or a native compiler.

The central next issue is field dynamics in large systems. A sparse density
of extra records does not by itself imply a small local field disturbance:
mobile defects can propagate, and their speeds need not stay bounded in the
fixed-J limit. Neither the finite-volume ring limit nor the uniform density
bound closes that issue. It remains an explicit proof obligation, without a
claim that the obstruction is fundamental or that a TOE follows.


## Landing scope and No-Go Discipline Gate

- **N1 — Domain:** only the model, graph, sector, preparation, observables and order of limits explicitly specified above.
- **N2 — Alternatives:** other instruments, Hamiltonians, states and scaling paths are not excluded.
- **N3 — Imports:** supplied quantum and probabilistic structures are model assumptions; the native axioms do not select them.
- **N4 — Dependencies:** named companion arguments are used within their stated scope; no audit grade is inherited.
- **N5 — Evidence:** exact finite algebra and numerical stability controls corroborate the displayed proofs. Floating spectra and propagations are not interval enclosures. Historical tables are not independently certified by their presence here.
- **N6 — Resolution:** fixed-volume, uniform-volume and ordered-limit statements keep their distinct hypotheses; no exchange of limits is inferred.
- **N7 — Remaining work:** native selection, physical implementation, energy supply, preparation and empirical identification remain separate obligations except for explicitly proved model-specific results.
- **N8 — Authority:** this source applies no audit verdict, retained grade or assembly decision.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository premise boundary only; it does not derive the supplied model.
- [hardcore_record_motion_generates_gauge_rings_bounded_theorem_note_2026-09-24](HARDCORE_RECORD_MOTION_GENERATES_GAUGE_RINGS_BOUNDED_THEOREM_NOTE_2026-09-24.md): conditional argument only within its explicit hypotheses.
- [uniform_record_density_with_live_formation_bounded_theorem_note_2026-09-24](UNIFORM_RECORD_DENSITY_WITH_LIVE_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-24.md): conditional argument only within its explicit hypotheses.

Finite-dimensional linear algebra, operator calculus and the explicit inequalities above are mathematical tools. Referenced literature is attribution or context unless its actual assumptions and use are stated in the argument.

## Source and verification

Source PR #8635, frozen head `ff1edc030d8a2aaec9aab16a2354e7cc113ef8cf`. The primary review session uses no subagents; no separate fix reviewer or formal audit is claimed. Original auxiliary packets, failed attempts and historical seals remain recoverable on the original PR branch. The combined receipt records each original path disposition.

```bash
python3 scripts/homogeneous_field_star_penalty_for_mobile_records_2026_09_24.py
```

The canonical wrapper executes the selected scientific controls in a fresh temporary directory, retains their generated result JSON in its stdout, and ends with TOTAL. It does not execute historical sealing or approval instructions.
