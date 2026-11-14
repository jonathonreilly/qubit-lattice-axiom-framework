## Repo search

Search terms: `force.response`, `VAR-SLAB`, `lambda_odd`,
`ODD-0`, `twist.indicator`, `even.two.slice`, `odd.spectral.gap`,
`electric.flux`, `twisted.partition`, and `ground.state.transform`.
Refs searched in `/Users/jonreilly/Projects/Physics`: `origin/main`,
`pr/10114`, `pr/10133`, `pr/10134`, `pr/10141`. Broad searches produced
unrelated force-response and electric-flux hits; their bounded output is not
an exhaustive negative search. The narrow search for the named constructions
returned no hits. Relevant predecessor statements are recorded below.
`library/prior/gap-fr-check-astra.md` is absent. The targeted registry search
found no row for FR, VAR-SLAB, or the odd gap. This is the assigned check of
row 922, not a new attack on that row or the reading assigned to row 928.

Provenance: OpenAI Codex, gpt-6-astra, xhigh; research text at
`70c7b97c50a6da4be552c839ec764f9ee2f6cc6d`. Not an audit; grants no status.
Source: `library/gap-fr-opus.md`, all 166 lines, by Claude Opus 5.5 max.
Source SHA-256: `9f12899c9e843d4ad1085e5505c14726a282be86730d2a8933a69b9501df4d12`.
Only this output file is edited. No numerical or computer-assisted proof.

Scope: exact force identities, even-law identities, twist martingale,
fixed-box spectral asymptotics and their threshold, transfer and Langevin
odd gaps, ODD-0, line quotients, sheet identities, and fact-test estimates.
The underlying transfer construction and cited results are inputs, not fresh
claims of this check. No order-one gap, confinement, or cutoff-uniform bound
will follow merely from checking these identities.

Checkpoint: complete. Source remains pinned. All requested statement
verdicts are below. The corrected threshold, distinction between the two
odd gaps, fact-test limits, and flat-wall failure must travel with any
reuse. The author file, FINISH and all registries remain unchanged.

### Prior statements actually read

The refs resolved to `4d88da5504d356762deb6b1a1c2695336af9fb81`,
`f76f6c649cff7dffbab664d8976e680e8f287fe9`,
`89faef229ff6e6bde42baad15ed8270c2f4087d8`,
`1e70c7211a2cdbc39001e619f1dd89db45e25851`, and
`c73ad7b177d94f89ff37b77386936e3d52b48b05`, respectively.

| Hit and source lines read | Exact statement and distance from this target |
|---|---|
| `origin/main:research/mass-gap/library/gap-mid-max.md:219–233` | Identity FL gives `1+S=(1+S_0)/(1-U)`, with `U=Tr[T^t(1-P_0)]/Tr T^t=(1/8) sum_{k!=0}(1-Z[k]/Z)`. It already identifies flux weight with twist traces and proves the Perron vector is centre-even. It does not give the force-response identities. Credit this predecessor, not row 922, for that spectral split. |
| `pr/10114:.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MASS_GAP_LOCAL_BLOCK_ASTRA.md:106–149` | For a simple loop with b distinct edges, its Haar second moment is `1/4` for SU(2), and `kbar_B W_C=r_f^b W_C`; the text derives `kbar_B >= (1+v_N/r_f^b)^(-1) (F tensor F*)`. This supplies older loop normalization and a convolution argument, not ODD-0 or a two-slice response bound. The November 8 digest identifies the same note on pr/10133; no independent proof is inferred from the copy. |
| Local `gap-wall-assume-max.md:299–354`, with `gap-wall-assume-check-astra.md:19–71` | T2–T6 already give `Var_w(rho)=4p(1-p)` and `4p(1-p)<=E_w norm(grad log rho)^2/lambda`. The correction retains the wall potential in `grad log A^t` before cancellation. These are the explicit inputs to row 922; this report does not claim them as new. |

The full `prior/repo-search-2026-11-08.md` was read. Its target is older
UV/history work; its relevant loop-transfer hit is the second row above.
No Repo prior work line is supplied in FINISH row 927. Searches of the
registry and the rest of this sparse checkout found no duplicate check.
Broad capped method searches are discovery only; the completed narrow
five-ref query returned no named FR/ODD-0/twist-indicator construction.

The SA index README, matching chunk rows and neighbours, and obligations
were read before these bounded outline reads. Credit Ethan Sussman and
Levent Alpoge, with Claude and Codex as authors of their text:

* `chunk-02:90–104` points to SA 2315–2335: the gauge-averaged operator
  `L=P C_E^(1/2) exp(-V) C_E^(1/2) P` is positive trace class and
  `Z_s(0)=Tr L^s` (GL8). This is transfer infrastructure. Its kernel is not
  silently identified with the symmetric wall-potential representative A.
* `chunk-01:65–72` and obligations:24 point to SA 588–599: the explicit
  spectral density `E exp(-E)dE` gives `(1+t)^(-2)` decay without a gap.
  This supplies no FR or odd-sector lower bound.
* `chunk-16:5–11` and obligations:887 point to SA 17235–17245:
  `||D_b(P_e-P_e0)|| <= C b_k exp(-c d(b,O))` is a separate requirement
  on compatible exterior/stored data. It concerns RG force derivatives,
  not the thermal twist force here, and is not asserted proved there.

