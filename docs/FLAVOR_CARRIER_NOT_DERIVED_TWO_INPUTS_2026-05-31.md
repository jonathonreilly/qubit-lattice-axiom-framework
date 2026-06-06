# Flavor Carrier Derivation: 2/9 Is Not A Bare Character; Carrier And Basepoint Remain Open

**Date:** 2026-05-31
**Claim type:** bounded_support
**Actual current surface status:** bounded-support
**Trace class:** negative_route_pruning
**Reachability to target:** prunes
**Runner:** `scripts/flavor_carrier_not_derived_two_inputs_2026_05_31.py` (SCORECARD 8/8).
**Audit posture:** this is source repair only. It does not retag the audit ledger or request an audit/status change.

## Question

Can the charged-lepton flavor carrier be derived from the retained finite generation
representation by reading the value `2/9` as a bare `C_3` character on the corner
module, without the fixed-point/index determinant apparatus? And does the same finite
equivariance select the `r=1/2` basepoint?

## Verdict

The bare-character shortcut fails. The finite calculation still has useful content:
`2/9` is the `L_3(1,2)` determinant-denominator weight of the nontrivial `C_3`
doublet. It is not a bare representation character. Removing the determinant
denominators removes the value.

This note therefore prunes one derivation route only:

1. A finite `C_3` triplet has bare characters `1` on the singlet, `omega+omega^2=-1`
   on the doublet, and `1+omega+omega^2=0` on the full triplet. None equals `2/9`.
2. The value `2/9` appears as
   `L_3(1,2)=(1/3) sum_{k=1,2} 1/((omega^k-1)(omega^{2k}-1))`, i.e. from the
   two-eigenvalue normal/doublet determinant denominator.
3. A `C_3`-equivariant Hermitian operator has the circulant form
   `H=aI+bC+conj(b)C^2`, but equivariance alone leaves `r=|b|^2/a^2` free.
4. The section arithmetic `Q(r)=1/3+(2/3)r` gives both `Q(1/2)=2/3` and `Q(1)=1`;
   this calculation does not choose between them.

Consequently, this artifact does **not** derive the physical carrier, does **not** select the basepoint, and does **not** close the species-to-flavor identification.
It only blocks the specific route that tried to obtain both the value and the physical
carrier from bare finite characters.

## Closed finite packet

### A. Bare characters do not supply 2/9

Let `C` be the cyclic generator on the triplet with eigenvalues `{1, omega, omega^2}`.
The bare finite character data are:

```text
chi_singlet(C) = 1
chi_doublet(C) = omega + omega^2 = -1
chi_triplet(C) = 1 + omega + omega^2 = 0
```

None is `2/9`. Therefore the attempted identification
`2/9 = bare finite-representation character` is false.

### B. The determinant-denominator calculation does supply 2/9

On the nontrivial doublet, the determinant-denominator terms are

```text
1 / ((omega^k - 1)(omega^(2k) - 1)) = 1/3,  k = 1,2.
```

Hence

```text
L_3(1,2) = (1/3) * (1/3 + 1/3) = 2/9.
```

The one-factor expression `1/(omega^k-1)` is not the determinant inverse. The
determinant inverse is the two-eigenvalue product above. Thus the finite value can be
kept only as a resolvent/Lefschetz-style doublet weight, not as a bare character.

### C. Equivariance leaves the basepoint parameter free

For every complex `b` and positive real `a`,

```text
H = aI + bC + conj(b)C^2
```

commutes with `C`. The ratio

```text
r = |b|^2 / a^2
```

therefore ranges freely inside the equivariant family. The framework-native finite
operator form does not pick `r=1/2`.

### D. Carrier selection and basepoint selection remain outside this packet

The arithmetic

```text
Q(r) = 1/3 + (2/3)r
```

checks both candidate readings:

```text
Q(1/2) = 2/3
Q(1)   = 1
```

This packet does not decide which section is physical. Nor does it identify the finite
generation factor as the charged-lepton flavor carrier. Those are still open bridges for
future framework-native work.

## What changed relative to the prior wording

The previous wording treated the route failure as an input-count theorem. That was too
strong for the source. The repaired claim is narrower and more auditable:

- proved: `2/9` is not a bare `C_3` character;
- proved: the determinant-denominator doublet calculation gives `2/9`;
- proved: `C_3` equivariance alone does not select `r`;
- not proved: the physical carrier;
- not proved: the physical basepoint;
- not proved: a theorem that there are exactly two independent irreducible inputs.

No new axiom is introduced.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them; it does not promote this note or change the audited claim scope.

- [physical_lattice_necessity_note](PHYSICAL_LATTICE_NECESSITY_NOTE.md)
