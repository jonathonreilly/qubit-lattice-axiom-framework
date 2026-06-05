# Record axiom pressure-test C — the chirality shot via record-flow linearization at `r=1/2`

**Date:** 2026-06-04
**Claim type:** meta
**Claim boundary:** This is a **pressure-test / design-exploration** note for a *candidate* (non-adopted)
Record axiom. It does **not** introduce, adopt, or rely on any new axiom or import. It tests, with purely
algebraic checks (no PDG / measured masses), whether the **linearization of the stipulated records/Lüders
sharpening flow** at its `r=1/2` stationary point supplies the **Hermitian, C₃-orbit-splitting chirality
grading** `Γ_χ` that the charged-lepton Koide `Q=2/3` needs. The stipulated map `r→2r²` and the
existence/stability of `r=1/2` are taken from the bounded source
`docs/FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02.md`; the chirality target and the
anticommutation obstruction are the retained
`docs/KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md` and
`docs/KOIDE_ANTICOMMUTING_OPERATOR_DERIVATION_THEOREM_NOTE_2026-05-10.md`.
**Runner:** `scripts/record_axiom_ptC_chirality_linearization_2026_06_04.py` (SUMMARY 34/34 PASS, 0 FAIL).
**Cache:** `logs/runner-cache/record_axiom_ptC_chirality_linearization_2026_06_04.log`.

## The question (the one new angle the stability frame opens)
The charged-lepton Koide `Q=2/3` needs a **Hermitian involution** `Γ_χ` (`Γ²=I`, spectrum `±1`) that
**anticommutes** with a mass operator **and splits the C₃ orbit** (singlet vs doublet). Prior chirality
attempts failed on a **static** structure: the doublet's complex structure `J` is **anti-Hermitian**
(spectrum `{0,±i}`) and `⟨v|J|v⟩=0` (vacuous); site-diagonal gradings gave `Q=1/2`, not `2/3`. The deciding
distinction was **Hermitian vs anti-Hermitian**.

The new angle: the candidate Record axiom induces a record-**flow** on the sector-weight dial (Lüders-type
sharpening `p→p²/Z`, reducing to `r→2r²`), whose `r=1/2` stationary point gives `Q=2/3`. **Linearize** the
flow at `r=1/2`. The Jacobian/Hessian of a **real** functional is **symmetric = Hermitian** — naturally on
the comparator-compatible side, unlike the anti-Hermitian `J`. *Does its stable/unstable (Z₂) eigensplit
supply the `Γ_χ` the static `J` could not?* If the **same** axiom whose stationary point is `r=1/2` also
supplied chirality via its linearization, that would be a deep double-unlock.

## Verdict: NOT-UNLOCKS-CHIRALITY (the double-unlock does not close)
The prompt's key structural insight is **correct** — the linearization *is* Hermitian — but Hermiticity was
never the obstruction. The linearization lands in the **commutant** of `Γ_χ`, not its anticommutant. The
shot fails on four independent axes, any one of which is fatal.

### (1) The flow operators are block-diagonal in `singlet | doublet` ⇒ they commute (the decisive obstruction)
The record flow lives on the **2-sector dial**, whose state space is `singlet ⊕ doublet`. That partition **is
the eigenbasis of** `Γ_χ` (`Γ_χ` has `+1` on the singlet, `−1` on the doublet). Hence **every** operator the
flow generates — Jacobian, Hessian, the arrow contrast — is **block-diagonal** in `singlet | doublet`, and
block-diagonal operators **commute** with `Γ_χ` (verified symbolically for an arbitrary block-diagonal
operator). Conversely, `{H,Γ_χ}=0` **forces** `H` to be purely **off-block** (zero singlet and doublet
diagonal blocks) — i.e. it *requires* singlet↔doublet coupling, which the dial cannot produce. This is the
retained circulant no-go (`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO`) reached from the **dynamical** side:
"circulants commute" ↔ "2-sector-flow operators are block-diagonal, hence commute."

### (2) The genuine 3-gen flow has no `r=1/2` fixed point — only the reduced 1-D dial does
The point `(P_singlet,P_doublet)=(1/2,1/2)`, i.e. pointer probabilities `p=(1/2,1/4,1/4)`, is **not** a fixed
point of the genuine 3-generation Lüders map `T(p)=p²/Z`: it maps to `(2/3,1/6,1/6)` (it keeps sharpening
toward the singlet vertex). The genuine fixed points are the **vertices** and the **democratic center**
`(1/3,1/3,1/3)`. The `r=1/2` fixed point exists **only after** the doublet has been grouped, i.e. in the
**reduced 1-D dial** `r→2r²`. "Linearize at `r=1/2`" therefore yields the **scalar** `f'(1/2)=2` — a `1×1`
object — not a grading on the 3-gen space.

