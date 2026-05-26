# Dependency Map — Existing Dynamics-Lane Chain Tagged Native vs Import

**Date:** 2026-05-26
**Lane:** `dynamics-lane-native-axioms-only-20260526`
**Status:** **research-lane mapping artifact.** Not a theorem note. Not for landing.
**Purpose:** Trace every step in the existing dynamics-lane chain (from A1+A2 to
the lepton/quark mass observable and the δ=2/9 question) and tag each step
NATIVE / RETAINED-CITATION / IMPORT-REQUIRED / DEMOTED. Identifies what is
salvageable using only A1+A2 + retained inventory, and where the chain hits
non-derivable imports.

## Legend

- **NATIVE** = follows from A1+A2 directly using standard mathematics (no further
  framework content needed).
- **RETAINED** = cited from an `origin/main` retained source-note; usable in this
  lane without further import.
- **IMPORT** = requires content outside A1+A2+retained inventory; cannot be used
  in this lane. The specific import is named.
- **DEMOTED** = was in the M-work chain but the supporting note has been retracted
  / rejected; cannot be cited as authoritative here.

## Chain 1 — Lepton-sector kinematic shape (from A1+A2 to `cos(δ + 2πk/3)`)

| # | Step | Tag | Source / required import |
|---|---|---|---|
| K1 | Per-site site algebra is `M₂(ℂ) = Cl(3,0)`; "i" is the pseudoscalar `e₁e₂e₃` | **NATIVE** | A1 |
| K2 | `Z³` spatial substrate with local interactions | **NATIVE** | A2 |
| K3 | The pseudoscalar `i` satisfies `i² = -1`, generates a genuine U(1) phase `e^{iθ}` | **NATIVE** | standard Cl(3) algebra from A1 |
| K4 | Three-generation cyclic symmetry C₃ on the framework's generation sector | **RETAINED** | retained from generation-counting work (cited in `KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18.md` etc.) |
| K5 | Circulant kernel `K = a·I + b·(J - I)` on the C₃ triplet | **RETAINED** | same source |
| K6 | C₃ character decomposition: trivial character `a₀ = (l₁+l₂+l₃)/√3`, nontrivial `z = (l₁ + ω̄·l₂ + ω·l₃)/√3` with `ω = e^{2πi/3}` | **RETAINED + NATIVE** | character algebra is standard math; the assignment to the C₃ triplet is retained |
| K7 | Clock action `C: z → ω·z` (the C₃ generator) | **RETAINED + NATIVE** | group action on the irrep |
| K8 | CP-evenness gives real coupling structure (`D` real, `θ = 0`); cosines only | **RETAINED** | retained CP-evenness |
| K9 | Koide cone `\|z\|/a₀ = 1/√2 ⟺ Q = 2/3` (lepton) | **RETAINED** | `KOIDE_*` retained chain |
| K10 | Brannen circulant eigenvalue formula: `m_k ∝ 1 + √2·cos(2πk/3 + δ)` | **RETAINED** | `KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18.md`, `KOIDE_CIRCULANT_CHARACTER_BRIDGE_NARROW_THEOREM_NOTE_2026-05-09.md` |
| K11 | The mass observable `m_k²` is the modulus-squared of the eigenvalue triplet, normalized | **RETAINED** | standard from the circulant diagonalization |

**Chain 1 verdict:** **fully native + retained**. The lepton mass formula's
KINEMATIC SHAPE `cos(δ + 2πk/3)` requires no admitted imports. The δ parameter
appears in the formula as a **free parameter**; the formula does not specify
its value.

## Chain 2 — The Bernoulli family identities (the retained value source)

