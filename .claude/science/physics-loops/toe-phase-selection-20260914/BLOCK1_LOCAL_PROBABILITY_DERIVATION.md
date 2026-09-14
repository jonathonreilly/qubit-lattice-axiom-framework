# Actual ground-state local probabilities at finite penalties

Personal working proof, 2026-09-14. This result concerns the explicitly supplied
clock Hamiltonian. It does not identify a phase or a native Record law. The
proof below needs a separate challenge before any public milestone claim.

## Abstract finite-dimensional statement

Let the Hilbert space be a product of three-state coordinate registers. Suppose
H is real symmetric with nonpositive off-diagonal entries and has a normalized
nonnegative ground vector Omega, with energy E. Choose a finite register set R
of size r. Split H=H_far+H_near, where H_far acts only on the complement of R,
its imaginary-time semigroup has nonnegative entries, and H_near>=0. Suppose
the diagonal entries of H_near are at most C and the off-diagonal hopping
amplitudes of H include at least h>0 for both cyclic shifts of every register
in R, uniformly in all other coordinate values. All other hopping amplitudes
remain nonnegative after these baseline shifts are subtracted.

For every coordinate pattern s on R and every tau>0,

    Prob_Omega(a_R=s) >= exp(-2 C tau)
          [(exp(2 h tau)-exp(-h tau))/3]^(2r).                 (1)

C is a local constant. It may depend on couplings and on R, but need not grow
with the total system size. This is a lower bound on diagonal probabilities,
not a claim that the local reduced density matrix has full rank.

## Proof

Let X_l denote the cyclic coordinate shift. The matrix

    G = -H_far - C I + h sum_(l in R)(X_l+X_l*)

is entrywise at most -H. Off the diagonal this follows from the baseline
hopping assumption; on the diagonal it is C>=diag H_near. Both matrices are
Metzler matrices (their off-diagonal entries are nonnegative). Adding a common
large scalar multiple of I makes both entrywise nonnegative, so their power
series imply the entrywise order

    exp(-tau H) >= exp(tau G)
      = exp(-C tau) exp(-tau H_far) K_R,
    K_R = product_(l in R) exp[tau h(X_l+X_l*)].

Each one-register factor has diagonal
(exp(2h tau)+2exp(-h tau))/3 and off-diagonal
k=(exp(2h tau)-exp(-h tau))/3>0. Every entry of K_R is therefore at least
k^r. Write the ground vector in local coordinate blocks Omega_u on the
complement. All blocks are entrywise nonnegative. The ground-state identity
Omega=exp(tau E) exp(-tau H) Omega consequently gives, entrywise,

    Omega_s >= exp[tau(E-C)] k^r
                   sum_u exp(-tau H_far) Omega_u.

The summands on the right are entrywise nonnegative. Their sum has squared
norm at least the sum of their squared norms. Hence

    ||Omega_s|| >= exp[tau(E-C)] k^r ||exp(-tau H_far) Omega||.

Spectral Jensen gives

    ||exp(-tau H_far) Omega||
       = <exp(-2tau H_far)>^(1/2) >= exp(-tau <H_far>).

Finally E-<H_far>=<H_near>>=0. Substitution and squaring prove (1). No
spectral gap, clustering estimate, thermodynamic extrapolation or assumption
that Omega lies in an integer-neutral sector enters this proof.

Positivity of H_near is a convenient normalization, not an irremovable
restriction on bounded local interactions. If H_near>=-m I, move the scalar
m I into H_near and subtract it from H_far. The same proof works with C+m.
Dropping the condition without changing C is invalid: the last Jensen step
would otherwise discard a possibly negative <H_near>.

## Application to the finite-penalty clock Hamiltonian

Work first on the full link-coordinate Hilbert space. For finite mu and
finite K,lambda>=0, the original link moves have rates at least
h=t exp(-4mu)>0, and each electric term 2t I-A_l is positive. Each Wilson
term and each lambda Q_c^2 is positive. Define H_near as the sum of all
declared local terms whose support meets R, and H_far as the remaining terms.
This gives H_near>=0, and H_far acts off R with a nonnegative imaginary-time
semigroup. If n_e,n_p,n_c count those near electric, face and cube terms,
one may take

    C = 2t n_e + (3K/2) n_p + 4 lambda n_c.

