---
claim_id: emergent_fermion_density_weak_field_source
claim_type: bounded_theorem
claim_scope: "CONDITIONAL on two separately supplied surfaces -- the designed fermion law of EMERGENT_3D_FERMION_ONE_QUBIT_PER_SITE_SUPERLATTICE_ROLE_PATTERN_EXISTENCE_BOUNDED_THEOREM_NOTE_2026-09-02.md, which that note declares a supplier model derived from no axiom, and the landed weak-field response surface of docs/GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md -- the operator n_v = (1 - B_v)/2 on the coarse sublattice 2Z^3 satisfies, on the named finite clusters and nowhere else: (T1) every clause of that bridge's source-readout uniqueness hypothesis as a named operator, being diagonal, a projector and hence positive, local on exactly the six coarse edge sites at 2v, phase invariant, and covariant under the 2Z^3 translations, and I(S) = sum_{v in S} n_v is a finite-additive scalar functional with I(empty) = 0 and I(S disjoint-union T) = I(S) + I(T) as an operator identity, which is the premise docs/RECORD_ADDITIVITY_DOES_NOT_SUPPLY_NEWTON_PRODUCT_BOUNDED_THEOREM_NOTE_2026-08-13.md records as supplied by no current Record. (T2) [N, T_ij] = 0 exactly for every coarse edge of the open 3x3x3 and 4x4x4 blocks, 216 anticommuting and 2700 commuting (component, B_v) pairs at 3x3x3 and 576 and 17856 at 4x4x4, the (B_i - B_j) factor of T_ij = (i/2) A_ij (B_i - B_j) being exactly what conserves the count while a bare A_ij B_i does not, and prod_v B_v = +I makes N even-valued. (T3) An A-string pair state on the open 5x5x5 block is an exact two-point source, <n_w> = 1 at the two endpoints and 0 at the other 123 coarse vertices with N = 2 and commutation with all 240 face stabilizers, for three axis and two non-axis separations; and on the open 2x2x2 cube's 4096-dimensional state space the vacuum is unique, the 28 two-excitation states are an orthonormal occupation basis, the encoded hop sum leaves that sector invariant, its spectrum equals the free-fermion pair sums of the 8x8 coarse hop matrix, and <n_v> = |psi(v)|^2 with <n_partner> = 1 to 3e-16 over four amplitudes. (T4) The response phi = G0 P0 rho to rho = <n>, with H = -Delta_lat, reproduces the landed monopole form as TWO reported outcomes, not one: the coarse tori L = 8, 12, 16 give 4 pi r G at r = L/4 of 0.4065, 0.3658 and 0.3468, all outside the 0.02 band that docs/POISSON_FINITE_VOLUME_WINDOW_AND_BIHARMONIC_OFFSET_BOUNDED_THEOREM_NOTE_2026-07-27.md sets about its own stable 0.3266-0.3269, while L = 32, 64, 96, 128 give 0.3307, 0.3275, 0.3269 and 0.3267, inside that band and matching that note's quoted values to four decimals at L = 96 and 128, and Richardson extrapolation gives the monopole coefficient 4 pi d G_inf(d) = 1.0194, 1.0064, 1.0009 and 0.9963 at d = 4, 6, 8, 10; all of it under a coarse/fine unit carry declared before the run and measured at 2, reading (i) giving 1/(4 pi d_coarse) = 1/(2 pi |r_fine|) and reading (ii) giving 1/(4 pi |r_fine|), a factor of two this note makes explicit and does not adjudicate. (T5) Under reading (ii) the six-site star average S obeys -Delta_fine = 6(1 - S), so phi_smeared(r) = phi_point(r) - (1/6)(delta_{r,0} - 1/N) exactly on the fine tori 16^3, 24^3 and 32^3, the correction being identically zero off the source site rather than an O(1/d^3) tail, and the star's dipole and traceless quadrupole vanish in exact rationals with the first non-vanishing multipole at l = 4. (T6) The encoded two-particle spectrum equals the free-fermion pair sums on the open 2x2x2 and 3x3x3 blocks, so the supplied law generates no interaction, and the response energy is exactly bilinear in the occupations, so the object the pooled response carries is the count product I(S) I(T) and NOT a mass product. (T7) n_v is a projector, so <n_v> lies in [0, 1] in every state and its source vector over the two eta sectors is [+1, +1], leaving residual sqrt(2) against the orientation-odd [+1, -1] that the chi_eta rho Phi cross term of docs/SIGNED_GRAVITY_APS_ACTION_ORIGIN_SUPERSELECTION_STABILITY_NOTE.md requires, while the only orientation-odd objects this construction has, A_ij with A_ji = -A_ij and the A-strings built from them, fail the diagonal, positive and vertex-density clauses; that is a scoped statement about this route and about no other. No mass, no M_phys, no G_Newton, no coupling, no test-body response law and nothing nonlinear appears anywhere. The fermion law is derived from no axiom, no axiom is amended, no status is set, and no registry entry is created."
upstream_dependencies: []
runner: scripts/emergent_fermion_number_density_weak_field_source_check_2026_09_02.py
---

