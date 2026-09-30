# Independent spectral-evolution approach before author comparison

This file is frozen before opening spectral-evolution-route/REPORT.md, FIRST_ORDER_FORMULATION.md or any new implementation. I have read only its CONTRACT.md and the complete original spectral-nonlinear-route/REPORT.md defining the actual finite law. No uniform evolution result is presumed.

## Exact Hamiltonian rewrite which appears to remove the extra derivative loss

The actual carrier is the full odd-grid six-component canonical metric/momentum space. Use the density pi, with the supplied factor of two on off-diagonal canonical slots and the grid-volume factor already specified in the source. Hamiltonian H=C[1], zero shift, is the normalized grid mean of

`T(g,pi)-K B^ij R_ij`,

where `T=a/sqrt(det g)[tr(g pi g pi)-tr(g pi)^2/2]`, `B=sqrt(det g)g^-1`, and the Ricci expression is the original Christoffel definition with spectral D and full grid products. No continuum Einstein-tensor variation may be substituted on the finite grid.

Introduce redundant analysis variables `q_k,ij=D_k g_ij` and `r_k^ij=D_k B^ij`. Set Gamma equal to its algebraic expression in g,q. Exact grid summation by parts, not a product rule, gives H=<T+K E>, with

`E=r_k^ij Gamma^k_ij-r_j^ij Gamma^k_ik`

`  -B^ij(Gamma^k_kl Gamma^l_ij-Gamma^k_jl Gamma^l_ik)`.

Hold q,r independent when differentiating this pointwise analytic expression. In symmetric-matrix Frobenius pairing, let B'(g)^* be the adjoint derivative of B. The exact metric variation is

`delta H/delta g=T_g+K E_g-K sum_k D_k E_qk-K B'(g)^* sum_k D_k E_rk`.

In particular the last term has B'^* OUTSIDE the derivative. It follows from `delta r_k=D_k[B'(g)delta g]` and one exact summation by parts. Replacing r by B'(g)q would assume a false finite spatial chain rule.

Let `F=T_pi=2a/sqrt(det g)[g pi g-g tr(g pi)/2]`. A proposed exact first-order analysis system is

`g_t=F`,

`pi_t=-T_g-K E_g+K sum D E_q+K B'^* sum D E_r`,

`q_t=D F`,

`r_t=D[B'(g)F]`.

Time differentiation and the ordinary finite-dimensional chain rule preserve q=Dg and r=DB(g) exactly. These are not extra canonical degrees of freedom. Each right side contains at most one spectral derivative of an analytic pointwise function of the augmented variables. The system must be checked with all six entries; taking a diagonal truncation before variation could hide an error.

This first-order rewrite makes a grid-uniform analytic estimate plausible. Directly estimating the original pi equation in (g,pi) alone loses two spatial derivatives; a naive first-order analytic Cauchy estimate for that unaugmented vector field is not justified.

## Uniform analytic estimates that would need proof

For the normalized Fourier Wiener norm `||u||_rho=sum_k exp(rho |k|_1)|u_hat(k)|`, circular multiplication has a uniform algebra bound because the odd-grid representative of k+l has l1 length at most |k|_1+|l|_1. Also `||D_j u||_rho'<=1/[e(rho-rho')]||u||_rho`. These statements are compatible with the absence of a finite product rule.

For pointwise analytic compositions there should be a stronger weighted derivative inequality, obtained termwise from their absolutely convergent power series:

`||D Phi(U)||_rho <= C(M) sum_k |k|_1 exp(rho|k|_1)|U_hat(k)|`.

It is an inequality using the frequency-sum bound, not an assertion `D Phi=Phi' DU`. It extends to the augmented equations with coefficients analytic in h near zero and polynomial in pi,q,r. Matrix inverse and determinant square-root branches need uniform majorants in the chosen component/matrix norm; smallness of h must be maintained independently of the potentially large gradient or momentum norm.

With a shrinking radius rho(t)=sigma0-lambda t, the derivative of the absolute Fourier sum has a negative term `-lambda sum |k|_1 exp(rho|k|_1)|U_hat|`. If the exact right side satisfies

`||U_t||_rho <=C0(M)+C1(M) sum |k|_1 exp(rho|k|_1)|U_hat|`,

choosing lambda>C1(M) supplies an a priori bound independent of J. The derivative-free g equation separately bounds metric motion. Taking time small enough keeps ||h|| below, for example, 1/4 and preserves positive real metrics. All constants must be made explicit as majorant bounds for the actual expression, rather than invoked as a missing analytic theorem.

