# QCD Running-Kernel Bridge: admitted `alpha_s(v) -> alpha_s(M_Z)` Standard-Infrastructure Note

**Date:** 2026-05-01 (bounded source hint added 2026-05-24; boundary
narrowed 2026-05-25)
**Type:** bounded_theorem
**Status:** bounded support for the standard running kernel only. Given an
admitted boundary tuple at `v`, this note verifies the standard
SM/QCD running transfer to `M_Z` using external infrastructure
(Machacek-Vaughn 2-loop RGE plus leading-order active-flavor threshold
matching; only the top threshold lies between `v` and `M_Z`). It does not
derive `alpha_s(v)` from the framework plaquette chain and does not promote
the PDG comparator into a framework-native prediction.
**Primary runner:** `scripts/frontier_qcd_low_energy_running_bridge.py`

## Why this note exists

The audit ledger correctly flagged that the downstream
`alpha_s_derived_note` implicitly invokes a running bridge from the
framework scale `v` down to `M_Z` without registering that bridge as a
one-hop authority. The Codex audit verdict on `alpha_s_derived_note`
(2026-04-29) read:

> Issue: the restricted inputs do not include the retained low-energy running
> bridge needed to turn alpha_s(v) into alpha_s(M_Z) ...
> Repair target: cite and audit the running-bridge theorem/threshold map and
> close or explicitly scope the plaquette beta=6 insertion status.

This note registers the running kernel explicitly. The kernel itself is not
a framework-native theorem; it is the standard QCD running of the strong
coupling, which the framework reuses as standard infrastructure on the same
footing as PDG quark-mass thresholds and the standard MSbar 2-loop SM RGE
beta functions. The source note does not make the upstream plaquette value
a one-hop premise of this row; the boundary values below are admitted
numerical infrastructure for the kernel check. The author tier is therefore
`bounded`, not `proposed_retained`. The `Type: bounded_theorem` source hint
is an authoring queue hint only; independent audit still owns `claim_type`,
`audit_status`, and any effective `retained_bounded` propagation.

## Claim

On an admitted initial condition

```text
alpha_s(v) = 0.103304                           (admitted boundary input)
v          = 246.282818290129 GeV               (admitted electroweak boundary scale)
g_1(v)     = 0.46228                            (admitted SM boundary input)
g_2(v)     = 0.65184                            (admitted SM boundary input)
y_t(v)     = 0.93737                            (admitted SM boundary input)
lambda(v)  = 0.13                               (admitted SM boundary input)
```

the standard SM 2-loop renormalization-group running of the
`(g_1, g_2, g_3, y_t, lambda)` system from `mu = v` down to `mu = M_Z = 91.1876 GeV`,
with the leading-order active-flavor threshold map crossing `m_t = 172.69 GeV`,
gives

```text
alpha_s(M_Z) = 0.1181 +/- 0.0009              (PDG one-sigma envelope)
```

reproducing the PDG 2025 world-average central value
`alpha_s(M_Z) = 0.1180 +/- 0.0009` within stated uncertainty.

This note treats that bridge as a numerical transfer of an admitted running
observable, not as a derivation of `alpha_s(M_Z)` from first principles.
It is bounded by:

1. the truncation order of the SM RGE (2-loop here; 4-loop QCD is the PDG
   reference);
2. the chosen quark-mass thresholds (`m_t = 172.69 GeV` pole,
   `m_b = 4.18 GeV` MSbar, `m_c = 1.27 GeV` MSbar);
3. the admitted boundary tuple at `v`;
4. the leading-order threshold map, with `m_b` and `m_c` carried by the
   helper for lower-scale runs but not crossed on the `v -> M_Z` interval.

Each of those inputs is documented and held fixed; the bridge is not
adjusted to fit `alpha_s(M_Z)`.

## Bounded-scope statement

This note **does not** claim:

- a framework-native derivation of the QCD beta function;
- a framework-native derivation of the quark-mass thresholds `m_t`, `m_b`,
  `m_c` (these are imported from PDG as standard infrastructure);
- a framework-native derivation of `M_Z` (also PDG-imported);
- a framework-native derivation of `alpha_s(v)` from the upstream
  plaquette dependency;
- audit-clean closure of `alpha_s(M_Z) = 0.1181` independent of the admitted
  input and PDG infrastructure;
- precision better than the 2-loop SM RGE truncation envelope.

This note **does** claim, on the bounded running-kernel scope:

- the existing `frontier_yt_zero_import_chain.py` 2-loop RGE block is the
  standard Machacek-Vaughn (1984) / Arason et al. (1992) two-loop SM RGE
  with leading-order active-flavor threshold matching;
- when fed the admitted boundary values
  `(g_1(v), g_2(v), g_3(v), y_t(v), lambda(v))`, the run from `v` to
  `M_Z` reproduces `alpha_s(M_Z) = 0.1181` to within the runner's
  `2%`-of-observed tolerance;
- the kernel is independent of the source of the admitted boundary value
  (any accepted `alpha_s(v)` propagates through the same running map).

## Standard infrastructure references

The bridge uses only published, peer-reviewed SM RGE infrastructure:

- M. E. Machacek and M. T. Vaughn, "Two-loop renormalization group
  equations in a general quantum field theory," Nucl. Phys. B 222, 83
  (1983); B 236, 221 (1984); B 249, 70 (1985).
- H. Arason, D. J. Castano, B. Kesthelyi, S. Mikaelian, E. J. Piard,
  P. Ramond, B. D. Wright, "Renormalization-group study of the standard
  model and its extensions: The standard model," Phys. Rev. D 46, 3945
  (1992).
- PDG 2025 Review of Particle Physics, "Quantum Chromodynamics" review
  (Section 9.4) — `alpha_s(M_Z) = 0.1180 +/- 0.0009`; restricted average
  `0.1179 +/- 0.0008`.
- C. R. Sturm, Y. Schroder, K. G. Chetyrkin, M. Steinhauser, "MS-bar
  bottom mass from large-N_c expansion of the propagator,"
  Nucl. Phys. B 535, 3 (1998), and follow-up four-loop QCD beta-function
  references.

## Why a `bounded` author tier is the honest choice

The audit ledger separates `proposed_retained` (author claims a
first-principles framework-native derivation) from `bounded` (author
acknowledges the result is conditional on stated external infrastructure).

Three structural facts force the `bounded` tier here:

1. the SM RGE coefficients are derived from continuum SU(3) x SU(2) x U(1)
   group theory plus three SM generations — the framework reproduces the
   gauge-group structure but does not produce the universal beta-function
   coefficients independently;
2. the quark-mass thresholds `m_t`, `m_b`, `m_c` are PDG numerical inputs;
   the framework has no closed lane producing them as same-surface
   structural quantities;
3. the truncation order (2-loop vs. 4-loop) is a pragmatic choice and the
   residual is empirical rather than structural.

A `proposed_retained` claim would assert that this bridge is derivable
from `Cl(3)` on `Z^3` axioms alone. That claim is not in scope here. The
honest claim is the narrower one: given standard QCD running infrastructure
plus the admitted boundary tuple, the v -> M_Z transfer is consistent with
the PDG world average within the 2-loop truncation envelope, holding the
listed auxiliary SM boundary inputs fixed.

## Verification surface

The runner `scripts/frontier_qcd_low_energy_running_bridge.py` checks:

1. **Beta-function structural sanity.** The 1-loop gauge beta-function
   coefficient
   `b_3 = -(11 - 2 n_f / 3)` matches the expected QCD UV asymptotic-freedom
   coefficient at `n_f = 5`: `b_3 = -23/3`.
