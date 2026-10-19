# Supporting mathematical source

Original: `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_DARK_FOURTH_CHECK.md`, SHA256 `d7613c4e87c2e13bbc8936e3dfa8d0b77de0b972d9fdf94f53d4ef001706ff75`. This extract preserves the mathematical argument and its limitations; historical execution descriptions are not fresh evidence. Current promotion boundaries: `docs/work_history/repo/review_feedback/NEUTRAL_CONTINUATION_BOUNDARIES_2026-10-18.md`. Original report and verdict history are recoverable in the archive manifest.

# Exact finite dark-segment fourth-order kernels

These are exact rational finite certificates, not an all-length or complete dark-family closure proof. No root files changed; root retains authorship.

The independent Fraction implementation constructs unnormalized localized dark states d_ell,j from all16 oriented diagonal-color pairs for ell2,4,6. Each localized vector has squared norm16; all relevant translations are distinct/orthogonal at L14/16, so no antipodal folding factor enters. It asserts PVP d_ell,j=0 exactly, using the complete energy8 projector. Native h entries and longitudinal excitation energies are integer; every resolvent and accumulated path amplitude is a Fraction. There is no numerical pruning, eigensolver, rational recognition or fitted normalization.

For two such dark vectors a,b, canonical fourth order reduces to

<a|V R V R V R V|b> -(1/2)[<RVa,RV K2b>+<RV K2a,RVb>].

Terms with K1 on either endpoint vanish because BOTH vectors lie in its kernel. The first term is computed as <VRVa,R VRVb>, with all intermediate two-hop states included. This bilinear formula does not imply the entire K4 action is closed on these vectors; outside-state terms remain possible.

For EACH L14 and L16, with translation variable j in <d_left,j|K4|d_right,0>, exact kernels are:

- left2/right4: -3/64 at j0 and j2, zero elsewhere.
- left4/right6: -3/64 at j0 and j2, zero elsewhere.
- left4/right4 after ground subtraction: -13/96 at j0, zero elsewhere.

The independently computed scalar ground fourth shifts are -7/48 and-1/6, respectively. These were subtracted only from the same-state diagonal.

For centered Fourier states L^-1/2 sum_j exp[iq(j+(ell-1)/2)] d_ell,j/4, the center difference between ell and ell+2 removes the translation phase: e^(iq)[-3/64(1+e^(-2iq))]=-3cos(q)/32. The d4 diagonal remains -13/96. Thus both hopping coefficients and the diagonal are certified for EVERY allowed momentum on these two finite rings, including possible zero hopping where cos(q)=0.

L12 at ell6 would require folded-state normalization because a segment and its complement coincide after exchanging the oriented colors. That case was deliberately avoided here; the root's sqrt(2) endpoint enhancement is not silently imported into the unwrapped formula. The finite certificates support the proposed local half-line coefficients, but they do not establish uniform-in-L error bounds, absence of couplings to other dark colors/lengths/channels, or all-order invariance. Degenerate dark mixing still has to be included in an actual pole/residue analysis. No native scalar or width claim is certified by these matrix entries.

Files and hashes:

- `/private/tmp/neutral-kink-dark-rational.py`: `a05ba6ff89377c93f1ea7e95d984d53d480800667ecf5b7415f5046edfebd235`
- `/private/tmp/neutral-kink-dark-rational.json`: `02ca039c4bccdd01d5263c4a81f07c98a2526d2a6389ff01c49d7186be662351`
