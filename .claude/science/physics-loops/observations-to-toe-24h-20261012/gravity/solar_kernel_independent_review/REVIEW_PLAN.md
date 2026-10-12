# Independent positive solar-kernel review

The frozen source is `gravity/solar_kernel_inversion/POSITIVE_RESPONSE_DERIVATION.md`
(`bfdeb9774193234308dd61ce25b68b30e35f25aa3b87d4f0fdb8357801d1c755`)
and `positive_kernel_check.py`
(`e87e53c00aa7c4a94017db5c46a1b6971c298f07a5a2d72c6d76c1c85d7365f9`).
The complete source and earlier Poisson derivations have been read. Previously
published target summaries and the author's numerical summaries are exposed.
This is an independent mathematical source review, not a blind prediction,
empirical fit, novelty search or formal audit verdict.

Before calculating, freeze these checks: independently derive the Poisson
Hessian convention, variable-change determinant and integration region;
differentiate the primitive; verify both branches of K and W, rationalization,
reciprocity, endpoint orders, monotonicity and interval inequality. Inspect
origin, infinity and zero-field saddle boundaries under the stated regularity.
Separate the Green solution from freely added harmonic tides.

Numerical checks will use an independently reconstructed direct phantom-source
integral in physical radius or an independently regularized angular coordinate,
plus a smooth-response control whose derivative is compactly supported. The
compact-support control can independently reconstruct W from its signed K
primitive and tests the lower bound without the exposed exponential response.
Parameter choices are diagnostics, not fits: eta = 0.5, 1, 2, 3, 4 for the
known response; compact derivative supports [0.3,0.8], [0.8,1.2], [2,5] at
eta=1; constant nu=1 is an exact null control. The midpoint threshold s=1 is
split explicitly. No empirical acceptance threshold or new parameter is fit.

Run the exact author checker with explicit runtime output; record finite
diagnostics separately from proof. Preserve failures and mutated artifacts.
The independent checker must accept explicit input/output paths, avoid expiry
and author-output overwrites, and record library versions and exact source
hashes. Campaign limits and stop/deadline checks belong in the execution wrapper.
