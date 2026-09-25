# Blind PRE: reference excitation energy versus the full charged input energy

This is the independent, pre-release answer to the bounded question dispatched
to `/root/rotor_upper_tail_check`. It is conditional mathematics of the four
admitted sources and their supplied quantum model. It is not an audit verdict,
a law-selection result, a preparation mechanism, or an energy-transfer claim.
No new author candidate or author runner was read or executed. The inherited
model and effort were retained, with no delegation.

The reference excitation energy is **not automatically the full input mean
increment**, even to leading finite order as the weak-field parameter tends
to zero. For the precise charged preparation, the increment is the reference
energy minus a positive semidefinite quadratic correction from the finitely
many changed electric and magnetic terms, up to an error tending to zero.
There is an analytic normalized one-excitation for
which the actual increment is negative. A low-frequency spectral restriction
does give a sufficient positive comparison; it does not follow from taking
the weak-field parameter small alone.

## 1. Sources, domain, and the compared objects

All source identities and frozen copies are in `SOURCE_PINS.json`. The three
parent science files are exact bytes of main
`0e6ad8285096ed668816f18caaa6fbbfbd9c50e8`:

| Source | SHA256 |
|---|---|
| Local pair form and general graph magnetic dynamics | `7c5bc10d0ca1127c2a1ef6f5cf9269caf6e8f023a09a061c2da0d8e033e35a7a` |
| Local compensation/common field-record limit | `c63db3296e5705c57693c2deb109e506f336fae4848d3ab0926d13a98929802b` |
| Weak-field wave packets | `651fa7cfd816ca5df8c401959458b7590c2f6ec706af437ef3ce31accb7d3ccf` |
| PR9143 preparation/calibration public note | `14ed0194fefd18eeee711e733bb76c75ce4a88832b01bc55dc41e6e058ba612b` |

The last source is frozen from the clean prepared-observation publication
checkout at `fb1991dfa6971e449513fb8e29884376739d21cc`. Its exact preparation
is an admitted provisional input. The applicable science workflow, reviewer
procedure, and instruction sources are also pinned. Complete earlier reads
of unchanged parents and procedures are reused where applicable; the needed
Hamiltonian, Gauss, weak-field, and preparation arguments were rechecked.

The prior independent 23/24 PRE, SHA
`3f9bae4b8de40697dce8ddd0d12382fd7b505156922ed8f713cc26de5e3a9a27`,
and its seal are explicitly known background. Its leading prepared mean
coefficients and elementary graph/hop conventions were known. The new finite
energy difference below was not imported from it. A new two-outward-hop Gram
calculation and a separate combinatorial compression derive the coefficients
needed here. The prior four-hop calculation is not executed or used as a
builder.

Take a fixed simple cubic torus of even side $L\geq6$, volume $V=L^3$,
with every edge stored from the even sublattice $A$ to the odd sublattice
$B$. These are the side restrictions of the supplied preparation. Side two
has repeated nearest neighbors, and side four has additional short winding
cycles; neither is included by silently reusing the coefficients below.
All matter states and rotor fields in the parent physical space are retained.

Let $C$ be the oriented elementary-plaquette curl matrix, and let

\[
\mathcal S=(\operatorname{im}\operatorname{div}^{*}\oplus\mathcal H)^{\perp},
\qquad \Omega=(C^{*}C|_{\mathcal S})^{1/2},
\qquad r=\dim\mathcal S=2(V-1),
\]

where $\mathcal H$ is the three-dimensional constant coordinate-link
space. A reference field has zero electric divergence and zero electric
winding. Its angle wavefunction is invariant along the gradient and harmonic
fibers. **Its harmonic-angle fiber is Haar distributed, not set to zero.**
The positive frequencies of $\Omega$ are

\[
\omega(k)=2\sqrt{\sum_{\mu=1}^{3}\sin^2(k_\mu/2)},\qquad k\ne0,
\]

