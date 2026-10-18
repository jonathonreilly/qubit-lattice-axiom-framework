# C2 findings: does constraint closure fix the seagull, and so the induced 1/G?

Provenance: a worker of the same model family. Checked by a fresh-context same-family agent (`../C2_check/REPORT.md`, PASS=13): confirmed, and its corrections are applied below. Saved by the supervisor from the hand-back.

| Runner | Method | Result |
|---|---|---|
| `c2_closure.py` | exact sympy, `kb.py` from B21_check | PASS=7 |
| `c2_sakharov_continuum.py` | exact sympy | PASS=4 |
| `c2_lattice_scalar.py` | numerical, two runs | PASS=5, FAIL=1 each |

The lattice FAIL is a preset convergence threshold of 1e−6 against measured values of 7e−6 and 1.4e−6. The effects reported are O(0.1–1), so it does not matter. Bug logs are kept for the first S4 ansatz. The L5 normalisation fix is explained in a code comment.

**Answer.**
- In the continuum, within the ≤ 2-derivative ansatz, closure fixes the seagull given the h-linear coupling. With B14's no-P-mixing form, it is the minimal covariant seagull.
- That seagull is **not** what restores the 06-08 bubble's Ward identity. Ward at K² is a property of the regulator and measure.
- **Closure cannot fix the induced 1/G, at any order (check).** The robust reason: covariant dim-6 couplings such as (c6 a²/2)√g R(∂φ)² are closure- and Ward-compatible, and shift 1/(16πG) by −6c6(aΛ)² × the Sakharov value, which is O(1) on a lattice.
- On the lattice, in addition, the O(a²) placement freedom (equivalently, re-identifying h → h + O(a²∂h∂h)) controls the K² contact.

## 1. Continuum closure

- **Setup.** Scalar, r = 1, field-independent lapse rule, isotropic ansatz with ≤ 2 derivatives:
  - V1: 20 candidates;
  - V2 = h²·matter²: 156 candidates.
- **{G, C}.**
  - The solution space is exactly the covariant family (√g)^t H_m(g) + ζ√gRφ², with s1 = −1 and s2 = t (a density-weight convention).
  - V2 is uniquely the second-order expansion.
  - **Homogeneous lemma:** no h²·matter² density is gauge-invariant with arbitrary N, so V2 is fixed by V1. For ultralocal couplings this is a one-line pointwise argument; it was argued, not computed, for Maxwell.
- **{C, C}.**
  - It fixes β = −1 and adds nothing at P·h·matter² for the minimal solution.
  - **ζ is decided here.** With no P–matter terms in C, ζ = 0.
  - If trP·φπ, N∇²(φ²) and φ²P² terms are allowed, one free direction remains. It is exactly the Jordan-frame map (predicted independently).
  - So ζ = 0 is a variable (frame) premise, not a canonical invariant. This corrects B21_check's "R1φ² free": that is true only in {C, G}.

## 2. Ward and the induced 1/G

- **P1 (exact).** The closure-forced minimal seagull is independent of K. Its tadpole is a pure Π(0) contact, which B4b showed cannot remove the K² break. The same holds for the covariant fermion seagull (argued, not computed).
- **P2 (exact).** A covariant proper-time regulator on Δ_g + ζR gives
  W⁽²⁾ = −Λ⁴/(64π²)[√g]⁽²⁾ − (1/6 − ζ)Λ²/(32π²)[√gR]⁽²⁾ + O(k⁴),
  and Ward holds. Here the K² contacts come from the measure factor in the regulator.
- **P4.** Proper time on the flat-measure Hessian gives a Ward ratio of 0.76; the check finds it breaks Ward already at k⁰. So Ward depends on the regulator and measure.
- **Induced 1/G (continuum, covariant regulator).** 1/(16πG) = (1 − 6ζ)Λ²/(192π²) per real scalar, the textbook heat-kernel value. ζ = 0 gives 1/G = Λ²/(12π), and conformal coupling gives zero.
- **Lattice ⟨φ²⟩ estimate only, a heuristic:** G ≈ 1.54 a² (m → 0), 1.64 a² (m = 0.5), 1.88 a² (m = 1) per minimally coupled scalar. The convention-free form is 1/(16πG) = (1/6 − ζ)⟨φ²⟩/2.
- **Remaining premises:** the regulator; ζ/frame; and the absence of covariant dim-6 couplings, scalar (check) and fermion a·√gRψ̄ψ (argued).

## 3. Lattice

There are three transcriptions of the closure-forced coupling: S (site-local), M1 (corner mean of h) and M2 (corner mean of W(h)).

| Transcription | Ward ratio | c_EH | × covariant reference | non-EH fraction |
|---|---|---|---|---|
| S | 0.64–1.06 | −0.0026 | −0.21 | 0.97 |
| M1 | 0.42–1.79 | +0.0044 | +0.36 | 0.98 |
| M2 | 0.42–1.06 | −0.0043 | −0.36 | 0.92 |

- M1 and M2 differ only by O(a²) leg placement, yet their K² symbols differ by 3.36 and the EH projection changes sign.
- That difference is exactly the a²Λ⁴ placement tadpole (residual 7e−8).
- No placement interpolation restores Ward; the best ratio is 0.85.
- **Reading:** the Ward ratio and c_EH depend on identifying site-h as the metric (check reframing). M1 = M2 after h → h + Q(h,h), and with a nonzero tadpole such a re-identification adds any hypercubic form. 1/G_ind is power-divergent and is not fixed by closure, which in any case holds only up to O(a²) (B14 E5).
- **What could fix it:** the complete microscopic lattice action; spectral sum rules (boson–fermion cancellation of the tadpoles); or a perfect-action principle, which depends on the blocking kernel.
- **B4b's 9-dimensional seagull space (interpretation):** 8 non-covariant placement directions that closure does not see, plus 1 covariant EH direction.

## Derived vs supplied

- **Derived:**
  - V2 fixed by V1;
  - the covariant family, with ζ = 0 under no-P-mixing;
  - K-independence of the minimal seagull;
  - the covariant Sakharov coefficient;
  - the O(1) lattice Ward violation and placement dependence (numerical).
- **Supplied:** H0, r = 1, the lapse rule, the ansatz, the regulator, the frame, and the transcriptions.
- **Not done:** Maxwell and fermion lattice numerics, P·h·matter² at ζ ≠ 0, higher orders.

## Prior art (from memory)

- Sakharov 1967; Visser 2002; Adler 1982; Zee 1981; Frolov–Fursaev–Zelnikov.
- DeWitt and Gilkey heat-kernel coefficients.
- Deser 1970; Gupta; Kraichnan; Feynman; Weinberg 1964–65.
- HKT; Flanagan 2004 (frames); Teitelboim 1973; Kuchař.
- Dittrich 2008; Bahr–Dittrich 2009; Gambini–Pullin; Jacobson (UV sensitivity of induced G); EFT field-redefinition shifts.
- Pauli–Villars Ward cures; lattice power-divergent mixing.
