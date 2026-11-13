# Independent regional, chart, and radial check

Research check only; no review, audit, landing, or retained-status authority.
Checker source checkout: `fbdfb3c1b8852e5de302fab6f0f7cfc70ba04cac`.
Started 2026-11-09. This file is the checker's sole writable artifact.

Final research signal: **`advance` for the four frozen proof candidates,
conditional on the supplied global `c_J` and finite-model inputs.** The final
primary note and corrected proof map match those results. One map wording
overstatement was corrected and its exact one-sentence delta verified;
there is no remaining finding within this check's scope. Final source hashes
are consolidated in section 13; original full-read coverage and the evidence
boundary are preserved in sections 6, 10, and 12.

## 1. Independence and initial read boundary

The derivations in sections 2--5 were made before reading any new regional,
nonlinear-chart, radial-profile, or external-advice deliverable. The parent
will supply frozen candidate hashes before comparison. No old gate verdict is
an input. The initial mathematical inputs were read completely:

| Source, relative to the target pack | SHA-256 |
|---|---|
| `parts/two-plaquette-compact-coercivity.md` | `b77fdb722d19c96594cddded301d9dd019c412b875721f5c28d1461415bb246e` |
| `parts/partial-terminal-normalizer-hessian.md` | `a17f372f928930bd9be6e81d68349a62232a027f17a13a7cd47e813f43584139` |

The supplied positive compact constant `c_J` is an explicit premise, not a
recertification of all ancestors. The domain is the actual two-layer law
`q_u K0 product_O k1`, zero sources, `V_O=I`, seven deleted terminal edges
from two elementary plaquette boundaries sharing one edge, odd `L>=3`,
`m>=3`, `kappa>0`. Surviving normalizers are part of the target.

Read instructions at this checkout: root `AGENTS.md` (hash
`7def904fdd52d811e7aba87a0d3d859bfb017cccd59703125f4a53f2805aaab2`),
`SCIENCE_WORKFLOW.md` (hash
`1c5bda5db3b59963290d75420a45a4857cf7f375417d64c4275a0e49490de4ca`),
repo physics-claim-reviewer and physics-loop skills, skill-freshness and
proof-search-governance instructions. Installed copies were not used. The
parent explicitly prohibited network/Git mutation and supplied preflight and
an active science lease; freshness beyond this local revision is not claimed.
No numerical jobs were launched. Parent-reported literature triage found no
matching direct deleted-law theorem and warned that whole-space/smooth-boundary
covariance formulas alone do not establish the cube result. This report does
not treat that search report as mathematical evidence.

## 2. Independent regional-energy derivation

Let `I` be a set of retained group-link variables, and let `F(I)` be **all
complete** energy factors whose full reader sets meet `I`. The exterior
readers of these factors form a collar `C`. Define `E_I` as their sum, with
the same coefficients as `E_J`. For `x` on `I`, write `(x,1)` for its global
extension by identities. Every factor outside `F(I)` vanishes at this
configuration. Consequently the accepted global premise gives exactly

    E_I(x,1) = E_J(x,1) >= c_J sum_(i in I) [1-w(x_i)].       (I1)

No translation invariance or periodic Fourier representation is used here.
Whole-factor incidence is essential: selecting only factors entirely inside
`I` would generally omit the constraints on its boundary variables. Likewise,
deleting part of a path mean or a normalizer changes the law.

There is a volume-independent mixed-increment bound for every finite-reader
energy factor `phi`:

    |phi(x,z)-phi(x,1)-phi(1,z)+phi(1,1)|
       <= A_phi sqrt(D_I(phi)) sqrt(D_C(phi)),              (I2)

where `D` sums `1-w` over the indicated reader links. Here is a route that
does not differentiate `|M|` at `M=0`. All factors are globally Lipschitz in
chord distance: product telescoping bounds paths, averaging bounds the mean,
and `||M|-|N||<=|M-N|` bounds its norm. If both local reader configurations
are in a fixed small identity neighborhood, the mean is bounded away from
zero; a bounded mixed Hessian and radial chart paths prove (I2). If either
reader group leaves that neighborhood, its `D` exceeds a fixed positive
threshold; the global Lipschitz estimate in the other group then proves
(I2), with a larger constant. This also handles rough exterior values.
For empty reader groups the mixed increment is zero. Finite reader cardinality
and bounded incidence keep the summed constant independent of volume.

Using Young's inequality with incidence included, (I1)--(I2) therefore give
the conditional relative-energy estimate

    E_I(x,z)-E_I(1,z)
       >= (c_J/2) D_I(x) - C(L,kappa,c_J) D_C(z).          (I3)

Necessary checks on a candidate: every selected factor is complete; its
reader set is the actual reader set after forest restriction; the mixed
estimate uses the rough/smooth split rather than an invalid global Hessian
bound for `|M|`; coefficients and multiplicities survive periodic projection.
This proof uses global `c_J` directly. A localized deterministic recovery
stencil is useful but not required for (I1) if all touching factors are kept.

**Discriminator.** For the simple positive local energy
`E(x,y)=x^2+(y-x)^2`, selecting only factors with every reader in `{y}` gives
zero while the identity-exterior extension has energy `y^2`. An omitted
crossing factor thus kills a regional coercivity claim. This example tests
the selection mechanism, not the SU(2) theorem itself.

## 3. Independent nonlinear fixed-chart and inverse derivation

