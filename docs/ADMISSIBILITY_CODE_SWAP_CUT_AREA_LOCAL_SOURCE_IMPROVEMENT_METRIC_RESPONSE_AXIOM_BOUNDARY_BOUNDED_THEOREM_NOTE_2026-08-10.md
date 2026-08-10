---
claim_id: admissibility_code_swap_cut_area_local_source_improvement_metric_response_axiom_boundary_bounded_theorem_note_2026-08-10
claim_type: bounded_theorem
claim_scope: "On a supplied finite q-regular binary sector, the code-symmetric compatible action uN+vE with u=-(q/2)v is exactly one-half log B times the occupied/unoccupied edge cut. On a finite periodic cubic quotient the anisotropic code-symmetric family is one-half the sum of directional log B_a times directional cut area; its one-site action increment is the exact cut-area increment, its cut edges dualize to a closed cubical two-chain, and its directional log-partition derivatives are cut means and covariances. Endpoint-local source allocations form an exact one-parameter improvement family: all have the same total action, code swap fixes the equal-endpoint member, and under a supplied graph-Poisson response their potentials differ only by a local occupation contact term. Explicit covariant metric extensions agree on the fixed-background action but have different diagonal and offdiagonal first variations, so that fixed-background scalar law and global cubic covariance do not uniquely determine a local metric derivative or conserved stress. No physical log-law license, action unit, metric family, source convention, dynamics, stress tensor, field equation, gravity, axiom necessity, or adoption is proved."
upstream_dependencies:
  - minimal_axioms
  - scale_reference_primitive
  - admissibility_ising_action_record_readout_pair_resource_response_axiom_boundary_bounded_theorem_note_2026-08-10
  - gravity_weak_field_source_response_bridge_bounded_theorem_note_2026-06-11
  - universal_gr_stress_ward_transverse_seagull_bounded_theorem_note_2026-06-08
  - observable_principle_source_coupled_local_action_admission_candidate_note_2026-05-21
runner: scripts/admissibility_code_swap_cut_area_local_source_improvement_metric_response_axiom_boundary_2026_08_10.py
---

# Code-Symmetric Cut Area, Local Source Improvement, And Metric-Response Boundary

**Date:** 2026-08-10
**Type:** bounded theorem and axiom-consequence map
**Scope:** supplied finite binary sectors, with the six-regular periodic cubic
specialization and compatible action inherited from the preceding block.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[admissibility_code_swap_cut_area_local_source_improvement_metric_response_axiom_boundary_2026_08_10.py](../scripts/admissibility_code_swap_cut_area_local_source_improvement_metric_response_axiom_boundary_2026_08_10.py)

## Result Up Front

The code-symmetric action found in the preceding block has an exact geometric
form that was not exposed there. Let `X` be the occupied set, let `N=|X|`, let
`E` count occupied/occupied edges, and let `|delta X|` count edges with exactly
one occupied endpoint. On every six-regular graph,

    6N=2E+|delta X|,

so

    3N-E=|delta X|/2.

The code-symmetric probability relation is `A B^3=1`. With
`S_stat=-log pi` modulo constants, it follows exactly that

    S_stat=(log B)/2 |delta X|.

Thus the compatible action on this line is a **statistical cut-area action**.
For `B>1`, it penalizes occupied/unoccupied interface area; for `0<B<1`, it
favors it. This is a statement about a finite probability law, not yet a
physical surface tension.

The local rule acquires the same interpretation. If an empty site has `k`
occupied neighbors, adding it changes the cut by

    Delta_i |delta X|=6-2k,

and changes the action by

    Delta_i S_stat=(3-k) log B.

The compatible local log odds are the negative of that increment. The
apparently independent conditional rule and global action are therefore the
local and global faces of one exact cut functional.

On a periodic cubic quotient, each cut edge is dual to one elementary
plaquette. Those plaquettes form the boundary of the occupied dual cubes, so
they are a closed cubical two-chain. Directional couplings give

    S_stat=(1/2) sum_a (log B_a) C_a,

where `C_a` is the number of cut edges parallel to axis `a`. The derivatives
of the finite log partition function are

    partial_(log B_a) Psi = -(1/2) E[C_a],
    partial_a partial_b Psi = (1/4) Cov(C_a,C_b).

At the isotropic point, cubic symmetry forces equal directional means and the
usual one-bulk/two-diagonal-shear response split. This is an exact cut-
orientation susceptibility. It is not a physical stress tensor.

