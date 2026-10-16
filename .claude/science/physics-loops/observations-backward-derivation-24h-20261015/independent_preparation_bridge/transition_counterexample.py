"""A prefix-to-drive state kick preserves quadratic closure but shifts its origin."""
AUDIT_TIMEOUT_SEC=120
import sympy as s
import json
# Real prefix coordinate a, samples1,2,3, weights3,-3,1.
# A valid clamped force at the chosen point is R=z+z², with z=2a.
# An unobserved common position kick delta=3/10 gives z=2a+delta.
a=s.symbols('a');delta=s.Rational(3,10);R=(2*a+delta)+(2*a+delta)**2
values=[R.subs(a,j) for j in [1,2,3]];weighted=sum(u*v for u,v in zip([3,-3,1],values))
rest=s.Integer(0);shifted=delta+delta**2
result={'weighted_force':str(weighted),'true_unkicked_rest_force':str(rest),'shifted_reference_force':str(shifted),'quadratic_closure_still_exact':s.Poly(R,a).degree()==2,'origin_bias_detected':weighted==shifted and weighted!=rest}
print(json.dumps(result,indent=2));assert result['origin_bias_detected']
