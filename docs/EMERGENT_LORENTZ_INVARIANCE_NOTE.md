# Low-momentum dispersion of supplied free cubic symbols

**Date:** 2026-04-15; source scope corrected 2026-10-21
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only.
**Primary runner:** [`frontier_emergent_lorentz_invariance.py`](../scripts/frontier_emergent_lorentz_invariance.py)

## Supplied mathematical model

For a>0 and real three-momentum p, take the two free symbols

```text
E_f^2(p) = a^-2 sum_i sin^2(a p_i),
E_b^2(p) = 4 a^-2 sum_i sin^2(a p_i/2).
```

These are supplied kinetic choices, not consequences of cubic adjacency alone. The [current axioms](MINIMAL_AXIOMS_2026-06-29.md) do not select a Hamiltonian or a physical fermion/boson branch. This note proves their local expansion and angular structure, not physical Lorentz invariance of an interacting theory.

## Expansion and angular proof

The cosine double-angle identity gives `sin^2(x)=x^2-x^4/3+O(x^6)`. Consequently, as a|p| tends to zero,

```text
E_f^2 = |p|^2 - (a^2/3) sum_i p_i^4 + O(a^4 |p|^6),
E_b^2 = |p|^2 - (a^2/12) sum_i p_i^4 + O(a^4 |p|^6).
```

The quadratic term is rotationally isotropic; the quartic term is cubic invariant but anisotropic. All coordinate sign flips leave each displayed symbol invariant, so these particular expansions contain no odd powers of an individual momentum component. This does not exclude every parity-even dimension-five operator or establish a physical EFT coefficient basis.

For a unit vector n, `1/3 <= sum_i n_i^4 <= 1`, with the lower bound at equal squared components and the upper bound on an axis. The axis/diagonal ratio of the quartic angular factor is three. The spherical average is 3/5 since each component's fourth moment is 1/5.

Let `r^2=x^2+y^2+z^2`. The homogeneous polynomial

```text
Q4 = x^4+y^4+z^4 - (3/5)r^4
```

is harmonic: its Laplacian is `12r^2-(3/5)20r^2=0`. Restricted to the unit sphere it is therefore purely degree l=4. Cubic-invariant quartics are combinations of `sum x_i^4` and `r^4`; harmonicity leaves one dimension. With conventional orthonormal complex spherical harmonics (the combination below is real),

```text
sum_i n_i^4 = 3/5 + (4 sqrt(pi)/15) K4,
K4 = Y_40 + sqrt(5/14)(Y_44+Y_4,-4).
```

At the north pole K4=3/(2 sqrt(pi)), fixing the displayed coefficient from `1-3/5=2/5`. This pattern is compatible with cubic symmetry. It cannot uniquely identify a microscopic lattice: a continuum model can supply the same quartic symbol.

## Finite hopping example and antiunitary boundary

The runner also constructs the real anti-Hermitian staggered hopping D on an even periodic L=8 cube and diagonalizes the Hermitian lift H=iD. The [exact antiunitary source](CPT_EXACT_NOTE.md) supplies the general even-L algebra: sublattice sign C and inversion P each flip H; bare conjugation K flips H; PK preserves H while CPK flips H. The runner checks the Hermitian-lift distinction and includes the nonzero CPK sign-flip control.

These are matrix identities. Neither the named matrices nor an invariant odd projection identify physical CPT, time reversal, charge conjugation or SME coefficients. The [Hermitian/SME bridge boundary](PHYSICAL_HERMITIAN_HAMILTONIAN_AND_SME_BRIDGE_NOTE_2026-04-30.md) remains separate. The [parity operator source](PARITY_OPERATOR_BASIS_DIMENSION5_LV_NO_GO_THEOREM_NOTE_2026-05-02.md) cannot be replaced by assigning minus-one parity weights to an unexamined list of bilinears; this runner now makes only the displayed scalar-symbol evenness claim.

## Conditional scale estimate

If a physical unit map a=1/M is supplied and E approximately equals |p|, the angular-average leading relative fermion correction is

```text
average |delta E^2|/E^2 approximately (a^2/3)(3/5)|p|^2 = E^2/(5M^2).
```

The factor 1/5 is an angular average, not the all-direction coefficient; the leading direction factor ranges from 1/9 to 1/3. Using the runner's supplied M=1.220890e19 GeV gives approximately 1.34e-39, 1.34e-33 and 1.34e-17 at E=1,1000,1e11 GeV respectively. The correction to E itself is half the leading relative E-squared correction. No observational uncertainty or accuracy is inferred from these numbers.

The registered [scale-reference primitive](SCALE_REFERENCE_PRIMITIVE_NOTE.md) supplies the Planck units reference, not a kinetic symbol, physical readout or a derived a/l_P=1 self-consistency theorem. It is an approved premise, not a source of bounded status. Experimental comparison requires a matched operator, helicity, species, units and observable map. No safety margin, birefringence bound or universal absence of dimension-three/four/five SME terms is established here. A full Lorentz symmetry statement requires more than this scalar dispersion.

## Execution and recovery

```bash
python3 scripts/frontier_emergent_lorentz_invariance.py
```

The runner checks numerical expansions, spherical harmonics, finite hopping spectra, antiunitary matrix algebra and scalar parity. Its Planck notes are contextual file reads only. Numeric checks and finite grids do not select the model. Literal-True certification lines and assigned parity-weight checks have been removed rather than counted as mathematical evidence; no numerical tolerance was relaxed.

The original narrative and dated audit discussion remain recoverable at commit `f24d17d97d372df977476e4a69674577f31af575`. This source correction changes no audit verdict. The stable filename remains for existing consumers, with the physical interpretation now explicitly conditional.