The local source question is subtler. Every cut edge can be divided between
its two endpoints with a parameter `theta`. All such allocations sum to the
same global action, but their local densities differ by a graph-Laplacian
improvement:

    rho_i^(theta)-rho_i^(1/2)
      =[(log B)/2](theta-1/2) (L x)_i.

Code swap sends `theta` to `1-theta`, so equal endpoint sharing is the unique
code-swap-even member of this declared allocation family when `B != 1`.
If the graph-Poisson equation is separately supplied, then in zero-mean gauge

    phi^(theta)-phi^(1/2)
      =[(log B)/2](theta-1/2) P0 x.

The ambiguity becomes a local contact improvement: its edge gradient vanishes
away from the cut. The exterior weak-field response is unchanged within this
family, while local contact/source values are not.

Finally, a fixed-background probability law does not determine a derivative
with respect to a metric variable it never contained. Two explicit local,
translation-covariant, proper-cubic tensor extensions agree exactly at the
background and have different first variations, including different
offdiagonal content. A geometry-dependent law family or source-coupling
convention is therefore a real additional bridge. Global cubic covariance by
itself does not imply a local Ward identity or stress conservation.

No canonical axiom is edited, and the fixed TOE percentages do not move.

## Machine Status And Trace

~~~yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The regular-graph cut identity, cubic dual-surface form, local flip law, directional covariance response, endpoint source-improvement family, conditional Poisson contact identity, and fixed-background metric-extension nonuniqueness are exact; physical action licensing, local metric family, conserved stress, field dynamics, gravity, and axiom adoption remain open."
trace_class: upstream_support
target_claim_id: admissibility_cut_surface_to_conserved_physical_metric_source_bridge
target_blocker_text: "turn the compatible pair action and site/edge response into a physically licensed, locally conserved source/stress tensor with metric or curvature response"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
campaign_native_target_reachability: advances
next_trace_action: "Test whether the code-swap-even cut density admits a source-contained local geometry family and Ward identity, or retain the exact geometry-family clause below as the unresolved physical bridge."
conditional_surface_status: "the code-symmetric compatible action is an exact closed dual cut-surface functional with directional covariance response; endpoint-local sources differ by a Laplacian contact improvement; no physical stress or metric equation is selected"
hypothetical_axiom_status: "a weak equal-endpoint source convention and a stronger geometry-family log-law clause are sufficient bridge shapes; neither is adopted, proved necessary, or claimed minimal"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
~~~

## Exact Target Contract

| Contract field | Block-10 value |
|---|---|
| target statement | classify the code-symmetric compatible action geometrically and determine exactly what remains before it can be a conserved physical metric source |
| quantifiers/domain | arbitrary finite regular binary graph for the cut theorem; finite periodic cubic quotients of side at least three for directional geometry |
| allowed premises | current four axioms, approved scale primitive as units only, Block-9 compatible action, elementary finite graph/probability algebra, and explicitly conditional weak-field composition |
| forbidden weakenings | calling cut count stress, covariance a metric Hessian, complement symmetry mass, or a supplied Poisson solve derived gravity |
| required edge cases | empty/full phases, `B=1`, both signs of `log B`, anisotropic axes, endpoint allocations, complement, and offdiagonal metric extensions |
| completion witness | general identities, exact cubic/K7/orbit fixtures, source-improvement proof, two inequivalent covariant metric extensions, and N1--N8 |
| outcomes not counting as closure | a name-level surface-tension analogy, one chosen source allocation, one supplied metric deformation, or a finite response renamed gravity |

## 1. Regular-Graph Cut Theorem

Let `G=(V,E_G)` be a finite `q`-regular graph and let
`x in {0,1}^V`. Define

    X={i:x_i=1},
    N=|X|,
    E_X=|{<ij> in E_G:i,j in X}|,
    C_X=|delta X|.

Counting the edge-ends incident on `X` gives the exact identity

    qN=2E_X+C_X.                                      (1)

The compatible action is

    S_stat=uN+vE_X,
    u=-log A,
    v=-log B.

Complementing every bit maps

    N -> |V|-N,
    E_X -> |E_G|-qN+E_X.

Therefore code-swap invariance modulo a configuration-independent constant is
equivalent to

    u=-(q/2)v,

or, on the probability side,

    A B^(q/2)=1.

Substituting (1) gives the exact theorem

    S_stat=v(E_X-qN/2)
          =-(v/2)C_X
          =(log B/2)C_X.                              (2)

The additive constant can be chosen so that both uniform configurations have
zero action. Complementation leaves `C_X` unchanged, so it leaves (2)
unchanged exactly.

