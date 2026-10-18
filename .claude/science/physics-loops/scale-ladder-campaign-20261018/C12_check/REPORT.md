# C12 check report

Provenance: a fresh-context checker of the same model family as the C12 worker, so not independent in family.
- **Model:** the separate C11_check build (`c11model.py`), with the opposite Bloch convention to C12's. The C12 runner and the wt-lanes model were not used.
- **New code:** the checker's own T1 frame (agrees with `tau_frames.npy` to 7e−16), D_b letter, batched central-difference W₃ and finite-range tests.
- **Reused:** only `c11lib.sphere_chern` (FHS) and `c11lib.rand_H`.
- **Resources:** about 4 minutes on ≤ 2 threads.

The checker's write was blocked; the supervisor saved this report from the hand-back.

**Verdict: no claim refuted. 19 checks pass, 0 fail. Four framing corrections.**

| Runner | Result | Covers |
|---|---|---|
| `chk_a.py` | 8/0 | the letter D_b |
| `chk_bc.py` | 11/0 | the single node; finite range ⇒ W₃ = 0 |

The first runs failed on three of the checker's own bugs, logged in `*_firstrun.log`:
- a phase taken as x instead of x̄;
- an m-scan grid too coarse at m = 1.2 and 2.8;
- a single-band FHS call that crashed the gap estimate.

## (a) The letter D_b: confirmed

- **q ↦ Rᵀq is the induced action.** Rᵀk* + πλ_R ≡ k* for all 24 lifts at both ±k*, and the extra 2πn is harmless because n̂ depends on q only through sin and cos. sin(Rᵀq) = Rᵀ sin q and Σcos q is invariant (4e−16).
- **Covariance.**
  - The T1 solution space is 1-dimensional on each D_b: Hermitian, +iε algebra, Pauli-equivalent.
  - Errors: unitarity 8e−16, periodicity 6e−16, covariance under all 24 lifts 1e−15.
  - Negative control: swapping τ_x and τ_y breaks covariance (0.33).
- **W₃.** 0.96571416 (N = 8), 0.99985871 (16), 0.99999945 (24) and 1 − 2e−9 (32), for D₊, D₋ and the SU(2) control alike.
  - W₃ is constant on m ∈ (1,3) (1.0000 at m = 1.2 and 2.8 with N = 64), and 0 at m = 3.5 and 4.
  - Additivity: D₊D₋ = 2, D₊D₊⁻¹ = 0, A0D₊A0⁻¹ = 1, D₊S = 1, D₊⁻¹ = −1.
  - Also seen: −2 at m = 0.5 and +1 at m = −2, the Wilson-type pattern.

## (b) The single node: confirmed

D₊ and D₋ were checked at m = 2 and 2.5.
- At −k* the spectrum is 1 ten times and −1 twice.
- On a 48³ grid, the closest approach to −1 outside a 0.3-ball around −k* is 0.339.
- All 120 Nelder–Mead minimisations converge to −k*.
- The cone is isotropic with speed 1/(3−m) (1 and 2), spread < 1e−6 and tilt ≤ 3e−12.
- FHS charges: lower band −1, upper +1, pair 0; the inverse flips the sign.
- Exact argument: n̂₄ = −1 forces q = (π,π,π).

## (c) S6: the logic is correct (K-theory recalled, not re-derived)

- **K₁ of the Laurent ring.** K₁(A[t,t⁻¹]) = K₁(A) ⊕ K₀(A) for regular A, and K₀(C[Zⁿ]) = Z (Quillen–Suslin–Swan). So K₁(C[Z³]) = C^× ⊕ Z³ and SK₁ = 0. Suslin's unstable SL_n = E_n is not needed, since W₃ is stable under U ↦ U ⊕ 1.
- **W₃ on GL_n.** W₃ is homotopy-invariant on maps T³ → GL_n (GL_n retracts onto U(n)) and additive under products. Elementaries contribute 0, and the abelian determinant factor contributes 0.
- **The hypothesis needs a finite-range inverse,** which is automatic for finite-range unitaries (U⁻¹ = U†). Control c5: D₊ truncated to Fourier range 6 is a Laurent GL map with W₃ = 1, but it is not unitary and its inverse is not finite range.
- **Numerical tests:**

  | Test | Unitaries | W₃ |
  |---|---|---|
  | c1 | finite-range covariant words | ≤ 3e−11 |
  | c2 | exp(iH) words | ≤ 1e−4 at N = 20 → 0; control with D₊ inserted gives 0.99999 |
  | c3 | random non-covariant finite-depth circuits | ≤ 1e−9 |
  | c4 | a non-circuit finite-range 1 − P + zP | 4e−12; quasi-local Chern-1 control gives 1.00000 |

- **New exact corollary.** sup_k ‖V − D_b‖ = 2 for every finite-range unitary V. Otherwise V·D_b⁻¹ never has eigenvalue −1, its logarithm gives a homotopy to 1, and W₃(V) = 1, contradicting S6. So D_b is not a norm limit of strictly local unitaries.

## (d) Framing

1. **"The obstruction is false in the declared C¹ class; it is a locality statement": fair, with a caveat.**
   - W₃ ≠ 0 rules out a spectral gap at every quasi-energy: if e^{iE} were never an eigenvalue, a logarithm cut at E would give a homotopy to 1.
   - The D_b step has closed quasi-energy surfaces around −k* at every E ∈ (0, π), and a 10-fold flat band at E = 0 touching the D_b block at 7 points.
   - "Single node, no doubler" holds in the node-counting sense at E = π.
2. **Q2's 7 nodes are for D₊·C̄** (complement moved to −1), not for D_b alone.
3. **Prior art (recollection).** For Hamiltonians, net chirality vanishes for any continuous H(k); SLAC escapes only by discontinuity. For Floquet unitaries, net chirality equals W₃ (Bessho–Sato, PRL 127, 196404 (2021)). The Floquet loophole is wider: analytic, exponentially local unitaries escape it. The locality that matters is finite range or generation by a local Hamiltonian. S6 resembles Dubail–Read 2015 and Chen et al. 2014 (no compact flat Chern bands); its novelty for 3D unitaries is unchecked.
4. **Admissibility.** By the corollary, admitting D_b is a real change of premise, not a limit of admissible steps.

## Corrections (applied by the supervisor to `../C12_winding_letters/FINDINGS.md`)

1. Gaplessness at every quasi-energy, and the node-counting sense of "no doubler".
2. Q2 refers to D₊·C̄.
3. Prior-art framing.
4. The norm-distance-2 corollary.
5. Status: S6's logic re-derived; D_b checked on a different build.
