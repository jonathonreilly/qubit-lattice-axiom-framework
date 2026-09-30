# Focused independent centered-law continuation check

2026-09-30. No blocking discrepancy was found in the source-bound
continuation. The actual full canonical Hamiltonian with centered
derivatives has the stated grid-uniform short analytic existence time
and O(epsilon^2) convergence of states and true constraint densities to
the supplied continuum comparison. This is a dependent continuation of
the already checked analytic proof, not formal review, audit, retained
status, or an independent theorem family.

The checked new author REPORT is
`e2efd8f2ef08b175d13ea70f09e4f3969701657fcfc1e1f07adddfdc0107d74d`.
Its source-bound parent proof is
`93e302c06d9e6a6c85f3c538f2d765ec1dcb5734065f740b310e9144f6abd6b8`,
with prior independent check
`11a2350888aea0c661b1ccf5f0196898ab9aa7012f0955b4e991bd257f3ba65f`.
Complete exact bindings appear in SOURCE_BINDINGS.json.

## Independent derivation before comparison

I read only the new CONTRACT before writing PRECOMPARISON.md, frozen
at 03:18:07 UTC with SHA256
`4a13e840b21687df7cc7d2e800c355242839868cf9f05d675c4b6f3214afb659`.
It derived the full all-frequency sampling commutator, combined-gradient
constant, exact augmentation applicability, use of unchanged bootstrap
and Volterra constants, and the three distinct locality statements.
The author proof, code and results were unread at that freeze. The
parent analytic proof had already been independently checked in full.

After freezing, I read the complete new REPORT, diagnostic source,
results, run log and pre-execution freeze. I did not import or execute
the author code. No numerical rerun was needed: the changed analytic
steps admit direct bounds, and the prior independent full 3D gradient
derivation applies to every real skew derivative, not just its previous
spectral numerical fixture. That previous fixture is not being relabeled
as a numerical test of the centered law.

## Exact law and support

For n=2J+1, epsilon=2pi/n, the centered shift difference is a real,
time-independent, skew-adjoint operator on the actual periodic grid.
The Hamiltonian is defined afresh by inserting it into every derivative
in the literal Christoffel curvature. Ordinary grid products, six full
canonical metric pairs, p=n^3 P, and pi_offdiag=p_offdiag/2 remain as
specified. Thus the normalization and the exact skew-summation variation
from the parent remain valid. No continuum product or chain rule is
inserted into a finite expression.

In particular, q=D_epsilon g and r=D_epsilon B(g), where
B=sqrt(det g)g^{-1}, give exactly H=mean[T+V(g,q,r)]. V is the parent's
algebraic expression. The adjoint r contribution to pdot is
B_g^* sum_j D_epsilon,j V_r_j, with B_g outside the derivative. Time
differentiation of q-D_epsilon g and r-D_epsilon B gives zero exactly.
The enlarged vector field is an analysis device defined off this
consistency manifold, while its consistent restriction is the actual
finite canonical evolution.

The report distinguishes support correctly:

- A Christoffel symbol uses the central metric and its radius-one axial
  star. The literal scalar constraint density includes D Gamma and has
  graph radius at most two about its stated site.
- At unit lapse, exact summation by parts yields a Hamiltonian density
  T+V(g,Dg,DB) supported on one radius-one star, of diameter two.
- Varying a sum of these stars makes the canonical equation stencil
  radius at most two. The actual momentum density
  pi^ij q_k,ij-2D_j(g_ik pi^ij) has radius one.

Matrix inversion and determinant square root act at a site and enlarge
none of these supports. Physical distances are stencil distances times
epsilon. This is a finite-range continuous-metric Hamiltonian with
derivative normalization depending on epsilon, not a fixed native
qubit realization or a preservation of block112's staggered seed.

## All aliases and the combined derivative constant

Let r(k) be the representative of a continuum Fourier mode k modulo n.
The centered symbol has exact periodicity

    sin(epsilon r_j(k))/epsilon = sin(epsilon k_j)/epsilon.

The coefficient of (D_epsilon,j I_n-I_n partial_j)f at representative l
is consequently the sum over all k with r(k)=l of

    i[sin(epsilon k_j)/epsilon-k_j] fhat(k).

This includes arbitrarily high original frequencies, including modes
whose samples are constant. There is no input-band restriction. For
all real t, integrating |1-cos t|<=t^2/2 gives
|sin t-t|<=|t|^3/6. With delta=rho-rho'>0, triangle inequality,
|r(k)|_1<=|k|_1 and sum_j|k_j|^3<=|k|_1^3 give

    sum_j ||(D_epsilon,j I_n-I_n partial_j)f||_rho'
      <= epsilon^2 L(delta) ||f||_rho,
    L(delta)=(1/6)[3/(e delta)]^3.

Thus the bound in equation (1) is correct for the combined three-vector
of derivatives as well as for each component. There is no missing factor
three. Summing further field or matrix components uses their stipulated
entry-sum norms. The all-frequency cubic estimate already prices the
aliases in this commutator; the CONTRACT's prospective extra exponential
term is unnecessary, as the final proof explicitly explains.

