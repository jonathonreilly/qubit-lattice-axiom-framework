# Repo search

**READ.** This checkout is pinned at
`9bb28a2fa8fdd1c1647aed0750dcb0a95567caeb`.
`prior/gap-joint-astra.md` is absent. The lead's
`prior/repo-search-2026-11-08.md` was read in full. It records
searches of main and PRs 10114, 10133, 10134 and 10141, mainly for
earlier RG targets. Its closest transfer hit is the soft-route
`MASS_GAP_LOCAL_BLOCK_ASTRA.md`. I fetched PR 10114 and read lines
1–166. Credit its Codex author for retaining the actual exterior
kernel in the local comparison. That result is a one-step local
witness, not the odd wrapping-sector upper bound requested here.
The fetched heads were main
`bb4ec020d5ada57c630dd89acc98a68397ade423` and PR 10114
`f76f6c649cff7dffbab664d8976e680e8f287fe9`.

**READ.** Two other useful prior passages were read on that PR:
`RD3.md:565–575` retains the same reference for event costs;
`RD4.md:448–460,687–694` requires exact overlap factorization before
a connected logarithm. Those are conditional soft-route results.
They do not supply the Wilson vortex activities below. Fresh main
and local target searches are retrieval checks, not an absence
theorem. The main and index discovery outputs are saved in
`/tmp/sa-gap-joint-astra.9OGb70/logs/`.
Searches of `open-registry.md`, `open-core.md`
and `l17c.md` found no other owner under gap-joint, gap-expose,
gap-block, gap-tree, joint resummation, odd sector, vortex or
icosahedral. FINISH row 811 is the present assignment.

**READ.** The closest results are already in this lane:
`gap-expose-astra.md` (E1)–(E18), with its line-by-line check by
Claude Opus 5.5; `gap-block-astra.md` sections 6–7, with the
corresponding check; and `gap-tree-astra.md` sections 3–6.
Credit Codex gpt-6-astra for those author arguments and Claude
Opus 5.5 for the checks. They supply the conserved flux, the
layerwise obstruction, the flat-plane weight, and the degree-twelve
distinction. None supplies the joint normalized activity estimate.
Those results are reused, not presented as new proofs.

# Joint surface sums with the original trace denominator

Author: **Codex gpt-6-astra max**, FINISH row 811, 2026-11-12.
Research text, not an audit; this grants no scientific status.
**READ** reports a source. **PROVED** means a hand argument in this
note, not an independent check. **ARGUED**, **GUIDE**, and **OPEN**
have their literal meanings. Definitions inherit their paragraph's label.

**READ.** Credit **Ethan Sussman and Levent Alpoge, with Claude and
Codex as the authors of their text**, for the convolution, transfer
trace and polymer convergence machinery used here. Their outline and
CA-I at `31a47c543775` were downloaded once each into the new scratch
directory `/tmp/sa-gap-joint-astra.9OGb70/`. Index lookup preceded
source reads. No downloaded paper is copied into the checkout.
The specified paper directory is absent on this machine.

## Checkpoint

**PROVED / OPEN — final checkpoint.** (J4) groups connected parity
surfaces, with their spin sums and integer-spin vacuum decorations
inside one integral and the original trace in the denominator.
(J9) gives a strong-coupling area bound. (J13) rules out the
uniform `400q<1` single-surface budget at beta one-half for the
stated ordering; it does not rule out the needed shape-sensitive
bound (J12). The high-spin and commutator tests in section 5
leave the signed low-spin Wilson comparison open. The next
decision is whether a class containing flat and almost-flat
surfaces admits a volume-uniform bound after its decorations
are summed. Source revisions are recorded above; no status is granted.

## 1. Exact activities after summing the vacuum decorations

**READ — setting.** Use (E1)–(E5) of `gap-expose-astra.md`.
The lattice has periods `n=(a,a,c,d)`, with `a>=3` and
`c,d in {a,2a}`. In a chosen frame, m is spatial and v is
the temporal twist paired with direction i. Drop the common
constant `exp(-beta N_p)` and write

\[
 Z_m=\int\prod_p e^{\beta\eta_{m,p}x_p}\,dU
     =\operatorname{Tr}L_m^{n_r},\qquad
 p_m(v)=\frac{Z_m-Z_{m+v}}{2Z_m}
       =\frac{\operatorname{Tr}(P_-L_m^{n_r})}
                    {\operatorname{Tr}L_m^{n_r}}.                 \tag{J1}
\]

