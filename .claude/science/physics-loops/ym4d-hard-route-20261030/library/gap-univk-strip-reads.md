lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-23T12:06Z

# Row 1417, gap-univk-strip-reads: the moving-read comparison of one complete native pair

Written by Claude Fable 5.2 (medium), Mac mini worker 2, at commit 5ae9c78c6. Started 2026-11-23T00:06Z (date -u).
Not checked by another model. Research-stage working state; no status.

Credit. The objects compared here (the kept strip matrix, its boundary and determinant factors, the glued restoring
operator, the pivots, the chart densities, the counting by uses) are constructions of Ethan Sussman and Levent Alpoge
(with Claude and Codex as authors of their text): YM4_1400.tex (cited "Y line"), the complete account part III (cited
"III line"), and the short outline (cited "O line"), all at revision 31a47c543775 (Y at 2bc0658f91d2). The background
structure is Balaban's. Rows 1404, 1406, 1410 and checks 1405, 1408, 1415 of this folder are the consumer and the
prior readings.

## 0. Plan (written before any reading; revised below as steps finish)

Problem (queue row 1417). One complete native pair of reads of a good aligned live label: its owning action and
counterterm, its original strip mask, tree and chart, its normalization. Compare, at the two real reads:

- U1. the kept strip matrix and its filed boundary and determinant factors (Y 76507-76554, 77278-77296);
- U2. the glued restoring operator;
- U3. the pivots and chart densities (Y 75023-75117, 76086-76105);
- U4. the Wilson background at fixed coefficient.

Decide: does the total change of these uses cost the shifted site load C (k-b+1)(l_b + l_(b-1)) per cell, in the
counting by uses of III 11963-11993 and Y 129399-129629 (each use once; a stored output is compared as a value or
expanded, never both)? If a use does not fit: name it, give its actual size, say whether it is a live factor beyond
the printed bounds. Not to redo: the ordinary stored strip coefficient (check 1415); CV, PD-REST, ZONE-FORM,
ZONE-RESERVE, ZONE-CAPACITY.

Steps, one per response, each appended here before the next:

1. Repo search and prior rows: row 1410, check 1415 in full; rows 1404, 1406, checks 1405, 1408 for the consumer.
2. Source read A: the owning action and counterterm (Y 61913-61932; O 6331-6356); fix the reading.
3. Source read B: the strip matrix and its factors (Y 76507-76554, 77278-77296).
4. Source read C: pivots, chart densities, restoring operator (Y 75023-75117, 76086-76105).
5. Source read D: the counting by uses (III 11963-11993; Y 129399-129629) and the per-cell domination (III 13337-13393).
6. The comparison: a list of uses, each with its change between the two reads and its charge.
7. Verdict per use; the first use that does not fit, with its size; next two rows.

## 1. Repo search and prior rows (written 2026-11-23, step 1)

Read in full: row 1410 (`library/gap-univk-native-ends.md`) and check 1415
(`library/gap-univk-native-ends-check-astra62.md`). Rows 1404, 1406 and checks 1405, 1408 were read through the
digest in row 1410 Section 1 and the citations of check 1415; I did not re-read them line by line.

What binds this row (from check 1415):
- (W3) of row 1410 fails. The counting rule is by uses: III 11963-11993 gives each slot one class (anchor zone j,
  read level k'); Y 129399-129424 recurses only on a child's empty-switch value; Y 129603-129629 replaces the raw
  brackets by the localized remainder. A stored output is compared as a value, or expanded into inputs and reads.
- The ordinary strip coefficient is paid: abs(A'(b)) <= C p_0(g_j) on the kept tests (O 17558, Y 63252) and
  norm(K_j^keep) <= C_w (Y 76514-76521) give (1/2) abs(delta tau_j) abs(<A', K A'>) <= C' d_j gfrak_j z_j.
- Open after check 1415: the fixed-coefficient change of each operator, chart factor and scalar between the two
  real reads (its D10, the field part of D8, D11 beyond the fixed matrix, D13 beyond the matched pivot, D5, D7), and
  the outer carrying action on its remaining plaquettes with its counter-insertions.

Repo search. `library/open-core.md` (one grep): no hit for "strip matrix", "restoring operator", "kept chain",
"operator entr", "moving read", RD-BG, strip-reads. FINISH rows that name this comparison: 1404 to 1410, 1415 and this
row. Owners used and not redone: CV, PD-REST (`library/open-registry.md` L19, L418), ZONE-FORM, ZONE-RESERVE,
ZONE-CAPACITY (L543-545, owner `b4-typed`, all open).

## 2. Sources read (appended as read)

- Y 61895-61940 (terminal exponent -A(x_k(.),U) + E_k + R_k + B_k - E_(k,S); the two sequences of a label).
- III 11805-11830, 11955-12060 (the pair of runs; "one assembly formula P_h, carrying no run index, applied to the
  array x^c of the run's stored numbers"; uses, classes, marks; the loads [[delta]]^u_j and [[delta]]^c_j).
- Y 129395-129760 (exponent of a nested history; arguments of the production formula; bounds on the class discs).
- Y 76495-76560, 77240-77300 (the complete kept quadratic; the parameter tube; the half-disc determinant).
- III 385-410, 13100-13135, 13330-13395, 17280-17300 (classical index rates; the read split G^(n) + G^rd + G^own;
  per-cell domination; the c-load envelope).
