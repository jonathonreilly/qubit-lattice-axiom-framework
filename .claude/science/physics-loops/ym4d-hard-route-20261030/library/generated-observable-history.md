# Generated marks and the missing uniform history estimate

Source: `parts/upper-chain.md` at 0cad38f3644a6749b0e4a5782335744bc1f45732,
Text 0, 14 and 20; gate `fourth-form-codex-b4de676b7.md`, finding 1.
Author: openai/gpt-6-astra/max macbook-codex, 2026-11-01.

Status: **unchecked** conditional finite-history theorem, with a proof below;
**gap** for the uniform moment closure (H20.5). This is an author calculation,
not independent review or an audit. No lemma from a paper is used. The finite
probability diagnostics concern the abstract inference, not the Wilson law.

## 1. The family, fixed before choosing a law

Work on a finite torus, with finitely many levels 0 through K. All auxiliary
variables needed by a randomized block map must be included in its joint law.
Write P_j(W,dV) for the reverse kernel from level j+1 to level j. Assume its
iterates give the actual conditional laws of the hierarchy. In particular,
given the coarser variables, the next finer variable has kernel P_j. This is
the precise tower/Markov premise used here; locality alone is not its proof.
Kernels at a specified regular top, including the reference field 1, are part
of the supplied data, not arbitrary versions on null sets.
Assume the displayed recipes define measurable functions and their kernel
integrals exist; a divergent source integral is not assigned a finite budget.

For one cell define C_j e(W) = P_j e(W) - P_j e(1). For a block c' define
H_j(e)_c' = sum_(c in B(c')) C_j e_c. These are unscaled observables;
C_j is distinct from the total-energy mark T_j of Text 14.
All coefficients below are deterministic once the kernels, extraction rule
and test function are fixed; they cannot depend on a subsequently chosen law
nu. The following recipes, not arbitrary membership in K_j, define the family.

