# Repo search

**READ.** This lane starts at `974b24a77862404946a0c034285b4e59a8793e70`.
`prior/gap-block-astra.md` is absent. The lead's November 8 search digest
concerns earlier admission and history tasks. Its closest hit is
PR 10114's `MASS_GAP_LOCAL_BLOCK_ASTRA.md`. I fetched that PR at
`f76f6c649cff7dffbab664d8976e680e8f287fe9` and read lines 1–166.
Its exact transfer, retained exterior normalization and positive local
witness are prior work. They do not estimate a wrapping twist deficit.
Credit its Codex author. Its different strong-coupling endpoint is not
re-derived here.

**READ.** Main was fetched at `bb4ec020d5ada57c630dd89acc98a68397ade423`.
The prior lane also names main's
`docs/BETA6_PLAQUETTE_TENSOR_NETWORK_FINITE_IRREP_SUPPORT_AND_RECOUPLING_WALL_NOTE_2026-06-04.md`.
I read it in full. It concerns SU(3), numerical coefficient samples,
and an unresolved higher-dimensional recoupling contraction. No numerical
assertion from it is an input. Its distinction between a face coefficient
and the sewn network remains relevant.

**READ.** `gap-tree-astra.md` was read in full. Its Haar-moment theorem,
distinguishing filters, free-insertion obstruction and flat-plane term
are inputs, not new results here. `gap-kappa-order.md:31–74` and
`prior/gap-seed-lit.md:47–53` retain the signed-contraction obstruction.
Credit Claude Fable 5.2 for the former, and Hendryk Pfeiffer and Robert
Oeckl for the dual representation described in the latter. Searches for
G22, charged boundary, resummed Wilson, Casimir filter, gap-block and
icosahedral in `open-registry.md`, `open-core.md` and `l17c.md` found no
other owner of this target. This is a bounded search, not an absence
theorem. The general four-PR search and row 804's more specific searches
are credited to their authors; they were not repeated wholesale.

# Exact Wilson blocks and the normalization obstruction

Author: **Codex gpt-6-astra max**, FINISH row 807, 2026-11-12.
Research text, not an audit; this grants no scientific status.
**READ** reports source content; **PROVED** labels a hand argument here,
not an independent check. **ARGUED** labels a scoped inference;
**GUIDE** labels a proposed route; **OPEN** labels a missing assertion.

**READ.** Credit **Ethan Sussman and Levent Alpoge, with Claude and
Codex as the authors of their text**, for all outline/account inputs.
Both specified files at `31a47c543775` were downloaded once into the new
empty directory `/tmp/sa-gap-block-astra.CAHwFy/`. Index lookups used the
README, chunk 02, chunk 29, obligations, and the 4.12–4.19/account indices.
Outline 2195–2257 supplies the Wilson convolution and its Bessel bounds.
Outline 2313–2393 supplies the exact transfer and the insertion inequality
(GL10); that inequality assumes a supplied contraction. It does not make
a contraction appear inside the original Wilson integral. Outline
31860–31884 and CA-I 2700–2716 explicitly separate the mass-gap question.
No matching charged Wilson-block theorem was located in the 4.12–4.19
index. Its large-field Schur complements are different objects.

## Checkpoint

**OPEN — final checkpoint.** The exact charged slab is (B2)–(B4).
With its Perron scalar it contracts for all three groups, (B5).
With its free-boundary scalar it expands at least as `c_B beta^(3/2)`
on the unit cube at large beta, (B8). The actual conditional cube
contracts for beta<1, (B27), but this omits the displayed multipliers
(B21)–(B22). The finite-matrix criterion (B19) retains every low-spin
channel and has a proved SU(2) tail; its degree-twelve step fails for
the controls. Its low-spin bound with a sewable scalar, and the exact
exposure representation in section 6, remain open. These are the next
decisions. No universal fixed-block impossibility, order-one (FQ), or
(V) is proved. No numerical calculation has been run.

## 1. An exact block and its charged boundary

**PROVED — construction, using the published transfer identity.** Let
`Q` be a finite rectangular three-dimensional lattice graph. Write `E`
for its spatial links, `P` for its spatial plaquettes, and `V_int` for
its interior vertices. There are at least two boundary vertices. Put
`b=|E|`, `p=|P|`, and use normalized product Haar measure throughout.
The three groups considered below are SU(2), its diagonal U(1), and
the binary icosahedral subgroup Gamma. In each case set

