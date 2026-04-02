---
title: "Reusing Legacy Code in Wasm: Key Challenges of Compilation and Code Semantics Preservation"
collection: publications
excerpt: 'WebAssembly (Wasm) is a binary format designed for executing performance-critical code in web browsers. A key objective of Wasm is to facilitate the integration of legacy codebases and libraries into web applications without requiring developers to rewrite them in JavaScript from scratch. In practice, however, this objective is constrained by limitations in currently available WebAssembly compilers.
In this paper, we investigate (1) the challenges that arise when cross-compiling high-level language codebases to WebAssembly, and (2) the extent to which WebAssembly compilers faithfully preserve program semantics in the resulting binaries. We also present WasmChecker, a differential testing framework for checking semantic equivalence between x86-64 binaries of C/C++ programs and their corresponding Wasm counterparts.'
date: 2026-10-10
venue: 'IEEE International Conference on Software Analysis, Evolution and Reengineering (SANER)'
image: 'https://raw.githubusercontent.com/SaraBaradaran/SaraBaradaran.github.io/master/papers/WasmChecker.png'
citation: 'https://raw.githack.com/SaraBaradaran/SaraBaradaran.github.io/master/papers/WasmChecker.bib'
paperurl: 'https://raw.githack.com/SaraBaradaran/SaraBaradaran.github.io/master/papers/WasmChecker.pdf'
code: 'https://github.com/SaraBaradaran/WasmChecker'
---