* a_0,c = e_a(c). Define a_(j+1,c') by (CF_j): the sum of a_j at the lift on
  a regular field, and its specified regular pullback extension elsewhere,
  with value zero when the first non-regular radius is zero.
* I_(j;c',c'') is the antisymmetric current specified in Lemma 14.16. On a
  regular field it is x_j^(-1)(E^r_W-E^r_1)G^cur_(c',c''); elsewhere it is
  the midpoint pullback extension specified there, or zero at the stated
  short radius. This recipe is supplied data here. Its estimates are not
  consequences of the history theorem. Put J_(j,c') = sum_c'' I_(j;c',c'').
* z_0=1, rho_0,c=0, r^f_0,c=0. At step j take beta_j to be the scalar
  extraction of Lemma 14.15(b) applied to the already generated rho_j. Set

      h_(j,c') = H_j(a)_c' - a_(j+1,c') - J_(j,c'),
      Rem_(j,c') = H_j(rho)_c' - beta_j a_(j+1,c'),
      z_(j+1) = z_j + beta_j,
      rho_(j+1,c') = Rem_(j,c') + z_j h_(j,c'),
      D_(j,c) = z_j a_(j,c) + rho_(j,c).

  h is defined by this exact full-kernel identity on every field. Thus the
  cut/surface term, the Q^reg and log J terms, the full Q^s change of law,
  and the good-to-full-law correction are all included. An estimate of only
  the first term of a covariance expansion for Q^s is not an estimate of h.
* For each fixed test f, let d_(c,c') = f(c)-f(c') and set

      r^f_(j+1,c') = H_j(r^f)_c'
        + sum_(c in B(c')) d_(c,c') C_j D_(j,c)
        + (z_j/2) sum_c'' (f(c')-f(c'')) I_(j;c',c'').

The family also contains the intermediate H_j(a), H_j(rho), H_j(r^f), Rem,
h, the individually weighted transports d_(c,c')C_jD_(j,c), and the finite
sums f(c)D_(j,c)+r^f_(j,c). There is no operation inserting an arbitrary
element of K_j or an extra source not listed in these recipes.

**Algebraic checks [unchecked].** Direct substitution, with no estimate, gives

    D_(j+1,c') = H_j(D)_c' - z_j J_(j,c').                  (G1)

Summing (G1), antisymmetry cancels the current and gives
sum_c D_(j,c)(V)=T_j(V)-T_j(1), with T_j the mu-centered total-energy mark
defined in Text 14. The subtraction is necessary already at j=0:
sum_c D_0,c=W, whereas T_0=W-<W>. Summing the recipe for r^f
then proves the identity for y_j(f;V)-y_j(f;1) in Theorem 14.13(ii), by
induction from r^f_0=0 and the tower premise. No bound on z, rho or r follows
from these identities. In Theorem 14.1c the actual cell mark is
e^i_(j,c)=f_i(c)D_(j,c)+r^(f_i)_(j,c), with a scalar centering constant left
outside the sum. These, and not all K_j elements, are its intended inputs.

**Actual bottom [unchecked, elementary].** Text 0 gives 24 plaquettes with
coefficient 1/4 and 0<=s_p<=2. Consequently

    0 <= a_0,c = D_0,c = e_a(c) <= 12,
    |x_0 f(c)D_0,c| <= 12 x_0 |f(c)|,
    rho_0,c = r^f_0,c = 0.                                (G0)

In particular ||x_0 D_0,c 1_E||_q <= 12 x_0 P(E)^(1/q)
under every law and for every event E, not just under laws in LL_0.
The classical recursion alone gives |a_j,c|<=12 L^(4j): at each step it
sums at most L^4 previous values, even on its pullback extension. This bound
is finite and explicit, but is not the uniform bound needed by the consumer.

## 2. Sources and normalization may not disappear in an iteration

Let F^e_(j,c)=x_j e_(j,c), A_(j,c)=x_j a_(j,c), t_j=x_(j+1)/x_j and
v^e_(j,c)=P_j F^e_(j,c)(1). In the format

    F_v = S_v + sum_(u preceding v) t_(v,u) P_(j) F_u,    (G2)

the nonconstant inputs and the complete sources at level j+1 are as follows.
Each block sum below runs over c in B(c'); all current sums run over c''.

| Output | Inputs and coefficients | Source S_v |
|---|---|---|
| A_(j+1,c') | none (the prescribed classical lift/pullback recipe is a source leaf) | A_(j+1,c') |
| x_(j+1)D_(j+1,c') | F^D_(j,c), coefficient t_j | -t_j sum v^D_(j,c) - x_(j+1) z_j J_(j,c') |
| x_(j+1)rho_(j+1,c') | F^rho_(j,c), coefficient t_j | -t_j sum v^rho_(j,c) + z_j t_j sum(P_j A_(j,c)-v^a_(j,c)) - (z_j+beta_j)A_(j+1,c') - x_(j+1)z_j J_(j,c') |
| x_(j+1)r^f_(j+1,c') | F^r_(j,c), coefficient t_j; F^D_(j,c), coefficient t_j d_(c,c') | -t_j sum(v^r_(j,c)+d_(c,c')v^D_(j,c)) + x_(j+1)(z_j/2) sum(f(c')-f(c''))I_(j;c',c'') |
| x_(j+1)Rem_(j,c') | F^rho_(j,c), coefficient t_j | -t_j sum v^rho_(j,c) - beta_j A_(j+1,c') |
| x_(j+1)H_j(e)_c' | F^e_(j,c), coefficient t_j | -t_j sum v^e_(j,c) |
| x_(j+1)h_(j,c') | none, a_j treated as the specified classical source | t_j sum(P_j A_(j,c)-v^a_(j,c)) - A_(j+1,c') - x_(j+1)J_(j,c') |

The weighted transports use the H row with each coefficient and reference
term multiplied by d_(c,c'). Deterministic linear sums are estimated by the
triangle inequality with the absolute values of their coefficients. This
table covers every operation of the specified family. It also shows why a
proof for H alone would not prove the statement for Rem, rho and r.

The reference terms v^e are integrals at the regular top 1. A proposed
induction can bound them by the previous level's moment budget at that law.
No source in this table is a free “tiny” term. The t_j factors telescope along
a path to x_J/x_i; they are not individually set equal to 1.

**Source bounds that do follow from supplied clauses [unchecked conditional
derivations].** Under (CF_j)(a), its budget C x_j and the regular point
masses in LL_j give |a_j(W)|<=C at every globally regular W. Its defined
extension is a value at such a field, or zero. Hence |A_j|<=C x_j on
every field. This uses the supplied uniform classical-form clause; it is
stronger than the elementary 12 L^(4j) bound and is not a consequence of
moment closure for arbitrary marks. For example the classical part of the
rho source has the explicit bound

    |z_j t_j sum(P_j A_j-v^a_j) - (z_j+beta_j)A_(j+1)|
      <= C x_(j+1)(2 |z_j| L^4 + |z_j+beta_j|).

If the specified current has its asserted regular-field K1 bound with
eta_(c',c'')=iota^new_j exp(-c d(c',c'')), and x_(j+1),lambda_(j+1)>=1,
zeta_(j+1)<=1, telescoping K1 at a globally regular field gives

    |x_(j+1) I_(j;c',c'')|
      <= C_(kappa,kappa_s) eta_(c',c'') x_(j+1)^(3/2).

Indeed tau_n^2<=C x_(j+1)(n+1)^4, so the energy terms are bounded by the
sum of (n+1)^6 exp(-kappa n); the profile terms are bounded by
the sums of exp(-kappa sqrt(n)) and exp(-kappa_s sqrt(n)).
For convergence, group n in [m^2,(m+1)^2): there are 2m+1 terms in the
square-root sum, each at most exp(-kappa m). Polynomial factors in either
sum are bounded by a constant times exp(kappa n/2), or exp(kappa m/2),
using exp(t)>=t^r/r! with a sufficiently large fixed integer r; the
remaining series is geometric.
For the single tier omit kappa_s. The prescribed regular pullback extension
keeps this same bound at every field. Summing exp(-c d) over the current's
other endpoint is uniform on a four-dimensional torus: the number of
points at integer distance r is at most C(r+1)^3 and its exponential
series converges. This bounds the current sources, conditional on that
regular K1 estimate; GH does not prove the estimate or a bound on z_j.

At the first energy transport there is also a direct bound with no rarity:
the sum of the L^4 bare energies lies in [0,12 L^4], so

    ||x_1 H_0(a_0) 1_E||_q <= 12 x_1 L^4 P(E)^(1/q).

These inequalities are useful source inputs but do not sum the full
history, prove the regular/locality induction for its other channels,
or produce the proposed quarter-contraction.

## 3. Finite-history theorem replacing the arbitrary-class assertion

**Theorem GH [unchecked; conditional implication with proof].** Take a
finite directed graph of the recipes (G2), with every edge going from level
i to level i+1. Fix a top law nu_J and its full reverse chain law

    dP_nu = nu_J(dV_J) P_(J-1)(V_J,dV_(J-1)) ... P_0(V_1,dV_0).

All probabilities and expectations below refer to this full chain law.

For each vertex v at level i>=1 supply an event B_v measurable at V_i and a
deterministic b_v>=0 such that |F_v|1_(B_v^c)<=b_v. At level zero supply the
pointwise bound |F_v|<=d_v; for this family use (G0). Suppose the quantities
on the right below are finite. There is no moment or transport assumption
on a function not in the graph.

For a descending path p=(v_J,...,v_i) starting at a specified root v_J set

    c(p) = product_(l=i+1,...,J) |t_(v_l,v_(l-1))|,
    D_p(E) = E intersect intersection_(l=i+1,...,J) B_(v_l).

Empty products are 1 and empty intersections are the whole space; E is any
event measurable at V_J. For 1<=q<infinity,

    ||1_E F_(v_J)||_q <=
      sum_(i=1,...,J) sum_(paths p ending at i) c(p) [
        b_(v_i) P_nu(D_p(E) intersect B_(v_i)^c)^(1/q)
        + (E_nu[1_(D_p(E) intersect B_(v_i))
                    |S_(v_i)(V_i)|^q])^(1/q) ]
      + sum_(paths p ending at 0) c(p) d_(v_0)
                    P_nu(D_p(E))^(1/q).                 (GH)

If |S_v|<=s_v pointwise, its term may be replaced by
s_v P_nu(D_p(E) intersect B_v)^(1/q). Unnormalized restricted moments are
essential: none of the laws conditioned on D_p(E) is claimed to be in LL.

**Proof.** At each nonbottom vertex (G2) and the good-event bound give

    |F_v| <= b_v 1_(B_v^c) + |S_v|1_(B_v)
                  + sum_u |t_(v,u)|1_(B_v) P |F_u|.     (G3)

Iterate this positive inequality down the finite graph. Conditional on
V_J, each resulting term is c(p) times the expectation of either a stopped
good term b_(v_i)1_(D_p(E) intersect B_(v_i)^c), a source term
|S_(v_i)|1_(D_p(E) intersect B_(v_i)), or a bottom term
|F_(v_0)|1_(D_p(E)). This uses the full reverse Markov premise and keeps
every intermediate indicator inside its kernel. For a nonnegative random
variable Z and q>=1, put m=E[Z|V_J]. The tangent inequality
Z^q>=m^q+q m^(q-1)(Z-m), followed by conditional integration, gives
(E[Z|V_J])^q<=E[Z^q|V_J]; at m=0 the assertion is immediate, and q=1 is
equality. The tangent inequality follows from the nonnegative derivative
of q t^(q-1) on t>=0. Integrating and taking the q-th root bounds each
term by the corresponding term of (GH). For completeness, the finite-sum
norm inequality used here follows from the same convexity: if Z_r>=0,
a_r=||Z_r||_q>0 and A=sum a_r, then
(sum Z_r)^q <= A^q sum_r (a_r/A)(Z_r/a_r)^q. Its integral is at most
A^q. Zero-norm terms vanish and may be omitted. Together with |F_0|<=d_0
this finishes the proof. No exponent is doubled or divided in an iteration. []

**How rarity can enter [unchecked conditional bound].** If B_v=A_v union
GG_v^c and P(GG_v^c)<=beta_i for each vertex at level i, then, for any
nonempty consecutive subpath T of D_p(E),

    P_nu(D_p(E)) <= min(P_nu(E),
        sum_(l in T) beta_l + P_nu(intersection_(l in T) A_(v_l))). (G4)

Indeed, either a GG failure occurs in T, or all its bad events are A events.
The union bound proves (G4), without any independence assumption. Choosing
T as the finer half of the path retains the depth gain of the good-set
probability and of a genuine chain rarity estimate. Neither (G4) nor (GH)
licenses multiplying P(E) by a marginal rarity probability.

## 4. Exact remaining inequality and consumer changes

Let H_q(v,nu) be the right side of (GH) with E=B_v for the root v. It is an
explicit sum of source restricted moments and path-event probabilities;
it is not the unknown norm of F_v. For prescribed output budgets U_v(q),
the sufficient closing inequality is

    sup_(nu in LL_J) H_q(v,nu) <= U_v(q) - b_v,
    for every generated root v and each required q.       (H20.5)

Then (GH) on B_v, together with the good-event bound, proves (K2) with
U_v(q). This proves a conditional statement, not (H20.5). A proof must
insert quantitative bounds for every source in section 2, the actual
bottom 12 x_0, and joint probabilities under every specified top law.
It must show that the resulting bound is uniform in cutoff, volume and
depth. For the original quarter-contraction claim its proposed right side
would be C(L)x_j^(3/2)eta+u/4+epsilon_(j,q)-b_v, with an explicitly bounded
epsilon_(j,q). No such epsilon is supplied by “tiny”.

**Gap.** (H20.5) has not been proved for this family from the current
regular-field, screening and rarity clauses. The elementary classical
bound 12 L^(4j) alone is insufficient; section 2 explains the improvement
available from (CF_j)(a) and the conditional current bound. Even after
these inputs, replacing reference terms by an assumed output (K2) would
be circular. An induction may use already proved lower-level (K2), but
its full path sum, including the generated good-event bounds and their
law-uniform locality estimates, has not been closed here.

K1 and K3 are separate obligations. Given their appropriate uniform
versions, a finite good-set construction supplies b_v and beta_i for use
above. GH does not establish them. The law class is all probability
mixtures of the listed top laws in Text 20; membership is not restricted to
finite convex combinations. A K3 estimate must be proved for a fixed
arbitrary mixture, with its conditional mean recomputed in that mixture.

| Consumer | Exact effect of the replacement |
|---|---|
| Lemma 14.15(a),(b) | Their regular-tier arguments still read K1, K2, K3 of their inputs. No new moment premise is discharged here. |
| Lemma 14.15(c) | The arbitrary-input uniform closure is withdrawn. GH applies only to the listed generated recipes; (H20.5) and K3 closure remain gaps. |
| Lemma 14.16 | h has the exact full-law source recipe above. Its rough-field moment assertion cannot follow merely from the regular identity. |
| Theorem 14.13(i),(ii) | The total mark identity requires T_j(V)-T_j(1); the smeared identity already subtracts the reference value. The bounds on rho, r and their moment induction are conditional on closing their separate history budgets; the old u/4 recurrence is not proved. |
| Theorem 14.13(iii), (TR_p) | Uniform all-order moments and the sharper g_j^2 bound under mu remain open. Finite-torus boundedness is insufficient. |
| Theorem 14.1c, then UV-OS(b) | Use only the generated e^i cells. The finite moment budget and the separation-decay induction are still gaps (gate findings 2,3), even if (H20.5) were closed. |

This is a weakening of the former closure claim, explicitly propagated to
its consumers. The algebraic assembly of Theorem 14.1b is unchanged.

## 5. Attempts to kill the replacement

**Gate spike [unchecked exact calculation].** The gate's seed
F_0=p^(-1/4)B has fourth norm 1, but its supremum is p^(-1/4). It violates
(G0) whenever p<(12x_0)^(-4). GH with the honest bottom d_0=p^(-1/4)
returns a term d_0 p^(1/4)=1, and correctly gives no contraction. Thus GH
neither admits that seed as the Wilson bottom nor suppresses its true cost.

**Bounded generated copy [unchecked exact calculation].** Let a Bernoulli
bit B be copied at every level of a finite chain and take the reference
state 0. Start from F_0=B and use F_(j+1)=b P_j F_j=b^(j+1)B, b>1, with
zero sources. This can represent b identical child contributions. Put
B_v={B=1}, b_v=0 and d_0=1. The unique history term (after collecting the
b identical edges) in GH equals b^J p^(1/q), the exact norm. The ratio of
successive norms is b, not 1/4, despite a bounded bottom. At any fixed
finite depth p can be chosen below every prescribed positive upper bound
on the finitely many rare intersections. Rarity therefore cannot create
a homogeneous operator contraction; it can pay an explicit history error.
This example is a test of the proposed inference, not a Wilson or a
full-clause countermodel. It does not refute (H20.5) with a sufficiently
large stated history budget. No counterexample to GH was found in these
tests; its proof is the argument in section 3.

**Additional radius gap [unchecked exact parameter calculation].** The
proposed bad event in Text 14 is A_c={min(n_0,M_j)<=R_j+3}, R_j=x_j^2.
It is the entire space if M_j<=R_j+3, including at n_0=infinity (an
everywhere-regular field). The claimed reduction of A chains to actual
non-regular marks therefore requires

    x_j^2+3 < floor(exp(lambda_j/5))                         (R20.5)

at every consumed level, or a changed definition and proof. The stated
upper adjacent-ratio bound and linear lower bound for x do not imply this.
For x_(K-d)=x_K(5/4)^d the adjacent bound is an equality, and, for x_K>=4b',
the elementary binomial inequality (1+1/4)^d>=1+d/4 gives (T3). But if
lambda_(K-d)=l_0+l_1 d with l_1<10 log(5/4), then

    log(x_(K-d)^2) - lambda_(K-d)/5
      = 2 log x_K - l_0/5 + d(2 log(5/4)-l_1/5) -> infinity.

Any finite choice of l_0 only postpones the failure. This tests the
consumer's stated flow-to-radius inference, not a producer's actual
trajectory. A separate upper linear growth bound might exclude it.
Alternatively R_j could be capped below M_j and the good-set estimates
redone; that repair has not been proved here. It would alter the A-chain
premise consumed by (H20.5). This is another reason the current history
probabilities cannot yet be substituted as uniform small bounds.

## 6. Reopening and limits

Next: resolve (R20.5) or replace the cutoff in A and the tested radii; then
prove (H20.5) for the recipes above, including vacuum constants and the
current/source norms, with a simultaneous K3 induction. Only after that
can a fixed Q(n) and the quantitative cumulant induction be undertaken.
No conclusion here excludes another proof of these bounds.

The source search for direct consumers covered parts/ and library/ at the
pinned revision. Full arguments used here are the upper-chain passages
identified above; a mapped-side search hit for Lemma 14.15 is a statement
of offered smoothing clauses, not a proof imported into this note. Neither
hard-core proof was read or transported to the other attempt. The later
interface repairs and I(k;D) have not been undertaken at this stop.