The complete index search for the other named objects found no matching
odd-law or twist-indicator result. This is not an exhaustive absence theorem
about differently named CA arguments. No CA theorem is used to discharge a
step here. Tadeusz Balaban's work enters the inherited UV context only;
no unavailable original paper or recalled confinement theorem is imported.

## 1. Corrected force and exact response: HOLDS

Source 26–51 and 64–69 (4.1(a)–(c)). Use `A=A^t`, `t=a/2`,
`A_J=A o Theta`, `E=(A+A_J)/2`, `O=(A-A_J)/2`. Both A and A_J are strictly
positive, so `E>0` and `|R|<1`, where `R=O/E`. All gradients below use
the unit-S^3 product metric. Upper-wall vectors are pulled back by J.

For a lower-wall link, differentiating the finite slab integral gives

`grad_b log A = -(grad_b V(u))/2 + beta mu_(u,v)(f_b)`.

The potential term cancels in the ratio. Thus the FR-c expression for
`Delta G_b=grad_b log rho` is exact. Since `|f_b|<=1`, its norm is at
most `2 beta`. There are `3|B|` links per wall and two walls; the total
bound is `24 beta^2 |B|`. This uses the correction already in row 901.

Direct division, without a spectral approximation, gives

`rho=(1-R)/(1+R)`, `X=-2 artanh R`,
`grad_u X=-2 grad_u R/(1-R^2)`.

Moreover `rho^2 w=Theta_*w`, and `|grad_u X|^2 o Theta=|grad_u X|^2`.
Therefore `E_w|grad_u rho|^2=E_w|grad_u X|^2=FR_u`, proving 4.1(b).
This is an integrated identity, not equality of its integrands.

For 4.1(c), integrate the first time layer last. Its common weight is
multiplied by `A^(t-1)(w_1,v)` in one slab and
`A^(t-1)(w_1,Jv)` in the other. Boundary half-potentials agree because
`V(Jv)=V(v)`. The normalized density ratio on that layer is exactly
`rho_(t-1)(w_1,v)/rho_t(u,v)`. Hence its expectation is one, and

`Delta G_b=beta Cov_mu(f_b,rho_(t-1)(w_1,v))/rho_t(u,v)`.

This also specifies the common first-layer sample space. The full slab
laws have different fixed final slices; no full-path absolute continuity
claim is required. The equality of the two wall sums follows by swap
symmetry, simultaneous J covariance, and isometric pullback.

## 2. Even two-slice law: HOLDS

Source 85–89 (5.1). Hilbert–Schmidt orthogonality of the even and odd
spectral kernels gives `integral E^2=Z_e`, `integral O^2=Z_o`, and
`Z_e+Z_o=Z`. Thus `Z_e=(1-p)Z`, and direct expansion of `(A+A_J)^2/4`
gives the printed mixture formula for w_e. Theta preserves w_e and changes
R to -R. Consequently

`E_e R=0`, `Var_e(R)=integral O^2/Z_e=p/(1-p)`.

Multiplication of `|grad_u X|^2` by `A^2/Z` gives exactly

`FR_u=4(1-p) E_e[|grad_u R|^2/(1-R)^2]`

`    =4(1-p) E_e[|grad_u R|^2 (1+R^2)/(1-R^2)^2]`.

The second equality averages the Theta pair. The variance identity is
exact; FR is a **weighted** Dirichlet energy. There is no uniform upper
comparison with the unweighted energy from `|R|<1` alone. The result line
at source 166 must say **one-wall response** for the formula with
`grad_u`; the all-wall sum is twice it. A Poincare inequality under w_e
is an alternative sufficient bound, not literally T6 under w.

## 3. Twist indicator and force covariance: HOLDS AFTER CORRECTION

Source 91–94 (5.2). Normalize the component weights to
`A/(A+A_J)` and `A_J/(A+A_J)`. Their difference is R. The actual final
configuration is either v or Jv. For integer `0<=s<t`, the remaining
partition weights are `A^(t-s)(w_s,v)` and `A^(t-s)(w_s,Jv)`.
Their normalized difference is `R_(t-s)(w_s,v)`. This proves the
conditional expectation formula and the martingale property.

At `s=t`, define `M_t=sigma` directly. The printed `R_0` is not a
smooth kernel ratio: `T^0` has a delta kernel. This endpoint convention
is required. Layer information here consists of the raw gauge fields;
passing to gauge-equivalence classes at the endpoint could hide the label.

In a fixed orthonormal tangent frame at u, the derivative of the common
first-layer log weight is `beta f_b`. Its boundary-potential factor has
zero covariance with sigma. Differentiating the normalized expectation
therefore proves `grad_b R=beta Cov_mix(f_b,sigma)`.

For the vector F of all first-layer forces, let `Gamma=||Cov(F)||op`.
For every unit vector z, Cauchy–Schwarz gives
`|Cov(z.F,sigma)|^2<=Gamma(1-R^2)`. Taking the supremum proves the
printed summed covariance inequality. It implies

`FR_u<=4 beta^2 Gamma_* E_w[1/(1-R^2)]`

`     =2 beta^2 Gamma_* (1+E_w cosh X)`.

Also `E_w rho=r` and `E_w rho^(-1)=E_w rho^3`, by the flip identity,
so the displayed cosh moment is correct.