# The emergent fermion's number density as the weak-field source: a named operator for the gravity lane's `rho`

**Date:** 2026-09-02
**Type:** bounded_theorem, explicitly conditional on two supplied surfaces
**Audit:** unset; independent audit remains a separate lane
**Status:** bounded - bounded or caveated result note
**Status authority:** independent audit only. This source changes no axiom, primitive, framework rule, or audit verdict.
**Primary runner:** [`scripts/emergent_fermion_number_density_weak_field_source_check_2026_09_02.py`](../scripts/emergent_fermion_number_density_weak_field_source_check_2026_09_02.py)
**Runner cache:** [`logs/runner-cache/emergent_fermion_number_density_weak_field_source_check_2026_09_02.txt`](../logs/runner-cache/emergent_fermion_number_density_weak_field_source_check_2026_09_02.txt)
**Parents:** none in the dependency sense. The two conditioning surfaces are quoted in "Setting" as conditions, not consumed as graded rows.

The gravity lane has a field equation and no matter to put in it. Its weak-field bridge proves that *if* it is handed a lattice amplitude, the density it must read off that amplitude is
unique -- and then stops, because nothing in the lane says what the amplitude is. Separately, the record-additivity note names the one algebraic object the Newton chain is missing, a
finite-additive scalar functional on record collections, and records that no current surface supplies it. This note observes that the emergent-fermion construction supplies both at once
in a single named operator, and computes what that operator does inside the lane's own equation: it satisfies every clause of the uniqueness hypothesis, it is conserved by the
construction's own hop, it is an exact point source, and the field it produces carries the landed `1/(4 pi |r|)` shape -- with one factor of two, between two readings of what "distance"
means, that this note makes explicit and cannot settle.

## Machine status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact finite-cluster operator theorems plus finite-dimensional numerical response computations, every one conditional on two named supplied surfaces and on nothing else. Groups A, B, C, F2, H are exact integer, F2/Z4 and exact-rational arithmetic with no floating point; groups D, E, F1, G are finite floating-point computations each reporting its residual against a tolerance declared before the run."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "The physical Newton residual is instead the source/test typing, mass-readout identification, and test-body response law. Current Record supplies none of the finite-additive scalar premise."
source_of_blocker_text: audit_ledger
reachability_to_target: partially_closes
artifact_role: theorem
next_trace_action: "Route to its owner the one question this note does not decide: which of the two unit readings, coarse-graph-physical or fine-lattice-physical, the framework's length is; then attack the two residuals this note leaves standing, the mass-readout identification and the test-body response law."
conditional_surface_status: conditional-support
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

## Exact target

The target is the conjunction of the seven statements below, exactly the runner's check groups `A`-`H`: `T1` (`A`) the density clauses and the additive functional; `T2` (`B`) conservation of the count by the
supplied hop, with mechanism and control; `T3` (`C`, `D`) pair states as exact point sources and the amplitude identity `<n_v> = |psi(v)|^2`; `T4` (`E`) the response, stated as two outcomes with the unit carry
declared in advance; `T5` (`F`) the smearing identity and the vanishing star multipoles; `T6` (`G`) bilinearity and the count product; `T7` (`H`) the positivity obstruction on the signed route. Each is proved
on named finite clusters and carries its own tag: `[exact]` where the arithmetic is integer, `F2`/`Z4` or exact-rational, `[numerical]` with a stated tolerance where it is floating point.

## Imports and authority

Imported scientific authority: none load-bearing. The Bravyi-Kitaev superfast encoding, the discrete Fourier inverse of the graph Laplacian, and Richardson extrapolation in `1/L` are standard methodology; every
object is redeclared here and the runner recomputes every statement, including a validation of its own Green-function implementation against the landed window note's published table before any new number is
reported. The two surfaces this note is conditional on are declared, quoted and named in "Setting"; they are conditions of the result, not graded dependencies, and this note cites none of their grades and
consumes no row. Non-load-bearing context pointers, plain file names with no grade and no dependency weight: `MINIMAL_AXIOMS_2026-06-29.md` (the four axioms quoted below);
`GRAVITY_CLOSURE_FROM_WEAK_FIELD_LINEAR_RESPONSE_BOUNDED_THEOREM_NOTE_2026-06-07.md`, whose own Source boundary forbids citing it for the `1/(4 pi r)` asymptotic, so the authority for that asymptotic is the
Maradudin import note quoted below; and `NEWTON_LAW_DERIVED_NOTE.md`, whose Non-Claims bound this whole exercise and are quoted in full below.

## Setting

The four framework axioms are quoted, not amended. **Lattice**: "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations, and proper cubic rotations
about each site." **Qubit**: "Each site has a domain of local possibilities," whose "full one-site possibility domain has algebraic presentation `M_2(C)`." **Admissibility**: "There is one fixed
nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations." **Record**: "Records form. When present, a record locks exactly one admissible local possibility. A site
never carries more than one record; records are permanent. Only records are readable. A readout value is determined by record content alone."

