# Assumptions And Imports

## Load-Bearing Premises

- Finite set of local interaction supports on finite Lambda.
- Uniform local-term norm bound `J`.
- Finite interaction-graph adjacent-term degree `D_I`.
- Lattice `ell_1` range bound `R_0 = 2a` for plaquette/hop/on-site terms.
- Duhamel expansion and operator-norm triangle/submultiplicativity.

## Forbidden Inputs Not Used

- No black-box Lieb-Robinson theorem.
- No thermodynamic-limit or continuum claim.
- No Yang-Mills mass gap.
- No completed cluster-decomposition filter theorem.
- No audit verdict edit.

## Repair

The invalid sequence count based on arbitrary support-union growth is replaced
by a chain count where consecutive local terms overlap. A chain reaching `Y`
from `X` must have length at least `ceil(dist_1(X,Y)/R_0)`, and the number of
length-`n` chains is bounded by `N_X D_I^(n-1)`.
