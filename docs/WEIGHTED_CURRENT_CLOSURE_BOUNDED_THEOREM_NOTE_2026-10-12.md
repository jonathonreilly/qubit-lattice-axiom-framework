---
claim_id: "weighted_current_closure_bounded_theorem_note_2026-10-12"
claim_type: "bounded_theorem"
claim_scope: "For a specified finite-range full-matrix spin density under exact energy-current conservation, first translation moments reduce the weighted current/boost bracket to an unweighted density. A complete finite site test is equivalent to beta-energy closure; supplied actual local-vector operators give the separate common-domain corollary. The fixed XX density fails for every real beta; no broader no-go or physical model is established."
upstream_dependencies:
  - microscopic_current_implementation_bounded_theorem_note_2026-10-12
  - microscopic_joint_flow_bounded_theorem_note_2026-10-12
runner: "scripts/weighted_current_closure_2026_10_12.py"
actual_current_surface_status: "conditional-support"
target_claim_type: "bounded_theorem"
trace_class: "upstream_support"
target_claim_id: null
target_blocker_text: "Test the full criterion on a specified intended density; separately construct actual self-adjoint operators and justify any global integration."
source_of_blocker_text: "handoff"
reachability_to_target: "partially_closes"
artifact_role: "theorem"
next_trace_action: "Test the full criterion on a specified intended density; separately construct actual self-adjoint operators and justify any global integration."
conditional_surface_status: "Finite local weighted-current closure criterion under exact conservation"
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "The specified density, conservation and optional self-adjoint local-vector actions remain supplied. Fixed-XX failure does not quantify over density improvements or other interactions."
audit_required_before_effective_retained: true
bare_retained_allowed: false
---

**Type:** bounded_theorem


# A finite local test for weighted current–boost closure

**Conditional bounded theorem, 2026-10-12; separate complete source review requires no mathematical correction.** Root supplied the
candidate coefficient-moment mechanism and is a contributor. This note proves
a conditional local-algebra reduction. It neither establishes conservation in
the intended model nor constructs physical self-adjoint boosts or a Poincaré
representation.

Under exact energy-current conservation, the weighted commutator has a finite
unweighted density. Its coefficients are negative first translation moments
of the local commutator density. A complete one-site matrix basis then gives a
necessary and sufficient finite criterion for its equality to beta times the
energy derivation. The conserving XX chain provides a concrete application:
its result contains an additional four-site word and fails that equality for
every scalar beta at the fixed density used below.

## 1. Inputs, provenance and claim boundary

S denotes the original research collection. The [frozen milestone handoff](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/16a69597714f8c62387c2e9ee92c445c40f91410/.claude/science/physics-loops/toe-boost-gap-fock-closure-20261012/HANDOFF.md) and [evidence map](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/16a69597714f8c62387c2e9ee92c445c40f91410/.claude/science/physics-loops/toe-boost-gap-fock-closure-20261012/EVIDENCE_MAP.json) preserve the original source bundles and complete own evidence. The direct in-branch proof dependencies are [Current](MICROSCOPIC_CURRENT_IMPLEMENTATION_BOUNDED_THEOREM_NOTE_2026-10-12.md): Finite current pair algebra and the canonical uniform finite-range dynamics at the source-matched hypotheses; no extra actual-operator assumptions are imported.; [Joint](MICROSCOPIC_JOINT_FLOW_BOUNDED_THEOREM_NOTE_2026-10-12.md): J15-J20 finite complete-site tests and finite-density orbit theorem; strong joint-flow conclusions are not assumed in the weighted local-algebra proof. Other named sources are historical context or transitive dependencies unless their use is stated explicitly. The complete original predecessor arguments were read, including their finite padded Jacobi proofs and tensor-word orbit theorem; source copies remain under the evidence-map entries for `weighted_current_closure/sources/`.