with two transverse polarizations. Here $\omega$ is dimensionless; the
reference excitation energy is divided by the supplied time scale $\tau$.

Fix $\tau>0$, set $K=g^2/(2\tau)$, $\delta=1/(4\tau g^2)$, and use
the full parent rotor Hamiltonian

\[
h_g=K D+\delta H_4,\qquad
H_4=-2\sum_{\{x,y\}:N(x)\cap N(y)\ne\varnothing}S_{xy}^{*}S_{xy},
\quad S_{xy}=F_yF_xP.
\tag{1}
\]

In the stored orientation the electric multiplication operator is exactly

\[
D(q,E)=\sum_{(x,b),\,q_b=0} E_{xb}(E_{xb}-q_x).
\tag{2}
\]

Every $A$ site is occupied in $P$. The nonnegative self-adjoint
multiplication operator $D$ can have unconfined directions; its domain is
not replaced with a strictly elliptic domain. $H_4$ is bounded at fixed
graph, so $h_g$ is self-adjoint on $D(D)$.

Let $\psi_0$ be the oscillator vacuum of
$(p^2+x^{*}\Omega^2x)/(2\tau)$. For any fixed normalized
$f\in\mathcal S\otimes\mathbb C$, let $\psi_f=a^{*}(f)\psi_0$.
Use the parent's normalized compact weak-field preparations
$\phi_{0,g}$, $\phi_{f,g}$, with a fixed smooth local cutoff, under
the scaling $A=gx$. The compared physical inputs are

\[
\Psi_{0,g}=J_-\phi_{0,g},\qquad \Psi_{f,g}=J_-\phi_{f,g},\qquad
\Delta E_g(f)=\langle h_g\rangle_{\Psi_{f,g}}
                  -\langle h_g\rangle_{\Psi_{0,g}}.
\tag{3}
\]

The supplied reference excitation energy is
$E_{\rm ref}(f)=\langle f,\Omega f\rangle/\tau$. A particular supplied
packet is evaluated by inserting its $f$; the result is not a function of
reference energy alone across all $f$.

## 2. Exact physical preparation and electric compression

Use the coordinates, modulo $L$,

\[
a=(0,0,0),\ d=(1,1,0),\ h=(2,2,0),\ c=(1,0,0),\ e=(0,1,0),
\quad v_1=(0,-1,0),\ v_2=(0,0,1),\ v_3=(0,0,-1).
\]

All $A$ charges are plus except $d,h$, which are minus. The three $v_i$
carry plus records. In $m_c$, $c$ is plus and $e$ empty; in $m_e$,
$e$ is plus and $c$ empty. Every other $B$ site is empty. With the
source's fixed integer common flow $s_{\rm com}$,

\[
J_c\phi=|m_c\rangle U^{s_{\rm com}}U_{dc}^{-1}\phi,\qquad
J_e\phi=|m_e\rangle U^{s_{\rm com}}U_{de}^{-1}\phi,
\qquad J_-=(J_c-J_e)/\sqrt2.
\tag{4}
\]

The common flow has divergence $-1_d-2_h+1_{v_1}+1_{v_2}+1_{v_3}$.
Each branch separately obeys $\operatorname{div}E=q-1_A$; orthogonal
matter words make $J_-$ an isometry. This preparation retains its relative
minus sign, fixed strings, and original resolved/coherent birth operators.
There is no branch measurement or changed detector.
Here $1_{db}$ below denotes one unit on the stored edge $(d,b)$, not a
matter occupancy projector.

For branch $b=c,e$, write $s^{(b)}=s_{\rm com}-1_{db}$, and
$w^{(b)}_{xu}=1_{q_u^{(b)}=0}$. Equation (2), conjugated by its string,
gives on the smooth reference core

\[
J_-^{*}D J_-=\sum_j w_j E_j^2+\ell\cdot E+c_0,
\tag{5}
\]

