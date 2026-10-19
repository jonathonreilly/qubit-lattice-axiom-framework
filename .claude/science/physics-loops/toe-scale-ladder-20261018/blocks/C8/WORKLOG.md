# C8 worklog (lattice Sakharov coefficient for the supplied two-qubit Dirac walk)

## Pre-registration (written BEFORE any coefficient was computed)

**Observable.** Static vacuum (Dirac-sea) quasienergy of the walk, E_vac = sum of the
negative eigenvalues of the walk generator H_a (C7 Theorem A: U = exp(-i a H_a), valid
where f > -1). For a static background field of wavevector q and amplitude lambda,
E_vac = E_0 + lambda^2 E2(q) + O(lambda^3). The induced-gravity number is the O(q^2)
Taylor coefficient of E2(q) per unit volume, in the spin-2 (TT) channel.

**Metric coupling (SUPPLIED PREMISE M, not derived).** Static spatial metric
gamma = 1 + h, lapse N = 1, shift 0, symmetric triad e = gamma^(-1/2) = 1 - h/2 + 3h^2/8.
H_a(k) = alpha_j P_j(k) + Phi(k).tau with P_j = rho(f) g_j, rho = arccos f / sqrt(1-f^2).
Primary coupling M1 ("frame coupling of the generator"): the spin-frame (Clifford
vector) part is contracted with the triad at the link midpoint,
  H_h = sum_{x,n} psi^dag_{x+n} [ alpha_b e_b^i(x+n/2) A^i_n + S_n ] psi_x,
where A^i_n, S_n are the Fourier coefficients of P_i(k), Phi(k).tau. In momentum space the
vertex between k and k+q is the symbol at the midpoint k+q/2. The flavour (Wilson) part
is a spatial scalar and is not modulated (only the measure, which is trivial at O(h) for TT).
Variants (same continuum limit, different UV; computed to expose non-uniqueness, NOT to
select one): M2 current P_j -> g_j (bare walk amplitude, no rho); M3 current -> s sin k_j
(naive nearest-neighbour); M4 full-symbol deformation V = -(1/2) eps_ij sin(k_j) dH/dk_i
(also couples the Wilson sector).
Lapse diagnostic L1: H_N = midpoint-quantised N(x) H_a; L2: (1/2){N, H_a}.

**Normalisation fixed in advance.** E_EH = -(1/16 pi G) int sqrt(gamma) R^(3) (static, N=1),
and for TT h: int sqrt(gamma) R = -(1/4) int (d h)^2 + O(h^3) (to be checked symbolically).
With h = 2 lambda eps cos(q.x), eps TT, eps:eps = 1: E_EH = (1/32 pi G) lambda^2 q^2 Vol.
Define c_G := a^2/(16 pi G_ind) per walk (one IR Dirac fermion), c = 1 units (tau = s a).
Then c_G = 2 * [q^2 coefficient of E2/(Vol lambda^2)] / s in lattice units.
a/l_P = sqrt(16 pi N_f c_G).

**Comparison criteria (declared before computing).**
1. Sign (decisive): c_G > 0 is required for attractive induced gravity. c_G <= 0 in the
   primary coupling M1 at b* or b_iso is reported as a failure of the Sakharov route for
   this walk/coupling, not repaired.
2. Continuum reference: proper-time heat kernel, one Dirac fermion,
   1/(16 pi G) = Lambda^2/(96 pi^2) (derived in NOTE; the repo note's 1/48 pi^2 omits the
   1/2 of det D = det(D^2)^(1/2)). Report Lambda_eff a = sqrt(96 pi^2 c_G) and its ratio to
   pi (BZ edge). "Same order as the cutoff estimate" means ratio in [0.1, 10]. No target
   value for c_G is used anywhere; nothing is tuned.
3. Isotropy: report the TT channels separately (q || z with Eg and T2g polarisations,
   q || (111)); the spread is a result.
4. Lapse diagnostic: covariance predicts zero O(q^2) lapse stiffness; report the lattice value.
Independent checks planned: (i) exact diagonalisation on a finite periodic lattice of
H_a + delta H (block-chain in k) vs the second-order formula on the same k grid;
(ii) q -> 0 limit vs direct second derivative of the homogeneous-deformation vacuum energy.

## Log
- 00:40Z c8_exact.py run 1: 11/1. The failure was E2 (minimal coupling): I wrote the
  spin connection with the (+,+,+) sign, Gamma_i = +(1/8) omega_i^a_b [gamma^a, gamma^b],
  while the gammas here satisfy {gamma^a, gamma^b} = -2 delta (signature +---). Lowering
  the frame index flips the sign. With the correct sign the identity holds exactly
  (residual 0); with the wrong sign a non-derivative residual ~ (dh) psi remains. Run 2: 12/0.