The sentence “Gamma <= 3|B| gives back 24 beta^2 |B|” needs a different
argument. Inserting that bound into the Gamma inequality leaves
`(1-R^2)^(-1)`, which can be large. Instead put
`m_+=E(F_b|sigma=+1)`, `m_-=E(F_b|sigma=-1)`. Bernoulli algebra gives

`Cov(F_b,sigma)=(1-R^2)(m_+-m_-)/2`.

Since `|m_+-m_-|<=2`, `|grad_b X|<=2 beta`, recovering the trivial
bound from section 1. The volume-free Gamma estimate remains conditional.

## 4. Large-time asymptotics and the threshold: HOLDS AFTER CORRECTION

Source 71–81 (4.2, 4.3), and 158, 161, 166. Fix the finite box B and
`beta>0`. Require a nonzero odd eigenvalue `lambda_->0`; otherwise the
displayed multiplicity and wave functions do not describe that sector.
At beta=0 the Wilson operator is rank one: `O=R=p=FR=0`, separately.

Here is a justification of the uniform one-derivative expansion omitted
from the source. Normalize T by lambda_0. In each parity sector remove
its top eigenspace. Compactness gives a strictly smaller remaining
spectral radius. Sandwich the residual power between two copies of T.
Evaluation of T and its first derivative is a bounded L2 functional,
uniformly on the compact configuration space. Cauchy–Schwarz bounds the
residual kernel and each first derivative by a fixed constant times that
smaller radius to power `t-2`. Also psi_0 is smooth, strictly positive,
and has positive minimum. Division by its two factors is thus legitimate.
This proves, in C1,

`R=e^(-t E_-)[sum_{k=1}^m h_k(u)h_k(v)+o(1)]`.

Trace-class spectral summation gives
`p=m e^(-a E_-)(1+o(1))`. The normalized density w converges uniformly
to `psi_0(u)^2 psi_0(v)^2`. Orthonormality gives
`integral psi_0^2 h_k h_l=delta_kl`. Applying the product limiting law
to the u-gradient, and then to the v-gradient, yields

`FR_u=4 e^(-a E_-) sum_k D(h_k)(1+o(1))`,
`I:=FR_u+FR_v=8 Dbar p(1+o(1))`.

Each D(h_k)>0: a zero-energy smooth function is constant, whereas h_k
is odd and has unit L2 norm. Thus a relative remainder is justified.
These constants and remainders depend on B and beta.

The first incorrect threshold is source 75. If `0<p_*<1/2`, then
the needed bound is `I<=4 lambda p_*(1-p_*)`, as its preceding phrase
correctly states. Substitution gives

`p <= [lambda p_*(1-p_*)/(2 Dbar)]/(1+epsilon(a))`,

where `epsilon(a)->0` is the actual relative error in I. The factor
`1-p_*` cannot be dropped into an `o(1)` as a tends to infinity with
fixed p_*. Dropping it is a separate small-p_* approximation.
With a fixed positive gap lambda uniform in a, applying its inequality
to F(u,v)=h_k(u) and taking the limit proves `Dbar>=lambda`.

The all-wall formula and the exponential rate HOLD. The claimed general
equivalence with the flux half needs the following correction: this is
an asymptotic relation at fixed B,beta, with a stronger threshold and
additional Dirichlet constants. It is not an exact equivalence at
`a=10`, nor a uniform equivalence along a changing box or cutoff.
Even a nonconfining model with a positive finite-box odd eigenvalue has
this large-a decay. Neither `E_- about sigma L_1` nor confinement
follows from this calculation. The bound of a particular link can also
decay faster if its leading gradient coefficient vanishes; E_- is the
rate of the nonzero summed response. Source 158 must retain `1-p_*`:
the leading trade-off is `lambda >= 2 Dbar p/[p_*(1-p_*)]`.

For 4.3(3), the stated normalized Haar sum of straight winding lines
does have energy `3 L_1`; their disjoint edge sets make distinct lines
orthogonal. It is a trial vector. Its identification with every lowest
odd wave function at positive coupling needs perturbative spectral
control. The Haar full gauge-invariant gap is `3 min(4,L_min)`:
a nonconstant spin network has no degree-one vertex, hence contains a
cycle, whose length is at least the graph girth `min(4,L_min)`;
each nontrivial edge costs at least 3. A fundamental shortest loop
attains the bound. Thus `2 Dbar/lambda about L_1/2` uses the additional
strong-coupling identification and `L_min>=4`. It is not a statement at
beta=0 about flux eigenfunctions, since that transfer odd sector is zero.
The transverse per-link factor in 4.3(4) likewise describes this trial
vector; it is not a general theorem of delocalization.

## 5. Transfer-chain odd gap: HOLDS AFTER CORRECTION

Source 97–101 (5.3). Set `pi=psi_0^2 du` and define U by `Uh=psi_0 h`.
Then U is unitary from L2(pi) to L2(du), preserves parity, and

`U Q U^(-1)=T/lambda_0`.

The eigenfunction equation proves Q1=1; symmetry of A proves detailed
balance. For its Markov Dirichlet form,

`D_Q(h)=(1/2) integral pi(du)Q(u,dv)|h(u)-h(v)|^2`,

the infimum of `D_Q(h)/||h||_pi^2` over odd h is
`delta_odd(Q)=1-lambda_-/lambda_0=1-exp(-E_-)`.

