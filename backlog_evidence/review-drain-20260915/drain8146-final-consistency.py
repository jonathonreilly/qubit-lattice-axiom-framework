exec(open('/private/tmp/review-drain-20260915/drain8146-repair-followup.py').read().split("s=(W/notes[8139]).read_text()")[0])
s=(W/notes[8138]).read_text();s=s.replace('term that couples the three sites behind a site all at once, not just in\npairs. Unlike the plane, this law remembers where the block began: if you\nstrip off the first layer, what remains is not the law of the smaller block.','three-neighbor normalizer. Its irreducible three-body component and the failure\nof first-layer stripping are witnessed at `(3,1,2)` and `(5,2,4)`; neither is\nasserted at every nonconstant triple.')
s=s.replace('So the pattern law of the whole lattice cannot be built by fitting blocks\ntogether; it is built by letting the first layer recede to infinity.','The constructed infinite law uses the limit as the first layer recedes to infinity.')
s=s.replace('Imports; every one is re-proved at the scope used, and no value or theorem is\nimported as authority.','Imports. The contraction and coupling arguments are proved here; the\ncountable extension and compactness results are explicit mathematical imports.')
s=s.replace('positive-chain contraction are classical references re-proved here at the scope used; no\nvalue, constant or theorem is imported as authority.','positive-chain contraction have the scoped proofs above; the probability theorems listed under Imports are mathematical inputs, not physical premises.')
s=s.replace('Q1 is proved for every box and every positive symmetric rule','Q1 factorization is proved for every box and every positive symmetric rule; Q1f irreducibility requires nonzero third difference')
s=s.replace('bulk is a nearest-neighbor pair term `−log K` plus a genuine three-body term','bulk at these witnessed triples is a nearest-neighbor pair term `−log K` plus a genuine three-body term')
(W/notes[8138]).write_text(s)
s=(W/notes[8139]).read_text();s=s.replace('# The three-dimensional formation law is a Markov field for the face-diagonal graph, not the nearest-neighbor one: eight distinct corner laws and the imprint of the sweep','# The three-dimensional formation law: the face-diagonal specification and eight distinct corner laws at the witnessed triple')
s=s.replace('uniqueness of conditional probabilities, ergodic decomposition — are named here\nand under Imports and re-proved at scope where load-bearing.','uniqueness of conditional probabilities and of finite measures — are explicit\nmathematical imports under Imports; ergodic decomposition is not used.')
s=s.replace('grouping into triples (R3a), so there are eight.','grouping into triples (R3a); at `(3,1,2)` the independent conditional witness\nthen proves eight distinct laws. Different groupings alone do not prove distinctness.')
s=s.replace('| R3: eight distinct laws; the covariant orbit; the mixture | proved (dependency sets; transitivity); within-pair witness executed (C1–C4) |','| R3: covariant orbit and probability mixture; eight distinct laws at (3,1,2) | covariance general in the region; distinctness uses the within-pair witness (C1–C4) |')
s=s.replace('the count `2` versus `8` explained','the count comparison is restricted to the witnessed setting')
s=s.replace('the formation law of the monotone class on Z^3 is now separated from every static law by its Markov graph','the stated nonzero-difference cases are separated from static laws by their conditional specification')
(W/notes[8139]).write_text(s)
# Canonical source names and links for the within-unit premise authority.
for pr,path in notes.items():
 p=W/path;s=p.read_text();links='\n### Linked source authority\n\n'
 for other,op in notes.items():
  if other!=pr and ('block '+{8138:'08',8139:'09',8141:'10',8142:'11',8146:'12'}[other] in s.lower()):
   links+='- ['+Path(op).stem.replace('_',' ').title()+']('+Path(op).name+'): only its explicit hypotheses and conclusions are used.\n'
 s=s.replace('## Prior art and what is new',links+'\n## Prior art and what is new')
 p.write_text(s)
print('consistency edits saved')