The allowed Hessian input gives `u^(-1) S_J''(0)>=c_J I`. To extend it to
a fixed Cartesian coordinate cube, one needs a volume-uniform local modulus
of continuity of `u^(-1)S_J''`, uniform in `u>=1`. Reader cardinality,
bounded factor incidence, smooth paths, and a lower bound `|M|>=r_*>0` on
the cube reduce this to the radial scalar bounds

    |B(s)| <= 1,   sup_(s>=s_*) s|B'(s)| < infinity,
    sup_(s>=s_*) s^2|B''(s)| < infinity,                  (I4)

where `B=(log Z)'`. These bounds imply uniformly bounded normalized third
derivatives of `-kappa*u <V,M>+log Z(kappa*u |M|)`. Haar is smooth on a
fixed injective chart and its normalized derivatives are bounded for `u>=1`.
The precise constants in a candidate must account for **complete kernels**.
The standalone normalizer has a negative Hessian at identity; it cannot be
dropped under a positivity claim.

A finite-incidence row estimate then yields

    ||u^(-1)S_J''(a)-u^(-1)S_J''(0)|| <= C max_e |a_e|.

Choosing one fixed small cube gives `S_J''(a)>=u c_J/2`. For a region with
all touching-factor readers in that cube, its conditional Hessian is a
principal compression of the Hessian at the global configuration extended
by identities. Thus it has the same lower bound even if the far exterior
is arbitrary. No such conclusion applies to a collar outside the small cube.

For any symmetric finite-range matrix `H>=lambda I` with absolute row bound
`B`, let `W_ii=exp(theta d(i,A))`. If nonzero matrix entries span distance at
most `R`, then the row and column Schur bounds give

    ||WHW^(-1)-H|| <= B(exp(theta R)-1).

If this is at most `lambda/2`, the weighted inverse has norm at most
`2/lambda`. Every principal compression inherits the gap, range, and row
bound, so no translation invariance is needed. An operator upper bound by
itself does **not** imply a uniform absolute-row bound in a growing dimension.

## 4. Independent cube covariance derivation and discriminator

Let the conditional chart law have positive smooth density proportional to
`exp(-S)` on a Cartesian cube, with `S''>=lambda I`. The scalar generator
is `L=-Delta+grad S dot grad`, with Neumann boundary conditions. For a
centered scalar `f`, solve `Lu=f` and set `w=grad u`. The vector equation is

    (L tensor I + S'') w = grad f.                         (I5)

The domain is important. Component `w_i` has zero trace on the two faces
normal to coordinate `i`, and natural Neumann conditions on every other
face. The quadratic-form domain is the product of these mixed spaces. It
is not the all-Neumann vector domain and not a whole-space inverse.

A weak justification on a cube can use the Neumann cosine basis. The scalar
weak solution has `H^2` regularity because `-Delta u=f-grad S dot grad u`
is in `L^2`; the rectangular Neumann Laplacian has the requisite `H^2`
estimate directly from its cosine expansion. Finite cosine sums approximate
in `H^2` and satisfy the face conditions. In the differentiated integration
identity, tangential derivatives of a scalar Neumann condition vanish;
normal components of vector tests vanish on their own faces. Integration
by parts on each face leaves no term. Corners have codimension at least two
and contribute no face measure. Taking the `H^2` limit gives (I5) in the
mixed vector form domain. This checks the boundary bridge rather than
importing a smooth-boundary or whole-space formula.

Then

    Cov(f,g) = <grad g, (L tensor I+S'')^(-1) grad f>_mu.   (I6)

Diagonal weights in the coordinate **labels**, constant as functions on
the cube, preserve every mixed face domain and commute with `L tensor I`.
Only `S''` changes under conjugation, so the preceding Schur perturbation
argument provides weighted covariance bounds. This construction requires a
uniform Hessian lower bound on the entire conditioned cube and a uniform
row/range bound there. It does not justify an unrestricted compact-law
covariance bound or a covariance claim with a rough collar.

**Boundary discriminator.** On `[-a,a]` with uniform density, the correct
vector operator for the observable `f(x)=x` is the Dirichlet Laplacian. Its
inverse applied to `1` is `(a^2-x^2)/2`, whose average is `a^2/3=Var(x)`.
An all-Neumann vector Laplacian has a constant zero mode and cannot supply
this inverse. More pointedly, for density proportional to
`exp(-epsilon*x^2/2)`, an incorrect all-Neumann formula returns
`1/epsilon` for `Var(x)`, while integration by parts gives

    epsilon E[x^2] = 1 - 2a exp(-epsilon*a^2/2)/Z < 1.

The positive boundary correction disproves that imported formula even in
the strictly convex one-dimensional case.

## 5. Independent radial normalization checks to apply

The exact hidden-law density has the decomposition

    exp(-u E_J) product_(surviving kernels) g(kappa*u*|M|),
    g(s)=exp(s)/Z(s),

relative to product probability Haar, with coordinate-independent factors
canceling upon normalization. Every surviving factor is included. In polar
coordinates for a retained link, Haar has radial factor `sin^2(r) dr` and
solid-angle measure; replacing it by `r^2 dr` is a comparison, not an exact
identity. A chart density additionally retains `j=(sin r/r)^2`.

For any exterior `z`, radial conditional density `p_z(r)` including all
these factors, and radial statistic `D(r)`, define the **same** partition
function

    Z_z(tau)=integral exp(tau*u*D(r)) p_z(r) dr.

