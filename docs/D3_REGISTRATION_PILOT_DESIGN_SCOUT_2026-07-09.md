# d=3 Registration-Onset Comparator: Pre-commission Design Scout

**Date:** 2026-07-09  
**Status:** design memo only; no measurement, derivation, formation rule, gravity claim, or audit-status claim  
**Decision sought:** identify one laptop-feasible block01 comparator that can test redundancy onset, tolerance stability, and the location of the effective bar on a genuinely three-dimensional finite subgraph of `Z^3`.

## Executive decision

Commission **route C on an open `3 x 3 x 3` qubit cube**, with the centre site as the pointer carrier, the six axial nearest neighbours as the primary disjoint fragment layout, and a uniform nearest-neighbour transverse-field Ising Hamiltonian. Use cubic-orbit exact Krylov evolution, not a `3 x 3 x 2` slab, for the claim-bearing pilot. The interaction is the same ordinary two-body bond on every edge; there is no centre-to-register controlled-copy gate. The `Z` pointer and its conditional imprint arise because the dominant `ZZ` bond term selects and approximately preserves `Z` while acting along all six incident edges.

This is the only route in the present table that combines (a) a full six-direction interior site, (b) non-Clifford onset dynamics, and (c) a plausible laptop calculation. It is not the same thing as deriving the interaction. In particular, `ZZ` privileges a basis. The strongest defensible label is **generic local interaction within a declared Ising-like dynamical class**, not generic over all two-qubit Hamiltonians. The pilot must fail, rather than be retuned after inspection, if approximate pointer conservation and excess fragment imprinting do not coexist over the predeclared parameter sweep.

Route A remains the scientifically clean successor once a controlled 3D gauge-basis method exists. Route B is the useful discrete-gauge cross-check. Route D is only a cheap geometry and analysis-pipeline rehearsal.

## Fixed interpretation and scope

The target synthesis asks a d=3 measurement to decide three empirical questions:

1. Does excess-gated redundancy onset occur with at least two disjoint fragments?
2. Is the attached effective threshold `theta*` insensitive to `delta` over `0.05, 0.10, 0.20`?
3. At headline `delta = 0.10`, is the bar at or above the sparse-window floor `theta = 0.2`?

The supplied quantum-Darwinism (QD) convention is retained. For pointer projectors `P_z` on system `S` and a fragment `F`, record content is the Holevo information of the pointer ensemble,

`chi_Z(S:F) = S(sum_z p_z rho_F^z) - sum_z p_z S(rho_F^z)`.

This is equivalently the system-fragment mutual information after dephasing `S` in the pointer basis. Full quantum mutual information is not substituted, because it would count non-record discord. Fragments must be disjoint; the primary redundancy count additionally rejects pairs with appreciable conditional fragment correlation. No joint fragment whose content is merely a local Gauss/star operator identity is counted as a written record.

The memo treats dynamics, preparation, pointer reading, finite-volume boundary conditions, and the `theta` proxy as declared comparator inputs. The minimal axioms supply `Z^3`, one-site `M_2(C)`, the shape of a fixed covariant nearest-neighbour admissibility rule, and record uniqueness/permanence/additivity; they do not choose this Hamiltonian, a formation rate, a pointer basis, a probability law, or a numerical threshold.

## Route table

The estimates below are back-of-envelope numbers for one ground-state calculation plus one `t = 0:0.1:10` trace at a single coupling, using 12--16 laptop-class performance cores and 32--64 GB RAM. They assume matrix-free operators, streamed observables, and optimized compiled kernels. Python-level bit loops would be much slower. “Reduced dimension” always names the reduction being used; truncation can make the U(1) upper bounds smaller, while spatial fixed points make a naive group-order quotient slightly larger.