### Consequences

1. `B>1` gives a positive statistical surface coefficient.
2. `0<B<1` gives a negative coefficient and favors larger cuts.
3. `B=1` erases the action and is the trivial intersection already isolated
   in Block 9.
4. For every complement-invariant normalized law,

       E[x_i]=1/2,
       E[N]=|V|/2.

   This is ensemble symmetry, not a claim that a realized configuration has
   half occupancy.
5. The cut action is complement even. It cannot be an affine calibration of
   the complement-odd volume variable `M=2N-|V|`: the empty and full
   configurations both have `C_X=0` but have opposite `M`.

The last point is a typed distinction only. It does not show that physical
matter must be a volume source, or that an interface cannot gravitate.

## 2. Periodic Cubic Directional Form

Take `V=(Z/LZ)^3` with `L>=3`, so the nearest-neighbor quotient is simple and
six-regular. Split occupied internal edges and cut edges by their unsigned
axis:

    E_X=E_1+E_2+E_3,
    C_X=C_1+C_2+C_3.

Each directional subgraph is two-regular, hence

    2N=2E_a+C_a,
    E_a-N=-C_a/2.                                    (3)

For positive directional parameters `B_a`, consider

    w(X)=A^N product_a B_a^(E_a).

Code swap is invariant modulo constants exactly when

    A product_a B_a=1.

Writing `t_a=log B_a`, the action becomes

    S_stat=sum_a t_a C_a/2.                          (4)

The isotropic specialization `t_1=t_2=t_3=log B` is (2).

### Local variation

Let `k_a in {0,1,2}` be the number of occupied neighbors of an empty site in
the two directions parallel to axis `a`. Adding that site removes `k_a` cut
edges and creates `2-k_a` cut edges in that direction, so

    Delta_i C_a=2-2k_a,
    Delta_i S_stat=sum_a t_a(1-k_a).                 (5)

The local weight odds are

    A product_a B_a^(k_a)
      =exp[-Delta_i S_stat].

In the isotropic case this reduces to

    Delta_i C_X=6-2k,
    Delta_i S_stat=(3-k)log B,
    odds=B^(k-3).

Thus Block 8's affine-logit rule is exactly the discrete first variation of
the cut area on the code-symmetric line.

## 3. Closed Dual Surface And Directional Response

Associate to every primal nearest-neighbor edge its perpendicular dual
plaquette. A cut edge contributes its dual plaquette. Equivalently, take the
union of dual cubes centered on occupied sites; its cubical boundary consists
exactly of those plaquettes.

Because the boundary of a boundary is zero, the cut plaquettes form a closed
cubical two-chain. In elementary primal language, every plaquette perimeter
contains an even number of cut edges: the four binary differences telescope
modulo two.

This is a finite chain identity. It does not assert smoothness, a continuum
area theorem, a worldvolume history, or a physical membrane.

Define the global cut-orientation tensor

    Q(X)=sum_a C_a e_a e_a^T                         (6)

with diagonal entries `C_a`. Under every proper cubic rotation `R`,

    Q(RX)=R Q(X) R^T,
    Tr Q=C_X.

For

    Psi(t)=log sum_X exp[-(1/2)sum_a t_a C_a(X)],

finite differentiation gives

    partial_a Psi=-(1/2) E[C_a],
    partial_a partial_b Psi=(1/4)Cov(C_a,C_b).        (7)

The Hessian is positive semidefinite. At `t_1=t_2=t_3`, cubic symmetry forces
the mean vector to be proportional to `(1,1,1)` and the covariance matrix to
have one diagonal value and one offdiagonal value. It decomposes into:

- one bulk/trace mode; and
- two traceless diagonal-shear modes.

The axis-cut carrier has no offdiagonal `xy`, `xz`, or `yz` coordinate. That
does not prove physical shear response vanishes. It says only that such a
coordinate is absent from this declared carrier; a geometry extension may add
one.

### Exact fixtures

On the orbit of a three-site wrapping line in the `L=3` quotient, the three
directional cut vectors are

    (0,6,6), (6,0,6), (6,6,0).

The orbit mean is `(4,4,4)` and its exact covariance has diagonal `8` and
offdiagonal `-4`. The bulk eigenvalue is zero because total area is fixed on
the orbit; the two diagonal-shear eigenvalues are `12`.

On the degree-six graph `K_7` at `B=4`, exact enumeration gives

    Z=4663/2048,
    E[C]=3948/4663,
    Var(C)=122288880/21743569,
    P(X=empty or full)=4096/4663.

