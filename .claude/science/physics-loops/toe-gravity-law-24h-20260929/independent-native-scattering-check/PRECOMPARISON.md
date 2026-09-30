# Independent precomparison: the native four-particle threshold

Written before opening the new author's report, evidence or implementation. The only new-route file read is CONTRACT.md. Inputs are the actual `native-stability-route/REPORT.md` operator definitions and SOS, the previously checked native Gram/bands, and the task's disclosure that Q consists of the nonmatching occupation graphs. The following is an independent derivation and a list of hypotheses still to check in a complete exterior construction. It is not an on-shell scattering calculation or a formal review verdict.

## Operator and closed sector

Use physical unordered occupied-site sets, with different-site hard-core b's commuting. The fixed operator is

`H0 = mu N - 2mu sum P_E - mu sum P_T + V3 + W_tau = A + mu D + W_tau`,

where `D(C)=sum_(x in C) (deg_C(x)-1)(deg_C(x)-2)/2` on the eighteen-neighbor graph, and mu,tau are strictly positive. All three terms of the last expression are positive exact local sums. No pair-boson algebra is assumed.

In N=4, a degree is in {0,1,2,3}; D counts vertices of degree zero or three. A four-vertex graph with D=0 has every degree one or two: it is a path on four vertices, a four-cycle or two disjoint edges, hence has a perfect matching. Therefore Q D Q >= Q for nonmatching configurations, and `B=QH0Q>=mu Q`, independently of off-diagonal hopping. This argument is pointwise and survives a fixed-total-momentum fiber.

There is also a crude finite operator bound requiring no enumeration. The SOS identity gives `2 sum P_E+sum P_T <= 2 sum_edges n_x n_y <=12` in N=4. Thus `sum_A,x Q_A†Q_A<=12`. Each gradient square is at most twice the two endpoint squares, so `W_tau<=144tau`. Also `A<=12mu` and `mu D<=4mu`. Consequently

`0<=H0<=M4 I`, with `M4=16mu+144tau`.

This proves bounded self-adjointness in the fixed-number sector and supplies a resolvent certificate:

`B^-1 = M4^-1 sum_(j>=0)(I-B/M4)^j`,

with operator remainder after j=n at most `(1-mu/M4)^(n+1)/mu`. The same construction applies below the closed-channel gap with the appropriate shifted bounds. Its validity does not depend on a numerical spectral extrapolation.

At fixed total momentum zero, translation acts freely on finite four-site sets, so an orthonormal physical basis is one representative per translation orbit. A P configuration with disconnected graph necessarily consists of exactly two disjoint graph edges. Every annihilated edge then leaves the other edge intact; any nonzero creation produces another graph edge. Such a configuration cannot couple to Q. P-to-Q coupling therefore starts only at connected P shapes. A connected four-vertex graph with edge displacements of l1 length two has diameter at most six, so there are finitely many such shapes modulo translation. Thus C=QH0P is finite rank in this fiber. This alone does not make Q finite dimensional.

Eliminating Q at zero gives the exact positive form

`H_eff = PH0P - C†B^-1 C >=0`.

For arbitrary P vector u, the energy at v=-B^-1Cu is `<u,H_eff u>`; completing the square proves this, and gives the exact full-space kernel correspondence. The self-energy is nonnegative and finite rank, but its subtraction need not be a positive interaction relative to free two-pair motion.

## What the free exterior must retain

Far-separated configurations have a unique pairing; near-contact perfect matchings can be multiple and must not be declared orthogonal channels. An exterior reference may use the symmetrized tensor square of the actual N=2 graph-edge sector, with its orthonormal physical pair basis, only after deleting a sufficiently large finite contact region so that the map to four-site occupation sets is an isometry. The pair basis has nine unoriented displacement types (three axial and six diagonal), not merely five collective labels. The remaining four internal states carry energy 2mu. Pair exchange and translation normalization must be fixed explicitly.

The exact non-null soft bands are

`epsilon_E(q)=tau ell(q)`,

`epsilon_Tij(q)=mu(2-S_ij(q))+tau ell(q) S_ij(q)`,

where `ell=2 sum(1-cos q_i)` and `S_ij=1+cos q_i cos q_j` belongs to [0,2]. Vanishing T Gram vectors do not create additional states. Since ell<=12, all nine bands satisfy

`h2(q) >= c ell(q) I`, with `c=min(tau,mu/6)>0`.

For T this follows by minimizing its affine dependence on S between 0 and 2; the high channels have energy 2mu. Thus the full two-pair free symbol at total momentum zero obeys `h_f(q)>=2c ell(q)I`, restricted to the physical exchange sector. Its only zero pocket is q=0. The five soft channels and their proper Gram normalization remain, while all high channels stay in the reference. Breakup and nonmatching configurations are not omitted; they occur in the gapped Q resolvent.

Since dimension is three, `integral_BZ dq/ell(q)` is finite with measure `d^3q/(2pi)^3`. Therefore free compact-source inverse quadratic forms are finite. This says `f in Dom(h_f^-1/2)` for compact f; in general it does NOT say `h_f^-1 f in l2`: a nonzero soft monopole produces a 1/r tail, whose square is not summable in three dimensions. This distinction is essential at threshold.

