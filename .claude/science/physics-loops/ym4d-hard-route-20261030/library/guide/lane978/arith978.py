"""Row 978 (gap-ladder-max): arithmetic evaluations quoted in the note.

Not a GUIDE run and not a numeric job: sub-second, no lattice, no sampling.
Nothing in the note rests on this file; the proofs there are by hand.

(1) Section 5.6 (b), idealised law pi(t) ~ t^(-3) up to the critical extent
    N_c, rate alpha = r/N_c with r = m_0++/T_c (r = 5.2 is a RECALLED value).
    With 2m = x N_c and t + 2m = N_c the exact test of Lemma IHC reads
        g(x) = log(2/(1 + exp(r x))) - 3 log(1 - x) >= 0   on (0, 1).
    g(0) = 0 and g'(0) = 3 - r/2.  The scan gives the interior minimum.
(2) Section 5.7: 2 sinh^2(omega/2), omega^2/2 and sinh(omega) at omega = 1.3.
"""
import math


def g(r: float, x: float) -> float:
    return math.log(2.0 / (1.0 + math.exp(r * x))) - 3.0 * math.log(1.0 - x)


def interior_min(r: float) -> tuple[float, float]:
    # minimum of g on [0.05, 0.95]; the point x -> 0 (g -> 0) is excluded
    pts = [(g(r, i / 10000.0), i / 10000.0) for i in range(500, 9500)]
    return min(pts)


if __name__ == "__main__":
    for r in (5.0, 5.2, 5.25, 5.3, 5.4, 5.6, 6.0):
        gm, xm = interior_min(r)
        print(f"r = {r:.2f}: interior min of g = {gm:+.4f} at x = {xm:.3f}; "
              f"g'(0) = {3.0 - r / 2.0:+.3f}")
    w = 1.3
    print(f"omega = {w}: 2 sinh^2(omega/2) = {2 * math.sinh(w / 2) ** 2:.3f}, "
          f"omega^2/2 = {w * w / 2:.3f}, sinh(omega) = {math.sinh(w):.3f}")
