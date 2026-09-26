# Independent proper-cubic projection and drift reconstruction

Complete primary note read at the identity in PRE_SOURCES.json before any
new author checker/results. All computations below were independently
implemented. No source correction has been identified.

## 1. Missing alternating operator component

For a proper signed permutation R with underlying permutation sigma,
det R=1 implies product(signs)=sign(sigma). Thus chi(b)=b1 b2 b3 satisfies
chi(Rb)=a(R)chi(b), where a(R)=sign(sigma) is a one-dimensional character.
If rho_(Rb)=U(R)rho_b U(R)^dagger, substitution c=Rb gives

    U(R)[sum_b chi(b)rho_b]U(R)^dagger
       =a(R)sum_b chi(b)rho_b.

Here U=1 direct-sum R is fixed. Any operator transforming by a must vanish:
the three proper two-coordinate sign flips have a=+1 and force its
singlet/triplet off-diagonal vectors and every off-diagonal triplet entry
to be zero. A coordinate three-cycle also has a=+1 and forces the three
triplet diagonal entries to agree. Finally a proper rotation whose
underlying permutation is a transposition has a=-1. It leaves that
remaining scalar block form unchanged, so the form must equal its negative.
This proves the zero operator directly, without a character-table import.

Equivalently, End(1+V) has two scalars, three vectors, and the five-dimensional
symmetric traceless tensor sector. The diagonal traceless part has the
two-dimensional permutation quotient, not the alternating character. The
independent exact 16-by-16 projection sum over all 24 rotations has all
256 entries zero, checking the conjugation/vectorization convention as well.

Affineness then makes delta p_b=delta_w chi(b)/8 invisible to the density
operator. This conclusion uses exactly the stated proper-24 action and
single-pair representation. It is not a classification of other physical
representations or larger blocks.

## 2. Positive readable example

For the proposed corner state, the triplet block is
(r-kappa)I+kappa bb^T. Its perpendicular and parallel eigenvalues are
5/32 and 3/16. The coupling to the singlet is only along b; its Schur
complement is 1/2-(3/48^2)/(3/16)=71/144. The axis Schur complement is
1/2-(1/16^2)/(1/6)=61/128. These prove strict positivity analytically.
Every trace is one and covariance follows directly from e->Re,b->Rb.
The script also checks all 56 leading principal minors and all 336
matrix covariance relations exactly.

Only corner states contribute to the (1,2) triplet entry, by kappa b1 b2.
Therefore Q12=|1><2|+|2><1| has expectation 2kappa Z12=Z12/48.
The cubic-weighted state sum is exactly zero. A constant family rho_a=I/4
is an explicit countercontrol: it is covariant and cubic-blind but has no
nonzero readable Z12 moment. Thus the representation result alone does
not imply a dynamical contradiction; the observable premise is essential.

## 3. Actual finite microscopic current

Both product preparations have constant X=A e2, Y=Z=0 and D_i=1/7,
with A=1/28. The second adds w(x)=eta cos(pi x/3), eta=1/16. The profiles
are normalized and strictly positive, minimum 3/56. The cubic perturbation
changes none of the lower moments, so the covariant affine encoding gives
identical local density operators. Independent encoded pair preparation
then gives identical full product density operators. No count conditioning
or retained preparation label is used.

In the actual four-context current, S_delta(p_l+p_r)_a equals
gamma delta.[X cross b_a], because X is constant and both Y contexts
vanish. The two endpoint mu terms vanish since Y=0. The symmetric part
of the Z12 current vanishes since Z12 is zero at both endpoints.
Since sum_a p_a b1 b2 b=(Y2,Y1,w), the exact remaining current is

    J_(delta,Z12)(x)=gamma/4 *delta.[X cross e3]
                                      [w(x)+w(q_delta x)].

Only the nonfixed delta=-e1 contributes. Its displacement is -2e1 and

    dot Z12(x)=-(gamma A/4)[w(x+2)-w(x-2)].

At x=1, w(3)=-eta and w(-1)=eta/2, giving 3 gamma A eta/8=3/3584.
The baseline derivative is zero, so the Q12 derivative difference is
(1/48)(3/3584)=1/57344. The encoded local density derivative difference
has entries (1,2) and (2,1) equal to 1/114688 and all others zero.
All statements use microscopic time and the actual rate k0/2+h/4.

The direct independent control sums all 14^4 color assignments of each
incoming and outgoing channel in five nonfixed directions for both
preparations, twenty cases in total. It forms the full fourteen-entry
current from the actual rate before projecting to Z12. Integer common
denominators and a checked int64 accumulation bound make these exact
calculations. A separate contraction gives the displayed current formula.
All 12 local preparation phases, full-product factorization and a two-pair
tensor example are checked. The first execution succeeded with empty stderr.

## 4. Scope

The fixed covariant affine representation necessarily loses w. The displayed
positive encoding also reads Z12 and therefore fails to assign a unique
initial Q12 derivative to these equal complete encoded product inputs
under the supplied classical law. More generally the same test applies
when that specific nonzero Z12 assignment is part of the interface; it
does not apply to a constant encoding with no such observable.

A fixed unitary change of basis preserves the projection and density
equalities. Input-correlated environments, retained classical information,
nonproduct/count-conditioned preparations, another U, larger blocks,
restricted preparation domains or different dynamics change the premises.
No universal no-go, quantum dynamics, later product evolution, physical
field identification, publication or audit status is established here.