| Source | SHA-256 | Role here |
|---|---|---|
| Original `MICROSCOPIC_CURRENT_IMPLEMENTATION_PROBE.md`, 399 lines | `bcc9b9503e49c17b6e6140c22f3971f35ccd3ed72de16f0371666dc9162dfd9a` | I1–I13 fix the current, geometric sign and local actions; the full note was read |
| [Current review, frozen original](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/16a69597714f8c62387c2e9ee92c445c40f91410/.claude/science/physics-loops/toe-boost-gap-fock-closure-20261012/evidence/weighted_current_closure/sources/MICROSCOPIC_CURRENT_IMPLEMENTATION_REVIEW.md.gz) | `305fa33efebf1e9f9dc09d0854eddf23065877004888f55e964d31cc403f6d17` | Source-bound review context; grants no review of this new proof |
| Original `MICROSCOPIC_JOINT_FLOW_PROBE.md`, 279 lines | `35bcb1013b0716a4faa33fdbd75ff067427c1dec8e377f63ebb17ac301786ebd` | J15–J20 give finite local tests and the finite-density orbit theorem; the full note was read |
| [Joint-flow review, frozen original](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/16a69597714f8c62387c2e9ee92c445c40f91410/.claude/science/physics-loops/toe-boost-gap-fock-closure-20261012/evidence/weighted_current_closure/sources/MICROSCOPIC_JOINT_FLOW_REVIEW.md.gz) | `9699043c35343901ef75ab6a29dd560ba4aa30f8a3b908643e959958e86447c9` | Complete review read; its receipt is the next row |
| `microscopic_joint_flow_review/receipt.json` | `a31a20468660e38ff42bf215dd84832a1f722551c29ea770156dfc71781d4b06` | Correct identity of the supplied review receipt |

Instruction authority is main `a13caa4885f547c8d206265b031ba7649e539fd9`
and planning `3a4b2c66a1ead7a1c48b4359627e968f681e3c39`; the source manifest
binds the current instruction copies. The minimal axioms and primitive registry
do not supply a Hamiltonian, its conservation identities or Lorentz closure.
None of the registered scale, kinetic-isotropy or realized-state primitives is
used in this mathematical implication. No new physical axiom or primitive is
adopted. The newer boost-flow and gapped-vacuum results are not premises here.

The exact target is a finite test on a **specified** density h. Earlier notes
give `[delta_h,delta_b]=delta_p` and finite tests of unweighted pair
commutation. The missing step is removal of the position weight in
`[delta_pj,delta_b]` under conservation. The selected-main statement searches
and their full outputs are saved in `weighted_current_closure/logs/`.
No exhaustive repository or literature novelty claim is made. The parent
owns the current open-PR scope search and all Git/publication actions.

## 2. Local hypotheses and the ordered bracket

Let the site algebra be a fixed full matrix algebra `M_n(C)`, with finite
`n >= 2`, on `Z^d`, `d >= 1`. All algebraic equalities below are on the local
tensor algebra. Use the l1 metric, integer `R >= 0`,
`B_R={x:|x|_1<=R}`, and the geometric convention

\[
 h_x=\tau_x(h)=h_x^*,\qquad \operatorname{supp}h\subset B_R,
 \qquad \|h\|\le h_*<\infty.
 \tag{W1}
\]

For a local A define the finite sums

\[
 \delta_h(A)=i\sum_x[h_x,A],\qquad
 \delta_b(A)=i\sum_x x_b[h_x,A],
 \qquad
 p_j(x)=\frac i2\sum_{|v|_1\le2R}v_j[h_x,h_{x+v}],
 \qquad \delta_{p_j}(A)=i\sum_x[p_j(x),A].
 \tag{W2}
\]

An infinite Hamiltonian or first-moment operator is not used to define these
sums. For each local input only finitely many commutators are nonzero. The
canonical current has radius at most `3R`, and, with
`c_(R,j)=sum_(|v|_1<=2R)|v_j|`,

\[
 \|p_j(0)\|\le h_*^2c_{R,j},\qquad
 [\delta_h,\delta_b]=\delta_{p_b}.
 \tag{W3}
\]

The bracket means `D E - E D`. W3 is the predecessor's finite pair
symmetrization; its half counts both pair orientations. The extra supplied
condition for a fixed j is

\[
 [\delta_h,\delta_{p_j}](A)=0\quad\text{for every local }A.
 \tag{W4}
\]

It is an exact operator-algebra identity, not an expectation, a vacuum-only
identity, or a numerical tolerance. W4 has the complete finite test J17 of the
joint-flow note; it is not a consequence of W2 for general h.

## 3. Finite padded Jacobi gives a weighted local density

Define the ordered commutator density

\[
 r_j(x)=\delta_{p_j}(h_x)
       =i\sum_{|y-x|_1\le4R}[p_j(y),h_x],\qquad r_j=r_j(0).
 \tag{W5}
\]

It is Hermitian and translation covariant. Overlap of supports requires
`|y-x|_1<=4R`, so

\[
 \operatorname{supp}r_j(x)\subset x+B_{7R},\qquad
 \|r_j\|\le2|B_{4R}|h_*^3c_{R,j}.
 \tag{W6}
\]

For any local density q define its weighted derivation by the same genuinely
finite rule, `W_b(q)(A)=i sum_x x_b[tau_x(q),A]`. Then

\[
 \boxed{[\delta_{p_j},\delta_b]=W_b(r_j),\qquad
        \delta_{r_j}=[\delta_{p_j},\delta_h].}
 \tag{W7}
\]

