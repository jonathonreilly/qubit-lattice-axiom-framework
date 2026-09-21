# Final independent review: local Gibbs circulations and KLS transport

The stated conditional constructions and transport comparison are supported.
Two narrow wording findings were corrected: generic nonnegative amplitudes
need not give strictly positive rates, and the six-axis/eight-cube partition
uses fourteen occupied labels. No unresolved load-bearing mathematical
finding or numerical/source discrepancy remains within this bounded check.

This is scientific scrutiny of two supplied models, not an audit, a new
hydrodynamic theorem, or a TOE judgment. The positive construction and its
transport limitation coexist consistently with the one-dimensional KLS
countercontrol. The latter preserves a correlated Gibbs law while carrying
nonzero current through winding configuration cycles.

The complete original notes were read first. I then reconstructed the
arguments, read the specified established literature, and wrote and executed
an independent exact checker. This work was sealed before I opened either
author checker, result JSON or run log. Thus this is independent
post-note/pre-checker reconstruction, not a claim of blindness to the
proposed mathematical formulas. All eight initially sealed artifacts remain
unchanged. The two source corrections were made only after that seal.

Final source identities:

| Source | SHA-256 |
|---|---|
| `LOCAL_GIBBS_RECORD_CIRCULATIONS.md` | `70a9abf1588e90e8a7065a5e1d6155f8f56997672b0303c0ea6cbca71fc1bf12` |
| `GIBBS_TRANSPORT_COUNTERCONTROL_1D.md` | `28949032a1b110e642a8d3765dd880a4d8487be02cc70b3b095275d7cde59069` |

The pre-checker seal is
`a9709714b8474a7dd96f49f44135f814323094351531ed73800097a98e0f9a05`;
the unchanged independent checker is
`1e40a0be9cad55574791f131614a4999b3c082425d2ffbaad7aaea2f7409e2b7`.
Fourteen exact control groups passed on the first execution. They supplement
the general arguments below; their count is not proof of the all-volume
or all-parameter claims.

## 1. Exact Gibbs invariance and local rates

Write `eta_j=R^j eta` for an orbit of one plaquette permutation. Its length
`ell` divides four. Its chemical count weight and `H_out=H-H_S` are constant.
For either circulation sign, orbit invariance of `a` gives

    pi(eta_j) a(eta_j) exp(H_S(eta_j))
      = Z^-1 a(eta) exp[-H_out(eta) + lambda.N(eta)] = F.

The `ell` transitions form a constant-flow directed cycle. Its incoming
and outgoing flows balance at each state. This remains true at lengths one
and two: a length-one self-transition contributes zero, and two separately
defined directions can lead to the same successor and must be added.
Summing these generators preserves the grand Gibbs measure. Conditioning
on conserved label counts preserves it as well. The same proof works for
the conditional law with fixed exterior and a fixed multiset on the square;
the normalizing constant is irrelevant.

Only interactions touching the square appear in the rate, so the rate is
local. For a fixed bounded finite-range interaction, `|H_S|<=C` independently
of volume. A fixed local finite-alphabet amplitude is bounded. **Generic
nonnegative amplitudes give nonnegative rates, not necessarily strictly
positive rates.** The later choice `a_±=nu(1±epsilon chi)`, `nu>0`,
`|epsilon|<1`, is strictly positive, with bounds

    nu(1-|epsilon|) exp(-C) <= r_±
                            <= nu(1+|epsilon|) exp(C).

For the nearest-neighbor example `H=-K sum t_x.t_y`, `|t|<=1` and there are
twenty bonds touching a square, so `C=20|K|` is a valid simple bound.

The added Metropolis transposition has Gibbs edge flow proportional to
`min(exp(-H(eta)),exp(-H(eta^xy)))`, with the same count factor. This is
symmetric. Every nearest-neighbor transposition has positive rate, and
adjacent transpositions on a connected graph generate every permutation.
Thus each finite label-count sector is irreducible and has the unique
canonical Gibbs law. For tagged records, equal-content swaps must still
be retained when they change the tagged state; only true self-transitions
may be dropped. With that interpretation, the same permutation argument
works for tags. There is no uniform mixing-time claim.