| # | Step | Tag | Source / required import |
|---|---|---|---|
| B1 | Discrete uniform distribution on `N` points has mean `M(N) = (N-1)/N` and variance `V(N) = (N-1)/N²` | **NATIVE** | elementary combinatorics |
| B2 | `V(N) = M(N)/N` (Bernoulli identity) | **NATIVE** | algebra on (B1) |
| B3 | `V(3) = 2/9`, `V(6) = 5/36` as instances of the family at `N = 3, 6` | **NATIVE** | direct substitution |
| B4 | `2/9` is multiply-determined in CKM: `K1: A²(1-A²) = 2/9`, `K2: 2·ρ·A² = 2/9`, `K5: A²/N_color = 2/9`, `K6: (1/N_color)(1 - 1/N_color) = 2/9` | **RETAINED** | `CKM_BERNOULLI_TWO_NINTHS_KOIDE_BRIDGE_SUPPORT_NOTE_2026-04-25.md` (`bounded_theorem`, claim_scope narrowed to conditional algebra on upstream `unaudited`/`proposed_retained` CKM rows) |
| B5 | `5/36 = V(6) = retained CKM η²` identification | **RETAINED (bounded)** | same source's quark-sector reading |
| B6 | `(N-1)/N²` is the canonical color-projected Bernoulli structure for `N_color = 3` and the quark-population structure for `N_quark = 6 = N_pair × N_color` | **RETAINED** | same source |

**Chain 2 verdict:** **native + retained-bounded** at the algebraic-identity
level. The identities `V(3) = 2/9` and `V(6) = 5/36` are bare algebraic facts.
Their identification with framework-physical quantities (Koide-cone offsets,
CKM η²) is the bounded-theorem layer.

## Chain 3 — The empirical anchor (PDG comparator only)

| # | Step | Tag | Source / required import |
|---|---|---|---|
| E1 | PDG charged-lepton masses `m_e, m_μ, m_τ`; sqrt-mass vector | **PDG (COMPARATOR)** | not a derivation input |
| E2 | Brannen formula at `δ = 2/9 rad` (offset from C₃-symmetric point `4π/3`) reproduces the sqrt-mass triplet to ~7×10⁻⁶ | **EMPIRICAL TEST** | uses (K10) + PDG; comparator-class numerical observation, not a derivation |
| E3 | PDG Wolfenstein `η ≈ 0.354 ± 0.012`, `η² ≈ 0.125` (vs framework `5/36 ≈ 0.139`, ~11% discrepancy) | **PDG (COMPARATOR)** | not a derivation input; recorded falsifier signal |

**Chain 3 verdict:** **PDG used as comparator only.** Neither E2 nor E3 is a
derivation input. E2's striking ~7×10⁻⁶ fit is the empirical motivation for
asking whether `δ = 2/9` has a structural source, but the question is not the
answer.

## Chain 4 — The `δ = 2/9` value question (the open frontier)

The Brannen formula (K10) gives the shape with **free δ**. The empirical anchor
(E2) says `δ = 2/9` reproduces PDG to ~7e-6. The question: **is there a
structural source for `δ = 2/9` natively?**

### 4a — The retained algebraic identity `V(3) = 2/9`

| Step | Tag | Source |
|---|---|---|
| The number `2/9` equals the retained Bernoulli variance `V(3) = (3-1)/3²` | **NATIVE** | (B3) |
| In radian, `2/9 rad ≈ 0.222 rad` | **NATIVE** | unit-substitution; observation |
| The Brannen formula at `δ = 2/9 rad` reproduces PDG to ~7e-6 | **NATIVE OBSERVATION** (E2) | (K10) + PDG comparator |

**Status:** `V(3) = 2/9` is a retained algebraic identity. Its appearance as
`δ` in the Brannen formula is an empirical fit, not a derived identification.
**No native derivation yet exists that forces `δ = V(3)` rather than any other
small radian value.**

### 4b — The bridge claim `3δ = Q` (closed PR #1940 inheritance)

