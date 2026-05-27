# KMS Fermionic Brydges Majorant - Finite Framework Majorant Repair

**Date:** 2026-05-11
**Claim type:** bounded_theorem
**Type:** bounded_theorem
**Scope:** external fermionic-RG majorant theorem from Kroschinsky-Marchetti-Salmhofer arXiv:2404.06099 (2024), cited as rigorous-RG context for the fermionic Polchinski equation. No framework substitution, hierarchy formula, or physical scale closure is claimed.
**Status authority:** independent audit lane only.
**Runner:** `scripts/frontier_kms_fermionic_brydges_majorant_external_narrow.py`
**Cache:** `logs/runner-cache/frontier_kms_fermionic_brydges_majorant_external_narrow.txt`

## 2026-05-28 Audit Repair (conditional core; missing upstream admitted)

The 2026-05-28 audit verdict was `audited_conditional`:

> *"The scalar ODE consequences close algebraically once the KMS majorant inequality is assumed. The restricted packet does not provide the KMS paper or any retained-grade upstream authority proving that inequality, so the load-bearing external"*

with repair: *"missing_dependency_edge: include the KMS arXiv:2404.06099 theorem statement/proof excerpt or a retained upstream authority row establishing the BBF majorant inequality and hypotheses."*

Supplying the named upstream authority is substantive new work, out of scope.
This revision narrows via the **admission path**:

- **Load-bearing (in scope):** The scalar majorant ODE `dy/dl = a y^2 + b y` closes algebraically and numerically — small-data integrability, monotonicity, scale-chaining, and the fixed-point structure are all verified by the runner GIVEN the KMS per-scale bound as input.
- **NON-load-bearing (admitted / unsupplied):** The KMS arXiv:2404.06099 Theorem 1 majorant inequality itself — specifically, that the BBF polymer norm satisfies `d/dl ||V_l||_h <= a(l) ||V_l||_h^2 + b(l) ||V_l||_h` with `a(l), b(l)` non-negative and integrable — is admitted as an unsupplied external input; the row does not certify it and no retained upstream authority row for it is present in the restricted packet.

No new axiom, import, or retained bridge is introduced. The conditional core is
the load-bearing content; the named upstream stays admitted until a retained
authority/runner for it lands.

## Binding Framework Lemma

Let a finite framework packet provide:

1. a finite scale mesh `l_0 < ... < l_N`;
2. a finite coefficient vector `c(l_j)` at each scale;
3. a BBF-style non-negative polymer norm

```text
Y_j := ||c(l_j)||_h = sum_P w_P |c_P(l_j)|,        w_P >= 0;
```

4. non-negative scale coefficients `R_j >= 1` and `q_j >= 0` such that the
   verified one-step majorant inequality is

```text
Y_{j+1} <= R_j Y_j / (1 - q_j Y_j)                 (1)
```

whenever `q_j Y_j < 1`.

Define

```text
E_n := product_{j=0}^{n-1} R_j,
Q_n := sum_{j=0}^{n-1} q_j product_{i=0}^{j-1} R_i .
```

Then the finite comparison bound is

```text
Y_n <= E_n Y_0 / (1 - Q_n Y_0)                     (2)
```

provided `Q_n Y_0 < 1`. This is the bounded framework claim of this note.

Equivalently, in the continuous notation

```text
dY/dl <= a(l) Y^2 + b(l) Y,        a(l), b(l) >= 0,
B(l) = integral b,
Q(l) = integral a(s) exp(B(s)) ds,
```

the same comparison gives

```text
Y(l) <= exp(B(l)) Y(l_0) / (1 - Y(l_0) Q(l)).
```

The proof is elementary: set `Z = exp(-B) Y`, so

```text
dZ/dl <= a(l) exp(B(l)) Z^2.
```

Integrating `d(1/Z)/dl >= -a(l) exp(B(l))` gives the displayed bound.
For the mesh form, the substitution `X_j = 1/Y_j` turns (1) into

