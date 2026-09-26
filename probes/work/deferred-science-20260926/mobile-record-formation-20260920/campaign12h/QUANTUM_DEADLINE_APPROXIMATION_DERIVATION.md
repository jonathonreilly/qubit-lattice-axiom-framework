# A consistent quantum clock with sharp deadline error

Primary extension, 2026-09-21. The input is the two-parent unknown-qubit
specification of `QUANTUM_WAITING_TIME_DERIVATION.md`. Parents may be disturbed;
no input-correlated preparation register is supplied. This is an approximate
quantum realization of a classical clock under an explicit error metric, not
an exact implementation or an axiom-derived dynamics.

## Input from the separate waiting-law calculation

The independent waiting report, SHA-256
`29b4ae34525945f2272b4c0da3db4ac5640554013d6692cfc982cf3b3a43614b`,
was sealed before accessing primary sources. Its section 2 proves a sharp
binary-observation optimum at a chosen deadline. The report and its entire
checker have been read, and all five sealed artifacts verified. This note
credits that pointwise optimization to the independent calculation. It adds
the simultaneous consistency and complete-deadline optimization below.

For epsilon>0, 0<|j|<1, put x=2 epsilon j^2 t, z=exp(x), r=3/j^2>3,
q=exp(-6 epsilon t)=z^(-r). The target survival on product parents with
dot product u in {-1,0,1} is q exp(-xu). Every quantum binary effect can
be averaged under simultaneous proper cubic rotations without increasing
its maximum row error. Its averaged form is E=alpha I+beta T, where
T=sum_i sigma_i tensor sigma_i, with eigenvalues +1 and -3 on the triplet
and singlet sectors. Hence 0<=alpha+beta<=1 and 0<=alpha-3beta<=1.

The equal-mixture input witness gives error >=q(cosh x-1)/2. Nonnegative
triplet effect implies S(-1)<=2S(0), and hence error >=q(exp(x)-2)/3.
The sharp fixed-deadline error is

delta_*(t) = q (cosh x-1)/2,       1<=z<=3,
           = q (z-2)/3,          z>=3.

The attaining coefficients are

alpha=q(1+cosh x)/2, beta=-q sinh x,        1<=z<=3,
alpha=q(z+1)/3,     beta=-alpha,            z>=3.

The positivity and upper effect bounds are proved in the independent report;
for example the first-interval singlet upper bound reduces to
4z^4-7z^2-2z+5=(z-1)^2(4z^2+8z+5)>=0, using r>=3.
This derivation is a finite-dimensional quantum-effect calculation, not a
claim that a Markov no-event semigroup optimizes the criterion.

## The entire family is a physically consistent survival POVM

Let P_T and P_S be the orthogonal triplet and singlet projectors. The two
attaining survival eigenvalues can be written

s_T(z)=z^(-r)(3-z)(z+1)/(4z),          1<=z<=3,
      =0,                             z>=3;

s_S(z)=z^(-r)(2+7z-5/z)/4,            1<=z<=3,
      =(4/3)z^(-r)(z+1),              z>=3.

Both start at one, are continuous at z=3, and tend to zero. They are
nonincreasing. In the first interval, multiplying the sign-controlling
triplet derivative by its positive denominators gives

r(z-3)(z+1)-(z^2+3)<0.

For the singlet derivative, write r=3+h with h>0. Its corresponding numerator is

-(z-1)(14z+20)-h(7z^2+2z-5)<0  for z>=1.

In the second interval the singlet derivative has sign (1-r)z-r<0.
Thus E_*(t)=s_T(t)P_T+s_S(t)P_S decreases in operator order from I to zero.
The positive operator density -dE_*/dt integrates to I. Its derivative can
jump at the cutoff, but E_* is continuous, so no atom is required there.

An explicit experiment first measures the total-spin sector and then samples
a classical waiting time with survival s_T or s_S as appropriate. This is a
single protocol for all deadlines; it uses no preparation label. It generally
disturbs the parent state. The triplet waiting time has bounded support,
t_cut=log(3)/(2 epsilon j^2), so its conditional hazard becomes unbounded near
the cutoff. We allow an ordinary measured sector and a sampled classical
timer; no bounded, time-homogeneous quantum Markov generator is asserted.

Consequently the pointwise optimum is simultaneously attained for every t.
For the metric

D_K=max_(a,c) sup_(t>=0) |Pr(T>t|rho_a tensor rho_c)-exp[-H(a,c)t]|,

all quantum experiments have D_K>=sup_t delta_*(t), and the above experiment
attains equality. This is a Kolmogorov (deadline) distance. It is weaker than
the full timestamp total-variation distance, whose optimum is not derived here.

## Closed form of the optimum

For 1<=z<=3,
delta_*(z)=(z-1)^2/(4 z^(r+1)). Its maximum occurs at
z_*=(r+1)/(r-1), which lies between one and two because r>3. For z>=3,
z^(-r)(z-2)/3 is decreasing because its derivative changes sign only at
2r/(r-1)<3. It follows that the global optimum is

D_K^*=(r-1)^(r-1)/(r+1)^(r+1),        r=3/j^2.

The maximizing time is

t_*=log[(3+j^2)/(3-j^2)]/(2 epsilon j^2).

At weak coupling D_K^*=exp(-2) j^4/9+O(j^8); changing epsilon only rescales
the clock and does not change this dimensionless error. The bound increases
to 1/64 as |j| approaches one. This boundary limit does not adopt |j|=1 in
the positive-rate model. The optimum concerns survival accuracy across all
promised inputs, not small physical error for every possible future use.

## Matching the initial marked rates as well

The optimal survival family has

-s_T'(0)=epsilon(6+2j^2),
-s_S'(0)=6 epsilon(1-j^2).

These are exactly the eigenvalues of R=sum_b F_b, with
F_b=epsilon(I+j v_b dot sigma) tensor (I+j v_b dot sigma).
Each F_b commutes with Swap, hence with R. Set Q_b=R^(-1/2)F_b R^(-1/2).
These are positive and sum to I, with no cross-sector blocks. Following the
initial sector measurement, perform this POVM within that sector to select
a mark, independently of its subsequently sampled sector-conditioned timer.
The complete joint marked-time effect density is

G_b(t)=sum_(s=T,S) [-s_s'(t)] P_s Q_b P_s.

It is positive, sums and integrates to I, and G_b(0)=F_b. Thus the optimal
whole-deadline protocol also reproduces every initial marked rate. Its marks
and waiting time over a finite interval need not match the stipulated
classical joint process. This supplies a positive approximate-clock witness;
it does not repair the exact history incompatibility.

## Primary verification and remaining obligation

The monotonicity, global metric optimum and marked extension are new primary
arguments subsequent to the independent pointwise calculation. The primary
checker now verifies the symbolic derivative and normalization identities,
seven parameter cases with 1,002 deadlines each, the closed-form optimum
against direct scalar maximization, and all six marked initial effects per
case. The largest pointwise error-formula residual is below 3.34e-16. Complete
results and source identities are in `QUANTUM_DEADLINE_RESULTS.json`.
Selective independent scrutiny is still needed before publication. Do not
count the previous report as coverage of these added claims.
