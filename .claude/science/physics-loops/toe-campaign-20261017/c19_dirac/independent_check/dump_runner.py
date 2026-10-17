"""Exec the runner's own source up to Part 4 (no edits) and dump its Hb, Mm Bloch blocks for comparison."""
import pickle, sys, numpy as np
src = open('/home/user/qubit-lattice-axiom-framework/scripts/corner_fermion_massless_dirac_pair_protected_by_cube_rotations_and_pseudoscalar_dirac_mass_2026_10_17.py').read()
src = src.split('# ---------------- Part 4')[0]
g = {'__file__': '/home/user/qubit-lattice-axiom-framework/scripts/x.py', '__name__': 'rr'}
exec(compile(src, 'runner', 'exec'), g)
bl = g['bl']; blM = g['blocks_from'](g['Mm'])
pickle.dump(dict(bl=bl, blM=blM, kst=g['kst'], vel=g['vel'], EN=g['EN']), open('runner_blocks.pkl', 'wb'))
print('dumped', len(bl), len(blM))