\[
w_j=\tfrac12\sum_{b=c,e} w_j^{(b)},\quad
\ell_j=\tfrac12\sum_{b=c,e}w_j^{(b)}(2s_j^{(b)}-q_{A(j)}),\quad
c_0=\tfrac12\sum_{b=c,e}\sum_jw_j^{(b)}
          [(s_j^{(b)})^2-q_{A(j)}s_j^{(b)}].
\tag{6}
\]

There are no off-diagonal matter terms in $D$. Derivatives on the reference
subspace are projected to $\mathcal S$; this is how the Gauss and harmonic
constraints enter (5). It is false to replace this expression with
$\sum E_j^2$ in the charged sector. Let $W=\operatorname{diag}(w_j)$ and
$M=I-W$. Their exact weights are:

| Edges incident to | Number of edges | $w_j$ | $M_j$ |
|---|---:|---:|---:|
| $v_1,v_2,v_3$ | 18 | 0 | 1 |
| $c,e$ | 12 | $1/2$ | $1/2$ |
| All other $B$ sites | $3V-30$ | 1 | 0 |

Thus $\operatorname{tr}M=24$. For the explicitly recorded common-flow paths
in the independent controls, $c_0=10$; the two branch constants are 16 and
4. This number is a property of those chosen strings, not a universal
preparation energy. The constant cancels exactly from the normalized
comparison (3). The centered vacuum and one-excitation both have zero
momentum mean, even for complex $f$, by parity. Consequently the linear
term contributes only cutoff-tail error to their difference. No reset,
energy conservation assumption, or electric term is discarded in this step.

The smooth cutoff states, after a fixed finite string shift, belong to the
domain of every electric polynomial and in particular to $D(D)$. These
domain facts justify ordinary energy expectations directly; trace-norm
convergence of states would not by itself justify them.

## 3. Magnetic compression: a finite positive-cosine defect

In the empty-$B$, all-$A$-plus block the admitted pair theorem gives

\[
F_\emptyset(A)=c_G-4\sum_{p\in\mathcal P}\cos(c_p\cdot A),\qquad
c_G=-618|A|,
\quad F_\emptyset(0)=-642|A|.
\tag{7}
\]

Here $\mathcal P$ comprises the $3V$ elementary unoriented plaquettes,
and $c_p$ is their signed boundary. Define the charged compressed scalar
$F_J(A)=J_-^{*}H_4J_-$, evaluated on reference angle wavefunctions. This
is an expectation compression, **not** a claim that the range of $J_-$
is invariant under $H_4$. Equation (1) still includes all physical matter.

The exact result is

\[
F_J(A)=F_\emptyset(A)+R_L(A),
\qquad
R_L(A)=r_L+\sum_{u=1}^{70}\alpha_u\cos(k_u\cdot A),
\tag{8}
\]

with the following completely specified coefficient classes:

| Boundary class | Count | $\alpha_u$ |
|---|---:|---:|
| Other affected elementary plaquettes | 55 | 4 |
| Elementary plaquettes missing one branch's exchange | 11 | 2 |
| Central plaquette $a-c-d-e-a$ | 1 | 170 |
| Three six-edge boundaries, each a sum of two plaquette boundaries | 3 | 2 |

The constant is $r_6=4719$, and $r_L=4722$ for every even $L\geq8$.
Every $\alpha_u$ is positive and $\sum_u\alpha_u=418$. Complete integer
flows, edge endpoints, all coefficients, and an exact one- or two-plaquette
surface for each $k_u$ are in the Laurent and surface certificates. A
coordinate-free rule identifying the 67 plaquettes is the branch-eligibility
rule in the next paragraph, so the table is not a histogram without a
definition of its terms.

**Derivation of same-branch terms.** For a pair $x,y\in A$, an outward
hop moves $q_x$ to an empty $B$ neighbor and shifts that edge by $-q_x$.
The two-hop diagonal count in branch $b$ is

