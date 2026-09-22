# Independent reconstruction: homogeneous occupation penalty and charged rings

This is a blind bounded check of the supplied model. No new author homogeneous,
charged-potential, result, seal, checkpoint or registry was opened. The unchanged
independent normal-form and large-spin packets are reused at the identities in
Section 10. No publication or formal audit status is assigned.

**Result.** The model generates a positive electric-square term at second order
and a charge-transporting plaquette operator at fourth order. The latter is not
a pure-field plaquette term for arbitrary neutral charge contents. A finite-time
local comparison with a compact rotor **coupled to the occupied-sublattice
charges** can be justified uniformly in volume, with the explicit local dressing
and sufficient joint scaling in Section 6. A changed premise matters: the new
penalty permits first-order resonant hopping away from the code. I use the
larger full-space velocity `O(t)` and a correspondingly smaller birth rate.

The statements are conditional on the supplied Hamiltonian, tensor-product
hard-core statistics, gauge Hilbert space, checkerboard preparation, moment
condition and growing energy scales. They do not establish a thermodynamic
phase, a fixed-rate formation limit, bare-quench convergence or native closure.

## 1. Conventions and the actual low space

Let the periodic cubic graph have dimension `d>=2`, even periods at least six,
volume `V`, coordination `z=2d`, and `dV` positively oriented links. Let `A` be
one occupation checkerboard and `Bsub` the other. I write the supplied penalty
as `Bocc` to distinguish it from the sublattice:

\[
 B_{\rm occ}=\frac12\sum_{\langle xy\rangle}(n_x+n_y-1)^2
 =\sum_{\langle xy\rangle}n_xn_y-dN+\frac{dV}{2}.                 \tag{1}
\]

Every term is nonnegative. On a connected bipartite graph, `Bocc=0` requires
alternating occupation on every edge, hence exactly the two checkerboards.
Each has `N=V/2`. Their occupied contents can be arbitrary signs compatible with
the physical constraint `div E=q`. In particular the torus has total charge
zero, and the numbers of plus and minus records are both `V/4`. The assumptions
on the periods ensure this integer is available.

For a canonical edge `e=(x,y)`, charge `q=+1` or `-1` moving `x -> y` lowers
`E_e` by `q`. The reverse is the adjoint. Write

\[
 H=V_0(B_{\rm occ}+\epsilon T),\quad \epsilon=t/V_0,
 \quad T=-\sum_{e,q}(a^\dagger_{yq}U_e^{-q}a_{xq}+\mathrm{h.c.}),
 \quad C_S=S(S+1).                                               \tag{2}
\]

Here `V0>0`; the sufficient scaling below also takes `t>0`. The notation
`U^{-1}` in a single hop means the lowering **adjoint**, not an
inverse of a finite-spin partial shift. Local qutrit tensor factors give the
hard-core bosonic/permutation signs used below. An additional fermionic sign or
unrepresented record label would change the stipulated model.

Let `P` denote the selected `A`-occupied code inside the physical Hilbert space.
In the perturbative resolvent formulas one may include both zero-penalty
checkerboards; a word shorter than `V/2` hops cannot connect them. All orders used
below have that property on the stipulated tori.

Put

\[
 \alpha=2d-1.
\]

A first hop creates one vacant `A` site and one occupied `Bsub` site. The hopped
edge remains unlike-occupied, while the other `2d-1` edges at each endpoint
become equal-occupied. Its penalty is exactly `alpha`, independent of charges
and electric fields. Thus the physical one-hop gap is `alpha V0`.

For two distinct legal outward hops, their edges must have disjoint endpoints.
Write them as `(x,y)` and `(u,v)` with `x,u in A`. Let

\[
 w(e,f)=1_{x\sim v}+1_{u\sim y}\in\{0,1,2\}.
\]

If `X` is the set of `A` holes and `Y` the set of filled `Bsub` sites, with
`|X|=|Y|=r`, direct counting gives

\[
 B_{\rm occ}=2dr-e(X,Y).
\]

Consequently the two-hop energy is

\[
 b_{ef}=2\alpha-w(e,f).                                         \tag{3}
\]

