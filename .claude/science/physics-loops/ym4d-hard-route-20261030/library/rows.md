# ROWS: complex row bounds and the nonlinear DR input

Provenance: OpenAI Codex (GPT-6 family; exact serving variant and effort are not exposed), checkout `c0357c1fc52ab459bfe12daa62ca23336c85168a`, 2026-11-05. Research text, not an audit; grants no status. Source: Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text, revision `31a47c543775`.

## 1. Scope, sources, and early constants

This note supplies the local estimates and NL for **dr.md (4)**.
It uses the same admitted regular-pair envelope and geometry as frozen
[PW](pw.md). Its inputs remain P82 I1, I2, I4, I5, their matching
boundary spaces, the specified repaired walks, and parameter condition (P).
It does not supply DR's separate chain-domain admission or transport inputs.
The current is independent; it is never replaced by the action current.

There was no earlier rows.md in this checkout. The frozen DR note was
read whole. PW's Result, change log, coefficient proof, energy estimate,
walk estimate and parameter count were read. The checks below also use
nl-r9 §§3–6, P82 (17) and its proof, frozen CP12, and a3-derivative §§6–7
with its gate's curl and normalization repairs.

**Source record.** The outline-index README, relevant chunk rows with
neighbours, and obligations.md were consulted before the bounded reads.
The existing literature record lit-balaban.md was reused. The targeted
search was for straightened rows, PX141–PX154, Wilson Hessians, R9, and
multiplier blocks. SA and CA-I were fetched once each, at the pinned
revision, to /tmp/sa_ym4.tex and /tmp/sa_ca_I.tex. No run supplies a
mathematical step.

| Checked source | What this note uses |
|---|---|
| SA 10129–10161; index chunk 10 | Definition of the independent-current regular pair, local real gauges, raw rows, bilinear transposes, and defining Gram factors. |
| SA 10354–10410, 10562–10578; chunk 10 | The reduced expression defines the switched map. The NL estimate and the paired-current argument are sketched. In particular: “From then on only bounds are used”. |
| SA 11313–11347, 11375–11384; chunk 10 | The plaquette Hessian and its complex relative-form calculation are proved from insertion formulas. We use that calculation in a moving exponential chart and with local supremum norms. |
| SA 11508–11639; chunk 11 | The actual endpoint-corrected recursion, its summable raw radii, row density, and two-leg moment. The one-step and reference-radius arguments are partly sketched; the product and moment arguments are explicit conditional proofs. PW §4 supplies their library rebuild. The source warns: “Using two row sums would lose the fine density”. |
| SA 10548–10558; chunk 10 | Walk/tree assignment and payment for parameters; the outline sketches these. Frozen PW supplies the specific repaired implementation used here. |
| CA-I 49495–49547; CA index chunk 06, neighbouring supply rows | Application admission remains separate from the free-current operator theorem. No admission conclusion is inferred here. |

All borrowed constructions carry the Sussman–Alpoge authorship credit
above. Tadeusz Bałaban supplies the background and random-walk method.
This is a proof of the remaining steps in our specified reduction, not
a claim that the outline omits its own row calculation.

Use DR's \(X_w,F_w,Y_w\), and the pairings

\[
 \langle f,a\rangle_f=\eta^4\sum_b\tfrac12\operatorname{Tr}(f(b)a(b)),
 \qquad \langle u,v\rangle_Y=\sum_c\tfrac12\operatorname{Tr}(u_cv_c).
 \tag{1}
\]

Norms on colour are fixed finite-dimensional complex norms. Transposes
are bilinear. For a row carrier \(E_c\), write

\[
 a_c^*=m_c\sup_{E_c}|a|,\qquad
 n_E(a)=\max_{b\in E}\{m_b|a(b)|,m_b^2|\nabla_{\mathbf U}a(b)|\}.
 \tag{2}
\]

Every set includes its complete read stencil. P82 I5 and DR's
geometry give early constants \(G,N,D_0\ge1\): scales on a carrier
differ by at most \(G\); at most \(N\) carriers read one bond; and all
local carriers, plaquette reads and their stated adjacent stencils have
diameter at most \(D_0\). These constants depend on fixed \(L\), not depth.
Set **\(D_R=8(D_0+r_g+L+1)\)** now.

Here is the order for the other constants. Fix IN1 rows 1–2, including
Amendment 1's floor on odd \(L\). Work first on PW's larger provisional
complex envelope. Fix a one-step analytic radius \(\rho>0\) and a constant
\(A\ge1\) dominating the finite exponential, logarithm and mean estimates,
the reference-radius comparison, and the local Wilson estimates below.
They exist by the finite analytic arguments in §§2–4. Decreasing \(\rho\)
once incorporates every finite one-step coordinate count. All depend
only on the fixed early inputs.

In IN1 row 3 choose the final reference ceiling \(\epsilon_*>0\) and
\(r_R>0\) small enough that

