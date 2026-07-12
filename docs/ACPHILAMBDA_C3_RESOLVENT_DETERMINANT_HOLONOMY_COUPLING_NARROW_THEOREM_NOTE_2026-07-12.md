# AC_phi_lambda C3 Resolvent Determinant-Holonomy Coupling

**Date:** 2026-07-12
**Claim type:** positive_theorem
**Status authority:** independent audit lane. This source proposal does not
set or predict an audit verdict.
**Primary runner:**
[`scripts/acphilambda_c3_resolvent_determinant_holonomy_coupling_2026_07_12.py`](../scripts/acphilambda_c3_resolvent_determinant_holonomy_coupling_2026_07_12.py)
**Runner cache:**
[`logs/runner-cache/acphilambda_c3_resolvent_determinant_holonomy_coupling_2026_07_12.txt`](../logs/runner-cache/acphilambda_c3_resolvent_determinant_holonomy_coupling_2026_07_12.txt)

## Exact theorem

On the real normal plane of the proper cubic `C3` body-diagonal rotation, use
the basis in which the retained normal action is

```text
P_N = [[0,-1],
       [1,-1]].
```

Define the two resolvents and their group-order-normalized nonidentity sum by

```text
R_1 = (I-P_N)^(-1),
R_2 = (I-P_N^2)^(-1),
B   = (R_1+R_2)/3.
```

Then

```text
R_1 = (1/3)[[2,-1],    R_2 = (1/3)[[ 1,1],
              [1, 1]],                  [-1,2]],

R_1+R_2 = I,
B = I/3.
```

The inverse-normal-determinant density retained in
[`KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)
is

```text
h = (1/3) sum_(k=1)^2 det(I-P_N^k)^(-1) = 2/9.
```

The operator sum and the scalar density therefore obey the exact relation

```text
tr(B)=2/3=3h.
```

For real `beta`, define the finite unitary family

```text
U_beta = exp(i beta B).
```

Since `B=I/3`,

```text
U_beta = exp(i beta/3) I,
det(U_beta)=exp(2 i beta/3).
```

At `beta=1`, the principal determinant phase is `2/3`. Choose the exponential
root associated with the additive three-step lift:

```text
E = exp(i B/3).
```

It satisfies `E^3=U_1` and

```text
arg det(E)=2/9=h.
```

This is an exact coupling between the retained fixed-locus density and a
constructed determinant-holonomy line. It is a finite algebra theorem; the
physical identification boundary is stated below.

## Fermionic determinant-power consequence

Use `K=U_beta` as a supplied finite Grassmann kernel. The retained
[`ACPHILAMBDA_FERMIONIC_REALIFICATION_PFAFFIAN_POWER_IDENTITY_NARROW_THEOREM_NOTE_2026-07-12.md`](ACPHILAMBDA_FERMIONIC_REALIFICATION_PFAFFIAN_POWER_IDENTITY_NARROW_THEOREM_NOTE_2026-07-12.md)
gives, with its explicit Berezin orientation,

```text
Z_single(beta)=det_C(U_beta)=exp(2 i beta/3).
```

Writing this same single sector in Majorana-paired coordinates preserves its
determinant power and phase. Adjoining an independent conjugate sector instead
gives

```text
Z_pair(beta)
  = det_C(U_beta) det_C(conjugate(U_beta))
  = 1.
```

The ordinary realification determinant has the same phase-free scalar:

```text
det_R R(U_beta)=|det_C(U_beta)|^2=1.
```

Thus, at `beta=1`, the constructed nonzero determinant phase distinguishes the supplied
single sector from the supplied conjugate-paired total determinant. A
coordinate rewrite of the single sector preserves the phase.

## Determinant-character weights

For the integer determinant-character family

```text
chi_k(z)=z^k,   k in Z,
```

the constructed line gives

```text
chi_k(det U_beta)=exp(2 i k beta/3).
```

Within this family, `chi_k` is faithful on `U(1)` exactly for `k=+1` or
`k=-1`; `k=0` is trivial, and `|k|>1` has a nontrivial root-of-unity kernel.
Complex conjugation exchanges the two faithful orientations. The
conjugate-paired total line has net weight `k+(-k)=0` and hence trivial phase.
Indeed, `chi_1` is the identity and `chi_-1` is inversion. For `|k|>1`, the
nontrivial root `exp(2 pi i/|k|)` lies in the kernel of `chi_k`; for `k=0`,
every point lies in the kernel.

On the additive principal lift where `|2k beta/3|<pi`, the corresponding
symmetric three-step phase is

```text
delta_(k,beta)=2 k beta/9.
```

The target magnitude `2/9` therefore corresponds algebraically to
`|k beta|=1`. The displayed phase equation depends on the product `k beta`.
The equation fixes the product. Selection of the character factor belongs to
a physical-faithfulness theorem; selection of the connection factor belongs
to a normalization theorem.

## Physical identification boundary

The theorem domain is the finite construction of `B`, `U_beta`, and their
determinant lines above. The following physical identifications are separate
theorem targets:

- identification of `B` with the physical charged-lepton connection or action
  generator;
- identification of the physical fermionic kernel with `U_1`, `bC`, or another
  matrix carrying this determinant line;
- normalization `beta=1`;
- physical Record-character faithfulness within the displayed
  integer-character family;
- identification of the physical Record scalar with the folded principal
  determinant phase;
- physical realization of the `E` lift by three symmetry-equivalent Record
  contributions;
- selection between total-determinant and factor-resolved readout for a paired
  carrier.

The normal rotation has `det(P_N)=1`. The phase-bearing object is the
constructed resolvent exponential.

The theorem scope is the finite algebra above. The physical occupancy-grain
and R-eta readout claims lie outside that scope and have separate source rows.
Their joint positive theorem target identifies the physical total action
determinant with the displayed `U_1` sector, with or without its independent
conjugate; gives Record the folded principal phase of that total determinant
through a faithful character; and realizes the displayed `E` lift through
three symmetry-equivalent physical contributions. Under those derived
conditions, the single-sector total carries the nonzero `h` readout, whereas
the conjugate-paired total evaluates to phase-free `1`; the nonzero total phase
then matches the single-sector entry.

The construction is constant over every supplied registered-mass amplitude
ratio `r`; `r` remains a free dial. Axiom, primitive, import, comparator, and
premise-registry surfaces are unchanged.

## Verification

Run:

```bash
python3 scripts/acphilambda_c3_resolvent_determinant_holonomy_coupling_2026_07_12.py
```

Expected result: `PASS=34`, `FAIL=0`.