| Route | Local dimension and reachable `Z^3` sizes | State space after the stated reduction | Evolution and estimated wall clock per run | What it can and cannot measure |
|---|---|---:|---|---|
| **A. U(1) gauge + staggered fermions** | Matter site `d_m = 2`. Link choices: spin-1/2 quantum link `d_E = 2` as a diagnostic only; rotor `E = -1,0,1`, `d_E = 3`, as the minimum clean integer-flux truncation; and `E = -2,...,2`, `d_E = 5`, as the first cutoff check. Open `2 x 2 x 2` and `3 x 2 x 2` are reachable. The smallest rectangular volume with one site having six distinct, non-wrapped neighbours is open `3 x 3 x 3`, which is not reachable by direct exact evolution. | For an open connected graph, after Gauss reduction and fixed total charge, `dim <= N_matter(Q=0) d_E^(L-V+1)`. Thus `2^3` gives at most `70 x d_E^5`: 2,240 (`d_E=2`), 17,010 (`d_E=3`), 218,750 (`d_E=5`). `3 x 2 x 2` gives at most `924 x d_E^9`: 473,088, 18,187,092, or 1.805 billion. Already `3 x 3 x 2` is at most 3.186 billion for `d_E=2`; `3^3` is of order `C(27,13) 2^28 ~= 5.4e15` even at that smallest link dimension. These are safe upper bounds, not claims of exact retained counts. | Gauge-invariant basis enumeration; Lanczos ground state; sparse/matrix-free Krylov `exp(-iHt)`. `2^3`: seconds to minutes (`d_E=2,3`) or minutes (`d_E=5`). `3 x 2 x 2`: roughly 2--15 min (`d_E=2`) and 1--8 h with substantial memory (`d_E=3`); `d_E=5` and the full `3^3` geometry are out of laptop range. | **Can:** preserve the d=1 charge/E-field ontology, impose Gauss law exactly, repeat excess-over-GS certification, and expose link-cutoff dependence. Six incident E-field links are six candidate channels at an interior site. **Cannot now:** run the smallest full six-direction volume with a cutoff scan. Also, 3D Gauss law fixes the signed sum of six fluxes; it does not make each single link a complete copy. Individual-fragment redundancy must be measured, not inferred from the joint identity. |
| **B. Z2 gauge theory** | Link `d_E = 2`; optional matter qubit `d_m = 2`. Exact non-Clifford physical-basis work reaches open `3 x 3 x 2`; open `3^3` is borderline only with cubic-orbit reduction. Stabilizer-only work reaches far larger boxes. | In a consistent fixed-charge pure-gauge sector, `dim = 2^(L-V+1)`: 32 (`2^3`), 512 (`3 x 2 x 2`), 65,536 (`3 x 3 x 2`), and 268,435,456 (`3^3`). A restricted neutral two-sector matter pointer is roughly a factor two; freely mobile matter is much larger. Proper-cubic orbits reduce a centred `3^3` fixed sector to order `1.1e7` amplitudes per charge sector, subject to an explicit orbit count. | Commuting star/plaquette plus Clifford preparations: exact stabilizer tableau, sub-second to minutes even on large lattices. For generic gauge-invariant electric/magnetic/matter terms: physical-basis Lanczos/Krylov; seconds for the slab, roughly 1--6 h for a symmetry-reduced `3^3` sector if memory layout is successful. | **Can:** check exact Z2 Gauss copying, fragment parity observables, locality, and finite-size geometry cheaply; a non-Clifford version can in principle measure onset and `delta` response. **Cannot:** use a stabilizer result as threshold physics. Clifford information is quantized and onset is an exact circuit-depth jump, so the `delta` sweep and continuous `theta*` location are largely vacuous. As in U(1), a star parity is one collective constraint, not six independently certified records. A dynamical, gauge-neutral matter pointer must be specified without freezing in the answer. |
| **C. Generic-interaction qubit lattice** | Site `d = 2`. Open `3 x 3 x 2` has 18 qubits and is a fast methods check, but has no site with distinct `+z` and `-z` neighbours. Open `3^3` has 27 qubits and is the minimum claim-bearing box. A larger full box is not exact-laptop work. | Raw dimensions are `2^18 = 262,144` and `2^27 = 134,217,728`. For the isotropic open cube and a centre-symmetric preparation, quotienting the 27-bit basis by the 24 proper cubic rotations gives exactly **5,605,504 spatial orbits**. Global spin-flip sectors may be stored separately, but the proposed off-axis preparation uses both and does not provide another net factor of two. | Matrix-free exact Lanczos and Krylov in the cubic-orbit basis; local Pauli expectation contractions give one- and two-qubit conditional density matrices without expanding every sampled state. Slab: about 10 s--3 min. `3^3`: about 1--4 h per `(h/J, preparation)` point after basis construction; raw `2^27` work is more like 8--30 h and can exceed comfortable Krylov memory. | **Can:** measure all three requested outputs on the minimum non-wrapped 3D geometry, including a genuine non-Clifford onset, QD Holevo fragments, conditional independence, locality, the full `delta` sweep, and a frozen two-qubit-purity `theta` map. **Cannot:** claim gauge-native copying, derive the interaction, establish the thermodynamic limit, or prove literal permanence in a 27-qubit closed system. “Generic” survives only in the restricted sense that one uniform standard bond acts everywhere; `ZZ` still selects `Z`. |
| **D. d=3 constraint-propagation lift** | Cheapest version: one classical bit per site on open `3^3`, evolved by a fixed reversible nearest-neighbour parity rule over `GF(2)`. A seven-site axial cross is an even cheaper wiring test, but is all boundary and is not a volume. Linear updates scale easily to `9^3` and beyond. | Raw `3^3` configurations number `2^27`, but a centre-symmetric disturbance has four site orbits (centre, six faces, twelve edges, eight corners), so the cheapest shell model has only `2^4 = 16` symmetric configurations; equivalently evolve a 27-bit vector with a `27 x 27` binary propagator. | Exact bit-matrix propagation or exhaustive 16-state shell enumeration; much less than 1 s per trace, with large parameter sweeps in seconds. | **Can:** validate axis/octant fragment bookkeeping, first-hit logic, causal shell ordering, GS/baseline subtraction code, and finite-wrap diagnostics. **Cannot:** demonstrate quantum pointer selection, QND persistence, generic Hamiltonian copying, non-Clifford onset, or a physically comparable `theta*`. If the rule explicitly fans a centre bit into neighbours, it is precisely the hand-supplied copy mechanism the decisive campaign forbids. |