Then the normalized tilted moment is exactly `Z_z(tau)/Z_z(0)`;
`d_tau log Z_z=u E_tau D` and
`d_tau^2 log Z_z=u^2 Var_tau(D)`. Constants truly independent of the
integrated variables cancel. The reference-energy factor
`exp(-u E_I(1,z))` is such a constant and cancels exactly. A collar penalty
introduced only as an upper bound, such as `exp(Cu D_C(z))` from (I3),
does **not** automatically cancel against the denominator. A candidate
must either retain it, introduce an exactly normalized compensating weight,
or prove a sharper two-sided comparison.

For source derivatives of normalized expectations, quotient differentiation
must preserve covariance subtraction. At first order,

    d_theta E_theta F = E_theta[d_theta F]
        + Cov_theta(F, d_theta log p_theta).

Higher jets include the corresponding cumulant/partition-function terms.
Any proposed ratio-jet majorant must specify the source domain and a
nonvanishing denominator there. Real positive radial tilts do not alone
provide a complex nonvanishing neighborhood uniform in volume.

**Lost-normalizer discriminator.** At a path mean of norm zero the surviving
factor is `exp(0)/Z(0)=1`. At norm one with aligned output it is
`exp(t)/Z(t)`, not `exp(t)`. Replacing the surviving normalizer by a constant
changes the radial weights. Near identity it also changes the complete
kernel Hessian from the allowed source's
`t(|b-q|^2+(1-B(t))*v)` to `t(|b-q|^2+v)`. Thus a check of only the mismatch
term cannot detect the missing normalizer; a nonzero path-variance direction
is necessary.

Initial checkpoint: independent mechanisms and discriminators recorded.
Candidate conclusions have not yet been read or assessed. Next action:
receive exact candidate hashes, read all changed arguments and necessary
source windows, and append explicit findings or a narrow research signal.

## 6. Frozen candidates and complete mathematical read

The parent released the following files after the initial checkpoint. All
three were read completely, including their hypotheses, constants, source
jets, scope statements, and provenance sections. Hashes were checked against
the release before the reads.

| Candidate | SHA-256 |
|---|---|
| `parts/marginal-nonlinear-chart-estimates.md` (397 lines) | `cbc1dd1fe3ebeb75bc4c66ff6bb364e5e4fbee3b54563a0b24fb0539aa347d6f` |
| `parts/marginal-regional-relative-coercivity.md` (356 lines) | `2d142414fb4992c2a1e907d42d15ca9f7164ee6e90c892d8c3d529b39e297385` |
| `parts/marginal-regional-moments-and-ratios.md` (432 lines) | `b2d3d9bedfb52b11056788e1f72cd14c4f9846c733c86ee424c2240f13db647f` |

No Fable advice or old gate verdict was read. Necessary model/support windows
were then inspected, rather than accepting references as proofs:

- `compact-forest-exchange.md`, sections 1--5, lines 1--205, hash
  `b0d3a76a94a8cd43de186b1c93deb38327ea2b29aa2b1bbc16e1caa2e22ecef2`:
  exact compact map, product orbit Haar, reduced readers, source covariance.
  The read command also exposed the opening of section 6, including its
  elementary pure-orbit example; no gate file linked in its header was read.
- `arbitrary-boundary-interior-moments.md`, lines 1--220 (sections 1--6), hash
  `c58acdf2d0391847c631a358fcad2bd280e8f563c19947f976118272a4426d11`:
  source of the radial-cap/tower method. Its later appendices were not needed
  because the candidate writes and is checked for its complete profile proof.
- `local-conditional-tail.md`, lines 1--195, hash
  `cf47acdfe0deea09fe49f7b08d90d45a3aac0df3251062ba4f67f566e639072d`:
  complete-factor selection, eight input-kernel incidences plus the hidden
  output, cap estimate, and source convention. No old verdict was used.
- `rough-component-bound.md`, lines 1--120, specifically the direct reader
  geometry at lines 78--88, hash
  `1a4c40385f1fc492033f261f8ed938bed23f32475eb9a116347fd7361f9e9c44`.
- `flat-two-step-bound.md`, lines 25--95 and 135--172, hash
  `0f028f694bb686cf4272d8620329f1f2e8535d8af9a2d028bbde6965cab3f03a`:
  coordinate ownership, word length, reader incidence/range. Its earlier
  Fourier lower-gap proof was not imported or recertified.
- `compact-energy-coercivity.md`, lines 1--120, hash
  `7e8e798759239aadfc8c137125bf23f6d1de2cac18b714ddca70ea294cbaa4aa`:
  model geometry only; the later global proof remains the accepted premise.
- Repository `docs/SU2_TWO_REGION_BOUNDARY_RESPONSE_BOUNDED_THEOREM_NOTE_2026-11-08.md`,
  lines 1--155, particularly the explicit paired-path definition at 69--94,
  hash `94986863c312a5880569cdf8d663c191a3d802a51542e2b671bcfdbc615e913c`.
- `sources/marginal-regional-chart-prior-art-20261109.md`, full, hash
  `0f2365732c9c48e923a16bf0a78fb7821776f3e77fe9102c0812573c0f6a7c76`.
  This is search provenance, not external theorem verification by this checker.

The old `local-relative-coercivity.md`, `nonlinear-chart-response.md` and
`buffered-core-conditional-ratio.md` hashes were verified as method provenance;
their full arguments were not used as mathematical premises. Searches exposed
some old nonlinear bounds, after the independent derivation was recorded.
All decisive adapted arguments are present in the new candidates and were
checked directly. Truncated tool outputs were reread in smaller windows before
counting their mathematical coverage as complete.