Our independent 256-state square generator uses a genuine nonuniform
fixed exterior, a pair Hamiltonian with integer powers of two as Gibbs
weights, four symbols, arbitrary positive rational chemical weights,
the proposed circulation and a positive Metropolis component. Its exact
stationarity residual vanishes. Reversing the energy sign in the rate or
using a non-orbit-invariant amplitude produces nonzero residuals; the
first respective residual witnesses are `65025/128` and `-1`.

## 2. Cubic action, irreversibility and supplied correlations

For an orthogonal signed permutation Q, the required label action is

    e -> Q e,    b -> det(Q) Q b.

The oriented square normal transforms as
`n -> det(Q) Q n`, because it is the cross product of two edge vectors.
Consequently `n.sum b/4` is unchanged under all 48 actions. The pair
interaction `e.e' + b.b'/4` is unchanged too. Reversing the convention for
the square changes both `n` and the sense of `R`, exchanging `a_+` and
`a_-`; the generator is unchanged. These statements establish the full
rate covariance, conditional on the supplied Hamiltonian having the stated
symmetry. The checker verifies all 48 menu permutations, all 10,800
transformed pair scores and all individual axial contractions; linearity
then covers every square configuration.

On a length-four orbit with nonzero chirality and nonzero epsilon, the
opposite edge-flow ratio is `(1+epsilon chi)/(1-epsilon chi)`. For four
distinct labels, `R eta` differs from `R^-1 eta` on all four sites. That
transition is supported on exactly this square, and cannot be canceled
by another square or a two-site swap. Our explicit four-distinct-label
state has flow ratio `9/7`, confirming nonreversibility of the combined
finite generator. Length-two or zero-chirality orbits need not be
irreversible, and epsilon zero removes this drive.

On a square with vacant exterior, two `+e1` and two `-e1` labels have
internal energies `4K` in alternating order and zero in adjacent-pair
order, hence relative weight `exp(-4K)`. Nontrivial supplied interactions
can therefore change same-count arrangement probabilities. With arbitrary
occupied exterior, boundary terms must also be included; the isolated
square example should be read with that boundary fixed or vacant.
At K zero, or for a count-only Hamiltonian, the law reduces to the old
uniform canonical law. Correlations of a chosen vector observable and a
particular thermodynamic phase do not follow from nonuniformity alone.

## 3. Permanent formation, displacement cancellation and Euler scope

For V vacancies, any conservative permutation gives `L_cons V=0`.
Single-site births with total rate `b_x>=b_min>0` at each vacancy give

    L V = -sum_(vacant x) b_x <= -b_min V.

Every finite stationary law must have zero expected vacancies and hence
be supported on full occupancy. Let `H_v=sum_(q=1)^v 1/q`, `H_0=0`.
Before filling, `L[H_V/b_min]<=-1`, since one birth changes H_V by `-1/V`.
Optional stopping on the finite chain gives
`E tau_fill <= H_(V_initial)/b_min`; in particular filling is almost sure.
Constant total birth rate b_min at each vacancy attains the bound regardless
of intervening conservative motion. Our exact count test gives `H_4=25/12`
at b_min one and a strictly negative vacancy drift in the positive grand
Gibbs law. Thus that law cannot remain stationary after such births.

After filling, the finite irreducible conservative count-sector chain
converges to its canonical Gibbs measure. The late law is the mixture
selected by the random final counts. No infinite-volume phase, count law,
uniform mixing estimate, or old product Euler trajectory is supplied by
this argument.

For a closed configuration cycle supported in a bounded contractible
region, choose one consistent lift of that region into Z^3. For each label
define the position moment `M_a=sum_x x 1_(eta_x=a)`. Each physical local
transition has displacement `Delta M_a`; over a closed cycle it sums to
zero. Multiplication by the constant stationary cycle flow does not
change the cancellation. Reverse cycles and reversible edge pairs have
the same property, and exterior conditioning does not affect it.

The result is exactly zero spatially averaged homogeneous Gibbs current
for every chemical potential. Translation invariance converts the spatial
average into current per unit volume/direction. Our full conditional
generator has zero weighted displacement current for all four labels,
including orbit lengths one, two and four. This does **not** say that the
configuration-space circulation flow vanishes.