When `w=2`, the edges are opposite sides of one elementary plaquette and the
energy is `2(alpha-1)`, not `2alpha`. The period restriction excludes winding
four-cycles being silently counted as elementary plaquettes.

## 2. Second order and Gauss cancellation

For an edge with occupied endpoint `x in A`, let `eta_e=+1` if `x` is the
canonical tail and `-1` if it is the head. Its outward squared matrix element
on the code is the diagonal operator

\[
 a_e=1-\frac{E_e^2-\eta_e q_xE_e}{C_S},\qquad 0\le a_e\le1.       \tag{4}
\]

This formula includes blocked finite-spin moves: it is zero at the relevant
endpoint. All `a_e` commute. The exact second-order block is

\[
 H^{(2)}=-\frac{t^2}{\alpha V_0}\sum_e a_e.                       \tag{5}
\]

The field/charge linear term does not have to be guessed or averaged. On the
physical code,

\[
 \sum_e\eta_e q_{x(e)}E_e
 =\sum_{x\in A}q_x\operatorname{div}E_x
 =\sum_{x\in A}q_x^2=\frac V2.                                  \tag{6}
\]

This is an operator identity and remains valid in entangled superpositions of
charges and fields. Therefore, with

\[
 K=\frac{t^2}{\alpha V_0 C_S}>0,
\]

\[
 H^{(2)}=K\sum_eE_e^2
 -\frac{dVt^2}{\alpha V_0}-\frac{KV}{2}.                         \tag{7}
\]

No bare electric-square term was inserted. Its origin is the nonunitary
finite-spin hopping amplitude; the two final terms in (7) are scalars.

## 3. Complete fourth-order block and its normalization

Here is the canonical Hermitian low-block convention. Let
`R=(1-P0) Bocc^(-1) (1-P0)`, where `P0` contains the zero-penalty sector.
Since `PTP=0` and the odd low coefficients vanish, the coefficient of
`t^4/V0^3` is

\[
 \mathsf H_4=-PTRTRTRTP
 +\tfrac12\{PTR^2TP,\,PTRTP\}.                                  \tag{8}
\]

The anticommutator is the normalization/folded term. For example, elimination
of the excited component gives a generalized low eigenproblem with metric
`I+epsilon^2 PTR^2TP`; conjugation by its inverse square root produces this
term. It cannot be replaced by counting only paths which avoid the code.

All first/last intermediate energies equal `alpha`. Thus

\[
 PTRTP=\alpha^{-1}\sum_ea_e,\quad
 PTR^2TP=\alpha^{-2}\sum_ea_e,
\]

and the folded term is `(sum a_e)^2/alpha^3`.

For every unordered pair of disjoint outward edges, there are four diagonal
irreducible histories: two outward orders and two return orders. Their sum is
`-4 a_e a_f/[alpha^2(2alpha-w)]`. Pairs sharing an endpoint cannot be the two
outward hops; they contribute only through the folded term. Combining these
facts gives the full diagonal coefficient

\[
 \mathcal L_S=\frac1{\alpha^3}\left[
 \sum_ea_e^2+2\sum_{\substack{e<f\\e\cap f\ne\varnothing}}a_ea_f
 -\sum_{\substack{e<f\\e\cap f=\varnothing\\w(e,f)>0}}
       \frac{2w(e,f)}{2\alpha-w(e,f)}a_ea_f\right].              \tag{9}
\]

The `w=0` disjoint pairs cancel exactly. The `w=1` terms do **not** cancel.
This finite-range diagonal correction includes more than plaquette pairs.

To specify the off-diagonal operator, orient a plaquette as
`x0 -> y1 -> x2 -> y3 -> x0`, where `x0,x2 in A`. Let `s_i` be the sign of
the traversal of its `i`th edge relative to the canonical orientation. Define
`R_(p,S)` on an initial charge pair `(q,r)` by

\[
 |q,r\rangle_A\otimes|E\rangle\longmapsto
 |r,q\rangle_A\otimes
 \left(\prod_{i=0}^1 U_{e_i}^{-s_iq}ight)
 \left(\prod_{i=2}^3 U_{e_i}^{-s_ir}\right)|E\rangle.             \tag{10}
\]