| Step | Tag | Source |
|---|---|---|
| Posit identification `3δ = Q = 2/3`, giving `δ = Q/N_gen = 2/9` | **IMPORT (BRIDGE HYPOTHESIS)** | `DYNAMICS_LANE_SEED_NOTE` from closed PR #1940; not on `origin/main`; user-rejected as unapproved import |

**Status:** **DEMOTED.** Cannot be cited as authoritative in this lane.

### 4c — The π-bridge primitive `P` (open)

| Step | Tag | Source |
|---|---|---|
| The literal `2/9 rad` (a transcendental radian) is the identification needed to make `δ = V(3)` exact | **RETAINED ADMISSION** (open primitive `P`) | six prior no-go routes; admission unchanged |
| By Lindemann-Weierstrass, no Q-rational combination of retained rationals produces `2π`; hence no Q-rational combination can derive `2/9 rad` as a literal radian | **NATIVE** (standard math) | L-W theorem; retained inventory enumeration through `RADIAN_BRIDGE_EXPANDED_INVENTORY_BOUNDED_NOTE_2026-05-10_radianexp.md` |
| Six prior no-go routes (Z₃-qubit Pancharatnam-Berry, selected-line Berry, irreducibility audit, native-angle exhaustion, dimensional-inventory exhaustion, expanded-dimensionless-inventory exhaustion) | **RETAINED** | `KOIDE_*_RADIAN_BRIDGE_NO_GO_NOTE_*` chain |

**Status:** **OPEN PRIMITIVE.** Native machinery rules out Q-rational
derivation of `2π`; closing requires either a structural mechanism not in the
retained inventory, OR a re-expression that bypasses the radian unit.

### 4d — The FRG / asymptotic-safety attempt (rejected by user, M-work)

| Step | Tag | Source |
|---|---|---|
| D1 (dynamical flavon), D2 (IR fixed point), D3 (phase-locking) | **IMPORT (REJECTED)** | M3 work; not approved |
| Eichhorn-Held precedent / Wetterich machinery / mode-locking | **IMPORT (REJECTED)** | M3 work; not approved |
| Result: D3 fails (no algebraic fixed-point dynamics produces `δ=2/9`) | **DEMOTED** | depended on D1+D2 background |

**Status:** **DEMOTED.** Cannot proceed via this route in this lane.

## Chain 5 — The framework's retained native dynamics (alternative attack surface)

The framework has retained dynamics OTHER than the M-work's FRG attempt:

| Step | Tag | Source |
|---|---|---|
| Lattice-growth dynamics with decoherence on Z₂ DAGs | **RETAINED** | per-memory: mirror_symmetry_breakthrough, axiom_chain_closure |
| Corrected propagator: `1/L^p` attenuation; gravity as pure phase effect | **RETAINED** | per-memory: corrected_propagator |
| Brannen CH three-gap closure (Berry=CH, Ω=1 derived, operator map) | **RETAINED** | per-memory: brannen_ch_three_gap_closure |
| Wilson plaquette action | **IMPORT (admitted, per `bridge_gap_resolution_c_locked` memory)** | Wilson is admitted import, not derived from Cl(3)/Z³ |
| Per-site Cl(3) unitary evolution operators | **NATIVE** | A1 + standard QM |
| Emergent time from anomaly cancellation | **RETAINED** | per the dynamics-lane seed note's "framework forces gravity + emergent time" reference; need to verify this is `origin/main` retained, not just M-work assertion |

**Chain 5 verdict:** The framework has SOME retained native dynamics (lattice +
decoherence + Brannen CH closure + corrected propagator gravity). These are
candidates for attacking the `δ` question NATIVELY without invoking FRG /
asymptotic safety.

**Open verification task:** confirm which of (lattice + decoherence), (Brannen
CH), (corrected propagator), (emergent time) are actually `origin/main`
retained vs branch-local. Some of the memory entries point to recently retained
work; some may not be on main yet. This research lane should not assume — it
should cite each piece's `origin/main` source.

## What is salvageable from the M-work chain

