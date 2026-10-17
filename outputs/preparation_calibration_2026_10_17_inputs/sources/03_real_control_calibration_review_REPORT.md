# Selective analytical review of the real-control calibration contract

## 1. Finding, scope and source exposure

The proposed finite-box conclusion is supported by the analytical checks
below, conditional on the unchanged parent runtime and nominal preparation
premises. No blocking mathematical failure was found in the claimed
`0 <= eta <= 10^-5`, `0 <= epsilon <= 10^-9` box. The complete finite
output trace error is strictly below `.00996404 < .01`, with the same
finite apparatus, old age, common profile, central residual and output
registers as the parent.

One substantive proof clarification is needed in proposal lines
105–110. Its seed promise is a lower bound on success probability, so the
actual deficiency is `d <= epsilon`. The disturbance from the actual
subnormalized projected state is bounded by `sqrt(d(4-3d))`, not in general
by `sqrt(epsilon(4-3epsilon))` for every `epsilon in [0,1]`. The final
function `g(d)=d+sqrt(d(4-3d))` is monotone on `[0,1]`, which proves the
stated final `g(epsilon)` inequality. Section 5 gives the proof and an exact
two-dimensional counterexample to the intermediate wording. This is a
proof clarification, not a counterexample to equation (4), and the existing
intermediate inequality is valid in the displayed small-epsilon box.
There is also a minor strict-endpoint correction in proposal equation (1):
when `eta=0`, its final `eta Bcal < 10eta` should be non-strict. The
later strict complete-output ceilings remain valid because their nominal
runtime/preparation budgets have separate strict slack.

This is a source-exposed selective review. I authored the earlier exact
product preparation and the real local preparation used here, and I knew
the realifier and resonance dependencies before this assignment. The root
proposal was supplied in full before this derivation. The same inherited
model and reasoning effort are used. Neither blindness, model diversity,
nor independent revalidation of the entire parent scattering chain is
claimed. Root retains source disposition and all publication decisions.
This packet is separate from the current real-control publication.

No scientific program, source checker, matrix computation, sampled parameter
check, optimizer or mutation ran for this review. The decisive checks are
the full-space Duhamel calculation, purification algebra, two-isometry trace
expansion, variation bounds and extensive-energy example written below.
Metadata copying/hashing is recorded separately and is not scientific
corroboration. No prompt, axiom, repository, Git, checkpoint or audit verdict
was changed. There was no delegation or other-chat message.

## 2. Exact sources and inherited premises

The reviewed proposal is [the byte-preserved source](inputs/candidate/PROPOSAL.md),
9298 bytes, SHA256
`64d81ab828fe2ad28efd526350f8f0286bd07455db0bab9686f2053008c35adc`.
Its candidate freeze is
`e273aea0b6ee119df774582333c97857c2ac6461e30275f9e0a6696264ea3ecd`;
its source map is
`7a9fc3b11f9f751b86ee56f1fed2d85ca25ec729e71ce5be4a8998da80be8a5b`.
All twelve explicitly frozen candidate members plus the candidate freeze
are copied unchanged here; the nine original/snapshot pairs were also
checked against their actual original bytes. See [SOURCE_MAP.json](SOURCE_MAP.json).

The load-bearing inherited source pins are:

| Source | SHA256 | Use in this review |
|---|---|---|
| Realifier `ROUTE.md` | `c1cf729c2639d682a66df72b880c529dbabfc1768935ae62d170538973ce2018` | Exact positive full-qubit runtime, chiral invariant-sector map, scalar and geometry |
| Real preparation `CANDIDATE.md` | `57e1cebcee12bf6499564051f91f981fe11814d73d45b9e1168c045e65ab9b8c` | Exact controls, nominal supported setup, resource formulas and qualified resonance interface |
| Joint root `ACCEPTANCE.json` | `98315ba16275ceb44dd3fcf32d655d1e92d42da7c7678600327be89d9d1ba852` | Existing conditional source status only |
| Joint root `QUALIFICATION.md` | `4ac00b22cc37f4e2d4179ca0963f7228a16e5512663c86ebe04e34d23f0c70b4` | Exact scope and remaining parent limitations |
| Earlier product preparation `CANDIDATE.md` | `b7ef6e98b16bcffb609cbf8a9cca2aee03d4bb20ac6295e99c744f488ad14227` | Historical rank-one seed lemma; algebra rederived in section 5 |
| Earlier product root acceptance | `43e1609d6e38b2220e35e1637428263e49b38d1ac22ed282ee64f3d7d3f60ca5` | Preserved historical source record; no thermal apparatus is imported |