\[
n_x^{(b)}n_y^{(b)}-r_{xy}^{(b)},\quad
n_x^{(b)}=|N(x)\setminus O_b|,\quad
r_{xy}^{(b)}=|N(x)\cap N(y)\setminus O_b|,
\]

where $O_c=\{c,v_1,v_2,v_3\}$, $O_e=\{e,v_1,v_2,v_3\}$.
Two destination assignments interfere within a branch precisely when they
exchange two common empty neighbors and $q_x=q_y$. Thus for each elementary
plaquette the difference from (7) has cosine coefficient 2 times the number
of branches in which the two $B$ corners are not both empty or the two
$A$ charges differ. This gives 56 plaquettes of coefficient 4 and 11 of
coefficient 2 before the cross-branch term is added.

For completeness, the two occupied-$B$ sets block 43 and 44 plaquettes.
Exactly 22 plaquettes have opposite $A$ charges: the two negative $A$
sites each meet 12, and their shared plaquette is removed twice. Four blocked
plaquettes in either branch already have opposite $A$ charges. The missing
exchange sets therefore have sizes 61 and 62. Their intersection has size
56: 22 opposite-charge plaquettes plus 35 blocked in both branches, minus
their one common central plaquette. The resulting union has 67 elements.

Writing $m_x=|N(x)\cap O_b|$, the constant defect for a branch is

\[
\sum_{\{x,y\}}[6(m_x+m_y)-m_xm_y-|N(x)\cap N(y)\cap O_b|].
\tag{9}
\]

The first and last sums are 2592 and 60. For two distinct occupied $B$
vertices, the number of ordered choices of neighboring $A$ vertices whose
stars overlap is 20 at diagonal separation and 14 at axial separation two.
The axial value becomes 15 on $L=6$, due to a wrapped pair of $A$ sites.
The same-$B$ contribution to $\sum m_xm_y$ is 60. The $c$-branch has
five diagonal and one axial $B$ pairs; the $e$-branch has four diagonal
and two axial pairs. Hence their product sums are 174,168 for $L\geq8$,
and 175,170 for $L=6$. Equation (9) yields the stated constants. These
counts require only the six neighbor lists, and are checked independently
in `ELECTRIC_RESULTS.json`.

**Derivation of cross-branch terms.** A common output of $S_{xy}J_c$ and
$S_{xy}J_e$ must occupy both $c,e$ and one additional initially empty
vertex $t$. Filling $c$ or $e$ requires a plus $A$ source. If that
source is the same in both branches, it must be $a$: the other common
neighbor $d$ is negative. The other $A$ site $y$ can be any of the
18 sites whose stars overlap $a$; its destination must avoid
$c,e,v_1,v_2,v_3$. There are $18\cdot6-5\cdot5=83$ such paths.
Their common phases are the central Wilson character, and the minus sign
in $J_-$, combined with the $-2S^*S$ in (1), gives **plus** $166\cos$
of that character. Adding the previous coefficient 4 gives 170.

For distinct plus sources there are exactly three further matchings. Their
six-cycles, written as vertex loops, are

\[
a-c-d-e-(-1,1,0)-(-1,0,0)-a,
\]

\[
c-d-e-(0,1,s)-(1,1,s)-(1,0,s)-c,\qquad s=+1,-1.
\]

Each matching contributes its character and conjugate with coefficient 1,
hence $2\cos$. One verifies exhaustiveness by taking the possible plus
source in $N(e)\setminus\{d\}$, the one in
$N(c)\setminus\{d\}$, and their common destination $t$, excluding the
five occupied-or-exchanged vertices. These are local finite sets; no
long-range or empty-postbirth-sector assumption enters.