The charge projectors in (10) refer to the **input** pair; the swap follows
the conditional shifts. Its adjoint is the reverse circulation. Every factor
is one partial raising/lowering operation; all four edges are distinct.

There are four admissible orderings for a specified orientation, with
denominators `alpha, 2(alpha-1), alpha`. Hence the complete block is

\[
 H^{(4)}=\frac{t^4}{V_0^3}\mathcal L_S
 -J\sum_p(R_{p,S}+R_{p,S}^\dagger),\quad
J=\frac{2t^4}{V_0^3\alpha^2(\alpha-1)}>0.                       \tag{11}
\]

Equations (5) and (11) are exact perturbative coefficients, not an assertion
that a whole many-body low-energy spectral band remains isolated uniformly in
volume. The local remainder construction below supplies the dynamical control;
it does not require `epsilon V` to be small.

No other four-hop nontrivial low transition exists: before a return, the first
two hops must be disjoint outward moves. Crossed returns require both cross
edges and therefore one plaquette. This also proves that all transported
contents have been retained in (10).

Two useful distinctions follow.

- Equal charges give the usual two field-loop orientations (with a charge-
  dependent choice of which one is called forward).
- Opposite charges are **exchanged**. In that sector the two orientations in
  (10) give the same final charges, link shifts and amplitudes; equivalently
  `R_(p,S)=R_(p,S)^dagger` on that sector. Their amplitudes add. This is not a
  pair of independent classical probabilities and not an ordinary pure-field
  magnetic plaquette term.

In the unitary-shift limit, all `a_e=1`. The diagonal term becomes a scalar.
The exact counts on the full cubic torus are

\[
 M=dV,\quad M_{\rm meet}=dV\alpha,\quad
 M_2=dV(d-1),\quad M_1=dV[\alpha^2-2(d-1)].                       \tag{12}
\]

For the last identity, choose the cross edge of a length-three path: there are
`dV alpha^2` choices. A pair with two cross edges is counted twice, and there
are two opposite-edge pairs per elementary plaquette. Substitution in (9)
gives

\[
 \mathcal L_\infty=\ell_d V I,
 \qquad \ell_d=\frac{2d(\alpha^2-1)}{\alpha^3(2\alpha-1)}.         \tag{13}
\]

For example, `ell_2=32/135` and `ell_3=16/125`.

The finite-circuit normal form used below can have the same fourth-order block
as this canonical convention. Choose first-order edge generators from the
off-frequency hopping and solve each later homological equation with zero
zero-frequency part. For distinct edges,
`P S_(1,e) S_(1,f) P=0`: two distinct edge hops cannot restore occupation.
The projected second-order Baker-Campbell-Hausdorff correction from ordering
the edge gates consequently vanishes; the second-order generator itself is
off-frequency. Thus there is no second-order unitary rotation within the code
which would change (8) by a commutator with the nonconstant second-order block.
Alternatively, a different fixed circuit block convention must explicitly keep
that commutator. Its unitary-shift limit is unchanged because the unscaled
second-order block is then scalar. I use the zero-block-rotation convention.

## 4. The new resonances and the fast commuting penalty

The earlier onsite-penalty velocity estimate cannot be reused unchanged.
For a vacancy hop `x -> y`, directly from (1),

\[
 \Delta B_{\rm occ}
 =\sum_{z\sim y,\,z\ne x} n_z
  -\sum_{z\sim x,\,z\ne y}n_z.                                 \tag{14}
\]

This can vanish away from the code. The independent bulk checker exhibits a
physical neutral half-filled `6 x 6` state with `S=3`, a nonzero legal hop
`(0,0) -> (0,5)`, and `Bocc=18` both before and after. Its full charge and
electric words are saved. Therefore the first-order average `D1` of `T` with
respect to `Bocc` is generally nonzero in the full Hilbert space. It annihilates
the selected code, but the dual evolution used in a locality estimate cannot
be assumed to stay in the code after a local error source.

