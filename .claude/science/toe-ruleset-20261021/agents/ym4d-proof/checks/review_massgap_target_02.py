"""Diagnostic for the preserved structural-equality failure in control 01."""
import sympy as s,json,sys
from datetime import datetime,timezone
q,w=s.symbols('q w',positive=True);C=w*q+(1+w)*q**3;lhs=s.expand(C-w*q);rhs=(1+w)*q**3
residual=s.Poly(lhs-rhs,q,w);remaining=s.Poly(lhs,q,w)
checks={'original_structural_equality_failure_reproduced':lhs!=rhs,'intended_polynomial_identity_exact':residual.is_zero,'remaining_coefficients_positive':all(c>0 for c in remaining.coeffs()),'remaining_monomials_positive_on_positive_variables':all(all(e>=0 for e in exponents) for exponents,c in remaining.terms())}
print(json.dumps({'utc':datetime.now(timezone.utc).isoformat(),'checks':checks,'passed':sum(bool(x) for x in checks.values()),'total':len(checks),'expanded_left':str(lhs),'unexpanded_right':str(rhs),'exact_residual':str(residual.as_expr()),'diagnosis':'Structural SymPy equality was the wrong equality test. The exact polynomial residual is zero and the positive remainder proves the intended lower bound. Original 15/16 output is preserved.'},indent=2,sort_keys=True));sys.exit(0 if all(checks.values()) else 1)
