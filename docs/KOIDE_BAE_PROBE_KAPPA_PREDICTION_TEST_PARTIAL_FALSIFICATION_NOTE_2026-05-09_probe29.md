# Abstract Isotype-Weight Functional versus Fourier Zero-Locus Obstruction

Date: 2026-05-09

Source repair: 2026-07-18

**Type:** `bounded_theorem`

**Scope:** exact finite-dimensional algebra for a supplied logarithmic functional
**Status:** source repaired; a fresh independent audit is required

## Claim

Let

\[
H=aI+bC+\overline b\,C^2,\qquad a\in\mathbb R,\quad b\in\mathbb C,
\]

and split its Frobenius norm into the trivial and nontrivial cyclic
isotypes,

\[
E_+=3a^2,\qquad E_\perp=6|b|^2.
\]

For supplied positive weights \(\mu,\nu\), consider the supplied functional

\[
S_{\mu,\nu}=\mu\log E_+ + \nu\log E_\perp
\]

on the open part of the fixed-norm surface
\(E_++E_\perp=N>0\). Its unique stationary point is

\[
E_+=\frac{\mu}{\mu+\nu}N,
\qquad
E_\perp=\frac{\nu}{\mu+\nu}N.
\]

Consequently, where \(b\ne0\),

\[
\kappa:=\frac{a^2}{|b|^2}
=2\frac{E_+}{E_\perp}
=\frac{2\mu}{\nu}.
\]

Thus the supplied weights \((\mu,\nu)=(1,2)\) select \(\kappa=1\), while
equal weights \((1,1)\) select \(\kappa=2\). The former stationary point
does not lie on the abstract Fourier zero locus

\[
a^2-2|b|^2=0,
\]

whereas the latter does. This is a bounded obstruction: the particular
supplied \((1,2)\) functional cannot select that polynomial locus.

## Proof

Put \(p=E_+\), so \(E_\perp=N-p\) and \(0<p<N\). Then

\[
S_{\mu,\nu}(p)=\mu\log p+\nu\log(N-p),
\]

with

\[
S'_{\mu,\nu}(p)=\frac{\mu}{p}-\frac{\nu}{N-p},
\qquad
S''_{\mu,\nu}(p)=-\frac{\mu}{p^2}-\frac{\nu}{(N-p)^2}<0.
\]

The displayed stationary energies follow immediately, and strict
concavity makes the stationary point unique. Since
\(E_+/E_\perp=a^2/(2|b|^2)\), the ratio formula follows for \(b\ne0\).
Finally,

\[
a^2-2|b|^2=0
\quad\Longleftrightarrow\quad
E_+=E_\perp.
\]

For positive weights this occurs at the stationary point exactly when
\(\mu=\nu\).

### Independent global-maximizer reconstruction

Set \(t=E_+/N\) and \(q=\mu/(\mu+\nu)\). Without differentiating,

\[
S(t)-S(q)=-(\mu+\nu)
D_{\mathrm{KL}}\!\left((q,1-q)\,\|\,(t,1-t)\right)\le0.
\]

Equivalently, weighted AM-GM applies to \(t/q\) and
\((1-t)/(1-q)\), whose \((q,1-q)\)-weighted arithmetic mean is exactly
one. Equality requires \(t/q=(1-t)/(1-q)\), hence uniquely \(t=q\).
This proves the same global maximizer by a route distinct from the
derivative and curvature calculation.

## Global polynomial statement and the \(b=0\) boundary

The polynomial equation \(a^2-2|b|^2=0\) is globally meaningful. At
\(b=0\) it forces \(a=0\). The ratio \(\kappa=a^2/|b|^2\) is not defined at
that origin and is used here only on \(b\ne0\). No ratio value is assigned by
continuity at \(b=0\).

The exact Fourier equivalence used here is proved in the
[Abstract Hermitian-Circulant Fourier Invariant Theorem](KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md).
That theorem supplies only the finite polynomial identity; it supplies no
mass assignment or physical carrier.

## Exact in-scope and excluded conclusions

Exact in scope:

1. the exact isotype-energy formulas;
2. the unique stationary energy fractions for a supplied positive-weight
   logarithmic functional;
3. the exact mismatch between the supplied \((1,2)\) stationary point and
   the abstract equal-energy/Fourier zero locus;
4. the \(b\ne0\) domain of the ratio statement and the global polynomial
   boundary.

Not derived:

- that either logarithmic functional is physically selected or canonical;
- that \(H\) carries charged-lepton masses or square roots of masses;
- a P1 assignment, cyclic-compression carrier, physical selector, MRU
  principle, or scalar measure;
- an unconditional prediction or falsification of a charged-lepton relation.

### Conditional empirical comparator (not theorem evidence)

If one additionally supplies both (i) the P1 square-root-mass assignment and
charged-lepton carrier/readout and (ii) the claim that the \((1,2)\)
logarithmic functional is the physical law for that carrier, then its
\(\kappa=1\) stationary locus disagrees with the charged-lepton square-root
mass Fourier comparator \(\kappa\simeq2\). From the supplied snapshot
\((m_e,m_\mu,m_\tau)=(0.51099895,105.6583755,1776.86)\,\mathrm{MeV}\),
the runner independently recomputes \(\kappa=2.0000369318\); this is printed
as uncounted support and is not used by any theorem check. The snapshot is
also recorded in the source-side
[circulant derivation note](KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18.md).
Under those two added premises the mismatch is a
partial falsification of that *conditioned model only*; it is not a
falsification of this framework, which supplies neither premise here.

This repair preserves that narrow conditional comparator while removing the
former unconditional physical “partial falsification” reading. The exact
result is the abstract supplied-functional obstruction above.

## Executable witness

Run:

```bash
python3 scripts/cl3_koide_bae_probe_kappa_prediction_test_2026_05_09_probe29.py --mode normal
python3 scripts/cl3_koide_bae_probe_kappa_prediction_test_2026_05_09_probe29.py --mode independent
python3 scripts/cl3_koide_bae_probe_kappa_prediction_test_2026_05_09_probe29.py --mode hostile
```

The normal mode checks the direct matrix and stationary-point algebra. The
independent mode reconstructs the result from the Bernoulli KL identity and
weighted AM-GM, without differentiating the supplied functional.
The hostile mode requires wrong weights, missing normalization factors,
ratio extension to \(b=0\), and false zero-locus identifications to fail.
With no `--mode` argument, all three modes run so the single canonical
SHA-pinned cache records every evidence path.
