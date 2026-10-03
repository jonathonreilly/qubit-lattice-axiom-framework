The contest gives **failure** by A45's criterion; both failure conditions hold at 6³ and 8³.
- **The λ′ optimum sits at zero within error.** The best gain over λ′ = 0 is at most 2.0σ (6³) and 1.4σ (8³). It does not grow with size, and the energy is flat in λ′ up to 0.2, then rises at 0.3.
- **Ordered states win or tie at every j.** At j = 0.30 the λ′ state's margin goes from +0.00096 (2.0σ) at 6³ to −0.00036 (−0.8σ) at 8³, so it shrinks and changes sign.

This message is the full report. I did not write `SP/c8/A47/REPORT.md`, because my harness forbids subagent report files.

**Housekeeping**
- No git writes, no repo edits, no PRs.
- Scripts are in `SP/c8/A47/` and import `SP/c8/A46/a46lib.py` and the A43 spin-wave library.
- Every run went through `run.sh` with the same gates as A44/A46:
  - load gate below 6 (actual 1.8–2.7) and free memory at least 25% (actual 30–39%);
  - the shared `NUMLOCK`, released after each run and now free;
  - `nice -n 10`, the four BLAS caps at 1, and a Python alarm of 290 s or less.
- The longest run took 233 s; peak memory was 464 MB. No ring terms were used.

**Grades.** EXACT (proof or exact arithmetic), CHECKED (finite computation with stated tolerance or error bars), ARGUED (reasoning without proof), COMPARATOR (literature from memory, not adopted). Every rule here is supplied, not adopted.

## 1. Question

A45 §6 asked for one energy contest.

- **Trial state.** The projected U(1) parton state. It has the soldered nearest-neighbour hop iλσ^a (λ = 1) plus the face-diagonal hop iλ′σ·d̂, with λ′ ∈ [0, 0.3] (below 1/(2√2)).
- **Rule.** The soldered-covariant rule (J₁, K₁) = (−1, 2) plus j Σ_fd (2σᶜσᶜ − σ·σ), for j = 0.20–0.40 in steps of 0.05. In the Klein-dual frame this is the J₁–J₂ Heisenberg rule H′ = Σ σ·σ + j Σ_fd σ·σ.
- **Sizes.** 6³ and 8³.
- **Competitors:**
  - the λ′ = 0 (SU(2)) state;
  - spin-wave-corrected Néel and collinear (π,π,0) states;
  - weakly ordered projected states (π-flux plus a small Néel or collinear field m).
- **Success** needs all three: the optimum λ′ ≠ 0; it beats every corrected ordered state by more than three combined error bars at both sizes; the margin does not shrink from 6³ to 8³.

## 2. Answer, graded

Energy per nearest-neighbour bond is E(j) = e_J′ + 2j·c₂, in dual-frame units with J₁′ = 1. The errors come from binning the combined series per sweep. The neighbour and face-diagonal estimates are anti-correlated, which makes the errors small: ±0.0003 at j = 0.3, against ±0.0013 and ±0.002 separately.

**Trial versus the lowest competitor (CHECKED).**

| j | Size | Best λ′: E | λ′ = 0: E | Gain over λ′ = 0 | Lowest competitor: E | Margin |
|---|---|---|---|---|---|---|
| 0.20 | 6³ | 0.10: −0.8504(5) | −0.8492(5) | +0.0012 (1.6σ) | Néel spin waves −0.9072 | −0.057 |
| 0.20 | 8³ | 0.20: −0.8465(7) | −0.8462(5) | +0.0002 (0.3σ) | Néel spin waves −0.9072 | −0.061 |
| 0.25 | 6³ | 0.10: −0.8103(3) | −0.8093(3) | +0.0010 (2.0σ) | Néel spin waves −0.8912 | −0.081 |
| 0.25 | 8³ | 0.20: −0.8066(5) | −0.8065(3) | +0.0001 (0.2σ) | Néel spin waves −0.8912 | −0.085 |
| **0.30** | **6³** | 0.10: −0.77016(28) | −0.76947(26) | +0.0007 (1.8σ) | collinear m = 0.1 (projected) −0.76920(40) | **+0.00096 (2.0σ)** |
| **0.30** | **8³** | 0.10: −0.76690(29) | −0.76673(26) | +0.0002 (0.5σ) | Néel m = 0.05 (projected) −0.76726(36) | **−0.00036 (−0.8σ)** |
| 0.35 | 6³ | 0.10: −0.7300(4) | −0.7296(3) | +0.0004 (0.8σ) | collinear spin waves −0.7752 | −0.045 |
| 0.35 | 8³ | 0.10: −0.7277(4) | −0.7270(4) | +0.0007 (1.2σ) | collinear spin waves −0.7752 | −0.048 |
| 0.40 | 6³ | 0.10: −0.6899(6) | −0.6898(5) | +0.0002 (0.2σ) | collinear spin waves −0.8018 | −0.112 |
| 0.40 | 8³ | 0.10: −0.6884(6) | −0.6872(5) | +0.0012 (1.4σ) | collinear spin waves −0.8018 | −0.113 |