## 7. Checks of the released mathematics

### 7.1 Exact law and reader geometry

Deleting a terminal output integrates its own normalized kernel to one; it
does not delete a `K0` factor or any other terminal normalizer. The conditional
formula in each candidate keeps exactly all surviving factors meeting the
chosen reduced coordinate set. Unselected factors are constant for that
conditional and cancel. The root-fixed tree map remains a Haar-preserving
bijection after deletion because every remaining factor is separately gauge
invariant. It does not require quotienting any additional symmetry created by
deletion. The orbital source formulas therefore retain the correct joint law.

The one-cell collar and incidence claims admit a direct structural check
from the actual path definition. In a centered odd-`L` block each root leg
has length at most `4(L-1)/2`; the two legs plus the straight `L` bridge give
`5L-4`. Both legs and the bridge stay in the two adjacent blocking cubes.
An internal input edge can therefore be read only by the eight kernels
incident to its block root; a crossing edge belongs only to its face kernel.
An intermediate variable is additionally the output of its own `K0` factor,
giving at most nine output-inclusive incidences. A fine link has six
plaquette incidences. Repeated word occurrences still require the word-length
factor, which the candidate's squared conservative constants include.

Centered `L` cubes nest in centered `L^2` cubes because
`L(L-1)/2+(L-1)/2=(L^2-1)/2`. Hence all retained tail owners in a selected
factor lie within periodic terminal-cell l-infinity distance one of any
selected reader cell. Fine plaquettes have the same diameter bound. Reversed
occurrences have both endpoints in the same two blocks and do not enlarge
it. Tree restriction deletes readers; it does not replace paths by long tree
words in reduced variables. Periodic projection merges labels but retains
occurrence multiplicities. These observations justify `N_1(A)\A`, the
`24+9*kappa*(p+1)^2` energy constant, and `9*kappa*p^2` radial-deficit
constant for fixed `p=5L`, also for wrapped regions and `m=3`.

### 7.2 Regional stationary field and all-compact relative energy

The candidate proves a stronger statement than the initial identity-centered
estimate (I3). Its all-identity regional Hessian is exactly the principal
compression of the accepted full leading Hessian. The geometric series in
its equation (12) has nonnegative spectral interval below one after choosing
`M'>M`, so the operator-norm decay and ambient-distance range imply (13).
Summing the deliberately overcounting four-dimensional shells gives a finite
weighted block-sup inverse norm. This does not need a translation-invariant
forest, a connected region, or detours confined to the region.

The forcing is supported within one factor range of the exterior because
every complete factor has zero gradient at the all-identity reader field.
The stated third-derivative/incidence estimate then makes the weighted
fixed-point map a contraction with radius proportional to the collar
amplitude. Its fixed point is stationary in every group tangent direction:
the coordinate exponential map is a local diffeomorphism there. Iteration
from zero also gives the asserted continuity in the finite collar variables.

For the global compact step, I reconstructed the factorwise remainder:
subtract both the value at the stationary background and the zero-background
factor. Its global size is `O(epsilon)` by compact Lipschitz continuity.
Its local Hessian is `O(epsilon)` by the smooth background interpolation.
Subtract its linear differential paired with the common global proxy
`Im(q)`; Taylor gives `O(epsilon)*sum d(q,I)^2` in a fixed cap. Outside
the cap that sum is bounded below, so the global Lipschitz bound gives the
same estimate without differentiating a zero mean. Exact stationarity cancels
these linear proxies after summation in the same right-tangent frame.
The accepted regional baseline then absorbs the remainder for fixed small
`epsilon_*`. This proves the claimed all-compact lower bound, unique leading
minimum, and the separate cap upper bound. The proof does not imply that this
point minimizes the full finite-`u` action, as the candidate correctly states.

### 7.3 Nonlinear chart, corners, and weighted covariance

The exact identity Hessian, including the positive complete-kernel variance
correction and `2/(3u)` Haar term, matches the allowed source. The radial
cumulant argument is valid at every fixed order: under the tilted Haar law,
`X=1-w` has moments bounded by `C_n(1+z)^(-n)`, and every cumulant partition
has the same total power. This bounds the derivatives of `h(t r)` uniformly
in `u` on `r>=1/2`; the value of `h` need not be uniformly bounded. The
anchored derivative counts include all differentiated slots, and Schur row
bounds turn the local Hessian variation into a volume-uniform operator bound.
The chosen `delta` and `u_*` consequently establish the claimed convexity.
Small output fields are handled by the same smooth template argument and do
not silently extend compact coercivity to arbitrary terminal outputs.

The cube proof agrees with the independent domain analysis. The scalar
weighted Neumann problem is first solved with a possibly nonuniform gap;
rewriting it as an unweighted Neumann Poisson problem gives `H^2` regularity
and cosine-polynomial approximation on the box. For these polynomials the
normal derivative of a tangential gradient component vanishes, while the
normal vector test component vanishes on its own face. Their integration by
parts identity thus has no omitted boundary term. `H^2` convergence passes
it to the weak solution. The odd/even reflection construction gives density
in the specified mixed `H^1` vector form domain; no extra corner condition is
being assumed. The operator is a diagonal collection of mixed diffusions
plus the Hessian, not the all-Neumann operator. Constant label weights
preserve these component domains, and the bounded perturbation estimate
proves the covariance decay with `4/(u*c)`. This passes the truncated-Gaussian
discriminator in section 4. No whole-space covariance theorem is imported.

