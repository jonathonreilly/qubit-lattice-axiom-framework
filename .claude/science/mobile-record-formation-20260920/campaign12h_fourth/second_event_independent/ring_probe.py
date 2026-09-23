from pathlib import Path
import json
import numpy as np
from scipy.linalg import eigh
from operators import ring_operators, first_outputs, group_eigenvalues
D = Path(__file__).resolve().parent
rows = []
for theta in (0., .217, np.pi / 4, np.pi / 2, 1.11):
    basis, H2, H4, G, _, _ = ring_operators(4, theta)
    ev, V = eigh(H2)
    outputs = first_outputs(4, basis)
    blocks = []
    for ids in group_eigenvalues(ev):
        U = V[:, ids]
        g, w = eigh(U.conj().T @ G @ U)
        h4 = U.conj().T @ H4 @ U
        blocks.append({'energy': float(ev[ids[0]]), 'dimension': len(ids),
                      'loss_eigenvalues': g.tolist(),
                      'H4_eigenvalues': eigh(h4, eigvals_only=True).tolist(),
                      'H4_loss_commutator_norm': float(np.linalg.norm(h4 @ (U.conj().T @ G @ U) - (U.conj().T @ G @ U) @ h4)),
                      'weights_by_loss_eigenvector': [abs(w.conj().T @ U.conj().T @ a).tolist() for a in outputs],
                      'total_output_weights': [float(np.linalg.norm(U.conj().T @ a)**2) for a in outputs]})
    rows.append({'theta': theta, 'Gamma_eigenvalues': eigh(G, eigvals_only=True).tolist(),
                 'H2_Gamma_commutator': float(np.linalg.norm(H2 @ G - G @ H2)),
                 'H2_H4_commutator': float(np.linalg.norm(H2 @ H4 - H4 @ H2)),
                 'H4_Gamma_commutator': float(np.linalg.norm(H4 @ G - G @ H4)),
                 'initial_loss': [float(np.vdot(a, G @ a).real) for a in outputs],
                 'blocks': blocks})
out = {'scope': 'Independent numerical probe from complete legal charge/field moves; weights_by_loss_eigenvector are amplitudes, not squared probabilities.', 'rows': rows}
(D / 'RING_PROBE_RESULTS.json').write_text(json.dumps(out, indent=2) + '\n')
print(json.dumps(out, indent=2))
