# Independent reconstruction of the stationary quantum-metric test

This calculation was completed before access to any third-campaign author
proof, script, or result. The three definition sources and their complete
hashes are in `SOURCES.json`. It concerns the fixed winding matching and its
closed fourteen-color process. Time below is microscopic time, with each
actual routed channel having rate `k0/2+h/4`.

## 1. What complete positivity would require

Write the classical preparation map as

    E(mu) = sum_eta mu(eta) tensor_u rho_(eta_u).

An exact intertwiner in the tested sense would be a CPTP map Phi_t satisfying
`Phi_t E(mu)=E(mu P_t)` on the supplied family of initial distributions, which
includes the stationary product and the small product perturbations used
below. An intertwiner on the full classical state space certainly satisfies
this requirement. No quantum semigroup assumption is needed for the test.

If `Phi(Sigma)=Sigma>0`, complete positivity applied to the positive block
matrix

    [ Sigma,                  Delta                 ]
    [ Delta,                  Delta Sigma^-1 Delta  ]

and the Schur complement give

    Phi(Delta Sigma^-1 Delta)
       >= Phi(Delta) Sigma^-1 Phi(Delta).

Taking the trace proves `Q_Sigma(Phi(Delta)) <= Q_Sigma(Delta)` for Hermitian
Delta. Two-positivity and trace preservation suffice. Thus a positive right
derivative dictated by the finite classical generator contradicts even the
existence of such CPTP maps for every sufficiently small positive time. It
does not merely contradict a particular Lindblad representation.

## 2. Stationarity directly from the microscopic swaps

For a signed coordinate direction delta let `q(u)=u+delta-e1`. Its fixed
`+e1` route is omitted. The other cycles have four distinct context sites at
N=2048. With a symmetric tensor S_delta and colors `(l,a,b,r)`, the drive is

    h = S(l,a)+S(a,r)-S(l,b)-S(b,r).

Exchanging a and b reverses h, so reverse rate minus forward rate equals
`-h/2`. Along any route cycle, the sum of h is zero: nearest-position terms
cancel after a shift, and the distance-two terms also cancel after a shift.
A homogeneous product weight is unchanged by exchanging any two colors.
Consequently its stationary master equation is the product weight times
`-(1/2) sum h=0`. Reducibility of the count sectors does not affect this
statement. In particular, the uniform color product pi is stationary.

The preparation of pi is `Sigma=tau^tensor K`, with `tau=sum_a rho_a/14` and
`K=N^3/2`. Every specified rho_a is strictly positive, so Sigma is full rank.
Any exact intertwiner fixes Sigma. The finite checker enumerates all 14^4
words on a four-position route cycle, checking this telescoping cancellation
and the actual reverse rate, rather than inferring stationarity from a mean
current alone.

## 3. The global metric derivative needs only one-pair marginals

Let `p_x(theta)=1/14+theta f_x`, with

    f_x(a)=e_a2 X_x/2+b_a3 Y_x/8,
    R_x=sum_a f_x(a)rho_a=X_x R_X+Y_x R_Y,
    R_X=(rho_A2+ -rho_A2-)/2,
    R_Y=(1/8)sum_a b_a3 rho_a.

These are admissible probabilities for `|theta|<1/7`; their sums are one and
all entries are positive. Both R_X and R_Y are Hermitian and traceless.
The tangent of the full product preparation is

    Delta=sum_u R_u tensor tau_(all other pairs).

If D is its exact time derivative after the full classical evolution, D may
contain correlations. Nevertheless,

    Sigma^-1 Delta + Delta Sigma^-1
      =sum_u [tau^-1 R_u+R_u tau^-1]_u tensor I_rest,

so exactly

    Q'(0)=sum_u Tr D_u [tau^-1 R_u+R_u tau^-1],              (A)

where D_u is the one-pair partial trace. No product closure at positive time
is used. Each first-coordinate plane contains N^2/2 black anchors, so division
by K changes the sum to `(1/N)sum_x`.

All encoding matrices are real symmetric. Define the real symmetric metric

    G_ij=Tr R_i tau^-1 R_j,   i,j in {X,Y}.

Then (A) per pair is `2 avg_x (X_x,Y_x) G (dot X_x,dot Y_x)^T` whenever the
initial marginal derivative stays in these two color directions. That last
property is proved below, including cancellation of the other directions.

## 4. Linearization from the actual four-context generator

The tensor is

    S_delta(a,b)=(gamma/2)delta.[e_a cross b_b+e_b cross b_a].

At uniform p0 the two vector means vanish, so `S_delta p0=0`. Expand the
actual outgoing current `E[c(l,a,b,r)(I_a-I_b)]` to first order in four
independent local probability perturbations f_l,f_u,f_w,f_r.
The constant-rate part contributes `(k0/2)(f_u-f_w)`. A perturbation in
either endpoint contributes zero to the drive because each unperturbed
context has mean S_delta p0=0. A perturbation in either outside context
contributes `2 S_delta f/14` before the factor 1/4 in c. Thus

    J_delta^(1)(u)
       =(k0/2)(f_u-f_w)+(1/28)S_delta(f_l+f_r).            (B)

This derivation counts the actual half-rate channel once. The independent
checker sums the actual rates over all 14^4 color words, varies each of the
four slots in each of the two tangent directions, and compares all fourteen
current components: forty nonfixed-direction cases, all exact. The sampled
rate extrema over the complete four-color domain are 1/20 and 21/20.

