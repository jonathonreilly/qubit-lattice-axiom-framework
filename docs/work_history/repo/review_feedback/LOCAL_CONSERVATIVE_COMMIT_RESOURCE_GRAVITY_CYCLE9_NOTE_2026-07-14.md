# Local Conservative Commit-Resource Gravity — Cycle 9

**Date:** 2026-07-14

**Type:** meta

**Authority:** none. This is an exact finite construction and bounded route
tournament. It is not an axiom proposal, audit verdict, retained theorem,
empirical gravity claim, or assertion that the universe is literally a
computer. It changes no axiom, primitive, registry, queue, or audit surface.

Companion runner:

```text
scripts/local_conservative_commit_resource_gravity_cycle9_2026_07_14.py
```

## Result Up Front

The strongest compute/storage-limited route now has a small exact local law
with substantially more reach than direct record-edge freezing:

> A commit creates a local resource-debt token; debt tokens move by symmetric
> nearest-neighbor exclusion; export removes them into a renewal reservoir;
> the local debt density reduces one common scheduler available to every
> probe.

This law is strictly nearest-neighbor in its bulk update, exactly conservative
when the local source and export reservoirs are included, translation and
proper-cubic covariant, and realizable by one binary `M2` resource carrier per
working site. Its exact one-point equation is linear diffusion despite the
microscopic exclusion interaction. With sustained commit and export currents,
repeated local dynamics converges to a stationary lattice Green response. On
a side-40 cubic torus, radii `4` through `10` fit `a+b/r` with
`R^2 > 0.9998`, and `b` is within four percent of the finite-volume target
`j/(4 pi kappa)`.

No nonlocal Poisson inverse appears in the update rule. The inverse is a
theorem about the fixed point of repeated local relaxation.

The same law also supplies a clean active-source map distinct from archive
count:

```text
active source = commit current,
archive count = time integral of successful commits.
```

A stationary current can coexist with a linearly growing permanent archive;
changing old archive content does not change the stationary field when the
current law does not read it. A one-time commit does not remain a stationary
source: its debt token diffuses toward the uniform mode. Thus archive remains
inert unless a separate archive-coupling clause is added.

Finally, if debt reduces a common local scheduler,

```text
q(x) = 1 - gamma [n(x)-n_0],       gamma > 0,
K_probe(x) = q(x) K_probe^0,
```

then positive-energy probe levels are lower near a positive commit source.
The corresponding scalar potential rises outward, so its discrete force has
the attractive sign. Every finite probe generator, including composites, has
all local frequency gaps multiplied by the same `q`; the fractional response
is a universal local lapse within this law.

These are theorems of the displayed local law, not of the four axioms alone.
The construction still needs independent law values and physical bridges:

- the mass-to-commit-current map;
- commit, export, diffusion, and lapse coefficients;
- a maintained renewal reservoir or export-to-infinity architecture;
- the common scheduler's identification with all physical matter;
- a quantum/reversible dilation of the dissipative Markov relaxation;
- a covariant block code when archive, resource, and probe coexist; and
- tensor gravity, light bending, nonlinear self-coupling, and the Einstein
  limit.

The result therefore closes several weak-field G-lane architecture questions
inside one exact candidate law, but does not close gravity as a TOE lane. Its
honest classification is `partial-attempt-with-named-untested-routes`.

## The Smallest Law Found

Let every working resource site carry an occupation

```text
eta_x in {0,1},
```

where `eta_x=1` means one unit of processing/transport debt occupies the site.
For every nearest-neighbor edge `<xy>`, equal-rate symmetric exclusion swaps
`eta_x` and `eta_y`. A local commit reservoir at `x` transfers a debt token
into an empty resource site at rate `alpha_x`; a local export reservoir removes
a token at rate `beta_x`.

For a finite configuration `eta`, the continuous-time local generator is

```text
(G f)(eta)
 = kappa sum_<xy> [f(eta^xy)-f(eta)]
 + sum_x alpha_x (1-eta_x) [f(eta^{x,+})-f(eta)]
 + sum_x beta_x eta_x     [f(eta^{x,-})-f(eta)].
```

Each bulk swap conserves the exact number of debt tokens. Each birth or death
is also conservative after its adjacent reservoir counter is included: a
token moves from the commit reservoir into the field or from the field into
the export reservoir. The field alone is open at those interfaces.