The displayed infimum in source 97 HOLDS. Calling **E_- itself** the
spectral gap of the discrete chain is wrong: E_- is its logarithmic
decay rate, or the odd spectral bottom of `-log Q`. This distinction
must propagate to source 161 and 166. It is also a different operator
from the Langevin odd gap under w_e in section 8.2.

A further correction is needed to “the flux half is a Poincare
inequality for Q”. A gap fixes an extremal eigenvalue; a thermal trace
also counts multiplicities and higher levels. For example, on 2n points
let J exchange pairs and `Q=q I+(1-q)Pi`, with Pi uniform averaging and
`0<q<1`. Q is symmetric, strictly positive entrywise, and has odd gap
`1-q`. Yet

`p(a)=n q^a/[1+(2n-1)q^a] -> 1/2` as n grows at fixed a,q.

This hand example refutes the claimed abstract equivalence from the
structural premises alone. It is not a Wilson counterexample. At fixed
B a trace bound can follow with additional prefactors; none is uniform
merely because a gap is positive.

The odd-kernel bound in 5.3(2) HOLDS. For even `s>=2`, set
`g_u=P_o T^(s/2) delta_u`, a genuine L2 vector. Its norm squared is
`O^s(u,u)`. Then `O^t(u,v)=<g_u,T^(t-s)g_v>`, and the operator norm
on the odd sector is `lambda_-^(t-s)`. This proves the claimed bound,
including `t=s`. No derivative estimate or lower bound for E follows
without further constants.
The factorization printed for `T^t` must read `T^t P_o`; its use for
the odd kernel is correct.

The qualitative Perron conclusion `lambda_-<lambda_0` HOLDS, as does
the stated projective contraction bound. Here is a direct verification
of the latter. Ground-state factors cancel from the cross ratios
defining Delta. For two rows of Q their density ratio lies in [m,M]
with `M/m<=exp(Delta)` and mean one. Their total variation is at most
`(M-1)(1-m)/(M-m) <= tanh(Delta/4)`. The first bound follows by
bounding the positive part of the ratio minus one by its secant;
the second follows by maximizing at
`m=exp(-Delta/2)`, `M=exp(Delta/2)`. Hence
`osc(Qh)<=tanh(Delta/4) osc(h)`. Apply this to a nonconstant odd
eigenfunction h to obtain `lambda_-/lambda_0<=tanh(Delta/4)`.

The subsequent assertion that the projective diameter is **at least** of
order beta times volume is not proved by the text. Entrywise Wilson
bounds readily give an extensive **upper** bound; that does not prove
a lower bound on the actual diameter after gauge averaging. Treat the
Birkhoff discussion as an unquantified route assessment. For 5.3(4),
write `S_-(a)=sum_{j odd}(lambda_j/lambda_0)^a`. The printed bootstrap
holds because a sum of squares is at most the square of a nonnegative
sum. Cauchy–Schwarz also proves log-convexity of S_-; this is not a
claim of log-convexity for the ratio p. Neither supplies its first small
value. “Every transfer bound” and “no trace or chessboard identity”
are not proved exclusions of other methods. Correct 5.4 and 6.6 to
report only that the displayed attempts supplied no order-one FR bound.

## 6. Odd Langevin reduction, ODD-0 and line quotients

**8.2, source 145–147: HOLDS.** Odd functions have zero w_e mean.
R is admissible and swap symmetric. Write
`D_u=E_e|grad_u R|^2`. The defining inequality gives
`p/(1-p)<=2D_u/lambda_odd`. The source's bound
`D_u<=FR_u/(1-p)` proves exactly `p<=2FR_u/lambda_odd`.

There is a stronger consequence of the already checked symmetric
identity, without a new supplier. For `|R|<1`,
`(1+R^2)/(1-R^2)^2>=1`, so `FR_u>=4(1-p)D_u`. Therefore

`p <= FR_u/(2 lambda_odd)`.

The weaker printed estimate remains true. No comparison between the
best gaps of w and w_e is supplied, so the “price of about 4” is only
constant bookkeeping, not an assertion that these two gaps coincide.

**ODD-0, source 149–150: HOLDS, with equality.** At beta=0, w_e is
product Haar on the two slices. Peter–Weyl decomposition and vertex
gauge projection commute with the product Laplacian and J. In a
nonzero invariant component the half-integer edges have even degree
at each vertex: a central gauge transformation at that vertex acts by
their parity. In the v slice, odd J parity says their mod-2 cycle
crosses the selected direction-1 cut oddly. Conservation at vertices
makes the parity the same at every parallel cut. The L_1 cuts use
disjoint direction-1 edge sets, so there are at least L_1 such edges.
Each costs `4j(j+1)>=3`; all u-slice contributions are nonnegative.
Orthogonal summation proves the lower bound for all smooth invariant F.
A single fundamental winding trace in v has exactly L_1 spin-1/2
edges, is odd, and attains energy/variance `3L_1`. Thus
`lambda_odd=3L_1`.

**Single-line identity and quotient, source 151: HOLDS.** For a simple
straight line, freeze all links but b. Its normalized trace is a unit
linear coordinate on S^3, possibly composed with inversion, an isometry.
The spherical gradient therefore has norm squared `1-chi_l^2`.
The line is w_e-centred by J symmetry. If `q=E_e chi_l^2`, its
Rayleigh quotient is exactly `L_1(1-q)/q`, with `0<q<1` at finite beta.
For this quotient to be small relative to L_1, q must approach one;
this is closeness of the **line holonomy**, not every individual link,
to the centre in mean squared trace.

