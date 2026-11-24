lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-25T02:37Z

# gap-k2-end-class-fable (row 1471): the end class (END-K2) with numbers

Started 2026-11-24T14:37Z (date -u), Mac mini worker 1, Claude Fable 5.2 medium, pinned at bf0e5e0ec.
Status of this file: IN PROGRESS. Nothing below is checked by a second party.

## 0. Plan (written first, per the save protocol)

Item: component C2 of the K-II tool of row 1468 (`library/gap-k2-tool-design-fable.md` sections 3-4, 7).
To prove, with numbers: explicit eps_E > 0 and v_E(m) = O(log m) such that every family realizing a local
rule of norm at most eps_E (weighted norm of 4.2 at x of order one, or a justified variant) on the sixteen
twisted tori of spatial side m and time sides v, 2v, v >= v_E(m), wrap error <= 1/100, has purity >= 457/625.
Also the entry: largest beta_E such that Wilson at beta_E after one Q2 step of stated strength is in the class.

Steps (each appended here before the next starts):
1. Read row 1468 sections 3-4, 7 (statement, norm 4.2, Fact PUR, map Q2). Record exact statements used.
2. Read Theorem E (row 1354), Theorem END-D (row 1353), Theorem BS (row 1340): what they prove, with which
   norm (supremum bounds), and what ports.
3. Compare the weighted norm of 4.2 with the supremum bounds those theorems use; find the first failure or
   show the port goes through.
4. Prove (END-K2) with explicit constants, or repair the norm and prove the repaired statement.
5. Entry: beta_E and the Q2 strength.
6. Count of certified entry steps from beta about 2.3 to beta_E; next two rows with decisive outcomes.

Marks used below: [PROVED] = full argument written here or cited to a row with its location;
[SKETCHED] = argument outlined, a named step not written; [GUESSED] = no argument.