The root qualification is read as a source decision, not retained audit or
native implementation. Its notice about the historical preparation runner's
non-discriminating ramp-budget comparison remains in force. That historical
passing clause is not used as proof here. The analytical Gram/Duhamel
argument is the inherited preparation premise.

The unchanged family has

    K = 2I + Z1 Z2,
    W = [(9+12i)I + (-16+12i)X1 X2]/25,
    kappa in [10^-12,10^-8], sigma=10^-6,
    T=kappa^-2, M=ceil(50T), M>=16.

All static runtime coefficients remain their pinned exact values. The real
apparatus uses `2M+6` physical qubits. Its finite full Hamiltonian is
`H=HR,M`; no old pair encoding or replacement occurs. The comparison space
is the same space into which the finite clock and the normalized infinite
output are embedded in the parent. The finite evolution is not compared
with a separately truncated and renormalized output packet.

Write `E0=2J(1-cos k0)`, `c=cos(2k0)`, `s=sin(2k0)` and
`d_c=1+c+s` to avoid confusing this coupling notation with seed deficiency.
The inherited scalars are

    cR = 2nu + 2kappa d_c,
    cseed = E0 + cR,
    r = 4J + 3kappa d_c,
    Phi = 5cseed + 4r + 3pi/4.

The nominal five-unit setup obeys, in operator norm on all old columns,

    ||U0 E_e0 - exp(-iPhi) E_chi exp(-5iK)|| <= sqrt(2)kappa,

where `E_chi=(E_e0-i E_e1)/sqrt(2)`. The already qualified runtime
intertwining yields finite complete error `<.004832` from `E_chi` on
`[T,2T]`, and infinite complete error `<.003832` for every `t>=T`.
Both include the actual common profile, all four old columns at their
old-dependent total energies, and the fixed nonzero central residual.
I reuse these premises, without claiming a fresh interval, bound-state,
threshold, normalization or scattering proof. The new larger-coupling
feasibility packet is not used.

## 3. Whole-block calibration budget on the full finite space

Put the fourteen fixed PSD blocks in order as follows. Blocks 1–9 are
the eight edge complements and one positive pin making up `R`. Blocks
10–14 are `Q_e0,m(+1)`, `n_e1`, `Q_m,e1(-1)`, `n_e0`, `n_e1`,
with respective profiles `w1,w1,w2,w2,w3`. The repeated onsite matrix
belongs to two different time channels. Each of the fourteen factors
`1+xi_a` is constant, with `|xi_a|<=eta`, `0<=eta<1`.

For a signed real hopping `h`,

    Q_uv(h)=|h|(n_u+n_v)+h(a_u^dagger a_v+a_v^dagger a_u)

has eigenvalues `{0,0,2|h|,2|h|}` on the complete two-qubit space.
The complement `2|h|I_uv-Q_uv(h)` has the same eigenvalue multiset.
Thus both norms are `2|h|`, while `||n||=1`. These are full positive
block norms. They are not norms of hopping-only representatives after
discarding identity terms.

The isolation norm sum is the exact expression

    Aiso = sum_(a=1)^9 ||R_a||
          =4J+4kappa d_c+E0-kappa <1/7.

With nominal nonnegative profiles `p_a(s)`, the error is

    DeltaA(s)=A_xi(s)-A0(s)=sum_a xi_a p_a(s) B_a.

For the full propagators, differentiation of `U_xi(5,s)U0(s,0)` gives
the exact variation-of-constants identity

    U_xi(5,0)-U0(5,0)
      = -i integral_0^5 U_xi(5,s) DeltaA(s) U0(s,0) ds.

Unitarity and the triangle inequality imply

    ||U_xi-U0|| <= integral_0^5 ||DeltaA(s)|| ds
      <= eta sum_a ||B_a|| integral_0^5 p_a(s) ds
      = eta [4Aiso + 3pi/4 + 3pi/2 + pi/2]
      = eta Bcal,
    Bcal := 4Aiso+11pi/4 < 4/7+121/14=129/14<10.

The exact three pulse contributions are `(2+1)pi/4`,
`(2+1)pi/2`, and `pi/2`. No cancellation, core invariance or correct
chirality is needed for the actual perturbed trajectory in this estimate.
The static base Hamiltonian cancels from the Duhamel difference. Its
extensive norm never enters. Tensoring with a passive reference preserves
this operator norm. This proves the stated independence from clock length
and from the input state for each finite apparatus.