**Averaged-line formula, source 152: HOLDS AFTER CORRECTION of its
interpretation.** Put `N=L_2 L_3`. The N straight lines have disjoint
links. Translation invariance gives their common q. For
`F=N^(-1) sum chi_l`, its variance is exactly the printed cbar and
its energy is `L_1(1-q)/N`. Hence the displayed quotient is correct.
It is small when `(1-q)/(N cbar)` is small, not “exactly” when lines
are strongly correlated: `1-q` can itself be small. Under Haar,
`q=1/4`, `cbar=1/(4N)`, giving `3L_1`, consistently with ODD-0.
At positive coupling, the assertion `cbar about q/N` is an additional
correlation estimate. It is not implied by a small thermal flux weight.

## 7. Sheet identities and direct estimates

**6.1, source 106–109: HOLDS AFTER CORRECTION.** A centre change of
interior variables turns the endpoint-flipped slab into the ordinary
slab with weight `W_Sigma`. It fixes the bottom boundary. Consequently
`E_mu W_Sigma=rho`. If the observed plaquette is not on the sheet,
its trace and its bottom derivative are unchanged by that map, proving
the printed covariance formula. Two disjoint homologous sheets bound
an interior flip, giving `E_mu W_i W_j=1` for `i!=j`.

The single-sheet second-moment identity also holds, provided the
right-hand plaquette variables are in the changed endpoint ensemble:

`E_mu W_i^2 = rho E_(mu_(u,Jv)) exp(2 beta sum_{p in Sigma_i} x_p)`.

Jensen gives the stated lower bound with expectations under that same
law. It gives no positive lower bound on those plaquette means.
The numerical mean 0.6 is recalled GUIDE data, not a proved mean in
this ensemble and for these boundary values. A large sheet moment
therefore remains conditional on the sign and size of that sum.

Different sheet positions need not have equal second moments at fixed
u,v. The exact variance formula for N disjoint sheets is

`Var_mu(N^(-1) sum_i W_i)`

` = N^(-2) sum_i (E_mu W_i^2-1) + 1-rho^2`.

The source formula holds if its `E W_Sigma^2` denotes the **average**
of these N second moments, or if equality of those moments is proved.
For flat sheets placed strictly away from the first time layer,
`N<=(t-1)L_1` is the available number of time/cut positions. Neither
that count nor Jensen proves that the first variance term dominates
for the true boundary law. Likewise the raw covariance equals
`rho Delta G_b/beta`; its rate statement needs the fixed-box
asymptotics and beta>0, and a particular component may vanish.

**6.2, source 111: HOLDS AFTER CORRECTION of scope.** For any coupling
of the two slab laws, let D be the event that the variables determining
f_b differ. Then `|E f_b-E f'_b|<=2 P(D)`, proving the coupling bound.
The subsequent no-contraction claim is only about the named sufficient
influence estimates. It is not a theorem about every possible block
coupling. In particular the source supplies no argument that every
vertex-block method has the same 0.775 ceiling. Its cited layer
obstruction is a background-uniform, one-layer statement; it does
not establish failure of this averaged, thick-slab response estimate.
The decimal `4G_3 about 1.0109` is explicitly GUIDE in its source
`gap-wall-assume-max.md:38–40`; the hand threshold there is beta>4/3.
No unavailable numerical evaluation of G_3 is used here.

**6.3, source 113: HOLDS AFTER CORRECTION.** The two-term squared
triangle bound is exact. To turn it into an FR estimate requires a
bound on both terms under w, including the term with Jv. A bound for
typical unflipped endpoints alone does not supply that bound, since
`Theta_*w=rho^2 w`. Assuming each term has the needed exponential
estimate, its prefactor still matters. For a proposed all-wall bound
`I<=C |B| beta^2 exp(-2mt)`, the sufficient thickness is

`t >= [log(C |B| beta^2)-log(4 lambda p_*(1-p_*))]/(2m)`.

The printed 7.3 omits the local constant, beta and lambda, and is
GUIDE only. Its scale arithmetic is consistent: with the supplied
numbers `3|B| beta^2=126960` and `2mt=12`, so the displayed trial
one-wall expression is `126960 exp(-12)`, of order one. The two-wall
sum and the triangle factors must be included in C. An upper bound
larger than the desired threshold is inconclusive; it does not prove
that the actual response is too large. Calling the hypothetical
clustering bound “true” needs the stated missing slab hypotheses.

**6.4, source 115: HOLDS AFTER CORRECTION of conventions and scope.**
For a left-invariant derivative D_g, Haar integration gives
`0=integral D_g exp(beta sum x_p)`; hence the displayed Ward identity
holds in left-trivialized components. One cannot average tangent
vectors at different g without such a convention. A positive
Bakry–Emery curvature bound implies a Poincare lower bound, so
`kappa<=lambda` is valid in the matched convention. The gradient
semigroup estimate alone does not bound the initial energy of R;
one must supply a representation of R to which it applies. No such
representation or order-one curvature bound is established here.

