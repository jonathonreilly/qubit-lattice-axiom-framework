# CKM Mass-Operator Projector-Overlap Typing Theorem

**Date:** 2026-07-12

**Claim type:** bounded_theorem

**Actual current-surface status:** exact support/boundary theorem

**Trace class:** upstream_support

**Reachability to target:** supports

**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.

**Primary runner:**
[`scripts/frontier_ckm_mass_operator_projector_overlap_typing.py`](../scripts/frontier_ckm_mass_operator_projector_overlap_typing.py)

## 1. Target and result

The parent theorem note
[`CKM_DOWN_TYPE_SCALE_CONVENTION_SUPPORT_NOTE_2026-04-22.md`](CKM_DOWN_TYPE_SCALE_CONVENTION_SUPPORT_NOTE_2026-04-22.md)
isolated a composite typed bridge,

```text
down-mass data -> rank-(1+5) operator X_R -> |V_cb|,
```

but also proved that fixed mass spectra do not determine CKM orientation.
This note separates the exact typing result from the remaining dynamical
alignment law.

The positive result is a basis-covariant CKM readout from a supplied *pair* of
quark mass operators:

```text
|V_cb|^2 = Tr(P_c^u P_b^d).                              (1.1)
```

Here `P_c^u` and `P_b^d` are spectral projectors of the left-handed up- and
down-sector mass-squared operators. No diagonalizer phases, observed masses,
or fitted CKM entries enter (1.1).

The five-sixths bridge is therefore equivalent to one explicit invariant
alignment law,

```text
Tr(P_c^u P_b^d) = (m_s/m_b)^(5/3).                       (1.2)
```

Equation (1.2), not the determinant power, is the remaining dynamical target.
The negative result is correspondingly narrow: no universal down-only,
unitarily equivariant map followed by a conjugacy-invariant scalar readout can
produce physical `|V_cb|` on the full nondegenerate mass-pair domain.

## 2. Explicit theorem conditions

Let `M_u` and `M_d` be supplied complex `3 x 3` quark mass operators acting
between the usual right- and left-handed generation spaces. Define their
left-handed positive operators

```text
H_u = M_u M_u^dagger,
H_d = M_d M_d^dagger.                                    (2.1)
```

Assume simple positive ordered spectra

```text
spec(H_u) = {u_u < u_c < u_t} = {m_u^2,m_c^2,m_t^2},
spec(H_d) = {d_d < d_s < d_b} = {m_d^2,m_s^2,m_b^2}.     (2.2)
```

The ordering labels are an explicit quark-name convention on already supplied
mass operators. This note does not derive the operators, their spectra, or
their identification with physical quarks from the framework axioms.

For a simple eigenvalue, define the spectral projector without choosing an
eigenvector phase:

```text
P_i^u = product_(k != i) (H_u-u_k I)/(u_i-u_k),
P_j^d = product_(l != j) (H_d-d_l I)/(d_j-d_l).          (2.3)
```

Let `U_u` and `U_d` be any unitary left diagonalizers and use the standard CKM
definition

```text
V = U_u^dagger U_d.                                      (2.4)
```

Equation (2.4) is the supplied physical meaning of the quark mass operators;
it is not a new framework axiom or primitive.

## 3. Spectral-projector overlap theorem

**Theorem 1.** Under (2.1)-(2.4),

```text
Tr(P_i^u P_j^d) = |V_ij|^2.                              (3.1)
```

**Proof.** Simple spectra give rank-one projectors

```text
P_i^u = |u_i><u_i|,
P_j^d = |d_j><d_j|.
```

Therefore

```text
Tr(P_i^u P_j^d)
  = <u_i|d_j><d_j|u_i>
  = |<u_i|d_j>|^2
  = |V_ij|^2.
```

The expression is invariant under eigenvector rephasing. Under a simultaneous
weak-basis change `W`, both projectors transform as `P -> W P W^dagger`, and
cyclicity of trace leaves (3.1) unchanged. Thus

```text
|V_cb| = sqrt(Tr(P_c^u P_b^d))                           (3.2)
```

is a target-free, basis-covariant typed readout. Beyond `H_d`, a sufficient
extra relational datum is the up-sector charm projector `P_c^u`; the full
operator `H_u` is sufficient but not logically necessary.

The compressed overlap operator supplies an equivalent one-dimensional
determinant form:

```text
O_cb := P_c^u P_b^d P_c^u
      = |V_cb|^2 P_c^u,
det_(Ran P_c^u)(O_cb) = |V_cb|^2.                        (3.3)
```

This determinant is on the physical overlap line. It is not the six-state
normalized determinant of the parent construction.

## 4. Exact reformulation of the five-sixths target

Define the supplied down-spectrum ratio

```text
R := m_s/m_b = sqrt(d_s/d_b).                            (4.1)
```

