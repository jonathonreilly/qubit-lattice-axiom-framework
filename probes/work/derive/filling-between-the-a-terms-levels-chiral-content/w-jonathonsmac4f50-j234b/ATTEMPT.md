# Filling between the a-term's levels: is the content at the Fermi level chiral? — attempt 1

Worker `w-jonathonsmac4f50-j234b`, model `claude-opus-5-5`. Task `J:derive:filling-between-the-a-terms-levels-chiral-content:a1`.

**Provenance.** Blocks 76 to 78 (#8611, #8612, #8613) and the fork probe on the branch of #8572 (`FORK_PROBE_source_link_20260922.md`) were written by the same model family (Claude Opus). They are open and unrefereed; I restate what I use. There were no prior attempts at claim time, and the plan is my own.

**Scope.** This works within the supplied clauses: block 54's family on the qubit coin, and block 77's staggered term as a supplied background. Nothing is adopted. The parked decisions (the statistical postulate; a larger site algebra) are not touched. The free many-record state is the **comparator**, not the framework's state: block 78 shows that one record per site is an interaction. No gravitational claim is made. Classical results (Weyl semimetals, Nielsen–Ninomiya, Haldane's Fermi-surface Berry phases, Kogut–Susskind) are comparators only.

## 1. The exact statement attempted

Let `h(k) = a₀ + 2aΣ_j cos k_j + Σ_j σ_j sin k_j` (block 54 T1(a); block 77). The two bands are `E_±(k) = a₀ + 2aΣcos k ± |sin k|`. The free comparator fills every one-record state with energy below `μ`.

**(A) Levels and senses.**
- At the eight zeros `k = πn`: `h = a₀ + L_n`, with `L_n = 2a(3 − 2|n|)`.
- The sense of zero `n` is `χ_n = det(∂ sin k/∂k)|_{πn} = (−1)^{|n|}`. The multiplicities are 1:3:3:1, with one sense per level (block 77 T1).

**(B) Every filling, every `a₀, a` (`μ` not a level).** Give the Fermi sheets the orientation of the boundary of the occupied region. Then:
- the upper band's sheets carry the Berry charge `−Σ_{L_n<μ−a₀} χ_n`;
- the lower band's sheets carry `+Σ_{L_n<μ−a₀} χ_n`;
- the total is **zero**.

Per band, for `a > 0` and `a₀ = 0`:

| window | upper band | lower band |
|---|---|---|
| `(2a, 6a)` | `+1` | `−1` |
| `(−2a, 2a)` | `−2` | `+2` |
| `(−6a, −2a)` | `+1` | `−1` |
| outside all levels | 0 | 0 |

Every zero lies inside a pocket of one band: an electron pocket if its level is below `μ`, a hole pocket if above. A pocket holding a set of zeros carries `−Σχ` over them. So right minus left over all gapless content is `Σ_n χ_n = 0`. **No filling has gapless content of a single sense.**

**(C) Staggered term `mε`, every `a₀, a, m`.**
- The spectrum is exactly `a₀ ± √((E_±(k) − a₀)² + m²)`.
- The only gap is `|μ − a₀| < |m|`. Outside it the Fermi sheets are the massless ones at `a₀ ± √((μ − a₀)² − m²)`, so no pocket is gapped.
- For `a ≠ 0` the zeros are **not** gapped. Each pair `(n, n + (111))` stays two-fold degenerate at `a₀ ± √(L_n² + m²)` and splits linearly: a Weyl point of speed `|L_n|/√(L_n² + m²)` and sense `sign(L_n) χ_n`. This corrects the "massive pairs" reading of block 77 T4 (see Step 4.4).

**(D)** What the hard-core case would need: stated, not proved.

**The task's HIT condition is not met:** no filling has single-sense gapless content, already in the free comparator.

## 2. Steps

### Step 1 — levels and senses (PROVED; CHECKED 1.1, 1.2)
- At `k = πn`: `sin(πn_j) = 0` and `Σcos(πn_j) = 3 − 2|n|`. So `h(πn) = a₀ + 2a(3 − 2|n|)` times the identity.
- The coin vector is `d(k) = sin k`. Its Jacobian at `πn` is `J_n = diag((−1)^{n_j})`, so `χ_n = det J_n = (−1)^{|n|}`.
- The counts are `C(3, |n|)` = 1:3:3:1, and each level holds zeros of one sense.
- `Σ_n χ_n = 1 − 3 + 3 − 1 = 0`.

