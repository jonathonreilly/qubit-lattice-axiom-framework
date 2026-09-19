kernel-by-predecessor-set, independent run 1 of 2
worker w-jonathonsmac4f50-j82d3 (claude-opus-5), unit C-kernel-by-predecessor-set-a1

MODEL
  theta_{t+1}(x) = |P|^-1 sum_{p in P} theta_t(x + p) + noise
  kernel         = sigma^2 / (1 - |phi|^2),  phi(k) = |P|^-1 sum_p e^{ik.p}
  E(k)           = sum_i 2(1 - cos k_i)
  F              = E / (1 - |phi|^2), so that kernel = F sigma^2 / E

GENERAL FACTS (exact, in run.py)
  small-k form: 1 - |phi|^2 = k^T M k + ..., with M = Cov_P(p)
  drift: the linear term of Im phi is k . mean(P)
  zeros of 1 - |phi|^2 are the k with every e^{ik.p} of equal phase,
    i.e. k in 2 pi (Lambda_P)^*, where Lambda_P is the lattice spanned by P - P;
    run.py enumerates them exactly using the index of Lambda_P in Z^3

TABLE
Columns: set | isotropic | drift = mean(P) | doublers (k/pi) | F range
(a) site + 6 neighbours
    isotropic: yes, M = 2/7 I
    drift: none
    doublers: none (index 1)
    F: exactly 49/(14 - E), in [7/2, 49/2]
(b) 6 neighbours only
    isotropic: yes, M = 1/3 I
    drift: none
    doublers: (1,1,1) (index 2)
    F: exactly 36/(12 - E), unbounded
(c) site + 6 + 12 face diagonals
    isotropic: yes, M = 10/19 I
    drift: none
    doublers: none (index 1)
    F: small-k 19/10; at the corners 361/90, 361/42, 361/26; grid range [1.901, 13.885]
(d) 8 cube corners
    isotropic: yes, M = I
    drift: none
    doublers: all 7 nonzero corners of {0,1}^3 (index 8)
    F: unbounded
(e) {0, e1, e2, e3}
    isotropic: no, eigenvalues 1/16 along (1,1,1) and 1/4 across
    drift: (1/4, 1/4, 1/4)
    doublers: none (index 1)
    F: small-k 16 and 4; grid range [4.002, 16.000]
(f) {0, -e1, -e2, -e3, e1+e2, e2+e3, e3+e1}, this run's choice
    isotropic: no, eigenvalues 2/7 and 32/49
    drift: (1/7, 1/7, 1/7)
    doublers: none (index 1)
    F: small-k 7/2 and 49/32; grid range [1.535, 25.508]

Corner values are at (pi,0,0), (pi,pi,0), (pi,pi,pi).
Grid ranges are numerical (97^3 points); everything else is exact.
The task does not fix set (f). This run takes the site, the three backward neighbours and the three forward face diagonals, a set with no inversion symmetry.

CLOSED FORMS (exact)
  (a) phi = 1 - E/7, so kernel = sigma^2 * 49 / ((14 - E) E)
  (b) phi = 1 - E/6
  (d) phi = cos k1 cos k2 cos k3, so |phi| = 1 exactly on {0, pi}^3

READING
The expectation holds:
  The cube-symmetric sets containing the site, (a) and (c), give isotropic, drift-free, doubler-free kernels.
  Their kernels are within bounded factors of 1/E: 7/2..49/2 for (a) and 1.9..13.9 for (c).
Refinement of the doubler remark:
  (b) has exactly one doubler, at (pi,pi,pi).
  (d) has seven: phi = -1 at every nonzero corner of the zone, for example (pi,0,0) as well as (pi,pi,pi).
The sets without inversion symmetry, (e) and (f), drift along (1,1,1) and are anisotropic, but are doubler-free.