Here is the finite-padding proof, including the term that would survive without
W4. Let `A in A(Y)` and choose the finite center set `T=Y+B_(8R)`. Set
`P_T=sum_(y in T)p_j(y)` and `B_T=sum_(x in T)x_b h_x`. In
`delta_pj delta_b(A)`, the inner h center is within R of Y and the outer p
center is within `3R+2R=5R`. In the reverse order, the inner p center is
within 3R and the outer h center within `R+6R=7R`. Thus both nested
derivations equal their finite double commutators with these sums. Finite
Jacobi gives

\[
 [\delta_{p_j},\delta_b](A)
 =-[[P_T,B_T],A]
 =-\sum_{x,y\in T}x_b[[p_j(y),h_x],A].
 \tag{W8}
\]

A nonzero nested summand requires p/h support overlap and at least one of
their supports to meet Y. If neither meets Y, both commute with A, and Jacobi
makes the nested commutator zero. In the first case the centers lie within R
and 5R of Y; in the second they lie within 3R and 7R. All contributing pairs
therefore already belong to T. Regrouping only those finite summands yields
`i sum_x x_b[r_j(x),A]`. Dropping the weight in this same proof gives the
second identity in W7. No boundary term survives on this padded input. The
finite operators themselves need not agree at their boundary.

In particular, W4 gives `delta_rj=0`, with the reversed sign relative to
`[delta_h,delta_pj]`. It does **not** give `r_j=0`.

## 4. Finite orbit moments remove the weight

Choose a Hermitian one-site basis `1,T^1,...,T^(n^2-1)`, orthonormal for the
normalized trace, with all nonidentity members traceless. A nonidentity tensor
word has finite nonempty support and no nonzero translation stabilizer: a
finite nonempty set cannot be invariant under arbitrarily large multiples of
a nonzero lattice translation.

Expand a Hermitian local q of radius L as

\[
 q=c1+\sum_O\sum_v c_{O,v}\tau_v(w_O),\qquad
 s_O=\sum_v c_{O,v},\qquad
 m_{O,b}=\sum_v v_b c_{O,v}.
 \tag{W9}
\]

Only finitely many orbits and translations occur; all coefficients are real.
Each reference `w_O` can be chosen among words supported in `B_L` in that
orbit. The finite-density theorem J20 says

\[
 \delta_q=0\quad\Longleftrightarrow\quad s_O=0
 \text{ for every nonidentity orbit }O.
 \tag{W10}
\]

Its essential necessity argument is finite: for one site z collect from all
translates of q only the words with nonidentity factor at z. Each fixed word
has coefficient exactly its orbit sum, and the collected operator `K_z` is
local. If `delta_q` vanishes on the full site factor, `K_z` belongs to that
factor's commutant. Its partial trace at z is zero because all collected
factors there are traceless. Hence `K_z=0`. Linear independence of the finite
tensor basis gives every orbit sum, choosing z in a word's support. The same
finite coefficient calculation proves sufficiency. Scalars contribute no
commutator and never require an infinite scalar sum.

For every local A, even without conservation, finite relabeling gives

\[
 \boxed{W_b(q)(A)=W_b(q^{(0)})(A)+\delta_{t_b(q)}(A),\qquad
 q^{(0)}=\sum_O s_Ow_O,\quad t_b(q)=-\sum_O m_{O,b}w_O.}
 \tag{W11}
\]

To prove it, fix an orbit and put
`Z_O(Y)={z:(z+supp w_O) intersects Y}`. This is a finite set. In its
contribution to `W_b(q)(A)`, the change of variable `z=x+v` yields exactly

\[
 i\sum_{z\in Z_O(Y)}\sum_v c_{O,v}(z_b-v_b)[\tau_z(w_O),A]
 =i\sum_{z\in Z_O(Y)}(s_Oz_b-m_{O,b})[\tau_z(w_O),A].
 \tag{W12}
\]

Every sum displayed is finite. Terms whose commutator vanishes may be included
without changing it. Thus W11 does not rearrange a divergent first moment.
For `delta_q=0`, W10 kills the weighted residue. Applying it to W5 gives

\[
 \boxed{t_{jb}=-\sum_O\Bigl(\sum_v v_bc_{O,v}\Bigr)w_O,
 \qquad [\delta_{p_j},\delta_b]=\delta_{t_{jb}}.}
 \tag{W13}
\]

There is no extra half, factor i or beta in W13. The half is already in the
current W2; both i factors and the minus from the Jacobi bracket are accounted
for in W7/W8. Here `c_(O,v)` are coefficients of `r_j` itself.