Consequently the one-parameter cut susceptibility is

    partial_t^2 Psi=Var(C)/4=30572220/21743569.

These rational numbers are a finite fixture, not a cubic-universe prediction.

## 4. Endpoint Source Allocation And Improvement

Equation (2) fixes a global scalar. A local source density still needs an
allocation rule. For `theta in [0,1]`, give a fraction `theta` of every
cut-edge action to its occupied endpoint and `1-theta` to its empty endpoint.
With `k_i=sum_(j~i)x_j` and `t=log B`, define

    rho_i^(theta)
      =(t/2)[theta x_i(6-k_i)
             +(1-theta)(1-x_i)k_i].                 (8)

Every cut edge contributes once in total, so

    sum_i rho_i^(theta)=t C_X/2=S_stat              (9)

for every `theta`.

Let the positive graph Laplacian be

    (Lx)_i=6x_i-sum_(j~i)x_j.

Direct subtraction yields

    rho_i^(theta)-rho_i^(1/2)
      =(t/2)(theta-1/2)(Lx)_i.                      (10)

Thus the endpoint family is one exact Laplacian-improvement line. Code swap
maps

    rho^(theta)(1-x)=rho^(1-theta)(x).

For `t != 0`, requiring the **local density itself** to be code-swap even
selects `theta=1/2` inside this family. This is a conditional uniqueness
statement: it assumes endpoint locality, count-once allocation, and local
code-swap evenness. More general local improvements remain possible.

### Conditional weak-field composition

The weak-field source-response packet takes a supplied scalar source and
solves

    L phi=P0 rho,

where the same graph Laplacian is inverted on the zero-mode-removed sector.
If one conditionally inserts (8), then (10) gives

    phi^(theta)-phi^(1/2)
      =(t/2)(theta-1/2)P0 x.                        (11)

This follows from `L^+ L=P0`. The right side is constant within each binary
phase, so its edge gradient vanishes on every non-cut edge. Within the
endpoint family:

- the total source is identical;
- the exterior/bulk force away from the interface is identical; and
- the contact value at the interface can differ.

This is an improvement/contact theorem. It is not a derivation that `rho` is
the gravitational source, that `L` is the physical field operator for this
law, or that the force is realized.

## 5. Why Fixed-Background Covariance Does Not Select Stress

The current law is given on one fixed cubic graph. A stress tensor normally
requires a derivative with respect to a local geometric source. That derivative
cannot be recovered from a single value of a function without specifying its
extension away from that value.

The abstract statement has a concrete local witness. Let `h_i` be a supplied
symmetric tensor source. Define the local equal-endpoint cut tensor

    q_i=sum_(a,+/-) [1_(x_i != x_(i+/-a))/2] e_a e_a^T.

It is local and proper-cubic covariant. Also define the centered environment
gradient

    d_i,a=x_(i+e_a)-x_(i-e_a),
    p_i=d_i d_i^T.

This is also local, symmetric, translation covariant, and proper-cubic
covariant. Consider the geometry extensions

    S_[lambda,mu](x;h)
      =S_stat(x)+sum_i Tr[h_i(lambda q_i+mu p_i)].    (12)

For every `lambda,mu`,

    S_[lambda,mu](x;0)=S_stat(x).

Yet the first derivative at `h=0` is `lambda q_i+mu p_i`. The cut tensor is
diagonal. On the exact `L=3` configuration with occupied sites `(0,0,0)` and
`(0,1,1)`, the summed environment tensor is

    [[4,0,0],
     [0,4,-2],
     [0,-2,4]],

so it supplies an offdiagonal `yz` response that the cut tensor lacks. All
members are covariant; all agree on the fixed-background action; their metric
derivatives differ.

This proves the narrow negative claim:

> The fixed-background binary scalar law and global proper-cubic covariance do
> not uniquely determine a local metric derivative.

It proves no impossibility for a supplied geometry family, source-coupled
action convention, local Ward identity, continuum limit, or other carrier.

Nor does covariance alone imply conservation. Using the declared backward
difference

    (div q)_i,a=q_i,aa-q_(i-e_a),aa,

the singleton fixture has nonzero divergence at individual sites, although
the sum of each divergence component vanishes by periodic telescoping. A local
symmetry, dynamics, or on-shell geometric equation is required before a Ward
identity can be asserted.

## 6. Exact Bridge And Axiom-Side Residual

The result separates two useful candidate clauses. They are hypothetical only.

### Weak code-swap-even interface-source clause

One sufficient narrow convention is:

> Conditional on a physically licensed code-symmetric binary cut action, its
> local scalar interface source is the equal-endpoint density: each
> occupied/unoccupied nearest-neighbor edge contributes one half of its local
> cut action to each endpoint. The density is even under interchange of the
> two code symbols. A field coupling, if any, is separately specified.

This selects `theta=1/2` inside (8). It does not license the log-law action,
fix `B`, supply an action unit, introduce a metric, or derive conservation.

### Physical geometry-family source/action clause

One sufficient stronger clause is:

> Conditional on a supplied compatible, projectively consistent family of
> finite-region laws `pi[g]` defined for a registered local geometry source
> `g`, the physical source action is
> `S_phys[g]=s_*[-log pi[g]]+C[g]`, with one fixed positive action unit `s_*`.
> The local physical stress/source is the registered first variation of this
> same action with respect to `g`, with site and unordered-edge terms counted
> once. The family is locally covariant under the declared geometry-source
> transformations, and any claimed conservation law must be the corresponding
> proved discrete Ward identity. The scalar Record readout remains distinct.

This wording supplies a geometry **family**, not merely one background law,
and makes the source derivative part of the same object. It is sufficient to
remove the ambiguity exhibited by (12) once `pi[g]` itself is specified. It is
not adopted, recommended, proved necessary, or claimed literally minimal.

The existing
[source-coupled local-action candidate](OBSERVABLE_PRINCIPLE_SOURCE_COUPLED_LOCAL_ACTION_ADMISSION_CANDIDATE_NOTE_2026-05-21.md)
is an open-gate convention route, not a new axiom theorem. It already proposes
that local source derivatives define insertions and connected responses. That
reframing could house the geometry-family bridge downstream without changing
the four canonical axioms. Therefore this block does **not** conclude that a
new axiom is required.

If the physical log-law clause is supplied and dual plaquettes have area
`a^2`, the conditional surface coefficient is

    tau_stat=s_* log B/(2a^2).

The approved scale-reference primitive converts powers of `a` to physical
units. It does not fix `s_*`, `B`, the sign, a metric family, or a field
coupling.

Even the stronger clause leaves open:

- which geometry family `pi[g]` is physical;
- the local Ward/conservation theorem;
- temporal extrusion of the spatial cut into a spacetime worldvolume;
- the field equation, nonlinear completion, coupling, and regime; and
- selection of one realized history.

## 7. Consequence For The TOE Lanes

This block sharpens the gravity/source and causal boundaries without changing
the fixed scores.

| Lane | Exact consequence | Still open |
|---|---|---|
| operational quantum / records | the binary compatible action is a cut surface distinct from the scalar Record readout | physical code, source/readout context, formation process |
| causal time | the spatial cut is a closed two-chain on each supplied slice | update law, worldvolume history, clock/rate, causal propagation |
| inertia / matter | complement-even interface action is separated from complement-odd volume/magnetization | physical matter/source identification and dressed inertia |
| gravity / source / resources | exact statistical surface coefficient, local improvement family, directional response, and conditional exterior Poisson invariance | physical log-law, metric family, conserved stress, field equation, coupling |
| Born probability / realized history | compatible Gibbs weights become exact cut-area weights on the code-symmetric line | selection of `B`, continuous M2 law, realized member/history |

No current-axiom physical or autonomous obligation is retired. The exact cut
geometry is conditional on the supplied binary law and code-swap line; the
physical source/metric bridge remains additional. Therefore the fixed TOE
percentages do not move.

## 8. Relation To Existing Sources

| Source | Exact use | Boundary preserved |
|---|---|---|
| [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) | fixed cubic adjacency, proper-cubic covariance, local probability clause | no source/action, metric, or dynamics imported |
| [Block 9 action/resource note](ADMISSIBILITY_ISING_ACTION_RECORD_READOUT_PAIR_RESOURCE_RESPONSE_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md) | `A B^3=1`, `u=-3v`, pair action and covariance response | no physical action or stress inherited |
| [Weak-field source response](GRAVITY_WEAK_FIELD_SOURCE_RESPONSE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md) | conditional graph-Poisson equation and zero-mode inverse | `rho` and the physical field identification remain supplied |
| [Stress-Ward packet](UNIVERSAL_GR_STRESS_WARD_TRANSVERSE_SEAGULL_BOUNDED_THEOREM_NOTE_2026-06-08.md) | exact warning that the full metric-source Hessian and physical spin-two identification remain open | its Dirac carrier is not imported into the binary law |
| [Source-coupled local-action candidate](OBSERVABLE_PRINCIPLE_SOURCE_COUPLED_LOCAL_ACTION_ADMISSION_CANDIDATE_NOTE_2026-05-21.md) | existing convention/reframe path for local source derivatives | open gate, not current axiom content |
| [Scale-reference primitive](SCALE_REFERENCE_PRIMITIVE_NOTE.md) | units conversion only | no dimensionless coefficient, source, or coupling supplied |

