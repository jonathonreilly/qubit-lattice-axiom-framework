# Stable cut completion controls the source remainder at every fixed activity order

Personal proof candidate, 2026-09-15. This combines the stable forest
interpolation with a new cut-flip identity and the graph Holder estimate.
Its conclusion is uniform in component restrictions at each fixed particle
number. It supplies no bound uniform in that particle number and therefore
no evaluation of the activity expansion at its physical value one.

## 1. Fixed coefficient and source subtraction

Use the all-shape infinite-cubic component representation from the earlier
notes. For n_e+n_m=n>=1, let C_(n_e,n_m),a(z) denote the connected formal
coefficient of lambda_e^n_e lambda_m^n_m in a finite component restriction,
with physical source z h_a. Include the actual hard core, both species,
all orientation signs, and the usual 2^n/(n_e!n_m!) factor. The source
amplitudes are L_i=-g<S_i,Ph_a> or -i b<n_i,Qh_a> as before.

The object to be bounded is the coefficient with its constant and quadratic
source terms subtracted. Global sign reversal makes it even in z. For
Y_sigma=sum_i sigma_i L_i, use the exact Taylor identity

    cosh(zY)-1-(zY)^2/2
      = (z^4 Y^4/6) integral_0^1 (1-u)^3 cosh(uzY) du.   (1.1)

Expand Y^4 into monomials with four source legs, retaining their sign
factors. Write the final cosh as the average of exp(+uzY), exp(-uzY).
The latter is a residual source factor with |uz|<=R for |z|<=R.

Apply the finite connected BKAR identity from the forest note. Each tree
derivative has two possible pieces: a same-species hard-core term or an
odd J' term, and a mixed even cosine difference or an odd sine term.
The same-species residual Gaussian exponential is kept intact. A selected
mixed derivative removes its pair factor; no division by a possibly zero
mixed factor is used. Residual hard-core factors have modulus at most one.

Represent every even tree term by two spatial edges and every odd term
by one spatial edge. A hard-core term admits the two-edge local majorant
from the graph Holder note. The original tree guarantees connectivity
among all n component vertices. The four source legs connect their marked
vertices to an additional vertex 0, which is fixed in space.

For these estimates, move the self-weights from the measures nu into
the residual weight and use the unweighted shape/translation/mark counting
measures outside it. Each self-weight occurs exactly once.

## 2. The residual family stays stable under a cut flip

Let s=s^T be the fixed forest correlation matrix. Keep original diagonal
self-weights, and the modified positive Gram matrix J' of the forest note.
After several operations below, the same-species off-diagonal coupling is
s_ij r_ij J'_ij, where r is an entrywise product of matrices R_A(t):

    R_A(t)_ij = 1 if i,j are both in A or both outside A,
                t otherwise,                -1<=t<=1.

Each R_A(t) is positive semidefinite with diagonal one: it is the Gram
matrix obtained by assigning one unit vector to A and another, with inner
product t, to its complement. Hence s composed entrywise with r and J'
remains positive semidefinite.

Each remaining mixed factor has the form

    1+s_ij(cos theta_ij-1)
       +i sigma_i sigma_j s_ij sin(theta_ij) r_ij.      (2.1)

Its modulus is at most one for every real |r_ij|<=1: decreasing the
absolute imaginary part from its endpoint value cannot increase the
modulus. This extension retains the original integral phase periodicity.
Source factors take the form

    exp[zeta sum_i sigma_i L_i r_i], |zeta|<=R,
    r_i=product_(earlier cuts A containing i) t_A.

All r_i have absolute value at most one. The residual weight, including
its original self-weights, is consequently bounded by

    exp[-sum_i x_i m_i/64 + R sum_i |L_i|].             (2.2)

Here the local reserve comes from c0=1/32 and integer currents, exactly
as in the forest note. Removed mixed or hard-core factors do not affect
the positive Gram calculation. Signs conjugate the Gram matrix and do
not change its positivity. This holds for arbitrary repeated or overlapping
component lists, not only compatible endpoint configurations.

## 3. One exact operation removes a troublesome bridge

For a term produced so far, its explicit prefactor is a mass/position
amplitude times the sign monomial M_sigma represented by its selected
odd spatial edges and its source legs. Even spatial edges have been
doubled. Suppose its augmented graph has a bridge. Removing the bridge
gives a cut A of component vertices not containing vertex 0. The cut has
exactly one edge, so flipping every sigma_i with i in A changes M_sigma
to -M_sigma. All non-sign prefactors stay unchanged.

If U_sigma is the residual factor, sign-average invariance gives

    average_sigma M_sigma U_sigma
      = (1/2) average_sigma M_sigma
                                [U_sigma-U_(flip_A sigma)].          (3.1)

Insert a fresh cut parameter t by multiplying r_ij by t across A and
its complement and r_i by t for i in A. At t=1 the residual is U_sigma;
at t=-1 it is U_(flip_A sigma). The family is precisely the stable
family of section 2, so

    (3.1) = integral_(-1)^1 (dt/2)
                      average_sigma M_sigma partial_t U_sigma(t).  (3.2)

Differentiation produces only the following terms:

* A same-species crossing pair contributes
  -s_ij J'_ij sigma_i sigma_j times its earlier r_ij. The Gaussian
  exponential remains in the residual.