### (3) The natural Hermitian liftings are either degenerate or isotropic — not a Z₂ involution
- **Lift A — Hessian of the 2-sector entropy** on the full 3-gen weight space at `r=1/2`: it **is** real
  symmetric (Hermitian ✓), but it is **rank 1**, spectrum `{−3/4, 0, 0}` — **not** a Z₂ grading (which needs
  spectrum `±1`). Its only non-trivial eigenvector is the singlet-vs-doublet **contrast** `(−1,1,1)`; the
  doublet-internal directions are flat. It neither commutes nor anticommutes with `Γ_χ` (it is off the
  algebra because the 2-sector grouping is blind to the doublet's internal structure).
- **Lift B′ — Jacobian of the genuine flow** at the democratic center: C₃-symmetric circulant, spectrum
  `{0 (singlet), 2, 2 (doublet)} = 2·(doublet projector)`; **commutes** with `Γ_χ`. The unstable manifold is
  the **whole** doublet (C₃-symmetric) — a singlet/doublet contrast, not a sign *within* the doublet.
- **Lift C — operator flow** `ρ→ρ²/Trρ²` on the doublet, linearized at the balanced state `ρ=I/2`: the
  Jacobian is `2·Identity` on the tangent (**isotropic**). No preferred Z₂ direction; no `Γ_χ`.

### (4) The arrow orients the singlet/doublet *axis*, not a sign *within* the doublet
The flow's irreversible/unstable direction is the contrast `diag(2,−1,−1)` (traceless), a **function of the
2-sector partition**, hence block-diagonal ⇒ **commutes** with `Γ_χ`. The arrow can pick the singlet/doublet
**axis** but cannot put a sign **inside** the doublet, which is what a chiral `Γ_χ` (anticommuting,
orbit-splitting *off-block*) requires.

## The Koide `Q` the linearization-grading gives
The only non-trivial grading the flow supplies is the singlet-vs-doublet contrast. Its eigenvector readout
gives `Q ∈ {1/3 (singlet (1,1,1)), ∞ (doublet collapse)}` — and the rank-1 Lift-A Hessian eigenvector
`(−1,1,1)` gives `Q=3` and fails the lightcone `⟨v|Γ_χ|v⟩=0`. **In no case does it give `Q=2/3`.**

**Control (the target is real).** A hand-built **off-block** Hermitian `H=|s⟩⟨w|+|w⟩⟨s|` (`s` the singlet,
`w⊥s`) — exactly the form the dial flow **cannot** produce — **does** anticommute with `Γ_χ`, has spectrum
`{−λ,0,+λ}`, and its non-zero-eigenvalue eigenvectors satisfy `⟨v|Γ_χ|v⟩=0` and give `Q=2/3`. So the failure
is **specifically** the missing singlet↔doublet off-block coupling, not Hermiticity.

## Summary table
| Lifting of the flow at the fixed point | Hermitian? | Z₂ involution (`±1`)? | vs `Γ_χ` | Koide `Q` |
|---|---|---|---|---|
| A: Hessian of 2-sector entropy (3-gen) | yes | no (rank 1, `{−3/4,0,0}`) | neither | `3` (off-cone) |
| B: genuine 3-gen map at `r=1/2` | — | — (no fixed point there) | — | — |
| B′: genuine map Jacobian at center | yes | no (`{0,2,2}`) | commutes | — |
| C: doublet operator flow at `ρ=I/2` | yes | no (isotropic `2·I`) | commutes | — |
| arrow contrast `diag(2,−1,−1)` | yes | no (`{2,−1,−1}`) | commutes | `{1/3, ∞}` |
| **control off-block `H` (NOT from flow)** | yes | spectrum `{−λ,0,λ}` | **anticommutes** | **`2/3`** |

## What this opens (next paths, not a closure)
This is a genuinely informative negative: it isolates the obstruction to a single crisp, basis-independent
statement — **the chirality grading must be off-block (singlet↔doublet), and no operator generated by the
2-sector record dial is off-block.** The record-flow stationary point delivers the *value* `r=1/2`/`Q=2/3`
but is structurally **block-diagonal**, so it cannot also deliver the chirality. Forward paths the framing
suggests: (a) a flow that is **not** dial-reducible — one acting on the *full* 3-gen density operator with a
C₃-**breaking** generator that mixes the singlet and doublet sectors (the only way to populate the off-block);
(b) couple the chirality to the independently-flagged off-block import shared with the generation-ID gate
rather than seeking it inside the sector-weight dynamics. The static `J` was anti-Hermitian; the dynamical
Hessian is Hermitian but block-diagonal — the live question becomes which structure supplies an
**off-block** Hermitian generator.

## Reproduction
```
python3 scripts/record_axiom_ptC_chirality_linearization_2026_06_04.py
# SUMMARY: 34 PASS / 0 FAIL ; VERDICT: NOT-UNLOCKS-CHIRALITY
```
