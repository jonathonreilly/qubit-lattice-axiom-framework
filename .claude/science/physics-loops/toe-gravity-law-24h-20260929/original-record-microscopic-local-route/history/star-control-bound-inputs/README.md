# Exact inputs bound by the first executed control

CHECK_RESULTS.json records RUN_CONTRACT.md SHA ffa70aaab56dba424c0293be31f01fe7db38dbc37aa0a6e915255636f591944f and SOURCE_IDENTITIES.json SHA3e96de84fdcd01262fb90e1b1f98215421be9d4de85211f74d9ae6f620b51d81. The current versions later gained the two further control contracts, one additional source identity, the independent receipt and a remote-main reconfirmation.

At final packaging these original bytes were reconstructed by removing only those appendages; both SHA256 values were checked exactly against the ORIGINAL executed CHECK_RESULTS.json before the historical copies were written. The runner and CONTRACT hashes still match their original result bindings. The original result was not rewritten to pretend it ran against the later expanded metadata. This directory preserves the exact historical bound bytes and the reconstruction provenance.