Sampling analytic initial g,pi at radius 2sigma0 gives a uniform initial augmented bound at sigma0: q and r each cost one Cauchy radius gap. Sampling B(g0) commutes with its pointwise evaluation, whereas differentiating it need not commute with sampling. The normalized-mean canonical volume factors must cancel in the actual ODE before applying a uniform estimate.

Finite ODE continuation plus these estimates would establish existence on a common interval. Continuum existence can then be obtained by compactness into a smaller analytic radius, using exponentially small Fourier tails and a uniform bound on time derivatives at a still smaller radius. One must pass the augmented constraints q=partial g and r=partial B(g) and the exact evolution equation to the limit; bounded finite ODE solutions alone do not identify the continuum limit.

Uniqueness and a rate need a separate stability estimate. Comparing at a smaller shrinking radius should absorb the principal derivative of the difference; terms multiplying a differentiated reference solution cost another fixed radius gap. A possible inequality is

`d||U-V||_rho/dt <=(C1-lambda)|U-V|_(rho,1)+C(M,delta)||U-V||_rho+||forcing||_rho`.

Reference gradients are bounded using the larger analytic strip. It must be proved for the actual nonlinear composition/outer-product expressions. This is not a Sobolev stability or strong-hyperbolicity assertion.

## Sampling and product-rule residuals

Interpolation I_J of analytic samples is a circular alias sum. For rho>rho', the tails give

`||I_J f-f||_rho' <=2 exp[-(rho-rho')(J+1)] ||f||_rho`.

The derivative commutator `D_J I_J f-I_J partial f` has only aliased high-frequency terms and costs an additional frequency factor. A safe bound follows by spending part of the radius gap, or by a factor of order `(J+1)+1/(rho-rho')`. Similar estimates must be propagated through every pointwise inverse, square root, product and derivative in the actual Hamiltonian vector field. Nonlinear compositions do not preserve a finite band.

For trigonometric interpolants, the finite evolution should be compared with the continuum augmented vector field plus an exponentially small forcing at a smaller radius. Combining this with the stability inequality, not compactness alone, can give a quantitative convergence rate. The initial augmented sampling mismatch q_J versus sampled partial g0 and r_J versus sampled partial B(g0) must be included. A rate may lose some of the original strip width; its constants and polynomial factors should be stated honestly.

Finite constraint density is the actual sampled Christoffel expression. It contains one more derivative of q; the momentum density is `J_k=pi^ij D_k g_ij-2 D_j(pi^ij g_ik)`. Their convergence requires another radius gap and their own alias estimates. They are not exactly preserved merely because canonical Jacobi is exact.

For the continuum comparator, the exact source algebra gives, at lapse one and zero shift,

`J_i,t=0`, `C_t=aK partial_j(g^ij J_i)`.

Thus continuum constrained initial data remain constrained. Only after the evolution and density consistency estimates can one deduce exponentially small finite constraint errors. This would not establish exact finite first-class closure, nor cover arbitrary initial data satisfying only a discrete constraint.

## Diagnostic checks to seek after the proof is read

The diagonal, x-dependent restriction is plausibly invariant because reflection in y and reflection in z preserve the full finite Hamiltonian and reverse each relevant off-diagonal component. Translation invariance in y,z removes their derivatives. This symmetry argument has to act on the complete canonical tensor law before reducing it.

For the proposed pulled-back Kasner solution, put f'(x)=1+eta cos x. The continuum metric is

`g=diag(t^(-2/3) f'(x)^2,t^(4/3),t^(4/3))`.

In the actual normalization, momentum follows from g_t=F, giving

`pi^ii=sqrt(det g)/(a t) (p_i-1)/g_ii`, with p=(-1/3,2/3,2/3).

Hence `pi^xx=-4 t^(2/3)/(3a f')`, `pi^yy=pi^zz=-f' t^(-4/3)/(3a)`. K does not enter this flat-spatial-slice solution. Its kinetic constraint vanishes by the Kasner identities. The sampled curvature density can vanish for this special diagonal geometry while its full finite Hamiltonian variation still has alias errors, so checking density alone is insufficient. An independent finite directional derivative must test the actual curvature Hamiltonian gradient.

A successful trajectory diagnostic does not by itself prove the uniform analytic theorem, and its chosen time may exceed a conservative rigorously guaranteed interval. The calculation should retain alias and precision failures. Even a successful analytic theorem remains local in coordinate time for supplied continuous, spatially nonlocal canonical data; it does not derive a record clock, the native carrier, the original walker or smooth-data numerical stability.