The record ontology is what makes the object below a density at all. `n_v` is not a new primitive and not a site: it is a **readout of six records**. The six fine edge sites `2v +- e_a` around the coarse corner
`2v` each carry a record; `B_v` is the product of their six `Z` values, so `n_v = (1 - B_v)/2` returns `1` exactly when those six records carry odd parity and `0` when they carry even. Nothing is read that is
not a record, and the value is determined by record content alone, as Record requires. That is the whole of the identification: the gravity lane's `rho` is a parity readout of six neighbouring records.

**Supplied surface one -- the fermion law.** From
`origin/physics-loop/emergent-3d-fermion-superlattice-existence:docs/EMERGENT_3D_FERMION_ONE_QUBIT_PER_SITE_SUPERLATTICE_ROLE_PATTERN_EXISTENCE_BOUNDED_THEOREM_NOTE_2026-09-02.md`, verbatim: "The **encoding**
is the Bravyi-Kitaev superfast encoding written on the coarse sublattice, with the code qubits exactly the coarse edge sites. The direction order at every coarse vertex is `-x < -y < -z < +x < +y < +z`." and
"`B_i = -1` marks the excitation; the **hop** across the coarse edge `(i, j)` is `T_ij = (i/2) A_ij (B_i - B_j)`." Its Proof boundary, verbatim and outranking every summary: "The law of Theorems 1 to 3 is a
**designed supplier model**: Admissibility fixes that there is one covariant nearest-neighbour rule and leaves its form to the supplier, and this note supplies one form and computes its consequences, deriving
that form from no axiom and claiming for it no privileged status." Everything below inherits that conditional.

**Supplied surface two -- the weak-field response.** From `docs/GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md`, verbatim: the quadratic source action `A[phi; rho] = (1/2) <phi, H
phi> - <P0 rho, phi>` "has the unique stationary solution, modulo the constant zero mode, `phi = G0 P0 rho`." And the clause this note answers, verbatim: "For a lattice amplitude `psi`, the only local,
diagonal, positive, phase-invariant quadratic density that is translation covariant and normalized by `sum_x rho_psi(x) = ||psi||^2` is `rho_psi(x) = |psi(x)|^2`. On finite periodic volumes the Poisson solve
uses `P0 rho_psi`, i.e. the zero-mode-subtracted density. The zero mode is the total-mass/background sector and is not part of the local force law." The lane proves a uniqueness statement **conditional on being
handed a `psi`**, and nothing in the lane names one. That is the gap this note fills.

**The `1/(4 pi |r|)` authority.** From `docs/LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md`, verbatim: with the stencil `(-Delta_lat f)(x) = 6 f(x) - sum_{|y - x| = 1} f(y)`, the Green's
function satisfies "`G(r) -> 1 / (4 pi |r|)` as `|r| -> infinity`", and "The leading `1 / (4 pi |r|)` continuum-limit form is therefore the framework's own nearest-neighbor `Z^3` Poisson kernel normalization
with unit lattice spacing." That last clause is load-bearing: the fermion lives on `2Z^3`, and the unit is what moves.

And from `docs/POISSON_FINITE_VOLUME_WINDOW_AND_BIHARMONIC_OFFSET_BOUNDED_THEOREM_NOTE_2026-07-27.md`, verbatim: the scaling window `r = max(3, floor(N/16)), ..., floor(N/4)` "gives a stable exponent near
`1.66`; its outer-edge normalization is near `0.327`, not `1`", with `4 pi r G` at `r = N/4` equal to `0.3269`, `0.3267`, `0.3266` at `N = 96, 128, 192`, the last three exponents agreeing "within `0.02`", and
"The stable finite-volume number is not the continuum target `1`." That value and that band are read here **before** the run and used as the tolerance; the run chooses none of its own.