## A finite-contact criterion for the interacting inverse

The following hypotheses need explicit geometric verification, rather than merely naming asymptotic channels:

1. After removing finitely many relative shapes, the physical P exterior is isometric to the free two-pair reference with a finite set of basis states deleted. The exact exterior block D_e is its Dirichlet compression. Any blocked hard-core pair moves near contact are included in the deleted region.
2. All deviations from that free exterior, and all support of C†, lie in the finite physical contact space J. Its coupling L to the exterior has finitely supported columns.
3. The free fiber normalization and exchange quotient are consistent with the physical occupation inner product; duplicated contact matchings have not introduced extra vectors.

Under these conditions the exterior Green form `G_e=D_e^-1` exists on compact sources. Compression inverse monotonicity bounds it by the full free Green form. More explicitly, the finite-hole Dirichlet Green function is obtained by subtracting the finite matrix correction `G_EF G_FF^-1 G_FE`; G_FF is positive definite because the full free symbol is positive almost everywhere. The matrix-valued inverse symbol is integrable, so its Fourier coefficients tend to zero. The same is true of the finite-hole compact-source Green function.

After Q elimination, write the contact/exterior blocks as `[[A_J,L†],[L,D_e]]`. The exact zero-energy contact criterion is the finite matrix

`S0=A_J-L† G_e L >=0`.

Its positivity follows by approximate minimization over exterior l2 vectors. Invertibility of S0 is the condition needed for an interacting compact-source Green form. Positivity and absence of l2 eigenvectors alone would not suffice: a generic positive three-dimensional operator can have a zero resonance. If S0 is singular, its null vector constructs a decaying generalized zero state with finite form energy, possibly with a 1/r tail. It must be tested rather than silently discarded.

For THIS local SOS operator there is a possible direct exclusion of that decaying resonance, contingent on the physical exterior hypotheses above. For a zero vector of S0, regularized minimizers have total SOS energy tending to zero. Local coefficient convergence and positivity force every local SOS row of the limiting configuration function psi to vanish. Its exterior tends to zero by the free Green argument; its Q part lies in l2 by the closed-channel gap; therefore psi tends to zero on all escaping relative configurations.

To see the decisive constraint, fix the annihilation center at zero and define `q_A(eta)=(Q_A(0)psi)(eta)` for an unordered residual two-site set eta. The fiber gradient squares impose `q_A(eta-e_i)=q_A(eta)`. Along diagonal translations of eta, the associated four-site configurations escape to infinite separation from the fixed annihilated pair. Their amplitudes tend to zero, so q_A is zero. Hence every Q_A annihilates psi. The original normal-ordered expression then gives pointwise `(4mu+V3)psi=0`, forcing psi=0, a contradiction to a nonzero contact component. This would establish S0 positive definite and the compact-source inverse once all contact/exterior details and local limiting steps are verified. It does not assert a spectral gap above zero.

The same argument excludes an l2 zero state in the fiber directly: q_A belongs to l2 of residual coordinates by finite incidence, and a nonzero diagonal-translation-constant sequence cannot be l2. The fiber argument is needed: absence of a normalizable zero state in the full vacuum Hilbert space does not by itself exclude an eigenstate in one total-momentum fiber.

## Threshold relaxation is not an on-shell T matrix

Let Phi represent specified correctly normalized soft pair amplitudes at infinity, with a physical contact extension, such that every SOS row vanishes outside a finite region. Then its row energy E(Phi) is finite and `j=H0 Phi` is compactly supported in the fiber. If the compact-source inverse above exists, minimization over decaying finite-energy corrections gives

`E_threshold(Phi)=E(Phi)-<j,H0^-1 j>`.

This is a threshold quadratic form, with inverse interpreted as a form/energy-space solution. Independence of the contact extension follows by completing the square when two extensions differ by a compact vector. In this particular SOS formulation the affine energy is a sum of nonnegative row norms, so the relaxed form is nonnegative. This reasoning requires checking that Phi really kills the exterior SOS rows, not merely that a projected band eigenvalue is zero. A nonnegative Feshbach matrix alone would not imply a nonnegative interaction amplitude relative to an arbitrary free reference.

Strict positivity in every incoming tensor direction requires more. A zero relaxed affine form yields a bounded generalized SOS zero state with a nonzero incident constant at infinity; the decaying-state argument no longer kills its constants. One needs actual hard-core/contact pin constraints, or an exact finite witness, to exclude it in any claimed direction. Positivity of the unrelaxed quartic pulse and a finite-volume many-body lower bound cannot simply be substituted for this test. I have not assumed strict positivity, a scattering length, elastic-channel normalization or an angular mode count here.

Finally, an on-shell positive-energy scattering operator needs a limiting-absorption argument, appropriate open channels and flux/group-velocity normalization, and control of thresholds or resonances as energy varies. None follows just from the zero-energy inverse form or its finite Schur certificate. No condensate, asymptotic bosonic commutator, phase, cross section or tensor propagation conclusion is imported.
