# Dirac Dynamics Unlock Path From The PR #4747 Axiom Reset

**Date:** 2026-06-30
**Claim type:** source-side unlock map / bridge consequence
**Status authority:** independent audit lane only. This note does not set an
audit verdict, refresh generated ledgers, or register a primitive.
**Primary runner:**
[`scripts/dirac_dynamics_unlock_path_from_axiom_reset_2026_06_30.py`](../scripts/dirac_dynamics_unlock_path_from_axiom_reset_2026_06_30.py)

## Claim

If PR #4747's Lattice/Qubit/Admissibility/Record axiom reset is accepted, and
PR #4748's strict nearest-neighbor composition bridge is retained as the
operational composition reading of Admissibility, then the repo has a complete
unbounded route to the spatial Dirac kinetic branch:

```text
PR #4747 axioms
  -> strict nearest-neighbor composition
  -> no face-diagonal mixed terms in the free Z^3 translation algebra
  -> anticommuting one-site edge coefficients
  -> Pauli / Cl(3) edge frame
  -> plaquette flux(-1)
  -> Kawamoto-Smit / staggered-Dirac kinetic branch K1
```

Here "Dirac dynamics" means the repo's static spatial first-order
Dirac/staggered kinetic spine. It does not mean a full temporal Hamiltonian,
record-production law, probability rule, or measurement theory.

## Path

### 1. Axiom Base

PR #4747 supplies the minimal ontology:

- **Lattice:** physical sites are `Z^3` with nearest-neighbor adjacency,
  translations, and proper cubic rotations.
- **Qubit:** each site has a local possibility domain whose full one-site
  algebraic presentation is `M_2(C)`.
- **Admissibility:** one fixed nearest-neighbor admissibility rule determines
  the available subset of possibilities at each site.
- **Record:** a record locks exactly one available local possibility, and only
  records are readable.

This gives nearest-neighbor availability, one-qubit site capacity, and cubic
covariance. It does not by itself specify how availability influence composes.

### 2. Composition Bridge

PR #4748 supplies the missing bridge:

```text
Composing primitive nearest-neighbor availability influences must not create a
direct face-diagonal availability influence.
```

This is strict nearest-neighbor composition. It is not a Hamiltonian, a time
law, a probability rule, or a measurement rule. It is the locality-preservation
condition needed for composed availability influence.

### 3. Unbounded Selector Theorem

In the free `Z^3` translation algebra, the twelve face-diagonal monomials are
independent. For an edge-supported carrier

```text
D = sum_mu Gamma_mu nabla_mu,
```

strict nearest-neighbor composition says that `D^2` has no mixed
face-diagonal terms. Equivalently,

```text
Gamma_mu Gamma_nu + Gamma_nu Gamma_mu = 0    for mu != nu.
```

That is a coefficient identity on the infinite lattice, so it is unbounded in
lattice volume. Finite tori can add wrap-holonomy convention data, but the
selector is not proved by a finite-volume scan.

### 4. Qubit Capacity Forces The Pauli Frame

Inside `M_2(C)`, three independent no-leak edge coefficients saturate the
one-qubit anticommuting capacity. Up to unitary/frame rotation they form the
Pauli / `Cl(3)` frame. Their plaquette holonomy is flux `-1`.

The scalar branch `Gamma_mu = I` has flux `+1` and produces a nonzero
face-diagonal mixed coefficient. It therefore fails strict nearest-neighbor
composition.

### 5. Kinetic-Order Blocker Retired

The existing two-flux theorem already reduced the kinetic problem to two frame
classes:

```text
K0: flux(+1), scalar tight-binding branch
K1: flux(-1), Kawamoto-Smit / staggered-Dirac branch
```

Before PR #4748, the open residual was the one-bit selector `K1` versus `K0`.
Strict nearest-neighbor composition supplies that bit:

```text
K0 leaks face-diagonal influence under composition.
K1 cancels face-diagonal influence under composition.
```

So the old P-KIN residual is no longer an admission on this route. It becomes
theorem content, conditional only on accepting strict nearest-neighbor
composition as the bridge reading of Admissibility.

### 6. P-SD Absorbing Frame Activates