An Euler closure whose constitutive flux is this homogeneous mean current
has identically zero flux and flux Jacobian. The conclusion is conditional
on that closure and these additive conserved fields. It proves neither
hydrodynamic convergence nor absence of diffusive or other modes.
Importantly, locality of individual transitions is weaker than a
decomposition into bounded contractible configuration cycles.

## 4. KLS certificate and transfer-matrix formulas

For a current word `(a,0,1,d)`, the incoming predecessor is `(a,1,0,d)`.
Its Gibbs weight ratio is `z^(a-d)`. A current `(a,1,0,d)` has an outgoing
move at the stated `r_ad`. Hence the master-equation residual divided by
the configuration weight is exactly

    F(a,b,c,d)=1_(bc=01) r_ad z^(a-d)-1_(bc=10) r_ad.

Solving the 16 symbolic equations `F=h(abc)-h(bcd)` with `h(000)=0`
uniquely gives the note's table, including the factors `2/(1+z)` and
`(z-1)/(z+1)`. This is an identity of rational functions for every z>0;
kappa multiplies h. Its periodic telescoping proves stationarity at all
N>=4 and arbitrary finite chemical potential. Fixed-count restrictions
remain stationary because every jump conserves counts.

Separately assembled complete generators at N=4,5,6, each at three rational
parameter pairs, give exact zero stationarity residual. Their positive
currents agree with the finite transfer expression

    P_N(a,b,c,d)
      = T_ab T_bc T_cd (T^(N-3))_da / Tr(T^N).

For finite J and mu the transfer matrix is strictly positive. Perron-Frobenius
gives a positive normalized eigenvector v and simple largest eigenvalue
Lambda, with `|Lambda_2/Lambda|<1`. The limit of the displayed finite formula
is `v_a T_ab T_bc T_cd v_d/Lambda^3`. Its associated stochastic transition
matrix is `P_ab=T_ab v_b/(Lambda v_a)` and stationary law `v_a^2`.
The one-dimensional centered subspace of functions on {0,1} has eigenvalue
`u=Lambda_2/Lambda`, which directly proves

    Cov(sigma_0,sigma_r)=rho(1-rho) u^r, rho=v_1^2.

The four-word current is a sum of strictly positive terms and is therefore
strictly positive in the grand law. In the empty/full binary count sectors
it is zero; the positive-current claim is not a claim about those sectors.
Since `det T=exp(mu)(z-1)`, a nonzero finite J gives a nonzero nearest-neighbor
covariance. Antiferromagnetic J gives negative u and alternating correlations.
All these finite-parameter correlations decay exponentially, not critically.

At J zero the independent Bernoulli law gives `j=kappa rho(1-rho)`.
An additional exact check at half density, `mu=-J`, yields

    u=(sqrt(z)-1)/(sqrt(z)+1),
    j=kappa sqrt(z)/[(1+sqrt(z))(1+z)].

At z=1/4,1,4, kappa one, the respective exact currents are `4/15,1/4,2/15`
and eigenvalue ratios `-1/3,0,1/3`. These independently check the current
and correlation normalizations with attraction and repulsion.

There is no contradiction with §3: a single class-1 record on a five-site
ring makes five allowed clockwise moves to return to its original
configuration, carrying physical displacement five. Its canonical current
per bond is `kappa/5`. The wrapped coordinate moment telescopes to zero
only because the boundary jump has coordinate increment -4 instead of
physical increment +1. This is precisely the winding hypothesis excluded
from the contractible-cycle argument.

## 5. Fine labels and the vector-covariance boundary

For a genuine partition of the whole menu into classes A and B, put
`Z_A=sum_(a in A) exp(lambda_a)` and similarly Z_B. Summing the fine Gibbs
weights over labels at fixed class configuration gives
`Z_B^N exp[-H(sigma)+(log Z_A/Z_B)sum sigma]`.
Thus the class chemical potential is `mu=log(Z_A/Z_B)`. Conditional on the
entire class configuration, fine labels are independent across sites, with
probabilities proportional to their chemical weights inside the specified
class. A cross-class swap preserves every fine count, so its chemical
factor cancels in the Gibbs ratio and the same pointwise F certificate
applies. Symmetric same-class swaps satisfy detailed balance. Our separate
256-state four-fine-label generator verifies this with nonuniform chemical
weights and a positive same-class swap rate.

