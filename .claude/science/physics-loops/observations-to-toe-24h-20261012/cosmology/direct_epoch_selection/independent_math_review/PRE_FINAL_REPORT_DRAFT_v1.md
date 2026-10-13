# Independent mathematical check: radiation and dust limiting systems

## Disposition and exact scope

The equations, fixed points, both dust Jacobians and characteristic polynomials, radiation radial modes, and transverse field exponents in the current epoch note agree with an independent derivation from the stated three-field analytic action. **The original missing transverse-velocity restriction is a real domain omission; the separately preserved v2 correction closes it.** No algebraic correction is required in the displayed limiting systems or their stated linear classifications.

This conclusion concerns the handwritten mathematical source. It does not review the parent's subsequently completed epoch implementation or its reported 194-check execution, establish finite-era convergence, select observed fluid abundances, certify a no-go packet, or perform a formal audit/publication gate. The parent remained the theory/implementation author. The reviewer independently reconstructed the equations and checked the proposed claims without importing parent code or using another review as positive evidence.

Source identities:

| Source | SHA-256 |
| --- | --- |
| Original epoch hand derivation v1 | `bafa1e27b87f79b0e1e94917127b5f27060febcf09eda73160290e9a3dda344d` |
| Current epoch hand derivation v2 | `504d273484b5596e61b931214c68bb2561ea2117ceac10bcd717efaf25ee7f99` |
| Imported analytic-action hand derivation v2 | `322a932eef3de5de4d963aae2c623693d12a5942828f971335cc7a6c03ef7d2` |

The complete bytes of all three notes and the parent's domain-correction receipt are retained in the review snapshot. All three notes and the correction were read completely. The original and corrected epoch notes have identical text from the dust-system section onward, including all 24 indented equation lines. Only the limiting-domain paragraph changed. The final exact-source receipt supplies the authoritative full hashes, paths and final unchanged-source checks.

## Independent starting equations and normalization

The imported action has field term -2 K_AB partial(phi^A) partial(phi^B)-4V, divided by 16πG_*, and universal matter metric exp(2sqrt(a)u)g. This normalization gives the scalar force K^AB(V_B+alpha_B sigma), with alpha=(sqrt(a),0,0) and sigma=4πG_*rho_m. There is no extra factor of two multiplying V_B. For ideal radiation r=4πG_*rho_r, its trace vanishes, so there is no direct u force from radiation.

For Einstein e-fold time N and p=dphi/dN, direct use of the canonical Friedmann and Raychaudhuri equations gives

  H² = 2(sigma+r+V)/(3-K_AB p^A p^B),
  h = -(sigma+4r/3)/H²-K_AB p^A p^B,
  p_N^A = -(3+h)p^A-Gamma^A_BC p^B p^C
           -K^AB(V_B+alpha_B sigma)/H².

The reviewer independently computed all Christoffel symbols by differentiating the metric, rather than importing the note's listed coefficients. With D=1+c(x²+y²), c=2(1+a)/3, the metric is diag(1,4a/(9D),a/(3D)). There are eight nonzero ordered x/y Christoffel entries, including their symmetric duplicates; all u entries vanish. They agree with the imported action note.

The exact symbolic program sets H_v=1 as a choice of units. Every reduced variable and eigenvalue in this review is dimensionless and expressed in Einstein N, so this does not alter a limit or discard a physical parameter. The constant potential, the nu restoring force and all finite-x/y corrections remain in the full equations before taking limits.

## R1-domain: why the original reduction required correction

In v1, the dust paragraph required y/x→0 but did not require y_N/x→0. This is insufficient: K_yy y_N² can remain of leading order even when the transverse field amplitude vanishes.

An exact family of admissible instantaneous states makes the omission concrete. Set a=1, U=V=0, P=-3/2, W=1, x=t→infinity, y=0, y_N=t/5 and r=0. It satisfies the original amplitude/density restrictions and finite u,u_N. The full action gives

  F → 75/56,      P_N → -3/100,

where the proposed dust reduction without a velocity restriction would give F=4/3 and P_N=0. The surviving transverse kinetic term is beta_r/25, and the connection term also contributes. These values were derived exactly by the independent symbolic program. This is a counterexample to the originally stated vector-field limiting domain, not a counterexample to the corrected dust equations.