\[
 x(g)=\tfrac12\operatorname{tr}g,\quad
 w_\beta(g)=e^{\beta x(g)},\quad z_G=\int_G w_\beta,
 \quad k_G=w_\beta/z_G,
 \quad A(U)=\exp\{\tfrac\beta2\sum_{p\in P}x(U_p)\}.
 \tag{B1}
\]

The constant `exp(-beta)` per plaquette is omitted on both sides of
every identity; restoring it multiplies each operator and its scalar
by the same known factor. Let `C` be convolution by `k_G` on one link,
`K=C^{tensor E}`, and `P_int` the interior vertex gauge projection.
The boundary Hilbert space and one-step operator are

\[
 \mathcal H=L^2(G^E,dU)^{G^{V_{\rm int}}},\qquad
 T=z_G^b A K P_{\rm int} A\big|_{\mathcal H}.
 \tag{B2}
\]

This is the Wilson integral on `Q times [0,1]`. Interior time links
are integrated, while time links on its spatial boundary are fixed
to the identity. The two spatial ends receive half their plaquette
action. Thus sewing consecutive slabs gives full weight at each
interior layer, exactly once. Its literal kernel is

\[
 T(U,V)=A(U)A(V)\int_{G^{V_{\rm int}}}
       \prod_{e\in E}w_\beta\bigl(U_e(h\cdot V)_e^{-1}\bigr)\,dh.
 \tag{B3}
\]

Here boundary components of h are the identity. Equation (B3) follows
by writing each temporal plaquette with its two time links. It retains
all boundary spatial links and all representation channels. It is a
specialization of the transfer identity credited above, not a new
transfer method. For thickness n the exact kernel is `T^n`.

**PROVED — the charge is an actual boundary charge.** Choose a boundary
vertex v. Let Theta multiply each incident link by the central element
`-I`, with the usual orientation convention. This is a boundary gauge
action, not an interior constraint. Define

\[
 \mathcal H_-=\{f\in\mathcal H:f(\Theta U)=-f(U)\},
 \qquad P_-=\tfrac12(1-\Theta).
 \tag{B4}
\]

An open fundamental Wilson line from v to a different boundary vertex
has a nonzero matrix coefficient in this space. Interior gauge
transformations cancel along that line. A and K commute with Theta,
as does `P_int`; hence T preserves (B4). The norm used below is the
ordinary `L^2(dU)` operator norm on this space. No representation
subspace is substituted for the full boundary space.

**PROVED — exact resummation.** For SU(2), the cited character formula
gives `C=sum_j r_j Pi_j`, with `r_j=I_(2j+1)/I_1` and `r_0=1`.
Its factorial bound makes the character expansion absolutely and
uniformly convergent: `|chi_j|<=d_j` and `sum_j d_j^2 r_j<infinity`.
The finite product can therefore be integrated term by term. Conversely,
(B3) is that entire sum with every internal label resummed. On U(1),
the exponential power series gives the same justification; Gamma has
finitely many irreducibles. Positivity as an operator also holds for
all three: every term in `exp(beta chi_V/2)` is a positive multiple of
a representation character, hence a positive-definite function. A
positive sum is positive definite. Gauge averaging is an orthogonal
projection commuting with K and A. Thus `T>=0`. This argument assumes
no sign for an individual sewn spin-network amplitude.

## 2. Strict finite-block contraction is shared by both controls

**PROVED, Proposition 1.** Put `N=b+p`. For every finite beta>0,
T has a simple leading eigenvalue lambda>0 and a continuous strictly
positive eigenfunction psi, normalized by `integral psi^2=1`. The
same scalar lambda, chosen on the full space, satisfies

\[
 \left\|T|_{\mathcal H_-}/\lambda\right\|
 \le 1-e^{-4\beta N}<1.
 \tag{B5}
\]

This holds for SU(2), U(1), and Gamma. For the same slab repeated n
times its scalar is `lambda^n` and its charged norm is at most the
nth power of the right side. It is not a contraction that passes the
two comparison-group tests.

**PROVED — argument.** The continuous kernel (B3) obeys
`m<=T(U,V)<=M`, where `m=e^{-beta N}`, `M=e^{beta N}`. It is compact,
self-adjoint and positive. The spectral theorem supplies a top
eigenfunction. Replacing it by its absolute value cannot decrease its
Rayleigh quotient; strict positivity of the kernel makes equality
possible only for constant complex phase. The eigenvalue equation
then gives a strictly positive continuous eigenfunction. Two linearly
independent top eigenfunctions would have a linear combination changing
sign, contradicting that equality condition. This proves simplicity.
Gauge invariance and simplicity put psi in H and make it Theta-even.

