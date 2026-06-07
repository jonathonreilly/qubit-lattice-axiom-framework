# No Hidden Carrier Symmetry Forbids the Marginal Lorentz Operator: Closure (i) Fails (No-Go)

**Date:** 2026-06-06
**Claim type:** no_go (structural, systematic enumeration)
**Type:** no_go
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome. The label is a source-side claim-boundary declaration.
**Primary runner:**
[`scripts/frontier_no_hidden_carrier_symmetry_forbids_lorentz_marginal_2026_06_06.py`](../scripts/frontier_no_hidden_carrier_symmetry_forbids_lorentz_marginal_2026_06_06.py)
**Cached runner output:**
[`logs/runner-cache/frontier_no_hidden_carrier_symmetry_forbids_lorentz_marginal_2026_06_06.txt`](../logs/runner-cache/frontier_no_hidden_carrier_symmetry_forbids_lorentz_marginal_2026_06_06.txt)

---

## Role

This note closes the last framework-native constructive target of the
Lorentz-naturalness obstruction. The quantified obstruction
[`LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06.md`](LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06.md)
(#3123) named three escapes: **(i)** a hidden symmetry of the `Cl(3,0)/Z³ +
continuous-time` carrier that forbids the marginal `c`-operator; **(ii)** an
admitted custodial / `c_t=c_s` axiom; **(iii)** an interacting strong-coupling CFT.
The companion `RECORD_CANNOT_PROTECT_LORENTZ_MARGINAL_COUPLING_NO_GO_NOTE_2026-06-06`
(#3126) showed the custodial symmetry, if it exists, must come from **Quantum/Lattice**,
not Record. This note **systematically searches Quantum/Lattice** and finds: **closure
(i) fails.** No carrier symmetry forbids the operator. Runner **16 PASS / 0 FAIL**.

This is a decisive negative that **completes the enumeration**: only (ii) [a new
axiom] or (iii) [precluded by asymptotic freedom] remain.

## The single sharpest reason

The marginal operator `O_c = ψ̄ γ^i (c_s − c_t) ∂_i ψ` (the SME `c`-trace, the
`c_t/c_s` velocity split, equivalently species max-speed differences) is a
**Lorentz scalar**: dimension-4, CPT-even, P-even, `O_h`-even, gauge-singlet,
chiral-even. A symmetry forbids an operator only if the operator is **odd** under
it. `c_t/c_s` is odd **only** under a transformation that **mixes the time axis with
a space axis** (a `(t,x)` rotation = the boost / SO(4) generator). Every carrier
symmetry of the framework acts either

- **purely within the 3 spatial axes** — `O_h` (spatial signed-permutations), and
  the internal `su(2)` which *is* the spatial rotations via the internal–external
  merger; or
- **purely on the fiber** — gauge `SU(3)×U(1)`, the `U(1)` phase, the chiral
  `γ₅`/staggered `ε(x)`, CPT —

and **none mixes time with space**, because the framework's time is a *separate
continuous* structure, **not** a lattice axis. The only symmetry that would forbid
`O_c` is the `t↔x` symmetry — the fourth signed-permutation direction the `Z³`
(spatial) Lattice axiom **structurally denies**, i.e. exactly the new axiom (ii).

## The systematic enumeration (runner)

| Carrier symmetry | acts on | `O_c` even/odd | forbids `O_c`? |
|---|---|---|---|
| `O_h` (spatial signed-perms) + time-parity | 3 spatial axes | **even** (invariant dim 2 = `c_t,c_s`) | no |
| internal `su(2)` = inner `Cl(3,0)` Aut | the fiber (= spatial rot via merger) | **even** (`c_s` magnitude invariant) | no |
| gauge `SU(3)×U(1)`, `U(1)` phase | colour/charge index | **even** | no |
| chiral `γ₅` / staggered `ε(x)` | the chiral grading | **even** | no |
| CPT (the `K`/CPT readout) | spacetime+conjugation | **even** (its power is exhausted on the CPT-*odd* sector) | no |
| Cl(3,0)→Cl(3,1) Clifford normalization | — | per-generator rescaling preserves `{γ,γ}=2η` → the metric ratio is **free** | no |
| SUSY-analog (boson↔fermion velocity tie) | — | **absent** (fermions=site-qubits, bosons=link-variables; no substrate map) | n/a |
| **`t↔x` boost / SO(4) (B₄ hypercubic)** | mixes time & space | **odd** | **yes — but = the absent 4th lattice axis** |

Concretely (runner): under `O_h × time-parity` the velocity coefficients
`(c_t,c_x,c_y,c_z)` have invariant dimension **2** (`c_t, c_s`) — the split survives;
only `B_4` (which contains `t↔x`) collapses to dimension **1**. The internal `su(2)`
and gauge leave the Lorentz-scalar velocity magnitude invariant. The Clifford
algebra fixes the velocity-operator *direction* (`σ_i²=I`, eigenvalues `±1`) but the
coefficient `c_s` is a free rescaling (`σ_i → c_s σ_i` preserves `{·,·}=2c_s²δ`), so
the metric ratio `c_t/c_s` is not fixed by the algebra. The unique generator under
which the split `c_t − c_s` is odd is the `(t,x)` swap.

## Why the obvious candidates fail (one line each)

- **SUSY** (the *known* custodial route, Nibbelink–Pospelov): the framework has no
  boson–fermion symmetry — the one mechanism that ties gauge-boson to fermion
  velocities is structurally absent.
- **The RG attractor** (#3121): drags `v_F, v_b` together *dynamically* (`η→1`), but
  that is an attractor, not a symmetry forbidding the operator — the UV mean-shift
  survives it (Collins).
- **Emergent CFT** (closure iii): conformal symmetry contains Lorentz but needs
  `γ~1` strong coupling at the regeneration scale; asymptotic freedom gives
  `γ~0.1–0.24` (#3123). Precluded.
- **The free-staggered SO(4)** (`lorentz_boost_..._so4`): an *emergent continuum*
  (`a→0`) property of the free 2-point function — **not** a finite-`a` carrier
  symmetry, so it cannot protect a coupling against UV regeneration.

## Verdict

**Closure (i) is foreclosed.** No hidden symmetry of the `Cl(3,0)/Z³ +
continuous-time` carrier forbids the marginal `c`-operator, because that operator is
a Lorentz scalar and every carrier symmetry acts within-space or on the fiber — none
mixes time with space (time is continuous, not a lattice axis). Combined with #3126
(Record cannot do it either), the Lorentz-naturalness custodial mechanism must be
**either (ii) an admitted `c_t=c_s` axiom** (the 4th signed-permutation / SO(4)-hypercubic
direction the `Z³` axiom denies — strictly a new postulate) **or (iii) a
strong-coupling CFT** (precluded by the framework's asymptotic freedom). The
enumeration of framework-native escapes is complete and empty.

## What this note does NOT claim

- It does **not** claim the framework is inconsistent — only that the Lorentz-
  naturalness residual has no existing-structure custodial symmetry.
- It does **not** contradict #3123, #3126, #3121, the tree-level dissolution, or the
  retained emergent-Lorentz / boost-from-bivectors notes (the boost generators close;
  the issue is the *coefficient*, not the algebra).
- **No** new axiom, primitive, repo vocabulary, or class tag; **no** PDG/fitted/`β=6`/
  `g_bare` input. It does **not** set or change any audit status.

## No-go discipline (N1–N8 summary)

- **N1 routes:** every carrier symmetry class (spacetime / internal / gauge / Clifford
  / chiral / CPT / SUSY-analog / emergent-CFT / novel) enumerated and excluded; the
  only forbidder is `t↔x` = the absent axiom. **N2:** the exclusion is independent
  across classes (each fails for its own reason). **N7 steelman:** the SUSY-analog and
  the emergent-SO(4) are the strongest positive candidates; both fail (no substrate
  boson–fermion map; SO(4) is `a→0`-emergent, not a carrier symmetry). **N3/N5/N6:**
  "closure (i) fails" means precisely "the `c`-operator is even under every carrier
  symmetry"; not an inconsistency claim.

## Reprove-and-cite ledger

- **Reproven here** (runner): the `O_h`/`B_4` velocity-coefficient invariant dims
  (2 vs 1); the internal-`su(2)`/`U(1)` invariance of the velocity magnitude; the
  Clifford per-generator rescaling freedom (`σ_i²=I` fixes direction not coefficient);
  the `t↔x` odd-ness of the split; the SUSY-analog absence.
- **Cited** (comparator/scope only): `RECORD_CANNOT_PROTECT_LORENTZ_MARGINAL_COUPLING_NO_GO`
  (#3126), `LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION` (#3123),
  `EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR` (#3121), the internal–external
  `su(2)` merger, `koide_onsite_weyl_boost_from_bivectors`, the free-staggered SO(4)
  note; Collins et al *PRL* 93 (2004) 191301; Nibbelink–Pospelov hep-ph/0502106.

## Audit dependency repair links

This section records explicit dependency links for the audit citation graph. It does
not promote this note or change any audited claim scope.

- [LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06.md](LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06.md)
- [SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md](SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md)
- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)
- `RECORD_CANNOT_PROTECT_LORENTZ_MARGINAL_COUPLING_NO_GO_NOTE_2026-06-06.md` (the companion #3126; not yet on main — backticked to avoid a broken citation-graph edge)

### Source-note boundary

**Hypothesis set:** (1) the three axioms (Lattice `Z³` spatial, Quantum `Cl(3,0)`,
Record), continuous time native; (2) the framework's gauge `SU(3)×U(1)`, staggered
chiral `ε(x)`, internal–external `su(2)` merger, and Cl(3,0)→Cl(3,1) boost structure;
(3) the marginal `c`-operator as the residual of #3123/#3126. The result is a
systematic finite-group / algebraic symmetry enumeration.

**Forbidden-imports check:** no new axiom, primitive, repo vocabulary, or class tag;
only standard terms (signed-permutation group, invariant, Clifford rescaling, Lorentz
scalar, custodial symmetry, SUSY). No fitted/PDG/`β=6`/`g_bare` value consumed.

**No-promotion statement:** this note does **not** promote, demote, or set the audit
status of #3123, #3126, #3121, or any upstream row. The audit lane is the only status
authority.