\[
 16G r_R<\rho,\quad 16G\epsilon_*<\rho,\quad
 \exp\!\left(\frac{A(\epsilon_*+16G r_R)}{L-1}\right)<2,\quad
 A\eta|h|\le\tfrac14\quad(\|h\|_X\le4r_R).
 \tag{3}
\]

The last condition follows from \(\eta\le m_b\). Include the smaller
radii required in §2 in this same early choice. Use the smaller of
this reference ceiling and PW's. The larger provisional envelope is
retained for Cauchy estimates. Define **\(C_R\ge1\)** to dominate the
constants in (8), (9), (11), and (16), including \(G,N\), finite colour
factors and a local weight transfer of two. These uniform upper bounds
are proved below. They involve no later parameter or pair. Fix also
\(\gamma_*\le1\) below PW's current ceiling and DR's
\(c_\sharp-a_{\rm reg}\), with \(a_{\rm reg}<c_\sharp\).

DR leaves these early ceilings to be fixed. Equation (3) fixes them
once, on the entire resulting open envelope, independently of the
pair and of all later parameters.

PW's auxiliary inverse scales and rates precede the actual \(M_1,R_1\)
as specified there. Their floors, and these local constants, are all
chosen before \(\kappa\). Choose \(\kappa\) in the amended IN1 window.
Only afterwards choose \(\bar\kappa\), parameter length, source radii,
and \(M\), in that order. Later radii lie inside the fixed ceilings.
IN1 rows 6–10, including the final coupling decrease for admission,
do not redefine these constants. They are independent of \(M,\bar\kappa\).

## 2. Complex rows, including absolute derivatives

At every complex reference in the chosen envelope, on a fixed
*supremum* ball \(a_c^*<\rho\), PW §4 proves

\[
 \sum_b|K_a(c,b)|\le A m_c,\qquad
 |K_a(c,b)|\le A\eta^4m_c^{-3}.
 \tag{4}
\]

These are raw-row, counting-coordinate derivatives. This ball does not
require a small first difference of the additional increment \(a\).
The reference itself retains the regular-pair first-order hypothesis.

The argument uses both endpoint factors in SA PX141. The flat one-step
Jacobian is the length-\(L\) straight-segment average, with row and column
sums \(L,L^{-3}\). On a height-\(j\) carrier put \(t_i=L^{i-j}\).
In the reference frames, PW's first-exit argument bounds the reference
and increment radii at step \(i\) by \(A(\epsilon_*+a_c^*)t_i\).
Successive Jacobians and incremental frame changes have relative row
and column errors at most that quantity. Since
\(\sum_{i<j}t_i\le(L-1)^{-1}\), their products have bounds
\(A L^j,A L^{-3j}\). The initial physical factor is \(\eta\);
\(\eta L^{-3j}=\eta^4m_c^{-3}\) gives the density in (4).
Bare rows have \(q_c(a)=\eta a(c)\), so (4) is exact there.
Outward rows keep their prescribed endpoint convention and adjacent
carrier; no extra sum over heights is introduced.

**Absolute Taylor assertion.** There are early \(A_1,\rho_1>0\) such
that, uniformly at \(a_c^*\le4G r_R\), for every \(n\ge0\),

\[
\begin{split}
 \sum_{b_0,\ldots,b_n}
 |D_{b_1}\cdots D_{b_n}K_a(c,b_0)|
       &\le A_1 n!\rho_1^{-n}m_c^{n+1},\\
 \sup_{b_0}\sum_{b_1,\ldots,b_n}
 |D_{b_1}\cdots D_{b_n}K_a(c,b_0)|
       &\le A_1 n!\rho_1^{-n}\eta^4m_c^{n-3}.
\end{split} \tag{5}
\]

Fixed colour components are included at a fixed norm-equivalence cost.
One-variable Cauchy alone does **not** convert a general multilinear
operator norm into its full absolute coefficient sum. We instead use
the actual finite recursion.

At one step there are at most \(d_L\) input and output coordinates in
each dependency neighbourhood, with bounded incidence. Cauchy's formula
on a fixed finite polydisc bounds the absolute degree-\(k\) coefficient
sum by \(C_L^k\): there are at most \(d_L^k\) degree-\(k\)
multiindices. Keep the flat linear matrix separately. At a step whose
centre has radius \(\delta_i\le A(\epsilon_*+4G r_R)t_i\), an
increment of size \(z\) has positive majorant

\[
 L(1+A\delta_i)z+\frac{LAz^2}{1-Az}.
 \tag{6}
\]

The absolute derivative matrix, with one input marked, has row and
column bounds respectively

\[
 L\left(1+A\delta_i+\frac{2Az}{(1-Az)^2}\right),\qquad
 L^{-3}\left(1+A\delta_i+\frac{2Az}{(1-Az)^2}\right).
 \tag{7}
\]

For the column bound, sum the finite nonlinear coefficient majorant
over the bounded set of outputs reading that input. Absorb its factors,
including \(L^3\), into \(A\). The leading column term stays exactly
\(L^{-3}\). Work in colour-coordinate supremum norms at this calculation;
the flat matrix is scalar on colour. Thus fixed colour factors enter
the nonlinear coefficient bound, not once at every linear level.

