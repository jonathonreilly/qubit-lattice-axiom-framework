# Equilateral source correspondence v1

Date: 2026-10-15. Reviewer: /root/localized_history_check. Root remains scientific author. This is a focused correspondence report, not a formal audit or a landing decision. The independently frozen mass-order proof, implementation, 120-control result and report are preserved unchanged.

## Sources and extent read

I read all 146 lines of MASSIVE_REFINEMENT_WORKING_v1.md, all 126 lines of massive_refinement_controls_v1.py, and the result JSON. I did not execute or import the author script. The scope of the present correspondence is the triangle clock example, its temporal profile/limit and the implementation evidence claimed for them. The broader moving clock/force operator-distance derivation and its conservative suppliers were read for context; this report is not an independent validation of every estimate in that derivation.

## General kernel and triangle

My earlier independent derivation, frozen before either author source was opened, gives, for real data and N=int(p^2+|grad h|^2+mu^2 h^2),

  G_mu = (1/(2 pi^2)) int_mu^infinity (k/omega)
           sum_AB Re(C_A(omega) conjugate(C_B(omega))) sinc(k r_AB) d omega,
  k=sqrt(omega^2-mu^2), C_A(omega)=int c_A(t) exp(i omega t)dt.

This is the squared energy dual norm for the same physical temporal weights. There is no extra real-data factor of two. Changing mu changes both k/omega and every spatial sinc argument. The latter change cannot be omitted when comparing masses.

For three equal positive profiles at an equilateral triangle of side r, the spatial density is 3v+6 sin(v omega r)/(omega r), v=k/omega. With omega_0 r=pi, v=2/3 and mu=sqrt(5) omega_0/3, this is 2+3sqrt(3)/pi, while the massless value is 3. The ratio is

  2/3+sqrt(3)/pi = 1.2179955620884586... > 1.

It agrees exactly with the author's section and code. It is a second concrete noncollinear construction compatible with my earlier, different three-point counterexample. It does not contradict single-point or collinear-point ordering, and does not establish mass reversal for the special two-body coherent clock-plus-force count fixture.

## Compact smooth limit

For any nonzero real psi in C_c^infinity, c_T=partial_t[psi(t/T)sin(omega_0 t)] is real, smooth, compact and has exactly zero integral. Its transform is -omega/2 times the difference of the two shifted transforms T psi_hat(T(omega+/-omega_0)). On the positive frequency half-line, |C_T|^2/T concentrates at omega_0, with positive mass proportional to omega_0^2 ||psi||_2^2. The other peak is on the negative half-line, as required for real data. Because the spatial densities are bounded and continuous near omega_0>mu, rapid decay of psi_hat controls the complement and the quotient of the two Gram integrals tends to the displayed density ratio. Consequently sufficiently large finite T gives a compact C-infinity, zero-clock-integral counterexample. This is an existence argument, not a numerical identification of its smallest admissible T.

## Implementation correspondence and qualifications

The code's chat is the exact transform of the derivative of cos^2(pi t/(2T)) sin(t) on [-T,T], extended by zero. Its sign and Fourier normalization agree with the integration-by-parts formula. The cutoff implementation correctly zeros the density below omega=mu, resolves a spectrum of width 1/T, and uses the correct equilateral distances. The 3D angular check sums the three spatial phases before squaring, retaining interference; its target is the same factor derived above.

The numerical profile is not C-infinity across the support boundary. For the T values chosen in the script (integer multiples of pi), its zero extension is C1, with higher derivative jumps. It is still an admissible compact L2 clock weight, and the note's separate arbitrary smooth-envelope argument proves the C-infinity existence statement. These two roles must remain distinct. The result already labels the finite calculations as diagnostics rather than as the smooth existence proof.

The stated high-frequency tail supplier follows from the real-profile Parseval identity int_0^infinity omega^2 |C|^2 d omega=pi ||c'||_2^2, the density bound 0<=S_mu<=9 and the conservative derivative estimate shown in the code. The difference between two quadrature orders is not a rigorous quadrature error certificate. The computed finite ratios therefore remain diagnostics as labeled. No universal monotonicity assumption is used by this triangle argument. The code's zero-offset small-mu rate controls test the displayed bound formula, not a measured mass/energy and not the separate full proof of that bound.

The recorded author result contains 13 controls and matches the frozen script/note identities. Its triangle ratios are 1.2012343444691058, 1.2138855113228115 and 1.2169725245282104 at T=10pi,20pi,40pi. The pointwise angular factor is 3.6539866862653803 versus the analytic 3.6539866862653763. Those are author-executed diagnostics; I did not rerun them or count them as new independent controls. The 120 controls of my preceding independent counterexample remain separately identified.

## Scoped conclusion

No discrepancy was found between the author's equilateral formula/limit and my independently derived general energy kernel. The implementation uses the correct interference factor and records its finite numerical scope. The finitely differentiable numerical envelope qualification above should survive any canonical summary. Neither this example nor my earlier counterexample selects a physical field, observed geometry, action, mass, energy budget or measurement map. No formal audit verdict is applied.

## Exact identities

All author paths in this section are relative to the physical_bridge directory. Prior independent paths are relative to independent_mass_order_v1. Full paths are in the identity sidecar.

- Author `MASSIVE_REFINEMENT_WORKING_v1.md`: `448ec6ee42a4ae27c087cc05efcf940f047054228862be8fd76952c7493ce6bb`.
- Author `massive_refinement_controls_v1.py`: `9674ee5a3ec50361df27f4a63e723931085b9cae2d1dbbbc7418fe8d77a7f451`.
- Author `MASSIVE_REFINEMENT_RESULTS_v1.json`: `a92e03d28c8008d0c501a098c8b52455aa36b1afacd2c3c20baba92361092c74`.
- Prior independent `MASS_ORDER_PRECHECK_v1.md`: `30518157177387a7d90d3c218a638ae78aa30fb8cfbab310f663d34076c3fb51`.
- Prior independent `independent_mass_order_check_v1.py`: `3d60a7a1a45fba1aefe5b532e880d2d6bf43c3c464e27fea03bda32bba09012b`.
- Prior independent `INDEPENDENT_MASS_ORDER_RESULTS_v1.json`: `547625d491ed9c6a2d8f2f41b406c8db13246f95f0c1c1dfd5244c79eac66bbe`.
- Prior independent `MASS_ORDER_REVIEW_v1.md`: `355fa24cbf0632a586139597b7505537d3c0783eb617f1035cdb42435478129e`.
- Prior independent `MASS_ORDER_REVIEW_IDENTITY_v1.json`: `d8f05bbf1646acd90ca15da69d9429c51e61284f32beb7b178dec2d6b697c8a6`.