**Topology.** Every character in (8) is divergence free. The three displayed
six-cycles each bound two elementary plaquettes and have zero harmonic
signature, including at $L=6$. The other characters are plaquettes. Thus
Haar averaging on the harmonic fiber leaves this particular first-moment
polynomial unchanged. This conclusion follows from the complete terms, not
from a general permission to set harmonic angles to zero. The $L=6$
constant change in (9) is an overlap-graph effect. The previously observed
topological corrections to squared operators cannot be imported into this
first-moment calculation. For $L\geq8$, the finite neighbor patterns above
are unchanged: coordinate differences capable of generating a new wrapped
distance-two pair occur only at $L=6$ in this support. No growing-volume
weak-field estimate follows from that local coefficient observation.

The fiber average is taken after contracting the matter paths and both
strings. It is not independent dephasing of the two $J_-$ branches. Such a
dephasing would discard the cross term 166 and change the supplied input.

In particular, the common divergent mean coefficient is

\[
\mu_L=F_J(0)=-642|A|+r_L+418.
\tag{10}
\]

It equals $-64199$ at $L=6$ and $-159212$ at $L=8$, matching the
explicitly known prior PRE background by this new computation.

## 4. The finite input energy increment

The magnetic Hessian on the reference transverse space is

\[
H_J=4\Omega^2-\sum_u\alpha_u k_uk_u^*,
\tag{11}
\]

where all $k_u\in\mathcal S$. For the oscillator one-excitation, the excess
symmetrized coordinate and momentum covariances over vacuum are

\[
\Delta\langle xx^T\rangle
 =\operatorname{Re}(\Omega^{-1/2}ff^*\Omega^{-1/2}),\quad
\Delta\langle pp^T\rangle
 =\operatorname{Re}(\Omega^{1/2}ff^*\Omega^{1/2}).
\tag{12}
\]

They follow by applying the creation/annihilation relations once; in a single
real mode their diagonal entries are $1/\omega$ and $\omega$, fixing
the factors of two. The constant term $\mu_L/(4\tau g^2)$ is the same for
both normalized inputs. Equations (5), (11), and (12) therefore give

\[
\boxed{\quad
\Delta E_g(f)=\frac1\tau\left[
\langle f,\Omega f\rangle
-\frac12\|M^{1/2}\Omega^{1/2}f\|^2
-\frac18\sum_u\alpha_u|k_u^*\Omega^{-1/2}f|^2
\right]+O_L(g^2/\tau).
\quad}
\tag{13}
\]

Embedding $\mathcal S$ into the full edge space is understood in the term
containing $M$. All domain, projection, and string contributions have been
accounted for. The leading finite correction is negative semidefinite.
Equality with $E_{\rm ref}$ in the limit holds precisely when

\[
M^{1/2}\Omega^{1/2}f=0,
\qquad k_u^*\Omega^{-1/2}f=0\quad\hbox{for every }u.
\tag{14}
\]

There can be many such $f$: the combined defect has rank at most
$30+70=100<r$. Thus (13) does not assert a strictly negative correction
for every excitation, or negativity of every full increment. Reference
anharmonicity still prevents promoting (14) to exact finite-$g$ equality.

Here is a direct error justification, rather than an inference from norm
approximation alone. For an uncut reference Gaussian and a real character
vector $k$,

\[
\langle e^{igk\cdot x}\rangle_f-\langle e^{igk\cdot x}\rangle_0
=-\frac{g^2}{2}|k^*\Omega^{-1/2}f|^2
  \exp[-g^2 k^*\Omega^{-1}k/4].
\tag{15}
\]

The finite Laurent polynomial thus permits exact evaluation and termwise
expansion. If $F_J=\sum_k a_ke^{ik\cdot A}$, a uniform uncut error bound
for unit $f$ in (13) is

\[
\frac{g^2}{32\tau}\sum_{k\ne0}|a_k|(k^*\Omega^{-1}k)^2.
\tag{16}
\]

