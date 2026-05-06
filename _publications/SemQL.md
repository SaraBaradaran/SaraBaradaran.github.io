---
title: "LLM-Integrated Declarative Program Analysis"
collection: publications
excerpt: 'We introduce SemQL, a query language that enhances traditional program analysis tool CodeQL with an oracle invocation construct, which allows the analyzer to call external oracles like LLMs to handle tasks requiring semantic reasoning beyond syntax. While existing program analysis tools excel at analyzing code structure, they struggle with analyses requiring semantic/subjective judgments, e.g., detecting string literals in code which expose sensitive information. SemQL bridges this gap by allowing queries to combine structural analysis with LLM-based judgments. We also propose an efficient query evaluation method that reduces the cost of using the LLM, and demonstrate the system usefulness on real-world code analysis problems.'
date: 2026-12-13
author: 'Sara Baradaran, Amirmohammad Nazari, and Mukund Raghothaman'
venue: 'PLDI Workshop on the State Of the Art in Program Analysis (SOAP)'
image: 'https://raw.githubusercontent.com/SaraBaradaran/SaraBaradaran.github.io/master/papers/SemQL.png'
citation: 'https://raw.githack.com/SaraBaradaran/SaraBaradaran.github.io/master/papers/SemQL.bib'
paperurl: 'https://raw.githack.com/SaraBaradaran/SaraBaradaran.github.io/master/papers/SemQL.pdf'
code: 'https://github.com/SaraBaradaran/SemQL'
---