Replace every fine increment coordinate by the positive variable
\(t_0s\). Recursively use (6), including all absolute Taylor coefficients.
For \(0\le s\le\rho_1\), a first-exit product estimate gives
\(z_i(s)\le2st_i\), after choosing \(\rho_1\) small at the early
stage (3). Multiply \(1+C_Lt_i(\epsilon_*+r_R+s)\); the logarithms
have a bounded geometric sum. This proves convergence of the positive
series as well as its bound. Apply (7) to the marked input along that
recursion. Its absolute derivative series has row sum at most
\(A_1m_c\) and column sum at most \(A_1\eta^4m_c^{-3}\) at
\(s=\rho_1\). Each nonnegative coefficient is bounded by this value
times \(\rho_1^{-n}\). Restoring physical input units gives (5).
The matrix chain rule and ordered incremental endpoint factors were
included before taking absolute values. Returning from the carrier gauge
and colour coordinates costs one fixed norm factor per external leg.
Its order dependence is absorbed by decreasing \(\rho_1\), not by a
factor at every level.

Let \(\mathcal C(a)=q(a)-K_0a\). Equation (5), integration from zero,
and the fine/counting transpose in (1) give

\[
\begin{split}
 m_b^3|(K_h-K_0)^{\mathsf T}\nu(b)|
   &\le C_R\widehat n_b(h)\max_{c\ni b}|\nu_c|,\\
 m_b^3|K_h^{\mathsf T}\nu(b)|
   &\le C_R\max_{c\ni b}|\nu_c|.
\end{split} \tag{8}
\]

Each transpose entry is \(\eta^{-4}K(c,b)^{\mathsf T}\).
The second line of (5) cancels \(\eta^4\); scale comparability and
the at-most-\(N\) carriers finish the estimate. The reads fit within
\(D_R\).

DR's dexp is \(E_h=\int_0^1\exp(it\eta\operatorname{ad}h)dt\).
Its series gives \(\|E_h-I\|\le e^{C\eta|h|}-1\le1/2\).
The Neumann series for \(R_h=(E_h^{\mathsf T})^{-1}\) gives

\[
 |R_h|\le2,\qquad |R_h-I|\le C_R\eta|h|
                                  \le C_R\widehat n_b(h).
 \tag{9}
\]

Its absolute derivative series converges on the larger ball.
Equations (8)–(9) prove **(Rows)** throughout the complex envelope.

Equation (5) also proves, with absolute coefficient majorants, for
\(\|a\|_X\le r\le r_R\),

\[
\begin{gathered}
 |\mathcal C(a)|_Y\le C_*r^2,\qquad
 \|\mathcal C'(a)\|_{X_w\to Y_w}
 +\|\mathcal C'(a)^{\mathsf T}\|_{Y_w\to F_w}\le C_*r,\\
 \|K_0\|_{X_w\to Y_w}+\|K_0^{\mathsf T}\|_{Y_w\to F_w}\le C_*,\\
 \|(\mathcal C''(a)[u,\cdot])^{\mathsf T}p\|_{F,w}
       \le C_*\|u\|_{X,w}|p|_Y,\\
 \|((\mathcal C''(a)-\mathcal C''(0))[u,\cdot])^{\mathsf T}p\|_{F,w}
       \le C_*r\|u\|_{X,w}|p|_Y.
 \tag{10}
\end{gathered}
\]

The last two lines also allow the weight on \(p\). Local weight transfer
costs at most two when \(\theta D_R\le\log2\). Fix \(C_*\) early,
also dominating the Wilson constants below.

## 3. A complex Wilson pairing bound

We prove a stronger bilinear version of **(Pair)**. For
\(\|a\|_X\le r_R\), and arbitrary test fields \(v,u\),

\[
 |F''(a)[v,u]|\le C_R\eta^4
 \left\{\sum_p|\nabla_{\mathbf U}v|_{E_p}m_p^{-2}n_{E_p}(u)
       +\sum_b|v(b)|m_b^{-3}n_{E_b}(u)\right\}.
 \tag{11}
\]

The first sum can equivalently sum all based first-difference slots
on the plaquette read. A fixed incidence factor converts the stencil
maximum to that sum. This is DR's permitted full-gradient version.
The stencils are fixed throughout.

**Proof.** Put \(V=e^{i\eta a}\mathbf U\). On an interior plaquette,
the product of its four exponentials gives

\[
 |P_V-I|\le C\eta^2m_p^{-2}
       (\epsilon_*+n_{E_p}(a)+n_{E_p}(a)^2).
 \tag{12}
\]

The linear oriented insertion sum is \(\eta^2d_{\mathbf U}a\),
up to the prefix-curl correction
\(\eta(1-\operatorname{Ad}P_{\mathbf U})\) times two transported
values. Terms with at least two insertions have bound
\(C\eta^2\sup|a|^2\) by the exponential series. The reference
plaquette has bound \(\epsilon_*\eta^2m_p^{-2}\).
Complex transports are bounded in the supplied real gauge;
no uncontrolled complex gauge is introduced.

