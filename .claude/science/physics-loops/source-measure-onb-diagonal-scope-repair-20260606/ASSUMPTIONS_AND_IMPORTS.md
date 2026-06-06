# Assumptions And Imports

Load-bearing assumptions:

- `V = C^6`.
- `O_i = E_ii` for `i = 1..6`.
- `D_6` is the diagonal subspace of `End(V)`.
- The pairing is `<A,B>_HS = Tr(A^dagger B)`.

No load-bearing repo-status dependency is used. The finite linear algebra is
constructed and checked directly by the runner.

Explicitly not imported:

- physical `Y_T` top/`W` source semantics;
- `g_bare = 1`;
- any `F_Htt` form-factor formula;
- `N_c = 3` as a physical color theorem;
- observed or fitted Standard-Model values.