There is, however, no need to put the enormous `V0` itself into the propagation
speed. The penalty is a sum of mutually commuting, bounded, range-one terms.
For an operator supported on `X`, conjugation by `exp(i s Bocc)` involves only
penalty bonds meeting `X`: all other penalty terms commute with the operator
and with the retained terms. The support enlarges by at most one graph step,
and the norm is unchanged, for every `s`. This argument works for arbitrarily
large `V0 s`; it is not an expansion in that quantity.

Moreover (1) shows that `Bocc` has integer spectrum on these tori. For any local
operator, its Bohr-frequency pieces

\[
 A_\nu=\frac1{2\pi}\int_0^{2\pi}
       e^{isB_{\rm occ}}A e^{-isB_{\rm occ}}e^{-i\nu s}\,ds
\]

are still local after the one-step enlargement. All possible frequencies are
bounded by the occupation support size, independently of the link dimension.
The inverse on nonzero frequencies, `sum_(nu!=0) A_nu/nu`, has a support-size
dependent norm bound with no `S` or volume factor. For Hermitian `A` it is
anti-Hermitian and solves the required commutator equation.

The already checked finite-depth construction now applies with these changed
local averages. Recursively remove off-frequency coefficients through an order
`m`: split each local coefficient into its frequency-zero part `D_j` and its
off-frequency part; exponentiate the latter homological solution with parameter
`epsilon^j`, in a fixed coloring/order of its bounded-support gates. Subsequent
coefficients include the ordering commutators. The finite number of colors and
the gate norms depend on `d,m`, not on `S,V`. Taylor's formula for this finite
gate product gives

\[
 Y_m H Y_m^\dagger
 =V_0 B_{\rm occ}+V_0\sum_{j=1}^{m}\epsilon^jD_j+\mathcal R,
 \quad [D_j,B_{\rm occ}]=0,
 \quad \|\mathcal R\|_{\rm loc}\le C_m V_0\epsilon^{m+1}.         \tag{15}
\]

Each term and gate preserves Gauss, total record number and the separate plus
and minus counts. This is an explicit finite algorithm for the local dressing;
it is not a claim that it is autonomously produced by the given Hamiltonian.
At the order chosen below `m<V/2` on every stipulated torus. Hence the selected
checkerboard is invariant under the diagonal part of (15). Its first-order
coefficient is zero; its second and fourth are (5) and (11). Odd projected
coefficients vanish because every hop toggles the parity of `N_(Bsub)`. The
next code coefficient has local size `O(V0 epsilon^6)`.

After removing `V0 Bocc` by the commuting-penalty interaction picture, the
full-space local velocity is bounded by

\[
 v_\epsilon\le C_m(V_0\epsilon+\beta),                           \tag{16}
\]

including the resonant `D1`. Finite-support enlargement under the fast penalty
has only changed the constants and ranges. Applying an onsite interaction-
picture claim literally to (1), or using `O(V0 epsilon^2)` without addressing
`D1`, would leave a missing step. These are failed shortcuts, not failures of
the sufficient construction below.

## 5. Birth instruments and their full source bound

On a canonical empty edge let

\[
 V_{e,+}=a^\dagger_{x,+}U_e a^\dagger_{y,-},\qquad
 V_{e,-}=a^\dagger_{x,-}U_e^\dagger a^\dagger_{y,+}.
\]

I normalize the resolved choice as two jumps `sqrt(beta) V_(e,+/-)`, or the
coherent choice as one jump
`sqrt(beta)(V_(e,+)+exp(i phi_e)V_(e,-))`. Both give the same empty-edge loss,
although their recycling maps and general histories differ:

\[
 \Gamma_e=2\beta P_{00,e}\left(1-\frac{E_e^2}{C_S}\right).       \tag{17}
\]

Cross terms in `J^dagger J` vanish by orthogonality of the charge outputs. The
two coherent signs used as two simultaneous jumps without a `1/sqrt(2)` factor
would double (17); it changes constants, not the sufficient powers below.
The loss is not a scalar multiple of `P00` at finite spin. The Gauss commutators
vanish exactly, including at the partial-shift endpoints.

