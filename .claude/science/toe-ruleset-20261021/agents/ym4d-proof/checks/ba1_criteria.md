# ba1 criteria (BFT lane A). Written 2026-10-28 04:48 UTC, BEFORE the script ba1_cz.py exists and before any output.

## Object
The degree-0 lattice Calderon-Zygmund kernels that carry COMP-F1's |x|^-4 tail (PROOF [S22] COMP-F1; LINEAR_PACKAGE
Prop 3.7: the Pi_ex part of the fine-curvature map). On the 4D periodic torus of side N (fine units; ONE coarse unit when
N = n = L^k), with the lattice Laplacian symbol phi(p) = sum_a |nu_a|^2, nu_a = e^{ip_a} - 1, and p = 0 removed:
- K12: symbol nu_1 conj(nu_2) / phi   (a mixed second difference of the Green function);
- K11: symbol (|nu_1|^2 + |nu_2|^2)/phi - 1/2   (the (12,12) entry of Pi_ex = d Delta^-1 d^* on 2-forms, minus its
  angular mean 1/2; the p = 0 value set to 0).
Both kernels sum to 0 over the torus (p = 0 value 0).

## Quantities (for each N in {6, 9, 12, 18, 27, 36, 54}; 9 = 3^2, 27 = 3^3 are depths k = 2, 3 at L = 3)
- S1(N) := sum_y |K(y)|: the l^inf -> l^inf norm of convolution by K (sup -> sup).
- A_alpha(N) := N^-alpha sum_{y != 0} |K(y)| |y|^alpha (|y| the torus-minimal Euclidean length), alpha = 0.5 and 0.25:
  the exact norm bound of g -> K*g from (pointwise alpha-Hoelder seminorm in coarse units, [g]^c = N^alpha [g]) to sup,
  valid because sum_y K = 0 (triangle inequality: |K*g(x)| = |sum_y K(y)(g(x-y) - g(x))|).
- C_K(N) := max_{y != 0} |y|^4 |K(y)|.
- Informational: box sums max_R |sum_{|y|_inf <= R} K(y)|; the response of the sup-worst source g = sign(K(-.)) and its
  coarse Hoelder seminorm (lower bound over axis and diagonal shifts).

## Pre-registered criteria
- A1 (sup norm grows; the COMP-F1 mechanism inside one coarse unit): for both kernels S1(N) is strictly increasing over the
  list, and S1(54) - S1(6) >= 0.5.
- A2 (coarse Hoelder -> sup is depth-uniform): for both kernels and alpha = 0.5: |A(54) - A(27)| <= 0.15 A(54), and
  max_{N >= 18} A(N) <= 1.25 min_{N >= 18} A(N).
- A3 (the kernel hypothesis of Lemma CZ-a): for both kernels C_K(54) <= 1.2 C_K(27).
- alpha = 0.25: informational only (slower convergence, N^-alpha corrections).
A FAIL is recorded as a FAIL. Scope: one coarse unit only (scales 1/n .. 1); the long-range part (G0-F3) is NOT tested.

## Resources
Under the numeric lock; nice 10; BLAS/FFT threads 1; peak < 1 GB (N = 54: arrays of 8.5e6 doubles); target < 5 min.