**6.5, source 117: HOLDS AFTER CORRECTION of the recalled formula.**
The cited local reading `prior/gap-lit-flux.md:21` records the
SU(2) Wilson-loop bound as
`<W(C)> <= 2[(1-Z^-/Z)/2]^(A_C/(L_mu L_nu))`.
It uses the **deficit** of the twist ratio, not that ratio itself.
This source-level correction matters when the ratio tends to one.
Credit Tomboulis and Yaffe and the later formulation by Kanazawa.
Their proofs were not reopened and supply no new premise here.
The row-928 literature task is not rerun.

## 8. Fact-test estimates

### 8.1 Common test and discrete replacement: HOLDS

Source 123 and the inequality in 134. For a smooth compact group with
the stated positive gap, T6 implies
`I>=4 lambda p(1-p)`. Positive kernels give `0<=p<1/2`, and
`p(1-p)` is strictly increasing on that interval. Therefore if
`p>=p_0>p_*`, the needed relative threshold on I is impossible.
This tests the pair of inputs and their margin; it does not identify
which absolute bound fails.

For a finite group, define the two-slice heat-bath energy by
`D_w(f)=sum_b E_w Var_w(f | all other boundary links)`.
If lambda_G is the gap for that chain, its defining inequality gives
`D_w(rho)>=4 lambda_G p(1-p)`. If instead lambda_G is the gap of the
full-torus heat-bath chain, lift f to that torus. Conditional variance
decreases upon additionally conditioning on interior links. Thus its
full-chain energy is at most D_w(f), and the same displayed bound
still follows. These are the two precise meanings of the “marginal
argument”. There is no identity replacing `D_w(rho)` by a squared
finite difference of log rho.

### 8.2 U(1) rotor calculation: HOLDS AFTER CORRECTION

Source 125–130 and the U(1) trial mode in 152. This calculation is
conditional on the spin-wave/zero-mode model, with monopoles omitted.
It is not an estimate for the full Villain or Wilson ensemble.
Write `N=L_2 L_3`. The uniform mode theta_1=Phi/L_1 has kinetic
action `beta N/(2L_1) integral dot(Phi)^2`, so its inertia is
`beta N/L_1` and `E_1=L_1/(2 beta N)`. This derives the coefficient
independently of the transfer eigenfunction expansion in section 4.

For the circle heat kernel put

`K_tau(psi)=sum_{n in Z} exp(-(psi+2pi n)^2/(4tau))`,
`rho(psi)=K_tau(psi+pi)/K_tau(psi)`, `tau=t E_1`.

An irrelevant common normalizer cancels. Near psi=0, the denominator's
nearest image and the numerator's two nearest images give

`X(psi)=-pi^2/(4tau)+log[2 cosh(pi psi/(2tau))]`

up to exponentially small image terms on a fixed smaller interval.
The printed X' is consequently a **small-tau approximation**, not
an exact global heat-kernel identity. The law `w(dpsi)` proportional
to `K_tau(psi)^2 dpsi` is concentrated there with variance
`tau(1+exponentially small error)`. On `|psi|<=pi/2` the image
errors are exponentially small; outside, its probability is so
small as well. Finally the integral of
`sech^2(pi psi/(2tau))` against that concentrated density is
`O(sqrt(tau))`: substitute `psi=2tau z/pi` and use
`integral sech^2 z dz=2`. It follows that

`E_w X'^2 = pi^2/(4tau^2) [1+O(sqrt(tau))]`,

`I=2(L_1/N) E_w X'^2`

` = 2 pi^2 beta^2 N/(t^2 L_1) [1+O(sqrt(tau))]`.

Thus the coefficient in source 127 and the typical per-link size in
128 HOLD in this model and limit. Averaging unwrapped line angles
to define Phi needs a chosen spin-wave chart. Its cosine is not
automatically a globally defined smooth observable of compact link
angles. The collective Rayleigh trial in 152 is therefore a model
guide until that extension is supplied.

An independent hand check of the seed arithmetic uses fractions:
`beta=23/10`, `L_i=20`, `t=5` give `E_1=1/92`, `tau=5/92`, and
`I_leading=(1058/125) pi^2`. The elementary bounds `3<pi<22/7`
place this between 76 and 84. This verifies the order `10^2`, not
an error bound for the model at tau=5/92. At `p_*=1/5000`, the
leading comparison factor is of order `10^5/lambda`, not an
unqualified `10^5`. No value of lambda=1 was established.

At fixed beta and `a=L` in a cube, `tau=1/(4beta)` is **constant**.
The correct exact rotor scaling is

`I=(2/L) J(1/(4beta))`, `J(tau)=E_w X'^2`.

It becomes `8 pi^2 beta^2/L [1+O(beta^(-1/2))]` in an additional
large-beta limit. The source's `1+o(1)` as L grows alone does not
remove this error. If `p_beta` is the rotor odd weight at this aspect
ratio, T6 gives

`lambda <= I/[4 p_beta(1-p_beta)]`,

not `lambda<=I` at fixed beta. In the rotor,
`p_beta=sum_{k odd} exp(-2tau k^2)/sum_k exp(-2tau k^2)`;
it approaches 1/2 as tau decreases. The denominator is close to one
only with this separate approximation. The rate `lambda=O(1/L)`
is conditional on this rotor model and fixed aspect ratio.