### Step 2 — the Berry charge of each band at each zero (PROVED; CHECKED 2.1, 2.2; executed E2)
- **Band curvature.** Off the zeros, `|d(k)| > 0`. The scalar part does not change eigenvectors, so the two bands are those of `d̂·σ` with projectors `P_± = (1 ± d̂·σ)/2`.
- **Convention.** The curvature is `F = i tr(P[∂₁P, ∂₂P])`, which is `dA` with `A = i⟨u|du⟩`.
  - For `d̂ = n̂(θ, φ)` it equals `∓(1/2) sin θ` for `P_±` (2.1).
  - So on a sphere the upper band's Chern number is `−deg(d̂)` and the lower band's is `+deg(d̂)`.
- **Degree near a zero.** Near `πn`, `d = J_n q + O(|q|³)`, so on a small sphere `deg(d̂) = sign det J_n = χ_n` (2.2).
- **Charges.** Hence `q⁺_n = −χ_n` and `q⁻_n = +χ_n` (outward normal).
- **Numerical check.** A link-variable flux through a small sphere reproduces this at all eight zeros (E2). Its orientation was calibrated on the identity map `d = q`, whose upper-band Chern number is `−1` by 2.1.

### Step 3 — the Fermi sheets carry no net charge (PROVED; CHECKED 3.1–3.3; executed E3)
- **Setup.** Let `R_± = {k ∈ T³ : E_±(k) < μ}`, with `μ` a regular value of `E_±` and not a level. The curvature `F_±` is a closed 2-form on `T³` minus the zeros.
- **Stokes.** Apply Stokes to `R_±` minus small balls around the zeros it contains. The torus has no other boundary. This gives `∮_{∂R_±} F_± = Σ_{n ∈ R_±} q^±_n`.
- **Which zeros each region contains.** `E_±(πn) = a₀ + L_n`. So both regions contain exactly the zeros with `L_n < μ − a₀`.
- **Totals.** Upper sheets carry `−Σ_{L_n<μ−a₀} χ_n`; lower sheets carry `+Σ_{L_n<μ−a₀} χ_n`, which equals `−Σ_{L_n>μ−a₀} χ_n` because `Σχ = 0`. The sum is 0 for every `μ`, `a₀` and `a`. The table in §1 is (3.1, 3.2).
- **Pocket by pocket.**
  - An electron pocket (upper band) around `n` carries `q⁺_n = −χ_n`, with the outward normal.
  - A hole pocket (lower band) around `n` carries `−q⁻_n = −χ_n`, because the occupied region's boundary faces into the pocket.
  - So every pocket carries its own zero's `−χ_n`, electron or hole alike. Merged pockets carry the sum over the zeros they hold (3.3).
- **Executed (E3).** On a `40³` grid with periodic components, at `a = 0.1`:
  - every zero sits in its own pocket;
  - in `(2a, 6a)` there are 7 electron pockets and 1 hole pocket around the top zero.

  At `a = 0.6` the pockets merge: in `(2a, 6a)`, one electron sheet holds seven zeros and a hole sheet holds the top zero. They carry `+1` and `−1`.
- **Answers to (a) and (b).**
  - Between `+2a` and `+6a`, all eight species are gapless at the Fermi level. The lone top species (sense `+`) is hole-like. The seven others (net sense `−1`) are electron-like. Right minus left = 0.
  - Between `−2a` and `2a`: electron pockets around the four lower zeros (net `+2`), hole pockets around the four upper zeros (net `−2`). Right minus left = 0.
  - Between `−6a` and `−2a`: the mirror image of the first case.
  - What the scalar hop does distinguish is an **electron–hole imbalance of sense**, ±1 or ±2 per band. The comparator is a Weyl semimetal's axial imbalance. It is not chiral content: the total vanishes.

### Step 4 — the staggered term, exactly (PROVED; CHECKED 4.1–4.9; executed E1)

**4.1 Block form (4.1, 4.2).**
- `ε` shifts the wave vector by `π(111)`, and `h(k + π(111)) − a₀ = −(h(k) − a₀)`.
- In the basis `(k, k + π(111))`: `H − a₀ = τ_z ⊗ (h(k) − a₀) + m τ_x`.
- The two terms anticommute, so `(H − a₀)² = (h − a₀)² + m²`. The spectrum is `a₀ ± √((E_±(k) − a₀)² + m²)`, which is block 77 T4's formula.