After tagging:

- **Chain 1 (kinematic shape)**: fully retained. Brannen circulant formula is
  the framework-native lepton mass shape. **Available for native use.**
- **Chain 2 (Bernoulli identities)**: native + retained-bounded. **Available
  for native use.**
- **Chain 3 (PDG anchor)**: comparator only. **Available as falsifier signal.**
- **Chain 4a (V(3) = 2/9 algebraic)**: native. **Available.**
- **Chain 4b (3δ=Q bridge)**: demoted. **NOT available.**
- **Chain 4c (π-bridge primitive)**: retained admission. **Available as named
  obstruction.**
- **Chain 4d (FRG attempt)**: demoted. **NOT available.**
- **Chain 5 (native retained dynamics)**: partially retained (needs
  origin/main verification per piece). **Conditionally available pending
  verification.**

## What the lane can attack natively

Three candidate attack directions, all using only Chains 1-3 + Chain 4a + 4c +
verified pieces of Chain 5:

### Direction α — Native dynamics test of `δ = V(3)`

**Question:** does the framework's retained native dynamics (Chain 5, verified
pieces) determine `δ` to be `V(3) = 2/9`, or any other specific value?

**Method:** start from A1+A2 + retained native dynamics. Compute the C₃-axis
phase `δ` as a function of the native dynamical machinery (decoherence rates,
plaquette eigenphase, corrected-propagator parameters). Check if it lands at
2/9 rad.

**Falsifier:** if native dynamics gives `δ = 0` (no phase) or any other
specific value ≠ 2/9 rad, the value-question is closed negatively in this
direction (need different mechanism).

**No imports required** if Chain 5 pieces are verified retained.

### Direction β — Native kinematic reformulation

**Question:** in the retained Brannen formula `cos(δ + 2πk/3)`, can `δ` be
re-expressed as a function of `Q` (or other retained dimensionless) without
passing through a literal radian?

**Method:** explore re-expressions of the formula that use `Q = 2/3` as an
explicit input rather than `δ = Q/3` as a radian. Test the four K1-K4
substrates (Cl(3) projector triple product, cumulant expansion, determinantal,
Plancherel-Frobenius) without invoking the `KH` hypothesis as a framing —
just attempting the re-expressions directly.

**Falsifier:** L-W applies. If every native re-expression hits the
transcendental-π wall, the π-bridge is structurally irreducible without new
content.

**No imports required.** (`KH` was a hypothesis-framing; the actual K1-K4
substrates are retained.)

### Direction γ — Native isolation of the π-bridge gap

**Question:** assuming Directions α and β both hit walls, can we PRECISELY
state what new content would close the gap?

**Method:** characterize the exact structural input needed to close `P`. The
input must be such that (a) it does not require A1+A2 extension, (b) it
licenses the literal-rational-radian identification.

**Output:** a sharpened residual statement (not a closure, not a new axiom
proposal, just a precise statement of what's missing).

**No imports required** to perform the characterization.

## Process commitment

Each direction's deliverables follow the charter:
- Native derivations explicitly cite retained sources.
- Imports: NONE required for any direction (pending Chain 5 verification).
- Clean import-free pieces become small-PR candidates.
- Negative results (walls hit) go through N1-N8 discipline before claiming any
  no-go.

## Verification needed (priority for next cycle)

Before launching Direction α, verify on `origin/main`:

1. Is the lattice-growth-with-decoherence dynamics retained on main? (Find the
   actual retained source-note in `docs/` on origin/main.)
2. Is the Brannen CH three-gap closure retained on main? (memory says yes
    2026-04-22, runner 16/16, but main may have audited it since.)
3. Is the corrected propagator with `1/L^p` retained on main?
4. Is the emergent-time-from-anomaly-cancellation retained on main?

For each unverified piece, demote to "memory-claimed-but-unverified" until
checked against `origin/main`.
