# Cubic color information in a covariant single-pair density encoding

**Status:** proposed exact representation identity and finite compatibility
witness; author control and independent scrutiny pending. Raw research only,
not a completed general no-go package. Date:2026-09-22.

Fix the previously used singlet/triplet rotation representation U(R)=1 direct-sum R
on one pair's four-dimensional Hilbert space, for the24 proper signed
permutation matrices R. Suppose density matrices assigned to the fourteen
colors transform covariantly, and probabilistic mixtures are encoded affinely.
No alternative rotation representation, larger block or restricted preparation
family is excluded by the following calculation.

## 1. An exact missing representation

For a cube color b in{+-1}^3 let chi(b)=b1*b2*b3. Write R as a signed
permutation with underlying coordinate permutation sigma. Since det R=1,
the product of its three signs is sign(sigma), and

    chi(Rb)=sign(sigma) chi(b).

Let a(R)=sign(sigma). For any covariant family rho_b, the operator
T=sum_b chi(b)rho_b obeys U(R)T U(R)^dagger=a(R)T. But the exact matrix
projection on the16-dimensional operator space is

    P_a=(1/24)sum_R a(R)[U(R) conjugate tensor U(R)]=0.

The accompanying control constructs every R and evaluates all256 entries
over the rationals. An analytic explanation is that the operator space of
1 direct-sum the vector representation contains two scalars, three vectors,
and the symmetric traceless rank-two tensors. Under coordinate sign flips,
only the scalar and diagonal-tensor components are invariant. The remaining
diagonal traceless subspace carries the two-dimensional permutation quotient,
which has no alternating one-dimensional component. The exact projection
also establishes the identity without importing that decomposition.

It follows that T=0. Changing only the cubic color moment w by replacing
p_b with p_b+delta_w*chi(b)/8 leaves the encoded pair density unchanged.
This is independent of the particular positive covariant matrices chosen.
The statement concerns this specified U and affine preparation map.

## 2. A positive encoding with a visible quadratic color observable

For a concrete compatibility test, choose q=1/2,r=1/6,lambda_A=1/16,
lambda_B=1/48,kappa=1/96. Define

    rho_A(e)=[[q,lambda_A e^T],[lambda_A e,r I]],
    rho_B(b)=[[q,-i lambda_B b^T],
              [i lambda_B b,r I+kappa(bb^T-I)]].

These trace-one matrices are strictly positive and covariant. Positivity
is checked by all four exact leading principal minors for each of14 states.
For Q12=|1><2|+|2><1|,

    Tr[rho(p) Q12]=2 kappa Z12.

This family still loses w, as every family with the stated covariance must.
It is a preparation map only; no quantum evolution is supplied.

## 3. Exact initial-drift witness using the existing color law

Use the fixed winding N=12 process, gamma=1,k0=11/10. At every site take
D_i=1/7, X=(0,A,0),Y=Z=0,w=0, with A=1/28. Explicitly all probabilities
are1/14 except p_A2,+ increased by A/2 and p_A2,- decreased by A/2.
For the second preparation add eta*cos(pi*x/3)*chi(b)/8 to every B-color
probability, with eta=1/16. Both preparations are strictly positive.

Their density matrices coincide at every black site, and therefore their
full product density matrices coincide exactly. The second has the spatial
cubic moment w(x)=eta*cos(pi*x/3), while all lower moments are unchanged.

Use the exact four-context current from DIMER_NONLINEAR_INITIAL_DRIFT.md,
not a continuum limit. Since X is constant and Y=0, its Z12 projection is

    J_(delta,Z12)(x)=gamma*[delta.(X cross e3)]
                              *[w(x)+w(q_delta x)]/4.

The symmetric part vanishes since Z12=0. Only delta=-e1 has both a
nonzero contraction and displacement; its winding displacement is-2e1.
Incoming minus outgoing current at x=1 gives

    d_t Z12(1)|0=-gamma*A*[w(3)-w(-1)]/4
                =3*gamma*A*eta/8=3/3584.

The baseline derivative is zero. Thus the two equal density operators
receive Q12 derivatives differing by2*kappa*(3/3584)=1/57344.
No density-operator evolution can assign both derivatives on a preparation
domain containing these two states with the stated observable assignment.

More generally, the representation identity forces w-blindness for any
such covariant single-pair affine encoding. The drift contradiction also
requires a nonzero readable Z12 observable, or another explicitly tested
observable sensitive to the lost information under evolution. Covariance
alone does not prove a drift contradiction for an encoding that maps
everything to one state. This observability premise must not be omitted.

The result is a targeted design constraint on this representation, encoding
rule and preparation domain. It leaves larger blocks, different physical
representations, extra state information, restricted states and different
generators open. It neither refutes the separate positive quantum models
nor establishes a general impossibility result for a TOE.