### Route-A truncation and geometry note

The `d_E = 2` quantum-link option is not a convergence proxy for the integer rotor unless its background-charge and Gauss conventions are separately shown compatible. A claim-bearing U(1) result would need at least `E_max = 1` versus `E_max = 2`, with negligible probability on `|E| = E_max`, stable event times, and stable `theta*`. That check is affordable on `2^3` but not on the first full branching volume.

Open `2^3` is three-dimensional as a graph, but every vertex is a corner of degree three. A thickness-two periodic direction aliases the `+` and `-` neighbours and cannot supply independent opposite fragments. Open `3^3` is therefore the smallest rectangular `Z^3` subvolume with a centre and all six distinct axial exits. A seven-site axial cross has the six exits but no bulk, no buffer, and boundary conditions at every register; it is a geometry surrogate, not the requested volume measurement.

## Fragment geometry for route C

Label the open cube by coordinates `(x,y,z) in {-1,0,1}^3` and put the pointer carrier `S` at `(0,0,0)`.

### Primary six-axis layout

The six finest disjoint candidate registers are

`F_(+x), F_(-x), F_(+y), F_(-y), F_(+z), F_(-z)`,

each consisting of the one qubit at the corresponding axial nearest neighbour. These are six candidate channels, not six registers by assertion. The measured redundancy is the size of the largest certifying subset whose members are pairwise conditionally independent within a frozen tolerance. Cubic symmetry leaves only two pair types to evaluate: opposite-axis and orthogonal-axis.

For certifying fragments `F_a,F_b`, define

`C_ab(t) = I(F_a:F_b | Z_S)`

on the state dephased in `Z_S`. Take `eta_ind = 0.02 bit` and count a pair together only when `C_ab <= eta_ind`. This makes `R >= 2` a statement about two recoverable, disjoint, conditionally decoupled imprints rather than two views of one correlated environment block. The value `0.02 bit` is predeclared to match the d=1 excess floor; it is a comparator convention, not an axiom-derived number.

### Octant cross-check

`Z^3` also offers eight strict octants. On `3^3` their non-plane representatives are the eight corner qubits `(s_x,s_y,s_z)` with each `s_mu in {-1,+1}`. They form a second, disjoint-within-layout eight-fragment test at Manhattan distance three. Axis and octant counts are **alternative layouts** and must not be added to claim `R = 14`: paths to the corners pass through the axial/edge shells and can share mediators. The octant panel is useful for measuring the late register front and detecting boundary recurrences, not for replacing the six-axis headline.

