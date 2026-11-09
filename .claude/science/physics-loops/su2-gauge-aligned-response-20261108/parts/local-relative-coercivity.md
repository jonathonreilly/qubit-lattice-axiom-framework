# Small-collar stationary field and global relative energy coercivity

Research proof, 2026-11-08; the independent mathematical check and source
identities are in `../gates/relative-component-check.md`. This is a leading-energy
theorem, not formal retained status or a connected-response theorem.
Sources read: the supervisor pack's `compact-energy-coercivity.md`,
`flat-two-step-bound.md`, and `local-conditional-tail.md`, at
`/Users/jonreilly/.codex/worktrees/su2-two-block-response/Physics/.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/`.
Uses their exact finite two-step geometry and leading centered-gap energy.
No new network/literature search, numeric job, or Git mutation. The method
combines their compact coercivity with a uniform local inverse construction
and a compact perturbation lemma proved here. Inherited host model identifier
unavailable; worker launch effort medium. Only this deliverable is written.

## 1. Precise statement

Fix odd L>=3 and kappa>0, fine torus side N=L²m with m>=3, terminal V=I.
Use the translated terminal-root fine forest of the flat proof, with every
fine tree link fixed I and every intermediate link retained. A retained link
is owned by the terminal cell containing its tail; each cell owns
m_link=3L^8+1+4L^4 links. For a set R of terminal cells let J_R contain all
its owned links. Include each fine plaquette and each COMPLETE, output-
inclusive centered kernel gap that reads J_R, exactly as in local-tail §1.
Write their leading energy sum E_R(a,z). Exterior reader coordinates are
fixed to z; exterior coordinates unread by these factors are irrelevant.

There exist epsilon_*, C, alpha, c>0 depending only on L,kappa and the
fixed forest, not on R,N,u, such that the following holds. If every exterior
retained-coordinate reader has quaternion chord distance d(z_e,I)<=epsilon
with 0<=epsilon<=epsilon_*, there exists a stationary field a*(z) on J_R,
lying in a fixed small logarithm chart, with

    |log a*_e| <= C epsilon exp[-alpha dist(owner(e),R^c)].       (1)

The logarithm is exp(i x·sigma), and |log| means |x|. Distances are shortest
periodic terminal-cell graph distances. For R equal to the whole torus,
a*=I and the right side is understood as zero; empty R is trivial.
Stationarity is with respect to every retained coordinate in J_R. Moreover,
for EVERY q in SU(2)^(J_R), with componentwise multiplication a*_e q_e,

    E_R(a*q,z)-E_R(a*,z) >= c sum_(e in J_R)[1-w(q_e)].          (2)

No cap restriction is imposed on q. Thus a* is the unique global minimizer
of this leading local energy, although only local smoothness is needed
near a*. The assertion concerns the leading energy, not the full log density
with finite-u radial factors or Haar-coordinate density added.

## 2. Local geometry and uniform constants

For fixed L the factors belong to a finite family of translated templates.
Their arities, word lengths, coefficients, and number of factors reading a
coordinate have finite uniform bounds. Full input/output reader inclusion
is essential. Every pair of reader owners in one factor is at terminal-cell
graph distance at most r0=2. Plaquettes can touch diagonal cells, still at
distance two. Kernel footprints occupy their two endpoint blocks; at level
zero these blocks are nested inside neighboring terminal cells. Substituting
fixed tree identities creates no new reader or interaction range.

All factor functions are globally Lipschitz in their compact reader variables,
with uniform constants: unitary word products telescope, quaternion averaging
is linear, the Euclidean norm is 1-Lipschitz, and the output pairing is smooth.
No derivative of |M| at M=0 is used in this assertion. On a sufficiently
small uniform all-reader identity chart every path transporter is close to I,
so |M|>=1/2. There all factor functions are smooth with bounded derivatives
through order three, uniformly over templates. Fix one such chart radius
r_s>0. All constants below are maxima over this finite template family,
including occurrence multiplicities, and finite incidence sums. They are
existence constants, not numerical values.

At exterior I, unselected global factors have every reader equal to I and
vanish. Hence the complete global compact coercivity gives, for every q,

    E_R(q,I)=E_global(q extended by I)
             >= c_E sum_(e in J_R)[1-w(q_e)],                  (3)

with the uniform c_E>0 from compact-energy-coercivity. There is no witness
support loss: this is the global inequality applied to the extended field.

## 3. Uniform stationary construction, including boundary penetration