The recent open cutting PRs #6043--#6048 and #6073 concern a different finite
cell-cutting incidence system. They do not contain the regular-graph identity
`3N-E=|delta X|/2`, the compatible binary action, the endpoint improvement
family, or the metric-extension comparison. PRs #6069 and #6072 classify an
inter-site word law and semantic repair map; neither collides with this result.

## 9. No-Go Discipline Gate

The narrow negative claim is only:

> One fixed-background code-symmetric scalar law plus global proper-cubic
> covariance does not uniquely determine its derivative with respect to an
> unsupplied local metric source, and the displayed covariant cut tensor is not
> automatically locally conserved.

No broad source, stress, metric, gravity, dynamics, or axiom no-go ships.

### N1 — Materially Distinct Routes

The route families are normalized by mathematical object, mechanism, and
terminal obligation.

| Route family | Object / mechanism | Result against the narrow claim | Marker |
|---|---|---|---|
| anisotropic cut family | directional `B_a` and cut counts; differentiate (4) | constructs diagonal source coordinates once the off-background `B_a` family is supplied; the isotropic background alone does not supply that family | ATTEMPTED |
| code-swap-even endpoint source | local edge allocation; complement symmetry | uniquely selects `theta=1/2` inside (8), but only after local source typing is imposed and it supplies no full metric tensor | ATTEMPTED |
| source-coupled local action | local action/source convention; functional derivative | remains a live open-gate route that can define the derivative downstream; it is additional convention content, so no broad no-go is allowed | ATTEMPTED |
| covariant environment tensor | centered neighbor gradients `p_i=d_i d_i^T` | explicitly supplies offdiagonal response while agreeing at the background, proving nonuniqueness rather than impossibility | ATTEMPTED |
| metric-reparametrized Dirac route | deform a supplied kinetic operator and derive stress vertices | remains live on a different carrier; it cannot identify the binary cut derivative without a carrier bridge | ATTEMPTED |
| physical M2 occupation-current route | local update, reservoir, and transported occupation | supplies a conserved current on a supplied code/update, but the current is not identified with the cut action or energy | ATTEMPTED |
| ordered stochastic update | local rates with the cut Gibbs law stationary | remains live; a generator, mobility, schedule, and physical time interpretation are not selected by the static law | ATTEMPTED |
| dual-surface tension route | closed cut two-chain and local area variation | gives the strongest positive interface interpretation here; physical action units, history, and metric coupling remain open | ATTEMPTED |

There are more than five genuinely different families. Several remain live, so
the broad claim “no stress/source route exists” fails N1 and is rejected. The
narrow fixed-background nonuniqueness claim survives because two explicit
covariant extensions already prove it.

### N2 — Wall Independence And Collapse

The full physical-gravity residual is collapsed to four conditions:

- `W_action`: physically license `S_phys=s_*[-log pi]` and its unit;
- `W_geometry`: supply the local geometry-dependent law/source family whose
  derivative defines the local source;
- `W_Ward`: prove the appropriate local conservation/Ward identity on the
  selected dynamics or on-shell geometry; and
- `W_field`: supply the field equation, coupling, nonlinear completion, and
  validity regime.

| Pair | Closing first closes second? | Closing second closes first? | Independent? |
|---|---:|---:|---:|
| `W_action` / `W_geometry` | no: a scalar action at one geometry has no derivative | no: a metric family need not be the physical log law | yes |
| `W_action` / `W_Ward` | no: physical naming gives no local symmetry | no: a conserved current need not be this action | yes |
| `W_action` / `W_field` | no: source action supplies no field operator | no: a field equation does not select microscopic source action | yes |
| `W_geometry` / `W_Ward` | no: (12) gives nonconserved covariant derivatives | no: conservation alone does not define a metric derivative | yes |
| `W_geometry` / `W_field` | no: source variation supplies no curvature equation | no: geometry dynamics does not select the matter derivative | yes |
| `W_Ward` / `W_field` | no: conservation gives no coupling or evolution equation | no: a field equation can impose rather than derive source compatibility | yes |

