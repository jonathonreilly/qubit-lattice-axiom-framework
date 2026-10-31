# dag55_1 — criteria (written 2026-10-28T23:10:58Z UTC, BEFORE the graph data file and BEFORE the checker script)

Owner: SMALLNESS_DAG.md (Step 5 / T56-5), Opus 5.5 worker (claude-opus-5-5). No git. Plain python 3, standard library
only (no third-party import, no numpy, no floats anywhere in a verdict). Run with `python3 -I -B`.

## Files (to be written after this one, in this order)
1. `checks/dag55_1_graph.py` — DATA ONLY: `NODES` (dict id -> record) and `EDGES` (list of records). No logic.
2. `checks/dag55_1_dag.py` — the checker. Imports the graph by path (no sys.path games beyond loading that one file).
3. `checks/dag55_1_out.txt` — stdout of one run, kept unaltered. Any re-run after a code fix gets a new id (dag55_2, …)
   with its own criteria file; this file is never edited after the run.

## Data model (fixed now)
- Node record: `sym` (the symbol as printed), `file`, `string` (a locating string that occurs in that file), `live`
  ∈ {live, off, superseded, unplaced}, `status` (the defining statement's status word as the source gives it), `tier`
  ∈ {0 structural source, 1 analytic/geometric constant, 2 threshold, 3 coupling/flow object, 4 sink}, `growth` (a
  list of tags, each with its own file+string evidence): `K` (the node's own definition grows with the number of RG
  steps K or with the level k), `T` (grows with the coarse side T or a volume), `Tk` (uniform only at fixed coarse
  side, where the relevant coarse side is a level-k side T_k = T·L^{K-1-k}, hence unbounded in K on a fixed torus),
  `Tfix` (proven only at fixed final side T), `unstated-K`, `unstated-T` (uniformity asserted by a target or needed by a
  consumer, but no source proves it).
- Edge record: `src`, `dst`, `kind`, `file`, `string`. Direction **src → dst = "src must be fixed before dst"**
  (dst is defined from src, or dst is constrained by an inequality involving src, or the source text orders them).
  `kind` ∈ {def, le, order, req, implicit, fixedpoint}:
  def = dst is defined from src; le = an inequality "dst ≤ f(src, …)" or "dst ≥ f(src, …)"; order = an explicit order
  statement in the source; req = dst's statement needs src as a hypothesis; implicit = dst depends on src only through
  a law, family or definition whose uniformity in src is not stated (e.g. a hypothesis quantified over laws that are
  themselves indexed by src); fixedpoint = the dependence is a fixed-point condition on a sequence, not a choice of a
  constant. An edge may carry `absorbs: True` when the cited text shows that a growth of src does NOT propagate to
  dst (e.g. a level-count factor beaten by the running of the coupling); the absorbing string is then required.

## What the checker computes, and the verdict rules (pre-registered)
A. **Schema (S).** Every edge endpoint is a node id; every node and edge has non-empty `file` and `string`; ids unique;
   kinds and tags in the allowed sets; every `absorbs` edge has its own string. S PASS iff all hold. If S FAILs on the
   real graph, no other verdict is reported for that graph.
B. **Cycles (DAG-F1).** Tarjan strongly-connected components, run twice: (B-all) on all edges; (B-strict) on all edges
   except kinds `implicit` and `fixedpoint`. Every SCC with ≥ 2 nodes, and every self-loop, is reported with one
   explicit cycle through it (node list and, for each edge on it, kind + file + string). DAG-F1 is **FOUND** iff B-all
   has a nontrivial SCC; it is reported separately whether B-strict also has one (a cycle made only of def/le/order/req
   edges is a cycle in the written hierarchy; one that needs an implicit or fixedpoint edge is a cycle through an
   unstated quantifier or a fixed point, and is labelled so).
C. **Growth (DAG-F2).** Seeds = nodes with a `K`, `T` or `Tk` tag. Propagate src → dst along every edge not marked
   `absorbs`. Separately propagate `Tfix`, `unstated-K`, `unstated-T` as "uniformity not established" taints. Report:
   every seed with its evidence; every tainted node with one shortest witness path from a seed; and, explicitly, whether
   each tier-4 sink is tainted. DAG-F2 is **FOUND** iff at least one seed exists on a node whose `live` is `live`.
D. **Order.** Kahn's algorithm on the condensation (each SCC one super-node), deterministic tie-break by (tier, id).
   The order is reported for the live subgraph and for the full graph. Validity is re-checked independently: for every
   edge src → dst in the acyclic part, position(src) < position(dst). An invalid order is a checker FAIL.
E. **Counts.** Nodes by `live`, edges by kind, unplaced (DAG-F3) nodes listed with their candidate sites.

## Controls (each must behave as designed, or the checker is declared UNABLE TO DECIDE)
- **C1 (designed FAIL, cycle).** Copy the real graph and add one back-edge from the sink to a tier-2 threshold that the
  sink depends on (sink → that threshold). B-all and B-strict MUST report a nontrivial SCC containing both endpoints of
  the injected edge, and an explicit cycle that uses the injected edge. Fires = reported.
- **C2 (designed FAIL, growth).** Copy the real graph and tag one tier-0 source that has a directed path to the sink
  with `K` (evidence "INJECTED"). The sink MUST be reported tainted, with a witness path starting at that source.
- **C3 (designed FAIL, schema).** Copy the real graph and add an edge to a non-existent id. S MUST FAIL.
- **C4 (null control).** A hand-made 6-node acyclic graph (written in the script, with its unique valid order stated in
  advance): no SCC reported; the order produced equals the stated one.
- **C5 (positive control).** A hand-made graph with exactly one 3-cycle a → b → c → a plus a tail: exactly one
  nontrivial SCC {a, b, c} reported.
- **C6 (absorb control).** A hand-made chain s → x → y with s tagged `K` and x → y marked `absorbs`: x tainted, y NOT
  tainted.

## What a PASS does not mean
The checker decides only properties of the graph as encoded. It cannot decide that an edge was read correctly from its
source: that is checked by re-reading each edge's string (SMALLNESS_DAG.md records the re-read). A "no cycle" result is
a statement about the encoded edges; an edge I failed to encode is invisible to it. The DAG-F3 list (symbols I could not
place) is the explicit boundary of what was encoded.

## ADDENDUM A (appended 2026-10-28, before the graph data file and before the checker exist; `ls checks/dag55_*` at the
## moment of appending lists only this criteria file)
- **S2 (string audit, verdict-bearing).** For every node and every edge, the `string` must occur verbatim (exact substring,
  after reading the file as UTF-8) in `file`, where `file` is a path relative to the lane directory
  `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/` (the existence lane is reached as `../ym4d-existence/EXISTENCE.md`).
  A record may carry `string2` (a second locating string, also required to occur, possibly in `file2`). S2 PASS iff every
  string is found. Each miss is listed (record id, file, string). If S2 FAILs on the real graph, the misses are corrected in the
  graph data under a NEW id (dag55_2 …), never by editing dag55_1's files after the run.
- **C7 (designed FAIL, string audit).** Copy the real graph and replace one edge's string by a string that occurs in no lane
  file (fixed in the script: "ZZZ-NOT-IN-ANY-FILE-dag55"). S2 MUST FAIL on exactly that record.
- Volume field: nodes may carry an informational `vol` string (how the source states the node's volume behaviour). It is
  printed as a table; it carries no verdict beyond the `growth` tags of C.