The existing kinetic-class forcing note already proves that on the selected
flux `-1` branch, the site-local absorbing frame exists and is unique up to
site-local `U(1)` gauge times one global frame. Thus P-SD is no longer a
separate premise once K1 is selected.

### 7. Kawamoto-Smit Phase Law Activates

The Kawamoto-Smit substep-2 note proves the local phase law under P-KIN/P-SD.
After steps 5 and 6, those are supplied by the strict-NN bridge plus the
two-flux and absorbing-frame theorems. On simply connected regions, the phase
systems form one local gauge class:

```text
eta_1 = 1
eta_2(x) = (-1)^(x_1)
eta_3(x) = (-1)^(x_1 + x_2)
```

Boundary holonomies on finite tori remain convention surfaces, not failures of
the local Dirac kinetic derivation.

### 8. Realization-Gate Impact

The staggered-Dirac realization gate's kinetic-form clause is the main direct
unlock:

```text
old: kinetic-form clause bounded by P-KIN/P-SD/P-FLUX
new: kinetic-form clause supplied by strict NN composition + two-flux theorem
     + absorbing-frame theorem + Kawamoto-Smit phase forcing
```

The full realization gate still has non-kinetic boundaries. The strict-NN
bridge does not by itself derive species-labeling conventions,
`AC_phi_lambda`, theta, source/action coefficients, gauge species, Born
weights, measurement context, or temporal evolution.

## Repo Unlock Table

| Existing blocker | New supplier | Result |
|---|---|---|
| kinetic-order selector / B-BIT | strict nearest-neighbor composition in the free `Z^3` translation algebra | retired on the bridge route |
| P-KIN broad Dirac kinetic declaration | two-flux theorem plus strict-NN rejection of K0 | reduced to theorem content |
| P-SD site-local spin diagonalization | absorbing-frame theorem on selected K1 | supplied on the selected branch |
| gamma/edge index pairing | no-mixed-term condition ties independent lattice edge directions to anticommuting one-site coefficients | supplied within the bridge surface |
| scalar spectator K0 | nonzero face-diagonal leakage under composition | rejected |
| FSB-K / Z P-FLUX route | thermal/spectral selector | becomes corroborating downstream support, not load-bearing for the kinetic spine |
| finite torus APBC/PBC wrap signs | boundary-holonomy convention | remains separate convention data |

## Audit Work After This PR

If #4748 is retained, the audit refresh should target these source rows:

1. Re-audit
   [`STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md`](STAGGERED_DIRAC_KINETIC_CLASS_FORCING_NARROW_THEOREM_NOTE_2026-06-10.md)
   with the strict-NN bridge as the selector replacing B-BIT.
2. Re-audit
   [`STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md`](STAGGERED_DIRAC_KAWAMOTO_SMIT_FORCING_THEOREM_NOTE_2026-05-07.md)
   so P-KIN/P-SD are no longer treated as naked premises on the selected
   branch.
3. Re-audit
   [`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md`](STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md)
   to split the kinetic-form clause from the remaining non-kinetic residuals.
4. Reclassify downstream rows that depend only on the Dirac kinetic spine, while
   leaving rows bounded if they still depend on `AC_phi_lambda`, theta,
   source/action, observable identification, probability, temporal dynamics, or
   species-labeling convention.

## Minimal Axiom Fallback

If reviewers reject strict nearest-neighbor composition as bridge-derived from
Admissibility, the minimum foundation iteration is not a broad Dynamics axiom.
It is one Admissibility sentence:

```text
Composing nearest-neighbor admissibility influences does not create a direct
face-diagonal admissibility influence.
```

That sentence would make the bridge axiom-level content. If reviewers accept
the bridge as the operational reading of the current Admissibility axiom, no
further axiom edit is needed.

## What Still Does Not Unlock

This path does not derive:

- probability or Born weights;
- measurement/readout context selection;
- record-production dynamics or a time metric;
- a Hamiltonian or transfer operator beyond the spatial kinetic branch;
- `AC_phi_lambda` species-labeling content;
- theta;
- source/action coefficients, gauge species, or physical observable bridges.

Those remain separate downstream targets.

## Verification

Run:

```bash
python3 scripts/dirac_dynamics_unlock_path_from_axiom_reset_2026_06_30.py
```

Expected close:

```text
TOTAL: PASS=43 FAIL=0
```