### Minimum size and boundary qualification

In the purely combinatorial sense, `R >= 2` can be written on any open graph with a degree-two vertex, and an open `2^3` corner has three disjoint neighbours. That is not the campaign's question: it privileges a corner, has no opposite directions, and makes all registers boundary registers. For a cubic-covariant interior pointer with distinct `+/-` directions and no periodic identification, **open `3^3` is minimal**. Periodic extent two is invalid because opposite neighbours coincide; a `3 x 3 x 2` slab is therefore methods-only.

The `3^3` cube still has no radial buffer: each axial register lies on a face. A `5^3` cube would be the minimum full box with two-link axial rays and one extra shell before the boundary. Consequently block01 may establish short-time `R >= 2` onset, but it cannot establish macroscopic permanence or a volume-stable redundancy plateau. The positive gate requires onset before the measured outward-and-return front can contaminate the centre; later samples are reported as finite-volume persistence diagnostics only.

### Excess-over-GS baseline and `theta*`

For each Hamiltonian parameter point, compute a deterministic same-Hamiltonian ground state and cache, for every candidate fragment, `chi_GS(Z_S:F)`, the ground-state conditional-fragment correlations, and the six centre-bond purities. Feeding that stationary state through the event finder must return zero events for every `delta`, because the excess term subtracts each cached value from itself.

For a dynamical state, a fragment certifies at tolerance `delta` only when all of the following hold:

1. `H(Z_S) >= 0.05 bit`;
2. `chi_Z(S:F) >= (1-delta) H(Z_S)`;
3. `Delta chi_F = chi_Z(S:F) - chi_GS(Z_S:F) >= 0.02 bit`;
4. it can be included in a pairwise-independent subset under `C_ab <= 0.02 bit`.

Registration is the first sampled time at which the largest such subset has `R_ind >= 2`. No adjacent fragments are joined to manufacture certification, and no negative excess is clipped.

Attach to each onset the GS-subtracted, unnormalised two-qubit linear entropy averaged over the six equivalent centre bonds,

`theta(t) = (1/6) sum_a {[1-Tr rho_(S,F_a)(t)^2] - [1-Tr rho_(S,F_a,GS)^2]}`.

Thus `theta* = theta(t*)`. This retains the d=1 map's `GS-subtracted (1-purity)` form and its two-site local dimension, while avoiding the arbitrary choice of one spatial axis. There is no rescaling to `[0,1]`, no fit between samples, and no post-hoc change if the bar falls below `0.2`. The mapping is a frozen comparator convention, not an identification derived from the axioms.

## Block01 pilot recommendation

### Model, size, and preparation

Use route C on the open 27-site cube with energy unit `J = 1`:

`H_lambda = -J sum_<ij> Z_i Z_j - lambda J sum_i X_i`,

with the same bond and field on every site/edge in the finite box and the predeclared sweep

`lambda = h/J in {0.05, 0.10, 0.20}`.

Evolve at `Jt = 0:0.1:10`. The headline onset must occur by `Jt <= 1`; later times expose loss, recurrence, and the outward register profile rather than rescue a late first hit. Open boundaries are fixed before the run. No centre coupling is changed, no fragment-dependent field is added, and no term is turned off after a register is written.

Use one spatially symmetric, uncorrelated, generic off-axis preparation,

`|psi_0> = |n>^(x27),  n = (1,1,1)/sqrt(3)` on the Bloch sphere,

and designate only the centre qubit as `S` in the analysis. This state has no initial intersite record and has nontrivial `Z` entropy without putting the environment in a specially chosen `Z` eigenstate. It is nevertheless a supplied receptive preparation. A positive pilot would show formation under that declared preparation, not formation for arbitrary states.

The Hamiltonian has exactly the nearest-neighbour-rule shape named by Admissibility and is covariant in the bulk under translations and proper cubic rotations. Admissibility does not supply this Hamiltonian. The reason it can write a `Z_S` record is dynamical: conditional on `Z_S = +/-1`, each incident `ZZ` bond gives the neighbour a different local phase evolution. That mechanism is present on every bond, not installed as a centre-controlled recording gate. Equally, it is fair review criticism that the interaction is diagonal in `Z`; route C is not basis-neutral.

### Observable set