A bare birth annihilates the entire code because every edge has one occupied
endpoint. For a dimensionless jump `j_e` and its dressed version
`b_e=Y_m j_e Y_m^dagger`, locality of the finite circuit gives

\[
 \|b_eP\|\le C_m\epsilon,\qquad \|b_e\|\le\sqrt2.
\]

For any code density `sigma`, entangled or otherwise,

\[
 \|\mathcal D[b_e](\sigma)\|_1
 \le\|b_eP\|^2+\|b_e\|\|b_eP\|=O(\epsilon).                  \tag{18}
\]

The jump part alone is `O(epsilon^2)`, but the anticommutator need only be
`O(epsilon)`. Thus (18) includes no-event backaction and avoids an unjustified
replacement of the full dissipator by the event probability.

## 6. A sufficient joint scaling and local comparison theorem

Choose fixed `K,J,beta0>0` and integer `S -> infinity`. Set

\[
 \epsilon^2 C_S=\frac{J\alpha(\alpha-1)}{2K},\quad
 V_0=\frac{2K^2C_S^2}{J(\alpha-1)},\quad t=\epsilon V_0,
 \qquad \beta=\beta_0\epsilon^{3d},\qquad m=3d+6.                \tag{19}
\]

These choices reproduce exactly the `K` and `J` in (7),(11). In particular
`epsilon=O(S^-1)`, `V0=O(S^4)`, `t=O(S^3)`, and (16) is `O(epsilon^-3)`.
Both energy scales and the large link memory are supplied resources. Fixed
finite spin with `epsilon -> 0` cannot keep both coefficients positive and
finite: `J/K=2 epsilon^2 C_S/[alpha(alpha-1)]` tends to zero.

For each finite torus, let `sigma_(S,V)` be **any** physical code density
embedded in integer rotors, with the uniform bound

\[
 \sup_{S,V,e}\operatorname{Tr}\sigma_{S,V}(1+E_e^2)^2\le M_4<\infty.
                                                                    \tag{20}
\]

Correlations and charge-field entanglement are unrestricted. Prepare the actual
microscopic state as `Y_m^dagger sigma_(S,V) Y_m`. This dressing preserves
number and Gauss exactly and changes any fixed local bounded expectation by
`O(epsilon)`. It also preserves a uniform fourth-moment bound: each fixed-order
gate is generated by a bounded sum of words shifting a link by at most a fixed
integer, whose commutator with `(1+E^2)^2` has a uniform weighted bound; applying
that bound through the finite-depth gates gives a constant multiple of (20).

Let `mathsf R_p` be (10) with unitary rotor raising/lowering shifts. On the
selected occupation code the target is

\[
 H_{\rm ch.rot}=K\sum_eE_e^2
              -J\sum_p(\mathsf R_p+\mathsf R_p^\dagger),
 \quad \operatorname{div}E_x=q_x\ (x\in A),\quad
       \operatorname{div}E_y=0\ (y\in Bsub).                       \tag{21}
\]

The active code matter at each `A` site is its two charge states. Equation (21)
preserves the supplied Gauss constraints and charge counts. It moves those
charges by the two-step plaquette exchanges. It is not the zero-charge free
rotor and does not in general preserve a field-only winding number.

For every bounded fixed-support code field/charge observable `O_X`, use its
local occupation-preserving extension and spin compression in the microscopic
system. For fixed `T` and all sufficiently large `S`, the following sufficient
estimate holds:

\[
 \sup_{0\le s\le T}
 \left|\langle O_{X,S}\rangle_{{\rm micro},s}
       -\langle O_X\rangle_{{\rm ch.rot},s}\right|
 \le C_{X,T,d,K,J,\beta_0,M_4}\|O_X\|
       \left[\epsilon+\frac{(1+\log C_S)^d}{C_S}\right].         \tag{22}
\]

The right side is independent of the torus volume and of the charge/field
correlations. The reference in (22) uses the same embedded `sigma_(S,V)`;
there is no assertion that a global Fourier cutoff of an arbitrary infinite-
volume state has large probability. To identify a single limiting state, one
may additionally assume local convergence of these initial densities, or take
`S -> infinity` at each fixed finite volume first.