**4.2 The only gap (4.6, 4.7).**
- `√(λ² + m²) ≥ |m|`, with equality iff `λ = 0`.
- For `a ≠ 0`, `E_+ − a₀` takes the values `6a` at `k = 0` and `−6a` at `k = π(111)`. So the massless sheet at `a₀` exists, and the gap is exactly `2|m|`, around `a₀`.
- For `|μ − a₀| > |m|` the Fermi sheets are `{E_± = a₀ ± √((μ − a₀)² − m²)}`: massless sheets, not gapped. Their Berry charges add to zero by Step 3, applied at each of the two energies.

**4.3 The zeros stay gapless (4.3–4.5, 4.9; executed E1).**
- At a zero the block is `(L τ_z + m τ_x) ⊗ 1_σ`. Its eigenvalues are `±√(L² + m²)`, **each twice**.
- The first-order term `τ_z ⊗ σ·(J q)`, projected on the `+` eigenspace, is `(L/√(L² + m²)) σ·J q`.
- The exact eigenvalues along a line are `±√((L ± q)² + m²)`. Their splitting at small `q` is `2Lq/√(L² + m²)`.
- So for `L ≠ 0` each zero pair is a Weyl point at `a₀ ± √(L² + m²)`, with speed `|L|/√(L² + m²)`. The upper point's sense is `sign(L) χ_n`, the same from either member of the pair (4.9).
- The positive branch's lowest energy is `m`, not `√(L² + m²)`. It is reached on the massless sheet at `a₀`, which for small `a` is a sphere `|sin k| = |L|` around each zero.
- *Executed (E1)*, at `a = 0.2`, `m = 0.7`: the pair sits at `1.3892` and splits with speed `0.863779` against `L/√(L² + m²) = 0.863779`.

**4.4 On block 77 T4.**
- Its energies are exact. The reading "one pair of mass `√(m² + 36a²)` and three of mass `√(m² + 4a²)`" holds only at `a = 0`.
- For `a ≠ 0` the zeros are two-fold degenerate points with linear dispersion: offset Weyl points, not masses.
- The one gap `mε` opens is at `a₀`, on the Fermi sheets of the massless model: a nesting gap, because `E(k + π) − a₀ = −(E(k) − a₀)`.
- Block 77 T3's `(H + mε)² = H² + m²` holds with `H` replaced by `H − a₀`. But with the `a`-term, `(H − a₀)²` vanishes on whole sheets, not at the zeros. So "a rest energy the same for every species" describes the band minimum `m`, not the zeros.

**4.5 A nodal surface (4.8).** On `Σcos k = 0` the block is `τ_z ⊗ σ·s + m τ_x`, with eigenvalues `±√(|s|² + m²)`, each twice. With `mε`, the two positive (and the two negative) branches touch on this surface. The Berry bookkeeping in 4.2 uses the smooth block labels `i = ±` of Step 3, not sorted bands.

### Step 5 — the hard-core case (statement; ASSUMED where marked)
- **What (B) rests on.** It is topological: a two-component coin of finite reach on a closed Brillouin torus has Berry charges that add to zero, and each band's Fermi sheets enclose a set of zeros.
- **What exclusion is.** Block 78 shows it is an interaction that conserves record number and commutes with translations, so the free-sheet argument does not apply.
- **The expected statement (ASSUMED).** A lattice system with a conserved on-site charge and finite-range, translation-invariant dynamics cannot have low-energy content with a net anomaly of that charge. This is 't Hooft anomaly matching; its lattice form is the interacting extension of Nielsen–Ninomiya. It is not proved here.
- **What would be needed for single-sense low-energy content under exclusion.** One of:
  1. giving up conservation of record number in the dynamics. Formation adds records, and the walk's generator conserves them;
  2. a wall of a higher-dimensional bulk, where chiral content lives on the wall (the fork probe's "fourth direction with a wall");
  3. non-local reach;
  4. a larger coin (parked; not raised).
- **Why the task's second clause is moot.** Its condition, that exclusion does not destroy chirality, never arises: the free comparator has none to destroy.

## 3. Where the route stops

The route succeeds for (a) to (c) in the free comparator. The first place it cannot go is (d): the interacting statement rests on an ASSUMED anomaly theorem. Neither the free comparator nor Step 5 finds a filling with single-sense content.

## 4. What would finish it

1. A proof of the interacting no-go for the hard-core record gas. One route: flux insertion on a torus with spectral flow of the many-record ground state.
2. Alternatively, an exact small-torus count of many-record states under exclusion showing the same electron–hole sense imbalance and no net chirality.
3. An owner's decision on which of the four ingredients of Step 5, if any, the framework would state.
4. A corrected statement of block 77 T4 for `a ≠ 0` (Step 4.4). Reported here, not fixed.