The interpolant-to-continuum difference still has its separate sampling
tail. On a positive radius reserve that tail is exponentially small in
J and can be absorbed into a uniform O(epsilon^2) bound, since
epsilon=2pi/(2J+1). The stated equation (2) compares actual samples and
does not silently omit an interpolant error.

## Uniform analytic time and stability

On each representative mode, |sin(epsilon k_j)|/epsilon<=|k_j|. The
combined derivative norm is therefore bounded by the same N seminorm,
and the same one-radius Cauchy estimate holds. The circular Wiener
product and N-seminorm inequalities do not depend on the derivative
symbol. All local coefficient maps in the augmented system are unchanged.

Consequently the parent's finite majorant rules yield the same C0,C1,
C_h and scale Lipschitz constant C. Its initial M0 estimate also applies:
D_epsilon I_n f is bounded by N(f), and summing its three components
does not introduce a factor three. The shrinking-radius bootstrap,
strict metric margin, reality, and finite-dimensional continuation use
only these upper bounds. They establish the same T0 and shortened
Volterra time T for the new finite Hamiltonian.

No step divides by the centered symbol or invokes coercivity, a lower
symbol estimate, a uniform Sobolev estimate, or the absence of extra
ultraviolet behavior. Its poor high-frequency lower bound is therefore
not a gap in this analytic proof. It remains a material limitation of
stronger claims that have not been made.

The already constructed continuum trajectory can be reused directly.
For rho2=3sigma0/4, rho1=sigma0/2 and delta=sigma0/4, the finite source
is a sum of local P factors multiplying precisely the commutators above.
It is bounded by epsilon^2 L(delta) sum_l m_P_l m_Q_l. The initial
g,p samples agree, while the q,r mismatch is bounded by epsilon^2
L(delta)(||h0||_rho2+||B(g0)-I||_rho2). Applying the previously checked
time-ordered Volterra bound gives exactly equation (2), including its
factor two. The sampled continuum q and r need not obey the finite
consistency relations; the analytic vector field and the common convex
ball exist off that manifold, which is all this comparison needs.

This comparison supplies convergence without assuming an independent
continuum well-posedness theorem or proving another hyperbolic estimate.
The alternative compactness argument is also compatible with the changed
symbol: its fixed-mode convergence and uniformly controlled analytic
tails suffice after reserving a radius margin.

## Actual constraints and diagnostic check

The actual scalar density remains the literal kinetic-minus-curvature
expression with centered D; it must not be replaced by the alternative
unit-lapse energy density. The momentum density is obtained by exact
finite summation by parts in the given spatial generator. Both densities
contain at most one derivative of a local analytic map of augmented U.
Their scale Lipschitz bound between sigma0/4 and sigma0/8 is unchanged.
The new sampling estimate gives their separate O(epsilon^2) defects.
The parent's full continuum algebra propagates zero continuum initial
constraints, hence the claimed finite constraint-error bound follows.
No exact finite constraint surface or algebra follows from this argument.

Inspection confirms that the diagnostic replaces the derivative matrix
in both the original Hamiltonian and the exact-adjoint dynamics. It
retains the true C and J_x, including the nonzero initial J_x. The
diagonal, x-dependent subspace remains invariant by the same transverse
reflection/translation argument as in the parent. J_y and J_z vanish
there by symmetry; they were not independently evolved numerically.

There is also a simple independent expression for the initial error.
For the stated Kasner data at t=1, set f=1+eta cos x. Then
g=(f^2,1,1), p=(-4/(3f),-f/3,-f/3), so the literal C is zero for any
derivative acting on these data: the curvature cancels and the kinetic
contraction cancels algebraically. But

    J_x=-(4/(3f))[D(f^2)-2f Df]
       =-8 eta^2 sin(epsilon)[1-cos(epsilon)] sin x cos x
          /[3 epsilon(1+eta cos x)].

This nonzero quantity is O(epsilon^2) even before evolution, owing to
the centered product-rule defect. It independently explains the saved
initial constraint behavior; it is not a numerical observation fitted
to a convergence plot. The full derivative formula includes all aliases,
although this particular initial fixture has only a few metric harmonics.

The saved source/results record a 2.325e-16 axial gradient discrepancy
and state-error/epsilon^2 ratios tending to approximately 1.459e-5 on
n=17 through 257. The execution record is 14.854 seconds and 106,938,368
bytes peak RSS. These are author diagnostics inspected here, not new
independent trajectory evidence or interval-certified errors. The fixed
duration 0.01 is not certified by the analytic majorants. The new
FREEZE.json is explicitly a pre-execution snapshot; this check separately
binds the completed JSON and run log without relabeling that earlier
snapshot.

## Scope and result

The analytic continuation is valid within the stated small-metric analytic
preparation, unit lapse, zero shift, and fixed-period refinement. It gives
a finite-range actual-Hamiltonian approximation over a common positive
time, retaining the entire finite canonical grid and its ultraviolet
branch. It is compatible with obstructions to exact finite local closure.
It does not select this law from the axioms, realize native M2 geometry,
couple the original walker, identify a record clock, provide generic
smooth-data or long-time stability, or prove unique graviton content.

No author files or prior frozen checks were edited. Deadline and stop
sentinel were checked at the start; no new compute job, background worker,
network mutation, formal disposition, or prior-art novelty claim was made.
