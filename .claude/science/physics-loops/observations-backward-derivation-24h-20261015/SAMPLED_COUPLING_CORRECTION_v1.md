# Preserved sampled-inverse correction

The first author execution returned31passing and2failing controls. The
characteristic-polynomial failure was a structural SymPy equality comparison;
the expanded difference is zero. The coefficient-sensitivity failure exposed a
real error in the derivation: differentiating the backward extrapolation with
respect to p leaves an additional -s*F2/p^2 term. Consequently the uniform
coefficient-error bound must contain (2+2*S)/p_min^2, not (2+S)/p_min^2.

Version2 corrects the derivative and bound, and compares expanded polynomial
differences. The pulse identity, recurrence, positivity proof and shape inverse
are unchanged. Version1 source, runner and failed output are retained exactly.
This is a mathematics/control correction; no empirical conclusion follows.