Here `x_p=tr(U_p)/2`, `N_p=6a^2cd<=24a^4`, and `eta_m`
is a closed sign cocycle. For these pairs, `0<Z_(m+v)<=Z_m`.
The target (E17) is `Q_F<=C a^p eta_*^(a/2)`, with the given
`0<eta_*<1`, uniformly on `I=[beta_-,beta_+]` inside `(0,infinity)`.
Its maximum is over the frame-1 crossed pairs `m_2=0, i=3,4`.

**READ — the starting identity is already Proposition SC.**
`gap-kappa-order.md:35–74`, by Claude Fable 5.2, expands each
plaquette into sinh and cosh. Link sign changes eliminate nonclosed
sets. We use this identity; we do not claim a new surface expansion.

**PROVED — connected resummation of that identity.** Let `cal S`
be the finite set of nonempty, link-connected, closed mod-two
plaquette surfaces. Branching is allowed. Two members are
incompatible when they share a link, including self-incompatibility.
Every closed plaquette set has a unique decomposition into compatible
members of `cal S`. Each component is closed because all faces
incident to one link belong to the same component.

Set

\[
 C(U)=\prod_p\cosh(\beta x_p)>0,\quad t_p(U)=\tanh(\beta x_p),
 \quad w_m(S;U)=(-1)^{\langle m,S\rangle}\prod_{p\in S}t_p(U),
\]
\[
 \Xi(w;U)=\sum_{\mathcal F\ {m compatible}}
                      \prod_{S\in\mathcal F}w(S;U).
 \qquad Z_m=\int C(U)\Xi(w_m;U)\,dU.                    \tag{J2}
\]

The second equality is SC followed by the unique decomposition.
The cocycle pairing is independent of its representative.
All sums in (J2) are finite, at every finite beta. This is a
polymer polynomial depending on U, integrated against one common
positive weight. It is not a gas of independent SU(2) activities.

There is also pointwise positivity for the two physical endpoints.
Here `E_4` is the full spacetime edge set:

\[
 C(U)\Xi(w_m;U)=2^{-|E_4|}\sum_{b\in\mathbb F_2^{E_4}}
       \exp\!\left\{\beta\sum_p
             \eta_{m,p}(-1)^{(db)_p}x_p(U)\right\}>0.       \tag{J3}
\]

To verify (J3), expand each exponential as cosh plus signed sinh.
The average of `(-1)^<b,partial S>` is one if `partial S=0`
and zero otherwise. No gauge-orbit division or stabilizer factor
is omitted: this is an average over all link sign cochains.

**PROVED — a finite identity for single-surface contributions.**
Order the surfaces with `v(S):=<v,S>=1` in any deterministic order.
For one such S, let `w^[S]` have weight `-w_m(T)` on earlier odd
surfaces, and `w_m(T)` on later odd and on every even surface.
Its value on S is immaterial below. Write `Xi_comp(S)` for the
polymer polynomial restricted to surfaces compatible with S.
Define

\[
 D_m(S)=\frac1{Z_m}\int C(U)\,w_m(S;U)
                  \Xi_{\rm comp(S)}(w^{[S]};U)\,dU.
 \qquad p_m(v)=\sum_{S:v(S)=1}D_m(S).                    \tag{J4}
\]

Proof: change the signs of the odd polymer variables one at a time.
The polynomial is affine in each variable. Its derivative with
respect to `w(S)` is exactly `Xi_comp(S)`, so that change subtracts
`2w_m(S) Xi_comp(S)`. Telescope, integrate, and use (J1).
No logarithm, convergence premise, division by an intermediate
partition function, or positivity of D is needed.

**PROVED — what is summed before the absolute value.** In each
term of (J4), `C prod t_p` is a product of sinh on the selected
surfaces and cosh elsewhere. The full half-integer character sum
on every selected face and the full integer character sum on every
other face have therefore already been performed. All integer-spin
vacuum decorations, including ones attached to S, remain inside
the same integral. The polynomial sums every compatible closed
parity component, with its signs, before `|D_m(S)|` is taken.
Disconnected vacuum contributions are retained through the same
`Z_m=Tr L_m^(n_r)` as the consumer. No isolated-block scalar is used.
The factorial bound (GL3) and `|chi_j|<=d_j` make each
character series uniformly absolutely convergent. There are
finitely many faces, so these regroupings are legitimate.
Individual integrands and D's can have either sign. (J3) does not
assert their positivity or that of arbitrary intermediate polynomials.