For the endpoint `eta=0`, write `||U_xi-U0||<=eta Bcal<=10eta`,
or state the final strict inequality only for `eta>0`. At zero all
calibration errors vanish and both sides are zero. This minor correction
to proposal line 51 does not affect any later strict output bound.

Consequently the perturbed preparation satisfies

    ||U_xi E_e0 - exp(-iPhi) E_chi exp(-5iK)||
       <= sqrt(2)kappa + eta Bcal.

The approximation is to the specified nominal phase and state. Independent
amplitude errors generally destroy exact core cancellation and the exact
pulse product; no exact perturbed core theorem is being asserted. All
resulting leakage, including old/source entanglement, is in the norm error.

## 4. Scalar, old-aging and complete runtime composition

The whole-block error includes all identity terms. To make this explicit,
let `alpha_a` be the normalized-trace identity coefficient of isolation
block `R_a`. An edge complement has `alpha_a=|h|`; the pin has
`alpha_9=(E0-kappa)/2`. Thus

    alpha_iso = sum_a alpha_a = Aiso/2.

The full-space identity coefficients of `Q(+1)` and `Q(-1)` are one,
and that of an occupation is one half. If the ordered channel errors are
those of section 3, the exact change of the integrated Pauli-identity
coefficient during setup is

    delta_theta = 4 sum_(a=1)^9 xi_a alpha_a
       +(pi/4)xi_10+(pi/8)xi_11
       +(pi/2)xi_12+(pi/4)xi_13+(pi/4)xi_14.

In particular `|delta_theta| <= eta[2Aiso+11pi/8]`. The unchanged
runtime identity contribution `5alpha_R` can be extensive but is common
to both propagators. The actual integrated full-space identity coefficient
is `5alpha_R+4alpha_iso+11pi/8+delta_theta`. This is distinct from
the supported comparison phase `Phi`: nonidentity terms act nontrivially
on the core, and the `2I` in the literal old `K` is already retained in
`exp(-5iK)`. The perturbative bound has already charged this scalar
difference; adding it again would double count it.

After setup, all added controls are zero. Multiply the entire setup
difference by the same runtime unitary, with no change in its norm. The
inherited runtime implication then gives

    ||exp(-itH)U_xi E_e0 - V_t||
      < .004832 + sqrt(2)kappa + eta Bcal
      < .00483202 + 10eta,

    V_t = zeta exp[-i(Phi+cR t)] B_t^R exp[-i(t+5)K] W,
    t in [T,2T].

Here `|zeta|=1` and `B_t^R` is the same complete common output
isometry from the parent. The aging identity uses only

    exp(-itK) W exp(-5iK) = exp[-i(t+5)K] W,

because `[W,K]=0`. It does not assume `[H,K]=0`; the latter is
generally false. The actual preparation is not assigned an exact old
factorization. Total elapsed time is `5+t`, with no age reset on release.

There is no factor of the later runtime `t` multiplying the control
calibration error: the two full Hamiltonians agree after time 5. This
would not hold for a calibration error left on in the runtime. The fixed
central residual is not removed, the original sigma and kappa interval are
not enlarged, and arbitrary-accuracy closure is not obtained.

For any old/reference density matrix `rho`, isometries `F,V` with
`||F-V||<=delta` give

    F rho F* - V rho V*
       = (F-V)rho F* + V rho(F*-V*),
    ||F rho F* - V rho V*||_1 <= 2delta.

This applies after tensoring the passive reference. The finite-state
embedding into the common comparison space is an isometry too, so it
preserves trace distance, including for actual components outside the
one-head ideal branch. Thus the pure auxiliary seed gives unhalved trace
error `<.00966404+20eta`, and `<.00986404` at `eta=10^-5`.
All old/reference/source/emitter/rail outputs are retained.

The same bounded local control perturbation can be used on the inherited
infinite representation, where it is a bounded perturbation of the same
self-adjoint base dynamics. Conditional on that parent representation,
the infinite complete operator ceiling becomes `.00383202+10eta` for
`t>=T`. This does not turn any fixed finite apparatus into an all-future
device. The new imperfect-input trace claim below is made for the finite
apparatus and needs no infinite many-head or energy-domain extension.

## 5. Full joint seed implication and the necessary wording repair

