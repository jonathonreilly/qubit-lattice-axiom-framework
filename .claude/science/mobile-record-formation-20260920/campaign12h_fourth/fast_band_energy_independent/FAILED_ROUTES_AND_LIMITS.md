# Retained failures, rejected routes and limits

The first complete executable run passed all assertions. Its stderr contains
two SciPy FutureWarnings: integer W diagonals were cast to float64 when forming
the floating Hamiltonians. The exact source snapshot, stdout, stderr and
receipt remain preserved. This is not recorded as a failed scientific test.

Rejected routes:

- Treating the first high vector as immediately bright would predict the
  wrong small-time law. Its two vacancies are opposite, so the bare loss
  annihilates it. The high-band Hamiltonian then produces bright components.
- Treating that initially dark vector as permanently protected would omit
  the signed second-order Hamiltonian FF^dagger-F^dagger F. The exact path
  certificate rejects this inference.
- Dropping the rotated O(epsilon) off-block no-event terms without using the
  rapid spectral separation would give an error as large as the component
  under study. The proof instead uses an O(epsilon^3) nonunitary spectral
  similarity on the rescaled no-event problem.
- A trace-norm density approximation does not control this divergent energy.
  The proof directly tracks cluster amplitudes and the full Hamiltonian.
- A fixed-spin numerical epsilon limit is not the joint spin/resource limit.
  Both are stated separately, including their different cubic forms.
- Compact fast-time convergence does not settle fixed positive physical time,
  infinite fast-time survival, or a complete second-birth path law.
- The ideal microscopic post-mark vector is not an exact finite-window
  conditioned state. An explicit shrinking positive window controls the
  rescaled energy; its probability is not bounded below in the joint limit.

The initial canonical dressed-jump coefficient remains a provisional reused
dependency pending its separate independent comparison. No new fast-band
author packet, external personal calculation or campaign checkpoint was read.
