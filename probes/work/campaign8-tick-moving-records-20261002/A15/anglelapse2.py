#!/usr/bin/env python3
"""A15: angle lapse, gentler steps and both signs of theta (supplied 1D toy). Same machinery as
anglelapse_and_phantom.py: shared beat, gate angle ramps from thA to thB over 'width' sites; quasi-energy per cycle
(with the gate phases) is conserved; 'matching' lists right-moving partner momenta on the far side."""
import os, signal
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
signal.alarm(55)
import numpy as np
from anglelapse_and_phantom import run_angle
for thA, thB in ((0.3, 0.25), (-0.3, -0.25), (0.6, 0.5), (-0.6, -0.5)):
    for K0 in (np.pi - 0.3, np.pi + 0.3):
        for width in (0, 60):
            tr, rf, Kt, pred = run_angle(thA, thB, width, K0)
            print("thA=%+.2f thB=%+.2f K0=%.3f width %2d: transmitted %.4f reflected %.4f K_out %.3f matching %s"
                  % (thA, thB, K0, width, tr, rf, Kt, pred))