Let `X=DR` denote the actual old pair and an arbitrary passive reference,
and let `A` include every source, emitter and clock qubit. The pure
auxiliary vector `|s>=|e0>` means exactly the full prescribed seed.
For any joint density matrix `omega_XA`, set

    P=I_X tensor |s><s|,
    d=Tr[(I-P)omega],
    rho_X=Tr_A omega,
    tau_X=<s|omega|s>.

The input promise is `0<=d<=epsilon<=1`. It need not specify `d`
exactly. Purify `omega` to `|Psi>` and apply `P` also to that purification.
Its good and bad components have squared norms `1-d` and `d`.
In their normalized two-dimensional basis, the difference from the
subnormalized projected pure state is

    |Psi><Psi|-P|Psi><Psi|P
      = [[0, sqrt(d(1-d))], [sqrt(d(1-d)), d]].

Its eigenvalues are

    (d +/- sqrt(4d-3d^2))/2.

Therefore its trace norm is `f(d)=sqrt(d(4-3d))`, with the endpoint
cases obtained directly or by continuity. Partial-trace contractivity
implies

    ||omega-Pomega P||_1 <= f(d).

Also `Pomega P=tau_X tensor |s><s|`. In an auxiliary basis starting
with `|s>`, off-diagonal auxiliary blocks disappear under partial trace,
so

    rho_X-tau_X = Tr_A[(I-P)omega(I-P)] >=0,
    ||rho_X-tau_X||_1 = d.

No conditioning, discarded output or factorization assumption is present.
The triangle inequality gives the bound to the actual unconditioned
old/reference marginal:

    ||omega-rho_X tensor |s><s|||_1 <= g(d),
    g(x)=x+sqrt(x(4-3x)).

It remains to replace `d` by the supplied upper bound. For `0<x<1`,

    g'(x)=1+(2-3x)/sqrt(4x-3x^2).

This is nonnegative for `x<=2/3`. For `x>=2/3`, both sides in the
comparison `sqrt(4x-3x^2)>=3x-2` are nonnegative, and their squared
difference is

    (4x-3x^2)-(3x-2)^2 = 4(1-x)(3x-1) >=0.

Thus `g` is monotone on `[0,1]`, by continuity also at the endpoints.
It follows that

    ||omega-rho_X tensor |s><s|||_1
      <=g(d)<=g(epsilon)
      <=epsilon+2sqrt(epsilon)<=3sqrt(epsilon).

This proves proposal equation (4) for a probability lower bound, including
arbitrary old/reference correlations. Exact rank-one purity at `epsilon=0`
forces the product state, but nonzero deficiency does not.

The intermediate wording at proposal lines 105–109 is too broad if used
for arbitrary `epsilon in [0,1]`. Take a one-dimensional `X`, a
two-dimensional auxiliary, and

    |Psi>=sqrt(1/3)|s>+sqrt(2/3)|b>, <s|b>=0.

Its actual deficiency is `d=2/3`, allowed by `epsilon=1`. Its distance
from the subnormalized good block is `2/sqrt(3)>1`, whereas
`sqrt(epsilon(4-3epsilon))=1`. This exact small counterexample requires
no numerical run. It refutes that intermediate substitution, not the final
claim: `g(1)=2` remains a valid upper bound.

The narrow replacement text is:

> Let `d=1-Tr(Pomega)<=epsilon`, with `0<=epsilon<=1`. Projection
> costs at most `sqrt(d(4-3d))`, and replacing the subnormalized
> old/reference marginal by the actual marginal costs `d`. Their sum is
> `g(d)<=g(epsilon)` because `g` is increasing on `[0,1]`.

Alternatively restricting the intermediate argument to `epsilon<=2/3`
would suffice for the displayed numerical box, but the replacement above
preserves the general statement. It adds no new preparation mechanism.

## 6. Complete imperfect-input composition

Let `F_t` denote the actual full setup-plus-runtime isometry into the
comparison space. First compare `F_t omega F_t*` with
`F_t(rho_X tensor |s><s|)F_t*`. Their trace distance is unchanged
by the actual common unitary and embedding, and is at most `g(epsilon)`.
Next compare the latter state with the ideal complete output defined by
`V_t rho_X V_t*`, using section 4. The result is

    ||rho_actual,out(t)-V_t rho_X V_t*||_1
       < g(epsilon)+.00966404+20eta,
       t in [T,2T].