At every sampled time, stream the following quantities from symmetry-adapted local Pauli expectations:

- `p_z(t)` and `H(Z_S,t)` for the centre pointer, plus total-variation pointer drift from `t=0`;
- `chi_Z(S:F,t)` and `Delta chi_F(t)` for all 26 exterior one-site fragments, grouped by Manhattan distance and cubic orbit, with the six axial neighbours retained individually for `R_ind`;
- `I(F_a:F_b | Z_S)` for the opposite-axis and orthogonal-axis pair classes;
- `R_ind(delta,t)` for `delta = 0.05,0.10,0.20`, the first-hit time, and the number of consecutive samples for which `R_ind >= 2` remains true;
- the six centre-bond two-qubit density matrices and `theta(t)` defined above;
- the local excess bond energy/activity profile, the first sampled maximizer of `sum_F Delta chi_F`, and `xi_reg`, the largest Manhattan distance with `Delta chi_F >= 0.02 bit` at that maximizer;
- ground residual, Krylov norm error, symmetry-orbit normalization, entropy bounds `0 <= chi <= H(Z_S)`, and agreement of symmetry-related observables.

The one- and two-qubit conditional states require only local Pauli expectation values. The 134-million-component raw state need not be materialized at every time. A full-Hilbert `3 x 3 x 2` calculation must reproduce the same observable code paths before the orbit-reduced `3^3` run, but the slab result carries no physics conclusion.

### Exact d=1 gate analogs

The output should preserve the d=1 five-check structure and first-sampled-hit convention.

**CHECK-01 — GS control and excess certification.** For each `lambda`, compute the same-Hamiltonian ground state, feed its stationary trace through the identical event routine, and require event counts `[0,0,0]` in `delta` order. Certification uses `chi - chi_GS >= 0.02 bit`, not raw `chi`. Also report the generic product state's `t=0` values, which must have zero intersite `chi` to numerical tolerance.

**CHECK-02 — demolition panel.** Use the same centred Frobenius normalization as d=1,

`C_F(H,O) = ||[H,O]||_F / (||H||_F ||O-Tr(O)I/d||_F)`.

Across centre, face, edge, and corner site classes, require `max C_F(H,Z_i) < min C_F(H,X_i)`, and report the corresponding `Y_i` values. At every headline onset require the `Z_S` population drift to be at most `0.10` in total variation. Run the same record analysis with `X_S` declared as pointer; the demolition control passes only if it has no excess-gated `R_ind >= 2` onset by `Jt=1`. The commutator ordering alone is not record sufficiency; it is the pointer-selection panel.

**CHECK-03 — events plus locality.** At headline `delta=0.10`, every predeclared `lambda` must have a six-axis event with `R_ind >= 2` by `Jt=1`. No Manhattan-distance-two or -three singleton may certify before the axial onset. Report `Delta chi` by shell and `xi_reg` exactly even when no event occurs. A first hit followed by immediate loss is labeled `TRANSIENT-ONSET`; require at least three consecutive samples (`0.2/J`) with `R_ind >= 2` for the pilot's finite-time persistence flag. That flag is not a claim of permanent storage.

**CHECK-04 — `delta` insensitivity.** For each `delta`, take the median `theta*` over the three `lambda` values. Missing onset at any `(lambda,delta)`, a nonpositive/nonfinite median, or

`max_delta median(theta*) / min_delta median(theta*) >= 1.5`

fails the check. The headline remains `delta=0.10`; no tolerance is selected after viewing the result.

**CHECK-05 — bar location.** At `delta=0.10`, print each `lambda`'s `theta*`, the median and range, and label each eventful case `inside` when `theta* >= 0.2` and `BAR-BELOW-WINDOW` otherwise. No event is `unavailable`, not zero. A bar below `0.2` is a substantive measurement, not machinery failure. The campaign target is answered only if CHECK-03 and CHECK-04 are meaningful; CHECK-05 then locates rather than defines the bar.

The numerical machinery gate should separately require ground residual `<= 1e-8`, state-norm error `<= 1e-9`, QD entropy-bound error `<= 1e-9`, cubic-equivalent observable disagreement `<= 1e-9`, and, on changing to `Delta(Jt)=0.05`, an onset-time shift no larger than `0.1/J` and a `theta*` shift no larger than 5%. Physics absence must return `BAR-NOT-PINNED`, not `MACHINERY-FAIL`.

