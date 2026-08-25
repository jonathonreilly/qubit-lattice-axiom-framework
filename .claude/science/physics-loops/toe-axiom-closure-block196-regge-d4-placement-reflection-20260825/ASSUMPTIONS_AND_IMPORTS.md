# Assumptions And Imports

| input | allowed role | authority | forbidden promotion |
|---|---|---|---|
| Regge `DIRS15` and `gauge_map` | 15 vertex-edge directions and exact vertex-displacement Ward symbol | existing exact runner | not a reflection/full-frame closed carrier |
| Block-48 reflection union | exact 22-edge time-reflection carrier and Laurent label translations | existing bounded runner | not a D4 intertwiner or physical transfer law |
| Block-77 `raw_gauge` and `vector_placement` | ten D4 tensor rows, four link-centered gauge columns, and fixed placement chart | existing exact runner | no silent raw-column identity |
| Block-77 `ROTATIONS` | the 24 proper-spatial frames used to induce the 40-edge unoriented carrier | existing exact runner | no fitted extra rows or alternative orbit after execution |
| Block-190 source/action basis | ordering of the ten D4 tensor slots and later source typing | exact stacked parent | response and action inversion remain sealed |
| Block-192/193 L24 carrier | later periodic source placement only | exact stacked parent | no physical time, channel, cadence, or response in this block |
| Block-195 PR #7724 | exact history-channel dependency boundary and portfolio handoff | immediate parent | no broad OS/history no-go |
| full half-lattice grading | minimal group-closed placement extension `u_mu^2=z_mu^-1` and frozen `C=diag(u_mu)` | explicit target ansatz forced by the Block-77 center chart | not an axiom, clock, or physical observable |

The component-order conversion `(3,0,1,2,6,8,9,4,5,7)` is frozen before the
solve.  The gauge-carrier leg `C=diag(u_x,u_y,u_z,u_t)` is explicit, not
fitted, and may not be absorbed into an unreported column relabelling.  The
15-row coefficient support is the four singleton placement grades times
`s<=d`, decomposed into four exact 800-variable systems; the twelve
non-singleton grades are forbidden.  All 22/40 rows are induced rather than
fitted.  PR #7669 supplies no load-bearing map; pincer PR #7327 is reserved for
the conditional post-map Riesz gate.

For the 40-edge induction, embed each spatial rotation as `diag(R_3,1)`.
Canonicalize an image modulo reversal by requiring its first nonzero component
positive; if reversal is required, use the unreversed image as the anchor
offset and hence as the Laurent translation.  This convention is frozen.
