# A stationary Euler-scale wave limit for immutable context exchanges

Primary derivation, 2026-09-21. A separate pre-source proof reconstructs the
same stationary Fourier-propagation limit for both supplied generators,
including the axis-balanced extension. Its full report/checker and all 16
artifacts/six dependencies have been read and verified. Report SHA
`772046745ac814c32adcd8f36e3c8415ddf4a3a4b37435e8992441c6c8d5be68`;
seal SHA `c729b0f85e0350b834380909001ef62f0db0378fdf114b108f5feef7f6e0e8d1`.
It uses canonical current averaging and a crude quantitative Poincare bound;
the primary proof below uses one anchored conditional current and successive
limits. This agreement supplies separate mathematical support, not formal
retention, final publication-source review, or a physical-field identification.
No novelty claim is made for the fluctuation method.

## 1. Claim with explicit limits

Take the conservative context exchange on the N^3 periodic cubic lattice,
with fixed u,E and either of the two bounded rates in
`CONTEXT_EXCHANGE_ACOUSTIC_DERIVATION.md`. The rate floor c_*>0 is fixed as N
grows. Start in a fixed full-support homogeneous product pi_p. There are no
births in this statement. Put V=N^3, C=diag(p)-p p^T, and let xi_x be the
six-vector of occupied-label indicators. Macroscopic time has generator N L_N.

For a fixed nonzero integer vector m, let K=2 pi m and define

`Y_N(K,t)=V^(-1/2) sum_x exp(-i K dot x/N) [xi_x(Nt)-p]`.

Let A_i be the Jacobian of the exact product current J_i at p, with the
microscopic u,E held fixed, and A(K)=sum_i K_i A_i. The target is

`E |Y_N(K,t)-exp[-i A(K)t] Y_N(K,0)|^2 -> 0`                    (1)

for every fixed finite t, and jointly for any finite list of fixed times
and Fourier modes. In particular, the microscopic dynamic covariance has
the explicit limit

`E[Y_N(K,t) Y_N(K,0)^*] -> exp[-i A(K)t] C`.                   (2)

The initial product central limit theorem then gives joint Gaussian Fourier
limits transported by the linearized Euler equation. Complex conjugacy of
opposite modes is retained. This note proves finite-dimensional statements,
not tightness in a specified infinite-dimensional path topology.

At the isotropic composition p_a=rho_*/6 with u=-2E rho_*, E!=0,

`lim_N E[Y_rho,N(K,t) conj(Y_rho,N(K,0))]`

` = rho_*(1-rho_*) cos(c_s |K|t)`,

`c_s^2=4 E^2 rho_*^2(1-rho_*)/3`.                              (3)

Thus, under the stated hypotheses, this is a microscopic
long-wavelength correlation limit, rather than just a current eigenvalue
or a fitted finite-lattice speed. It is classical, stationary and tied to
supplied rates and a supplied composition. No relativistic or TOE
identification follows.

## 2. A finite-state forward/backward bound

First consider any finite stationary continuous-time Markov chain with
generator L and strictly positive stationary law pi. Irreducible sectors
are allowed. Write S=(L+L^*)/2 in L2(pi), and

`D(g)=<g,-Sg>`,

`||F||_(-1,S)^2 = sup_g {2<F,g>-D(g)}`.

Suppose F is orthogonal to the kernel of S. The finite-dimensional equation
`-S u=F` has a solution orthogonal to that kernel, and the displayed norm
equals `<F,(-S)^(-1)F>=D(u)`.

On a stationary path over [0,t], the forward martingale is

`M_t=u(eta_t)-u(eta_0)-integral_0^t L u(eta_s) ds`.

The reversed stationary path has generator L^*, so its terminal martingale is

`Mhat_t=u(eta_0)-u(eta_t)-integral_0^t L^*u(eta_s) ds`.

Adding cancels the endpoints exactly:

`integral_0^t F(eta_s) ds = (M_t+Mhat_t)/2`.

Both martingales have second moment `2t D(u)`. The square inequality
`(a+b)^2<=2a^2+2b^2` therefore proves

`E[(integral_0^t F(eta_s) ds)^2] <= 2t ||F||_(-1,S)^2`.         (4)

No reversibility or uniform sector condition on L-S was assumed. On the
accelerated process N L the right side is divided by N. Apply the bound
separately to real and imaginary parts when needed. The argument is entirely
finite dimensional, including the Poisson equation on each count sector.

