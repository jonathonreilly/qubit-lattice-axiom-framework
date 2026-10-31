"""h4: threshold arithmetic (informational; [inference] where the one-loop rate is used). Criteria: checks/h4_criteria.md."""
import math

L, d, kappa = 3, 4, 1.0
Ad = (d - 1) * L * (L - 1) / 2
ok = True
print("N eps1 | eta_1(RS) eta_q(RS-lin) | a_eta(RS) a_eta(lin) | a_RS(c=625) a'_RS(c=81) | a'' | n_sharp(B0=0) n_H(B0=0.1) n_H(B0=1)  [old route | new route]")
for N in (2, 3):
    beta = 11 * N ** 2 / (12 * math.pi ** 2)
    d0 = min(1 / (640 * N), 2 / N ** 3)
    for e1 in (0.25, 0.5, 1.0):
        eta1 = min(e1 / (2 * L ** 2), e1 ** 2 / (512 * N * Ad))
        etaq = min(e1 / (2 * L ** 2), e1 / (256 * N * Ad), d0 / Ad)
        ae1, aeq = eta1 ** 2 / (2 * N), etaq ** 2 / (2 * N)
        aRS = min(ae1, kappa * e1 ** 2 / (256 * N)) / 625
        aRSn = min(aeq / 81, kappa * e1 ** 2 / (1024 * N))
        app = 0.9 * e1 ** 2 / (4 * N)
        row = []
        for a in (min(app, aRS), min(app, aRSn)):
            ns = [math.floor((4 + 38416 * B0 / math.log(L)) / (a * beta)) for B0 in (0.0, 0.1, 1.0)]
            if not (ns[0] == math.floor(4 / (a * beta)) and ns[0] <= ns[1] <= ns[2]):
                ok = False
            row.append(ns)
        print(f"{N} {e1} | {eta1:.2e} {etaq:.2e} | {ae1:.2e} {aeq:.2e} | {aRS:.2e} {aRSn:.2e} | {app:.3f} | "
              f"{row[0][0]:.3e} {row[0][1]:.3e} {row[0][2]:.3e} | {row[1][0]:.3e} {row[1][1]:.3e} {row[1][2]:.3e}")
print(f"I1: {'PASS' if ok else 'FAIL'}")
