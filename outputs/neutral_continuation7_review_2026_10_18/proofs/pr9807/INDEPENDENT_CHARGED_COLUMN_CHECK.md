<!-- Original PR9807 source SHA256 8a5bdaa9d91330ef41bdbca6bf9ff9222f9bb72c93cf319f947c095e569f0971. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Charged whole-column route: focused assessment

Verdict: PASS as a constructive route, with the source and transfer qualifications below. This is an assessment of the derived leading branch, not a completed new canonical theorem or a formal audit.

## Prior work and symmetry

WHOLE_COLUMN_MODE_PROOF.md already derives the fixed-even-height winding coefficient on the entire wall-free space. Its principal growing-height result is a frozen spectral-window family, not the present isolated odd-charge dispersive band. NATIVE_CHARGED_GROUND_DYNAMICS_NOTE describes a different charged line: local Z changes X/Y plane characters inside the flat manifold, with a row-tunneling scale. The proposed whole-column X operator instead changes every z-plane Z character and, for even L, preserves all physical X/Y plane characters. Its transverse translations have identical charge patterns, so the earlier plane-charge mobility restriction permits both transverse directions.

For even transverse periods the row/column flat kernel preserves column-number parity. Fixing positive X/Y characters leaves one orbit state per compatible syndrome in either column-parity sector. The odd sector has no Q0 state. The minimum Q is four; its syndromes are rectangle corners, with odd rectangle area. Minimum perimeter eight occurs only for the filled 2×2 bad-plaquette square, equivalently one reversed column, up to translations and the flat kernel. The next odd rectangles have a side at least three and perimeter at least twelve. With b=3L/8192 the separation is 2b(12−8)Jλ6=JDλ6, D=8b. Larger Q costs an additional order-λ4 amount and cannot compete for sufficiently small λ using the all-Q relative bound.

## Native motion

Projecting an adjacent pair-column flip onto the one-column translates gives exactly the four nearest-neighbor moves. Both directions carry the same negative winding coefficient for even L. Consequently

 E_ch(q)=common(λ)−2Jγ_L λ^L(cos qx+cos qy)+higher terms,
 γ_L=binom(2L−2,L−1)/8^(L−1).

For L10, γ=12155/33554432. The leading gap from the selected even vacuum is J(L/16)λ4+O(Jλ6). The resolved small-momentum increment is Jγλ10|q|² to leading order. There is only one minimum pattern per momentum, so there is no small orientation splitting of the neutral Q8 construction. Excursions to other odd Q4 shapes begin at second hopping order λ^(20−6)=λ14; local corrections to the first hopping can already occur at λ12. Both are later than λ10. Diagonal local coefficients are common over the translated minimum and cannot introduce an earlier dispersion.

The existing all-Q low-energy embedding and fixed-order weighted-spatial-moment reductions offer a simpler polynomial-grid transfer here: internal isolation is order λ6, and a final absolute tail JR²λ^M is negligible compared with λ^(10+2p) if M>10+4p. This still requires applying those reductions in the odd charge fibre and retaining the common higher diagonal shifts. It is not licensed by global small norm of the entire no-wall band. Fixed p and fixed L are essential; choose the finite normal-form order separately for that p. A continuous derivative of finite-grid energies should not be claimed; resolved-grid quadratic increments suffice.

## Readout and limits of interpretation

Define Xbar_q=R^(-1) sum_r exp(−iq·r) product_z X_(r,z), with V=LR². At λ=0 its action on the normalized positive-character flat vacuum is the normalized momentum superposition of one-column orbit states: norm and leading pole weight are one. A local single-column probe has weight 1/R² at a specified momentum. A 1/sqrt(V) convention instead gives leading weight 1/L. State the convention explicitly.

For a matched dressed source this leading result is immediate. For the bare physical Xbar_q on polynomial grids, provide the local translated-pattern Gram estimate after the wall/Q transformations: finite-order dressing corrections should be O(λ) in normalized vector norm, uniformly in R, plus the chosen global tail. A crude O(λ) local error summed by triangle gives O(Rλ), and is insufficient when p>1. Likewise crude projector-tail multiplication by ||Xbar_q||≤R requires M>6+3p; this is compatible with an arbitrarily large fixed M. No source-weight obstacle was found, but the local Gram step should be written rather than silently inferred from fixed-R convergence.

The original distance-two ZZ source C is exactly charge preserving and cannot create this odd-charge particle from the even vacuum. The new readout is an explicitly charged physical L-spin operator, not a newly derived original-C residue. Distinct Xbar operators commute, which supports a hard-core spin/bosonic algebra description; it establishes neither canonical boson commutators nor fermionic statistics.

This is a useful distinct prospective matter channel: wall-free charged column, gap order λ4 and hopping order λ10, versus the previous N2 heavy defect with gap order J and hopping order λ. Coupling to the neutral scalar branch remains a separate matrix-element or scattering calculation. Symmetry permits a charge-preserving interaction but neither fixes a nonzero vertex nor proves universality, on-shell radiation, relativistic propagation, or a many-particle theory. Use the existing global-ground existence result only with its exact charge-sector hypotheses; no uniqueness or universal ground preparation is supplied by this route assessment.