For the exponential chart define \(v^a=E_av,\ u^a=E_au\).
The derivative of a link has these left generators. Its mixed
second logarithmic generator has size \(C\eta|v||u|\).
To verify this, differentiate
\(\log(e^{i\eta(a+tv+su)}e^{-i\eta a})\) twice and divide by
\(i\eta\); its fixed-ball analytic series has two insertion factors.
The generator is traceless. Its plaquette trace therefore vanishes
at \(P_V=I\), leaving a factor \(P_V-I\).

The other mixed terms are the sixteen ordered insertion terms.
At \(P_V=I\), cyclicity makes their trace the pairing of the
two insertion sums. Subtracting this value gives

\[
 \left|F_p''(a)[v,u]
  -\eta^4\langle\mathfrak d_Vv^a,\mathfrak d_Vu^a\rangle\right|
 \le C\eta^2|P_V-I|\sup_{E_p}|v|\sup_{E_p}|u|.
 \tag{13}
\]

This includes the mixed chart term. It is a direct complex calculation,
without a real-part operation or an action-current bound.

The integral for \(E_a\) gives \(|E_a|\le C\). Its transported
first difference has bound \(C\eta|\nabla_{\mathbf U}a|\).
Changing the covariant-difference link from \(\mathbf U\) to \(V\)
costs \(C|a|\sup|v|\). The prefix-curl correction is
\(\eta^{-1}(1-\operatorname{Ad}P_V)\) times two transported values,
as in SA PX117 and the a3 gate. Consequently

\[
 |\mathfrak d_Vv^a|\le C\left(|\nabla_{\mathbf U}v|_{E_p}
                                      +m_p^{-1}\sup_{E_p}|v|\right),
 \qquad |\mathfrak d_Vu^a|\le C m_p^{-2}n_{E_p}(u).
 \tag{14}
\]

For example, differencing \(E_a\) costs
\(C\eta|\nabla a||v|\le Cr_Rm_p^{-1}|v|\).
The reference and moved plaquette corrections obey the same bound
by (12) and \(\eta\le m_p\). Insert (12),(14) into (13), and
sum the fixed plaquette incidences to obtain (11).

At the action boundary the layer is bare, \(m=\eta\).
The direct bound \(C\eta^2|v||u|\) for each plaquette second
derivative equals the value term in (11). Thus missing plaquettes
cause no problem. Take \(a=th,u=h\) to obtain **(Pair)**. \(\square\)

The proof also supplies absolute local derivative majorants for the
paired expression. A first difference remains a first-difference slot
of \(X\); it is not bounded by \(\eta^{-1}|u|\).
The coefficients in (12)–(14) are finite analytic functions of the
scaled values and first differences on a fixed stencil. The identity

\[
 f(x)-f(y)=\int_0^1Df(y+t(x-y))(x-y)\,dt
 \tag{15}
\]

removes divided differences of analytic matrix functions, uniformly
for \(0<\eta/m\le1\). These formulas thus have extensions to
independent value/difference slots on a fixed analytic ball.
Finite-polydisc Cauchy bounds their absolute Taylor coefficients,
with the fixed stencil count absorbed into the radius as in (6).
The full-gradient column estimate in §5 applies term by term, also
after differentiating in \(a\). No uniform absolute second derivative
of a Green kernel is asserted.

## 4. The local nonlinear Wilson force

Put \(N_0(a)=F'(a)-F'(0)-F''(0)a\). We check nl-r9 §3.2 here,
since the paired estimate alone would not bound this force in \(F\).
Uniformly at our complex reference, for \(r\le r_R\),

\[
 \|N_0(a)\|_F\le C_*r^2,\qquad
 \|N_0'(a)u\|_{F,w}\le C_*r\|u\|_{X,w}
 \quad(\|a\|_X\le r).
 \tag{16}
\]

Both estimates have absolute local majorants in value/first-difference
slots. In particular they use no difference of the independent current.

**Proof.** Transport the four oriented insertions to the plaquette
base, and denote them by \(X_1,\ldots,X_4\), including their factors
\(i\eta\). For traceless complex two-by-two matrices,
\(X^2=\tfrac12\operatorname{Tr}(X^2)I\). Hence traces with a repeated
letter in degree three vanish. The remaining cubic coefficient is

\[
 \sum_{i<j<k}\operatorname{Tr}(X_iX_jX_k)
 =\tfrac12\operatorname{Tr}
       \left[(\textstyle\sum_iX_i)\sum_{i<j}[X_i,X_j]\right].
 \tag{17}
\]

For each ordered triple the three terms on the right have signs
\(+, -, +\), each with twice its ordered trace before the factor \(1/2\).
This proves (17). The insertion sum is \(i\eta^2\mathfrak d_{\mathbf U}a\).
The difference from the forward curl has the curvature factor already
used in §3.

We spell out the derivative that could otherwise lose a power of
\(\eta\). In a flat-corner notation let
\(v=a_\mu(x), w=a_\nu(x), u=\nabla_\mu a_\nu(x), t=\nabla_\nu a_\mu(x)\).
The oriented values are \(v,w+\eta u,-v-\eta t,-w\). Their six
commutators sum to

