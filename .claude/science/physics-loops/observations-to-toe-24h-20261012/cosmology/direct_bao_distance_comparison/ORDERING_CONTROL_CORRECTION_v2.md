# Version2 primary ordering controls

The independent review executed an actual copied-source mutation swapping
only the last two parsed quantity labels. The original1676assertions all
passed while the reference quadratic changed from10.357 to about37855.5.
The original code reads the correct DH,DM order; this is a demonstrated
coverage gap. Preserve the original run and successful-but-wrong mutant.

Version2 reconstructs the actual full parsed redshift/value/type vector from
seven separately released tracer files. It independently parses their tokens,
then binds every actual combined-array entry. It reconstructs the block
covariance and checks every entry after the combined file's declared printed
precision (eight digits after the decimal in scientific notation). Nothing
is refitted; release covariance entries, shapes, normalization and scores are
unchanged. This supplements source hashes with an ordering-sensitive physical
input check. Run the same actual label swap with freshly correct hashes.