## 3. Conditional mixing of a local current

Let j_i be one scalar component of the actual forward exchange current
`c_i(eta)[xi_x-xi_(x+e_i)]`; its product expectation is the corresponding
component of J_i(p). It is bounded and depends on four sites. Choose a fixed
cube B_l containing its footprint, with M=(2l+1)^3, and set

`hat j_l = E_pi_p[j_i | the seven counts in B_l]`,

`h_l=j_i-hat j_l`.

Conditional on the block counts, pi_p is the uniform arrangement law.
Internal nearest-neighbor swaps connect each fixed-count sector, so for
some finite A_l, uniform over the finitely many sectors,

`E Var(g | outside B_l, counts B_l)`

` <= A_l sum_(e inside B_l) E[(g(eta^e)-g(eta))^2]`.             (5)

This holds for every global test function g, by fixing the outside
configuration and then applying the finite-sector Poincare inequality.
Because h_l has conditional mean zero, Cauchy-Schwarz gives

`|E[h_l g]| <= C sqrt(A_l D_(B_l,unweighted)(g))`.               (6)

Take deterministic real coefficients a_x bounded in absolute value by one,
and form `F_N=V^(-1/2) sum_x a_x tau_x h_l`. Sum (6), use Cauchy-Schwarz
over x and note that each edge belongs to at most M translated blocks.
The symmetric part of the actual generator satisfies

`D_N(g)=<g,-S_Ng> >= (c_*/2) sum_e E[(g^e-g)^2]`.

Consequently

`|<F_N,g>| <= C sqrt(A_l M/c_*) sqrt(D_N(g))`,

`||F_N||_(-1,S_N)^2 <= C A_l M/c_*`.                            (7)

The kernel consists of functions of the global counts: strict positive
adjacent-swap rates connect each global count sector. Every tau_x h_l is
orthogonal to those functions, since fixing the outside and the block counts
fixes the global counts. Thus (4) applies without an unremoved zero mode.
For all t<=T,

`E |integral_0^t V^(-1/2) sum_x a_x tau_x h_l(eta_(Ns)) ds|^2`

` <= C T A_l M/(N c_*)`.                                      (8)

First N grows with l fixed. No quantitative estimate of A_l as l grows is
needed. This step supplies mixing for the actual context-dependent process;
it does not assume independent successive times.

## 4. Linearizing the canonical current

Write q for the six empirical occupied frequencies in B_l. Sampling four
fixed positions from its uniform count sector differs from independent
sampling with probabilities q by at most C/M in total variation, uniformly
over the counts. It follows that

`hat j_l=J_i(q)+r_l(q)`, `|r_l(q)|<=C/M`.                        (9)

The current polynomial has bounded second derivatives on the closed
probability simplex. Define the centered block remainder

`W_l=hat j_l-J_i(p)-A_i(p)(q-p)`.

Its mean under pi_p is exactly zero, by conditional expectation and E q=p.
Taylor's formula, (9), and the fourth moment of a bounded independent block
sample give

`E W_l^2 <= C E|q-p|^4+C/M^2 <= C/M^2`.                        (10)

Translated W_l's on disjoint blocks are independent under the stationary
product. Each block overlaps only O(M) others. Hence, for bounded a_x,

`E |V^(-1/2) sum_x a_x tau_x W_l|^2 <= C/M`.                    (11)

Stationarity and Cauchy-Schwarz in time bound the corresponding time
integral's second moment by C T^2/M. This estimate uses no independence in
time. It is valid uniformly in N sufficiently large relative to fixed l.

For a_x=exp(-i K dot x/N), averaging xi over B_l multiplies its Fourier
mode by the deterministic block multiplier phi_l(K/N). This multiplier
tends to one as N grows at fixed l, with `|phi_l-1|<=C_K l/N`.
The product variance of each Y_N is exactly C, uniformly in N. Thus replacing
the averaged density by xi in the linear term costs O(T^2 l^2/N^2) in second
moment. The constant current term vanishes because sum_x a_x=0 for the
fixed nonzero mode and all sufficiently large N.

Combining (8)-(11) proves the first-order current replacement

`sup_(t<=T) E |integral_0^t [Z_i,N(K,s)-A_i Y_N(K,s)] ds|^2`