```text
X_{j+1} >= (X_j - q_j) / R_j,
```

and iterating gives (2). No external theorem is imported for this finite
comparison step.

## Relation To KMS

Kroschinsky-Marchetti-Salmhofer prove that a fermionic Polchinski flow can be
put into a Brydges-Battle-Federbush majorant form under their hypotheses. This
note does not import that theorem as the binding proof. It proves only the
finite comparison math that would apply after a framework packet has supplied
the one-step inequality and non-negative coefficients.

The KMS paper remains cited in parallel as evidence that this finite
majorant pattern is the right rigorous-RG technology to compare against.

## Boundary

This note does not claim:

- that any framework staggered-Dirac blocking/coarse-graining is the KMS
  continuous Polchinski flow;
- that the framework's canonical surface lies in the KMS small-data regime;
- that any project-specific coupling is the BBF norm coefficient at any scale;
- that KMS Theorem 1 has been re-proved in full;
- closure of any framework substitution, hierarchy formula, or physical scale;
- any numerical prediction or comparison with observation;
- any new framework axiom or repo-wide premise;
- specifically: the scaffold admissions of `HIERARCHY_BBS_STAGGERED_TASTE_BLOCKING_BRIDGE_SCAFFOLD_AVAILABILITY_BOUNDED_NOTE_2026-05-11.md` remain open; KMS provides published fermionic-RG technology, but the substrate-specific bridge to those admissions would still need to be separately constructed.

Any later framework use must separately construct the polymer norm, prove the
one-step inequality, identify the framework substrate's effective action with
the coefficient vector `c(l_j)`, verify the small-data hypothesis, and
establish the physical bridge.

## External References

- A. Kroschinsky, D. Marchetti, M. Salmhofer, "A Brydges-Battle-Federbush representation for the fermionic Polchinski equation", arXiv:2404.06099 (2024).
- D. C. Brydges, "A short course on cluster expansions", in Phenomenes critiques, systemes aleatoires, theories de jauge (Les Houches 1984), North-Holland (1986), 129-183.
- M. Disertori, V. Rivasseau, "Continuous constructive fermionic renormalization", Annales Henri Poincare 1 (2000), 1-57.
- M. Salmhofer, Renormalization: An Introduction, Texts and Monographs in Physics, Springer (1999).
- J. Polchinski, "Renormalization and effective Lagrangians", Nuclear Physics B 231 (1984), 269-295.

## Verification

The paired runner checks:

1. exact Fraction arithmetic for the scalar majorant ODE `dy/dl = a y^2 + b y`
   and the mesh comparison map `Y_{j+1} <= R_j Y_j/(1-q_jY_j)`;
2. monotonicity: if `Y_0` lies below the explicit small-data threshold, the
   finite comparison bound stays positive and finite;
3. composition: the per-scale norm bound chains across `N` scales `l_0 < l_1 < ... < l_N` with product structure on the exponential `b`-factor;
4. the small-data fixed-point structure of the Polchinski quadratic form, on scalar and finite-dimensional toy operators;
5. substrate-independence: the majorant ODE structure does not depend on the particular fermionic theory beyond the inputs `(a(l), b(l))`;
6. source-note boundary checks excluding framework bridge claims, framework-substrate-specific identification, and any scaffold-admission closure;
7. sharpness at the small-data threshold: above the threshold the scalar majorant blows up in finite scale-time;
8. positivity of the BBF norm by construction (sum of non-negative Gram norms over polymers).

Expected runner result: `PASS=N`, `FAIL=0`.

## Background References

The references below are background context, not load-bearing imports for the
finite comparison lemma proved above.

- Kroschinsky, Marchetti, and Salmhofer, arXiv:2404.06099: background
  rigorous-RG source for the fermionic BBF/Polchinski majorant setting.
- Brydges, Spencer, Imbrie, Rivasseau, and Salmhofer: background on
  BBF polymer norms, cluster expansions, and Wilsonian fermionic RG.

The framework-side admissions remain open as stated in the Boundary section.