The external theorem attribution needs correction too. The actual
row-786 source `gap-tu-retry.md:83–100` states Theorem V for the
gauge-invariant Villain Langevin gap at `beta>=2^14`, with **no rate**.
It was read at its statement and is an inherited input, not rechecked
here. A search of that file finds no twist/flux theorem. The citation
chain `gap-kurt-max.md:91–93` calls row 786 a “twist theorem” but
does not supply one. Hence source 125 has no verified cited theorem
for `p` bounded away from zero. That assertion must remain a physical
or rotor premise here, and Theorem V cannot be used at beta=2.3.

### 8.3 Frozen groups: FAILS as a quantitative fact test

Source 132–135 and the frozen-sector assertion in 152. The statement
that the differential FR is undefined on a finite group HOLDS.
The discrete Poincare implication HOLDS by section 8.1 above.
The claimed domain-wall response size does not follow from it.

The first missing step is source 133: a twisted wall is asserted to
be uniformly distributed over about `t L_1` positions for typical
fixed u,v. No wall representation, boundary-law estimate, pinning
bound, or positive lower response is supplied. The ordering window
is labelled GUIDE in the cited row, and is not a theorem here.
Even given wall probability `1/(t L_1)`, a nonzero contrast in the
specific scalar observable is a further premise. Under those
premises a **one-wall** sum of order
`c^2 beta^2 N/(t^2 L_1)` is consistent dimensional counting; the
other wall adds the corresponding factor. This is a conditional
heuristic, not a proved estimate for Q_8 or 2T.

Source 135's “as it must” is invalid for the mean-observable analogue:
no exact variance identity connects that observable to p. For the
discrete ratio energy alone, `p>p_*` does force failure of its
relative threshold, whatever the positive finite-box gap is.
The absolute energy size and the asserted tunnelling-small odd gap
still require a sector test function and a transition estimate.
The note explicitly leaves the former open at 134 and 164; it must
not conclude that both absolute factors have been determined.

### 8.4 SU(2) and the global reading: HOLDS AFTER CORRECTION

Source 137–139, 152, 155–158, 162–166. The conditional fixed-box
formula `I about 8p Dbar` holds by section 4. The additional estimates
`E_- about sigma L_1`, `Dbar about 3L_1`, centre-vortex absorption,
and the transverse line-correlation claim are not established at
order-one coupling. Even a small p only gives the desired response
threshold with control of Dbar/lambda and the asymptotic remainder.
Thus “SU(2) satisfies FR” is a physical expectation with those
premises, not a result of this check.

The block comparison proposed at 156 is valid **conditionally** on
uniform conditional-slice Poincare constants and maximal correlation
`rho_max<1`. To see its form, on mean-zero L2(w) let P_u and P_v
be conditional-expectation projections onto the two slice subspaces.
Their angle is controlled by rho_max. The map `(g,h)->g+h` has
squared norm at most `1+rho_max`, by
`|<g,h>|<=rho_max||g||||h||`. Hence
`||P_u+P_v||<=1+rho_max` there, and

`E Var(F|u)+E Var(F|v)>= (1-rho_max) Var(F)`.

Applying the two conditional Poincare inequalities proves the
displayed comparison with `c=1` in the sum-of-two-blocks convention.
It does not prove either input at order one. Importing one-layer
influence ceilings for the nonlocal two-slab conditional measure
also needs an actual comparison, absent here.

**8.4(3), source 157: FAILS as a flat-wall force witness.** The cited
W1-t statement bounds a supremum of a **twist coefficient** using
wall-to-wall rectangles. More decisively, at `u=v=1` every component
of `grad log rho` is exactly zero. Indeed X is invariant under global
conjugation, and a configuration of central boundary links is fixed
by every such conjugation. The differential in any one link must
therefore be an invariant covector under the adjoint SO(3) action on
its tangent space. The only such covector is zero. This also holds
at `(u,Jv)`, since the flipped boundary links are still central.
Thus a nonzero flat-wall twist deficit is compatible with **zero**
boundary force response, at every beta and thickness. It cannot
witness the asserted failure. A supremum obstruction using other
boundary fields would require a separate argument. The L2
formulation does weight exceptional walls by w, as stated.

The statements that these attempts supply no order-one FR bound and
no cutoff-uniform supplier HOLD as reports of what the text proves.
No claim that all other methods fail follows from this review.

## 9. Verdict map and limits

Each source range is in `gap-fr-opus.md` at the pinned commit. A verdict
on a GUIDE calculation checks its stated conditional model and arithmetic;
it never promotes that model to an estimate for the actual gauge theory.