` <= C_T [A_l M/(N c_*)+1/M+l^2/N^2]`,                        (12)

where `Z_i,N=V^(-1/2) sum_x exp(-i K dot x/N) j_i(tau_x eta)`.
The supremum is outside expectation. First take N to infinity and then
l to infinity. This is the required first-order Boltzmann-Gibbs replacement
for this finite-range, multiple-conservation-law generator.

## 5. Fourier martingale and deterministic propagation

The microscopic conservation identity gives exactly

`Y_N(K,t)=Y_N(K,0)+sum_i b_i,N integral_0^t Z_i,N(K,s) ds+M_N(t)`,

`b_i,N=N[exp(-i K_i/N)-1]`.

Each swap changes Y_N by at most `C_K/(N sqrt(V))`. There are O(V) bounded
clocks, accelerated by N. Therefore

`E tr <M_N>_t <= C_K t/N`.                                    (13)

Set `B_N=sum_i b_i,N A_i`, which converges to -i A(K). The exact
variation-of-constants formula for this semimartingale is

`Y_N(t)=exp(B_N t)Y_N(0)+integral_0^t exp[B_N(t-s)] dM_N(s)`

` +sum_i b_i,N integral_0^t exp[B_N(t-s)]`

`                         [Z_i,N(s)-A_iY_N(s)] ds`.             (14)

The matrices exp(B_N s) and their derivatives are bounded uniformly in N
on every fixed [0,T], because B_N is bounded. By the martingale isometry,
(13) makes the stochastic convolution vanish in L2. To handle the last
term, put X_i,N(t)=integral_0^t[Z_i,N-A_iY_N] ds and integrate by parts:

`integral_0^t exp[B_N(t-s)] dX_i,N(s)`

` = X_i,N(t)+integral_0^t B_N exp[B_N(t-s)] X_i,N(s) ds`.

Minkowski's inequality and (12) make this vanish in L2 in the same
successive limits. No maximal-in-time version of (12) is needed. This
proves (1). Cauchy-Schwarz and the exact finite product covariance C then
give (2).

For any finite collection of modes, their initial real and imaginary
Fourier sums are sums of independent bounded triangular-array terms. The
elementary Lindeberg central limit theorem applies; the discrete Fourier
orthogonality determines their limiting covariances. Statement (1) at a
finite collection of times transports this initial Gaussian law. This is
the claimed finite-dimensional fluctuation limit.

## 6. Density waves and limits of the result

The already derived identity A_i C=C A_i^T implies preservation of the
stationary covariance under the limiting propagation. At the tuned
isotropic composition the density and vector equations are

`d delta rho/dt=-i a K dot delta g`,
`d delta g/dt=-i b K delta rho`,

`a=2E rho_*(1-rho_*)`, `b=2E rho_*/3`, `ab=c_s^2`.

Initial product density-vector covariance is zero and density variance is
rho_*(1-rho_*). Solving the two linear equations yields (3). The two
transverse vector and two quadrupole modes remain zero-speed modes on this
time scale. They are part of the limit, not silently discarded variables.

The statement concerns k=K/N and microscopic time Nt at fixed K,t, with
fixed positive exchange floor. It neither gives a uniform rate of
convergence nor identifies the finite-k damping. The constants A_l can
grow without control because the proof takes successive limits. It is
not a proof at a vanishing swap floor, at fixed microscopic wave number,
under nonstationary formation, or after allowing the rates themselves to
depend on N. It does not establish a Lorentz-invariant interacting field,
quantum amplitudes, a physical clock, or selection of the tuned density.

## 7. Established method, candidate application

Forward/backward stationary martingale decompositions and Boltzmann-Gibbs
replacement are established machinery. The finite-state inequality is
derived explicitly in section 2 so that no nonreversible hypothesis is
hidden in a theorem import. Liming Wu's 1999 primary article,
[Forward-backward martingale decomposition](https://www.numdam.org/item/AIHPB_1999__35_2_121_0/),
is relevant general context. Olla and Xu's
[anharmonic-chain Euler fluctuation paper](https://arxiv.org/abs/1808.00306v3)
is an example of the broader program, not a theorem applied to this
seven-state context-exchange process. At the time this note was first
written, the bibliographic records and abstracts had been inspected; their
full proofs had not been imported. The proof obligations for the present
model are written above and require independent checking.