**The missing scalar.** From `docs/RECORD_ADDITIVITY_DOES_NOT_SUPPLY_NEWTON_PRODUCT_BOUNDED_THEOREM_NOTE_2026-08-13.md`, the hypothesis, verbatim: "**Finite-additive scalar hypothesis.** On a supplied class of
finite record collections, `I` is scalar-valued, `I(empty)=0`, and `I(A disjoint-union B)=I(A)+I(B)` for disjoint `A,B`." And its `claim_scope`, verbatim: "The physical Newton residual is instead the
source/test typing, mass-readout identification, and test-body response law. Current Record supplies none of the finite-additive scalar premise." And from `docs/NEWTON_LAW_DERIVED_NOTE.md`, **Non-Claims**,
verbatim: "This row does not prove: the lattice Poisson equation as a physical equation of motion; the `Z^3` Green-kernel asymptotic from first principles; the test-mass force/source response rule `F = -M_test
grad(phi)`; the physical product law `M_source M_test`; the gravitational coupling normalization; Newton's law as an unconditional framework output; continuum/null-geodesic/general-relativistic gravity claims."
Every one of those is still not proved after this note.

**The signed sector's demand.** From `docs/SIGNED_GRAVITY_APS_ACTION_ORIGIN_SUPERSELECTION_STABILITY_NOTE.md`, verbatim: the proposed `S_int = - chi_eta(Y) M_phys <rho, Phi>` needs a source vector over `(chi=+,
chi=-)` of `[+1, -1]`, while "retained positive Born/Gauss source" contributes `[+1, +1]` and the APS and Wald terms `[0, 0]`; "It cannot span the required orientation-odd source `[+1,-1]`." What that sector
wants of matter is a density that is **signed**.

## Obligation graph

The proof is acyclic; each node after `P0` is checked by the correspondingly lettered runner group, and the strongest supported scope is precisely `P0`-`P7`. `P0`, declared here and conditional: the two
supplied surfaces above, the coarse sublattice, the encoding, the hop, and the response operator. `P1` (`A`): the density clauses, the additive functional, and the parity constraint. `P2` (`B`): conservation of
the count by the hop, with its mechanism and its control. `P3` (`C`, `D`): pair states as exact point sources, and the amplitude identity in the `2^12` space. `P4` (`E`): the response, its validation against
the landed table, its two outcomes, and the unit carry. `P5` (`F`): the smearing identity and the star's multipoles. `P6` (`G`): bilinearity of the response energy and absence of an interaction term. `P7`
(`H`): the positivity obstruction on the signed route.

## Definitions

The **coarse sublattice** is `2Z^3`; a coarse vertex `v` sits at the fine site `2v`, and the coarse edge from `v` in direction `e_ax` sits at the fine site `2v + e_ax`, an edge site. Code qubits are exactly the
coarse edge sites. For an ordered coarse edge `(i, j)`, with the direction order `-x < -y < -z < +x < +y < +z` at every coarse vertex,

```text
A_ij = X(edge site of (i,j)) * prod Z(edges ordered before it at i) * prod Z(edges ordered before it at j),   A_ji = -A_ij,
B_i  = prod of the six Z's on the edges incident to i,
S_f  = the ordered product of the four A's around a coarse plaquette f,
T_ij = (i/2) A_ij (B_i - B_j),
n_v  = (1 - B_v)/2,   I(S) = sum_{v in S} n_v,   N = I(all coarse vertices).
```

`n_v` is the **number density** this note proposes as the gravity lane's `rho`, and `I` the scalar functional on finite coarse-vertex sets. The **response** is the landed one, unchanged: `H = -Delta_lat` with
the seven-point stencil, `G0 = H^{-1}` off the constant mode, `P0` the projection off that mode, and `phi = G0 P0 rho`. On a torus of side `L`, `G0` is diagonal in the symbol `lambda(k) = 6 - 2(cos k_x + cos
k_y + cos k_z)` with the `k = 0` entry set to zero, which is exactly `P0`.

Two **unit readings** are carried side by side, both declared before the run and neither fitted. **Reading (i), the coarse graph is physical**: `2Z^3` with its nearest-neighbour graph is graph-isomorphic to
`Z^3`, so the landed theorem applies verbatim in coarse units, `G -> 1/(4 pi d_coarse)`, and since `|r_fine| = 2 d_coarse` that is `1/(2 pi |r_fine|)`. **Reading (ii), the fine lattice is physical**: `n_v` is
pushed onto the fine lattice with weight `1/6` on each of the six fine edge sites carrying `B_v`, and the far field is `1/(4 pi |r_fine|)`. The two differ by exactly a factor of two. This note computes both,
reports the ratio, and does not decide between them.

## Theorem 1 -- the count is a named operator meeting every clause, and it is the missing additive scalar

**Conclusion.** On the open coarse blocks `3x3x3` (`V/n/k_faces = 27/54/26`) and `4x4x4` (`64/144/63`):

1. `n_v = (1 - B_v)/2` is **diagonal** in the site basis, since `B_v` is a product of six `Z`s and carries no `X`; **positive**, being a projector `n_v^2 = n_v` with spectrum `{0, 1}`; **local**, supported on
   exactly the six coarse edge sites incident to `2v`; **phase invariant**, trivially, being diagonal; and **translation covariant** under every `2Z^3` shift of the `4^3` coarse torus. The `n_v` commute
   pairwise.
2. `I(S) = sum_{v in S} n_v` satisfies `I(empty) = 0` and `I(S disjoint-union T) = I(S) + I(T)` as an **operator identity**, checked on 30 random disjoint coarse-vertex pairs across the two blocks.
3. `prod_v B_v = +I` on both blocks, so `N` is even-valued and excitations exist only in pairs.

**Proof.** Items 1 and 2 are exact: diagonality, support and covariance are read off the symplectic representation, the projector and additivity statements are computed in exact Gaussian-rational Pauli-sum
arithmetic, and pairwise commutation is a symplectic form evaluation over all vertex pairs. Item 3 is an exact `Z4`-phase product. No floating point enters.

**What this settles and what it does not.** Item 1 says the bridge's five-clause hypothesis is met by a *named* operator, so `rho_psi = |psi|^2` stops being conditional on an unsupplied carrier; it does not
make that uniqueness statement any stronger than the bridge already proved it. Item 2 supplies the finite-additive scalar functional the additivity note records as supplied by no current Record, conditionally
on the supplied fermion law -- exactly the shape of premise that note asked for. Item 3 matches the lane's `P0`: an intrinsically pair-created source is the neutral source the finite-torus Poisson solve is
built for.

## Theorem 2 -- the supplied hop conserves the count exactly, and the mechanism is visible

**Conclusion.** For every coarse edge of the open `3x3x3` and `4x4x4` blocks, `[N, T_ij] = 0` exactly, as a Pauli-sum identity in exact Gaussian rationals. The mechanism: each of the two components `A_ij B_i`
and `A_ij B_j` anticommutes with exactly `B_i` and `B_j` and commutes with every other `B_v` -- `216` anticommuting against `2700` commuting `(component, B_v)` pairs at `3x3x3`, and `576` against `17856` at
`4x4x4`. The control: a bare `A_ij B_i` alone does **not** commute with `N`, its commutator carrying two Pauli terms.

**Proof.** Exhaustive and exact. `N` is formed as the full sum over all vertices, `T_ij` as the exact two-term Pauli sum `(i/2) A_ij (B_i - B_j)`, and the commutator is expanded term by term with `Z4` phase
bookkeeping and exact rational coefficients; a residual of zero is the vanishing of the term dictionary, not a tolerance. The anticommuting sets are computed by symplectic form over every `(component, vertex)`
pair rather than assumed from the encoding relations.

**Reading of the control.** Conservation is a property of the *supplied hop*, not of `A_ij`. `A_ij` moves an excitation by flipping two `B`s, which changes `N` by `0` or `+-2`; the factor `(B_i - B_j)` is
precisely the projector onto the number-conserving component. Had that factor not been there, the count would not be a matter charge and this note would have stopped here.

## Theorem 3 -- pair states are exact point sources, and the density is the squared amplitude

**Conclusion.**

1. On the open `5x5x5` coarse block, the `A`-string from `v` to `v'` applied to the vacuum gives `<n_w> = 1` exactly at `v` and `v'` and `0` at each of the other `123` coarse vertices, with `N = 2`, for axis
   separations `d = 1, 2, 3` and for two non-axis separations; and each of those five strings commutes with all `240` face stabilizers of the block, `1200` of `1200` pairs. So `rho = delta_v + delta_v'` is an
   exact two-point source on a code state.
