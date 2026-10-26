# Finite determinant and supplied quarter-power statistic

**Date:** 2026-05-10 (source scope corrected 2026-10-23)
**Type:** bounded_theorem
**Source-note proposal disclaimer:** this is a conditional finite mathematical
result. Independent audit alone controls effective status.
**Primary runner:** [finite determinant checks](../scripts/frontier_hierarchy_heat_kernel_d4_compression.py)
**Cached output:** [runner output](../logs/runner-cache/frontier_hierarchy_heat_kernel_d4_compression.txt)

The finite determinant identity survives. The old heat-kernel argument does
not derive a physical quarter-power compression law. The spectrum and the
quarter-power statistic below are supplied mathematical inputs. No derivation
of the spectrum from primitive dynamics, no continuum limit, and no physical
mass or temperature identification is claimed.

## Supplied spectrum

Let L be 2 or 4, let u and the reference scale mu be positive, and set
n_L=8L. Suppose Q_L=D_L†D_L has the positive eigenvalues

```text
lambda_(k,a) = u² [3 + sin²((2k+1) pi/L)],
k=0,...,L-1; a=1,...,8.
```

Here D_L is an n_L by n_L matrix and the spectrum is an assumption. The
runner uses dimensionless eigenvalues lambda/mu², with u_0=u/mu. The
multiplicity eight is supplied; no taste realization or lattice equivalence
is proved. Positive u is essential to the logarithms and inverses below.

The spectrum is constant at each of these endpoints: 4u² at L=2 and
(7/2)u² at L=4. Thus

```text
det Q_2 = (4u²)^16,        |det D_2| = (4u²)^8,
det Q_4 = ((7/2)u²)^32,   |det D_4| = ((7/2)u²)^16,
R_D = |det D_4| / |det D_2|² = (7/8)^16,
R_Q = det Q_4 / (det Q_2)² = (7/8)^32 = R_D².
```

The determinant relation follows from det(D†D)=|det D|². The ratios cancel
the same u and reference scale across the endpoints. These formulas do not
require any asymptotic approximation or external determinant theorem.

## Finite zeta identity

For q_j=lambda_j/mu²>0 define the entire finite sum
zeta_L(s)=sum_j q_j^(-s), using real log q_j. Differentiating each term gives

```text
-zeta_L'(0) = sum_j log q_j = log det(Q_L/mu²).
```

If K_L(t)=sum_j exp(-t q_j), then, for Re(s)>0,

```text
integral_0^infinity t^(s-1) K_L(t) dt = Gamma(s) zeta_L(s).
```

This follows by a finite sum of convergent integrals and the substitution
x=t q_j. The finite sum itself supplies the continuation to s=0. There is
no infinite determinant regularization, no Weyl law, and no ultraviolet
limit in this statement. The runner's two identical sums of logarithms are
a consistency display, not an independent numerical proof of this identity.

## Two different normalizations

The ordinary geometric mean singular value is a mass-dimensional quantity

```text
G_L = |det D_L|^(1/(8L)) = (det Q_L)^(1/(16L)),
G_4/G_2 = R_D^(1/32) = R_Q^(1/64) = (7/8)^(1/2).
```

It does **not** give the old quarter-power ratio. Instead define, as an
extra supplied choice, the dimensionless statistic

```text
C_L = (|det D_L| / mu^(8L))^(1/(16L))
    = (det Q_L / mu^(16L))^(1/(32L)),
C_4/C_2 = R_D^(1/64) = R_Q^(1/128) = (7/8)^(1/4).
```

These equalities follow from the positive real powers and the exact products
above. The denominator 16L is twice the actual singular-value count 8L.
C_L is not a physical mass and is not the ordinary geometric mean singular
value. Defining mu*C_L as a mass-valued readout is an additional choice;
it does not derive a physical observable. The physical readout remains open.

The previous text used the D ratio as a D†D ratio and then removed a square
root in its interpretation. Those are inconsistent normalizations. The
correct D†D denominator for this supplied quarter-power statistic is 32L,
not 16L. The equalities above retain the quarter ratio without that mistake
and without claiming its exponent is physically selected.

## Why the old thermal argument fails

The old displayed density and free-energy expression were

```text
rho(lambda) = V4 lambda/(16 pi²),
f(T) = -T/V4 integral_0^infinity rho(lambda) log(1+exp(-lambda/T)) d lambda.
```

Formally substituting lambda=T x, including d lambda=T dx, gives exactly

```text
f(T) = -T^3/(16 pi²) integral_0^infinity x log(1+exp(-x)) dx.
```

The integral is positive and finite: near zero its integrand is bounded
by x log 2, and at infinity it is bounded by x exp(-x). Hence the displayed
expression scales as T^3, not T^4. This refutes that specific algebraic
scaling assertion. It is not a counterexample to the separate continuum
Stefan theorem.

There is also a dimensional error before any integral is evaluated: an
eigenvalue lambda of D†D has mass dimension two, while physical temperature
has mass dimension one in natural units. Therefore lambda/T is not a
dimensionless thermal energy ratio. Replacing lambda by an energy, changing
the density, or specifying a continuum limit would be new assumptions and
is not done here.

The finite counting function saturates: for lambda above the largest of
the n_L eigenvalues, N_L(lambda)=n_L. Thus N_L(lambda)/lambda² tends to zero.
These fixed 16- and 32-element spectra cannot verify an asymptotic law with
a positive lambda² coefficient. This does not refute Weyl's theorem for
operators satisfying its own hypotheses; it rejects its use as evidence
from these fixed finite counts.

## Separate continuum comparison and open obligations

The [supplied continuum Stefan calculation](AXIOM_FIRST_STEFAN_BOLTZMANN_THEOREM_NOTE_2026-05-01.md)
assumes oscillator/Gibbs statistics, two polarizations, linear dispersion,
and a three-dimensional continuum measure. Under those premises,
u(T)=pi² T^4/15 in natural units, and its algebraic inverse is
T=(15u/pi²)^(1/4). The shared exponent does not identify C_L with energy
density, temperature, an EWSB scale, or any mass. The runner checks the
supplied inverse separately; its text checks confer no scientific authority.

The rational equality 1/4=4/2^4 is also independent of any physical readout.
The finite table of other integers is a comparison, not a dimensional or
uniqueness proof. NO PDG observed values enter this calculation.

Outstanding obligations are a physical operator realization, a justified
continuum limit if one is wanted, a correctly dimensioned thermodynamic
identification, and a physical choice of readout. None is resolved here.
The finite theorem neither asserts their truth nor proves their impossibility.

## Historical recovery

The complete stronger note, runner, and cached output are preserved at Git
revision `fbd1e8030c02ec6fdbb95bdf819be020aa7f043a`, at these same repository
paths. They are historical claims and failures, not current evidence for
heat-kernel compression or a physical readout. The earlier determinant,
dimensional-compression, bosonic-bilinear, and realization-gate discussions
remain provenance in that preserved version; their claims are not imported
as premises into this self-contained supplied-spectrum theorem. No audit
verdict or ledger status is changed by this correction.