* A remaining mixed crossing pair contributes
  i s_ij sin(theta_ij) sigma_i sigma_j times its earlier r_ij.
  That pair factor is removed from the residual product.
* The residual source contributes zeta L_i sigma_i times its earlier
  r_i for some i in A. Its source exponential remains.

Thus every derivative term adds either one spatial edge crossing this
cut or one source edge from A to vertex 0. Its additional scalar cut
parameters have modulus at most one. The selected bridge ceases to be
a bridge, and adding an edge cannot create new bridges. No estimate has
yet discarded the sign cancellation that required this operation.

Apply (3.2) to another bridge of each resulting term, if any. At most
n operations are needed, since the connected augmented graph has n+1
vertices. Choose cuts from the combinatorial graph alone, independent
of signs, positions and interpolation parameters. Every resulting graph
is bridgeless, has K source legs with 4<=K<=n+4, and at most 3n+2
edges counting multiplicities. The expansion at fixed n is finite.

This argument uses cut flips, not a sequence of single-vertex derivative
estimates. Merely covering all initially odd vertices with another edge
would not guarantee the absence of an unmarked bridge.

## 4. Summation after completion

Now take absolute values. The modified same-species kernel J' has the
same kappa(x)=(1+|x|_1)^(-4) spatial majorant as the original Coulomb
kernel, plus a local term, with polynomial mass factors. The sine is
bounded by the raw phase with the same majorant. Even tree bonds have
two such factors. Every source leg has the L_i function of its component
anchor, with l^p norm at most

    C_f sqrt(x_i) ||fill_i||_1 a^(2-4/p), p>=2.

The graph Holder construction needs only connectivity and absence of
bridges; it does not need even degrees once those properties are known.
Mix a tree of the spatial graph plus one uniformly chosen source edge
with the containing/avoiding-tree distribution, with delta=1/[4(K-1)].
Every spatial exponent is strictly above one, every source exponent is
at least 4K/5>2, and the sum of source reciprocals is at most 5/4.
Each completed graph therefore contributes a spatial sum bounded by

    C_(graph,f,R,parameters) (mass polynomial) a^(2K-5).

For a<=min(g,b)/(128 C_f R), with the R=0 case immediate, the pointwise
source bound |L_i|<=C_f a sqrt(x_i)m_i leaves from (2.2) the reserve

    exp[-sum_i x_i m_i/128].                           (4.1)

All fixed-degree mass polynomials are summable against the complete
anchored shape count if

    g^2/128>log 393, b^2/128>log 393.                   (4.2)

For example both x>=1024 suffice. beta=32,N=256 is one fixed finite
choice meeting (4.2). The number is a sufficient coefficient-bound
range, not a newly established phase window.

Since n is fixed, all tree choices, cut completions, mass powers and
interpolation integrals have finite constants. K>=4 then gives

    sup_(|z|<=R) |C_(n_e,n_m),a(z)-C_(n_e,n_m),a(0)
                           -(z^2/2) C_(n_e,n_m),a''(0)|
       <= C_(n_e,n_m,f,R,beta,N) a^3.                  (4.3)

As in the four-component note, the subtraction is made inside the
coefficient sum. Equation (4.3) gives an absolutely convergent subtracted
infinite-kernel functional, uniform in finite component restrictions.
It is not a separate convergence assertion for its unsubtracted or
quadratic pieces. The graph summation and all-shape domination justify
passage of this subtracted object through increasing restrictions.

## 5. The remaining all-order issue is explicit

The containing/avoiding-tree construction allows spatial exponents close
to one as n grows. For the displayed construction their distance from
one can be of order 1/n^2. There are also many cut-completion choices
and increasingly high filling moments. Nothing here bounds the constants
in (4.3) by a summable activity sequence. A positive radius of convergence
that reaches physical activities one has not been proved.

The result is a proposed Gaussian source remainder at every fixed formal
activity order. Fixed-order disappearance of non-Gaussian terms cannot
be interchanged with an uncontrolled infinite sum. The signed quadratic
response, state construction and finite-free-boundary matching remain
separate tasks. This cut operation is a new mechanism toward the response
problem; it is neither a TOE result nor a model or axiom obstruction.

## 6. Finite challenge and personal review

The finite checker exercises 840 initial graphs with 2-8 component vertices
and all 4,100 possible next crossing-edge choices encountered along sampled
completion paths. Each choice removes its selected bridge and creates none.
The exact cut identity is separately tested on the four-cube cochain
couplings, with two mixed tree factors removed, a previous negative cut
parameter, complex sources, and a zero remaining mixed factor. The analytic
product-rule derivative agrees with numerical differentiation within 1.06e-52;
the integrated sign-flip identity agrees within 1.38e-54, at 45-digit working
precision with floating cochain inputs. These are identity checks at those
inputs, not 45-digit certification of the underlying projection matrix.

Three source mutations dropping, respectively, the same-species, mixed or
source derivative term are rejected by assertion. A fourth mutation removing
the imaginary unit from a mixed sine is rejected by the original-exponential
pair comparator in the four-component source checker. Its earlier comparator
shared the C/O decomposition on both sides and was strengthened during review.
An initial zero-string parsing failure in the cut checker is preserved; using
the exact integer zero fixed it without changing a formula or tolerance.

The review is personal, following the user's no-subagent instruction. It
does not supply independent review or retained status. The full derivation,
not the number of finite checks, carries the proposed fixed-order result.