With equal chemical potentials within the six-axis and eight-cube orbits,
both raw vector means within each orbit vanish. A vacancy has zero vectors.
Therefore each conditional vector mean given the class field vanishes,
and conditional site independence gives zero distinct-site covariance of
every pair of raw e/b components in this grand law. Scalar class covariance
can remain nonzero. The check explicitly assigns vacancy to B, uses all
15 labels, obtains zero 6-by-6 vector covariance, and a strictly positive
scalar covariance `762801276816/17830021398721` on a four-site ring.

This is a **grand-law** statement. Conditioning on fixed fine counts removes
conditional independence: four all-A sites with exactly two `+e1` and two
`-e1` give distinct-site component covariance `-1/3`. Thus the zero-vector
claim must not be imported into an arbitrary fine-count canonical sector.
The note currently scopes that claim correctly to the grand Gibbs law.

The source correction now explicitly uses the fully occupied fourteen-label
restriction for its six-axis/eight-cube partition. If vacancy is retained in
a separate fifteen-label version, it must be assigned to a class explicitly;
either assignment preserves the zero-mean vector argument because its
feature is zero. The independent fifteen-label control above checks this
extension with vacancy assigned to B; the corrected source itself claims
the fourteen-label restriction. The chain direction still breaks spatial
cubic symmetry.

## 6. Complete author-source comparison

After the initial seal I read both complete author checkers, both full
result JSON files and both full execution logs. No author scientific
execution was repeated. `compare_sources.py` authenticates source/result/log
bindings and the complete correction diff; `SOURCE_COMPARISON.json` records
the exact identities. The reported author control groups are 12 plus 5.
Authentication of those records is not additional independent calculation.

The circulation checker is SHA-256
`f0c012e63355ed14f90ff7ed7e4247a521d427ceaddeffd49f84c353e2cc0037`.
Its 4,096-state generator is a four-label, six-site projected-feature
diagnostic, with boundary interactions and one exterior-only interaction.
The stationary generator residual, constant orbit flows and nonreversible
witness are computed in floating point. It is not a full fifteen-label
cubic-lattice enumeration. Its exact square-energy calculation and
48-action chirality control have the advertised narrower meanings.
The general cycle-flow proof and the conditional full48 covariance are
reconstructed above; the independent checker also uses all fifteen labels
for the pair-energy/group identities and an exact rational conditional
finite generator. This avoids treating a floating-point residual or a
single symmetry test configuration as the proof.

The one-dimensional checker is SHA-256
`6eae0e4d6899e907b6c09e9a5bcc6038df13a8b2f17280ea6fa3f75b3426e34a`.
Its all-z sixteen-word identity is symbolic. Its complete binary and
four-fine-label generators and transfer matrices use floating point.
The displayed finite-N currents are compared with the appropriate finite
transfer formula; small nonzero errors against the infinite-ring current
are reported as finite-size differences, not falsely asserted to vanish.
The raw-vector averaging check covers the occupied orbit means. The
independent exact controls verify both the intended grand-law result and
a fixed-fine-count counterexample outside that scope. No implementation
factor, direction convention, conservation, current or covariance mismatch
was found.

## 7. Narrow correction acknowledgment

**F1: closed.** In the generic circulation construction, the sentence
“positive bounded local rates” is now “nonnegative bounded local rates.”
The later stated parameter family has its own strict positive lower bound.
The original note identity was
`ee45014c7b58d32fee3f26c1eac01dbe4047ec5294464724d648e71a76406f8d`.

**F2: closed.** The fine-label orbit paragraph now explicitly refers to the
fully occupied fourteen-label restriction. The earlier paragraph allowing
an extra vacancy label assigned to a class remains a separate extension.
The original note identity was
`31a83be65af3f7066490631e01789d3e09bf00414f4391c605a97366c8937485`.

