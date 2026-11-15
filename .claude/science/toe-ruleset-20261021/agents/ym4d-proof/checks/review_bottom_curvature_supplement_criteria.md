# Supplement criteria, before implementation

The first independent source and scalar runs have completed with 61/61 and 26/26 predicates. No author-checker code has been inspected. All original thresholds and outputs are retained. This supplement addresses a limitation of the first source check: its q was reconstructed from w2, so the Euler/Hodge consistency alone could be self-confirming.

Independently obtain each top-current component by evaluating the trilinear cubic on three separately solved linear lifts with momenta p,q,-p-q and cyclic noncommuting colours. Use that q in the BC2 Euler source before any second-order solve. Require agreement with the w2-derived q, vanishing low numerator on both null sheets, and Cauchy recovery of direct curvature with the original 2e-9 / 2e-8 relative-plus-absolute tolerances. Delete each source leg and require the same 100x residual / 1e-8 mutation threshold. Include genuinely complex external theta and both sheets, not only real theta.

Use exact integer three-cube edge arithmetic for pure-gradient BCH2, its mixed polarization, and d3 cancellation. A false componentwise derivative bound or replacement by O(f^2) alone is not assumed; look for the mixed a*f contribution and keep any failed detector.

Use the already independently written Cell geometry and linear solves as reviewer-owned helper code; the new top-current construction differs from the direct second-order solve. This reuse is disclosed and is not a second independent implementation of Cell. Tests are finite diagnostics only. No author helpers imported. Existing scalar/source programs remain unchanged.