2. On the open `2x2x2` coarse cube -- `12` code qubits, a `4096`-dimensional state vector, with no dense many-body matrix formed anywhere -- the vacuum is the unique joint `+1` eigenvector of the six face
   stabilizers and all eight `B_v`; the `28` two-excitation string states are orthonormal to `2e-16` and are exact occupation eigenstates; the encoded hop sum leaves that `28`-dimensional sector invariant,
   leakage `4e-16`; its spectrum equals the free-fermion pair sums `{mu_a + mu_b}` of the `8x8` coarse hop matrix, whose levels are `-3`, `-1` three times, `+1` three times, `+3`; and against a pinned partner
   `<n_v> = |psi(v)|^2` at every vertex with `<n_partner> = 1`, worst deviation `3e-16` over the pinned-partner ground state, the top state, a localized wavepacket and a generic complex amplitude.

**Proof, and what item 2 is for.** Item 1 is exact: `<B_v>` in a stabilizer state is `+1` or `-1` by a symplectic form evaluation, so `<n_w>` is an integer, and the face-stabilizer commutation is likewise
exact. Item 2 is a `2^12` state-vector computation with the stabilizer projector applied generator by generator, seeded twice independently to establish uniqueness of the vacuum ray, every residual against the
declared `1e-14`. It is there because the identification must not be an artefact of the stabilizer formalism: the amplitude identity `<n_v> = |psi(v)|^2` is the exact sentence the bridge's uniqueness clause
presupposes, and it is verified here in the full Hilbert space for a generic complex amplitude, not only for the eigenstates that are convenient.

## Theorem 4 -- the response, as two outcomes and one declared unit carry

**Conclusion.** With `phi = G0 P0 rho` and `rho = <n>` on coarse tori:

1. **Validation first.** The recomputed `4 pi r G(r)` at `r = 10` on the landed fixed window rounds to `0.190 / 0.432 / 0.568 / 0.709 / 0.782` at `N = 32 / 48 / 64 / 96 / 128`, the window note's own published
   row. The `G0` used below is that object, not a reimplementation.
2. **Outcome one.** At the scaling-window outer edge `r = L/4` the small coarse tori `L = 8, 12, 16` give `4 pi r G = 0.4065 / 0.3658 / 0.3468`, every one **outside** the window note's own `0.02` band about its
   stable `0.3266`-`0.3269`.
3. **Outcome two.** From `L = 32` the readout enters that band, `0.3307 / 0.3275 / 0.3269 / 0.3267` at `L = 32 / 64 / 96 / 128`, matching the quoted `0.3269` and `0.3267` to four decimals at `L = 96` and `128`.
4. **The coefficient.** Richardson in `1/L`, `G_inf = 2 G_128 - G_64`, gives `4 pi d G_inf(d) = 1.0194 / 1.0064 / 1.0009 / 0.9963` at `d = 4 / 6 / 8 / 10` -- the landed coefficient `1`, inside the declared
   band.