### 7.4 Arbitrary-exterior radial profile and tower

The candidate's regional lower bound comes from extending by identity beyond
the selected set and its full collar, then bounding the omitted nonnegative
factors by `K_E*T_collar`. It is valid even for rough collars and zero means.
The entire profile box `0<=theta_x<=c_J/2` leaves a lower coefficient
`c_J/2`, and the further exponential moment uses `lambda_*=c_J/4`.

The scalar comparison `H(t)exp[-t(1-r)]<=H(tr)<=H(t)` follows exactly from
`0<=(log H)'<=1`; it requires no large-`u` asymptotics. The cap denominator
and Gaussian numerator carry identical `H(kappa*u)^k` for the **actual**
selected surviving count and identical `u^(-3n/2)` for the actual integrated
coordinates. Those factors cancel algebraically in their ratio. The collar
penalty remains as `(2*K_E+K_r)*u*T_collar`, as it must. Thus the candidate
passes the failed-collar-cancellation test stated in section 5.

After Jensen, the same fixed tilted law conditioned on a smaller set has
exactly the same complete factors and profile restrictions. Taking its tower
expectation gives `m_r<=q*m_(r+1)+a*|N_r|/((1+b)*u)` with `q=b/(1+b)<1`.
This is a bound on expected radial size, not a weak-dependence assertion.
Its polynomial volume overcount remains valid when the torus balls saturate.
Integrating the exact derivative of the tilted logarithmic moment along
`theta=t*1_A` is justified throughout the profile box. The buffer selection,
Markov threshold, and final `u` threshold then give `eta(u)^|S|` under every
quotient exterior for the event that **each** cell of `S` is rough.

### 7.5 Ratios, full source jets, and independent partition arithmetic

The good event is `B_S^c`, not the event that every core/collar link is in
the small chart. Its partition function is positive, including at `delta=2`.
The identity `L_S=log Z_R-log Z_good=-log(1-p)` is exact with the original
orbit variables still integrated. Real positive finite integrals supply
the local derivatives used here; no complex zero-free neighborhood is claimed.

For the four distinct labels `s,t,c,d`, every mixed distinct-label derivative
of the log weight vanishes. Each terminal variation belongs to its own
kernel, normalizers do not depend on the terminal output, and original hidden
sources have no explicit terminal-output dependence. Thus the cumulant
identity in (28) is correct. A deleted terminal score is zero; an unselected
surviving factor cancels from the ratio and also has zero effective score.
The event indicator is fixed, so it adds no parameter derivative. The result
does not cover repeated derivatives at one terminal output.

I independently enumerated set partitions recursively in the tool runtime,
using exact small integers rather than candidate-supplied expected constants.
For `k=1,2,3,4`, summing `(|pi|-1)!` over partitions of `k+1` labels gives
`2,6,26,150`. There are 15 partitions of four labels. The computed contributions
to the fourth-order chain-rule bound were:

| Block sizes | Contribution |
|---|---:|
| 4 | 300 |
| 3,1 | 832 |
| 2,2 | 432 |
| 2,1,1 | 2304 |
| 1,1,1,1 | 1536 |
| Total | **5404** |

The elementary bound `p^j<=p` and `(1-p)^(-j)<=2^j` for `p<=1/2` gives
exactly the candidate's constant. It is deliberately loose but valid.

Two exact finite-law probes distinguish the formula from omissions:

1. Let all four insertions equal a Bernoulli indicator `Y` with probability
   `p=1/3`, and take `B={Y=1}`. With the sum of the four parameters denoted
   `r`, `L=log(1-p+p*exp(r))-log(1-p)`. Its fourth mixed derivative is
   `p(1-p)(1-6p(1-p))=-2/27`; the unnormalized bad weight instead gives
   `p=1/3`. This sign-changing test detects a lost quotient normalization.
2. Let an independent orbit sign `H=+1,-1` be uniform, set `F=YH`, `G=H`,
   and take both terminal-label insertions to be `Y`. The full partition is
   `(1-p)cosh(t)+p*exp(epsilon_c+epsilon_d)*cosh(s+t)`, while the good
   partition is `(1-p)cosh(t)`. The four-label derivative of their log ratio
   is `p(1-p)(1-2p)=2/27`. Separate orbit projections give `E_H F=E_H G=0`
   and would incorrectly give zero. The candidate's joint integration and
   conditional covariance formula pass this probe.

These are exact mechanism discriminators, not numerical simulations of the
SU(2) model. Together with the path-variance normalizer and cube boundary
probes, they test the specific omissions that could otherwise produce a
misleading positive check.

## 8. Research signal and remaining scope

**Signal for the three frozen candidates: `advance`, conditional on the
explicit accepted global `c_J` premise and the supplied finite SU(2) model.**
No material mathematical error was found in the frozen arguments. They
deliver the actual deleted-law regional small-collar stationary/relative
energy supplier, fixed-chart nonlinear principal Hessian/covariance supplier,
and arbitrary-exterior radial-profile/buffered complementary-ratio jet
supplier. These are resolved intermediate inputs rather than a restatement
of the full connected-response target.

