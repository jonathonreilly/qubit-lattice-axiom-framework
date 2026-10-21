"""Conditional FRW continuity algebra, not a derivation of vacuum dynamics.

Stable historical filename. All geometry, Lambda identification, conservation
and fixed-radius premises are supplied. No audit or observational status follows.
"""
import sympy as s


def main():
    R, c, G, H = s.symbols("R c G H", positive=True)
    Rd, w, Q, lp = s.symbols("Rdot w Q lp", real=True)
    rho = 3*c**4/(8*s.pi*G*R**2)
    drho = s.diff(rho, R)*Rd
    continuity = drho + 3*H*(1+w)*rho - Q
    solution = s.solve(continuity, w)[0]
    checks = {
        "fixed positive radius, separate conservation implies w=-1":
            s.simplify(solution.subs({Rd:0,Q:0})+1)==0,
        "varying radius R proportional to scale factor gives w=-1/3":
            s.simplify(solution.subs({Rd:H*R,Q:0})+s.Rational(1,3))==0,
        "H=0 fixed radius leaves w unconstrained":
            s.simplify(continuity.subs({H:0,Rd:0,Q:0}))==0,
        "exchange Q=3H rho permits w=0 at fixed radius":
            s.simplify(continuity.subs({Rd:0,w:0,Q:3*H*rho}))==0,
    }
    corrected = rho*(1-lp**2/(4*R**2))
    checks["fixed R and lp correction has zero time derivative"] = (
        s.simplify(s.diff(corrected,R)*0+s.diff(corrected,lp)*0)==0)
    checks["variable lp correction need not be constant"] = s.diff(corrected,lp)!=0
    print("Supplied rho=3c^4/(8 pi G R^2); positive corrected rho requires |lp|<2R.")
    print("General conditional solution:",solution)
    for name, ok in checks.items():
        print(("PASS" if ok else "FAIL")+": "+name)
    print("No microscopic vacuum identification, fixed-R dynamics or observed precision is checked.")
    if not all(checks.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