Both original notes are byte-preserved in
`../gibbs_transport_corrections/*.md.before`. I verified those bytes against
the initial seal, rebuilt the complete unified diff, and checked that the
exact inverse replacement recovers each original. The diff SHA-256 is
`60895ff36ac8a3fff3bdf61bc12f856fea58db96f88aa9eea84a87d3325e68e2`.
No formula, Hamiltonian, rate definition, checker or result was changed.
`CORRECTION_ACK.json` binds the exact revisions and closes both findings.

## 8. Established machinery and external source boundary

The circulation construction uses established divergence-free Markov-flow
and local-cycle machinery. I checked De Carlo and Gabrielli,
[Gibbsian stationary non equilibrium states, arXiv:1703.02418v3](https://arxiv.org/abs/1703.02418v3),
equations (13)-(15), the construction (50)-(51), and §3.7's winding examples.
Equation (52) is the current definition at the start of §4. No hydrodynamic
convergence theorem is imported from that discussion.

For the one-dimensional comparison I checked Luck and Godreche,
[Nonequilibrium stationary states with Gibbs measure for two or three species, cond-mat/0604274v2](https://arxiv.org/abs/cond-mat/0604274v2),
§2/Table 2 and (2.20)-(2.30). The rates agree with their totally asymmetric
heat-bath model under `J_spin=J_binary/4`, up to count-dependent energy
terms, and kappa=1/2 in their time convention. This is established KLS
structure, not claimed as a novel method. The table identity and transfer
calculations above were independently reconstructed.

Version-specific PDFs were read through the web PDF text and downloaded
only into this deliverable directory for source identification:

| External source | Bytes | SHA-256 |
|---|---:|---|
| De Carlo/Gabrielli v3 | 415034 | `9db3f36bc5d5614692acbef74cb446ece27e98979d3a6196c84313e0dcc5797f` |
| Luck/Godreche v2 | 238659 | `4b3051b08964dd2cf997d7aacc52d70051e7f3287f1eb56aae1ccce1a6391c0f` |

`EXTERNAL_SOURCES.json` records URLs and the limited reading boundaries.
The full papers were not treated as imported theorems beyond those stated
sections, and no novelty was inferred from rediscovering their machinery.

## 9. Assumptions and limits retained

The circulation conclusions require a fixed bounded finite-range
interaction, orbit-invariant amplitudes, and the specified polar/axial
symmetry for the cubic statement. Its positive Metropolis component is
what gives finite-sector irreducibility. Degenerate or count-only H need
not produce new arrangement correlations. A square energy comparison
requires accounting for its exterior interactions. Tagged irreducibility
requires keeping permutations that exchange distinct tags even when their
contents coincide. None of these points changes the proved construction.

The birth conclusion is finite-volume and uses strictly positive total
formation at every vacancy with no deletion; it is not an infinite-lattice
global-filling claim. The Euler-current statement is conditional on local
equilibrium and the indicated definition of conserved-field flux. The KLS
comparison is directional and one-dimensional; finite J, mu and positive
kappa are essential to its stated strict positivity and exponential
correlation properties. Zero-current all-one/all-zero canonical binary
sectors, J=0 independence, and singular parameter limits are not exceptions
to the correctly scoped statements.

The fine-label lift has a supplied scalar interaction. In the symmetric
occupied-orbit grand law it has no distinct-site raw-vector covariance.
It therefore does not solve the requested combination of a three-dimensional
cubic-covariant correlated vector state, nonzero relevant transport and a
proved collective limit. The notes keep that construction problem open.

## 10. Evidence, failures and disposition

`INITIAL_DERIVATION.md`, `independent_check.py`, `INDEPENDENT_RESULTS.json`
and the full `INDEPENDENT_CHECK.log` are unchanged from the pre-checker
seal. The scientific execution had no failed attempt. Wrong-energy-sign
and non-orbit-invariant-amplitude controls do fail stationarity as intended
and their exact witnesses are preserved; the winding and fixed-fine-count
controls preserve the important limits of the cancellation statements.
The post-source comparison passed on its first execution; its full log,
source identities and correction acknowledgment are retained.

All newly written files are in `gibbs_transport_independent/`. The reviewer
changed no production note, checker, Git state, PR, audit result, model or
reasoning setting and launched no agents. The author made only the two
acknowledged source-wording corrections. This is a completed bounded
scientific check, with no unresolved finding in the stated comparison and
no formal retained/audit verdict.