| Statement | Source lines | Verdict |
|---|---:|---|
| Step 1–2: T3/T4/T6 inputs and corrected FR-c | 26–51 | HOLDS with the already supplied row-901 force correction |
| Step 3: fixed-cutoff scope versus first-passage uniformity | 53–58 | HOLDS; quoted upstream theorems remain inputs |
| 4.1(a): ratio and derivative | 64–65 | HOLDS |
| 4.1(b): integrated score-gradient identity | 66 | HOLDS |
| 4.1(c): first-layer likelihood ratio and covariance | 67–69 | HOLDS |
| 4.2: C1 and trace asymptotics | 71–74 | HOLDS AFTER CORRECTION: beta>0/nonzero odd spectrum; beta=0 separately |
| 4.2: needed-size equivalence and limiting Poincare bound | 75 | HOLDS AFTER CORRECTION: retain `1-p_*` and fixed-box scope |
| 4.3(1)–(2): flux interpretation and decay rate | 78–79 | HOLDS AFTER CORRECTION: summed fixed-box rate; physical string tension remains a premise |
| 4.3(3): Haar trial and full Haar gap | 80 | HOLDS AFTER CORRECTION: trial/perturbative status, `L_min>=4` for the quoted ratio |
| 4.3(4): per-link delocalization | 81 | HOLDS AFTER CORRECTION: a model/trial-vector statement |
| 5.1: even law, variance and weighted energy | 85–89 | HOLDS; keep the one-wall versus two-wall convention |
| 5.2: mixture martingale | 91 | HOLDS AFTER CORRECTION: endpoint M_t defined directly |
| 5.2: force covariance and Gamma bounds | 92–94 | HOLDS AFTER CORRECTION: repair the trivial-bound argument |
| 5.3(1): Q transform and odd gap | 97 | HOLDS AFTER CORRECTION: gap is `1-exp(-E_-)`; a trace also needs multiplicities |
| 5.3(2): odd-kernel bound | 98 | HOLDS; factorization is for `T^t P_o` |
| 5.3(3): Perron/projective bounds | 99 | HOLDS AFTER CORRECTION: no extensive lower bound on actual Delta was proved |
| 5.3(4): bootstrap and log-convexity | 100 | HOLDS AFTER CORRECTION: these concern S_-; remove universal method exclusions |
| 5.4 and 6.6: attempts provide no supplier | 102, 119 | HOLDS AFTER CORRECTION to the attempts actually displayed |
| 6.1: sheet identities and averaging variance | 106–109 | HOLDS AFTER CORRECTION: averaged second moments; size assumptions remain GUIDE |
| 6.2: coupling and influence-ceiling reading | 111 | HOLDS AFTER CORRECTION of scope |
| 6.3: clustering comparison and required thickness | 113 | HOLDS AFTER CORRECTION of hypotheses, prefactor and lambda dependence |
| 6.4: Ward/curvature discussion | 115 | HOLDS AFTER CORRECTION of tangent convention and missing application |
| 6.5: recalled Wilson-loop inequality | 117 | HOLDS AFTER CORRECTION: use the twist deficit |
| Step 7 common relative-threshold test | 123 | HOLDS |
| 7.1: row 786 cited as a twist/flux theorem | 125 | FAILS: cited source contains no such theorem |
| 7.1: spin-wave calculation and seed arithmetic | 126–130 | HOLDS AFTER CORRECTION of limiting regimes and gap denominator |
| 7.2: no continuous gradient; discrete T6 | 132, 134 | HOLDS with the precise energy convention above |
| 7.2: domain-wall size and “both analogues” conclusion | 133, 135 | FAILS as a quantitative deduction; conditional heuristic only |
| 7.3–7.4: actual SU(2) absorption and rival diagnosis | 137–139 | HOLDS AFTER CORRECTION to conditional physical interpretation |
| 8.1: quoted Langevin status | 143 | HOLDS as a citation of the stated upstream ranges, not a fresh check |
| 8.2: `p<=2 FR_u/lambda_odd` | 145–147 | HOLDS; the same identities give `p<=FR_u/(2lambda_odd)` |
| 8.3: ODD-0 | 149–150 | HOLDS, equality `lambda_odd=3L_1` |
| 8.3: one-line Rayleigh quotient | 151 | HOLDS |
| 8.3: averaged-line quotient and collective modes | 152 | HOLDS AFTER CORRECTION: distinguish exact quotient from correlation and model premises |
| 8.4(1): no gain from slab identities alone | 155 | HOLDS AFTER CORRECTION to the displayed identities, not all possible estimates |
| 8.4(2): two-block comparison | 156 | HOLDS AFTER CORRECTION: uniform conditional gaps and maximal correlation; no transferred ceiling |
| 8.4(3): flat walls witness failed supremum FR | 157 | FAILS: every response gradient is zero at central flat walls |
| 8.4(4): gap/response trade-off | 158 | HOLDS AFTER CORRECTION: retain `1-p_*` and the asymptotic error |
| 8.5 and original RESULT | 160–166 | HOLDS AFTER CORRECTION by the preceding verdicts; no unconditional order-one claim survives |

The two important exact outputs survive: the variance/weighted-energy
description under w_e, and the odd-Langevin sufficient criterion.
They leave both the needed FR estimate and an applicable order-one odd
gap open. The asymptotic calculation supplies neither uniformity in B
nor uniformity along first passage. The counterexample at flat walls
removes a claimed obstruction; it does not establish the supremum bound.

Not re-proved: the upstream Wilson transfer construction, the existing
strong-coupling Langevin-gap theorems, Theorem V, Balaban's UV estimates,
or the external confinement literature. Not performed: numerical runs,
Lean, audits, registry/status edits, commits, pushes, or outward posts.
The sole deliverable is this local research check at the requested path.

RESULT: The exact force-response, even-law variance/weighted-energy identities, odd-Langevin implication, ODD-0 and line quotients survive, with the stated conventions; the large-time threshold, spectral-gap identification and fact-test readings need the explicit corrections above; the cited U(1) flux theorem, frozen-group quantitative deduction and flat-wall force witness FAIL. FR, an order-one odd gap and cutoff uniformity remain open; this research check grants no status.
