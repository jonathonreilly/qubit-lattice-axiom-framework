# 24^3 fixed-momentum test (Campaign 5, 2026-09-27)

Open PR 9361 puts the per-field curvature estimate on 24^3 at k = pi/12 at 0.856 +- 0.042 (four seeds, 960 walkers), below 20^3
(0.990 at pi/10) and 16^3 (1.061 at pi/8), with a 24^3 energy per plaquette 0.0036 below the 8^3 population-free value. A 24^3
doubled-population run (seeds 603, 604 at 1920 walkers) is in progress in Campaign 5.

This runner measures 24^3 at k = pi/6 (the second mode), the same momentum as 12^3's smallest (1.057 +- 0.013 at 3840 walkers, open
PR 9356). An estimate near 1.06 places the 24^3 decrease in the momentum (softening); one near 0.86 places it in the torus or its
population. Self-contained (projector code from open PR 9328's runner); about 3.2 h at 960 walkers; memory about 0.55 GB.