The finite runner also uses the discrete lazy relaxation

```text
phi_{t+1}(x)
 = (1/2) phi_t(x)
 + (1/12) sum_{y~x} phi_t(y)
 + epsilon [c_t(x)-e_t(x)].
```

This is the exact one-point sampled form for the bulk diffusion with a fixed
current comparator. It reads only the site, its six neighbors, and local
commit/export event fields. Its matrix is

```text
P = I - L/12,
```

where `L` is the current six-neighbor positive graph Laplacian. `P` is
symmetric, nonnegative, and doubly stochastic. The runner verifies exact
rational conservation and covariance under every one of the 24 proper cubic
rotations.

The word “smallest” is scoped. This is the smallest scalar law found in the
tournament: one binary working resource and one equal edge rate, plus local
commit/export interfaces. There is no global minimality theorem over all
reversible cellular automata, quantum walks, block codes, or nonlinear
resource laws.

## Why Exclusion Gives an Exact Linear Field

Microscopic exclusion looks nonlinear because a hop needs an occupied source
and empty target. For a symmetric edge, however,

```text
eta_y(1-eta_x) - eta_x(1-eta_y) = eta_y-eta_x.
```

The two-point term cancels exactly. Therefore the occupation mean

```text
n_x(t) = E[eta_x(t)]
```

obeys

```text
d n_x/dt
 = kappa sum_{y~x} [n_y-n_x]
 + alpha_x [1-n_x]
 - beta_x n_x.
```

No independence or mean-field factorization is used. The runner builds the
complete 256-state Markov generator on the periodic `2 x 2 x 2` multigraph,
solves its stationary distribution, and verifies that its eight exact
one-point means agree with the closed eight-dimensional linear system.

This is consistent with primary SSEP literature, used here as parallel scope
support rather than load-bearing authority:

- Faggionato gives a graphical stirring construction and density-field
  duality for SSEP on countable sets:
  [Graphical constructions of simple exclusion processes with applications to random environments](https://arxiv.org/abs/2304.07703).
- De Masi, Presutti, Tsagkarogiannis, and Vares study local birth/death current
  reservoirs and the resulting heat equation/Fourier law:
  [Current reservoirs in the simple exclusion process](https://arxiv.org/abs/1104.3445).
- Derrida, Lebowitz, and Speer analyze the nonequilibrium stationary state
  generated by open SSEP reservoirs:
  [Large Deviation of the Density Profile in the Steady State of the Open Symmetric Simple Exclusion Process](https://arxiv.org/abs/cond-mat/0109346).

The finite identities in this note are derived directly by the runner.

## Local Iteration Produces the Green Response

First hold a positive commit current at `a` and an equal export current at
`b`. The sampled one-point update is

```text
phi_{t+1} = P phi_t + epsilon (delta_a-delta_b).
```

Because the source has zero sum, the constant mode is absent. Every other
eigenvalue of `P=I-L/12` lies in `[0,1)`. Hence the local iterations converge
to the unique mean-zero fixed point

```text
(I-P) phi_* = epsilon (delta_a-delta_b),
L phi_*     = 12 epsilon (delta_a-delta_b).
```

Equivalently,

```text
phi_* = 12 epsilon L^+ (delta_a-delta_b),
```

but this last line describes the fixed point; it is not the microscopic
operation. A side-3 runner solves the fixed point in exact rational arithmetic.
A side-9 runner confirms that direct repeated neighbor updates equal the
finite spectral geometric sum at steps `1,10,50,200,1000` and converge to the
fixed point below `10^-12` relative error.

### Reservoir-complete stationary source

For one birth reservoir at `a` and one death reservoir at `b`, stationary
current conservation gives

```text
j = alpha (1-n_a) = beta n_b,
kappa L n = j (delta_a-delta_b).
```

Let

```text
g = L^+ (delta_a-delta_b),
R_eff = g(a)-g(b).
```

Then

```text
j = 1 / [1/alpha + 1/beta + R_eff/kappa].
```

For equal source/export rates at antipodal sites, the stationary density is

```text
n = 1/2 + (j/kappa) g.
```

Thus the active amplitude is not assigned independently after solving the
field; the finite reservoir law fixes it through vacancy, extraction, and
effective resistance.

On the side-40 fixture, `n` stays strictly in `[0,1]`, satisfies the local
stationary equation to machine precision, is invariant under all 24 proper
cubic rotations, and has the controlled `1/r` window stated above. The
existing lattice Green theorem identifies the asymptotic infinite-volume form
of the same operator as

```text
g(r) = 1/(4 pi r) + cubic O(r^-3).
```

The new content here is not that Green asymptotic. It is that a concrete
strictly local conservative process generates that operator and source at its
stationary one-point level.

## Active Source Is Commit Current, Not Archive Count

Let `A_T` be the number of permanent commit records written through time `T`.
At stationarity,

```text
E[A_T-A_0] = j T,
```

while `n(x)` is time-independent. Two worlds may therefore have different old
archives and the same present `j,n`; or the same archive and different present
commit currents.

This closes the source-identity ambiguity **inside this candidate law**:

```text
J_active^+(x) = alpha_x E[1-eta_x],
J_export^-(x) = beta_x E[eta_x].
```

The generator reads those currents, not `A_T`.

The physical mass-to-commit map is still open. The law does not prove that a
kilogram of cold matter performs a particular number of commits per tick, nor
that all rest energy is maintained record current. It only makes the source
observable non-discretionary after the commit operation and its rates have
been supplied.

The distinction also has a hard renewal consequence. If every successful
commit writes a permanent record, the archive grows at rate `j`. One-record-
per-site permanence then needs fresh sites, export, migratory encoding, or an
ever-growing boundary archive. The stationary resource field does not erase
that storage cost.

## Correct Sign — On the Scalar-Lapse Surface

Take the relative debt field

```text
varphi(x) = n(x)-n_0
```

and define available scheduler fraction

```text
q(x) = 1-gamma varphi(x),       gamma>0.
```

A positive commit current makes `varphi` positive and largest near the
source. Thus `q` is smallest near the source. For a localized positive-energy
probe with flat generator eigenvalue `E_s>0`, the common scheduler gives

```text
E_s(x) = q(x) E_s,
V_s(x) = E_s [q(x)-1] = -gamma E_s varphi(x).
```

Since `varphi` decreases outward in the tested Green window, `V_s` rises
outward. Its negative discrete gradient points inward. Reversing the
debt-to-scheduler sign makes the force point outward; the runner performs that
paired sign ablation.

This is the correct attractive sign for a positive scalar lapse/well. It is
not the prior spin-2 exchange-sign theorem, does not derive a metric tensor,
and does not establish light bending or nonlinear GR. The sign follows only
after the positive commit-to-debt orientation, `gamma>0`, positive probe
energy, and scheduler-energy map are all part of the exact law.

## Universal Local Lapse — And Its Precise Scope

For any finite local probe generator `K_s`, impose one substrate scheduler:

```text
K_s(x) = q(x) K_s^0.
```

Every eigenvalue difference then scales by `q(x)`. If a composite probe has

```text
K_AB^0 = K_A tensor I + I tensor K_B,
```

the entire composite generator is likewise `q K_AB^0`; composition does not
change the fractional lapse. The runner checks a two-level clock, an unrelated
three-level clock, and their six-level composite.

This is a real universality theorem of a common scheduler clause. It is not a
derivation of that clause from diffusion or Record. Giving species different
`gamma_s` immediately breaks universality, as the paired-law ablation shows.
Binding energy, spatially varying transport, radiative stability, and the
full equivalence principle remain outside the finite local-gap result.

The approved kinetic-isotropy primitive supplies only `c_t=c_s` in regulator
form. It does not supply `q`, `gamma`, the resource process, or common matter
coupling.

## Boundary And Renewal Cost

A stationary nonconstant profile carries a steady resource current. Exact
summation by parts gives

```text
kappa <varphi,L varphi>
 = j [varphi(a)-varphi(b)] > 0.
```

The runner verifies this equality. The right side is the work that the commit
and export reservoirs must maintain; without them, lazy diffusion decreases
the Dirichlet energy and flattens the field.

Three boundary facts follow:

1. On a finite closed torus, sustained positive injection without equal
   export grows the constant mode and has no stationary solution.
2. A finite source reservoir with `B` tokens supports the steady current for
   only expected duration `B/j`.
3. Indefinite stationarity therefore requires a return pump, fresh boundary
   resource, or export to infinity. Each option has an energy, entropy, and
   archive-identity cost not supplied by the bulk diffusion law.

The bulk Markov process is number-conservative but dissipative as a probability
evolution. A half-identity/half-SWAP local averaging channel sends a pure
resource configuration to a mixed state of purity `1/2`. A closed-system
unitary on the same carrier cannot do that. An exact microscopic quantum
completion needs an environment, ancillary clock/randomizer, measurement
record, or a larger reversible automaton whose coarse-graining yields SSEP.

## Does `M2` Suffice?

The answer depends on the layer:

| layer | smallest result established here |
|---|---|
| working debt field alone | one `M2` binary occupancy per site suffices for SSEP |
| local exclusion edge | two neighboring `M2` sites; SWAP conserves occupation exactly |
| independent binary archive content plus binary debt occupancy | one `M2` is too small for two independent readable bits; an `M4` two-qubit block has dimensional room |
| archive + debt + independent probe | generally a larger block or spatial code |
| dissipative Markov update as closed unitary physics | system `M2` alone does not suffice; a dilation/environment is needed |

This is a dimension and purity boundary, not a full block-construction theorem.
`M4` room does not select a geometric block origin, prove a proper-cubic code,
or implement renewal. Reusing one `M2` sequentially, migratory archives, and
nonlocal encodings remain live alternatives.

## What Becomes Theorem, And What Remains Law Content

| G-lane item | status conditional on the displayed exact law |
|---|---|
| strict local propagation | derived from SSEP swaps |
| bulk conservation | exact, event by event |
| translation/proper-cubic covariance | exact |
| source map | active source equals commit current; archive count is not read |
| stationary field equation | `kappa L n=j(delta_a-delta_b)` derived |
| stationary Green response | derived as the local fixed point |
| controlled `1/r` window | runner-verified; asymptotic routed to existing same-operator theorem |
| scalar attractive sign | derived from positive debt plus common scheduler/positive-energy clauses |
| universal local lapse | derived for arbitrary finite local generators under common scheduler |
| superposition at one-point level | derived from the closed linear mean equation |
| physical mass source | mass-to-commit map remains independent |
| Newton coefficient | depends on independent law values `alpha,beta,kappa,gamma` and units |
| eternal source | renewal reservoir/export remains independent |
| exact quantum microphysics | Markov dilation and block code remain independent |
| full equivalence principle | only local gap universality established |
| tensor/nonlinear gravity | nonlinear metric completion remains independent |

The effective scalar strength in the weak stationary window is proportional to

```text
G_eff(lattice units) ~ gamma j / (4 pi kappa).
```

Conservation and cubic symmetry do not select `alpha`, `beta`, `kappa`, or
`gamma`. Changing `kappa` in the paired-law runner changes the stationary
amplitude while preserving locality, conservation, and covariance.

## Axiom Need

This cycle supports **no axiom addition**. It demonstrates that local
propagation, the Poisson/Green silhouette, active-source semantics, scalar
sign, and local fractional lapse can coexist as consequences of one compact
exact law. That is evidence to keep them out of constitutional wording while
the law is still being selected.

The candidate should be parked as a conditional theorem import:

```text
Conditional on the local commit-resource exclusion law and common scheduler,
the current lattice supports a conservative cubic-covariant resource field
whose maintained source-sink state has a Green 1/r window, attractive scalar
well, and composition-independent local lapse.
```

Formation, probability, the physical commit rate of matter, renewal, and the
quantum/metric completion remain outside that statement. “The universe is
compute limited” is interpretation until those invariants and couplings are
selected or derived.

## No-Go Discipline Gate

**Status:** PASS for the narrow negatives below. Overall result:
`partial-attempt-with-named-untested-routes`; no broad gravity, carrier, or
resource-theory no-go is shipped.

### N1 — Alternative routes

1. **Direct record-edge deficit — ATTEMPTED.** It is exactly compactly
   supported one edge from a record and therefore has no direct `1/r` window
   (`RECORD_CONDITIONED_EXCHANGE_CAPACITY_GRAVITY_FINITE_PROBE_NOTE_2026-07-14.md:35`).
2. **One-time locally conserved commit pulse — ATTEMPTED.** It preserves one
   token but relaxes to the uniform mode on a finite torus, so archive
   permanence alone does not maintain a stationary field (runner G).
3. **Sustained source without export — ATTEMPTED.** Its constant mode grows
   exactly linearly; a finite closed conservative volume has no stationary
   one-sign source (runner C/G).
4. **Paired fixed commit/export current with lazy diffusion — ATTEMPTED,
   CONDITIONAL SUCCESS.** Strict local iterations converge exactly to the
   source-sink Green fixed point (runner C-E).
5. **Microscopic SSEP with vacancy-limited birth/death reservoirs — ATTEMPTED,
   CONDITIONAL SUCCESS.** The complete Markov generator closes the one-point
   Poisson equation and fixes current self-consistently (runner F).
6. **Archive occupancy as source — ATTEMPTED.** It generates a Green field but
   retains history trails and makes source scale with accumulated archive,
   reproducing the prior source-identity problem (runner G; prior note line
   72).
7. **Species-specific lapse gates — ATTEMPTED.** They preserve the resource
   field but fail universal fractional clock response (runner H).
8. **Common scheduler — ATTEMPTED, CONDITIONAL SUCCESS.** It makes arbitrary
   local finite probe gaps and composites share the same fractional lapse
   (runner H).
9. **System-only unitary realization of the Markov relaxation — ATTEMPTED,
   NARROW FAILURE.** The displayed local averaging sends a pure state to a
   mixture, so that channel is not a closed unitary on the same system
   carrier; dilation routes remain open (runner I).
10. **Fresh boundary/export architecture — ATTEMPTED BY BUDGET.** It can
    maintain the current, but a finite reservoir lasts only `B/j`; an
    explicit return or infinite-export law remains required (runner I and
    `RECORD_CAPACITY_RENEWAL_CONSTITUTIONAL_PRESSURE_NOTE_2026-07-14.md:75`).

### N2 — Wall-Independence Audit

After collapsing downstream phrasings, five independent walls remain:

- `S`: physical formation and mass-to-commit-current map;
- `R`: renewal/export boundary and its energetic/archival support;
- `C`: dimensionless law values and physical normalization
  (`alpha,beta,kappa,gamma`);
- `Q`: covariant carrier code plus reversible/quantum dilation; and
- `G`: tensor, lensing, nonlinear, and Einstein completion.

| pair | closing first closes second? | closing second closes first? | independent? |
|---|---:|---:|---:|
| `S,R` | no | no | yes |
| `S,C` | no | no | yes |
| `S,Q` | no | no | yes |
| `S,G` | no | no | yes |
| `R,C` | no | no | yes |
| `R,Q` | no | no | yes |
| `R,G` | no | no | yes |
| `C,Q` | no | no | yes |
| `C,G` | no | no | yes |
| `Q,G` | no | no | yes |

The field equation, Green inverse, source/archive distinction, scalar sign,
and local fractional universality are not counted as walls after the exact law
is supplied; they are derived consequences of its clauses. The common
scheduler clause itself is part of `C/Q`, not derived from diffusion.

### N3 — Hidden-Wall Scan

Potentially misleading phrases are classified explicitly:

- **“conservative”** means bulk token number plus local reservoir counters;
  the field subsystem alone is open at commit/export sites.
- **“active source”** means the displayed transition current, not a preferred
  state, archive density, or mass by definition.
- **“stationary”** includes maintained reservoirs and their work; it is not a
  free equilibrium of a one-time record.
- **“capacity”** is the candidate scheduler fraction `q`; its identification
  with physical proper time is a law clause.
- **“universal”** is tested for local finite generator gaps and composites;
  it is not a full renormalized equivalence-principle theorem.
- **“attractive”** is the scalar positive-energy lapse sign; it is not a
  spin-2 or geodesic theorem.
- **“M2 suffices”** applies to the resource bit alone, not co-located archive,
  probe, and dilation layers.
- **“by construction”** statements in the derivation name supplied law
  clauses, not framework-derived facts.

No hidden condition is promoted without appearing in the five-wall inventory.

### N4 — Residual Matching

| cited witness | exact prior residual | present residual | match/use |
|---|---|---|---|
| `RECORD_CONDITIONED_EXCHANGE_CAPACITY_GRAVITY_FINITE_PROBE_NOTE_2026-07-14.md:35-38` | direct edge response is one-edge deep; archive freezes finite region | generate far field by repeated local transport and expose archive cost | yes; direct-rule comparator and closure target |
| same note `:72` | archive versus active source not chosen | source is commit transition current | yes; closed inside candidate law |
| same note `:137` | common edge field carries universality | common scheduler carries local gap universality | partial match; stronger matter/metric universality remains open |
| `RECORD_CAPACITY_RENEWAL_CONSTITUTIONAL_PRESSURE_NOTE_2026-07-14.md:22,64,75,141` | finite archive saturation and need for invariant resource/renewal/export | maintained SSEP current needs reservoirs and growing archive | yes; wall `R` |
| `LATTICE_GREENS_1_OVER_R_FROM_HEAT_KERNEL_RESOLVENT_THEOREM_NOTE_2026-06-07.md:23,45` | same `Z3` Laplacian Green identity and asymptotic | local process generates that operator at stationarity | yes; asymptotic authority only |
| `GRAVITY_ATTRACTION_SIGN_FROM_SOURCE_POSITIVITY_AND_SYMMETRIC_MEDIATOR_NARROW_THEOREM_NOTE_2026-06-08.md:18-25` | spin-2 exchange/source-action orientation | scalar scheduler-well sign | no; cited only as a nonmatching boundary, not support |
| `POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md:25,37,62` | counts alone do not determine absolute elapsed time or rate | common scheduler gives a relative local lapse | no; this cycle does not retire the absolute clock-rate boundary |

Nonmatching spin-2 and absolute-time citations are not used as evidence for
closure.

### N5 — Rhetoric And Resolution

- “One commit does not make a stationary field” was tested for a finite
  periodic diffusion process; no claim is made about every infinite-boundary
  or nonlinear soliton route.
- “Source without sink has no stationary solution” is for a finite closed
  conservative torus's nonzero constant mode; export to infinity remains
  live.
- “One `M2` is too small” is only for two independent co-located perfectly
  readable binary labels; sequential reuse, blocks, and nonlocal encoding are
  not excluded.
- “Not unitary” is only for the displayed reduced Markov averaging channel on
  the same carrier; reversible dilations are expressly open.
- “Universal lapse” is local and finite-generator-level; extended bodies,
  binding energy, transport trajectories, and radiative completion were not
  tested.

Every negative is therefore scoped to its tested site, block, finite-volume,
or reduced-channel resolution.

### N6 — Partial-Closure Paths

The candidate law creates four import-retirement paths without constitutional
change:

1. the Poisson inverse becomes the fixed-point theorem of local SSEP
   relaxation;
2. active source becomes the exact commit transition current rather than a
   discretionary label;
3. the attractive scalar sign follows from positive debt, positive energy,
   and the common scheduler orientation; and
4. composition-independent local lapse follows algebraically from a single
   scheduler multiplier.

The approved Lattice axiom supplies the graph and symmetry; Qubit supplies the
resource carrier algebra; kinetic isotropy supplies only `c_t=c_s`; the
realized-state primitive permits pointwise evaluation only. None supplies the
candidate dynamics, source rates, scheduler, boundary, or normalization.

The proper route is a named conditional law, bounded theorem, and later
import-retirement audit—not a new axiom claim.

### N7 — Steelman

A hostile reviewer should say that this construction is still too dissipative
and too large: a reversible local quantum cellular automaton might encode
resource, archive identity, and a mass current in one moving `M2` pattern,
generate an effective massless Green mode without maintained ideal
reservoirs, and recover tensor gravity through its conserved stress rather
than an imposed scalar scheduler. That route is not excluded. The SSEP result
shows one exact constructive existence path and sharpens its costs; it does
not prove uniqueness or minimality across reversible laws. This steelman is
strong enough to prohibit a broad no-go.

### N8 — Cross-Cycle Echo

The prior cycle warned that direct edge loss has no far field and that source,
clock, sign, and renewal were separate. This cycle demonstrates the right way
such walls can retire: a deeper exact local law makes the inverse, source map,
sign, and local universality consequences of one packet. The same mechanism
could later retire `S`, `R`, `C`, `Q`, or `G`; none should be called a required
new axiom merely because it remains open now.

It also preserves the earlier archive lesson. A recyclable working process can
run indefinitely while permanent records accumulate elsewhere, but that is
not free storage. The steady field's export current and the archive's fresh
support are different flows and both must be closed.

## Verification

Run:

```bash
python3 scripts/local_conservative_commit_resource_gravity_cycle9_2026_07_14.py
```

The PASS count contains related checks and is not an independent evidence
count.
