# Independent Gaussian benchmark before analysis-code/results access

2026-09-21. Only the complete adaptive diagnostic plan has been read for this
new unit. Previously sealed sampler construction and compact-data checks are
available unchanged; the new squared-flux script/results have not been opened.

Use orthonormal Fourier amplitudes Etilde=Ehat/sqrt(V). For Gaussian weight
exp[-K sum_x |E(x)|^2/2], conditioning a nonzero-symbol mode to be transverse
gives Cov(Etilde)=K^-1 P_T, with trace 2/K in three dimensions. Therefore
the recorded S_T=|Ehat|^2/(2V) has mean 1/K. The zero mode has no Gauss
constraint and three independent components of variance 1/K. Since
F_i=sqrt(V)Etilde_i(0), E[F_i^2]/V=1/K, giving the stated global/local ratio
one. The numerical boxes are odd and the four selected nonzero modes have
nonzero centered-divergence symbol; extra even-volume corner zeros do not
enter this normalization.

On an odd L torus, charge edges take steps +/-2e_i. A closed cycle has
2 sum steps_i = L times an integer winding. Odd L forces that winding even,
so F_i=L W_i, W_i integer. This formula is not the unrestricted even-torus
flux quantization. The Gaussian zero-mode cost is K F_i^2/(2V)=K W_i^2/(2L).
Thus with local stiffness proxy S=1/K, the discrete Gaussian has variance
parameter sigma^2=L S and weights exp[-W^2/(2sigma^2)]. Its global/local ratio
is E[W^2]/sigma^2, not E[W^2]/S or E[W^2]/L alone.

Poisson summation gives exactly, with r_n=exp[-2pi^2 sigma^2 n^2],

  d(sigma^2)=1-4pi^2 sigma^2 (sum_n n^2 r_n)/(sum_n r_n).

For finite positive sigma^2 this is below one. With r=exp[-2pi^2 sigma^2],

  0 < 1-d <= 8pi^2 sigma^2 r(1+r)/(1-r)^3.

Here n^2>=n bounds the positive-n numerator by sum n^2 r^n, and the
Poisson denominator is at least one. This supplies an explicit small
quantization bound when the distribution is broad. It applies to the
added Gaussian sector benchmark; neither the record ensemble's winding
sector entropy nor a Gaussian effective free energy has been derived.
Capacity bounds and other effective corrections are outside this benchmark.

The estimator must first square each raw F_i, then average within each
1024-visit block. Squaring an existing block-mean F_i would underestimate
it. The local statistic is the equal mean of four S modes, each already
normalized by 2V; the global statistic is the equal mean of three F_i^2/V.
For paired block resampling the reported ratio should be a ratio of jointly
resampled means, not a mean of per-block ratios or independently resampled
numerators and denominators.

Uncentered moments are appropriate to this stated inversion-symmetric grand
benchmark. The empirical mean F_i/sqrt(V) is an independent finite-run
diagnostic, not something to set to zero or subtract silently. A finite
run can nevertheless miss the target even with small mean. Sixteen blocks
is only a display threshold. Adaptive reuse of eight trajectories, unknown
between-block dependence and multiple diagnostics prevent treating an
interval narrowly excluding one as a calibrated rejection of the benchmark.

This stage has not inspected whether any particular recorded interval excludes
one. Full results and source identities will be compared only after this seal.
