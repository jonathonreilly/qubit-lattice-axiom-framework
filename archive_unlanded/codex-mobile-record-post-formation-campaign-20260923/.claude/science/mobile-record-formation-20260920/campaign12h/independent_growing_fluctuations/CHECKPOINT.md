# Current independent checkpoint

No new primary source has been read. The full theorem and the new
nonstationary replacement estimate are proved in REPORT.md. The complete
independent checker finished with 108 groups passed and zero failures.

- Exact product trajectory: p0(t)=p0(0)exp(-6 beta t),
  pa(t)=pa(0)+p0(0)(1-exp(-6 beta t))/6.
- The deterministic stationary transport statement is false with births.
  The candidate is the six-field linear Gaussian SDE with drift
  B_K(t)=-i sum_i K_i DJ_i(p(t))-beta 11^T and noise covariance
  beta p0(t) I dt, retaining conjugate/opposite-mode relations.
- A direct evolving-law energy lemma closes the fast block residual.
  Solve (partial_t+G_N)u=-F_t with terminal zero. Exact forward evolution
  of mu_t gives
  E|integral F|^2=||u_0||^2+integral E Gamma_G(u)
               =2 Re integral <u,F>_mu.
  If |<F_t,h>|<=a_t sqrt(E_0,t(h)), the exchange floor yields
  E|integral F|^2<=2 integral a_t^2/(N delta).
  The conditional canonical block bound supplies the same a_t as in the
  stationary proof, uniformly along the full-support product trajectory.
- The correct reverse generator is the weighted formal adjoint minus
  diag(partial_t log mu_t). Its birth transitions are occupied a to vacancy
  at beta p0(t)/pa(t). A naive stationary adjoint would not have zero row
  sums. This will be checked explicitly, even though the proof uses the
  direct energy route instead of reversal.
- C(t)=diag(p)-p p^T satisfies
  Cdot=B_K C+C B_K^*+beta p0 I because DJ_i C=C DJ_i^T.
  All six birth-noise fields matter, including the zero-characteristic
  quadrupole and transverse modes of the tuned witness.

The 2,401-state complete generator checks both context families and both
rate implementations at three exact points on a biased full-support
product trajectory. They include exact reversal/score, energy, covariance,
noise normalization and noncommuting time-drift controls. Four numerical
groups also check the additive-functional inequality on the complete
growing chain. All raw output is in RUN.log; its one SciPy FutureWarning
is followed by the complete RESULTS.json content and is not suppressed.

The proof supplies finite-mode, finite-time Gaussian convergence and an
L2 approximation by a prelimit stochastic convolution. Deterministic
transport alone has a strictly positive limiting error covariance.
Full-support, fixed horizon/modes/floor and the specified macroscopic birth
scaling remain premises. No empty-state or infinite-dimensional result,
and no audit/retention verdict, is claimed.

Final verification matched all eight unchanged report/seal dependencies,
all 108 successful groups, the full progress log, and the complete JSON
suffix of the raw run log with its warning preserved. PRE_SOURCE_SEAL.json
records the completed source/output identities. The remaining action is
returning the bounded result. No primary comparison, new calculation
branch, publication action or audit is part of this task.