Action unit and lattice-unit conversion are not counted as two walls: `s_*`
belongs to `W_action`, while the approved scale primitive already supplies the
units ruler. Tensor indices and temporal extrusion belong to `W_geometry` and
`W_Ward`, not extra duplicated walls.

### N3 — Hidden-Wall Scan

The proof's load-bearing conditions are explicit:

- finite supplied binary sector;
- regular graph, with simple periodic cubic quotient `L>=3` for directional
  statements;
- compatible pair action from Block 9;
- optional code-swap relation;
- endpoint-local count-once family only for (8)--(11);
- supplied graph-Poisson operator only for the conditional response;
- supplied tensor source `h` only for the extension counterexamples; and
- no physical action license, dynamics, metric family, local symmetry, field
  equation, or realized history.

Rhetoric-trigger classification:

| Phrase class | Classification |
|---|---|
| “by construction” for dual cubes and local extensions | finite definition followed by explicit boundary/tensor checks; no hidden physical premise |
| “supplied” weak field, tensor source, and code swap | explicit conditional input |
| “registered” in candidate wording | hypothetical governance language only; not consumed by the theorem |
| “canonical” | used only to say the canonical memo is unedited |
| “naturally”, “obviously”, “standard QFT” | absent from load-bearing proof |

No hidden condition is promoted after the four-wall collapse.

### N4 — Residual Matching

| Source location | Prior residual | Present residual | Match? |
|---|---|---|---:|
| `MINIMAL_AXIOMS_2026-06-29.md`, Open Gates | source/action and physical observable identification absent | physical cut-action/source license absent | yes |
| Block 9, §§6--8 | pair coefficient and susceptibility are statistical; stress/metric bridge open | cut geometry closes the coefficient's shape but not physical stress | yes |
| weak-field source response, Claim 1 | graph-Poisson response closes for a supplied `rho` | endpoint family supplies conditional candidate densities, not their physical selection | yes, conditional composition only |
| stress-Ward packet, audit-boundary repair | full metric-source Hessian and physical spin-two identification open | fixed background lacks a selected metric derivative | yes |
| source-coupled local-action candidate, §0 | source derivative is an explicit convention, not current derivation | convention/reframe can close `W_geometry` downstream | yes, partial-closure route |
| `PLANCK_FINITE_RESPONSE_NO_GO_NOTE_2026-04-24.md` | finite signed-permutation group has no infinitesimal metric tangent | present law also has only global cubic covariance, but adds explicit external tensor extensions | similar, not used as proof |
| Cycle 313 physical-M2 common seam | conserved occupation is not energy/stress/gravity | alternate dynamics/current carrier, not the fixed-background derivative residual | no; context only |

Nonmatching rows are not used as negative witnesses.

### N5 — Rhetoric And Resolution Audit

| Resolution | Executed result | Negative wording allowed? |
|---|---|---|
| per element/edge | binary disagreement equals one cut plaquette; exact | yes: the edge indicator is not itself a physical stress assignment |
| per site | flip increment and endpoint improvement identities; exact | yes: displayed covariant local tensor need not be divergence free |
| per mode | bulk and diagonal-shear cut response; exact orbit fixture | only for declared cut coordinates; no claim about offdiagonal physical shear |
| per block/finite region | regular-graph cut theorem and K7 partition; exact | yes: fixed-background scalar action does not fix off-background derivative |
| lattice wide | periodic cubic closed two-chain and rotation covariance; exact | no global gravity or continuum-stress no-go |

The runner cache lands one substantive certificate line for each resolution.
The phrase “not a physical stress tensor” applies to the declared cut-
orientation object absent a physical derivative bridge; it is not a universal
claim about every completion.

### N6 — Partial-Closure And Primitive Registry Check

The Primitive Registry Check read the current machine registry and all four
current premise sources:

- `minimal_axioms` supplies fixed cubic adjacency, the local probability
  clause, and Record, but no source/action or metric family;
- `scale_reference_primitive` supplies `a^(-1)=M_Pl` as units only;
- `kinetic_isotropy_primitive` supplies only the structural kinetic-form ratio,
  not dynamics, stress, or a metric response theorem; and
- `realized_state_primitive` permits pointwise evaluation at a supplied
  realized state, not state selection or source dynamics.

None is counted as a wall or bounded import, and none is enlarged.

Partial closures that do **not** require a new axiom are:

| Path | Current status | What it could close |
|---|---|---|
| equal-endpoint code-swap convention | exact conditional theorem here | endpoint allocation inside (8) |
| source-coupled local-action candidate | existing `open_gate` convention route | identify local source derivatives without changing the four axioms |
| explicit downstream geometry family `pi[g]` | model-level bridge | metric derivative and contact/improvement scheme |
| weak-field Poisson composition | existing bounded conditional packet | scalar exterior response after `rho` is physically selected |
| metric-reparametrized kinetic action | existing bounded route on a different carrier | conserved stress vertices if a binary-to-kinetic carrier bridge lands |
| local update/current compiler | existing physical-M2 constructive route | conservation and temporal transport on a selected dynamics |

Therefore “a new axiom is required” is rejected. Owner adoption of a stronger
foundation clause is one governance option, not the only closure mechanism.

### N7 — Steelman

The strongest hostile objection is:

> The block has nearly built the bridge it says is open. Block 9 supplies the
> log-law action, code swap selects the equal-endpoint source, the existing
> source-coupled local-action convention tells us to differentiate it, and the
> weak-field packet supplies the graph-Poisson response. The endpoint
> ambiguity is merely a Laplacian improvement whose exterior field is
> unchanged. A model-level declaration of `pi[g]` could therefore complete the
> scalar source without any axiom edit, while the existing metric-
> reparametrized Dirac route could supply stress after a carrier map. Calling
> the gravity lane blocked by the scalar law would be premature.

This steelman is accepted. It defeats every broad source or gravity no-go. The
shipped claim is narrowed to the mathematical fact that one background value
does not choose its derivative, demonstrated by the explicit `(lambda,mu)`
family. The steelman's concrete next obligation is exactly to construct and
physically license one common `pi[g]` family or binary-to-kinetic carrier map.

### N8 — Cross-Cycle Echo

- The Planck finite-response note removed the route that tried to obtain an
  infinitesimal metric tangent from a finite automorphism group alone. Its
  surviving mechanism was to add a response envelope; (12) tests that same
  move explicitly rather than declaring it impossible.
- The source-coupled local-action campaign reframed an apparent new-axiom need
  as an open convention plus derivative theorem. This block preserves that
  mechanism in §6.
- Universal-GR metric-reparametrization notes add an explicit off-background
  kinetic family and obtain stress vertices, while keeping uniqueness and
  physical identification open. This is the strongest constructive analog.
- Physical-M2 source campaigns turned static scalar candidates into conserved
  occupation only by selecting a code, update, reservoir, and current. That
  mechanism remains available but does not silently identify the cut action.
- Blocks 8--9 repeatedly separated a static law, update semantics, readout,
  and physical source. The cut theorem composes those seams rather than
  treating recurrence as impossibility evidence.

Every previously successful retirement mechanism—convention reframe,
off-background family, or explicit dynamics—is represented among the live
routes above.

### Gate Result

PASS for the narrow fixed-background metric-derivative nonuniqueness and the
nonconservation of the displayed cut tensor.

FAIL / DO NOT SHIP for claims that no physical source, conserved stress,
geometry family, metric response, gravity law, or non-axiom convention route
can exist.

## 10. Verification

Run:

    python3 scripts/admissibility_code_swap_cut_area_local_source_improvement_metric_response_axiom_boundary_2026_08_10.py

The runner checks:

- current axiom, action, weak-field, stress-boundary, source-convention, and
  scale surfaces;
- exact directional degree/cut and complement identities on the periodic
  `L=3` cubic quotient;
- anisotropic and isotropic cut actions plus every local flip fixture;
- dual-surface parity closure and all 24 proper cubic rotations;
- exact directional orbit covariance and the rational degree-six `K_7`
  partition/response fixture;
- endpoint source totals, improvement, code swap, conditional Poisson contact,
  and exterior-gradient invariance;
- cut/environment tensor covariance, offdiagonal alternative, and explicit
  nonzero local divergence; and
- candidate wording, governance, canonical nonmutation, and N1--N8.

Expected final line:

    TOTAL: PASS=... FAIL=0

## Boundary Verdict

The compatible code-symmetric binary action is now geometrically exact:

    statistical action
      = one-half log B times occupied/unoccupied cut area,

with the local conditional odds equal to its exact discrete area variation.
Its directional derivatives are cut means and covariances, and its endpoint
source decompositions differ by a Laplacian contact improvement.

That closes a real resource geometry. It does not close the physical bridge.
A physical stress requires an off-background geometry family and a source
derivative; conservation requires a local Ward/dynamics theorem; gravity
requires a field equation, coupling, and regime. Existing convention and
model-level routes remain live, so no new-axiom necessity is claimed.

No canonical axiom is edited. No percentage moves.