Write `I=integral psi`. The eigenvalue equation and Rayleigh quotient
give `psi(U)<=MI/lambda` and `lambda>=m I^2`. The Doob kernel

\[
 (Pf)(U)=\frac{T(\psi f)(U)}{\lambda\psi(U)},\qquad
 d\pi=\psi^2dU
 \tag{B6}
\]

is reversible and Markov. Its density relative to pi is at least
`m lambda/(M^2 I^2)>=m^2/M^2=:epsilon`. Consequently
`P=epsilon Pi_pi+(1-epsilon)R`, with R a reversible Markov kernel.
Jensen's inequality gives `||R||_(L2(pi))<=1`. Theta-odd functions
have zero pi-mean. Multiplication by psi is a unitary map from
`L2(pi)` to `L2(dU)` and preserves charge. This proves (B5).

**ARGUED — what this rules out.** Fixed size alone cannot forbid every
common-scalar charged contraction: Proposition 1 gives such blocks.
It does not refute a no-go for (G22) with its required normalization
and sewing conditions. Nor does it answer the positive task: the same
construction contracts on both comparison groups. No degree-twelve
step enters its proof. The unresolved part is the stronger statement
including sewing, scalar cancellation and enough exposures. Neither
group blindness nor failure of this construction proves that every
possible fixed-block estimate fails those stronger requirements.

## 3. A free-boundary scalar can give expansion instead of contraction

**PROVED, Proposition 2 — an actual Wilson counterexample to one
normalization choice.** Take Q to be one three-dimensional cube:
`b=12`, `p=6`. Every spatial vertex is a boundary vertex, so
`P_int=1`. Use SU(2), the charge (B4) at a corner, and the exact scalar

\[
 Z_B=\langle1,T1\rangle.
 \tag{B7}
\]

This is the slab's free spatial-end integral, with its prescribed
temporal boundary. There are constants `c_B>0`, `beta_B<infinity`,
depending only on this cube, such that

\[
 \|T|_{\mathcal H_-}\|/Z_B\ge c_B\beta^{3/2}
       \qquad(\beta\ge\beta_B).
 \tag{B8}
\]

Thus (G22) is impossible for this block with this scalar at sufficiently
large finite beta. This is not a no-go for another scalar, another block,
or an estimate on a previously fixed compact coupling interval.

**PROVED — hand estimates.** Write `B_r={g:|g-1|<=r}` using the chord
metric on `S^3`. For `0<r<=1`, the coordinates
`g=(sqrt(1-|y|^2),y)` give

\[
 \frac{r^3}{4\pi}\le |B_r|\le\frac{4r^3}{3\pi}.
 \tag{B9}
\]

Indeed its y-radius is `r sqrt(1-r^2/4)`, between `sqrt(3)r/2` and r.
The normalized surface density there lies between `1/(2 pi^2)` and
`1/pi^2`. These inequalities imply (B9). Also, for beta>=1,

\[
 c_z e^\beta\beta^{-3/2}\le z_{SU(2)}(\beta)
 \le C_z e^\beta\beta^{-3/2},\quad
 c_z=\frac{e^{-1/2}}{4\pi},\quad C_z=\sqrt{2/\pi}.
 \tag{B10}
\]

The lower bound integrates over `B_(beta^(-1/2))`. For the upper
bound put `y=1-x` in the Haar integral. Its density is
`(2/pi)sqrt(y(2-y))<= (2 sqrt(2)/pi)sqrt(y)` on `[0,2]`.
Extend the exponential integral to `[0,infinity)` and use
`integral y^(1/2) exp(-beta y)dy=sqrt(pi)/(2 beta^(3/2))`.
In particular k_beta is bounded above and below by the corresponding
constants times `beta^(3/2) exp(-beta |g-1|^2/2)`.

Set `r=1/(8 sqrt(beta))`, `Omega=B_r^E` and
`f=1_Omega-1_(Theta Omega)`. The sets are disjoint. Hence f is an
actual charged vector and `||f||^2=2|Omega|`. Put `T_0=T/z_G^b`.
For `U,V in Omega`, each link difference has chord at most `2r`;
each plaquette holonomy has chord at most `4r`. Therefore

\[
 T_0(U,V)\ge c_1 e^{\beta p}\beta^{3b/2},\qquad
 c_1=C_z^{-b}\exp\{-(8p+2b)/64\}>0.
 \tag{B11}
\]