This is joint across all time layers. The temporal faces and spatial
faces are precisely the closed two-chain of (E5); no separate
absolute estimate of a layer selector occurs. It lies outside the
obstruction class of row 809.

## 2. Strong-coupling check, with the normalization fixed

**READ — the combinatorial theorem is already proved.**
The index rows at `sa-index/chunk-01.md:118–145` and
`obligations.md:34–48` lead to outline lines 1150–1375, read here.
Sussman and Alpoge prove the connected logarithm, its tree
cancellation, and the rooted bound under

\[
 \sum_{T\not\sim S}|w(T)|e^{b(T)}\le b(S).               \tag{J5}
\]

Credit Kotecky and Preiss for this criterion, as their text does.
The outline explicitly leaves the activity estimate to its user.
We apply its proved theorem; we do not rebuild its tree argument.
Outline 2195–2244 and 2313–2393 supplies (GL3), (GL4), (GL8)
and (GL10), also read here after the index lookup. None supplies
the order-one estimate in section 3. The indexed target searches
found no corresponding vortex estimate in CA-I items 4.12–4.19.
CA-I 2698–2716 keeps a mass gap outside the asserted theorem.

**PROVED — a uniform domain where (J4) is small.** Put
`t=tanh(beta)`, `rho=400 e t`, and assume `rho<=1/2`.
For example, `0<=beta<=1/2400` suffices, since `e<3` and
`tanh(beta)<=beta`. A plaquette has at most twenty link-neighbours.
The existing depth-first tree count gives at most `400^(k-1)`
connected k-face sets through a given face. The closed surfaces
are a subset. Thus, with `b(S)=|S|`,

\[
 \sum_{T\not\sim S}|w(T)|e^{|T|}
 \le21|S|\sum_{k\ge1}400^{k-1}(et)^k
 =\frac{21|S|et}{1-400et}\le\frac{21}{400}|S|<|S|.        \tag{J6}
\]

The factor 21 includes the face itself. This estimate holds for
every U, for all choices of signs of the polymer variables, and
after deleting polymers. The common majorant permits all sums
and integrals below. The logarithm branch starts at zero activity;
on real activities its exponential is positive by continuity and
nonvanishing. This statement includes the intermediate polynomials
in this small-coupling domain only.

**PROVED — cancellation of the vacuum logarithm.** In the connected
logarithm, a cluster without an odd surface has identical weight
before and after any chosen subset of odd signs is flipped.
Every surviving difference contains an odd root. Its coefficient
changes by at most two in absolute value. Sum over such roots;
overcounting only enlarges the bound. The rooted estimate from
(J5) bounds the decorations of a root S by `e^|S|`. The area
lemma of `gap-kappa-order.md` gives `|S|>=A_0=n_r n_i`
when `v(S)=1`. Consequently every such sign change obeys