The parent preserved v1 and wrote v2 before the parent epoch execution. V2 now requires y_N/x→0 in the dust limit and x_N/y→0 in the radiation limit, finite reduced variables, and a positive limiting Friedmann denominator. It also restricts uniform comparisons to compact sets away from the zero-denominator boundary. The invariant dust subspace y=y_N=r=0 is correctly identified as sufficient. Those changes remove the counterexample and provide the appropriate domain for the displayed reductions.

The corrected radiation radial calculation additionally restricts u_N=0 with finite u. At finite fields a nonzero constant u generally feels the nu restoring force; its neutral direction is a feature of the limiting system where nu/H² vanishes. The note explicitly treats this as an asymptotic reduction, so it is not claiming an exact finite-y invariant plane at every fixed u.

## Dust autonomous system from the full action

Use U=u/sqrt(a), V=U_N, P=x_N/x, W=sigma/(H_v²x²). On the corrected dust domain,

  K_xx x² → beta_m=2a/[3(1+a)],
  V_potential/(H_v²x²) → a(1/2-U+2U²).

The transverse kinetic and source terms vanish under the corrected restrictions. Transforming x_NN to P_N=x_NN/x-P² is essential: the leading Gamma^x_xx=-1/x contribution cancels this P² term. Direct limiting of the full action therefore yields exactly the note's F, h and four-component system. In particular,

  W_N=W(-3+aV-2P),

because sqrt(a)u_N=aV. Replacing this factor by sqrt(a)V would be a normalization error; the proposed source has the correct factor.

Both listed equilibria are in the physical reduced domain:

| Equilibrium | (U,V,P,W) | F | Limiting Friedmann denominator |
| --- | --- | --- | --- |
| E0 | (0,0,-3/2,1) | 2(1+a)/3 | 3(a+2)/[2(a+1)] |
| E1 | (-1/2,0,-3/2,3) | 2(1+a) | 3(a+2)/[2(a+1)] |

For each finite a>0 the denominator is positive. Both have h=-3/2. The independent derivative of the complete limiting vector field reproduces every entry of both proposed 4×4 Jacobians. Their determinants and characteristic polynomials agree exactly, not only at sampled parameter values.

Writing d=1/(1+a) and z=lambda(lambda+3/2), the E0 characteristic polynomial is

  z²+[(21+3a)d/2]z+(27/2)d².

Its z-discriminant is

  (9a²+126a+225)/[4(1+a)²] > 0.

The two z roots have negative sum and positive product, so both are strictly negative. For each, lambda²+(3/2)lambda-z has negative-real-part roots. Thus all four eigenvalues have strictly negative real part for every fixed finite a>0: E0 is a hyperbolic sink of this four-dimensional limiting system. This also permits the usual local asymptotic-stability conclusion for the smooth limiting ODE itself; it does not transfer that conclusion to a finite-duration era of the full theory without further comparison.

For E1 the polynomial is

  z²+[(13+3a)d/2]z-(9/2)d².

The z product is negative. Exactly one z root is positive; its lambda pair contains one positive real root and one negative root. The other z root gives two roots with negative real parts. E1 therefore has exactly one unstable direction in the four-dimensional limiting system. This is fully compatible with future vacuum convergence in the full action: the large-field dust approximation is not its late-vacuum asymptotic system.

Neither the two verified equilibria nor their local classifications were used to claim an exhaustive list of all fixed points or trajectories. The reduced coordinates also remove the absolute x amplitude; selecting a relative ratio W does not predict the observed matter abundance or an absolute epoch normalization.

## Radiation radial subsystem and u modes

On the restricted radiation subspace, K_yy y²→beta_r=a/[2(1+a)]. Limiting the full equations and using P=y_N/y and W=r/(H_v²y²) gives the proposed two-dimensional vector field. At (P,W)=(-2,1), F=c, h=-2 and the limiting denominator is (a+3)/(a+1)>0.

The independent Jacobian is

  [[-1, 2/(1+a)], [-2, 0]],