The electric quadratic contribution is exact before cutoff. The compact
cutoff, its derivatives, and the separate normalizations add a bound
$C_\chi g^{-m}e^{-c_\chi/g^2}/\tau$, for some fixed constants; multiplication
by the fixed strings preserves this estimate. The finite-dimensional vacuum
plus one-excitation family has uniform Gaussian polynomial tail bounds, so
(13) is uniform over normalized $f$ **at this fixed $L$**. Neither (16)
nor the cutoff constants is claimed uniform in volume.

Individually the two means are

\[
\frac{\mu_L}{4\tau g^2}
+\frac1{2\tau}\langle p^*Wp\rangle_n
+\frac1{8\tau}\langle x^*H_Jx\rangle_n+O_L(g^2/\tau),\quad n=0,f.
\tag{17}
\]

They are not low-energy preparations of the full Hamiltonian merely because
their reference excitation energy is small. In particular, the common
$g^{-2}$ preparation energy does not disappear from each mean when it
cancels in their difference.

## 5. An analytic counterexample to automatic energy identification

Let $c_p$ be the central plaquette boundary, and choose the legitimate
normalized one-particle mode

\[
f_p=\frac{\Omega^{1/2}c_p}{\sqrt{c_p^*\Omega c_p}}.
\tag{18}
\]

It lies in the zero-mode-removed reference space. The exact cubic incidence
counts are

\[
\|c_p\|^2=4,\qquad \|C c_p\|^2=28.
\]

The second identity counts its own curl overlap $4^2=16$ and twelve
adjacent plaquette overlaps of squared magnitude one. It remains valid for
all the allowed sides. Its reference energy is

\[
E_{\rm ref}(f_p)=\frac{28}{\tau\,c_p^*\Omega c_p}>0.
\]

The single central coefficient 170 in (13) already subtracts
$170\cdot16/(8\tau c_p^*\Omega c_p)=340/(\tau c_p^*\Omega c_p)$.
Every other subtraction is nonnegative. Hence

\[
\lim_{g\downarrow0}\Delta E_g(f_p)
\leq\frac{-312}{\tau c_p^*\Omega c_p}
=-\frac{78}{7} E_{\rm ref}(f_p)<0.
\tag{19}
\]

Equation (13) makes the increment negative also for all sufficiently small
positive $g$, with a threshold at fixed volume. This is an analytic witness,
not a sign inferred from a floating eigenvalue. It is consistent with the
full Hamiltonian: the prepared charged vacuum is not its ground state.

The independent floating Fourier controls give, at $L=8$,
$\tau E_{\rm ref}=2.6844494863572206$ and
$\tau\Delta E_0=-31.538145751842155$ for this witness. The analogous
$L=6$ values are $2.6844085537175566$ and
$-31.537677028495146$. These finite diagnostics corroborate (19); its proof
does not use those decimals.

## 6. A sufficient low-reference-frequency restriction

Let $P_\Lambda=1_{(0,\Lambda]}(\Omega)$ contain complete frequency shells,
and let $N_L(\Lambda)$ count the nonzero lattice momenta in that band
(two transverse polarizations each). Suppose $f=P_\Lambda f$. Set

\[
\eta_L(\Lambda)=\frac{133}{3}\frac{N_L(\Lambda)}{V}.
\tag{20}
\]

Then the exact limiting quadratic form in (13) obeys

\[
(1-\eta_L(\Lambda))E_{\rm ref}(f)
\leq\Delta E_0(f)\leq E_{\rm ref}(f).
\tag{21}
\]

This sufficient estimate is deliberately loose. To prove it, write
$r_f=\Omega^{1/2}f$. The loss relative to $\|r_f\|^2$ is the squared
norm of the stacked map with rows
$M^{1/2}/\sqrt2$ and
$\sqrt{\alpha_u/8}\,k_u^*\Omega^{-1}$, restricted to the band. Its squared operator norm
is at most its squared Hilbert--Schmidt norm. Translation and cubic symmetry
give