\[
 |\log\Xi(w';U)-\log\Xi(w_m;U)|\le\delta_\Lambda,
 \qquad
 \delta_\Lambda=
     \frac{N_p}{200}\frac{\rho^{A_0}}{1-\rho}.             \tag{J7}
\]

For clarity, the factorial in a rooted list is `1/(k-1)!`.
The sum over all possible odd roots dominates the unrooted
`1/k!` difference, including repeated polymers. This is exactly
the rooted series bounded in the cited theorem. It retains the
cancellation over connected graphs before the absolute value.

Deleting the polymers incompatible with a fixed S changes the
logarithm by at most
`sum_(T incompatible S) |w(T)| e^|T| <= |S|`.
This follows by rooting each removed cluster at one of its
deleted polymers and using the same bound. Combining it with
(J7) gives, directly for the fully dressed activities in (J4),

\[
 |D_m(S)|\le e^{\delta_\Lambda}(et)^{|S|}.                \tag{J8}
\]

Indeed divide the integrand by the positive `Xi(w_m;U)`,
apply the pointwise bounds, and integrate against the probability
measure `C Xi(w_m) dU/Z_m`. The denominator is still the full
Wilson trace. On the stated aspect ratios, `delta_Lambda` is
bounded uniformly in a and tends to zero as a grows.

Apply (J7) to all odd signs. It gives pointwise
`Xi_(m+v)>=exp(-delta_Lambda) Xi_m`.
Integrating against C and using (J1) proves

\[
 0\le F_m(v):=-\log(Z_{m+v}/Z_m)\le\delta_\Lambda,
 \qquad 0\le p_m(v)\le\delta_\Lambda/2.                  \tag{J9}
\]

This is a uniform exponential-in-area vortex bound. On a compact
positive subinterval of this domain it implies (E17) for every
fixed `0<eta_*<1`: `a^4 rho^(a^2)` eventually beats
`eta_*^(a/2)`, and the finitely many remaining a enlarge C.
This recovers a strong-coupling result, not an extension to order one.

**PROVED — the leading surface and its factor.** For a fixed torus,
the minimal closed set paired oddly with v is a translated flat
`(r,i)` plane. The area lemma forces one `(r,i)` face in every
stack; at equality all other orientations are absent. Closure at
its r- and i-links forces translation invariance in those two
directions, hence a plane. There are
`N_perp=product_(k notin {r,i}) n_k` such planes.
The already proved torus integral in Lemma T is `4^(-A_0)`.
The leading sinh term is `beta x_p`; every cosh has constant term
one. Spatial m pairs trivially with these temporal planes. Thus

\[
 p_m(v)=N_\perp(\beta/4)^{A_0}(1+O_\Lambda(\beta)),\qquad
 F_m(v)=2N_\perp(\beta/4)^{A_0}(1+O_\Lambda(\beta)).        \tag{J10}
\]

The remainder here is at fixed volume, not a uniform large-area
asymptotic. Analyticity follows from finite bounded group integrals
and `Z_m(0)=1`. Since `r_(1/2)=beta/4+O(beta^3)`, the leading
term agrees with the exact undecorated weight `r_(1/2)^A_0`.
The full decoration sum in (J4) has not changed that coefficient.

**READ — comparison with the requested literature.**
`prior/gap-lit-transport.md` credits Gerhard Muenster's 1981
strong-coupling vortex expansion. The journal DOI was inaccessible
in this run. The cited contemporaneous account by **Gerhard Mack
and Hildegard Meyer**, *Nuclear Physics B200* (1982), pp. 250–251,
equations (1.1)–(1.2), was read from rendered PDF pages in
`/tmp/sa-gap-joint-astra-paper.FnBGek/`. It defines
`vortex free energy = -(1/2) log(Z_tw/Z)`, not F as defined here.
Its exponential has transverse area in the exponent and its
prefactor counts the longitudinal area in lattice units.
Thus (J9) has the stated area-decay form, and half of (J10) has
the correct leading prefactor. The text attributes the all-orders
identification of its exponent with string tension to Muenster.
That stronger identification is not proved anew here.
[Mack–Meyer scan](https://www-library.desy.de/preparch/desy/postpr/1981/desy81-050.pdf).

**READ — comparison with the checked local results.**
`gap-vmf-lip.md`, by Codex gpt-6-astra, gives chord DC and INF,
the background-uniform layer estimate for `beta<2/3`, and the
full seed for `beta<2/9`. Its source and proofs were read, as
were the Theorem V and scope passages of its Claude Opus 5.5
check. The check's one-coordinate variance convention is retained.
(J2)–(J4) are exact identities for the same Wilson integrals at
all beta, so they preserve those conclusions. Our elementary
domain `beta<=1/2400` is smaller; it is not an improved seed.
The distinctions between a one-layer twist, a full seed, and the
area estimate are retained. No numerical check enters this comparison.

## 3. What would suffice at order one

**PROVED conditional criterion; its premise is excluded below.**
For the activities defined in (J4), one convenient sufficient
single-surface statement would be

\[
 \left|\int Cw_m(S)\Xi_{\rm comp(S)}(w^{[S]})\,dU\right|
       \le C_0q^{|S|}Z_m,\qquad 400q<1,                 \tag{J11}
\]

uniformly in the admissible geometry, beta in I, crossed pair,
and odd S, with a fixed specified ordering. Constants independent
of the lattice are essential. The old connected-set count would
then give `p_m(v)<=C_0 N_p (400q)^A_0/[400(1-400q)]`.
This is a scalar inequality against the actual trace. It is not
an all-exterior operator inequality of the kind refuted by (E7).
Section 4 proves that (J11) is too strong for a natural ordering
on `I_0=[1/2,1]`, even after the resummation in (J4).

**OPEN — the weaker useful criterion.** Fix one root face `root(S)`
of each surface. A sufficient replacement, permitting different
payments for flat and highly branched shapes, is

\[
 \sup_p\sum_{\substack{S:v(S)=1\\root(S)=p}}
          |D_m(S)|\le C_1 a^b e^{-\kappa a},
 \qquad \kappa\ge\tfrac12\log(1/\eta_*).                 \tag{J12}
\]

Here `C_1>0`, `b>=0`, and kappa are uniform in beta, geometry
and crossed pair. Then
`Q_F<=24 C_1 a^(b+4) eta_*^(a/2)`. This is the weakest
absolute-surface statement used in this note. It is still stronger
than the desired signed sum. It is not proved at order one, and
renaming it does not reduce its analytic content. A useful producer
would bound each class of shapes with its actual multiplicity,
or sum whole block interiors before forming the classes. The
constant 400 is not a lower bound on surface entropy.

## 4. An actual dressed plane defeats the uniform 400 budget

**PROVED — scope.** Take the untwisted measure `m=0`, any temporal
pair `(r,i)`, and a translated flat `(r,i)` plane S of area
`A=n_r n_i`. Put this S first in the ordering of odd surfaces.
At `beta=1/2`, for every allowed torus,

\[
                    D_0(S)>216^{-A}.                    \tag{J13}
\]

This refutes (J11) on any interval containing `1/2` for this
ordering, even with any fixed polynomial prefactor in the periods.
It does not refute (J12), an area law, or a different grouping of
the activities. In particular, the number of flat planes is only
polynomial; charging them the entropy of all connected sets is
unnecessary. The point of (J13) is that a failed upper majorant
has now been replaced by a lower bound on an actual dressed term.

**PROVED — an exact expression for the first activity.** Let N(S)
be the faces sharing a link with S, including S itself, and let
`P_far=P\N(S)`. Since S is first, the intermediate weights in
(J4) are the original weights. Expanding the last product below
and eliminating nonclosed parity sets by link signs gives

\[
 Z_mD_0(S)=Z_S^{\rm dec}:=
 \int\prod_{p\in S}\sinh(\beta x_p)
       \prod_{p\in N(S)\setminus S}\cosh(\beta x_p)
       \prod_{p\in P_{\rm far}}e^{\beta x_p}\,dU.          \tag{J14}
\]

Here `Z_m=Z_0`. Indeed the remaining odd faces can occur only
outside N(S). After integration they form precisely the closed
components compatible with S. Formula (J14) includes every
integer-spin decoration on and next to the plane.

**PROVED — a positive-transfer lower bound, despite the sinh.**
Choose r as time. The pattern in (J14) is time independent.
Every sinh face is temporal. Its convolution is positive
semidefinite: its eigenvalues are `c_j=z r_j` for half-integer
j and zero for integer j. The cosh convolution has `c_j` on
integer j and zero on half-integer j. In particular
`C_cosh>=C_1`, since the constant-kernel operator has only the
spin-zero eigenvalue one and `z>=1`. The full exponential
convolution is positive as well. Spatial factors in (J14) are
strictly positive; its spatial cosh factors are at least one.
The transfer identity is algebraic in the central face kernels,
so it applies also to these signed temporal kernels. Their
Fourier coefficients supply the positive operator used here.

Replace every cosh factor in (J14) by one. This cannot increase
the transfer trace. To justify both types of replacement, denote
the positive temporal tensor product by K and the spatial
multiplier by B, on the common gauge-invariant space. For fixed
B use `B^(1/2) K B^(1/2)` to compare `K>=K_0`. For fixed K_0
use `K_0^(1/2) B K_0^(1/2)` to compare `B>=B_0`. The two cuts
have the same nonzero eigenvalues. Gauge projection commutes
with these factors and preserves the order. The min-max principle
therefore compares every eigenvalue and then the trace of its
`n_r`th power. No operator monotonicity of powers is asserted.

The resulting integral factors into the isolated plane and the
far integral `Z_far`, because their plaquettes share no links.
Schur orthogonality on a two-dimensional torus gives

\[
 Z_S^{\rm dec}\ge Z_{\rm far}\,z^A
          \sum_{j\in\frac12+\mathbb N_0}r_j^A
       \ge Z_{\rm far}\,r_{1/2}^A.                     \tag{J15}
\]

For completeness, on that torus each edge joins two faces.
Orthogonality makes their spins equal, hence the spin is constant
on the connected torus. Each edge contributes `d_j^(-1)`, each
vertex a closed index trace `d_j`, and each face `d_j c_j`.
Since `F-E+V=0`, the result is `c_j^A`. Summing its allowed
half-integer spins proves the first sum in (J15). This also
recovers the fundamental-plane calculation already used in row 804.

**PROVED — the same full normalization costs only a local factor.**
There are `2A` plane links. Each belongs to six plaquettes.
The A plane faces account for four incidences each; every other
face touching the plane has exactly one plane link. Thus
`|N(S)|=A+8A=9A`. Periods at least three ensure the counts have
no identified neighbour or repeated edge.

Integrate the plane links in any fixed order, keeping all other
links fixed. Assign every face in N(S) to its first integrated
plane link. Let `k_e` be the number assigned to e. Then
`0<=k_e<=6` and `sum_e k_e=9A`. At the step for e, the factors
still depending on e have exponent `F_e.h_e`, in quaternion
coordinates, with `|F_e|<=beta k_e`. Their Haar integral is
`z(|F_e|)` and is at most `z(beta k_e)`.

Theorem V of `gap-vmf-lip.md` gives
`(log z)''(u)=Var_u(h_1)<=1/4` for all real u. Since
`log z(0)=(log z)'(0)=0`, two integrations give
`log z(u)<=u^2/8`. Applying this uniform bound removes the
assigned plaquettes and creates no new interaction. Induction
over the chosen links proves

\[
 Z_0\le Z_{\rm far}\exp\!\left\{
                 \frac{\beta^2}{8}\sum_e k_e^2\right\}
      \le Z_{\rm far}\exp(27\beta^2 A/4).               \tag{J16}
\]

This bound is uniform in the fixed exterior before it is
integrated. Combine (J15) and (J16):

\[
 D_0(S)\ge[\,r_{1/2}(\beta)e^{-27\beta^2/4}\,]^A.        \tag{J17}
\]

Use the already proved lower bound
`r_(1/2)(beta)>=beta/(4 e^beta)` from (E15). At `beta=1/2`
the bracket in (J17) is at least
`e^(-35/16)/8 > 1/(8 e^3)>1/216`, because `e<3`.
This proves (J13), without evaluating a Bessel function.
If (J11) held with `q<1/400`, it would imply
`(1/(216q))^A<C_0`, or the same inequality with a polynomial
on the right. Letting A grow contradicts either version.

**PROVED — the pointwise strong-coupling criterion also fails.**
One cannot extend (J6) to `beta=1/2` by sharper arithmetic
while retaining `b(S)=|S|` and a bound for every U. Set all
links to identity. Three elementary cube boundaries incompatible
with a fixed cube boundary exist: itself and two adjacent cubes.
Each has activity magnitude `t^6`, with `t=tanh(1/2)`.
Since `e>8/3`, we have `et>40/33>6/5`, and
`(et)^6>(6/5)^4=1296/625>2`. These three terms alone give
`sum_(T incompatible S) |w(T)|e^|T|>6=|S|`, violating (J5).
The violation persists on an open neighbourhood by continuity.
This is a counterexample to that criterion, not to convergence
under every possible resummation or weight b.

## 5. Attempts using the SU(2)-specific inputs

### 5.1 High spins: a true scalar tail, and the missing use of the filter

**PROVED — a fixed-face remainder with the right denominator.**
There is a useful estimate weaker than the relative operator
estimate that (E6) forbids. Define the unnormalized parent-spin tail

\[
 H_J(g)=z(\beta)\sum_{j>J}d_jr_j(\beta)\chi_j(g),\qquad
 \epsilon_J=\sup_{\beta\in I}
           z(\beta)e^\beta\sum_{j>J}d_j^2r_j(\beta).
                                                               \tag{J18}
\]

For a fixed set H of plaquettes, replace exactly those Wilson
factors in the original integral by `H_J(eta_(m,p) U_p)` and
leave every other plaquette factor unchanged. Call the resulting
signed integral `Z_m[H,J]`. Then

\[
 \frac{|Z_m[H,J]|}{Z_m}\le\epsilon_J^{|H|},\qquad
                         \epsilon_J\longrightarrow0.            \tag{J19}
\]

Indeed `|chi_j(g)|<=d_j` and `e^(beta eta x)>=e^(-beta)`
bound the absolute ratio of one replaced factor to its original
positive factor by epsilon_J, pointwise. Multiply the inequalities
and integrate against the original probability measure. The
factorial bound from (GL4) gives the explicit majorant

\[
 \epsilon_J\le e^{2\beta_+}
    \sum_{j>J}(2j+1)^2
                \frac{(\beta_+/2)^{2j}}{(2j+1)!}.                 \tag{J20}
\]

Its successive-term ratio tends to zero, so its tail tends to
zero by a geometric comparison after any sufficiently large
index. This is a hand existence argument, uniform on I.
No numerical cutoff choice is required.

**ARGUED — why this does not close (J12).** (J19) has a physical
positive exterior. It is a plaquette-function replacement, not
an orthogonal selector of a temporal link representation. Thus
it does not contradict (E6). It supplies neither the marked
surface polynomial in (J4) nor a dense set H in every winding
configuration. Summing arbitrary subsets H without locality
costs `(1+epsilon_J)^N_p`. Resumming this vacuum cost before a
surface estimate is precisely what is needed; it cannot be
replaced by declaring epsilon_J small.

Moreover, (J19) is **not SU(2)-selective**. The pointwise parent
character expansion can be restricted to U(1) or Gamma. The
same bound on H_J holds there, against their own positive Wilson
integrals. This scalar tail is different from convolving the
Wilson law of those groups on a high parent representation.

**READ — the genuinely distinguishing estimate.** The checked
(G12)–(G17a) in `gap-tree-astra.md` give, on
`V tensor Sym^(12k) V`,

\[
 \|C_{\beta}^{SU(2)}\|
 \le\frac{(\beta_+/2)^{12k-1}}{(12k)!}
       +\frac{(\beta_+/2)^{12k+1}}{(12k+2)!}
          \longrightarrow0.                                    \tag{J21}
\]

For Gamma its invariant `h^k in Sym^(12k) V` leaves a copy of
V with eigenvalue at least `beta_-/(4 exp(beta_+))`. U(1)
leaves a weight-one copy with eigenvalue at least
`beta_-/(2 exp(beta_+))`. These are the exact failing steps for
transplanting (J21). The first extra Gamma Haar invariant is
at degree twelve; Haar tensors agree through degree eleven.
The final simplified constants in (G16) are used only in their
checked range `beta<=1`. No such simplification is needed here.

**ARGUED — the attempted insertion into (J4).** Re-expanding the
sinh/cosh factors recovers the genuine Wilson Haar tensors.
They do not insert the convolution in (J21). The already proved
(G19) charges an inverse contraction for inserting a filter into
a Haar invariant tensor. (G20) retains charged spin one-half
even with arbitrarily many strands. The existing (G20)–(G21)
refute mandatory high-spin exposure of every winding term.
(J13) adds a lower bound with the decorations and original
normalization retained. It does not identify which spins dominate
that dressed integral. The earlier counterexamples are reused.

The remaining possibility is an exact joint block identity that
redistributes the low-spin terms and uses (J21) on the generated
channels, with its scalar comparison paid. No such identity or
low-spin estimate is supplied by the degree-twelve moment test.
Increasing J improves (J20), but does not estimate that low-spin
block. This attack stops at a specific missing Wilson realization,
not at the size of the factorial remainder.

### 5.2 Small commutators: coherent products and low-spin averaging

**READ.** Section 4.2 of `gap-ext-astra.md`, checked by Claude
Opus 5.5, supplies (LC):
`[A_N,B_N]=C_N=exp(i pi sigma_3/N)`, `C_N^N=-I`, with the
stated generator and commutator costs. U(1) fails because its
commutators are identity. Gamma fails because its identity is
isolated, so sufficiently small generators must be identity.
These are actual algebraic distinctions. They give no bound
on the other plaquettes changed by a Wilson-field deformation.

**PROVED — the low-spin test for independent conjugacy averages.**
Let `nu_N` be the law of the product of N independently Haar
conjugated copies of C_N. On spin j, its convolution is scalar
with eigenvalue `c_(j,N)^N`, where

\[
 c_{j,N}=\frac1{2j+1}\sum_{m=-j}^j
                     \cos(2\pi m/N)
 \ge1-\frac{2\pi^2j(j+1)}{3N^2}.                         \tag{J22}
\]

The sum uses step one in m. The bound is `cos u>=1-u^2/2`
and `sum_(m=-j)^j m^2=(2j+1)j(j+1)/3`; the latter follows
by the elementary square-sum formula, also for half-integer j.
Schur averaging makes each conjugated representation matrix a
scalar, and independence multiplies the scalars. For fixed J
and N large enough that the bound is nonnegative, Bernoulli's
inequality yields, uniformly for `0<=j<=J`,

\[
 c_{j,N}^N\ge1-\frac{2\pi^2J(J+1)}{3N}
                    \longrightarrow1.                          \tag{J23}
\]

Thus this explicit way to use (LC) barely changes any fixed
low-spin channel. It cannot give a fixed contraction there as
N grows. For `j=1/2` this is the already known obstruction
(E18)–(E20) of `gap-ext-astra.md`; (J22) states its whole
finite low-spin version. The coherent unrandomized product is
`-I` and has unit norm on every representation. It is a sign
change, not damping.

**ARGUED — what this test leaves.** A correlated deformation can
evade independent averaging; the existing common-coin example
already shows that. To use it in (J4), one must transform the
original links, retain the changed cosh background and all
compatible-surface factors, and control their joint integral
relative to Z_m. The last inequality in (LC) controls only the
commutator elements. It is not that integral estimate. No
correlated Wilson deformation meeting (J12) was obtained here.

### 5.3 Control groups and the scope of the failed attempts

**READ / PROVED — comparison table.**

| Step | SU(2) | U(1) | Binary icosahedral Gamma |
|---|---|---|---|
| (J2)–(J4), using central minus identity | Exact | Exact | Exact |
| Small-beta (J6)–(J9) | Holds | Same surface proof holds | Same surface proof holds |
| Fixed-face scalar tail (J19) in SU(2) parent characters | Holds | Holds after restriction | Holds after restriction |
| Charged high-parent convolution (J21) | Factorial smallness | Weight-one copy prevents it | `V tensor h^k` prevents it; first invariant at degree twelve |
| Nontrivial commutators approaching identity in (LC) | Available | Commutator identically identity | Discreteness prevents the sequence |
| Low-spin Wilson realization and bound (J12) at order one | OPEN | No conclusion | No conclusion |

The small-beta construction must be shared by the controls;
there is no group-selective premise in its proof. The last two
group-specific inputs have named failures, but their use in the
actual low-spin activity bound is still missing for SU(2).
No claim is made that (E17) itself is false for either control
on the particular interval `[1/2,1]`.

## 6. Exact remaining obligation and verification boundary

**OPEN.** The order-one obligation is the rooted normalized bound
(J12), or a weaker signed estimate of the sum in (J4). Its
integral must keep C, the intermediate compatible-surface sum,
and the original Z_m together. The difficult part is the signed
low-spin contribution with its attached integer-spin decorations.
A fixed-face high-spin bound is available in (J19); summing it
with those decorations and preserving a volume-free comparison
is not done. The existing parent-spin filters and (LC) do not
perform that resummation.

**ARGUED — what the three attacks decide.** The pointwise cluster
criterion works at small beta but fails at an explicit flat
configuration at `beta=1/2`. The uniform single-surface area
budget with factor 400 fails even after integration, by (J13).
The representation-theoretic attack isolates a controllable
fixed-face tail, but leaves the charged low-spin Wilson block
unestimated. The (LC) attack preserves those low spins under
independent isotropic averaging; its correlated alternative still
owes the full Wilson action and normalization. These are scoped
failures. They do not exclude a block resummation with a more
accurate count of shapes or useful cancellations between surfaces.

**GUIDE — next decision.** Do not request another termwise
high-spin exposure or a uniform factor below `1/400` for every
elementary surface. An informative next attempt would retain
the flat and almost-flat families inside one resummed class,
then estimate the remaining low-spin branching with its actual
shape count and the same exterior integral. Its first decisive
test is a volume-uniform bound for that class under attached
integer-spin decorations. This is a proposed next action, not
a theorem that such a bound exists.

**READ — verification.** All new mathematics above is by hand.
No numeric run, search over configurations, interval certificate,
or computer-assisted proof was used. Commands fetched and read
sources, rendered two literature pages, and edited this note.
The DOI lookup and the web PDF screenshot attempts failed; the
downloaded Mack–Meyer PDF was rendered locally instead. No
Muenster theorem beyond the stated reading was imported.
The new arguments have not been independently checked. A check
should focus on the intermediate-polynomial identity (J4), the
positive-transfer comparison (J15), and the local normalization
bound (J16); (J13) depends on those exact three ingredients.
Only this assigned output file was changed. It remains local,
uncommitted and unpushed, on `research/gap-joint-astra-20261112`
at the requested base commit. No PR, public post, registry edit,
audit action, or scientific-status update was made.

RESULT: OPEN AT ORDER ONE — an exact jointly dressed surface representation retains the original odd-sector trace ratio, and its strong-coupling area bound and leading vortex coefficient are proved by hand. A fully dressed flat plane at beta=1/2 refutes the uniform single-surface budget q^A with 400q<1, for the stated ordering. The fixed-face tail is bounded with the same denominator, but the signed low-spin sum (J12) remains open; neither order-one (E17), (FQ), nor (V) is proved. Not independently checked.