There are three links at the chosen corner. For
`U in Omega`, `V in Theta Omega`, their differences lie within `2r`
of `-I`. Their half-traces are at most `-1+2r^2`. On other links
use `x<=1`. Thus

\[
 T_0(U,V)\le c_2 e^{\beta p}\beta^{3b/2}e^{-6\beta},
 \qquad c_2=c_z^{-b}e^{6/64}.
 \tag{B12}
\]

Theta invariance makes the two diagonal integrals equal, and the two
cross integrals equal. Consequently the Rayleigh quotient of f is
at least `|Omega| beta^(3b/2)e^(beta p)(c_1-c_2 e^(-6beta))`.
By (B9), `|Omega| beta^(3b/2)>=(1/(2048 pi))^b`.
Choose `beta_B>=1` so that `c_2 exp(-6 beta_B)<=c_1/2`.
This proves `||T_0|H_-||>=c_3 e^(beta p)` with an explicit positive
constant c_3 defined by these expressions.

On the other hand, C and K are contractions and

\[
 Z_B/z_G^b=\langle A,KA\rangle
 \le\int A^2\le e^{\beta(p-1)}z_G
 \le C_z e^{\beta p}\beta^{-3/2}.
 \tag{B13}
\]

For the middle inequality retain one plaquette weight and bound the
other `p-1` weights by `e^beta`. Its holonomy is Haar when its links
are integrated. Divide the Rayleigh lower bound by (B13), giving
(B8) with `c_B=c_3/C_z`. No asymptotic expansion or numeric threshold
is needed. The same proof excludes normalization by `z_G^b integral A^2`.

**ARGUED — scalar meaning.** The scalar in (B7) is fully legitimate,
but it is too small for an all-boundary operator estimate in this
regime. The leading-eigenvalue scalar of Proposition 1 is different.
Calling either scalar “the vacuum factor” hides a consequential choice.
The original Wilson integral does not identify their repeated products.
This counterexample addresses that choice; it does not refute (G22)
with every allowable common reference.

## 4. A finite matrix plus a proved high-spin remainder

**PROVED — reduction on the actual boundary space.** There is an exact
way to retain the distinguishing high-spin decay without discarding
low-spin channels. Fix `I=[beta_-,beta_+]` with `0<beta_-<=beta_+`.
Let `sigma(beta)>0` be a specified common scalar for `T/z_G^b`,
continuous on I, with minimum `sigma_*>0`. It must later be matched
to the sewn integral; this subsection does not choose it after a
charged-sector normalization. Define

\[
 L_0=P_{\rm int}K^{1/2}A^2K^{1/2}P_{\rm int},\qquad
 M=L_0|_{\mathcal H_-}/\sigma.
 \tag{B14}
\]

With `X=A K^(1/2)P_int`, the two exact transfers are `T/z_G^b=XX*`
and `L_0=X*X` on H. X preserves charge, so their charged operator
norms agree. This uses the `XX*`, `X*X` identity, not an unbounded
inverse of convolution. It is the half-kernel cut used by Sussman
and Alpoge in (GL8).

Let `P_J` retain every link representation with `j_e<=J` inside H_-;
let `Q_J=1-P_J`. All boundary indices and intertwiner multiplicities
are retained. In an orthonormal spin-network basis of `P_J H_-`,
write `c_a=product_e r_(j_e(a))`. The finite matrix is exactly

\[
 (A_J)_{ab}=\frac{\sqrt{c_a c_b}}{\sigma}
       \int_{G^E}\overline{\phi_a(U)}\phi_b(U)
               e^{\beta\sum_{p\in P}x(U_p)}\,dU.
 \tag{B15}
\]

It is `P_J M P_J`. Thus even this finite matrix contains the entire
spatial Wilson exponential. No cutoff on its internal plaquette labels
has been taken. A signed state sum is not replaced by a positive gas.

**PROVED — a uniform remainder.** Put `t=beta_+/2`,

\[
 \eta_J=\sum_{n>2J}\frac{t^n}{(n+1)!},\qquad
 H_0=e^{\beta_+p}/\sigma_*,\qquad d_J=H_0\eta_J.
 \tag{B16}
\]

Then `eta_J -> 0`. Every link convolution has norm one, while on
`j>J` its norm is bounded by the corresponding term of this sum,
by the cited (GL4). Hence `||Q_J K Q_J||<=eta_J` and

\[
 D_J=Q_JMQ_J\ge0,\quad \|D_J\|\le d_J,
 \quad B_J=P_JMQ_J,\quad
 \|B_J\|^2\le \|A_J\|d_J.
 \tag{B17}
\]