The signal is not an audit verdict or retained status. It does not establish
full compact covariance, spatial connected-four decay, probability of a
global chart, overlapping-buffer composition, exterior differentiation after
averaging, nonidentity compact coercivity, or a physical mass gap. The global
compact theorem's ancestral chain was explicitly outside this assignment.
Provider: OpenAI/Codex, using inherited supervisor model and reasoning effort;
the host subagent tool did not expose an independent model identifier to the
checker. The parent was asked to record it if available. Independence here
means a fresh pre-candidate derivation and concrete alternative discriminators,
not provider diversity. No external Fable advice was read. No numerical
physics job, source edit, Git mutation, network action, or prompt edit was
performed. The tiny partition enumeration was deterministic bookkeeping.

Next checkpoint: parent may provide a frozen primary note and dependency map
for a separate scope-only comparison against these checked inputs. Until then
this signal applies only to the three hashes in section 6.

## 9. Independent normalized-energy extension, before author read

The parent requested this additional bounded check after section 8. The
derivation in this section precedes reading the newly supplied author file.
The parent confirms that the checker was spawned with no model/effort
override; the exact backend identifiers are unavailable to both sessions.
The recorded profile is therefore the **inherited supervisor profile**, not
an invented model identifier. The original three-file signal is unchanged.

For `t=kappa*u`, `H(t)=exp(t)/Z(t)`, and `r=|M|<=1`, define

    Phi_u(v,M)=kappa*(r-<v,M>)
                +(log H(t)-log H(t*r))/u.

Direct multiplication gives

    H(t)*exp(-u*Phi_u)=exp[-t*(r-<v,M>)]*H(t*r)
                     =exp(t*<v,M>)/Z(t*r).

Thus replacing every complete surviving kernel by this expression leaves
one coordinate-independent `H(t)` per kernel. The exact density relative
to product Haar is proportional to `exp(-u*Ehat_u)`, where `Ehat_u` is
Wilson energy plus the sum of these `Phi_u` terms. The regional expression
uses the actual complete selected surviving factors and the same reference
Haar measure, not a flat log-coordinate measure.

Since `(log H)'=1-B` lies in `[0,1]`, `log H(t)-log H(t*r)>=0` and hence

    Ehat_u >= E_J >= c_J sum_e[1-w(a_e)].                  (N1)

At all-identity readers `r=1`, every complete factor vanishes and has zero
differential. On the full compact set the correction as a function of `r`
has slope `-kappa*(1-B(t*r))`, bounded in absolute value by `kappa`.
Word telescoping and `||M|-|M'||<=|M-M'|` therefore give uniform global
Lipschitz constants for `u>=1`. A useful further check is the exact identity

    Phi_u(v,M)=-kappa*<v,M>+log Z(t*|M|)/u+log H(t)/u.      (N2)

The apparently nonsmooth linear norm terms cancel in (N2). The radial
`log Z(t*|M|)` is smooth at `M=0` for every finite `u` (its convergent
series is even). This does not imply uniform higher derivatives at zero
as `u` tends to infinity, and no such claim is needed.

In the common all-reader identity chart, `r>=1/2`. The already derived
moment/cumulant bounds for `h=log Z-t` give uniform derivatives through
any fixed order of `h(t*r)`. The correction is
`[h(t*r)-h(t)]/u`; its derivatives through order three are uniformly
bounded for `u>=1`. Together with the leading energy this proves uniform
local `C^3` template, incidence, and row bounds. At identity its Hessian is

    D^2 Ehat_u(0)=H_E,J+kappa*(1-B(kappa*u))*diag(V0,V1,O)
                >= c_J Id.                              (N3)

The family therefore satisfies exactly the regional proof's load-bearing
conditions, uniformly in `u>=1`: all-factor identity-extension lower bound,
principal baseline gap and row/range bounds, zero identity differential,
uniform local third derivatives, and uniform global Lipschitz continuity.
The same weighted contraction constructs a small stationary point for
`Ehat_(R,u)` under a sufficiently small complete exterior-reader collar.
The same quaternion-imaginary tangent proxy cancels its summed linear
remainders. The compact complement is controlled by uniform Lipschitz
continuity, so the proof yields a uniform all-compact relative lower bound
and small-cap quadratic upper bound. This point is consequently the unique
regional density mode **relative to product Haar**. It is not claimed to
minimize the flat-coordinate action, which additionally contains `-log j`.
All terminal outputs remain identity for the compact regional statement.

The proposed all-`u` chart sharpening also follows independently. Write
`S=uE_J+N+J_H`, with `N=sum h(t*r)` and `J_H=-sum log j`. At identity,
`D^2N(0)>=0` and `D^2J_H(0)=(2/3)Id`. Uniform anchored third derivatives
on the larger chart give constants `C_E,C_N,C_A` such that on a scalar
cube of radius `delta`, including small output slots when those are allowed,

    D^2 S >= [u*(c_J-C_E*delta)+2/3-(C_N+C_A)*delta] Id.

Choose `delta` small enough that `C_E*delta<=c_J/2` and
`(C_N+C_A)*delta<=1/6`. Then simultaneously for every `u>=1`,

    D^2 S >= (u*c_J/2+1/2) Id.                           (N4)

Principal conditional cubes retain this bound when all readers of their
touching factors remain in the fixed chart. This uses the identity PSD
normalizer Hessian rather than paying its whole second-derivative size by
a large-`u` threshold. A far unrelated exterior is still irrelevant. The
statement does not extend to a rough collar or an unrestricted compact
coordinate domain.

Independent extension checkpoint: (N1)--(N4) support the proposed bounded
extension. Next action is the full read of the frozen author file at its
supplied SHA, with particular attention to reference measure and zero means.