\[
 2[v,w]+2\eta[v,u]+2\eta[t,w]-\eta[v,t]
                         +\eta[w,u]-\eta^2[u,t].
 \tag{18}
\]

Differentiating the insertion sum in (17) puts a covariant difference
on the test variation. Transfer it to (18) by summation by parts.
For the leading term use the exact product rule for a covariant
difference of a commutator. It gives a sum of \(a\nabla a\) and
\(\eta(\nabla a)^2\) terms. Every other term in (18) already has
a factor \(\eta\). Its extra backward difference is bounded by
the two shifted values divided by \(\eta\), cancelling that factor.
Differentiating the other two insertions in (17) gives
\(C|a||\nabla a|\) directly. Covariant transports preserve the
product rule. Replacing the four prefix transports by this notation
adds terms with \(P_{\mathbf U}-I\); their bounds are included below.

The cubic terms containing \(P_{\mathbf U}-I\), after variation and
division by the fine volume, have bound
\(C\epsilon_*\eta m^{-2}|a|^2\). Terms of degree at least four
are bounded by \(C|a|^3\): at degree \(n\) the force coefficient
is \(C_n\eta^{n-4}|a|^{n-1}\), and its exponential majorant
converges on the fixed ball. Thus the complete interior force has
the absolute bound

\[
 C\left(|a||\nabla_{\mathbf U}a|
       +\eta|\nabla_{\mathbf U}a|^2+|a|^3
       +\epsilon_*\eta m^{-2}|a|^2\right).
 \tag{19}
\]

It is at most \(Cr^2m^{-3}\). An unpaired boundary plaquette has
the crude cubic force bound \(C\eta^{-1}|a|^2\). Its layer has
\(m=\eta\), which gives the same result.

All cancellations above are finite algebraic identities, performed
before taking absolute values. Formula (15) controls every analytic
divided difference; (19) is an absolutely convergent local series in
the normalized value and first-difference slots. Differentiate that
series with one leg \(u\). A quadratic term leaves one factor of
size \(r\); a higher term leaves at least two. The differentiated
geometric series converges on the larger ball. This proves the
second estimate in (16), with the weight on \(u\) and a fixed
stencil transfer. It also proves the asserted absolute majorant.
This checks the cubic identity, summation-by-parts step, and boundary
case of nl-r9 (3.4)–(3.7) on the complex envelope. \(\square\)

## 5. The counting multiplier and the column bound

The multiplier block is an output of PW's repaired energy expansion.
It is not obtained by inverting a switched lift.
Write \(Q=m^{-1}K_0\) in per-length row coordinates and
\(W_0=Q\mathsf GQ^{\mathsf T}\). The row measure in this convention
is \(m_c^4\). With the counting multiplier \(\zeta=m^3\nu\),

\[
 \langle QA,\nu\rangle_{m^4}=\langle K_0A,\zeta\rangle_Y,
 \qquad
 \Sigma=m^3W_0^{-1}m^{-1}.
 \tag{20}
\]

All diagonal factors have their displayed order. This agrees with
CP12 (2) for \(\mu=m^4,\ell=m\): the per-length multiplier is
\(m^{-3}\) times the counting multiplier.

Inject \(f_\nu=m^{-1}e_c\) into the last source slot of the
eight-variable system, with coefficient \(j=0\). Its energy dual
norm is \(|e_c|\); PW (6.2)'s represented-source norm is bounded
by an early multiple of this. Elimination gives

\[
 A=He_c,\qquad \nu=-W_0^{-1}m^{-1}e_c,\qquad
                         \zeta=-\Sigma e_c.
 \tag{21}
\]

The minus sign is the Schur-complement sign in the unfolded system.
The source norm follows directly from the pairing:
\(\sum_c m_c^4\nu_c(m_c^{-1}e_c)=\sum_c\zeta_ce_c\).
The output energy contains \(\|\zeta\|_{\ell^2(\mathrm{count})}\),
which bounds any one output coordinate. PW (6.3) contains the same
quantity in its local maximum norm. No factor \(m_c^{-4}\) is lost.

Let \(\Sigma_\omega\) be the normalized negative \(\nu\nu\) block
of the specified walk coefficient. Proposition 5 and (7.1) of PW,
applied to (21), give

