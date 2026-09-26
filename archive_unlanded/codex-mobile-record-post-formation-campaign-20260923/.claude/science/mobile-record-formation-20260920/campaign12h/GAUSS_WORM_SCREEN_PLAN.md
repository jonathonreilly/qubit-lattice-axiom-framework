# Pre-output plan: a static single-species loop-ensemble screen

2026-09-21, before production output. This explores the supplied thirteen-label
Gauss ensemble at z_B=0, beyond the independently checked dilute domain.
It is a mathematical equilibrium sampler that creates and removes auxiliary
currents. It is not the physical irreversible, permanent-record dynamics and
does not repair the formation-locality counterexample.

State: E_i(x) is zero except for at most one component of size+/-1 at each
site. D2 E(x)=sum_i[E_i(x+e_i)-E_i(x-e_i)]. The target closed-state law is
pi_z proportional z^(occupied sites) 1_(D2 E=0), z>0, on an odd periodic
cubic lattice. B labels are absent, not summed over.

Worm extension: store tail t and head h, with D2 E=delta_t-delta_h.
Choose uniformly one of six head steps (i,s), propose adding s to
E_i(h+s e_i) and moving h to h+2s e_i. Permit creation in a vacant slot
or removal of the opposite signed same-axis record, and reject any capacity
violation. Accept with min(1,z^Delta_n). Reverse steps undo the update,
with symmetric proposals; the extended weight z^n obeys detailed balance.
When h=t, a uniform relocation of both endpoints also preserves that
extended measure. The closed-state trace chain samples the desired law.
Count closed self transitions, including rejected proposals; dropping them
would change the trace-chain weights. No worm is force-closed or discarded
because it is long. Initialization and finite mixing remain separate issues.

Finite-volume accessibility has a direct proof. Regard each occupied slot as
a directed charge-graph edge from x-e_i to x+e_i, reversed when its sign is
negative. At a closed configuration every vertex is balanced, so the finite
directed graph decomposes into directed cycles. A worm following one cycle
backwards removes its edges with positive acceptance; repeating reaches the
empty state. Reversing these paths reconstructs any desired closed state
without violating midpoint capacity. Tail relocation permits starting at any
cycle vertex. Thus all closed states communicate at finite positive z, including
winding sectors. This proof does not provide a usable mixing-time bound.

Before production: verify the exact extended and trace-chain stationary law
on a one-dimensional three-site toy by rational linear algebra; compile the
general-dimensional sampler; check exact divergence at every measured
three-dimensional closed state. The small-dimensional check establishes
implementation controls, not the separate graph proof or a mixing estimate.

Production parameters fixed now: L in{9,13,17}, z in{0.2,1,4}, two chains
per pair, initialized empty and with every site carrying+e1 respectively.
Each chain uses5,000,000 burn-in attempted head moves followed by25,000,000
production attempts. Seeds are20260921300+case_index*2+initialization_index,
where case_index uses ascending L then ascending z. For z<0.5 sample every
1024th production closed-state visit; otherwise sample every visit. Eight
worker threads at most. Runtime calibration does not change scientific
targets; any uncompleted case remains explicitly uncompleted.

Record each sample's attempted-move index, occupation, four transverse
spectral traces and three global signed contents. Modes are(1,0,0),(2,0,0),
(1,1,0),(2,2,0), with physical lattice wave vector2pi mode/L.
Define S_T=|sum_x E(x)exp(-ik.x)|^2/(2L^3). At a closed state, the
longitudinal projection using sin(k) must vanish to rounding precision.
Exact integer Gauss constraints are checked separately. Initial full states
have nonzero winding; their agreement with empty-start chains is a useful
mixing diagnostic, not an imposed target.

Analysis: report both initializations separately before pooling. Estimate
uncertainty with nonoverlapping trace-sample blocks; fewer than16 complete
blocks of128 samples gives an insufficient-statistics flag. Compare density,
zero-mode behavior and the ratios S_T(mode1)/S_T(mode2), with paired block
resampling. Do not claim equilibration from one apparent plateau. For an
analytic quadratic regime the ratio approaches1/4 as L grows; a flat
transverse infrared spectrum would approach1. At finiteL the dilute leading
formula is8z^4|sin(k)|^2. That formula is a comparison at z=0.2, not a
controlled error bound there: its rigorous small-fugacity domain is much
smaller. No phase transition, scaling exponent, Coulomb phase, quantum
vacuum or formation-selected state is established by this finite screen.

Decision: a reproducible flat-spectrum tendency would justify a larger,
independently checked equilibrium study. Initialization disagreement,
poor winding exploration or insufficient blocks makes that case inconclusive.
Either result is preserved; no retrospective choice of favorable wave modes.
