# Supporting mathematical source

Original: `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_DARK_BOUND_CHECK.md`, SHA256 `2b46b11f5e3097b8b7d7d4f23ce69b970e912b16b0d7b9b83e33c802886b96ee`. This extract preserves the mathematical argument and its limitations; historical execution descriptions are not fresh evidence. Current promotion boundaries: `docs/work_history/repo/review_feedback/NEUTRAL_CONTINUATION_BOUNDARIES_2026-10-18.md`. Original report and verdict history are recoverable in the archive manifest.

# Conditional expanded dark-channel bound-state check

All quoted rational values check for the proposed dark half-line model. This report does not certify that it is the complete native effective dark sector. In particular, the discovered K4 leakage invalidates treating the earlier isolated d2 self-energy as the native leading real pole shift. Those earlier formulas remain truncated-model calculations.

## Half-line eigenproblem

Let sites n=0,1,... denote d2,d4,d6,..., with bulk diagonal b=-13/96, real hopping t=-3cos(q)/32 and boundary defect

v=-47/192+(1-9u)/(4(1+u))=(1-479u)/(192(1+u)), u=cos q.

For an eigenvector psi_n=N r^n, the bulk and boundary equations are E=b+t(r+r^-1) and E=b+v+tr. Subtraction gives r=t/v. For generic nonzero hopping, a normalizable bound state exists exactly when |v|>|t|. Its energy and boundary probability are

E_b=b+v+t²/v,
Z=|psi_0|²=1-(t/v)².

It lies below the bulk band [b-2|t|,b+2|t|] when v<0 and above it when v>0. At |v|=|t| the formal solution is not normalizable. At t=0 and v nonzero the boundary is trivially isolated; if both vanish the whole flat chain is degenerate and no distinguished simple bound pole follows from this formula.

At q=0 the exact substitutions give

E_b=-63659/45888,
Z=56797/57121.

I independently differentiated E_b(u): the small-q coefficient is -E_b'(1)/2=145219/456968. This is the coefficient in the supplied dark-energy units, hence multiplies Jperp^4/Jz^3 if those are the inherited physical units. It is not a relativistic velocity or a scalar-particle identification.

## Width and source conditions

The proposed dark bound state is bound relative to the narrow DARK continuum; it remains embedded in the wider bright continuum. Calling it a bound state must retain that distinction. If eliminating the bright channel gives, to leading dissipative order, the local term -i Gamma_bright(q) P0/2, first-order non-Hermitian perturbation theory gives

Gamma_bound(q)=Z(q) Gamma_bright(q).

Thus at q=0 the proposed leading full-width coefficient is

Z*(9/32)=511173/1827872.

The narrow dark Hamiltonian has scale Jperp*lambda³, while the bright loss has scale Jperp*lambda^4. At a fixed q with a finite dimensionless dark binding gap this is a small dissipative correction. An energy-dependent bright self-energy also changes pole normalization by its derivative, but the earlier regular fixed-q expansion makes that derivative higher order than the displayed Z factor. Near a dark band threshold the binding gap vanishes, so neither this perturbative width statement nor simple threshold substitution is uniform.

The rank-one loss assumption is essential. If deeper dark sites have direct bright couplings at the same order, the decay amplitude is the coherent sum over the full bound wavefunction, not just its boundary component. Off-diagonal self-energy terms can change or cancel the Z-rescaled width. The parent's ongoing H3-dark and full K4-closure checks are therefore required for any native inference. A successful diagonal/hopping extraction alone does not establish this assumption.

Similarly, the proposed original-source resonance weight is 2Z lambda^4 only if its leading relevant dressed source is the previously derived d2-local amplitude, with no other dark components of the same order. The bare effective-source result would be 2Z lambda². Dressing on deeper dark sites, degenerate canonical rotations or a different chosen ground/source state can alter the physical vertex. These cannot be settled from the dark energy matrix alone.

## Scope of the expanded route

The claimed finite-size identities H1 d_ell=0 and H2 d_ell=-2 d_ell identify a degenerate dark manifold; degenerate mixing at K4 is at the same order as the earlier real bright self-energy. It must be diagonalized before attaching a physical real dispersion. The half-line construction is an appropriate conditional way to do that, but it still requires proof or controlled evidence of: all accessible dark states, all K4 matrix elements, H3 coupling/closure, absence of competing same-order channels, the infinite-length limit, and the original source dressing.

Fixed-L checks at L8..16 need not establish a uniform thermodynamic effective Hamiltonian. The bright expansion remains nonuniform near q=pi, and the width cancellation near ±pi/3 and dark binding thresholds require separate limits. No native exact bound state, stable scalar, observed lifetime, physical detector coupling or cosmological bridge is established here. The rational results above are exact algebra for the provisional expanded model only.