The choice of representatives has a precise limitation. Replacing `w_O` by
`tau_u(w_O)` replaces `m_(O,b)` by `m_(O,b)-u_b s_O`. Under conservation
the scalar moment coefficient is unchanged, while the word is translated.
Thus `t_jb` can change as a literal local density, but its derivation is
unchanged. The difference is a finite sum of local translation differences.
Without conservation the moment changes too; its change cancels the change
of `W_b(q^(0))` in W11. Dropping that residue is invalid.

The scalar coefficient of `r_j` is actually zero: normalized product trace
annihilates each finite commutator in W5. Scalars in a general q, or scalar
additions to h, are harmless because they are removed at the commutator level.

## 5. Divergence primitives, support and the surviving residue

The same finite orbit theorem constructs Hermitian local primitives with

\[
 q=c1+\sum_{a=1}^d(a_a-\tau_{e_a}(a_a))
 \quad\text{when}\quad\delta_q=0.
 \tag{W14}
\]

For completeness, in each zero-sum orbit write its contribution as
`sum_v c_(O,v)(tau_v(w_O)-w_O)`. Choose a finite coordinate path from 0
to v. A positive step from u to `u+e_a` contributes
`-(1-tau_ea)tau_u(w_O)`; a negative step from u to `u-e_a` contributes
`(1-tau_ea)tau_(u-ea)(w_O)`. The paths telescope and contain finitely many
terms. This proves W14 with explicit finite primitives.

On a fixed local input, reindexing the two finite commutator sums gives

\[
 W_b(a_a-\tau_{e_a}a_a)(A)
 =i\sum_z\bigl(z_b-(z-e_a)_b\bigr)[\tau_z(a_a),A]
 =\delta_{ab}\delta_{a_a}(A).
 \tag{W15}
\]

Consequently `delta_tjb=delta_a_b` for every divergence primitive of `r_j`.
If two primitive lists have the same divergence, subtract W15: their bth
members differ by a density with zero derivation. Scalar changes of a
primitive and local curl changes are included. Literal primitives need not be
unique, and no unique local stress tensor is claimed.

Take `L=7R` for `r_j`. With representatives supported in `B_L`, W13 has
`supp t_jb subset B_L` too. If both a reference word and one of its
translates occur in `B_L`, choose any site of the reference support; its
displacement has l1 length at most `2L`. Therefore a finite explicit norm
bound is

\[
 \|t_{jb}\|\le2L\sum_{O,v}|c_{O,v}|\,\|w_O\|.
 \tag{W16}
\]

This coefficient bound is computable from h and is sufficient; no smallness
is asserted. Assigning `t_jb(x)` to `x+B_L` gives interaction diameter
`2L`, cardinality at most `|B_L|`, and per-site norm at most
`|B_L| ||t_jb||`. The coordinate paths above may be chosen monotone in each
coordinate. Each intermediate displacement has length at most `2L`, so the
primitive construction has support within `B_(3L)`. It is not necessary to
use that larger radius for the criterion below.

Without W4, W11 is the exact answer: the weighted residue remains. Equivalently,
finite translation gives

\[
 \tau_a[\delta_{p_j},\delta_b]\tau_{-a}
 =[\delta_{p_j},\delta_b]-a_b\delta_{r_j}
 =[\delta_{p_j},\delta_b]+a_b[\delta_h,\delta_{p_j}].
 \tag{W17}
\]

The same sign follows directly from
`tau_a delta_b tau_-a=delta_b-a_b delta_h`. The full weighted commutator is
translation covariant precisely when the conservation defect vanishes, as
seen by taking `a=e_b`. Origin shifts of the first moment have no effect under W4. Open
finite boundaries can carry nonzero terms; none has been discarded from an
uncontrolled infinite sum.

## 6. The necessary and sufficient complete local test, including beta

Fix a real beta, or a prescribed positive beta if that is the application's
convention, and assume W4 for every required j. Define

\[
 k_{jb}=t_{jb}-\beta\delta_{jb}h.
 \tag{W18}
\]

It is Hermitian and has radius at most `L=7R`. For a complete one-site matrix
basis `{E^mu_0}`, the target is equivalent to the finite identities

\[
 \boxed{
 [\delta_{p_j},\delta_b]=\beta\delta_{jb}\delta_h
 \quad\Longleftrightarrow\quad
 i\sum_{|x|_1\le L}[\tau_x(k_{jb}),E^\mu_0]=0
 \quad\text{for every }\mu,j,b.}
 \tag{W19}
\]