For a route displacement a, incoming minus outgoing current from (B) is

    (k0/2)[f_(x-a)+f_(x+a)-2f_x]
    +(1/28)S_delta[f_(x-2a)+f_(x+a)-f_(x-a)-f_(x+2a)].

For the present profile only the first component of a matters. The -e1
route has a=-2; all four transverse routes have a=-1. Their drive terms
cancel in opposite-direction pairs because S_-delta=-S_delta. Define

    Delta_s z_x=z_(x+s)+z_(x-s)-2z_x,
    Ls=(k0/2)(Delta_2+4 Delta_1),
    D z_x=z_(x+4)+z_(x-2)-z_(x+2)-z_(x-4).

Direct menu sums give `S_e1 f_X=4 gamma f_Y` and
`S_e1 f_Y=gamma f_X`. Therefore the complete fourteen-component marginal
derivative is exactly equivalent to

    dot X=Ls X-(gamma/28)D Y,
    dot Y=Ls Y-(gamma/7)D X.                              (C)

The checker also reconstructs all fourteen components on all N coordinate
planes from the five channel directions, separately from the scalar formula
(C). They agree as integer arrays with a common denominator.

## 5. Exact spatial sums

Let H=N/2, `T_x=H-2|x-H|`, `X_x=T_x/H`, and
`Y_x=X_((x-N/4) mod N)`. Here N=2048; the same identities below hold for
N divisible by four and at least sixteen. Ls is self-adjoint, D is skew,
X is even, and Y is odd. Consequently

    avg X Ls Y=avg Y Ls X=avg X D X=avg Y D Y=0,
    A=avg X Ls X=avg Y Ls Y,
    C=avg X D Y=-avg Y D X.

The squared one-step difference has average 16/N^2. The squared two-step
difference has average `64/N^2-128/N^3`: the two turning positions have zero
two-step difference and all other positions have magnitude 8/N. Discrete
summation by parts gives

    A=-64 k0 (N-1)/N^3.

For integer `0<=s<=N/4`, summing the piecewise affine triangles gives

    avg X_x Y_(x+s)
      =[2/N+32/(3N^3)]s-32s^3/(3N^3).

The correlation is odd in s. Hence `C=2(F(4)-F(2))`, giving

    C=8(N^2-144)/N^3.

At the specified parameters these are

    A=-22517/1342177280,
    C=262135/67108864.

Using (C), including all factors of two in (A), yields

    Q'(0)/K
      =2(G_XX+G_YY)A-(gamma/14)(G_XX-4G_YY)C
      =[-1468294 G_XX+5085081 G_YY]/4697620480.           (D)

The mixed metric entry drops out of this expression by the exact spatial
identities, even if it were nonzero.

## 6. Exact local quantum metric and result

The implementation rebuilds the twenty-four proper signed permutations,
their four- and three-element stabilizers, and the two stated integer seed
twirls; it imports no previous checker. Their traces are 1168 and 2125.
Transports to each label are checked to be independent of the stabilizer
representative. Tau is inverted rationally and `tau*tau^-1=I16` is checked
exactly. All integer matrices needed to reconstruct the metric are saved in
`RESULTS.json`.

The result is

    G_XX=2417748739555754821116820340799639977750
         /1317642545956945503834165709296483091641,
    G_YY=3294027190941045443247182637892226930624
         /5479433287981426997353428830244670390875,
    G_XY=0.

Numerically these diagonal entries are approximately 1.83490488143 and
0.601162021293. Substitution in (D) gives the reduced rational value

    Q'(0)/K
      =253943551350785258709380168798915548993408646371
       /3288323073641053210935625659843220349235316654080000
      =0.00007722585210266515021704709969859895278066... > 0.

This is an exact finite-N result. With Euler acceleration N, multiply it by
2048. No smooth-profile or large-N argument is used; corners in the triangular
profile cause no problem for the exact finite generator.

## 7. Controls and limitations

The symmetric contribution is about -0.0000817372179756; the drive contributes
about +0.000158963070078. Setting gamma=0 leaves a strictly negative derivative.
Reversing the quadrature Y changes the drive sign and gives approximately
-0.000240700288054. A constant spatial tangent has zero derivative. The
classical Fisher metric has diagonal entries 7 and 7/4, so its drive term
cancels and its derivative is exactly -157619/536870912. These controls
challenge the current orientation and quantum/classical normalization.

A separate exact 2x2 local-matrix control includes a two-site derivative
with a nonzero zero-marginal correlation term. The direct global derivative
and (A) both equal 27/77. A dephasing CPTP control fixing its reference state
decreases Q from 333/1225 to 9/50.

The positive value excludes CPTP exact intertwining under the stipulated
fixed preparation and input/resource assumptions. It does not invalidate
the encoding's positivity, covariance, or injectivity; these are different
properties. It does not exclude a changed encoding, extra input-correlated
resources, accessible classical labels, an approximate intertwiner, or a
different process. It makes no statement about native physical qubits,
locality of possible alternative quantum dynamics, formation, or a universal
quantum obstruction. The enormously large global matrix was never assembled:
the tensor identities prove its reduction exactly. No author third-campaign
calculation was consulted for this result.