Use x_e in R³ with a_e=exp(i x_e·sigma), and use principal logs y_e for
the small exterior readers. For epsilon<=1, |y_e|<=2epsilon. Define
F_R(x;y)=E_R(exp(ix),exp(iy)). Near zero it is smooth. Its x-Hessian at
(0,0), denoted H_R, is the principal restriction of the global Hmin:

    <x,Hmin x>=||d0 x0||²+kappa||x1-Q0x0||²+kappa||Q1x1||².

This follows either by expanding |M|-<output,M>, or by removing the
nonnegative finite-u variance correction from the flat normalized Hessian.
No intermediate Wilson action is introduced. The flat proof supplies

    g I <= H_R <= M I,                                  (4)

with g>0 and finite M depending only on L,kappa. Principal restriction
preserves both bounds, even for disconnected or arbitrarily shaped R.
Its range is at most r0=2 in ambient terminal-cell distance.

For clarity choose M'>M, put rho=1-g/M' in (0,1), and choose
0<alpha<-(log rho)/2. The Neumann expansion using M' gives, for cell blocks,

    ||(H_R^-1)XY|| <= g^-1 rho^ceil(dist(X,Y)/2).

Cells absent from R are omitted. Each cell has at most 3m_link real
coordinates. The shell bound (2r+1)^4 gives the uniform weighted block-row
constant

    A_alpha = g^-1[1+sum_(r>=1)(2r+1)^4 e^(alpha r)rho^(r/2)]<infinity.

Let s_X=dist(X,R^c), w_X=exp(alpha s_X), and define
||x||_w=max_(X in R) w_X |x_X|, with Euclidean norm on the cell vector.
Because s_X is 1-Lipschitz, the inverse has operator norm <=A_alpha on
this weighted sup space. This does not require convexity or connectedness
of R.

Put f(y)=grad_x F_R(0;y). Factors whose readers are all interior have zero
gradient at identity. Every remaining contribution is supported in a cell
at distance <=r0 from R^c; smoothness and bounded incidence show

    ||f(y)||_w <= B epsilon                                  (5)

for a fixed B, including the factor exp(alpha r0). Write

    grad_x F_R(x;y)=f(y)+H_R x+N(x;y),       N(0;y)=0.

