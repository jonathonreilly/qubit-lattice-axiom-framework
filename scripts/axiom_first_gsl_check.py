"""Conditional generalized-entropy balance; does not prove the GSL."""
import math

AUDIT_TIMEOUT_SEC = 30


def main():
    checks = []
    def check(name, ok):
        checks.append(bool(ok))
        print(f"{'PASS' if ok else 'FAIL'}: {name}")
    G, M, E = 1., 2., .1
    before = 4*math.pi*G*M*M
    after = 4*math.pi*G*(M+E)**2
    delta = after-before
    check("supplied Schwarzschild entropy increment", math.isclose(delta,8*math.pi*G*M*E+4*math.pi*G*E*E))
    for fraction in (.5, 1., 1.5):
        exterior_change = -fraction*delta
        total = delta+exterior_change
        check(f"absorption balance at fraction {fraction}", math.isclose(total,(1-fraction)*delta,abs_tol=1e-12))
        check(f"exterior entropy decreases at fraction {fraction}", exterior_change < 0)
    check("positive area alone does not imply entropy balance", delta > 0 and delta-1.5*delta < 0)
    evaporative_delta = 4*math.pi*G*(M-E)**2-before
    check("evaporation has decreasing supplied area", evaporative_delta < 0)
    check("insufficient assigned radiation fails balance", evaporative_delta+.5*abs(evaporative_delta)<0)
    check("sufficient assigned radiation satisfies balance", evaporative_delta+1.5*abs(evaporative_delta)>0)
    print(f"SUMMARY: PASS={sum(checks)} FAIL={len(checks)-sum(checks)}")
    print("Conditional bookkeeping only; no physical GSL proof.")
    return 0 if all(checks) else 1


if __name__ == '__main__':
    raise SystemExit(main())
