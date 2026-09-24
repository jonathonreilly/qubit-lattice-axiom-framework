#!/usr/bin/env python3
"""Independent discriminant for the zone-edge transcription at the finder's Pythagorean point."""
from fractions import Fraction as F
import math


def main():
    cw2, sw2 = F(96, 2305), F(2303, 2305)
    ce, se = F(24, 25), F(7, 25)
    assert cw2 * cw2 + sw2 * sw2 == 1
    assert ce * ce + se * se == 1
    cw = cw2 * cw2 - sw2 * sw2
    c2 = ce * ce - se * se
    tr = cw * (1 + c2)
    det = c2
    disc = tr * tr - 4 * det
    d = float(disc)
    t = float(tr)
    r1 = (t + math.sqrt(d)) / 2
    r2 = (t - math.sqrt(d)) / 2
    omega = 2 * math.acos(float(cw2))
    eps = math.acos(float(ce))
    g = (1 + float(c2)) / (2 * math.sqrt(float(c2)))
    om_c = math.acos(min(1.0, 1 / g))
    print(f"disc {float(disc):.6e} roots {r1:.4f} {r2:.4f}")
    print(f"omega {omega:.4f} eps {eps:.4f} omega_c {om_c:.4f} pi-omega {math.pi-omega:.4f}")
    if disc > 0 and r1 < 0 and r2 < 0 and omega > 10 * om_c and math.pi - omega < om_c:
        print(
            "HIT: confirmed - at eps=0.2838, omega=3.0583 (about 36 times omega_c) the transfer "
            "discriminant is positive and both roots are real and negative, so the zone edge is overdamped"
        )
        print(
            "SUMMARY: confirmed the window law misses a zone-edge window of the same width as the infrared window"
        )
    else:
        print("SUMMARY: not reproduced - the zone-edge point is not overdamped")


if __name__ == "__main__":
    main()