Local third-derivative bounds and incidence imply, whenever ||x||_infty,
||x'||_infty<=s and 2epsilon+s<r_s,

    ||N(x;y)-N(x';y)||_w
       <= K_alpha(s+epsilon)||x-x'||_w.                     (6)

Indeed the unweighted Hessian perturbation row sum is <=K(s+epsilon),
its range is <=r0, and the weight ratio along its nonzero entries is
<=exp(alpha r0). The Euclidean cell norm only changes K by a fixed
cell-dimension factor. These facts prove (6) uniformly in |R|.

Solve x=-H_R^-1[f(y)+N(x;y)]. On the closed weighted ball of radius
s=2A_alpha B epsilon, reduce epsilon_* until 2epsilon_*+s<r_s and
A_alpha K_alpha(s+epsilon_*)<=1/2 (strict inequality can be imposed).
Equations (5),(6) show this map preserves that ball and is a contraction.
The finite-dimensional Banach fixed-point argument produces x*, with
||x*||_w<=2A_alpha B epsilon, proving (1). It is the unique stationary
point in that contraction ball. The global uniqueness assertion follows
instead from (2), proved below. Full R has f=0 and x*=0 directly.
For each fixed R, the contraction iterations starting at zero are continuous
in the exterior principal logs and converge uniformly. Thus a*(z) is continuous,
in particular measurable, on the specified small-reader domain.

## 4. Compact perturbation lemma: nonsmooth means cause no gap

Here is the factor-level statement needed globally. Let h_f denote one
factor, including its coefficient 1 or kappa. Its variable readers are a
finite set S_f subset J_R, and its exterior readers have small values z.
Repeated occurrences are included in its formula, not treated as independent
coordinates. Define

    D_f(q)=h_f((a*_e q_e)_(e in S_f),z)
             -h_f((a*_e)_(e in S_f),z)-h_f(q,I).

All fixed tree links and terminal outputs remain I. Let
b(q)=Im quaternion(q) in R³ and let l_f,e be the derivative of D_f with
respect to x_e at q_e=exp(i x_e·sigma), all q=I. There is a uniform K_f,
bounded by one template constant K0, such that

    |D_f(q)-sum_(e in S_f) l_f,e·b(q_e)|
       <= K0 epsilon sum_(e in S_f) d(q_e,I)²               (7)

for all compact reader assignments q.

Proof. First D_f(I)=0, since h_f(I,I)=0. The stationary construction bounds
all a* reader distances by C epsilon; exterior readers satisfy epsilon.
Global Lipschitz continuity in these background parameters gives
|D_f(q)|<=K epsilon for all q. In the small all-q identity chart, uniform
third derivatives imply that the Hessian of D_f in q-log coordinates is
O(epsilon), and also |l_f,e|<=K epsilon. The latter conclusions follow by
integrating the parameter derivatives along small background logarithms;
|M| stays >=1/2 on this entire parameter/chart neighborhood. Taylor's formula
at q=I therefore gives

    |D_f(exp(ix))-sum_e l_f,e·x_e|<=K epsilon sum_e |x_e|².

Also b(exp(ix))=(sin |x|/|x|)x, so |x-b(exp(ix))|<=K|x|³;
log length and chord length are uniformly comparable in this fixed chart.
This proves (7) when every q reader is in a fixed chord cap of radius delta>0.

For the complement, at least one d(q_e,I)>=delta. The already proved global
bound |D_f(q)|<=K epsilon, the local derivative bound |l_f,e|<=K epsilon,
|b(q_e)|<=1, and bounded arity bound the left side by K'epsilon. Since
sum_e d(q_e,I)²>=delta², this is (7), after increasing K0 by delta^-2.
No global differentiation is performed. In particular the complement
argument covers M=0, antipodal q, and every singular locus of |M|. This
completes the two-regime proof.

## 5. Cancellation and absorption

Sum (7) over exactly the selected factors. For each interior coordinate e,

    sum_(f reading e) l_f,e
      = derivative_(q_e at I)[E_R(a*q,z)-E_R(a*,z)-E_R(q,I)] = 0.   (8)

The first derivative vanishes by stationarity of a*: the curve a*_e exp(itv)
is an admissible tangent variation, and the log chart has invertible tangent
map at a*. The last derivative vanishes because every baseline identity
factor has zero gradient. Thus left multiplication by a* is consistent
with the chosen global tangent proxy; no identification of unequal tangent
frames is assumed. Equation (8) kills the summed proxy terms exactly.

Bounded factor incidence converts (7) into

    |E_R(a*q,z)-E_R(a*,z)-E_R(q,I)|
       <= K_tot epsilon sum_(e in J_R) d(q_e,I)².

Since d(q,I)²=2[1-w(q)], combining with (3) proves (2) with
c=c_E/2 after additionally requiring epsilon_*<=c_E/(4K_tot).
The constants remain independent of R and volume. If q differs from I in
any retained coordinate, its right side is positive, proving uniqueness of
the global minimum. This is a global energy result despite the use of a
local stationary construction.

There is also a uniform quadratic cap upper bound. Reduce epsilon_* once
more so every a* and exterior reader remains strictly within the smooth
chart fixed in section 2. Choose rho_Q>0 small enough that d(q_e,I)<=rho_Q
keeps every interpolated a*_e exp(i t x_e dot sigma), 0<=t<=1, in that
chart, where q_e=exp(i x_e dot sigma). Bounded factor Hessians and incidence
give a uniform upper operator bound on the Hessian of
E_R(a* exp(ix),z). Its linear term at x=0 vanishes by stationarity. Taylor's
integral formula, and uniform comparison |x_e|<=C_log d(q_e,I), therefore give

    0<=E_R(a*q,z)-E_R(a*,z)<=C_Q sum_(e in J_R)d(q_e,I)^2       (9)

on this product chord cap, with C_Q and rho_Q independent of R and volume.
This is an energy bound on a cap; it does not condition the full law on it.

## 6. Exact-law boundary and recovery checkpoint

The actual conditional remains

    mu_R(da|z) proportional to exp[-u E_R(a,z)]
                           product_(c in C_R) H_u(|M_c(a,z)|) da,
    H_u(r)=exp(kappa u r)/Z(kappa u r).

The change a=a*q preserves product Haar; every one of these radial factors
must still be kept. Neither they nor their derivatives were included in the
stationarity claim. The proof grants a uniform small-collar leading-energy
minimizer, exponential penetration, and all-compact relative coercivity.
It does not alone grant a conditional tail with optimized prefactor,
collar occurrence probabilities, connected rough-sector summability,
full-law covariance decay, or any continuum conclusion.

Recovery: the load-bearing dependencies are global compact c_E, actual
leading Hmin gap g, bounded template incidence/range, and the local |M|>=1/2
chart. The only nonsmooth step uses global Lipschitz continuity, not a norm
Hessian at zero. No counterexample was found within the stated small-collar
hypotheses. Independent review should check the full-reader factor selection,
principal restriction, weighted contraction norm, and the cancellation (8).