Here are the changed proof steps, rather than an inheritance by analogy.

**Microscopic to code normal form.** The verified finite-dimensional local
Lindblad bound applies to the interaction picture of (15): all interactions
have fixed range and bounded operator/superoperator norms, the new speed is
(16), and the dimension-independent norm proof has no factor growing with
`2S+1`. Gauge constraints are handled by restricting the dynamics on the
unconstrained local tensor product, where those estimates apply.

Use the closed normal-form code evolution as the forward reference and the
full microscopic Lindblad propagator as the backward observable evolution.
For a nearby Hamiltonian remainder use its local norm; for a nearby birth
source use (18). For distant terms use the locality exponential and clip at
the corresponding near bound. The count of terms in a radius-`r` ball is
bounded by `C_d(1+r)^d` on every rectangular torus. This gives, with constants
depending on `X,T,m`,

\[
 \mathrm{error}\le C\|O_X\|\big[
 \epsilon+V_0\epsilon^{m+1}(1+v_\epsilon T)^d
 +\beta\epsilon(1+v_\epsilon T+|\log\epsilon|)^d\big].          \tag{23}
\]

This comparison retains the entire birth generator; it does not condition on
no births in the volume. With (19), the remainder term is `O(epsilon^3)` and
the birth term `O(epsilon)`. The initial/observable dressing costs `O(epsilon)`.

**Code normal form to fourth order.** On the code `D1=0` and the odd
coefficients vanish. Gauss gives the exact onsite electric term in (7); the
remaining fourth-order interactions have bounded local norm independent of
`S`. The higher code terms have norm `O(V0 epsilon^6)=O(epsilon^2)` per local
term. Remove `K sum E^2` in an onsite interaction picture, then apply the same
bounded-interaction comparison with a bounded speed. It contributes
`O(epsilon^2)`. Removing the scalars in (7),(13) affects only phase.

**Finite spins to charged rotors.** Extend the finite-spin shifts to all
integer electric values by the positive-part factors, for example

\[
 U_S=\mathsf U\sqrt{[1-E(E+1)/C_S]_+}.
\]

The embedded spin subspace is invariant. For integer `E`, the relevant
quadratics `E(E+1)` and `E(E-1)` are nonnegative. Pointwise,
`1-sqrt([1-x]_+) <= x` for `x>=0`, giving the same weighted shift error as
in the checked large-spin proof. On a density with fourth moment at most `M`,
each local difference between `R_(p,S)` and `mathsf R_p` has Hilbert-Schmidt
source norm at most `C_d sqrt(M)/C_S`. The charge swap is unitary and the
charge controls commute with electric weights, so the telescoping estimate
survives unchanged. Similarly, `0<=a_e<=1` implies
`1-a_e a_f <= (1-a_e)+(1-a_f)`; (9) minus (13) obeys the same bound.

The electric part commutes with `F_e=(1+E_e^2)^2`. Each rotor plaquette changes
a participating electric value by exactly one, conditional on the charges.
The weighted commutator bound is uniform because

\[
 \frac13\le\frac{1+(m\pm1)^2}{1+m^2}\le3.
\]

There are `2(d-1)` incident plaquettes and two orientations. The prior weighted
calculation therefore gives, for example the conservative bound

\[
 \sup_e\langle F_e\rangle_s\le M_4 e^{24J(d-1)s}.                \tag{24}
\]

No product-state assumption is needed. A conditional charge swap does not
alter the electric weight ratio. The local Hamiltonian differences are also
uniformly bounded in operator norm, although not small in that norm. Near/far
clipping at their state-dependent `O(1/C_S)` bound with the now bounded
velocity yields `(1+log C_S)^d/C_S`, the second term in (22).

Finally, the rotor domain step is not assumed. At each finite torus,
`K sum E^2` is self-adjoint and the finite sum of charge-controlled unitary
plaquette operators is bounded. First truncate all rotor electric values at
`M>=S`. The dimension-independent locality and weighted estimates hold
uniformly in both cutoffs. In the common electric interaction picture the
truncated interactions converge strongly, are uniformly bounded, and their
Dyson series converge strongly on fixed times. Trace-class states and bounded
observables pass to the limit; electric moments pass by positive truncation.
This supplies (24) and (22) without an unverified infinite-dimensional locality
theorem or operator-norm convergence of partial shifts to unitary shifts.