The factor 4 follows from |Q_c|<=2 on a six-face cube. A conservative
geometry-only estimate on the cubic lattice is

    n_e<=13r,  n_p<=4r,  n_c<=4r,
    C<=r(26t+6K+16lambda).

An electric term's declared support is the union of the faces incident on its
shifted edge, with at most thirteen edges. The relation of two edges belonging
to a common face is symmetric, which gives the first count. Boundary terms
only reduce these bounds. Exact local counts can improve the constant.

For the twelve edges of a bulk cube, the counts are n_e=60, n_p=30 and
n_c=19, giving C=120t+45K+76lambda. There are six cube faces and twenty-four
external faces attached to one cube edge each. The electric-term support
relation reaches the twelve cube edges, twenty-four outward edges at the
eight vertices, and twenty-four opposite edges of those external faces.
The near cubes are the cube itself, six face neighbors and twelve edge
neighbors. Corner-only contact involves no coordinate edge and is excluded.
The geometry runner reconstructs these counts on a 5x5x5 box independently
of this classification.

Perron-Frobenius supplies a unique strictly positive ground vector on every
finite full coordinate graph because every single-link shift is allowed.
The original gauge transformations are permutations commuting with H, so the
unique positive vector is physical. Thus applying the full-coordinate proof
does not select an unphysical state.

Take R to be the twelve boundary links of a cube c. There are coordinate
patterns on these links with Q_c nonzero. For example, starting at zero,
two appropriately oriented different edges sharing one face can make that
face wrap while the other affected faces do not; the cube then has integer
charge +/-1. The finite runner must provide the exact oriented assignment.
For any such pattern s, its projector is bounded above by the charge-defect
projector at c. Therefore (1) gives a strictly positive lower bound on
Prob(Q_c!=0), uniform over boxes containing the same local neighborhood.
It also lower-bounds <Q_c^2>.

The runner's explicit unit-cube assignment sets the x-directed edges anchored
at (0,0,0) and (0,0,1) to -1 and +1, respectively, and all other cube edges
to zero. With the product-cell orientation it has face flux
(-1,1,1,0,0,0) and Q_c=+1. It is an original coordinate assignment, so no
physical-space membership is inferred just from a desired flux pattern.

One may also sum (1) over all charged coordinate patterns. There are 243
physical cube fluxes, with charge-sector counts (1,50,141,50,1) for
Q_c=(-2,-1,0,1,2). These coefficients follow from
(z^-1+1+z)^6 at powers 3Q_c. Every flux has 3^7 coordinate representatives,
so the number of charged twelve-link patterns is 102*3^7=223074. Therefore

    Prob(Q_c!=0) >= 223074 exp(-2C tau)
                [(exp(2h tau)-exp(-h tau))/3]^24.

This remains a conservative lower bound, not a fitted density. The direct
single-pattern version alone already proves strict positivity.

The bound survives local weak limits of these finite-volume ground states.
At fixed finite couplings, the bare integer-neutral projector therefore
cannot become exact locally along this family of states. This does not
exclude a Coulomb phase: virtual defects and dressed low-energy gauge
observables are different questions. It also does not compare energies of
the separately conserved sectors of the hard temporal model, where h=0 and
the bound vanishes.

## Size and singular limits of the bound

The lower bound can be extremely small. It is informative about strict
positivity and volume dependence, not an accurate defect-density estimate.
For C>2rh its logarithm is optimized at

    tau = [log((C+rh)/(C-2rh))]/(3h).

This follows by differentiating the right side's logarithm. It is optional:
every fixed tau>0 already supplies the asserted positive lower bound. Use
logarithms to record very small values without numerical underflow.

As mu or lambda tends to infinity, h or the resulting lower bound can tend to
zero. Thus the result is consistent with the two hard-penalty projections.
It requires the stated nonnegative hopping and positive-term split; it is
not a general theorem about all Hamiltonians permitted by the framework.