## 10. Frozen normalized-energy extension check

After recording section 9, read the complete author file
`/Users/jonreilly/.codex/worktrees/su2-marginal-chart/Physics/.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/marginal-normalized-regional-coercivity.md`,
SHA-256 `e9923cce5efc7f31f5233543bfa6d5da5fd3923d1cd0377a9549bca0e2a1a062`.
Its dependency hashes match the previously checked inputs. The author credits
the complete-energy idea to Fable advice; this checker has not read the advice
and used only the formula supplied in the parent's neutral extension brief
before writing the independent derivation above.

The second expression for `Phi_u` in author equation (1) agrees with (N2),
and its upper comparison in (3) follows from monotonicity of `Z` on `[0,t]`.
The global Lipschitz constant in (5) is correct: separate the output change,
whose cost is at most `kappa*|v-v'|`, from the mean change in the bilinear
term and the radial `log Z`, each costing at most `kappa*|M-M'|`. This is
valid across zero. The local derivative argument does not incorrectly regard
the unbounded parameter interval as compact; it explicitly uses the uniform
tilted-moment estimates and then divides by `u`.

The regional family has a common principal gap, upper row bound, range,
global Lipschitz constant, and local third-derivative bounds. Checking the
contraction and compact-proxy steps line by line reveals no new dependence
on volume or `u`. Joint continuity in `(u,z)` for finite `u>=1` follows from
continuous matrix inversion and iteration with the same contraction factor
and initial bound; no compact parameter interval is needed. The full and
empty regions are handled. Equations (11)--(16) follow with the stipulated
identity terminal outputs and small **complete reader collar**. The mode is
correctly identified as the mode of the continuous density relative to
product Haar.

Two direct discriminators check the important scope boundaries:

- At `M=0`, `log Z(s)=s^2/8+O(s^4)`, so
  `D_M^2[u^(-1)log Z(kappa*u*|M|)]_(M=0)=(kappa^2*u/4)Id`.
  Thus a globally uniform Hessian or `C^3` claim would fail. The author
  claims only global Lipschitz continuity and local uniform higher bounds
  near identity readers, which passes this test.
- For one normalized kernel whose unit mean is `exp(i*b*sigma_1)` with
  small `b>0`, the Haar density in its output has mode at that mean. Along
  the radial log-coordinate line, the density relative to Lebesgue measure
  additionally has `j(a)=(sin(a)/a)^2`. At the Haar mode `a=b`, its log
  derivative is `2*(cot(b)-1/b)`, which is nonzero. Hence Haar and Lebesgue
  chart modes must not be identified. Author equations (4),(16) and their
  accompanying restrictions preserve this distinction.

For the all-`u` chart corollary, the three variations in (17) have uniform
operator bounds from the already checked anchored third-derivative rows.
The positive normalizer Hessian at identity is retained; only its local
variation is subtracted. Choices (18) therefore give exactly
`D^2 S >= (u*c_g/2+1/2)Id`, for all `u>=1`, including the small terminal
output extension and arbitrary scalar principal-coordinate restrictions
with every relevant fixed reader in the chart. The weighted perturbation
is at most `u*c_g/4 <= M_u/2`, so the mixed-cube theorem gives `2/M_u`
and the stated spatial exponential factor. The reference measure for this
corollary is correctly the chart's Lebesgue measure with its Haar Jacobian.

**Extension signal: `advance`, conditional on the same accepted `c_J` and
finite-model inputs.** No material error was found. This closes the full
normalized regional Haar-mode/relative-density supplier for small reader
collars and removes the earlier chart `u_*` threshold by shrinking one fixed
cube. It does not supply rough-collar convexity, unrestricted compact
covariance, global chart probability, or connected-four spatial decay.
The source/hash/read limits and non-audit authority from section 8 continue
to apply. No file except this checker report was edited.

Current checkpoint: all four released author candidates have a conditional
`advance` signal at their stated frozen hashes. Await the frozen primary
note and dependency map for their scope comparison.

## 11. Primary-note and proof-map scope comparison

Read completely at the parent's released hashes:

- `docs/SU2_MARGINAL_REGIONAL_AND_CHART_ESTIMATES_BOUNDED_THEOREM_NOTE_2026-11-09.md`,
  SHA-256 `487b639be4d9ed3138e7abcaf74daab0aa1f0249a4ecf30436e370ade07196d4`.
- Target pack `PROOF_TREE.md`, SHA-256
  `e75f40b93d64a182686a2067639c0dd3503c12e677b7a9705b952ea5398c9726`.

The full proof-map diff against the assigned base was also read. The new
rows/arrows and next-obligation text were compared to the four frozen
suppliers; unchanged older response claims were read for context but their
older mathematical dependency closure was not recertified here. The primary
note's Fable link is attribution only and was not opened. No Fable verdict
or advice became a proof premise of this check.

The primary note matches the checked mathematics: the exact deleted law,
one surviving normalizer per retained kernel, all-`u` chart bound on a
smaller cube, mixed cube covariance with true derivative supports, complete
normalized-energy mode relative to Haar, small full-reader collar for the
compact relative theorem, arbitrary quotient exterior for radial moments,
the complement `B_S^c` for buffered ratios, and two distinct terminal labels
for the fourth-order bound. It retains original-source orbital covariance
and keeps compact nonidentity backgrounds, connected-four composition,
overlapping buffers, further blocking, and the physical gap open. Its
`proposed_retained` header is an author proposal; the adjacent metadata
explicitly remains `bounded-support`, requires independent audit, and forbids
bare retained status. This checker confers no new status.