### Estimated run budget

Allow 1--3 h once to construct and validate the 5,605,504-orbit basis, then approximately 1--4 h per `lambda` for ground state plus streamed Krylov evolution. The three-point claim-bearing sweep is therefore an overnight **6--18 h** laptop job, with peak memory expected in the 16--40 GB range depending on Krylov depth and whether transitions are cached. The full-Hilbert slab validation and null controls should add less than 10 min. These figures are estimates; a Python-only orbit matvec could miss them by an order of magnitude and should be treated as an implementation failure, not a physics result.

### Two largest pilot risks and their signatures

1. **The QND/writeability window may be empty or fine-tuned.** At small `lambda`, the ordered GS can already carry nearly all available `Z_S` information, leaving no `0.02-bit` excess; at larger `lambda`, `Z_S` may move before neighbours certify. The signature is a direct tradeoff: `chi_GS/H(Z_S)` near one at the low end, then pointer drift above `0.10`, loss of commutator separation, or an `X`-pointer demolition event at the high end. Onset only at one narrow `lambda` or only in the commuting `lambda -> 0` limit does not support “generic local interaction.” The sweep is not retuned around that failure.
2. **Cubic symmetry may mimic copy multiplicity while the fragments share one correlated channel or a boundary return.** The signature is all six singletons crossing together while opposite/orthogonal `I(F_a:F_b|Z_S) > 0.02 bit`, or a first hit at/after the distance-two front and followed by a rapid recurrence. Such a run has raw `R=6` but `R_ind<2`, or is labeled `BOUNDARY-CONTAMINATED`; it does not establish redundancy onset.

## What would kill it

“Survives” below means that a route remains a scientifically distinct way to test the issue; it does not predict that the surviving route will pass.

| Failure mode | Detection signature and consequence | Routes that still survive |
|---|---|---|
| **No quasi-conserved pointer without basis/anisotropy tuning** | For route C, `C_F(H,Z)` is not separated from alternatives, `Z` populations move by more than `0.10` before any event, or positive onset exists only as `lambda -> 0`. This kills the claim that an ordinary non-Clifford local interaction both selects and writes the pointer over an open parameter interval. | **A** and **B** retain exact gauge charge/parity pointers. **D** cannot answer the pointer question. |
| **Ground-state correlations consume the excess budget** | `chi_GS/H(Z_S)` is already near one, so no fragment can gain `0.02 bit` even though raw `chi` is large. Raw certification must not replace excess certification. This kills the declared C preparation/parameter block; it is not evidence of new writing. | **A** and non-Clifford **B** remain alternative dynamics, though they must use the same excess test. **D** can test subtraction logic only. |
| **Onset is slower than reachable clean time** | `Delta chi` and `R_ind` are still rising at `Jt=1`, but the information front reaches the face/edge shells before first hit. Extending `T` on the same `3^3` cube would mix slow formation with boundary return and cannot rescue block01. A flat profile at numerical floor is stronger evidence for no channel; a rising profile is an unresolved horizon. | A larger tensor-network version of **C** could survive after an error-controlled methods study. Stabilizer **B** and **D** scale, but are too rigid/classical to settle non-Clifford threshold physics; exact **A** does not presently reach the needed volume. |
| **Finite-size wrap, face, or recurrence contamination** | Opposite neighbours coincide (any extent-two periodic route), onset follows an outward-and-return front, or event time/`theta*` changes materially between open boundary variants. The affected finite-volume result is killed. | **D** survives as a scalable geometry diagnostic. **A**, **B**, or **C** survive only on a larger non-aliased volume or with a controlled finite-size method; none of the small exact versions proves volume stability. |
| **Two “records” are not conditionally independent** | At every raw `R >= 2` hit, all candidate pairs have `I(F_a:F_b|Z_S) > 0.02 bit`. This is one correlated environmental block viewed twice, so route C block01 fails the permanence-grade criterion. | **A** or **B** may survive with separated flux patches or concentric surfaces on larger volumes, but the Gauss/star identity itself is not enough. **D** only debugs the fragment counter. |
| **`theta*` depends strongly on `delta`** | A missing event in the sweep or median factor `>= 1.5` makes the tolerance a dial. The selected comparator does not deliver the required effective threshold even if a headline event exists. | The other dynamical routes **A**, **B**, and **C** remain candidates in principle; **D** cannot establish a physical threshold. No tolerance may be dropped post hoc. |
| **The bar is robust but below `0.2`** | CHECK-03 and CHECK-04 pass, but headline `theta* < 0.2`. This does **not** kill the measurement. It kills compatibility of this comparator's frozen bar with the stated sparse window and must be reported as `BAR-BELOW-WINDOW`. | Any independent physical route may test model dependence. **A** has the strongest continuity with the d=1 proxy. A new normalization chosen to move the bar does not survive. |
| **The two-site purity map is judged non-portable across models** | Review finds that averaging qubit centre bonds, despite matching the d=1 two-site `1-purity` form and dimension, does not carry the same deposition meaning. Route C could still measure onset and `delta` stability, but it could not answer the sparse-window location question. | **A** survives best because it retains the staggered gauge cell and E-field substrate. **B** needs its own predeclared transfer map. **D** does not survive. |
| **U(1) link cutoff controls the event** | Boundary-flux weight is appreciable, or onset/`theta*` shifts between `E_max=1` and `2`. A route-A result at that size is a truncation artifact. | **B** and **C** have no electric-link cutoff. **D** remains non-quantum. |
| **Z2 onset exists only in the Clifford/stabilizer limit** | Information jumps in exact integer units at circuit depth and the `delta` sweep is automatically flat; adding a generic gauge-invariant non-Clifford term removes the effect. This kills route B as a threshold-location measurement. | **A** and **C** retain continuous-time non-Clifford onset physics. **D** does not. |
| **No finite closed system shows durable hold** | `R_ind` repeatedly forms and erases, with no interval longer than the predeclared three samples. The pilot may report a transient first hit but not permanence-grade storage. | Larger/fresh-fragment or effectively open versions of **A**, **B**, or **C** may survive. **D** can impose persistence by rule but would beg the physical question. |