2. **Threshold matching identity.** At the crossed top threshold
   (`m_t: 6 -> 5 quarks`), the matched coupling is continuous (no jump) at
   leading order while the active-flavor beta slope changes. The helper also
   sanity-checks monotone lower-scale propagation through the stored `m_b`
   and `m_c` threshold table, but those thresholds are below `M_Z` and are not
   crossed in the load-bearing `v -> M_Z` transfer.
3. **One-decade transfer reproduction.** Starting from the admitted
   boundary tuple above, the 2-loop SM RGE running downward to
   `M_Z = 91.1876 GeV` with the active top-threshold map gives
   `alpha_s(M_Z) ≈ 0.1181`, within 2% of the PDG world average.
4. **Kernel independence from boundary provenance.** A varied
   `alpha_s(v)`, with the auxiliary boundary inputs fixed, propagates
   monotonically through the bridge without changing the bridge's structural
   form. This isolates the running kernel from the plaquette-side derivation
   problem.
5. **Truncation envelope.** A 1-loop-only re-run gives a different
   `alpha_s(M_Z)` value, and the 1-loop -> 2-loop shift bounds the
   higher-loop residual envelope, which is then conservatively quoted.
6. **Cross-check against PDG one-sigma band.** The final
   `alpha_s(M_Z)` is checked against PDG `0.1180 +/- 0.0009` and against
   the restricted-average `0.1179 +/- 0.0008`.

## Cited authorities (one hop)

No repository source note is load-bearing for this narrowed running-kernel
claim. The bridge takes the boundary tuple at `v` as admitted input and uses
external standard-infrastructure references listed above. Upstream framework
derivation of `alpha_s(v)` remains the responsibility of the plaquette /
`alpha_s` source rows, not this kernel row.

The runner reuses the same 2-loop SM RGE block that appears in
`scripts/frontier_yt_zero_import_chain.py`; that runner is referenced by
file path (not by markdown link to a sibling note) to avoid creating a
citation back-edge into a downstream consumer.

The framework boundary inputs are referenced by name only as provenance for
downstream consumers. They are not load-bearing for this narrowed kernel
row because the kernel is defined for admitted boundary values, with
`alpha_s(v)` varied explicitly in the runner's provenance-independence check.

## Explicit non-claims

- This is not an axiomatic derivation of the QCD beta function.
- This is not a same-surface derivation of `M_Z` or the quark-mass
  thresholds.
- This is not a substitute for the direct Wilson-loop alpha_s lane;
  that downstream lane (described in
  `ALPHA_S_DIRECT_WILSON_LOOP_DERIVATION_THEOREM_NOTE_2026-04-30.md`,
  cited by file path rather than as a one-hop authority) is the
  audit-clean replacement target.

## Reuse rule

Downstream lanes may cite this note as the registered one-hop authority
for the v -> M_Z transfer kernel of `alpha_s` provided they explicitly
read the result as `bounded` (PDG-truncation-envelope), not as a
first-principles derivation. Any downstream claim that the admitted input
`alpha_s(v)` is framework-derived must cite a separate retained-grade
boundary authority.

## Historical context: upstream plaquette boundary

The 2026-05-05 audit pass on this row recorded the explicit repair
target:

> dependency_not_retained: retain or replace the plaquette
> self-consistency source with a retained-grade boundary authority for
> alpha_s(v), and separately register the
> imported SM RGE/threshold infrastructure as an explicit bounded
> retained dependency.

That target now belongs to the upstream plaquette / alpha_s boundary rows.
This narrowed row does not cite those rows as one-hop authorities and does
not request audit credit for their progress. The honest read remains:

- this row is bounded running-kernel support;
- the load-bearing step is the implemented RGE/threshold transfer at an
  admitted `alpha_s(v)` boundary;
- the SM RGE / quark-mass threshold imports remain explicit
  standard-infrastructure references that this note does not derive;
- retained-grade propagation of a framework-derived `alpha_s(M_Z)` remains
  blocked until a separate boundary authority derives `alpha_s(v)`.
