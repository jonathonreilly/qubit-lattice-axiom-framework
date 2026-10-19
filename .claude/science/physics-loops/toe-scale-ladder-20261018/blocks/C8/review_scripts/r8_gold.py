#!/usr/bin/env python3
"""b_gold runs of route B. 'author' frame: the h-plane frame produced by the author's build_F (imported ONLY to
reproduce the author's otherwise unstated mass direction; at b_gold W = 0, so chi is not defined by W).
Usage: r8_gold.py frame theta n   (frame = author | own)"""
import sys, os
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import r8_routeB as rb
fr, th, n = sys.argv[1], float(sys.argv[2]), int(sys.argv[3])
Fh = None
if fr == 'author':
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'scripts'))
    import c8_core as cc
    Fh = cc.build_F(cc.POINTS['gold'])[1:]
c = rb.run('gold', n, th, np.pi/2, 'M1', Fh=Fh)
print(fr, th, n, {k: f"{v:.6e}" for k, v in sorted(c.items())}, flush=True)
