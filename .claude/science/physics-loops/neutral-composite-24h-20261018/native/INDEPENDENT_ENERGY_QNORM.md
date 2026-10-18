# Fourier diagnostic norm and low-window fraction

Disposition: PASS for the specified bond-centered Q_q density and infinite-temperature spectral measure. No exact pole, nonzero beta-zero retarded response, or physical scalar identification follows. No repository edits or formal audit.

The source defines Q_q=sum_a[H_a,[H,H_(a,q)]], with Fourier phase at the inner bond center and the same1/sqrt(V) normalization as E_q. This density convention matters: the formula is not automatically the norm of another local partition of Q.

## Contraction and polynomial

The script collects each resulting Pauli string's coefficient by its original inner-bond center, then contracts equal strings. The center is unique for an inner bond on the stated lattice, so its assignment does not overwrite a distinct contribution with the same center. Double commutator coefficients already include all outer-bond sums. Center differences are reduced modulo the torus; the retained displacements have doubled coordinates at most2 in magnitude. At L5 they are unaliased, and Fourier evaluation at allowed torus momenta is consistent with the bond-center convention.

The root implementation divides by V in floating arithmetic and then checks proximity to integers. I independently accumulated all contraction numerators as exact Python integers and divided by V only afterward with Fraction. The resulting55 displacement coefficients agree exactly with the cosine expansion, not merely with sampled momentum values. This strengthens the arithmetic certification without changing the source. Control: neutral-energy-qnorm-independent.py/json.

The verified expression is

    N(q)/J^6 =1536+512 sum_a cos(q_a)
      +256 sum_(a<b) cos(q_a)cos(q_b)
      +256 sum_(a<b) cos(q_a/2)cos(q_b/2)
      +256 sum_(cyclic a,b,c) cos(q_a)cos(q_b/2)cos(q_c/2).

The pair sums are UNORDERED, and the cyclic sum has THREE terms. At q0 it is5376. The conserved energy projection has norm3072J^6, so its fraction is exactly4/7 at q0. Nonnegativity of N is guaranteed by the Pauli norm construction, not by positivity of each trigonometric term separately.

## Projection inequality

Use the Hilbert-Schmidt Liouvillian and its orthogonal spectral projector P_Omega onto |omega|<=Omega. Normalize e=E_q/sqrt(m0) and v=Q_q/sqrt(N). Their overlap magnitude is

    c(q)=|<E_q,Q_q>|/sqrt(m0*N)
        =|g(q)| sqrt(m0/N).

The energy moment bound gives ||(1-P_Omega)e||<=delta, where delta=sqrt(m2/(m0*Omega²)). Orthogonal splitting and Cauchy–Schwarz yield

    c <= ||P_Omega v|| + delta.

Therefore the diagnostic's normalized low-frequency mass obeys exactly

    mu_Qq(|omega|<=Omega)/N
      >= [max(0, |g(q)|sqrt(m0/N)
                    -sqrt(m2/(m0*Omega²)))]².

This argument does not assume that the part of Q orthogonal to E has high frequency, nor that it cannot interfere with the low-frequency projection. It explicitly bounds that possibility. It is valid for non-Hermitian Fourier components, since the Hilbert-Schmidt Liouvillian has an orthogonal spectral resolution and the associated measure uses absolute matrix-element squares. Require m0,N>0, as holds near q0 for nonzero isotropic J.

For Omega=A|J||q|, fixed A>0, isotropic moment asymptotics give delta->sqrt(8/3)/A, while c->sqrt(4/7). Consequently

    liminf_(q->0) mu_Qq(|omega|<=A|J||q|)/N(q)
      >= [sqrt(4/7)-sqrt(8/3)/A]_+².

The lower bound is nontrivial for A>sqrt(14/3). The absolute value of J makes the frequency scale positive; the root's AJ convention presumes J>0. Finite tori require compatible allowed momenta and a growing-volume sequence. The exact local polynomial and moment bounds are uniform across that sequence.

This is a positive fraction in a shrinking frequency window. It does not identify the distribution inside the window, separate elastic from inelastic weight, prove a delta-function pole, or determine dispersion or lifetime. At beta0 the retarded commutator expectation remains identically zero; the statement is about fluctuation spectral mass in the supplied tracial ensemble.