The final inequality is Cauchy–Schwarz for the positive quadratic
form M. If `a_J=||A_J||`, the same inequality, applied to a vector
`u+v` in the two subspaces, gives

\[
 \langle u+v,M(u+v)\rangle
 \le(\sqrt{a_J}\|u\|+\sqrt{d_J}\|v\|)^2
 \le(a_J+d_J)(\|u\|^2+\|v\|^2).
 \tag{B18}
\]

Therefore the following genuinely finite-block supplier is sufficient:

\[
 \sup_{\beta\in I}\|A_J(\beta)\|+d_J\le q<1.
 \tag{B19}
\]

This proves `||T|H_-||/(z_G^b sigma)<=q` in the stated Haar boundary
norm. All scalar factors are displayed. For example, when
`m=2J+1` and `t/(m+2)<1`,
`eta_J <= t^m/((m+1)!(1-t/(m+2)))`; thus a desired remainder has
an explicit hand choice of J. No computation certifies (B19).

**PROVED — the weakest exact test at this split.** If `d_J<1`, the
exact criterion is strict positive definiteness of the finite matrix

\[
 I-A_J-B_J(I-D_J)^{-1}B_J^*.
 \tag{B20}
\]

Indeed complete the square in the quadratic form of `I-M` using
the positive invertible block `I-D_J`. Bounded triangular changes of
variables preserve a uniform positive lower bound. The low space is
finite-dimensional, so strict positivity there supplies such a bound.
Conversely `I-M>=epsilon I` implies strict positivity of this Schur
complement by minimizing over the high component. Thus (B20) is an
equivalence, not a claimed advance over the norm problem. The useful
one-sided hand test is (B19), whose low-spin matrix remains to be bounded.

**READ plus PROVED — the first unavailable step for the controls.**
The small bound in (B16) uses SU(2) spin, not merely center parity.
Let h be the Gamma-invariant vector in `Sym^12 V` from (G12).
For every k>=1, the nonzero polynomial `h^k` is invariant in
`Sym^(12k) V`. Its matrix coefficient on Gamma is the constant
function. Convolution fixes it. On the charged space
`V tensor span(h^k)` it has the fundamental eigenvalue, bounded
below on I by `beta_-/(4 exp(beta_+))`, as proved in (G16)–(G17a).
The SU(2) coefficients for that parent representation tend to zero
factorially. This contradicts transplanting the high-spin bound.
The first extra invariant is precisely degree twelve.

For U(1), `Sym^(12k)V` contains a zero-weight vector and its charged
tensor product with V contains weight one. The latter eigenvalue is
at least `beta_-/(2 exp(beta_+))`, again by the cited argument.
The corresponding bound fails there as well. In the *actual* Gamma
or U(1) boundary Hilbert space these coefficients belong to low
representations; they cannot be labelled orthogonal high-spin states
just because an SU(2) parent label was large.

**OPEN.** This is a named failure of one local estimate for both
controls. It is not yet a block estimate passing the binding tests.
Neither (B19) at an order-one interval with a usable scalar nor the
sewing estimate is proved. In particular the high-spin remainder
cannot repair `a_J>=1`: a compression is a lower bound on the full
operator norm. Proposition 2 prevents this scalar choice from working
uniformly at large beta even after taking J to infinity. Choosing the
Perron scalar instead recovers the shared contraction of Proposition 1.

## 5. Conditional normalization and the checked chord bound

**PROVED — the missing multipliers are explicit.** For a symmetric
positive Wilson block kernel T, put
`a(U)=integral T(U,V)dV`, `Z=integral a`, and

\[
 \mathcal M=a^{-1/2}Ta^{-1/2},\quad
 D=(a/Z)^{1/2},\quad T/Z=D\mathcal M D.
 \tag{B21}
\]

Multiplication and kernels are distinguished in this formula.
The Markov kernel `Qf=Tf/a` is reversible in `dnu=(a/Z)dU`.
The unitary map `f -> sqrt(a/Z) f` conjugates Q to Mcal. Its top
eigenvalue is one. All multipliers are Theta-even. If its charged
norm is q, the bound for the original scalar is only
`||T|H_-||/Z <= (max a/Z)q`. The multiplier is not optional.

For compatible blocks `T_i=Z_i D_i Mcal_i D_i`, exact sewing gives

