# h2_55_a2 — replacement controls for gate A3 of h2_55_a (criteria written 2026-10-29T03:21Z, AFTER the h2_55_a run and
# BEFORE any h2_55_a2 script)

Why this file exists. h2_55_a ran once (03:20Z) with 27/27 gates PASS and 6/7 controls firing; its registered verdict is
**FAIL** because control A3-F did not fire. Diagnosis (stated before writing a2's script): A3-F's premise was false. The
Bianchi contraction Σ ε_{λμνκ} p_μ S_{νκ,ρσ} annihilates every term of S in which the first-pair index ν or κ is carried
by a factor p_ν or p_κ; every term of T^I, and of the sign-flipped T′, is of that kind. So Bianchi cannot detect sign
errors inside T^I; it detects exactly the I-structure (a ≠ 0), which is what Lemma TEN uses. h2_55_a's verdict stays FAIL
as recorded; this check supplies controls that test what the gates actually claim.

## Gates (re-run of A3.1 and A3.3 unchanged)
- **G1** = A3.1 (Gram form of T^I). **G2** = A3.3 (Bi[T^I] ≡ 0 and Bi[I] has a nonzero component).
## Designed-FAIL controls
- **C1** S := T^I + I (a = 1, b = 1): Bi[S] must have a nonzero component (Bianchi forces a = 0).
- **C2** T′ (T^I with its second term's sign flipped, as in h2_55_a A3-F): the Gram identity G1 must FAIL for T′
  (a sign error in T^I is caught by the Gram form, not by Bianchi).
- **C3** S := antisymmetrised dd(mr)(ns) structure (= 2I by h2_55_a A3.2): Bi[S] must have a nonzero component.
PASS = G1, G2 hold and C1, C2, C3 fire.