These arguments prove the stated conditional local comparison. They do not
prove it for the bare undressed initial checkerboard. The new resonant motion
makes it especially inappropriate to replace global dressing by mere local
initial-state closeness and then assume that closeness remains uniform in time.

## 7. Finite-time density and resource interpretation

For the chosen normalization, `Gamma_e <= 2 beta`. Hopping conserves `N` and
each birth adds two records, so without conditioning,

\[
 0\le\frac{\mathbb E N(s)-V/2}{V}\le4d\beta s.                  \tag{25}
\]

The prepared state has exactly `N=V/2` because the dressing conserves number.
Local occupation observables, or the bounded individual penalty bonds, also
give from the first comparison step a defect-density bound `O(epsilon)` on
fixed times. Stronger initial quadratic estimates do not by themselves prove
stronger dynamical field convergence.

At each finite `S` the stipulated birth rate is positive, but it tends to zero
in this limit. Thus (21) has no finite nonzero formation source. The mean
record gain estimate is not a theorem about absorption, long-time completion
or a selected equilibrium. Resolved and coherent births need not agree in
their finite-rate histories merely because their loss agrees.

The occupation penalty is homogeneous; the selected occupation checkerboard
and its preparation are not derived from a growth law. The target keeps the
charged matter sector and the imposed Gauss Hilbert space. Scalar subtractions
in the effective Hamiltonian do not pay the diverging `V0,t`, eliminate external
birth resources, or establish energy conservation for the formation apparatus.

## 8. Decisive independent controls and countercontrols

All three scientific runners were written here without author imports and
passed their first executions. Full stdout, empty stderr and command receipts
are retained. No failed assertion was suppressed. The invalid shortcut using
the old full-space velocity is retained as the explicit resonant countercontrol.

`finite_sector_check.py` builds every physical link/charge state on a square
with its outside cubic occupation environment frozen. The internal energy is
computed from the original bond penalty, not from a supplied denominator.
It constructs the full hopping matrix, resolvent and folded term and compares
every second/fourth low matrix entry with (5),(9)-(11). This is a complete
finite physical sector, not the full torus. At `S=1`, equal-charge sectors have
dimension 13 and opposite-charge sectors 18; code dimensions are three and
four. The two-dimensional equal-charge low fourth matrix is

\[
 \begin{pmatrix}1/27&-1/9&0\\-1/9&10/27&-1/9\\0&-1/9&1/27\end{pmatrix}.
\]

From zero internal field, the opposite-charge swap has matrix element `-2/9`,
twice the equal-charge orientation's `-1/9`. In ambient `d=3` those entries are
`-1/25` and `-1/50`. These are coefficients of `t^4/V0^3`. The full saved
matrices also confirm that removing the folded term changes the answer.

`weighted_sector_check.py` reuses only that own helper to check the complete
`S=2` opposite-charge sector in `d=2` (dimension 42, code dimension eight), and
the equal-charge sector in `d=3` (dimension 25, code dimension five). This tests
nontrivial factors `sqrt(2/3)` and all associated diagonal coefficients, rather
than only spin-one factors zero or one. All matrix entries agree exactly.

`algebra_bulk_check.py` independently constructs the `6^2` and `6^3` tori.
It counts every unordered pair of edges, checks actual bond energies after
representative two-hop occupations for `w=0,1,2`, and verifies the scalar
coefficients (13) by exact rational arithmetic. In `d=2` the pair counts are
216 meeting, 504 with `w=1`, 72 with `w=2`; in `d=3` they are 3240, 13608 and
1296. Physical neutral charge/field words, including an added circulation,
verify the Gauss linear identity (6) and the second-order sum of actual hopping
weights. The saved resonant half-filled word verifies the changed locality
hypothesis directly inside the physical sector.