\[
 |\Sigma_\omega(c',c)|\le A_E(A_E/M_1)^{|\omega|}
              e^{-(\tau/2)t_\omega(c',c)}.
 \tag{22}
\]

Here \(A_E,\tau>0\) are early, and \(t_\omega\) is the actual
connecting-tree length used to tag the full hull. This use of (7.1)
does not ask for an equation at switched parameters: each coefficient
is first estimated at its unswitched local inverse.

The same hull count as PW (8.2) gives

\[
 |s^\omega|\le e^{16\bar\kappa}
             e^{128\bar\kappa t_\omega/\ell_{\mathsf P}}.
 \tag{23}
\]

Retain PW's \(\ell_{\mathsf P}>8R_*\) and
\(\ell_{\mathsf P}\ge2048\bar\kappa/\tau\).
Thus switches cost at most \(\tau/16\) of the exponent.
A weight of rate at most \(\tau/16\) costs another \(\tau/16\).
Reserve \(\tau/8\) for the endpoint sum. The remaining positive
fraction pays the backward intermediate-pillar sums used in PW (7.1).
Their bound is P82 I4; each pillar carries boundedly many rows.
The repaired walk count is geometric. The already permitted early
increase of \(M_1\) makes its ratio at most \(1/2\). Summing
\(\sum_{n\ge0}2^{-n}=2\) proves

\[
 \sup_{c'}\sum_{c,\omega}
     |s^\omega|\,|\Sigma_\omega(c',c)|\frac{w(c')}{w(c)}
                         \le C_\Sigma e^{16\bar\kappa}.
 \tag{24}
\]

This is an absolute entry sum, uniform on the whole complex pair
envelope. Its constant includes the fixed endpoint and colour counts.
The diagonal mass in DR is unparameterized. Therefore the specified
\(M_s=\sum_\omega s^\omega\Sigma_\omega-a_0I\) satisfies

\[
 \|M_s\|_{Y_w\to Y_w}
 \le (C_\Sigma+a_0)e^{16\bar\kappa}.
 \tag{25}
\]

The estimate also holds for its absolute walk/diagonal majorant.
Normal convergence of holomorphic coefficients proves joint holomorphy.

For completeness, the needed column bound is also absolute.
For \(A_\omega=H_\omega(\cdot,c)e\), the energy part of (7.1)
controls \(\|m^{-1}A_\omega\|_{2,y}+\|\nabla_{\mathbf U}A_\omega\|_{2,y}\).
Cauchy–Schwarz on a pillar gives

\[
\begin{split}
 \eta^4\sum_{b\in y}m_b^{-3}|A_\omega(b)|
       &\le C\|m^{-1}A_\omega\|_{2,y},\\
 \eta^4\sum_{b\in y}m_b^{-2}|\nabla_{\mathbf U}A_\omega(b)|
       &\le C\|\nabla_{\mathbf U}A_\omega\|_{2,y}.
\end{split} \tag{26}
\]

The fixed factor is the square root of \(\eta^4\sum_{b\in y}m_b^{-4}\),
bounded by the pillar volume and finite component count. Complete
gradient stencils add only neighbouring pillars. Real/complex energy
norm comparison is part of PW's established local package. Multiply
by \(w(c)/w(y)\), use (23), and sum exactly as in (24). This gives

\[
 \sup_c\sum_\omega |s^\omega|\eta^4\sum_b\frac{w(c)}{w(b)}
 \left(m_b^{-3}|H_\omega(b,c)|
              +m_b^{-2}|\nabla_{\mathbf U}H_\omega(b,c)|\right)
                      \le C_H e^{16\bar\kappa}.
 \tag{27}
\]

In particular \(\|H(s)^{\mathsf T}\|_{F_w\to Y_w}\le C_He^{16\bar\kappa}\).
This proves the full-gradient column version needed with (11).
It uses a supported column's energy, rather than transposing a
field supremum estimate.

Enlarge the **early** \(b_0\) to dominate \(C_\Sigma+a_0,C_H\),
and PW's absolute field-output constants, and set

\[
 B=b_0e^{16\bar\kappa},\qquad
 \theta_*\le\min(\tau/16,\theta_{\rm PW},\log2/D_R).
 \tag{28}
\]

Equations (25), (27), and frozen PW give all three bounds in
**nl-r9 (4.2)**, with absolute majorants where used. The same
argument applies to a fixed positive diagonal row mass using its
early maximum in place of \(a_0\), if DR's stated variant is used.

## 6. Checking and applying nl-r9 to the specified maps

The notation in this section is DR's. All operators are held fixed
when differentiating in \(\alpha\). Put \(\mathcal C_2(a)=
\tfrac12\mathcal C''(0)[a,a]\). Choose early

\[
 0<r_0\le\min\{r_R/64,\,(2^{16}C_*^4)^{-1}\}.
 \tag{29}
\]

For \(\|\alpha\|_X\le R=4r_0/B\), the iteration

\[
 d\longmapsto\mathcal C(\alpha-Hd),\qquad |d|_Y\le4C_*R^2
 \tag{30}
\]

preserves the ball: its argument has norm at most \(2R\).
Its absolute Lipschitz majorant is at most \(2C_*BR\le1/4\).
Starting at zero, successive differences form a convergent geometric
series. On every smaller input ball the same argument, and uniqueness,
give \( |d|_Y\le4C_*\|\alpha\|_X^2\) and
\(\|h\|_X\le2\|\alpha\|_X\), where \(h=\alpha-Hd\).
Uniform convergence on smaller complex domains and the Cauchy integral
formula prove joint holomorphy in \(\alpha,s,A',\mathbf J\).

For \(\|\alpha\|_X\le r\le r_0/B\), set

\[
 A=\mathcal C'(h),\quad N=(I+AH)^{-1},\quad
 d'=NA,\quad Z=I-Hd'.
 \tag{31}
\]

Both \(N\) and \(N^{\mathsf T}\) have absolute Neumann sums at most
two. For the latter, the actual product is \(H^{\mathsf T}A^{\mathsf T}\);
(10) and (27) bound it on \(Y_w\). Implicit differentiation of (30)
gives, for two directions \(u,v\),

\[
 d''[u,v]=N\mathcal C''(h)[Zu,Zv],\qquad
 (d''[u,\cdot])^{\mathsf T}p
  =Z^{\mathsf T}(\mathcal C''(h)[Zu,\cdot])^{\mathsf T}N^{\mathsf T}p.
 \tag{32}
\]

These equations check the order of every transposed factor in
nl-r9 (5.3)–(5.4). They imply

\[
\begin{gathered}
 \|d'\|+\|d'{}^{\mathsf T}\|\le Cr,\qquad
 \|Z\|,\|Z^{\mathsf T}\|\le2,\\
 \|Z-I\|+\|Z^{\mathsf T}-I\|+\|N-I\|+\|N^{\mathsf T}-I\|\le CBr,\\
 \|(d''[u,\cdot])^{\mathsf T}p\|_{F,w}
                              \le C\|u\|_{X,w}|p|_Y.
 \tag{33}
\end{gathered}
\]

Domains and ranges are \(X_w,Y_w,F_w\) as in (10), (28), and
(31). To estimate \(d_3=d-\mathcal C_2\), subtract the value of
(32) at zero. Telescope in the order \(Z^{\mathsf T},Zu,\mathcal C''(h),
N^{\mathsf T}\). Their differences are bounded by \(CBr,CBr,Cr,CBr\).
The other factors stay bounded. Therefore

\[
 \|(d_3''[u,\cdot])^{\mathsf T}p\|_{F,w}
                       \le CBr\|u\|_{X,w}|p|_Y.
 \tag{34}
\]

These statements hold also with the weight on \(p\). They hold for
the corresponding absolute majorants, using (5) and the Neumann
series before any contractions of indices. At zero,
\(d'(0)=0,\ d''(0)=\mathcal C''(0)\). Thus the subtraction in
\(d_3\) removes exactly the linear current term in the derivative
of \(W_s\); vanishing of \(W_s(0)\) alone would not suffice.

Now use **exactly** DR (4):

\[
 W_s=-d_3'{}^{\mathsf T}p_s-K_0^{\mathsf T}M_sd
       -d'{}^{\mathsf T}M_sK_0\alpha
       +d'{}^{\mathsf T}M_sd+Z^{\mathsf T}N_0(h),
 \qquad p_s=H^{\mathsf T}\mathbf J.
 \tag{35}
\]

Differentiating gives the following eight terms:

\[
\begin{split}
 DW_su={}&-(d_3''[u,\cdot])^{\mathsf T}p_s-K_0^{\mathsf T}M_sd'u\\
 &-(d''[u,\cdot])^{\mathsf T}M_sK_0\alpha-d'{}^{\mathsf T}M_sK_0u\\
 &+(d''[u,\cdot])^{\mathsf T}M_sd+d'{}^{\mathsf T}M_sd'u\\
 &-(d''[u,\cdot])^{\mathsf T}H^{\mathsf T}N_0(h)
                         +Z^{\mathsf T}N_0'(h)Zu.
\end{split} \tag{36}
\]

Using (10), (16), (28), and (33)–(34), their bounds divided by
\(\|u\|_{X,w}\) are, in this order,

\[
 CB^2\gamma_*r,\quad CBr,\quad CBr,\quad CBr,\quad
 CBr^2,\quad CBr^2,\quad CBr^2,\quad Cr.
 \tag{37}
\]

For the first term use \(|p_s|_Y\le B\gamma_*\).
The third uses \(|M_sK_0\alpha|_Y\le CBr\).
The seventh uses \(|H^{\mathsf T}N_0(h)|_Y\le CBr^2\).
The other terms use the explicitly displayed small factors \(d'\),
\(d\), or \(N_0'\). This checks every term of nl-r9 (6.1)–(6.2).
There is no derivative of \(\mathbf J\), no \(\Delta H(s)\), and
no use of \(K_0H(s)=I\).

Since \(B\ge1,\gamma_*\le1,r\le1\), choose an early \(C_W\) so
the sum is at most \(C_WB^2r\|u\|_{X,w}\). Integrate on the
segment between two points of the unweighted \(r\)-ball. The segment
stays in that ball, with the weight only on its direction. Equation
(10) gives the constraint estimate in the same way. We obtain

\[
\boxed{\begin{split}
 \|W_s(a)-W_s(v)\|_{F,w}&\le C_WB^2r\|a-v\|_{X,w},\\
 \|\mathcal C(a)-\mathcal C(v)\|_{Y,w}
                              &\le C_Cr\|a-v\|_{X,w}.
\end{split}} \tag{38}
\]

Both maps vanish at zero, and \(DW_s(0)=0\) by (36).
This proves **NL for the stipulated maps**, not merely a
candidate continuation with the correct physical value.

## 7. Absolute majorants on common response balls

We specify what absolute means for the locality use in DR.
For a walk operator, sum the absolute norms of its *individual*
coefficients with their actual switch monomials. For a local map,
use its absolute Taylor/derivative coefficients after the finite
identities in §§2–4. For a force expression containing a difference,
use the value and covariant-difference slots that define \(X\).
This retains the actual stencil and its connection reads. It makes
no false assertion about a value-only norm for a differential operator.

PW (7.1), (7.4), (7.7), and its parameter argument bound the field
majorants of \(H,H_1,\mathfrak G\) by \(B\), after the early
enlargement of \(b_0\). Equations (24), (27) do the same for
\(M_s,H^{\mathsf T}\). Equations (5), (9), (10), (16), and (36)
provide the local derivative majorants. In particular all inverse
series in (31) and in the current formula are dominated by

\[
 \sum_{n\ge0}(C_*B\|h\|_X)^n.
 \tag{39}
\]

This is a bound on the expanded coefficient products, not just
the norm of their sum. Products retain repeated switch powers.
All bounds are uniform in the reference pair. The normal sums
are holomorphic in that pair; on smaller compact pair domains,
Cauchy applied term by term also permits any fixed finite number
of pair-direction derivatives. No derivative of the rough current
in a spatial direction is required.

To check the current's inhomogeneous term without a second-order
force estimate, write it as

\[
 H^{\mathsf T}(F'(h)-F'(0))
       =\int_0^1H^{\mathsf T}F''(th)h\,dt.
 \tag{40}
\]

Pair each individual column with (11), then use **both** sums in
(27). This gives an absolute bound \(CB\|h\|_{X,w}\).
The stronger version (11), with an arbitrary second argument,
also bounds its derivative in \(h\). Formula (15) gives its local
higher derivative majorants. Thus no unproved bound
\(\|F''(th)h\|_F\le C\|h\|_X\) is used in the current equation.
The independent anchor \(H^{\mathsf T}\mathbf J\) has bound
\(B\gamma_*\); the same Neumann series (39) treats it.

Choose DR's early \(c_*\) and \(\epsilon_D\) smaller if necessary.
With \(b_*=s_D\), its common balls are
\(\|\alpha\|_X\le2Bb_*\), \(\|h\|_X\le4Bb_*\).
Require

\[
 4Bb_*\le r_0/B,\qquad
 4C_*B^2b_*\le\tfrac14,\qquad
 2C_WB^4b_*\le\tfrac18.
 \tag{41}
\]

They follow from \(b_*=\epsilon_De^{-64\bar\kappa}\),
\(B=b_0e^{16\bar\kappa}\), by early choices
\(\epsilon_D\le r_0/(4b_0^2)\),
\(\epsilon_D\le(16C_*b_0^2)^{-1}\), and
\(\epsilon_D\le(16C_Wb_0^4)^{-1}\).
These are compatible with DR (9). The inner, outer, and multiplier
Neumann/iteration series now converge with the displayed absolute
majorants on common balls for every pair and switch in use.
This supplies the analytic-majorant input called ABS in DR.
It does not supply LIFT or equality of coefficients from separately
constructed regional problems.

## 8. Round conclusion and limits

This round closes both requested analytic inputs under the already
declared regular-envelope and frozen PW hypotheses. Three possible
losses were checked in the proof: the row transpose's \(\eta^{-4}\),
the Wilson cubic force's apparent \(\eta^{-1}\), and the multiplier's
physical row weight. They cancel respectively by the column density,
the cubic curl identity with the bare-boundary case, and the exact
conversion \(\zeta=m^3\nu\). Thus none leaves an open lemma here.

Only library/rows.md is changed. The statements are proved by Codex,
not yet checked by the other model. Frozen notes and their hypotheses
remain unchanged. Source retrieval, text searches and file checks are
bookkeeping, not computer-assisted proof.

## Result

**Proof**

For every complex pair in the admitted DR/PW regular-pair envelope,
with its matching geometry, branches, repaired walk specification,
frozen P82 inputs and parameter partition (P), **(Rows)** and the
full-gradient version of **(Pair)** hold with early \(C_R,r_R,D_R\).
The counting multiplier satisfies
\(\|M_s\|_{Y_w\to Y_w}\le B=b_0e^{16\bar\kappa}\), after an early
enlargement of \(b_0\). The accompanying absolute column and local
derivative majorants give nl-r9 (4.2), **NL for exactly dr.md (4)**,
and DR's ABS on the common solution balls.

All constants precede \(\kappa\) in amended IN1 order and are
independent of \(M,\bar\kappa\), mesh, depth and volume. The permitted
dependence on \(\bar\kappa\) is the displayed \(B\), the parameter
length floor, and the later solution/source radii. The separate
admission and transport obligations in DR remain. This result grants
no audit or scientific status.