Every displayed operator lies in the finite algebra `A(B_(2L))=A(B_(14R))`.
Terms outside the center ball commute with the site at zero. Necessity is
immediate. For sufficiency, linearity gives zero on the entire one-site
factor; translation covariance gives it at every site; the Leibniz rule gives
zero on every finite tensor product. Thus the test is necessary and sufficient
on all of `A_loc`. For qubits, X, Y and Z suffice since the identity test is
automatically zero. One observable, a subset of a larger site basis,
expectations or vacuum columns are not replacements for the complete operator
tests.

Equivalently, all nonidentity orbit sums of `k_jb` vanish. For a fixed finite
radius and representatives selected in advance from the complete tensor basis
on `B_L`, this is a finite polynomial test in the coefficients of h and beta:
p is quadratic in h, r and t are cubic, and the other term is beta times h.
The sparse controls may choose an actually present representative instead;
W13's representative invariance makes their derivation test identical.

If `delta_h != 0`, any successful diagonal identity determines beta uniquely:
choose a nonzero coefficient in a complete local-basis action of h and compare
the matching coefficient for `t_jj`. The remaining coefficients and diagonal
directions must agree with that same beta; all off-diagonal actions must
vanish. A separate requirement `beta>0` must also be checked. The theorem
does not select beta by dimensional convention. Under `h -> lambda h+c1`,
the actions p and t scale by `lambda^2` and `lambda^3`; a nonzero energy
action therefore has `beta -> lambda^2 beta` for `lambda != 0`.

If `delta_h=0`, W3 implies `delta_pj=0`, hence `r_j=0` and the target holds
for every beta without fixing it. If `R=0`, p and t vanish; for nonzero
on-site energy action a diagonal W19 then requires beta zero, so a supplied
positive beta fails. These are distinct degenerate cases.

This criterion fixes the energy density as well as its derivation. Replacing
h by a nontrivial local spatial divergence can preserve `delta_h` while
changing its weighted first moment by W15. No invariance under such energy
density changes, or unproved physical improvement freedom, is asserted.

## 7. Optional actual-operator consequence on the common local domain

This paragraph is a conditional domain statement, not an operator construction.
Supply a cyclic GNS representation and actual self-adjoint H, `P_j`, `B_b`
with `D=pi(A_loc)Omega` in their domains and exact actions

\[
 iH\pi(A)\Omega=\pi(\delta_h(A))\Omega,\quad
 iP_j\pi(A)\Omega=\pi(\delta_{p_j}(A))\Omega,\quad
 iB_b\pi(A)\Omega=\pi(\delta_b(A))\Omega.
 \tag{W20}
\]

Taking A=1 derives that all these operators fix Omega. Locality derives
invariance of D, so both mixed products are defined there. Thus

\[
 [P_j,B_b]\pi(A)\Omega
 =-\pi([\delta_{p_j},\delta_b](A))\Omega.
 \tag{W21}
\]

W19 gives, on this same D,

\[
 \boxed{[P_j,B_b]=-i\beta\delta_{jb}H,
 \qquad [B_b,P_j]=i\beta\delta_{jb}H.}
 \tag{W22}
\]

Conversely, W22 and W20 make the derivation
`C=[delta_pj,delta_b]-beta delta_jb delta_h` vanish on every vacuum column.
Apply it to AB: the Leibniz rule gives `pi(C(A))pi(B)Omega=0` for every
local B. Cyclic density gives `pi(C(A))=0`. A nonzero unital spin
representation is faithful on each local full matrix factor, so `C(A)=0`.
No separating vacuum is assumed. Hence the finite algebra test and the
common-domain vector identity are equivalent under W20.

For `K_j=P_j/beta`, `beta != 0`, W22 reads
`[B_b,K_j]=i delta_jb H` on D. The negative physical current clock
`Ad exp(-iy K_j)` has local derivative `-delta_pj/beta`, with precisely one
beta division. No beta division belongs inside W13. These statements do not
extend the commutator to unspecified full domains, prove essential
self-adjointness, or integrate the boost algebra. Positivity, a gap, joint
momentum commutation, particles, scattering and physical identification are
separate questions.

## 8. Exact examples and what they decide

### A. A nonzero divergence

On a one-dimensional qubit chain let `q=Z_0-Z_1`. Its orbit sum is zero,
its coefficient moment is `-1`, and W11 gives `t=Z_0`. Thus

\[
 \delta_q=0,\qquad W_1(q)=\delta_{Z_0},\qquad
 W_1(q)(X_0)=-2Y_0\ne0.
 \tag{W23}
\]

This fixes the moment sign and shows why replacing a zero derivation by a
zero density before weighting loses information. Adding `7I` changes neither
action. The controls also use a two-dimensional divergence, both coordinate
directions, alternative representatives, scalar primitive changes and a
nonzero local curl of primitives. They check the equalities as exact local
operators, not just traces.

