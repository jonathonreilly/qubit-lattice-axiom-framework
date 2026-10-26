"""Geometric entropy comparisons and countermodel to the former B2 premise."""
import math

AUDIT_TIMEOUT_SEC = 30


def main():
    checks = []
    def check(name, ok):
        checks.append(bool(ok))
        print(f"{'PASS' if ok else 'FAIL'}: {name}")
    G = 1.
    for R in (.1,1.,10.,100.):
        for fraction in (.01,.5,1.):
            E = fraction*R/(2*G)
            bh = 4*math.pi*G*E**2
            target = 2*math.pi*R*E
            area_bound = math.pi*R**2/G
            check(f"geometric ordering {R},{fraction}", bh<=target+1e-10 and target<=area_bound+1e-10)
            if fraction == 1:
                check(f"boundary equality {R}", math.isclose(bh,target))
    E,R = .01,100.
    entropy = -sum(p*math.log(p) for p in (.5,.5))
    check("qubit positive energy and sub-Schwarzschild parameters", E>0 and 2*G*E<R)
    check("qubit violates former B2", entropy>4*math.pi*G*E**2)
    check("qubit respects weaker target expression", entropy<2*math.pi*R*E)
    print(f"SUMMARY: PASS={sum(checks)} FAIL={len(checks)-sum(checks)}")
    print("No universal matter-entropy bound is proved by these checks.")
    return 0 if all(checks) else 1


if __name__ == '__main__':
    raise SystemExit(main())