The same checker constructs the complete two-site matter/link operators for
`S=1,2,3`, verifies both endpoint Gauss commutators and the exact resolved versus
one-coherent-jump loss (17), and symbolically verifies the parameter identities
(19). No production simulation, cutoff eigenvalue fit, all-size modular rank,
or PASS count is used in place of the proofs above.

## 9. Limits and unresolved extensions

The sufficient schedule is not optimized. A different valid control of
resonant propagation might permit larger birth rates or a smaller normal-form
order. This report does not establish such an improvement, nor a bare-quench
theorem, growing observation times, fixed-beta rotor dynamics, unrestricted
states spread across the full spin band, or a joint thermodynamic phase limit.

In particular, forgetting the charge exchange in (10) changes the limiting
model. In a neutral finite torus the charges cannot all have one sign. The
construction supplies a compact charged rotor/matter Hamiltonian, not a proof
that the charged matter can be dropped or that the previous source-free wave
packet theorem applies to arbitrary states here. The latter would require
additional state and sector arguments.

## 10. Dependencies, evidence identities and read boundary

`SOURCE_READ_BOUNDARY.json` gives complete absolute paths and byte counts. The
seven allowed identities were authenticated before this reconstruction:

| Previously checked source | SHA-256 |
|---|---|
| large-spin independent `REPORT.md` | `072e1b6c833d023bec988126ca79379848718455122f7462db20db069a790732` |
| large-spin independent `COMPARISON.md` | `9051d24628563bc39fed4a8167b5cafe9fc052bc72bc3bbdc7f5f88cf3cdb7b9` |
| large-spin independent `FINAL_SEAL.json` | `7620bb6ff3b16ec319f12ad0d588d45a56f0fd084ed192b59e8c86d0f9ac30d4` |
| uniform-local independent `REPORT.md` | `4dc693c1b9cadd94ea95ce01108a72570482ad82c10c4b3f5f611169f749621e` |
| uniform-local independent `COMPARISON.md` | `00048adee9d46312bb197b590d3d2c709e209d7527cd44c2c7f9942a96feea1c` |
| uniform-local independent `FINAL_SEAL.json` | `cc213db7ba3b00cce3ae52d8206878219257bda27b831bfdad93129a9dbcafcf` |
| previously read Barthel-Kliesch 1111.4210v2 source | `abdeedde2be6d39e29f766e860d90e54783f9a384c3dbf1e75244769a07e84a7` |

The only external theorem input is the already checked finite-dimensional,
dimension-independent, time-dependent local Lindblad estimate from
[Barthel and Kliesch, arXiv:1111.4210v2](https://arxiv.org/html/1111.4210v2).
Its previous full hypothesis/proof review is reused by identity. The new
commuting-penalty support argument, resonant term, charged path algebra, and
rotor domain passage are explicit above. No new network lookup was needed.

The exact new scientific runner/output identities are:

| Runner / output | SHA-256 |
|---|---|
| `finite_sector_check.py` | `7043a2e8928a2957a862f63d50ec53e311eba4aeb2ccbe1ed992a3fad3cf33e1` |
| `FINITE_SECTOR_RESULTS.json` and stdout | `04cbc26658a336da15b2de755688a622f8cf89e73f64576ab3c5e7d763434f37` |
| `algebra_bulk_check.py` | `188716a15df7fe68b2d02f85ecdc82314977d49d586bf0e2c91747f15d7732c2` |
| `ALGEBRA_BULK_RESULTS.json` and stdout | `29b8f8dff91e7d212f7710755b4128bb3b7d4a85bee76586dd5618c554c84afb` |
| `weighted_sector_check.py` | `4eea0563eea08e530aa062840a4e02ad2410743a604858ecff0db01ad3e2aa90` |
| `WEIGHTED_SECTOR_RESULTS.json` and stdout | `45a5136ed9085dc902063cc7de04bbe2f17a9dfdc65e490c352e46331fb0c4e3` |

All source code and complete result fields were read. `run_control.py` retains
the full streams and a separate command/source/output receipt for each run.
The PRE seal binds this report, those controls, the neutral specification and
the source boundary before author comparison. All other evidence and primary
files remain unchanged.