## Commission decision rule

Proceed with the route-C block01 only if the orbit-basis slab cross-check passes and the exact `3^3` resource estimate fits memory without reducing the fragment or time grids. A positive scout result requires CHECK-01 through CHECK-04, `R_ind >= 2`, the finite-time persistence flag, and clean locality. CHECK-05 then reports `inside` or `BAR-BELOW-WINDOW`; either is an honest location result. If CHECK-03 or CHECK-04 fails, return `BAR-NOT-PINNED`. If only raw `R` passes while conditional independence fails, return `CORRELATED-FRAGMENTS`, not a weaker redundancy claim.

Regardless of outcome, do not describe the result as deriving records, the Hamiltonian, the pointer basis, or the numerical bar from the four axioms. The strongest positive statement would be: **in this declared finite d=3 comparator and under the supplied QD reading, a uniform local Ising-class interaction exhibits excess-gated, conditionally independent redundancy onset with the reported tolerance stability and bar location.**

## Source-convention ledger

This scout uses only the four commissioned repo sources:

- `docs/REGISTRATION_BAR_DERIVATION_SYNTHESIS_2026-07-09.md` for the three d=3 deliverables and the no-formation-rule boundary;
- `scripts/registration_redundancy_onset_2026_07_09.py` for same-coupling GS excess, `delta = [0.05,0.10,0.20]`, `eps_exc = 0.02 bit`, `H_floor = 0.05 bit`, first-sampled onset, `R >= 2`, the `< 1.5` sensitivity factor, and GS-subtracted `1-purity` attachment;
- `docs/RECORD_FORMATION_POINTER_NON_DEMOLITION_DYNAMICS_CONSTRAINT_BOUNDED_THEOREM_NOTE_2026-06-05.md` for the dephased-pointer/Holevo record convention, pointer non-demolition necessity, locality/conditional independence, demolition, and finite-system persistence cautions;
- `docs/MINIMAL_AXIOMS_2026-06-29.md` for the `Z^3` nearest-neighbour geometry, one-site qubit algebra, Admissibility-rule shape, and the explicit separation between those axioms and any dynamics or formation rule.

All state-space counts, timing ranges, Hamiltonian choices, fragment-independence tolerance, and finite-volume gates in this memo are design estimates or proposed conventions. They are not measurements.
