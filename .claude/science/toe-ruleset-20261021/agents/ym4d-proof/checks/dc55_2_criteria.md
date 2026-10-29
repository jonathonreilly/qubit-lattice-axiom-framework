# dc55_2 — gauge-action composition law and the two cocycle forms (criteria written before the script)

Author: Opus 5.5 worker (claude-opus-5-5). Writes only checks/dc55_2_* . Exact rational arithmetic (fractions.Fraction) only.

## Claims under test (DICT55.md §1, convention C4)
For a link b = (b^-, b^+) and pointwise group-valued gauge functions g, g′ (pointwise product (g′g)(x) := g′(x)g(x)):
- (L) left action U^g(b) := g(b^-)U(b)g(b^+)^{-1}: (U^g)^{g′} = U^{g′g}  [the convention (U^a)^b = U^{ba}];
- (R) right action U^g(b) := g(b^-)^{-1}U(b)g(b^+): (U^g)^{g′} = U^{gg′}  [the convention (U^a)^b = U^{ab}];
- (Cocycle) if a map V ↦ Z(V) obeys Z(V^h) = Z(V)^{ĥ(h,V)} and ĥ is consistent, then the consistency condition reads
  ĥ(h_2h_1, V) = ĥ(h_2, V^{h_1})ĥ(h_1, V) for the left action and ĥ(h_1h_2, V) = ĥ(h_1, V)ĥ(h_2, V^{h_1}) for the right action.
  Test model: a single link, Z := identity map on configurations and ĥ(h, V) := h (trivially covariant), so the cocycle
  condition must hold with the convention-correct order and is tested against the opposite order.

## Test data
Exact non-commuting invertible 2×2 rational matrices (GL(2, Q); the composition law is pure group algebra, so the result for
SU(N) is the same algebra), at least 20 random instances with a fixed seed, plus one hand-chosen pair with g g′ ≠ g′ g.

## Pre-registered verdicts
- **PASS** iff: (L) holds exactly on every instance; (R) holds exactly on every instance; and both CONTROLS fire:
  - K1: the WRONG law for the left action, (U^g)^{g′} = U^{gg′}, FAILS on at least one instance;
  - K2: the WRONG law for the right action, (U^g)^{g′} = U^{g′g}, FAILS on at least one instance;
  - K3: for the trivially covariant model, the right-action cocycle order applied to the left action FAILS on at least one
    instance and the left-action order holds on all; and symmetrically for the right action.
- **FAIL** if (L) or (R) fails anywhere (then DICT55 C4 is wrong), or if any control does not fire (then the check is void).

## AMENDMENT 1 (appended before any dc55_2 script exists; replaces the K3 test model, which could not fire)
The "trivially covariant model" ĥ(h, V) := h of K3 cannot discriminate the two cocycle orders (with ĥ independent of V both
orders reduce to h-products that hold identically), so K3 as written would be a control that cannot fire. Replacement:
- Left-action model: configurations V ∈ GL(2,Q) with V^h := hV; target action t^c := ct; a NON-equivariant map
  X(V) := V M V (M fixed, non-scalar). Define c_L(h, V) := X(hV)X(V)^{-1}, so that X(V^h) = X(V)^{c_L(h,V)} by construction.
  Claim: c_L(h_2h_1, V) = c_L(h_2, V^{h_1})c_L(h_1, V) on every instance (left order). Control K3a: the right order
  c_L(h_1h_2, V) = c_L(h_1, V)c_L(h_2, V^{h_1}) FAILS on at least one instance.
- Right-action model: V^h := Vh; target action t^c := tc; X as above; c_R(h, V) := X(V)^{-1}X(Vh).
  Claim: c_R(h_1h_2, V) = c_R(h_1, V)c_R(h_2, V^{h_1}) on every instance (right order). Control K3b: the left order
  c_R(h_2h_1, V) = c_R(h_2, V^{h_1})c_R(h_1, V) FAILS on at least one instance.
PASS/FAIL as before, with K3 replaced by K3a and K3b.