5. **The unit carry.** `G_coarse^(64)(d) / G_fine^(128)(2d)` falls monotonically from `2.125` at `d = 2` to `2.0047` at `d = 16`: the ratio is `2`, the factor between the two readings, measured against a value
   declared before the run.
6. **The pair source.** `E(d) = <rho, G0 P0 rho> = 2 G(0) + 2 G(d)` exactly, to `2e-16`, at every separation on `L = 8, 12, 16`.

**Proof.** `G0` is the discrete Fourier inverse of `lambda(k)` with the zero mode set to zero, which is `P0` exactly rather than approximately; the response is one forward and one inverse transform. The window
comparison is against values quoted from the landed note before the run, with that note's own `0.02` band as the tolerance. The extrapolation is the standard `1/L` Richardson step on the periodic
zero-mode-removed Green function, applied at fixed `d`, with no fitting window and no free parameter.

**Both outcomes are the result, and the factor of two is open.** Items 2 and 3 answer different questions and are reported as two, not one: the small tori do not reach the landed value and are not evidence for
the identification, while items 3 and 4 say that deficit is finite volume -- it shrinks monotonically, lands inside the note's own band from `L = 32`, and extrapolates to the landed coefficient. The honest
reading of item 2 is about the box, not about `n_v`. Separately, reading (i) gives `1/(4 pi d_coarse) = 1/(2 pi |r_fine|)` and reading (ii) gives `1/(4 pi |r_fine|)`; item 5 measures the ratio at `2`, as
declared. Which reading is the framework's length is **not** decided here, and nothing below assumes one.

## Theorem 5 -- smearing changes nothing, exactly

**Conclusion.** Under reading (ii), let `S` be the six-site star average. Then `-Delta_fine = 6(1 - S)`, hence `G0 P0 S = G0 P0 - (1/6) P0`, hence

```text
phi_smeared(r) = phi_point(r) - (1/6)(delta_{r,0} - 1/N)      exactly.
```

Verified on the fine tori `16^3`, `24^3` and `32^3` to `6e-17`. Off the source site the two potentials differ only by the uniform `1/(6N)` that `P0` removes. Separately, in exact rationals the star has monopole
`1`, dipole `0`, traceless quadrupole `0` and every `l = 3` moment `0`, so by cubic symmetry the first non-vanishing correction is `l = 4`.

**Proof, and why it is sharper than expected.** The operator identity is one line of algebra on the stencil, then confirmed numerically on three fine tori; the multipole moments are exact rational sums over the
six offsets `+-e_x, +-e_y, +-e_z`, and the vanishing of the dipole and the traceless quadrupole is cubic symmetry, computed rather than asserted. The natural expectation was a quadrupole correction falling as
`1/|r|^3`. There is none: off the source site the correction is **identically zero** and the first surviving multipole is `l = 4`, so where the count is read -- at the coarse corner or spread over its six fine
neighbours -- changes the field nowhere except at the source site itself.

## Theorem 6 -- bilinearity, and what the pooled object actually is

**Conclusion.** The two-particle spectrum of the encoded hop on the open `2x2x2` (`28` states) and `3x3x3` (`351` states) blocks equals the free-fermion pair sums to `1e-14`: the interaction term is identically
absent. And the response energy is exactly bilinear in the occupations, `|E(r1+r2) - E(r1) - E(r2) - 2<r1, G0 P0 r2>| <= 3e-16` over `15` random multi-excitation configurations on `L = 8, 12, 16`.

**Proof.** The two-particle Hamiltonian is built explicitly on the antisymmetric sector and diagonalized; the pair sums come from the one-particle coarse hop matrix. The bilinearity identity is evaluated on
random configurations by three response solves each.

**The product is a count product, not a mass product.** The additivity note's Theorem 2 supplies `B_I(S, T) = I(S) I(T)` once a finite-additive `I` is in hand, and Theorem 1 item 2 puts one in hand. So the
object this route delivers is `I(S) I(T)`, the product of two **counts**. It is emphatically **not** `M_source M_test`: no mass appears anywhere in this note, and the identification of a count with a mass is a
separate premise this note neither supplies nor assumes.

## Theorem 7 -- the positivity obstruction, scoped to this route

**Conclusion.** `n_v` is a projector, so `<n_v>` lies in `[0, 1]` in every state, code or not, and its source vector over the two `eta` sectors is `[+1, +1]`. Least squares against the orientation-odd `[+1,
-1]` the `chi_eta rho Phi` cross term requires leaves residual `sqrt(2) = 1.414`, which is the signed note's own reported `1.414e+00`. And the only orientation-odd objects this construction has fail the source
clauses: `A_ji = -A_ij`, yet `A_ij` carries an `X` so it is not diagonal, it is a Hermitian involution of spectrum `{+1, -1}` so it is not positive, it is an edge object and not a vertex density, and it flips
exactly `B_i` and `B_j`; the `A`-strings built from it are likewise non-diagonal and supported along the whole path.

**Proof.** The projector property is exact. The residual is the same least-squares evaluation the signed note reports, on the same two-sector basis. The orientation and clause properties of `A_ij` and of the
string are exact symplectic and `Z4` statements, each one checked rather than inferred.