so its characteristic polynomial is lambda²+lambda+4/(1+a). Its roots are precisely

  lambda = [-1 ± sqrt(16Omega-15)]/2,
  Omega=a/(1+a).

They have negative real parts for each fixed finite a>0. At a=15 the root is repeated at -1/2 and the 2×2 matrix is not diagonalizable; a polynomial N prefactor can occur, but decay and the sink classification remain valid. For a<15 the modes are a complex pair; for a>15 they are real and negative. No decay rate uniform over unbounded a is established or implied.

The independent full-equation u linearization in the radiation limit is u_NN+u_N=0. Its constant and exp(-N) modes agree with the note. Consequently the radial sink does not select the conformal field value. At finite y the retained nu term acts again; its eventual effect must be followed with the full coupled equations.

## Transverse field exponents and curved-metric terms

The reviewer linearized the full field equations before taking the dominant-field limit. This avoids treating an amplitude equation as a canonical Cartesian-field equation or silently dropping connection terms.

At the constructed radiation solution, y_N=-2y and h=-2. In the x equation the mixed connection adds 4x_N and Gamma^x_yy y_N² adds 3x. The bare force contributes (9/4)x. Therefore

  x_NN+5x_N+(21/4)x=0,

with roots -3/2 and -7/2. At dust E0, x_N=-3x/2 and h=-3/2. The y mixed connection adds 3y_N, the transverse connection adds 3y and the potential force adds 2y. Thus

  y_NN+(9/2)y_N+5y=0,

with roots -2 and -5/2. Both total polynomials were checked by exact differentiation of the full metric-based operator. Removing the connection contributions would change the damping and stiffness in both cases.

These are signed field-amplitude modes in Einstein N. They are not directly eigenvalues of fluid-density fractions or of the full combined era-selection problem. In radiation domination, x∝exp(-3N/2) decays absolutely while x/y∝exp(N/2) grows relative to y∝exp(-2N). Similarly, at constant u a dust/radiation density ratio grows as exp(N). The radial radiation sink is therefore not a statement that every homogeneous perturbation is attracted to a forever-radiation history. This interpretation is consistent with the note's explicit subspace restriction and its warning that density/amplitude perturbations still require the full system. In the dust limit the two y/x modes decay as exp(-N/2) and exp(-N), but that by itself is still not a finite-era history-selection theorem.

Negative forward-N eigenvalues within a limiting model also do not establish a primordial initial-condition selection mechanism. On the constructed curve x and y decrease as N increases, so a finite physical history eventually leaves the large-field regime. The draft correctly leaves transition/equality behavior, finite-era attraction and observed amplitude selection for subsequent work.

## Controls, reading record and execution history

`derive_limits_v1.py` is reviewer-owned and reconstructs the metric connection, the full N operator, the limiting equations, all fixed-point residuals, all Jacobian entries and characteristic polynomials, the transverse coefficients and the velocity-domain counterexample. It imports no parent implementation. The recorded run completed in 4.0281 seconds with **73 exact symbolic identities and 21 high-precision matrix-eigenvalue controls passing; zero failures**. The matrix checks use seven finite positive a values, including the radiation critical value a=15. They supplement the analytic all-a sign argument rather than replace it.

Reviewer source SHA-256: `50f34b43ec526036d06fac66ca1b8fadc47cb78af55fd7f414685e3bc0b587c6`. The complete raw stdout, empty stderr, execution receipt, derived expressions, eigenvalue samples and source pins are preserved. There were no mathematical-program execution failures.

After the result was reported, the parent reported a stream disconnection and requested continuation from preserved files. This is recorded as a parent-reported communication interruption, not an independently observed science-execution failure. The checker output and snapshots were intact; no derivation was restarted and no result was replaced. The parent also reported a subsequent 194-pass epoch execution. Its code and evidence are outside this assigned mathematical check and were not read or evaluated here.

The only actual source finding was the v1 limiting-domain omission, documented with a concrete full-equation counterexample and preserved before the v2 correction. The final receipt binds all original/current source notes, the correction, reviewer code, complete outputs, exact source delta and this full report. This mathematical scope is complete for the pinned v2 note; implementation and finite-era claims remain separate work.