One narrow scope wording issue was reported in the initial proof-map hash,
line 126, Q-relative: **"It is not a finite-u normalized-action minimum."**
The leading-energy proof only does not assert this identification; it does
not prove that the two minima differ. In fact, with identity collar its
minimum `I` is also the normalized Haar-density mode. Recommended replacement:
**"This leading-energy statement does not assert a finite-u normalized-action
minimum."** This is a wording correction, not a defect in the candidate
relative-energy theorem. All other new map statements match the suppliers.

Scope checkpoint: primary note has no material overclaim at its frozen hash.
Await the parent-owned one-sentence map correction and refreshed hash; no
source file was edited by this checker.

## 12. Final scope reconciliation and checkpoint

The parent applied exactly the Q-relative wording correction. The refreshed
final hashes are:

| Final claim surface | SHA-256 |
|---|---|
| `docs/SU2_MARGINAL_REGIONAL_AND_CHART_ESTIMATES_BOUNDED_THEOREM_NOTE_2026-11-09.md` | `487b639be4d9ed3138e7abcaf74daab0aa1f0249a4ecf30436e370ade07196d4` |
| Target pack `PROOF_TREE.md` | `27f8019f8823524b5248ce65cf8f8599e1c91888f42a3f1b7ec8258f2b0a99e5` |

The corrected row was reread in its surrounding table. A deterministic
byte-level check replaced that single new sentence by its old wording in
memory and recovered the exact initial map SHA
`e75f40b93d64a182686a2067639c0dd3503c12e677b7a9705b952ea5398c9726`.
Thus no other map change is being covered by an old read. The primary hash
is unchanged. At this scope checkpoint all four proof candidate hashes were
refreshed and matched sections 6 and 10. The subsequent narrow clarification
delta is checked and pinned in section 13 below.

**Final scope result:** the primary note and corrected map accurately report
the four checked conditional finite-model suppliers. The initial unsupported
negative statement about coincidence of minima is resolved. No remaining
material overclaim was found in these claim surfaces. The mathematical
signals remain `advance` under the named `c_J` and supplied-model premises;
they are not formal review PASS, audit verdicts, or retained status. No
ancestral global-coercivity recertification or new physical identification
is implied. The full connected fourth response of the marginal is still
an explicitly open consumer.

Only this gate report was written by the checker. No editable prompt file,
author source, Git ref or index, or external service was modified. The inherited
supervisor profile and its unavailable exact backend identifiers remain the
accurate model/effort disclosure. The task's requested checks are complete.

## 13. Final clarification delta and consolidated source freeze

The parent supplied three narrow chart clarifications and a dependent source-
hash refresh after the preceding scope reconciliation. I compared each new
file byte-for-byte against the still-preserved original author copy in the
chart worktree. The comparison copies had exactly the fully read original
hashes from sections 6 and 10. The entire resulting unified diffs were read;
they contain only the following changes:

1. The chart note expressly counts `-log j(a_e)` as a local factor. If a
   scalar-coordinate subset selects one component of a link, its other
   frozen components are readers and must satisfy the small-chart condition.
   This is correct and makes the condition on all full-action readers
   explicit. Haar has zero spatial range between these same-link components,
   so the finite-template, row, principal-restriction, and mixed-domain
   arguments are unchanged.
2. It expands the actual word-length count: each root leg has at most
   `2(L-1)` edges and the bridge has `L`, totaling `5L-4`. This agrees with
   the independent geometric count in section 7.1.
3. The output-response sentence now specifies differentiation of the
   **chart-conditioned expectation** on the fixed chart and frozen boundary.
   This accurately identifies the normalized expectation in the covariance
   identity and makes no unrestricted-compact response claim.
4. The normalized-regional note changes only its chart source SHA to this
   clarified chart hash. Its mathematical text is unchanged.

The primary and corrected proof-map hashes were refreshed and are unchanged.
The final reviewed freeze is:

| File | Final SHA-256 |
|---|---|
| `parts/marginal-nonlinear-chart-estimates.md` | `b1e26baa37cf1dc47331d9a98a834afda5e7634d62f31df50600fd321fc45cb7` |
| `parts/marginal-regional-relative-coercivity.md` | `2d142414fb4992c2a1e907d42d15ca9f7164ee6e90c892d8c3d529b39e297385` |
| `parts/marginal-regional-moments-and-ratios.md` | `b2d3d9bedfb52b11056788e1f72cd14c4f9846c733c86ee424c2240f13db647f` |
| `parts/marginal-normalized-regional-coercivity.md` | `4e858ca74ea12b7f5a34ef0ac459526268120c30c8061d1ad633bb720e4ec2f8` |
| Repository primary theorem note named in section 12 | `487b639be4d9ed3138e7abcaf74daab0aa1f0249a4ecf30436e370ade07196d4` |
| Target pack `PROOF_TREE.md` | `27f8019f8823524b5248ce65cf8f8599e1c91888f42a3f1b7ec8258f2b0a99e5` |

**Final result at these bytes:** the four conditional mathematical `advance`
signals and the clean scope comparison remain valid. The clarifications
require no new mathematical assumption or changed inequality. No remaining
finding is open within this assignment. Full original reads plus exact
changed-window reads cover this final freeze. No external-review verdict
was read or substituted for a derivation; inherited-profile disclosure and
all stated scientific limits remain unchanged.