No isometry statement is asserted about a mixed preparation input. The
actual reference marginal is retained, as are all bad-sector weights and
coherences. The possible bad branch is never supplied to the one-head
runtime theorem; it is propagated by the actual full finite unitary and
handled by trace-distance stability.

At `eta<=10^-5` and `epsilon<=10^-9`,

    g(epsilon)+.00966404+20eta
      <=3sqrt(10^-9)+.00986404
      <.00996404<.01.

The middle strict inequality follows exactly from `9*10^-9<10^-8`
by squaring positive quantities. These are unhalved trace distances. The
margin below `.01` from the displayed rounded bound is `.00003596`.
No product-Gibbs law is assumed or obtained. In particular the stronger
`2epsilon` estimate for a classical/product delivery cannot be substituted
for the correlated-input guarantee without a stronger input premise.

## 7. Positive supports, channel count, strengths and slew

Because `1+xi_a>0`, whole-block scaling preserves the real PSD property.
It also preserves every onsite or ordinary nearest-neighbor support and
every internal density/hopping/identity ratio in that block. A calibration
box for independently perturbed Pauli coefficients would be a different
statement and is not proved here.

There are eight complement edge channels, one isolation pin, two pair
pulse channels, two spectator onsite channels and one phase onsite channel:
`8+1+2+2+1=14`. They occupy the same eight existing sites, and use only
the same eight existing edges. The second use of `n_e1` is a separately
calibrated time channel, even if hardware were eventually shared. No new
qubit or old/source control is added. The finite runtime block count and
qubit count therefore stay those of the parent; counting all preparation
channels gives `2M+42` positive channels excluding `K`.

The source-A/B loads stay `27.936224853155858` and
`22.228906875353305`; the old added incident loads stay
`1.993757127633340` and `1.198638631120596`. The separate old edge
has norm 3. This preserves the specified old added cap two, without
claiming a cap two at all sites. For each affected site, the precise
safe transformation of its parent peak estimate is

    actual total load <= unchanged runtime load
                         +(1+eta)*(parent added-control peak load).

One must not multiply an unchanged runtime or source load by a control
calibration factor and then call that the actual calibrated apparatus.
The proposal's aggregate bounds concern the added controls only.

The parent unit profiles have `max q=15/8`,
`max |q'|=10sqrt(3)/3`, and ramp slope at most `3/2`.
For the largest pulse window, a pair-plus-spectator norm sum is at most
`3*(pi/2)*(15/8)=45pi/16`. Hence the full added-control peak sum is

    <=(1+eta)[Aiso+45pi/16] <9(1+eta).

During a ramp the incident derivative norm sum is at most
`(1+eta)(3/2)Aiso`. During the largest pulse window, an incident pair
site has derivative load at most
`(1+eta)*2*(pi/2)*(10sqrt(3)/3)`; the spectator is smaller.
Thus the maximum incident control slew is `<20(1+eta)`.
Isolation is constant while pulses run, so no ramp slew is added there.

For `eta<=10^-5` these become respectively

    <9.00009<9.001,    <20.0002<20.001.

Constant multipliers preserve the parent C1 endpoint matching, including
zero controls and zero control derivatives at initial delivery and after
time 5. A bounded but rapidly varying relative error could retain the
Duhamel integral bound while destroying the derivative/variation bounds;
the proposal correctly excludes that inference, timing errors, profile
changes, support changes and persistent runtime errors.

## 8. All-state modeled work and the energy limitation

For every finite input state, including arbitrary correlations or many-head
components, let `rho(s)` evolve with `H+A_xi(s)`. The exact finite-space
identity is

    d/ds Tr[rho(s)(H+A_xi(s))] = Tr[rho(s) dot A_xi(s)].

The commutator contribution vanishes by cyclicity of trace. Since
`A_xi(0)=A_xi(5)=0`, integration gives

    Wsetup = Tr[H rho(5)]-Tr[H rho(0)]
           = integral_0^5 Tr[rho(s) dot A_xi(s)] ds.

The state is actual, and all identity/scalar terms are retained. Each
isolation profile rises from 0 to 1 and returns to 0, with total variation
2. Each pulse profile rises once and falls once, with variation twice its
peak. The full-block variation bound therefore gives

    |Wsetup| <= integral_0^5 ||dot A_xi(s)|| ds
      <=(1+eta)[2Aiso+6 max w1+6 max w2+2 max w3]
      =(1+eta)[2Aiso+165pi/16]
      <33(1+eta)<=33.00033<33.001.