**Exact scope.** This is a statement about **this** route: the objects the emergent-fermion construction as supplied makes available. It says that within this construction the diagonal positive candidate is
unsigned and the signed candidates are not diagonal or positive. It is not a no-go, it closes nothing, and it says nothing about whether some other construction, some other species, or some other sector could
supply `[+1, -1]`. The signed gate is exactly where the signed notes left it.

## Corollary -- what moved and what is left

Within the setting declared above, conditional on the two supplied surfaces, and on the finite clusters named:

1. The gravity lane's "no matter to source it" now has a **named candidate inside the four axioms**: a parity readout of six neighbouring records, satisfying every clause of the lane's own uniqueness
   hypothesis, conserved by the supplied dynamics, and producing the landed field shape.
2. The finite-additive scalar functional that `RECORD_ADDITIVITY_..._2026-08-13` records as supplied by no current Record is supplied here, conditionally on the fermion law. That note's `next_trace_action`
   names three residuals -- source/test typing, mass-readout identification, the test-body response law -- and this note supplies typing, distinct excitations at distinct coarse vertices being separately
   accessible with `I` evaluating on each, leaving the other two.
3. So the Newton lane's residual narrows to two: **the mass-readout identification**, what turns a count into a mass, and **the test-body response law** `F = -M_test grad(phi)`, which
   `NEWTON_LAW_DERIVED_NOTE.md` records as neither retained nor registered. Both are untouched here. One item is added, not removed: **which unit reading is physical**, a new open question this note creates by
   being explicit, and a better place to be than a hidden factor.

**Reading, not theorem.** Where the fermion sits, the count is one; where it does not, zero. The landed field equation answers that count with the same fall-off it already had, and the answer does not care
whether the count is read at the corner or spread over its six neighbours.

## What does not move

- No mass, no `M_phys`, no `G_Newton`, no coupling constant, and no absolute unit appears anywhere. The fermion note supplies none, and this note invents none.
- No test-body response law. `F = -M_test grad(phi)` is exactly as unsupplied after this note as before it.
- Nothing at nonlinear order: this note stays strictly at the linear response the bridge supplies. The signed sector is untouched; Theorem 7 is a property of this route's objects, not a bound on the sector.
- No axiom text is amended, extended, reworded, or reinterpreted, and no hypothesis is adopted. No status value is set, predicted, or implied. No premise registry, citation manifest, or axiom-premise node is
  created or edited.

## Interfaces named for other lanes, not moved here

- **The unit reading.** Whichever lane owns the framework's length scale should decide between reading (i) and reading (ii). Theorem 4 item 5 hands it a measured factor of `2` and two fully explicit
  alternatives; it does not hand it an answer.
- **The mass readout.** A lane deriving a mass should treat Theorem 6 as the statement it must connect to: the pooled object is `I(S) I(T)`, a count product, and what is missing is the map from a count to a
  mass, not a pairing rule.
- **The signed sector.** A lane pursuing `chi_eta rho Phi` should treat Theorem 7 as a survey of what this construction offers, and a reason to look outside it, not a bound on the search.

## Remaining live routes

1. Larger coarse tori and other geometries: the finite-volume story of Theorem 4 is established across `L = 8` to `128` and nowhere else.
2. A second species, spin, or a dispersion. The fermion note is explicit that none is supplied; the energy density `<c_i^dagger c_j>`, where a mass would come from, is not diagonal and so is not a candidate for
   the lane's `rho` at all.
3. The test-body side: nothing here constrains how a second excitation responds to `phi`.

## Executable claim block

The canonical machine-bound restatement of the seven theorem conclusions.