- **λ′ profile at j = 0.30.**
  - 6³: E is −0.7695, −0.7691, −0.7702, −0.7696, −0.7693, −0.7693, −0.7668 for λ′ = 0 … 0.30.
  - 8³: E is −0.7667, −0.7669, −0.7667, −0.7636 for λ′ = 0, 0.1, 0.2, 0.3.
  - So the energy is flat within noise up to λ′ = 0.2 and costs about +0.003 at 0.3.
  - E(λ′) = E(−λ′) exactly, because the η-rotation flips λ′ and leaves the projected state unchanged (EXACT; A46).
- **Variational ordered states win too, not only spin waves.**
  - Néel m = 0.2 gives −0.8756 (6³) and −0.8779 (8³) at j = 0.20.
  - Collinear m = 0.8 gives −0.7397 (6³) and −0.7338 (8³) at j = 0.35.
- **Spin-wave competitors alone.** At j = 0.30 Néel spin waves are unstable. The trial beats collinear spin waves (−0.7565) by 0.0137 at 6³ and 0.0102 at 8³. That margin shrinks with size, and the weakly ordered projected Néel state ties at 8³. So even this slice fails the test.
- **Spin-wave numbers (CHECKED; k-grid 6³ against 8³ agree within 5e-4).** Spin waves give an estimate (COMPARATOR as physics), not a variational bound.

| j | Néel | Collinear |
|---|---|---|
| 0.20 | −0.9072 | unstable |
| 0.25 | −0.8912 | −0.7632 |
| 0.30 | unstable | −0.7565 |
| 0.35 | unstable | −0.7752 |
| 0.40 | unstable | −0.8018 |

**16-site cluster at j = 0.3 (CHECKED, exact).**
- The exact ground state is −0.84518 per bond (non-degenerate; the next level is −0.82939).
- The best λ′ state is λ′ = 0.2, at −0.72798 with overlap 0.4403. For λ′ = 0 the numbers are −0.72698 and 0.4380.
- The weakly ordered states are close: Néel m = 0.05 gives −0.72665 (overlap 0.434); collinear m = 0.1 gives −0.72647 (overlap 0.436).
- So every simple state is about 0.12 per bond above the exact ground state, with overlap 0.44 or less.

**Verdict.**
- The U(1) deformation λ′ gains nothing significant (EXACT symmetry; CHECKED flatness).
- The parton background never beats the corrected or weakly ordered states.
- Under A45's failure branch (ARGUED): the parton route would need multi-spin star terms or more room. A46's ring-plus-J₂ window was also at the noise level.
- COMPARATOR: an SU(2) or U(1) parton mean field in 3D giving way to order matches the general expectation for cubic J₁–J₂.

## 3. Methods

- **States.** The A46 `mf_dual` hop matrix (soldered frame, rotated by V = ⊕V_x), at half filling with antiperiodic boundaries. All λ′ ≤ 0.3 are closed shells; the gap at λ′ = 0.3 is 0.92 (6³) and 0.57 (8³).
- **VMC.** Pair flips plus single flips. The per-sweep estimators of the neighbour and face-diagonal σ·σ come from O(N²) determinant ratios.
- **Machinery checks.** The λ′ machinery was validated in A46 against exact enumeration on 16 sites, and the Klein map passes the coordinator's check.
- **Spin waves.** A43's library with face-diagonal bonds appended (as in A44 `star_j2`). Stability is the minimum BdG eigenvalue over the k-grid.
- **Reused data.** Weakly ordered states from A46's L = 6 and L = 8 runs with face-diagonal measurement (same machinery), plus new runs (`neel:0.05` at 6³; `col:0.2/0.4/0.8` at 8³).

## 4. Checks (all in `SP/c8/A47/`; full outputs in `log_A`–`log_E.txt`)

| Run | Runtime, peak memory |
|---|---|
| `gaps47.py` | 11 s |
| 6³ batches A and B | 101 s and 104 s, 65 MB |
| 8³ batches C, D and E | 194 s, 185 s and 233 s, ≤ 217 MB |
| `lswt47.py` | 25 s |
| `ed16_47.py` | 3 s, 464 MB |
| `contest.py` | 0.1 s |

- First and second halves agree in every state (for example −0.7697/−0.7692 and −0.7666/−0.7668).
- The inverse drift was at most 4e-12.
- Batches A/B and C/D share an output tag, so `out_*` holds only the later batch; the logs keep the full outputs.

## 5. Open edges

1. A combined trial (λ′ plus a weak order field) and Lanczos-step or backflow improvement, to close the 0.12-per-bond gap to the exact 16-site ground state.
2. A finer j scan over 0.27–0.33 at 8³ and 10³ with twist averaging. The tie at j = 0.3 is the only place left to look.
3. Z₂ or pairing trials (Pfaffians).
4. Multi-spin star terms beyond J₂, which A45's failure branch points to.

## 6. Plain-language summary

The test asked whether adding a gentle diagonal hop to the two-part entangled background, the change that could let its hidden field behave like light, gives a rule under which that background is the calmest state. It does not. The diagonal hop barely changes the energy, and the best setting is indistinguishable from not adding it at all. At every rule strength we tried, a magnet-like ordered state is lower in energy or ties within the measurement noise, and the near-tie shrinks into a loss on the larger grid. On a small 16-place grid the true calmest state is well below every simple candidate, so none of them captures it.