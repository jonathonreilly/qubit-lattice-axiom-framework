import sys, pickle, subprocess
sys.path.insert(0, '/home/user/qubit-lattice-axiom-framework/scripts')
import cubic_covariant_nearest_neighbour_stabilizer_rules_one_qubit_defects_2026_10_17 as c1
ACTION = sys.argv[1]
d = pickle.load(open(f'orb3q_{ACTION}.pkl', 'rb'))
n = len(d['reps']); cl = c1.maximal_cliques(n, d['adj'])
print('orbits', n, 'maximal cliques', len(cl), 'sizes', sorted(len(c) for c in cl)[-15:], flush=True)
pickle.dump(cl, open(f'cl3q_{ACTION}.pkl', 'wb'))