### B. A fixed nonconserved energy density

For `h_x=Z_xZ_(x+1)+X_x`, the canonical current is
`p_x=-Z_xY_(x+1)-Z_(x-1)Y_x`. Direct finite Pauli algebra gives

\[
 [\delta_h,\delta_p](Z_0)
 =-8Y_0+8Y_{-1}X_0+8X_0Y_1-8Z_{-1}Y_0Z_1\ne0.
 \tag{W24}
\]

The four words are linearly independent. W7 still holds, but W11 retains a
nonzero weighted orbit-sum residue. Dropping it fails the exact action test;
W17 has a nonzero translation defect with the displayed sign. The reducer
refuses to label its output an unweighted reduction when the orbit sums are
nonzero. This is one specified model test, not a statement that conservation
is rare or impossible in another family.

### C. Conserved XX current, evaluated closure

Set, at the fixed normalization below,

\[
 f_x=X_xX_{x+1}+Y_xY_{x+1},\qquad
 \ell_x=X_xZ_{x+1}Z_{x+2}X_{x+3}
        +Y_xZ_{x+1}Z_{x+2}Y_{x+3},\qquad h_x=f_x.
 \tag{W25}
\]

Since `[f_0,f_1]=2i(X_0Z_1Y_2-Y_0Z_1X_2)`, W2 gives

\[
 p_0=Y_{-1}Z_0X_1-X_{-1}Z_0Y_1
       +Y_0Z_1X_2-X_0Z_1Y_2,
 \qquad r=\delta_p(f_0)=4(f_1-f_{-1}+\ell_0-\ell_{-2}).
 \tag{W26}
\]

Here r is nonzero but all its orbit sums are zero. One explicit primitive is

\[
 a=-4(f_{-1}+f_0+\ell_{-2}+\ell_{-1}),\qquad r=a-\tau_1(a).
 \tag{W27}
\]

Hence the exact energy-current derivations commute. The moment density can
be chosen as `t=-8(f_(-1)+ell_(-2))`, which has the same unweighted derivation as