\[
 \prod_{i=n}^{1}T_i
 =\Bigl(\prod_i Z_i\Bigr)D_n\mathcal M_n
   (D_nD_{n-1})\mathcal M_{n-1}\cdots
   (D_2D_1)\mathcal M_1D_1.
 \tag{B22}
\]

Thus products of q_i alone omit interface multipliers. One may bound
their norms, or use genuinely matched conditional measures from the
full exterior. Independent block marginals are not such measures.
Even this product bound still needs comparison with the *same*
untwisted exterior integral. It supplies no automatic vacuum cancellation.

**READ — the available full-lattice estimate.** `gap-vmf-lip.md`
Lemma DC and Lemma INF, lines 192–351, give chord influence row sum
`alpha=9 beta/2` for the four-dimensional Wilson law. The check
`gap-vmf-lip-check-opus.md` confirms these statements by a hand
reading, with no correction to their constants. For two fixed
exteriors of a finite block, the conditional kernels differ only
at its interior boundary layer D. If a test f is at influence-graph
distance ell from D, their normalized conditional means obey

\[
 |\mu_B^\eta(f)-\mu_B^{\eta'}(f)|
 \le\frac{2\Delta(f)\alpha^\ell}{1-\alpha},
 \qquad 0<\beta<2/9.
 \tag{B23}
\]

This is the checked lemma applied with the actual conditional laws.
It is a chord-Lipschitz estimate, not an `L^2` bound for all charged
boundary vectors, and retains each conditional partition function.
For a desired coefficient epsilon, this method permits

\[
 \ell\ge
 \max\left\{0,\left\lceil
 \frac{\log(2/(\epsilon(1-\alpha)))}{|\log\alpha|}
 \right\rceil\right\}.
 \tag{B24}
\]

It does not give a block length when alpha>=1. Replacing the bulk
majorant matrix C by `C^n` does not cure that defect: on the regular
bulk lattice `C1=alpha 1`, hence `C^n 1=alpha^n 1`. This is an
obstruction to that majorant, not a lower bound on actual influences.

**PROVED — an attempt on the single cube goes further locally, but
still loses the scalar.** For the cube of Proposition 2, Q in (B21)
has conditional density in V proportional to

\[
 \prod_{e\in E}w_\beta(U_eV_e^{-1})\,
       \exp\{\tfrac\beta2\sum_{p\in P}x(V_p)\}.
 \tag{B25}
\]

Each V-link meets two spatial plaquettes and six other V-links.
The checked single-site chord estimate gives influence `beta/8`
per such neighbour, and influence `beta/4` from its paired U-link.
Thus the internal V row sum is at most `3 beta/4`. The proof of
Lemma DC also allows a nonconstant discrepancy at D: replace its
diameter 2 in the telescoping step by the actual conditional distance.
For U and U' differing only on link j, this distance is
`(beta/4)|U_j-U'_j|` at j and zero elsewhere. Its same matrix series gives

\[
 \delta_j(Qf)\le\frac\beta4
    \sum_i\delta_i(f)(I-C_V)^{-1}_{ij},\qquad
 \Delta(Qf)\le \frac{\beta}{4-3\beta}\Delta(f).
 \tag{B26}
\]

This holds for beta<4/3; it contracts for beta<1. To transfer this
particular estimate to `L^2(nu)`, note that Q is compact and
self-adjoint there. Its kernel is smooth on the compact group
product. Every eigenfunction with nonzero eigenvalue is therefore
smooth and has finite Delta. A nonconstant eigenfunction with
eigenvalue t satisfies `|t|Delta(f)<=beta Delta(f)/(4-3beta)`.
Constants are the only functions with Delta zero. The charge is
odd, so constant eigenfunctions are absent. Applying this also to
real and imaginary parts proves

\[
 \|\mathcal M|_{\mathcal H_-}\|
 \le\frac{\beta}{4-3\beta}<1\quad(0<\beta<1).
 \tag{B27}
\]

This is a proved, fully resummed conditional cube estimate. To
return to its original scalar Z, (B21) still requires `max a/Z`.
For example `max a<=z_G^b e^(beta p)` and
`Z/z_G^b=<A,KA> >= (integral A)^2>=1`, using that K dominates
the projection onto constants, and Jensen's inequality.
The resulting sufficient factor is only
`e^(6beta) beta/(4-3beta)`. It exceeds one near beta=1. Thus this
attempt does not close the scalar estimate even where the normalized
conditional map contracts. No sharper bound on that multiplier has
been established here. Equation (B27) also makes no finite-group
exclusion; the named degree-twelve distinction remains in section 4.

## 6. What repeated exposures would have to prove

**READ.** The consumer is `gap-ext-astra.md:78–128`: on
`n=(a,a,c,d)`, `c,d in {a,2a}`, it keeps the original ratios
`R_m(v)=Z^(m+v)/Z^m`. The weaker (FQ) needs only the crossed-pair
deficits against the existing `S_ev>=eta_*^a` witness. An area bound
for those deficits is sufficient but stronger than necessary.

**PROVED — conditional composition, not an exposure construction.**
Suppose an exact defect expansion has been constructed with terms

\[
 \operatorname{Tr}(X_{\gamma,1}L_m\cdots
                   X_{\gamma,t}L_m),\qquad
 Z^m=\operatorname{Tr}L_m^t,
 \tag{B28}
\]

where `L_m>=0` is the same full Wilson transfer in every term.
The scalar factors, boundary identifications and multipliers of (B22)
must all be included in the X's or in the term's scalar coefficient.
Then Sussman–Alpoge (GL10), applied to the norm of each X, gives

\[
 \frac{|\operatorname{Tr}(X_{\gamma,1}L_m\cdots
                         X_{\gamma,t}L_m)|}{Z^m}
 \le\prod_j\|X_{\gamma,j}\|.
 \tag{B29}
\]

The positive-kernel assumption used in their further Gibbs-state
application is not needed for this absolute trace inequality. Thus
it also treats signed defect terms. Disjoint exposures in one layer
can be tensor products, so their norms multiply. For overlapping
exposures one must supply an actual factorization or a bound for
the intervening comparison maps; their count alone proves nothing.

For a concrete sufficient entropy budget, suppose that after all
nonwrapping decorations have been resummed, terms can be grouped by
a connected plaquette set gamma of area A containing a closed
mod-two surface with nontrivial twist pairing. Assume their
total absolute scalar coefficient is at most `h^A`, and their
operator product in (B29) is at most `q^(A/D-1)`, with `0<q<1`.
Here `h>0`, and `D>=1` is a fixed exposure-volume bound. Take h, D
and q uniform on I. These are hypotheses about the exact resummation,
not consequences of positive face coefficients.
A plaquette has at most twenty other plaquettes sharing a link in
four dimensions. Fixing a root, a canonical spanning-tree depth-first
walk of length `2(A-1)` encodes each connected set. There are at most
`20^(2(A-1))` such walks. The encoding determines the visited set,
so it bounds the number of sets. The already proved area lemma in
`gap-kappa-order.md` gives `A>=a^2` for a wrapping component.
Consequently, if

\[
 \rho=400h q^{1/D}<1,
 \tag{B30}
\]

absolute summation gives

\[
 |1-R_m(v)|\le
 \frac{N_p}{400q}\frac{\rho^{a^2}}{1-\rho}.
 \tag{B31}
\]

Any fixed twist multiplicity can be put in the coefficient budget
or in a fixed prefactor. Once the right side is at most one half,
`-log R_m(v)<=2(1-R_m(v))` for the admissible pairs with `R_m(v)<=1`.
Since `N_p=6a^2cd<=24a^4`, this supplies (V), and hence the required
large-a (FQ). The finitely many smaller a can be absorbed in its
prefactor, since the finite-volume ratios are positive and continuous
on I. Even a suitable exponential rate in a would suffice
for (FQ); no need to prove (B31) if that weaker budget can be met.

**OPEN — the exact missing exposure statement.** No expansion (B28)
with the stated coefficient and norm budgets has been constructed
for the original four-dimensional Wilson integral at order-one beta.
In particular, open temporal side data in (B3) must be restored and
sewn to all neighbouring blocks. Boundary gauge charge must become
the conserved center flux through a closed interface; a local charged
open line is not already that interface. One must cancel vacuum
decorations with the common `Z^m`, retain signs, and bound every
comparison multiplier. A packing argument only helps *after* those
charged insertions have been identified. Strictness in (B5) is far
weaker than (B30). This explains why it does not prove confinement
for the comparison groups.

## 7. Flat low-spin planes pay their own area

**READ plus PROVED consequence.** The exact term (G21), credited to
`gap-kappa-order.md` and `gap-tree-astra.md`, is
`2 r_(1/2)(beta)^A` in the untwisted-minus-twisted character expansion
after removing only the common one-plaquette vacuum factor. It has
no high-spin exposure. Partition its plaquettes among patches with
areas `A_1,...,A_s`, each face assigned once. The existing disc/torus
sewing calculation cancels the boundary dimension factors and leaves

\[
 r_{1/2}^{A_1}\cdots r_{1/2}^{A_s}=r_{1/2}^{A}.
 \tag{B32}
\]

This is exactly its area payment. Inserting a high-spin filter would
change the term. For a fixed compact I, continuity and strictness of
the normalized fundamental convolution give
`r_* = max_(beta in I) r_(1/2)(beta)<1`. Thus these individual terms
are uniformly area-small. In the stated aspect ratios there are at
most `4a^2` translated planes of each orientation. Even counting all
six orientations bounds their total by `48a^2 r_*^(a^2)` in that
one-plaquette-normalized expansion. This is not a bound for their
contribution divided by the full `Z^m`; that still needs the common
normalization in section 6. Branched low-spin surfaces and their
decorations are also not bounded by counting the flat planes.

**PROVED — the size growth that this particular payment requires.**
For this individual-plane payment on fixed I, patch area
`ceil(log(1/q_0)/(-log r_*))` suffices for a prescribed `0<q_0<1`.
It depends on I and q_0, not on the torus period a. If instead a
proposal demands a fixed `q_0<1` uniformly as beta tends to infinity
and pays an unbranched patch only by `r_(1/2)^A`, its area must grow
at least linearly in beta. Indeed `r_(1/2)=E_beta x` and, for
`y=1-x`, the law has density proportional to
`exp(-beta y)y^(1/2)sqrt(2-y)` on `[0,2]`. Relative to the gamma law
of shape 3/2 and rate beta it has the decreasing multiplier
`h(y)=sqrt((2-y)_+)`. For two independent gamma variables Y,Y',
`2 Cov(Y,h(Y))=E[(Y-Y')(h(Y)-h(Y'))]<=0`. Thus

\[
 1-r_{1/2}=E_\beta y\le\frac{3}{2\beta}.
 \tag{B33}
\]

The gamma mean on the right follows by one integration by parts.
For beta>=3, `-log(1-3/(2beta))<=3/beta`. If
`r_(1/2)^A<=q_0`, it follows that

\[
 A\ge\frac{\beta}{3}\log(1/q_0).
 \tag{B34}
\]

For a square patch of side ell this means
`ell>=sqrt(beta log(1/q_0)/3)`. This is a necessary growth law only
for this stated payment mechanism. It is not a no-go theorem for
resummed four-dimensional blocks with other scalar factors. It also
does not prescribe growth on the fixed interval requested in (G22).

## 8. Remaining obligation and delivery

**OPEN.** The requested group-selective, sewable (G22) is not proved,
and no theorem excludes all fixed-size realizations. The precise
analytic supplier left by this attempt is a bound such as (B19) on
the full low-spin matrix (B15), with its common scalar and boundary
comparisons paid so that the full exterior can be sewn. The other
missing supplier is the exact conserved-flux exposure representation
and summable coefficient budget of section 6. The degree-twelve
distinction controls the remainder; it does not supply either one.

**ARGUED — routes tested and next decision.** Perron normalization
gives an honest local contraction shared by both controls. The
free-boundary scalar gives the actual counterexample (B8). Conditional
normalization gives (B27), but (B21)–(B22) retain its unpaid cost.
The spin cutoff proves a small high-spin remainder but supplies no
contraction bound for the low-spin matrix. Increasing the number of putative filters
does not address that matrix. A further lane should either bound it
with a compatible exterior reference, or construct that reference
and flux interface first. Repeating the local filter calculation or
the finite-volume positivity argument supplies neither.

**READ — verification boundary.** Only this assigned note was written
in the checkout. The source files, registry, FINISH and scientific
status records were not edited. The mathematical arguments above are
by hand and have not been independently checked. No numerical or
computer-assisted proof step, external post, commit, or push was made.
The file remains local on `research/gap-block-astra-20261112`, based
on the requested pin. No conclusion of the checked strong-coupling
work was extended beyond its hypotheses.

RESULT: OPEN — constructed an exact resummed charged Wilson slab; proved shared Perron-normalized contraction, conditional cube contraction for beta<1, and a free-boundary-scalar obstruction growing as c_B beta^(3/2); reduced a usable SU(2) estimate to a low-spin matrix plus a controlled remainder whose parent-spin bound fails at degree twelve for Gamma and at weight one for U(1). The low-spin bound with sewable scalar costs and the conserved-flux exposure estimate remain open; no universal fixed-block no-go, order-one (FQ), or (V) is claimed.
