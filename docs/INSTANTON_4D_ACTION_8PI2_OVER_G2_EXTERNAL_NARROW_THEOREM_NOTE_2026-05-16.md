# 4D Instanton Action `8π²/g²` — Bounded Normalization Certificate

**Date:** 2026-05-16; scope repair 2026-05-29
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only.
**Primary runner:** [`scripts/frontier_instanton_4d_action_8pi2_over_g2_external_narrow.py`](../scripts/frontier_instanton_4d_action_8pi2_over_g2_external_narrow.py)
**Cache:** [`logs/runner-cache/frontier_instanton_4d_action_8pi2_over_g2_external_narrow.txt`](../logs/runner-cache/frontier_instanton_4d_action_8pi2_over_g2_external_narrow.txt)

## 2026-05-29 Audit Repair

The audit verdict was `audited_conditional` because the previous packet mixed a
bounded action-normalization certificate with a broader external instanton
package:

```text
scope_too_broad:
narrow the binding Statement and Upstream authority paragraph to the finite
Bogomolny/BPST-normalization certificate, or add a retained-grade authority
packet for Atiyah-Singer integrality, BPST existence, and Luescher
lattice-topology preservation; refresh the runner metadata check to match
bounded_theorem.
```

This revision takes the narrow path. The binding claim is only the bounded
algebraic/arithmetic certificate for the standard charge-one self-dual
normalization:

```text
S_inst = 8 π² / g².
```

The global Atiyah-Singer integrality theorem, BPST existence theorem, and
Luescher lattice-topology preservation theorem are external context only. They
are not retained-grade inputs in this row and are not needed for the narrowed
certificate.

## Claim

Assume the standard Euclidean Yang-Mills normalization:

```text
S[A] = (1 / (4 g²)) ∫ d⁴x Tr(F_μν F^μν),
Q    = (1 / (32 π²)) ∫ d⁴x Tr(F_μν *F^μν).
```

Also assume the Bogomolny/self-duality normalization for a supplied
charge-one self-dual sector:

```text
S[A] ≥ (8 π² / g²) |Q|,
F = *F, Q = 1  =>  saturation.
```

Then the minimal supplied charge-one self-dual action in this normalization is

```text
S_inst = 8 π² / g².
```

The runner verifies this symbolic specialization, the self-dual saturation
identity, and numerical evaluations at:

| `g²` | `S_inst` |
|---:|---:|
| `1/2` | `16 π² ≈ 157.913670` |
| `1` | `8 π² ≈ 78.956835` |
| `2` | `4 π² ≈ 39.478418` |

This is a bounded normalization certificate. It does not prove that the
framework has an instanton sector, that `Q` is integer for all smooth
configurations, that a BPST solution exists in a retained framework carrier, or
that a lattice topological sector is preserved under admissibility/flow.

## Explicit Non-Claims

This note does **not** claim:

- retained Atiyah-Singer integrality for all smooth finite-action SU(N)
  configurations;
- retained BPST existence or multi-instanton existence;
- retained Luescher lattice-topology preservation, Wilson-flow extraction, or
  continuum-limit `O(a²)` control;
- identification of any framework substrate with a 4D SU(N) gauge background;
- closure of any framework substitution, hierarchy formula, scale ratio, or
  physical observable;
- closure of `α_LM^16` or any framework `α^N` hierarchy at integer `N`;
- derivation of `v/M_Pl` or any dimensional scale ratio;
- a numerical comparison with observation;
- a new framework axiom or repo-wide premise.

Any later framework use must separately identify the framework substrate with
the 4D SU(N) gauge background, identify a framework observable with the
instanton sector, and verify the substrate-specific bridge.

## External Context

The following are useful published background references but are not
load-bearing retained authorities for this narrowed row:

- A. A. Belavin, A. M. Polyakov, A. S. Schwartz, Y. S. Tyupkin,
  "Pseudoparticle Solutions of the Yang-Mills Equations",
  Phys. Lett. B **59** (1975) 85.
- G. 't Hooft, "Computation of the Quantum Effects Due to a
  Four-Dimensional Pseudoparticle", Phys. Rev. D **14** (1976) 3432;
  erratum Phys. Rev. D **18** (1978) 2199.
- M. F. Atiyah, I. M. Singer, "The Index of Elliptic Operators I-V",
  Ann. Math. **87** (1968) 484-604; **93** (1971) 119-149; **93**
  (1971) 546-604.
- M. Luescher, "Topology of lattice gauge fields",
  Commun. Math. Phys. **85** (1982) 39.
- M. Luescher, "Properties and uses of the Wilson flow in lattice QCD",
  JHEP **08** (2010) 071; arXiv:1006.4518.

## Verification

The paired runner checks:

1. **T1:** symbolic supplied-normalization specialization
   `S_inst = 8 π²/g²` at `Q = 1`;
2. **T2:** global Atiyah-Singer/BPST/Luescher inputs are explicitly
   non-load-bearing in this row;
3. **T3:** numerical `S_inst` at `g² ∈ {1/2, 1, 2}`;
4. **T4:** numerical `exp(-S_inst)` at the same `g²` values;
5. **T5:** canonical `g² = 1` value and suppression;
6. **T6:** self-duality saturation identity under supplied normalizations;
7. **T7:** any lattice-topology/admissibility language is context only and
   not a retained preservation theorem;
8. **T8:** note declares `bounded_theorem`;
9. **T9:** no framework-substrate identification is claimed;
10. **T10:** no `α_LM^16`, hierarchy, or `v/M_Pl` closure is claimed.

Expected runner result: `PASS=N`, `FAIL=0`.

## Upstream Authority

- [`TOPOLOGICAL_INSTANTON_TEXTBOOK_INFRASTRUCTURE_IMPORT_NOTE_2026-05-17.md`](TOPOLOGICAL_INSTANTON_TEXTBOOK_INFRASTRUCTURE_IMPORT_NOTE_2026-05-17.md)
  is used only for bounded Hodge/Bogomolny and BPST normalization context. It
  is not cited here as retained authority for global Atiyah-Singer integrality,
  BPST existence, or Luescher lattice-topology preservation.