\[
 \boxed{t'=-8(f_0+\ell_0),\qquad
 [\delta_p,\delta_b]=\delta_{t'}\quad(d=1).}
 \tag{W28}
\]

For this **single fixed density**, the beta-energy condition fails for every
`beta in R`: `t'-beta h=(-8-beta)f_0-8ell_0`. The nearest-neighbor and
four-site words belong to different translation orbits. The four-site orbit
coefficient remains -8 whatever beta is, so W10/W19 reject closure. At
`beta=-8` the nearest-neighbor term cancels and the four-site term remains;
at the illustrative positive value beta=1 both remain. This is an exact
evaluation of the finite criterion on W25, with its density convention held
fixed. It is not a no-go for modified densities, other interactions, continuum
limits, different algebras or representations.

The literal r calculation can be inspected without the runner. Put
`c_x=Y_xZ_(x+1)X_(x+2)-X_xZ_(x+1)Y_(x+2)`. Then
`p_0=c_(-1)+c_0`, so finite unweighted relabeling gives
`r=2i sum_(x=-2)^1[c_x,f_0]`. The four contributions are

| x | `2i[c_x,f_0]` |
|---|---|
| -2 | `-4 ell_(-2)` |
| -1 | `-4 f_(-1)` |
| 0 | `4 f_1` |
| 1 | `4 ell_0` |

All other triples are disjoint from the bond. The table follows from
`[X,Y]=2iZ`, `[Y,Z]=2iX`, `[Z,X]=2iY`; for the two inner triples the cross
terms have two anticommuting sites and cancel. Each nearest-neighbor orbit
and each four-site orbit has coefficient moment 8. This verifies W26–W28
as finite algebra, separately from execution counts.

A separate seven-site **open** occupation-basis matrix calculation forms H
and the weighted B directly, then `P=i[H,B]`. H/P have a nonzero boundary
commutator, but its action vanishes on all three center-site Pauli probes.
The local action of `i[P,B]` agrees exactly with W28. In the center-X action,
one imaginary matrix entry is 16 while the corresponding energy-action entry
is zero; it is a beta-independent finite witness. Another entry is 16
against energy entry -2, requiring beta=-8 without resolving the first
entry. Sites are ordered `-3,...,3`, with site -3 the most significant bit;
the entries are respectively `(row 0,column 1)` and `(row 0,column 4)`.
The matrix computation checks padded local identities; it does not replace
the infinite-lattice proof or require finite open H/P to commute globally.
For this specific bond model each h operation enlarges support by at most one
site at either end and each p operation by at most two. Both orders of the
weighted double derivation on a site-zero probe therefore lie in `[-3,3]`;
every relevant bond and triple is included by the seven-site open construction.
This sharper fixture bound is compatible with the general conservative W8
padding and is not an assumed periodic identification of distant words.

## 9. Author evidence, failures and handoff

The finite proof is W1–W19; W20–W22 is an optional conditional local-domain
corollary. The complete-basis test is exact, not a numerical heuristic.
Checking its equations in the intended physical model remains an obligation.
The positive result is the finite reduction and necessary/sufficient test;
the XX failure is preserved as a fixed-model application.

The primary exact control is
`weighted_current_closure/controls/weighted_controls.py`. It uses Gaussian
rational coefficients for sparse local Pauli words in one and two dimensions.
The separate `controls/matrix_controls.py` imports no primary helper and
builds open-chain occupation-basis matrices with guarded Gaussian-integer
arithmetic. Both were written in this author context after the proof
mechanism was visible. They are different arithmetic routes, **not independent
scientific review**; a fresh reviewer still has to inspect the theorem.

The first sparse execution recorded 72 successful predicates and one failed
expected-current predicate. Its hand-written expected XX current had the
opposite sign; the direct multiplication preceding W26 identified that
expectation error. The canonical-current code and its computed r/t were
unchanged. The corrected run completed all 73 predicates. The original
source, stdout, stderr, result and 60-second timeout/exit receipt are preserved
under `logs/run1/`; the corrected run is `logs/run2/`. No failed control was
deleted or rewritten.

The first matrix run completed 25 exact predicates. The final version adds
eight finite sign/beta checks and completes 33. Those added checks use the
2-by-2 matrix fixture `H=2Z`, `B=Y`, `P=4X`, `beta=-4`; it satisfies
the displayed finite commutator signs but not energy-current conservation and
is explicitly not a physical lattice example. Its beta is a diagnostic, not
a proposed physical value. The largest guarded operation bound in the final
matrix run is 33,792 against `2^60`; no floating comparison is used.

Five actual copied-source mutations were executed with the same 73 sparse
predicates. Reversing the moment sign failed 26; deleting the current half
failed 2; reducing padding to radius one failed 1; testing only Z failed 1;
and ignoring conservation failed 1. All five exited 1 without a timeout or
unintended exception. Their successful, nondiscriminating rows remain too:
current rescaling still conserves in the XX example, zero-action probes cannot
detect a moment sign, and most fixtures do not require the deliberate
conservation-rejection guard. The mutation failures test these particular
controls; their counts do not establish the theorem.

Final sparse and matrix runs completed in about 0.112 and 0.551 seconds, with
exit 0. Each baseline and mutant run had a declared 60-second timeout; each
mutant completed in under 0.12 seconds. Exact commands, source hashes, output
hashes, timestamps, elapsed times, stdout and stderr are saved in
`logs/final_sparse/`, `logs/final_matrix/`, `mutations/`, and
`logs/final_execution_summary.json`. The first run's wall-clock field was
recorded after execution but mislabeled `started_utc`; its original receipt
is unchanged, and `logs/run1/metadata_note.json` documents the limitation.
Later receipts record start time before execution. No missing timing datum
has been reconstructed as an observed fact.

Reproduce the two baselines from S with Python 3 and NumPy for the second:

```text
python3 weighted_current_closure/controls/weighted_controls.py
python3 weighted_current_closure/controls/matrix_controls.py
```

Each writes its own result JSON beside the executed script and can be rerun.
The create-only orchestration helper `controls/run_controls.py` records the
one-time frozen baseline/mutation package; run it only in a fresh copy if
recreating that package. No runner cache is used. All open-boundary differences,
nonconserved defects, tested beta failures and the beta-independent entry are
present in the saved rows. Finite examples cannot certify arbitrary unbounded
operator domains, self-adjoint realizations, an integrated Lorentz group, or
physical particles.

Frozen author operational record: the receipt and author checkpoint bind the original deliverable and evidence.
The author will not assign audit status or publish this packet. Only this note
and `weighted_current_closure/` are written.
Editable prompt files changed: **none**. No repository source, Git ref/index,
PR, audit result, axiom, other chat or model setting was changed, and no
subdelegation was used. The fixed campaign deadline is
2026-10-12 16:00:52 UTC.


## Publication evidence and review record

The complete frozen author source is `WEIGHTED_CURRENT_CLOSURE_PROBE.md`, SHA-256
`561cc0109580b74c42b19af27ab35801deea61a9c304dc2f43da772e042448f7`. Its separate review is `WEIGHTED_CURRENT_CLOSURE_REVIEW.md`, SHA-256
`5796e74e9ad160de9d240d50a67b00a83dab51af25596f0c3d1f1bfcc1b3cc95`, with receipt SHA-256 `8afb751ac3fac724d43fa5078ce37a6818e864053966ebc63be409ba3cc6fbb4`.
The [evidence map](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/16a69597714f8c62387c2e9ee92c445c40f91410/.claude/science/physics-loops/toe-boost-gap-fock-closure-20261012/EVIDENCE_MAP.json) preserves the complete own
author/reviewer sources, earlier versions, failures, stdout/stderr, execution
receipts, root source-coverage records and their byte identities. The
[exact transformation map](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/16a69597714f8c62387c2e9ee92c445c40f91410/.claude/science/physics-loops/toe-boost-gap-fock-closure-20261012/PUBLICATION_EDITS.json) and
[reconstruction program](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/16a69597714f8c62387c2e9ee92c445c40f91410/.claude/science/physics-loops/toe-boost-gap-fock-closure-20261012/reconstruct.py) recover every byte of
this complete note and its entire primary. No mathematical correction is made.
Historical review-pending and worker-scope statements above describe the author
freeze; this separate appendix records the completed source review.

**Author/checker pairing:** Same selected model family in separate author/reviewer contexts; the selected model and reasoning effort were preserved. Candidate formulas and reported outcomes were visible before distinct controls, so this was neither blinded nor cross-family checking. Root proposed mechanisms and is a coauthor, not the independent reviewer. The mechanical preparer performed no new scientific review.

The complete W1-W28 source review requires no mathematical correction.
It checks the negative first translation moment, the retained conservation
residue, the complete finite-site equivalence and the optional common-local-
domain operator corollary under its separately supplied actual actions. The
Current I1-I13 algebra and Joint J15-J20 orbit theorem are the direct proof
uses. Newer boost-flow or gap-filter theorems are not premises. A zero local
derivation is not a zero density, and primitive/representative ambiguity is
handled at the original stated scope.

The complete sparse author helper is the canonical primary: 73 finite
predicates and five copied-source mutations, with 26, 2, 1, 1 and 1 failures.
Passing mutant rows remain visible: current rescaling can conserve, shared
wrong moments can cancel, and zero-action probes may not detect a sign.
The separate author occupation-matrix helper and all 33 final predicates remain
bound evidence, including all eight added sign/beta diagnostics and the 25-row
earlier version. The H=2Z, B=Y, P=4X, beta=-4 fixture does not conserve energy
current and is not a physical lattice model. The guarded integer maximum
33,792 is below 2^60; seven open sites give finite padding, not an infinite
system, and the global boundary commutator remains nonzero.

The original sparse run failed its handwritten expected-current sign, with
72 passing predicates and one failed predicate. Its computed current/r/t
were unchanged by the expected-sign correction. All original source, output
and receipts remain. The first receipt mislabeled an after-execution clock
as started_utc; its separate correction note does not invent a missing start.
The separate reviewer reconstructed the proof and used an eleven-site exact
CAR route plus complete qutrit matrix units. Its 205 finite predicates,
different beta witness and eight byte-exact author replays are preserved.
Root's lossless read grouped 187 zero-residual rows by full labels and read
18 other records; that compression is a read aid, not new scientific evidence.

The fixed XX density fails weighted beta-energy closure for every real beta
at that density. This does not quantify over density improvements, other
interactions or all models. No integrated Lorentz group, physical self-adjoint
realization, current conservation in the intended model, particle theorem or
new physical axiom follows. All hypotheses retain their supplied status.

The [canonical finite primary](../scripts/weighted_current_closure_2026_10_12.py) retains every
original calculation and failure gate. Publication adds only mapped input and
timeout declarations, an assertion guard and finite-scope output. Original
adjacent-result writes are suppressed where present; the complete original
JSON outputs remain in the evidence map. Required output destinations in the
Boost and Integrated CLIs become optional for ordinary canonical execution.
Where present, self-hash calculations remain and refer to the source actually run.

Preparation ran no primary, mutant, independent control, runner-cache API,
vocabulary fixer, graph builder or audit compatibility check. Actual canonical
execution and complete original mutation replay are root's subsequent work,
recorded in [delivery checks](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/16a69597714f8c62387c2e9ee92c445c40f91410/.claude/science/physics-loops/toe-boost-gap-fock-closure-20261012/DELIVERY_CHECKS.md). Historical
source-bound results are not fresh canonical results. No retained promotion,
applied audit verdict, Lean certificate, helper-registry change or completed
publication is asserted here. Combined candidate validation and strict audit
lint remain separate landing gates.

This is a frozen milestone record. Root owns the sole live campaign checkpoint
and its current science-checkout pointer. Editable prompt files changed: none.