```text
conditional_on: the supplied fermion law (declared supplier model, derived from no axiom) and the landed weak-field response surface phi = G0 P0 rho
proposal: rho(v) := <n_v>, n_v = (1 - B_v)/2, v in the coarse sublattice 2Z^3, a parity readout of the six records at 2v +- e_a
density_clauses: diagonal, projector (spectrum {0,1}, hence positive), local on exactly six coarse edge sites, phase invariant, 2Z^3 covariant; pairwise commuting
additivity_and_parity: I(empty) = 0 and I(S disjoint-union T) = I(S) + I(T) as an operator identity, 30 random disjoint pairs, open 3x3x3 and 4x4x4; prod_v B_v = +I on both blocks, so N is even-valued and excitations are pair-created
conservation: [N, T_ij] = 0 exactly for all 54 and all 144 edges; 216/2700 and 576/17856 anticommuting/commuting (component, B_v) pairs; bare A_ij B_i does not commute with N
pair_states: open 5x5x5, <n_w> = 1 at v and v' and 0 at the other 123 vertices, N = 2, 1200 of 1200 (string, face) pairs commute, three axis and two non-axis separations
state_vector_crosscheck: open 2x2x2, 12 qubits, dim 4096; unique vacuum; 28 orthonormal occupation eigenstates; sector leakage 4e-16; spectrum = free-fermion pair sums of the 8x8 hop matrix; amplitude identity <n_v> = |psi(v)|^2 and <n_partner> = 1, worst deviation 3e-16 over four amplitudes
response_validation: recomputed 4 pi r G at r = 10 rounds to 0.190/0.432/0.568/0.709/0.782 at N = 32/48/64/96/128, the landed table
response_outcome_one: 4 pi r G at r = L/4 is 0.4065/0.3658/0.3468 at L = 8/12/16, all outside the landed 0.02 band about 0.3266-0.3269
response_outcome_two: 0.3307/0.3275/0.3269/0.3267 at L = 32/64/96/128, inside that band, matching 0.3269 and 0.3267 to four decimals at L = 96 and 128
monopole_coefficient: Richardson 2 G_128 - G_64 gives 4 pi d G_inf(d) = 1.0194/1.0064/1.0009/0.9963 at d = 4/6/8/10
unit_carry: G_coarse^(64)(d) / G_fine^(128)(2d) falls monotonically 2.125 -> 2.0047 over d = 2..16; reading (i) 1/(4 pi d_coarse) = 1/(2 pi |r_fine|), reading (ii) 1/(4 pi |r_fine|); factor 2 declared, not adjudicated
pair_energy: E(d) = <rho, G0 P0 rho> = 2 G(0) + 2 G(d) exactly to 2e-16 on L = 8/12/16
smearing: -Delta_fine = 6(1 - S) so phi_smeared = phi_point - (1/6)(delta_{r,0} - 1/N) exactly, 6e-17 on 16^3/24^3/32^3; star dipole and traceless quadrupole 0; first correction l = 4
bilinearity_and_product: two-particle spectrum = pair sums to 1e-14 on 2x2x2 and 3x3x3, interaction identically absent; |E(r1+r2) - E(r1) - E(r2) - 2<r1, G0 P0 r2>| <= 3e-16 over 15 configurations; the pooled object is the count product I(S) I(T), NOT M_source M_test, and no mass appears
signed_sector: n_v projector => source vector [+1, +1]; least squares against [+1, -1] leaves residual sqrt(2) = 1.414; A_ij and A-strings are orientation-odd but non-diagonal, non-positive, not vertex densities
not_supplied: mass, M_phys, G_Newton, coupling, absolute unit, test-body response law, nonlinear order, any decision between the two unit readings
axioms_amended_status_values_set_registry_entries_created: 0, 0, 0
runner_result: PASS=25 FAIL=0
```

## Proof boundary

The fermion law is a **designed supplier model**, in that note's own words "deriving that form from no axiom and claiming for it no privileged status". Every statement here inherits that: if the supplied law is
not the framework's law, nothing below survives except as a statement about the supplied law. The weak-field response is likewise a supplied surface, bounded in its own note, and this note adds no authority to
it. The `1/(4 pi |r|)` authority is the Maradudin import note; `GRAVITY_CLOSURE_..._2026-06-07` may not be cited for that asymptotic and is not cited for it here.

The **unit carry is not adjudicated**: reading (i) and reading (ii) differ by a factor of two, the factor is measured, and this note declines to choose; any downstream use that needs a
single number must supply that choice itself and say so. Every response statement is at **finite volume**. The coarse tori are `L = 8, 12, 16, 32, 48, 64, 96, 128`, the smearing fine tori are `16^3`, `24^3`, `32^3`, and the unit carry reads a coarse torus against its
own `2L` fine partner; nothing is claimed for infinite lattices or for boxes outside those lists. The extrapolation of Theorem 4 item 4 is a `1/L` Richardson step between two of those sizes, not an infinite-volume theorem, and Theorem 4 item 2 is reported as an outcome precisely so that
the small-box failure is not hidden inside the large-box success.

No mass, no `M_phys`, no `G_Newton`, no coupling and no absolute unit appears; the source/test typing is supplied but the mass-readout identification and the test-body response law are not; nothing nonlinear is
touched. Theorem 7 is scoped to the objects this construction supplies and is not a no-go about the signed sector. The exact groups `A`, `B`, `C`, `F2` and `H` carry no floating point at all; the numerical
groups `D`, `E`, `F1` and `G` each report their residual against a tolerance stated before the run, the response tolerance being the landed window note's own `0.02`, read and quoted in
advance. No axiom is amended, no status is set, and no registry entry is created.

## Review record

An honest auditor should come away with: a conditional identification, not a derivation; seven statements on named finite clusters, five of them exact; one result reported as two outcomes
rather than resolved into one; one factor of two named as open, not absorbed; one negative about this route's signed candidates stated with its scope; and a residual list shorter by one
item, the finite-additive scalar, and longer by one, the unit reading. Nothing here is a fitted number: the one tolerance in the response is quoted from a landed note before the run, and the implementation is validated against that
note's own published table before any new value is reported. The note is self-contained in the sense that matters for replay -- `upstream_dependencies` is empty, every object is declared in "Definitions", the
runner imports nothing from the repository, and the two conditioning surfaces are quoted verbatim with paths rather than consumed as graded rows. Hard landing conditions are a fresh runner and cache pair
closing at `PASS=25 FAIL=0` with runtime under the declared `300` seconds and stdout under `5500` characters, and passing repository pipeline, strict-lint and changed-evidence gates; independent audit remains a
separate lane.
