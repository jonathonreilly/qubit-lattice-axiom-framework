# Bounded exact control plan

Price: at most10 child CPU seconds,45 wall seconds,100MiB observed child RSS,
BLAS/OpenMP1. CPU and wall are actively limited; RSS is measured at return,
not represented as a kernel-enforced limit on macOS. Original deadline and
both STOP sentinels checked immediately before launch. No full torus or
finite-density diagonalization. Only standard-library rational sparse code.

Independent expected identities, prior to execution:
1. Literal pinned S has six diagonal2/3 axial entries and three plane square
blocks diag3/2, adjacent+1/4, opposite0 (mu=1 coefficient).
2. Literal S/W coefficients in the nine physical bond rows reproduce the
real even pair-center Fourier symbol at order0 and2, including both plane
centers. Relative center displacements have l1 norm<=3; per-row absolute
mu/tau coefficients do not exceed3/24.
3. A full small hard-core fixture built from actual signed plane-difference
rows satisfies the density double commutator/second moment identities and
its nested-current N2 lift exactly. Its higher-occupancy remainder must be
exhibited NONZERO, so the test rejects silently discarding that correction.
Analytical all-volume estimates and ground-state spectral claims are not
numerically proved by these controls. Any failed expectation/capture stays.
