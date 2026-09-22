# Block 79 — control and findings (2026-09-22)

1. Disjoint machinery (`specs/supervisor_control_block79_walls.py`): dense spectra on 3D tori; transverse plane-wave reduction along `y, z` for dispersions; the exact runner has nullspaces on the corner-reduced ring.
2. **A first scratch that found nothing (supervisor).** Sharp walls (no defect layer) gave no zero modes; smooth walls gave exact ones; the difference was tracked to the parity of the defect layer and became T2 — the comparator's rule "a zero mode at every sign change" is not the lattice's.
3. **A claim withheld (supervisor).** The wall modes' transverse velocity matrices were computed in scratch to read off a handedness per corner; the projected velocities were small and the selection of zero modes per wall was unstable; the note makes no statement about handedness and says so.
4. Finding folded: the first control's corner count used a wrong projector (weights 13.5 per corner); replaced by a transverse Fourier transform at each `x` (4.0 per corner).
5. Finding folded: a name in the Executed section caught by the scan; reworded.