For any rank-one projector `Q` on an abstract six-dimensional space, let
`P=I-Q` and

```text
X_R = Q + R P.
```

Then

```text
det(X_R) = R^5,
Delta_6(X_R) := det(X_R)^(1/6) = R^(5/6).                (4.2)
```

Combining (3.2) and (4.2) gives the exact equivalences

```text
|V_cb| = Delta_6(X_R)
<=> Tr(P_c^u P_b^d) = R^(5/3)
<=> |V_cb|^6 = det(X_R) = R^5.                          (4.3)
```

Thus (4.2) packages the exponent but does not imply (4.3). The remaining
physical content is the scalar alignment law (1.2), relating one up-sector
eigenline, one down-sector eigenline, and the down-sector spectrum.

On a strict two-family `2-3` restriction there is an equivalent commutator
falsifier. With spectral gaps `Delta_u`, `Delta_d`, define

```text
chi := 2 ||[H_u,H_d]||_F^2/(Delta_u^2 Delta_d^2).
```

For a real relative rotation with `t=|V_cb|^2`,

```text
chi = 4 t(1-t).                                          (4.4)
```

The five-sixths law would require

```text
chi(R) = 4 R^(5/3) (1-R^(5/3)).                         (4.5)
```

The direct overlap trace is the primary readout because (4.4) alone has the
branch ambiguity `t <-> 1-t`.

## 5. Exact down-only boundary

**Theorem 2.** Let `Phi(H_d)` be any unitarily equivariant construction and
let `rho(Phi(H_d))` be any conjugacy-invariant scalar readout. Then the
composition is a class function of `H_d`; it cannot equal physical `|V_cb|`
for every nondegenerate pair `(H_u,H_d)`.

**Proof.** Fix a positive diagonal `H_d=D_d` and distinct positive up-sector
eigenvalues. Vary only the relative up-sector orientation,

```text
H_u(theta) = R_23(theta) D_u R_23(theta)^dagger.         (5.1)
```

The input `H_d`, its spectrum, every down-only spectral invariant, and hence
`rho(Phi(H_d))` remain fixed. But the projector theorem gives

```text
Tr(P_c^u(theta) P_b^d) = sin(theta)^2,
|V_cb| = |sin(theta)|,                                  (5.2)
```

which varies continuously. This contradicts a universal down-only
factorization.

A fixed external projector can evade the proof only by supplying an
orientation reference. The input is then `(H_d,P_ref)`, not down-only, and the
origin and physical typing of `P_ref` become separate theorem obligations.

This theorem does not rule out pair-based source/action dynamics, a derived
up-sector projector, paired NNI textures, or another orientation-carrying
construction. It rules out only the universal equivariant/invariant
down-only class.

## 6. Carrier-type audit

The parent's six-state `rank-(1+5)` determinant is an abstract conjugacy-class
construction. Nearby CKM atlas prose places a `1+5` split on the six states of
the weak-isospin by color block `Q_L=(2,3)`. In contrast, `H_u` and `H_d` act
on three-dimensional generation flavor. No theorem cited here identifies
those spaces or lifts `m_s/m_b` into the fivefold gauge complement.

The reduced STRC carrier also does not provide that lift: its displayed
`H_(1+5)=span{e_1,e_5}` is two-dimensional, with the five-channel represented
by one reduced axis. Treating that reduced axis as five independent mass
eigenvalues would add the missing lift by hand.

Accordingly, this note does not consume the atlas or STRC surfaces as
load-bearing dependencies; their carrier types do not supply (1.2).

## 7. What moved and what remains open

Established exactly here:

1. the phase-free, basis-covariant map from a supplied mass-operator pair to
   every CKM modulus;
2. the exact invariant statement of the five-sixths alignment target;
3. the universal down-only equivariant/invariant route obstruction;
4. the distinction between the generation-flavor overlap determinant and the
   abstract six-state normalized determinant.

Still open:

1. derivation of physical `M_u` and `M_d` from framework source/action data;
2. a dynamical theorem forcing (1.2) or (4.5);
3. a derived generation-to-six-state carrier lift, if that route is pursued;
4. absolute quark masses, RG transport, and empirical comparison.

The current claim is one bounded row with an exact support result and an exact
scoped boundary. Theorem 2 is not proposed as a separate `no_go` claim row.
This is not the physical five-sixths bridge and does not permit retained-grade
proposal language.

## 8. Verification

Run:

```bash
python3 scripts/frontier_ckm_mass_operator_projector_overlap_typing.py
```

The runner verifies the Lagrange projectors, overlap identity, weak-basis
covariance, compressed determinant, five-sixths equivalence, two-family
commutator formula, and explicit down-only countermodels using exact symbolic
or rational algebra. It contains no observed mass or CKM target value.
