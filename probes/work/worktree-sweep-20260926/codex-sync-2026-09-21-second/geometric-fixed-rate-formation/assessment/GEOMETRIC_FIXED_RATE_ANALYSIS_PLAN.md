# Fixed-rate formation: statistics and a conditional Gaussian comparison

2026-09-21. Author analysis specification, written while the declared 2496-run
experiment is running and before inspecting its production observable values.
The earlier nine-case pilots and eight-seed screen have already been seen.
This adds explicit definitions for the protocol's moment and ratio diagnostics;
it does not change the formation rule, cases, primary observables or exclusions.

Each completed history is one statistical unit. Its first axis shell contains
three non-conjugate wavevectors and its transverse power per polarization is
averaged within that history before estimating uncertainty. Winding power is
sum_i Phi_i^2/(3N). Cases that fail or reach the event cap are reported, not
silently replaced by new seeds. If any cell is censored, its completed-case
statistics are explicitly conditional on completion under that cap.

For every (N,beta) cell report the number completed, means and 95% pointwise
percentile bootstrap intervals from 10000 resamples of whole histories for:

* first axis-shell transverse power;
* winding power per component;
* ratios of mean shell2, shell3 and shell4 powers to mean shell1 power;
* ratio of mean winding power to mean shell1 power;
* mean total filling time divided by volume and mean slide count per site;
* fraction of sites with multiple birth events.

Use a fixed independent NumPy generator seed, 2109211530 plus the cell index
in lexicographic (N,beta) order. Retain the full per-history sufficient
statistics and analysis-source hash. Ratios are ratios of cell means, not
averages of the often noisy individual-run ratios. Intervals are descriptive,
pointwise and conditional on the generator; they are neither simultaneous
coverage statements nor a bound on finite-volume bias or simulator error.

Also report three dimensionless fourth-moment diagnostics, using the same
whole-history bootstrap:

    E[mean_axis(ST_mode^2)] / E[mean_axis(ST_mode)]^2,
    E[(mean_axis ST_mode)^2] / E[mean_axis ST_mode]^2,
    E[W^2] / E[W]^2.

Their conditional reference values are 3/2, 7/6 and 5/3 for an isotropic
Gaussian transverse field whose distinct non-conjugate modes and three real
winding components are independent, with common infrared variance. These
numbers follow from two complex transverse polarizations per nonzero mode,
three non-conjugate first-axis modes, and three real winding components.
The finite lattice has integer windings and need not have these laws.

Under that same *additional equilibrium Gaussian hypothesis*, the mean
nonzero-mode transverse power and W approach the same constant; shell ratios
approach one. Testing those relations is useful because exact microscopic
Gauss law alone does not impose Gaussian statistics, isotropic stiffness,
or equilibrium weights across topological sectors. Agreement would support
a candidate long-distance description over the simulated sizes. It would
not prove a Coulomb phase, a uniform matching law, a thermodynamic limit,
Maxwell dynamics, or a quantum identification.

No fitted asymptotic exponent or critical threshold is a primary result.
Any later fit or unplanned diagnostic must be explicitly exploratory.