\[
(P_\Lambda)_{jj}=\frac{2N_L}{3V},\qquad
\|P_\Lambda\Omega^{-1}c_p\|^2=\frac{2N_L}{3V}.
\tag{22}
\]

The second identity also follows by summing over all $3V$ plaquettes and
using $\sum_pc_pc_p^*=\Omega^2$ on $\mathcal S$; symmetry makes all
summands equal. A sum of two plaquette boundaries has squared norm in (22)
at most four times the one-plaquette value. The exact coefficient table gives

\[
\sum_u\alpha_u(\text{number of plaquettes in the supplied surface})^2
=55\cdot4+11\cdot2+170+3\cdot2\cdot4=436.
\]

Thus the kinetic contribution is at most $8N_L/V$, and the magnetic
contribution at most $109N_L/(3V)$, proving (20)--(21). The proof supplies
a computable band criterion without importing a sharp spectral threshold.

This also proves variation at exactly equal reference energy. The lowest
shell has dimension 12. Its normalized vector proportional to $P_\Lambda c_p$
has relative loss at least $85/V$ from the central term alone, by (22).
The average relative loss over an orthonormal basis of that shell is at most
$\eta_L/12=133/(6V)$. Therefore some other normalized vector in the same
shell has relative loss at most $133/(6V)<85/V$. Both reference energies
are $\omega_{\min}/\tau$, but their limiting full increments differ.

When $\eta_L<1$, the actual increment is positive for every normalized
state in that band and all sufficiently small $g$; (16) and the nonzero
gap make the choice of $g$ uniform within the fixed finite band. For the
lowest shell $N_L=6$, $L\geq8$ is already sufficient. At $L=8$, (21)
gives the explicit lower factor $123/256$. At $L=6$ the same trace bound
exceeds one and is inconclusive. The floating lowest-shell minimum ratio
there is about 0.50845, but no interval or exact spectral certificate of that
sharper assertion is supplied here.

There is also an exact finite-volume criterion: the norm of the stacked
band map just used is less than one. The control computes it in rank at
most 100 as a diagnostic, without presenting those floating eigenvalues as
a uniform proof. The trace bound gives a rigorous simple sufficient choice.

Low *mean* reference energy and spectral support are distinct. If a tail
is admitted, define its fraction of reference energy by

\[
\theta=\frac{\langle f,\Omega(1-P_\Lambda)f\rangle}
                 {\langle f,\Omega f\rangle}.
\]

Using the same proof on the full nonzero spectrum with
$\eta_{\rm all}=133(V-1)/(3V)$, the relative loss is bounded by

\[
\left(\sqrt{\eta_L}\sqrt{1-\theta}
       +\sqrt{\eta_{\rm all}}\sqrt\theta\right)^2.
\tag{23}
\]

Thus a controlled small **energy tail** can replace exact band support. A
mean-energy hypothesis needs an additional argument to bound that tail. At
fixed $L$, for $m=\langle f,\Omega f\rangle$,
$\omega_{\min}=2\sin(\pi/L)$, and any $\Lambda>\omega_{\min}$, one
sufficient bound is

\[
\theta\leq
\min\left(1,\frac{2\sqrt3\,(m-\omega_{\min})}
                     {(\Lambda-\omega_{\min})m}\right).
\tag{24}
\]

It follows from bounding the probability above $\Lambda$ using the spectral
gap and then multiplying by $\omega_{\max}=2\sqrt3$. A mean close enough
to the fixed-volume gap, combined with a band for which $\eta_L<1$, can
therefore imply a positive comparison through (23). This is a sufficient
inequality, not an optimality or necessity claim. There is no normalized
one-excitation with reference energy tending to zero at fixed $L,\tau$:
the minimum is $\omega_{\min}/\tau$. Lowering $g$ leaves that fact and
the defect in (13) unchanged. No arbitrary simultaneous volume, packet,
scale, and microscopic-spin schedule is controlled by these statements.

## 7. Independent controls, failure preservation, and limits