This is independent of clock length and valid for every finite input.
There is no need to claim the actual pulse has zero net work or that
the state stayed in the core. It is modeled Hamiltonian work, not the
supplier's heat, fabrication, control computation or reset cost.

The input-quality hypothesis alone gives no comparable clock-length-
independent energy or variance guarantee. For example take the old pair
in `|00>` and the auxiliary mixture

    (1-epsilon)|s><s| + epsilon |all><all|,

where `|all>` occupies every auxiliary qubit. This input meets the exact
joint seed promise and even has a product old/auxiliary state. On each
occupied clock bond, `Q(-J)` has expectation `2J`. There are two rails
with `M-1` bonds and four endpoint onsite contributions `J`. Thus the
clock energy of `|all>` is exactly

    4J(M-1)+4J = 4JM.

All other terms occupy a fixed number of sites and have expectations
independent of `M`. More explicitly the two component energy means are

    E_good = 3+E0+2nu+2kappa d_c,
    E_bad = 4JM+3+DeltaA+DeltaB+2hAB+u+gA+gB
               +2(lambdaA+lambdaB+mu0)+2E0+2kappa d_c.

These follow from the full positive-block definitions: hopping expectations
vanish on the all-occupied computational basis vector; the source vacancy
contacts vanish there; the six emitter cells plus compensators contribute
`2E0+2kappa d_c`. It is not necessary that either component be an
energy eigenstate. The mixture mean differs from `E_good` by
`epsilon(E_bad-E_good)=4J epsilon M+O(epsilon)`.

The mixture variance identity also yields

    Var_mix(H) >= epsilon(1-epsilon)(E_bad-E_good)^2,

with the nonnegative within-component variances retained. It can therefore
grow quadratically with clock length at fixed nonzero epsilon. This exact
example justifies the proposal's energy warning without pretending the
bad branch obeys one-head scattering. The bounded control work does not
remove a large incoming energy; it changes its mean by at most `33.001`.

The stated kappa interval itself has a finite maximum permitted `M`, so a
trivial finite energy bound using that maximum certainly exists. The point
is that the seed-probability contract alone does not provide a small,
clock-length-independent energy/moment continuation of the pure-seed
guarantee. It can only provide a bound that scales with the apparatus norm
or requires an additional weighted moment/tail premise. Trace-norm output
closeness and the all-state work bound are consistent with that limitation.

## 9. Coverage, evidence and remaining obligations

The complete 181-line root proposal, its full source map and freeze, and
the complete root real-control acceptance and qualification were read.
The unchanged parent realifier and real-preparation bodies were previously
read in full; the latter was authored by this reviewer. For this review,
the exact real-preparation definitions, core identity, schedules, Duhamel
statement, runtime interface, counts, resource and work sections were
refreshed (source lines 70–408 and 411–533). Earlier product preparation
lines 274–345 were refreshed for the rank-one marginal lemma, which was
then reconstructed above. Other copied historical qualification/freeze
records are preserved and hash-verified, not claimed as freshly re-reviewed
science. No source code or output was executed.

`SOURCE_MAP.json`, `CAPTURE_RECEIPT.json`, `capture.stdout` and
`capture.stderr` record the explicit metadata capture. The capture used
one subprocess with an actual 15-second external timeout, returned exit
zero in about 0.210201 seconds, and had empty stderr. No metadata failure
or scientific run occurred. Runtime identity is recorded in the source map.
The final manifest/freeze verification is likewise metadata-only. The
unchanged governing workflow hash matches
`71cab17ea2d5ec892b5d9dbefd608c0d51e77ea398a62f33679736510d9f63d3`.

The review supports only the supplied whole-block preparation calibration
and joint seed-probability implication at the unchanged exact runtime.
Native controls or cooling, pulse timing/calibration manufacture, arbitrary
Pauli coefficient noise, persistent runtime errors, long-time decoherence,
autonomous preparation, capture/reset/reuse, practical resource size and
physical Hamiltonian/energy/Record identification remain open. This review
does not qualify the separate larger-coupling route or joint static boxes.

The next decision is root's: apply the narrow `d`-first proof clarification
and the zero-calibration endpoint convention in a separate record or later
wrapper while preserving the frozen source,
then decide the conditional source disposition and whether it belongs in
a later coherent publication. No stronger theorem or retained status is
asserted by this packet.
