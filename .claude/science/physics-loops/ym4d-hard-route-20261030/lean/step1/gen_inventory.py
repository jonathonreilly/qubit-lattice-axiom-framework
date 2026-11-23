#!/usr/bin/env python3
"""Generator for Inventory.lean (row 1428).  Usage: gen_inventory.py HEAD VALUES OUT
HEAD: the hand-written Lean prelude; VALUES: three lines of 64 integers (slot, even, hist values
as printed by Lean's #eval, used only as the right-hand sides the kernel then checks)."""
import sys
head, values, out = sys.argv[1:4]
import re
vals = [[int(x) for x in re.findall(r'\d+', b)] for b in re.findall(r'\[[^\]]*\]', open(values).read())]
assert len(vals) == 3 and all(len(v) == 64 for v in vals)
first6 = [8**0 + 8**(t+2) for t in range(6)]
starts = [0]
for c in first6:
    starts = starts + [d + c for d in starts]
L = lambda xs: '[' + ', '.join(map(str, xs)) + ']'
fam = [('slot', '(wt 8)', vals[0]), ('even', '(evenAll 8)', vals[1]), ('hist', 'histLeaf', vals[2])]
s = open(head).read()
s += r'''
/-! ### The step list as a literal, and its first block -/

def stepsLit : List Step :=
  [.corner 65, .corner 513, .corner 4097, .corner 32769, .corner 262145, .corner 2097153, .check 0,
   .corner 72, .corner 520, .corner 4104, .corner 32776, .corner 262152, .corner 2097160, .check 1,
   .corner 4160, .corner 32832, .corner 262208, .corner 2097216, .check 2,
   .corner 4608, .corner 33280, .corner 262656, .corner 2097664, .check 3,
   .corner 266240, .corner 2101248, .check 4,
   .corner 294912, .corner 2129920, .check 5, .check 6, .check 7]
theorem steps_eq : steps 8 = stepsLit := by decide

/-- The six corners at node 0 (to nodes 2..7). -/
def first6 : List Nat := [65, 513, 4097, 32769, 262145, 2097153]
def restLit : List Step := stepsLit.drop 6
theorem stepsLit_split : stepsLit = first6.map Step.corner ++ restLit := by decide

/-- Degree vector of the pattern `m` at node 0: bit `t` of `m` is the corner to node `t + 2`. -/
def node0Const : Nat → Nat → Nat
  | 0, _ => 0
  | t + 1, m => (if (m / 2 ^ t) % 2 = 1 then 8 ^ 0 + 8 ^ (t + 2) else 0) + node0Const t m

def starts : List Nat :=
  ''' + L(starts) + r'''
theorem starts_eq : expand first6 [0] = starts := by decide
theorem starts_eq_masks : starts = (List.range 64).map (node0Const 6) := by decide

/-- Leaf for the histogram: the product of `w` over the nodes other than node 0. -/
def histLeaf (d : Nat) : Nat := wt 7 (d / 8)

/-! ### The 3 x 64 pieces, each its own kernel evaluation (generated) -/

'''
for name, leaf, v in fam:
    for k in range(64):
        s += f'theorem {name}_{k} : prunedS {leaf} restLit {starts[k]} = {v[k]} := by decide +kernel\n'
    s += f'\ndef {name}Vals : List Nat :=\n  {L(v)}\n'
    s += f'theorem {name}_pieces : starts.map (pruned {leaf} restLit) = {name}Vals :=\n'
    for k in range(64):
        s += f'  map_cons_eq ((prunedS_eq _ _ _).symm.trans {name}_{k}) <|\n'
    s += '  rfl\n\n'
s += r'''/-! ### Totals -/

theorem split0 (leaf : Nat → Nat) (rest : List Step) (cs : List Nat) :
    pruned leaf (cs.map Step.corner ++ rest) 0 = ((expand cs [0]).map (pruned leaf rest)).sum := by
  have h := split leaf rest cs [0]
  have e : ([0].map (pruned leaf (cs.map Step.corner ++ rest))).sum
      = pruned leaf (cs.map Step.corner ++ rest) 0 + 0 := rfl
  rw [← h, e, Nat.add_zero]

theorem total_of_pieces (leaf : Nat → Nat) (vals : List Nat)
    (h : starts.map (pruned leaf restLit) = vals) : pruned leaf (steps 8) 0 = vals.sum :=
  calc pruned leaf (steps 8) 0
      = pruned leaf (first6.map Step.corner ++ restLit) 0 := by rw [steps_eq, stepsLit_split]
    _ = ((expand first6 [0]).map (pruned leaf restLit)).sum := split0 leaf restLit first6
    _ = (starts.map (pruned leaf restLit)).sum := by rw [starts_eq]
    _ = vals.sum := by rw [h]

/-- Number of even subgraphs of K_{2,2,2,2}: `2^(24-8+1)`. -/
theorem even_subgraphs : pruned (evenAll 8) (steps 8) 0 = 131072 := by
  rw [total_of_pieces _ _ even_pieces]; decide
/-- The structurally admissible slots of the half-spin site tensor (row 1418). -/
theorem slots : pruned (wt 8) (steps 8) 0 = 12910079 := by
  rw [total_of_pieces _ _ slot_pieces]; decide
theorem slot_bytes : 12910079 * 32 = 413122528 := by decide

/-! ### Histogram by the pattern at node 0 (row 1418; check 1420) -/

/-- Are the two nodes of a two-bit mask antipodal? -/
def sameAxisPair (m : Nat) : Bool := m == 3 || m == 12 || m == 48

def expected (m : Nat) : Nat :=
  match popc 6 m with
  | 0 => 50920
  | 2 => if sameAxisPair m then 114551 else 115144
  | 4 => if sameAxisPair (63 - m) then 262978 else 265805
  | 6 => 635318
  | _ => 0

/-- For every pattern `m` at node 0: the sum over even subgraphs with that pattern of the
product of `w` over the other seven nodes. -/
theorem histogram :
    ((List.range 64).map (node0Const 6)).map (pruned histLeaf restLit) = (List.range 64).map expected := by
  rw [← starts_eq_masks, hist_pieces]; decide

/-- Number of fixed-leg labels in each of the six classes. -/
def classLabels (v : Nat) : Nat :=
  ((List.range 64).map fun m => if expected m = v then w (popc 6 m) else 0).sum

theorem histogram_labels :
    [50920, 114551, 115144, 262978, 265805, 635318].map classLabels = [1, 3, 12, 6, 24, 5] := by
  decide +kernel
theorem first_moment :
    ((List.range 64).map fun m => w (popc 6 m) * expected m).sum = 12910079 := by decide +kernel
theorem second_moment :
    ((List.range 64).map fun m => w (popc 6 m) * expected m * expected m).sum = 4329800859159 := by
  decide +kernel

end Step1

'''
for t in ['singlet_table','w_is_singlet','link_counts','link_total_by_occupancy','link_total_by_patterns',
          'div_mul_sanity','D_one','D_two','corners_card','corners_degree_six','prunedS_eq',
          'octahedron_even','octahedron_even_pruned','octahedron_slots_agree','split','steps_eq',
          'stepsLit_split','starts_eq','starts_eq_masks','slot_pieces','even_pieces','hist_pieces',
          'split0','total_of_pieces','even_subgraphs','slots','slot_bytes','histogram','histogram_labels','first_moment','second_moment']:
    s += f'#print axioms Step1.{t}\n'
open(out, 'w').write(s)