Four scientific scripts were independently written for this PRE:

1. `magnetic_increment_control.py` builds the actual two-hop charge-word
   outputs and contracts their Gram matrices with exact integer Laurent
   arithmetic. It checks Gauss, Hermiticity, and all harmonic signatures,
   and derives the full empty and charged coefficients on $L=6,8$.
2. `combinatorial_formula_check.py` uses the diagonal destination counts,
   same-branch exchange eligibility, and cross-branch matching rule above.
   It compares every coefficient against the first control at $L=6,8$,
   separately evaluates $L=10$, and constructs exact surfaces for all 70
   defect characters. It uses no charge-word propagation.
3. `electric_and_coefficients_check.py` checks the electric polynomial
   against direct evaluation of (2) on four integer divergence-free reference
   fields per side, preserves the full strings, and checks the constant
   count decomposition including the special $L=6$ axial count.
4. `energy_form_control.py` builds its own transverse Fourier basis and
   verifies its Gauss, orthogonality, and curl-eigenvalue residuals. It checks
   the exact integers 4 and 28 in (19), evaluates the derived finite quadratic
   form and several bands, and evaluates (15) at four $g$'s. Those last rows
   are explicitly **uncut Gaussian comparisons**; compactification is
   justified analytically by the tail estimate, not falsely executed as a
   finite numerical torus integral.

The first control ran in about 1.82 seconds and the Fourier control in about
3.37 seconds. Full stdout/result files and complete stderr files are retained.
The results are source-bound; this is neither an author-run reuse nor a
canonical-publication execution. The previously known leading means served
as disclosed comparisons, not as inputs from which the new coefficients
were generated. The decisive counterexample uses the exact central
coefficient and incidence counts, while the positivity restriction has its
own analytic norm bound. More floating rows would not strengthen those
proofs.

One path-handling failure is retained: the combinatorial script was briefly
created one directory above the assigned output directory. Its first command
failed with file-not-found before executing science. That newly created file
was immediately moved into the assigned directory; no pre-existing source
was changed. `COMBINATORIAL_FIRST_PATH_FAILURE_STDERR.txt` and its empty
stdout preserve the failure. Subsequent execution succeeded. A preliminary
electric result was expanded with the $B$-pair count details and only that
small control rerun; it did not reverse an earlier scientific result.
Draft inline-math delimiters lost during string transport were also repaired
before sealing; the formatting receipt records the change. The displayed
equations were preserved, and the Hilbert--Schmidt comparison was phrased
explicitly as an inequality for the squared operator norm.

Two mathematical cautions were tested rather than assumed. Potential
harmonic winding in a six-link expression was a live concern; the complete
computed characters and their explicit surfaces show none for this first
compression. Conversely, the simple low-band trace bound fails to certify
the $L=6$ lowest shell although a floating diagnostic is positive; that
inconclusiveness is retained. Neither is recast as a general obstruction.

The full original resolved and coherent instruments remain those of the
parents, but no jump is performed in (3). These input means are not a heat,
photon absorption, output energy, or reservoir-work calculation. A negative
input difference is not spontaneous extraction of useful work, and a
positive restricted difference is not an absorption selection rule. The
result does not prove charged-sector packet propagation or stability of the
initial cancellation. The energy operator here is the full common rotor
$h_g$, not the bare microscopic Hamiltonian; unbounded-energy convergence
cannot be inferred from the parent's density convergence.

The order used is fixed graph, fixed supplied strings and time scale, the
parent rotor construction, then $g\downarrow0$ for these smooth inputs.
If a microscopic approximation is wanted, its spin limit must first be
justified at fixed $g,L$, with a separate moment argument for energy.
Neither the physical scale, a detector, an autonomous source, a thermodynamic
limit, nor a new framework premise is selected. All prior PRE/POST packets
remain unchanged. This PRE and its evidence are to be sealed before any
candidate release; work stops at that seal.
