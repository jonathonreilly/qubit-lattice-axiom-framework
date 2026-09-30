#!/usr/bin/env python3
"""T25 test C: what is left of the species-labelling wall after naming and registration are removed?
C1 proper cubic rotations act on the three hw=1 corners as the full S3 (order 6).
C2 circulant with complex b: a transposition maps b->b*, spectrum invariant, mass order over Z3 characters flips.
C3 two circulant sectors: mixing V = U_u^dag U_d is a permutation matrix (monomial), for all (a,|b|,delta).
Pre-registration: PREREGISTER.md.
"""
import itertools, json
import numpy as np

out = {}
# ---- C1: action of the 24 proper rotations on hw=1 corners (momentum pi*e_i, sign of momentum irrelevant mod 2pi) ----
group = set()
for perm in itertools.permutations(range(3)):
    for signs in itertools.product((1, -1), repeat=3):
        R = np.zeros((3, 3))
        for i in range(3):
            R[perm[i], i] = signs[i]
        if round(np.linalg.det(R)) == 1:
            group.add(perm)   # signs act trivially on pi*e_i (pi ~ -pi)
out["C1_image_of_24_rotations_on_hw1_corners_order"] = len(group)
print("C1 image order:", len(group), sorted(group))

# ---- C2 ----
w = np.exp(2j * np.pi / 3)
J = np.roll(np.eye(3), 1, axis=0).astype(complex)
T = np.eye(3)[[1, 0, 2]].astype(complex)   # transposition of corners 1,2
F = np.array([[1, 1, 1], [1, w, w ** 2], [1, w ** 2, w]]).T / np.sqrt(3)  # columns: characters q=0,1,2
rng = np.random.default_rng(3)
rows = []
for _ in range(5):
    a = rng.normal(); b = abs(rng.normal()) * np.exp(1j * rng.uniform(0.1, 1.0))
    H = a * np.eye(3) + b * J + np.conj(b) * J.conj().T
    Hp = T @ H @ T.conj().T
    evs, evp = np.linalg.eigvalsh(H), np.linalg.eigvalsh(Hp)
    # circulant form of Hp
    bp = Hp[1, 0]   # entry coupling e1->e2
    ok_circ = np.allclose(Hp, a * np.eye(3) + bp * J + np.conj(bp) * J.conj().T)
    # diagonal of F^dag H F gives eigenvalue on character q
    dq = np.real(np.diag(F.conj().T @ H @ F)); dqp = np.real(np.diag(F.conj().T @ Hp @ F))
    order = list(np.argsort(dq)); orderp = list(np.argsort(dqp))
    rows.append({"spectrum_equal": bool(np.allclose(evs, evp)), "Hp_is_circulant": bool(ok_circ),
                 "b_->b*": bool(np.isclose(bp, np.conj(b))), "char_order": order, "char_order_after_T": orderp,
                 "flipped_q<->-q": bool(orderp == [(-x) % 3 for x in order])})
out["C2"] = [{k: (v if not isinstance(v, (np.integer,)) else int(v)) for k, v in r.items()} for r in rows]
out["C2"] = json.loads(json.dumps(rows, default=lambda o: int(o) if isinstance(o, np.integer) else str(o)))
print("C2 rows:", rows[:2])

# ---- C3 ----
worst = 0.0
mono = True
for _ in range(200):
    def circ():
        a = rng.normal(); b = abs(rng.normal()) * np.exp(1j * rng.uniform(0, 2 * np.pi))
        return a * np.eye(3) + b * J + np.conj(b) * J.conj().T
    Hu, Hd = circ(), circ()
    _, Uu = np.linalg.eigh(Hu); _, Ud = np.linalg.eigh(Hd)
    V = Uu.conj().T @ Ud
    P = np.abs(V) ** 2
    # monomial: each row has one entry ~1
    dev = np.max(np.abs(P - np.round(P)))
    worst = max(worst, dev)
    mono &= bool(dev < 1e-8)
out["C3_all_random_circulant_pairs_give_monomial_mixing"] = mono
out["C3_worst_deviation_from_permutation"] = worst
print("C3 monomial:", mono, "worst dev", worst)

ok1 = out["C1_image_of_24_rotations_on_hw1_corners_order"] == 6
ok2 = all(r["spectrum_equal"] and r["Hp_is_circulant"] and r["b_->b*"] and r["flipped_q<->-q"] for r in rows)
out["verdict_PASS"] = bool(ok1 and ok2 and mono)
print("VERDICT PASS =", out["verdict_PASS"])
json.dump(out, open("test_T25C_results.json", "w"), indent=1, default=str)
