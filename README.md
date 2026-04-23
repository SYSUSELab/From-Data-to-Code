# Bridging Generation and Training: A Systematic Review of Quality Issues in LLMs for Code

<div align="center">
  <h3>🚀 <a href="https://kaifeng-he.github.io/From-Data-to-Code/">View the Academic Website</a></h3>
</div>

<br>

## 📖 Abstract

Large language models (LLMs) frequently generate defective outputs in code generation tasks, ranging from logical bugs to security vulnerabilities. While these generation failures are often treated as model-level limitations, empirical evidence increasingly traces their root causes to imperfections within the training corpora. Yet, the specific mechanisms linking training data quality issues to generated code quality issues remain largely unmapped. This paper presents a systematic literature review of 114 primary studies to investigate how training data quality issues propagate into code generation. We establish a unified taxonomy that categorizes generated code quality issues across nine dimensions and training data quality issues into code and non-code attributes. Based on this taxonomy, we formalize a causal framework detailing 18 typical propagation mapping mechanisms. Furthermore, we synthesize state-of-the-art detection and mitigation techniques across the data, model, and generation lifecycles. The reviewed literature reveals a clear methodological shift: quality assurance is transitioning from reactive, heuristic-based post-generation filtering toward proactive, data-centric governance and closed-loop repair. Finally, we identify open challenges and outline research directions for developing reliable LLMs for code through integrated data curation and continuous evaluation. 

<div align="center">
  <img src="images/paper_collection.png" alt="Overview of the process of paper collection and filtering" width="80%">
  <p><em>Fig. 1. Overview of the paper collection and filtering process.</em></p>
</div>
<br><br>
<div align="center">
  <img src="images/lifecycle.png" alt="Lifecycle of Detection and Governance" width="80%">
  <p><em>Fig. 2. Conceptual Framework of Quality Issues and Mitigation in the LLM Lifecycle.</em></p>
</div>

---

## 📢 News

- **[2026-04]** 🚀 The `From-Data-to-Code` repository is officially launched.

---

## 📑 Table of Contents

- [Bridging Generation and Training: A Systematic Review of Quality Issues in LLMs for Code](#bridging-generation-and-training-a-systematic-review-of-quality-issues-in-llms-for-code)
  - [📖 Abstract](#-abstract)
  - [📢 News](#-news)
  - [📑 Table of Contents](#-table-of-contents)
  - [📚 Findings](#-findings)
    - [💻 RQ1: Generated Code Quality Issues](#-rq1-generated-code-quality-issues)
    - [📊 RQ2: Training Data Quality Issues](#-rq2-training-data-quality-issues)
    - [🔗 RQ3: Mapping: Data to Code](#-rq3-mapping-data-to-code)
    - [🔍 RQ4: Detection Methods](#-rq4-detection-methods)
      - [1. Code-Level Detection](#1-code-level-detection)
      - [2. Data-Level Detection](#2-data-level-detection)
    - [🛠️ RQ5: Governance Strategies](#️-rq5-governance-strategies)
      - [1. Code-Level Mitigation](#1-code-level-mitigation)
      - [2. Data-Level Mitigation](#2-data-level-mitigation)
  - [🤝 Contribution](#-contribution)

---

## 📚 Findings



### 💻 RQ1: Generated Code Quality Issues

We discard vague concepts like generic "code hallucination" and establish a unified taxonomy encompassing **9 core dimensions** of quality issues in LLM-generated code:

1. **Correctness**: Functional accuracy and executability, categorized into syntax errors, logical flaws, and API misuse.
2. **Security**: Resilience against malicious exploitation, categorized into inherent design flaws and external vulnerabilities.
3. **Compliance**: Adherence to legal, ethical, and safety standards, categorized into copyright infringement, privacy leakage, and malicious code generation.
4. **Robustness**: Ability to handle abnormal inputs gracefully, manifesting as inadequate error handling and boundary condition failures.
5. **Maintainability**: Ease of long-term code modification, categorized into disorganized structure and low reusability.
6. **Understandability**: Human-readability and clarity, manifesting as poor naming conventions and lack of documentation.
7. **Efficiency**: Optimal system resource utilization, categorized into suboptimal time complexity and improper memory management.
8. **Parsimony of Output**: Conciseness of generated results, manifesting as redundant logic, useless loops, and extreme verbosity.
9. **Miscellaneous**: Anomalies outside the core eight dimensions, primarily manifesting as instruction-following failures.


<br>

<div align="center">
  <img src="images/generated_code_issues.png" alt="Taxonomy of Generated Code Quality Issues" width="100%">
  <p><em>Fig. 3. Taxonomy of Generated Code Quality Issues</em></p>
</div>

**📄 Papers Referenced in this Section:**

1. LLMs Meet Library Evolution [2024-06] [[paper](https://arxiv.org/abs/2406.09834)]
2. Copilot Security [2022-04] [[paper](https://arxiv.org/abs/2204.04741)]
3. Copilot Evaluation [2025-01] [[paper](https://doi.org/10.1145/3524842.3528470)]
4. HalluCode [2024-04] [[paper](https://arxiv.org/abs/2404.00971)]
5. CodeHalu [2024-05] [[paper](https://arxiv.org/abs/2405.00253)]
6. EffiBench [2024-02] [[paper](https://arxiv.org/abs/2402.02037)]
7. Mercury [2024-02] [[paper](https://arxiv.org/abs/2402.07844)]
8. SStuBs [2023-03] [[paper](https://arxiv.org/abs/2303.11455)]
9. package hallucinations [2024-06] [[paper](https://arxiv.org/abs/2406.10279)]
10. HallTrigger [2024-07] [[paper](https://arxiv.org/abs/2407.04831)]
11. Large Language Models for Code [2023-02] [[paper](https://arxiv.org/abs/2302.05319)]
12. Purple Llama CYBERSECEVAL [2023-12] [[paper](https://arxiv.org/abs/2312.04724)]
13. Lost at C [2022-08] [[paper](https://arxiv.org/abs/2208.09727)]
14. AI Assistants Security [2022-11] [[paper](https://arxiv.org/abs/2211.03622)]
15. The Counterfeit Conundrum [2024-02] [[paper](https://arxiv.org/abs/2402.19475)]
16. Bugs in LLM-generated Code [2024-03] [[paper](https://arxiv.org/abs/2403.08937)]
17. GitHub Copilot, Amazon CodeWhisperer, ChatGPT [2023-04] [[paper](https://arxiv.org/abs/2304.10778)]
18. ChatGPT Code Quality [2023-08] [[paper](https://arxiv.org/abs/2308.04838)]
19. CloudAPIBench [2024-07] [[paper](https://arxiv.org/abs/2407.09726)]
20. CodeMirage [2024-08] [[paper](https://arxiv.org/abs/2408.08333)]
21. LLM-generated Code Efficiency [2024-04] [[paper](https://arxiv.org/abs/2404.06041)]
22. AutoAPIEval [2024-09] [[paper](https://arxiv.org/abs/2409.15228)]
23. DeSec [2024-10] [[paper](https://arxiv.org/abs/2410.08858)]
24. When Fine-Tuning LLMs Meets Data Privacy [2024-12] [[paper](https://arxiv.org/abs/2412.01072)]
25. Bias Unveiled [2024-11] [[paper](https://arxiv.org/abs/2411.10351)]
26. FairCoder [2025-01] [[paper](https://arxiv.org/abs/2501.05396)]
27. CodeIP [2024-04] [[paper](https://arxiv.org/abs/2404.15639)]
28. From Effectiveness to Efficiency [2024-06] [[paper](https://arxiv.org/abs/2406.00602)]
29. ENAMEL [2024-06] [[paper](https://arxiv.org/abs/2406.06647)]
30. DeVAIC [2024-04] [[paper](https://arxiv.org/abs/2404.07548)]
31. PTMs [2024-11] [[paper](https://arxiv.org/abs/2411.10565)]
32. Software Librarian [2024-08] [[paper](https://arxiv.org/abs/2408.05128)]
33. Codequal Analyzer [2025-06] [[paper](https://arxiv.org/abs/2506.02211)]
34. Artificial-Intelligence Generated Code Considered Harmful [2024-09] [[paper](https://arxiv.org/abs/2409.19182)]
35. Unveiling Inefficiencies in LLM-Generated Code [2025-03] [[paper](https://arxiv.org/abs/2503.06327)]
36. Python Tests Quality [2025-06] [[paper](https://arxiv.org/abs/2506.14297)]
37. CoQuIR [2025-06] [[paper](https://arxiv.org/abs/2506.11066)]
38. REAL [2025-05] [[paper](https://arxiv.org/abs/2505.22704)]
39. CIDRe [2025-05] [[paper](https://arxiv.org/abs/2505.19757)]
40. Infinite-Instruct [2025-05] [[paper](https://arxiv.org/abs/2505.23177)]
41. Quality In, Quality Out [2025-03] [[paper](https://arxiv.org/abs/2503.11402)]
42. Security and Quality in LLM-Generated Code [2025-02] [[paper](https://arxiv.org/abs/2502.01853)]
43. SwallowCode [2025-05] [[paper](https://arxiv.org/abs/2505.02881)]
44. ROSE [2025-07] [[paper](https://arxiv.org/abs/2507.12561)]
45. Refining ChatGPT-Generated Code [2023-07] [[paper](https://arxiv.org/abs/2307.12596)]
46. ReCode [2025-06] [[paper](https://arxiv.org/abs/2506.20495)]
47. Seed-Coder [2025-06] [[paper](https://arxiv.org/abs/2506.03524)]
48. Data-efficient Fine-tuning [2025-04] [[paper](https://arxiv.org/abs/2504.12687)]
49. CRPE [2025-05] [[paper](https://arxiv.org/abs/2505.10594)]
50. DeepSeek-Coder [2024-01] [[paper](https://arxiv.org/abs/2401.14196)]
51. CodeSmellEval [2024-12] [[paper](https://arxiv.org/abs/2412.18989)]
52. RPG [2025-05] [[paper](https://arxiv.org/abs/2505.10402)]
53. Repetition In Repetition Out [2023-10] [[paper](https://arxiv.org/abs/2310.10226)]
54. Beyond Correctness [2024-07] [[paper](https://arxiv.org/abs/2407.11470)]
55. Generated Code Diversity [2024-08] [[paper](https://arxiv.org/abs/2408.14504)]
56. CodeMI [2024-04] [[paper](https://arxiv.org/abs/2404.14296)]
57. CodeCipher [2024-10] [[paper](https://arxiv.org/abs/2410.05797)]
58. Code Llama [2023-08] [[paper](https://arxiv.org/abs/2308.12950)]
59. Codex [2021-07] [[paper](https://arxiv.org/abs/2107.03374)]
60. Path Planning Evaluation [2025-04] [[paper](https://arxiv.org/abs/2504.21276)]
61. CODEJUDGE [2024-01] [[paper](https://aclanthology.org/2024.emnlp-main.1118.pdf?utm_source=chatgpt.com)]
62. Synthetic Data Generation [2025-01] [[paper](https://ieeexplore.ieee.org/document/11080380)]
63. Unseen Horizons [2025-04] [[paper](https://ieeexplore.ieee.org/document/11029836)]
64. Code Generation Survey [2024-08] [[paper](https://dl.acm.org/doi/10.1145/3747588)]
65. DataRecipe [2024-10] [[paper](https://dl.acm.org/doi/10.1145/3691620.3695593)]
66. aiXcoder-7B [2025-04] [[paper](https://ieeexplore.ieee.org/document/11121702)]
67. Imperfect Code Generation [2024-05] [[paper](https://ieeexplore.ieee.org/document/10554837)]
68. ClassEval [2024-6] [[paper](https://ieeexplore.ieee.org/document/10549472)]
69. UCD-Training [2026-02] [[paper](https://arxiv.org/abs/2602.20799)]
70. DRAINCODE [2026-01] [[paper](https://arxiv.org/abs/2601.20615)]
71. RealSec-Bench [2026-01] [[paper](https://arxiv.org/abs/2601.22706)]
72. ShortCoder [2026-01] [[paper](https://arxiv.org/abs/2601.09703)]
73. APIKG4SYN [2025-11] [[paper](https://arxiv.org/abs/2512.00380)]
74. MultiCodeIF [2025-07] [[paper](https://arxiv.org/abs/2507.00699)]
75. Beyond Functional Correctness [2024-06] [[paper](https://arxiv.org/abs/2407.00456)]
76. Adadec [2025-06] [[paper](https://arxiv.org/html/2506.08980v1)]
77. Code Copycat Conundrum [2025-04] [[paper](https://arxiv.org/abs/2504.12608)]
78. AllianceCoder [2025-03] [[paper](https://arxiv.org/abs/2503.20589)]
79. RustEvo^ 2 [2025-03] [[paper](https://arxiv.org/abs/2503.16922)]
80. RobGen [2025-03] [[paper](https://arxiv.org/abs/2503.20197)]
81. Llm Hallucinations in Practical Code Generation [2024-09] [[paper](https://arxiv.org/abs/2409.20550)]
82. COFFE [2025-02] [[paper](https://arxiv.org/abs/2502.02827)]
83. AATK Benchmark [2021-08] [[paper](https://dl.acm.org/doi/10.1145/3610721)]




### 📊 RQ2: Training Data Quality Issues

We categorize intrinsic flaws within pre-training and fine-tuning corpora into **two core dimensions**:

1. **Code Attribute Quality Issues**: Inherent defects within individual code samples that models explicitly learn, categorized into correctness, security, compliance, robustness, maintainability, understandability, and efficiency flaws.
2. **Non-Code Attribute Quality Issues**: Non-code textual noise and macro-level dataset flaws. Categorized into:
   - **Compliance and Security Risks (Textual)**: Hazards inherent in textual data, categorized into illegal/harmful, copyright-infringing, and privacy-leaking text.
   - **Distribution Imbalance Issues**: Skewed dataset proportions, manifesting as imbalances across programming languages, domains, data types, or difficulty levels.
   - **Redundancy Issues**: Excessive repetition, manifesting as duplicate samples or synthetic data degradation.
   - **Inadequate Diversity**: Insufficient coverage of real-world scenarios, manifesting as underrepresented edge cases or niche business logic.
   - **Data Contamination Risks**: Leakage of evaluation data, primarily manifesting as benchmark test sets embedded in training corpora.
   - **Low-Value Data**: Data contributing little or negatively to learning, categorized into meaningless text, format noise, low-information-density text, erroneous text, and incomplete data.

<br>

<div align="center">
  <img src="images/data_quality_issues.png" alt="Taxonomy of Dataset Quality Issues" width="100%">
  <p><em>Fig. 4. Taxonomy of Training Data Quality Issues</em></p>
</div>

**📄 Papers Referenced in this Section:**

1. LLMs Meet Library Evolution [2024-06] [[paper](https://arxiv.org/abs/2406.09834)]
2. Less is More [2025-02] [[paper](https://arxiv.org/abs/2502.14212)]
3. DataMan [2025-02] [[paper](https://arxiv.org/abs/2502.19363)]
4. Phi-4 [2024-12] [[paper](https://arxiv.org/abs/2412.08905)]
5. SStuBs [2023-03] [[paper](https://arxiv.org/abs/2303.11455)]
6. DeSec [2024-10] [[paper](https://arxiv.org/abs/2410.08858)]
7. CIDRe [2025-05] [[paper](https://arxiv.org/abs/2505.19757)]
8. Infinite-Instruct [2025-05] [[paper](https://arxiv.org/abs/2505.23177)]
9. Quality In, Quality Out [2025-03] [[paper](https://arxiv.org/abs/2503.11402)]
10. SwallowCode [2025-05] [[paper](https://arxiv.org/abs/2505.02881)]
11. Seed-Coder [2025-06] [[paper](https://arxiv.org/abs/2506.03524)]
12. CRPE [2025-05] [[paper](https://arxiv.org/abs/2505.10594)]
13. Code Pretraining [2024-09] [[paper](https://arxiv.org/abs/2409.04556)]
14. StarCoder 2 and The Stack v2 [2024-02] [[paper](https://arxiv.org/abs/2402.19173)]
15. Repetition In Repetition Out [2023-10] [[paper](https://arxiv.org/abs/2310.10226)]
16. Every Sample Matters [2025-03] [[paper](https://arxiv.org/abs/2503.17793)]
17. Code Data Training Stage [2023-09] [[paper](https://arxiv.org/abs/2309.16298)]
18. WaveCoder [2023-12] [[paper](https://arxiv.org/abs/2312.14187)]
19. Brevity is the soul of wit [2024-07] [[paper](https://arxiv.org/abs/2407.00434)]
20. Benchmark Builders [2025-04] [[paper](https://arxiv.org/abs/2504.19444)]
21. CodeMI [2024-04] [[paper](https://arxiv.org/abs/2404.14296)]
22. CodeCipher [2024-10] [[paper](https://arxiv.org/abs/2410.05797)]
23. Code Pre-training Impact [2024-08] [[paper](https://arxiv.org/abs/2408.10914)]
24. DataComp-LM [2024-06] [[paper](https://arxiv.org/abs/2406.11794)]
25. Logical Inference Pre-training [2024-10] [[paper](https://arxiv.org/abs/2410.06735)]
26. Code Llama [2023-08] [[paper](https://arxiv.org/abs/2308.12950)]
27. Codex [2021-07] [[paper](https://arxiv.org/abs/2107.03374)]
28. Path Planning Evaluation [2025-04] [[paper](https://arxiv.org/abs/2504.21276)]
29. Datasets for Large Language Models [2024-02] [[paper](https://arxiv.org/abs/2402.18041)]
30. Synthetic Data Generation [2025-01] [[paper](https://ieeexplore.ieee.org/document/11080380)]
31. Cracks in The Stack [2025-05] [[paper](https://ieeexplore.ieee.org/document/11028470)]
32. Unseen Horizons [2025-04] [[paper](https://ieeexplore.ieee.org/document/11029836)]
33. RTL-Breaker [2025-03] [[paper](https://ieeexplore.ieee.org/document/10993260)]
34. MG-Verilog [2024-06] [[paper](https://ieeexplore.ieee.org/document/10691738)]
35. Code Generation Survey [2024-08] [[paper](https://dl.acm.org/doi/10.1145/3747588)]
36. DataRecipe [2024-10] [[paper](https://dl.acm.org/doi/10.1145/3691620.3695593)]
37. Training Data Extraction [2025-08] [[paper](https://dl.acm.org/doi/10.1145/3709018.3736331)]
38. aiXcoder-7B [2025-04] [[paper](https://ieeexplore.ieee.org/document/11121702)]
39. Imperfect Code Generation [2024-05] [[paper](https://ieeexplore.ieee.org/document/10554837)]
40. LLM-ProS [2025-05] [[paper](https://ieeexplore.ieee.org/document/11028406)]
41. Uncovering Pretraining Code in LLMs [2025-11] [[paper](https://arxiv.org/abs/2511.07033)]
42. APIKG4SYN [2025-11] [[paper](https://arxiv.org/abs/2512.00380)]
43. MultiCodeIF [2025-07] [[paper](https://arxiv.org/abs/2507.00699)]
44. RustEvo^ 2 [2025-03] [[paper](https://arxiv.org/abs/2503.16922)]
45. AATK Benchmark [2021-08] [[paper](https://dl.acm.org/doi/10.1145/3610721)]

### 🔗 RQ3: Mapping: Data to Code

How do data defects cause code generation failures? We summarize **18 propagation mechanisms** bridging the gap between dataset flaws and generated code defects:

1. **Direct Mappings (10 types)**: The classic "garbage in, garbage out" replication. The model explicitly memorizes dataset flaws and replicates them.
2. **Indirect Mappings (8 types)**: Insidious propagation. Non-code defects do not inject explicit errors but disrupt the model's internal representations via mechanisms such as _entropy collapse_, _representation bias_, or _semantic drift_.

<br>

<div align="center">
  <img src="images/sankey.png" alt="Sankey Diagram of Mapping from Data Issues to Code Issues" width="100%">
  <p><em>Fig. 5. Mapping mechanisms from Training Data Issues to Generated Code Issues.</em></p>
</div>

**📄 Papers Referenced in this Section:**

1. LLMs Meet Library Evolution [2024-06] [[paper](https://arxiv.org/abs/2406.09834)]
2. SStuBs [2023-03] [[paper](https://arxiv.org/abs/2303.11455)]
3. AutoAPIEval [2024-09] [[paper](https://arxiv.org/abs/2409.15228)]
4. CodeIP [2024-04] [[paper](https://arxiv.org/abs/2404.15639)]
5. CIDRe [2025-05] [[paper](https://arxiv.org/abs/2505.19757)]
6. Infinite-Instruct [2025-05] [[paper](https://arxiv.org/abs/2505.23177)]
7. Quality In, Quality Out [2025-03] [[paper](https://arxiv.org/abs/2503.11402)]
8. SwallowCode [2025-05] [[paper](https://arxiv.org/abs/2505.02881)]
9. Refining ChatGPT-Generated Code [2023-07] [[paper](https://arxiv.org/abs/2307.12596)]
10. CRPE [2025-05] [[paper](https://arxiv.org/abs/2505.10594)]
11. StarCoder 2 and The Stack v2 [2024-02] [[paper](https://arxiv.org/abs/2402.19173)]
12. CodeSmellEval [2024-12] [[paper](https://arxiv.org/abs/2412.18989)]
13. RPG [2025-05] [[paper](https://arxiv.org/abs/2505.10402)]
14. Repetition In Repetition Out [2023-10] [[paper](https://arxiv.org/abs/2310.10226)]
15. CodeMI [2024-04] [[paper](https://arxiv.org/abs/2404.14296)]
16. CodeCipher [2024-10] [[paper](https://arxiv.org/abs/2410.05797)]
17. DataComp-LM [2024-06] [[paper](https://arxiv.org/abs/2406.11794)]
18. Code Llama [2023-08] [[paper](https://arxiv.org/abs/2308.12950)]
19. Path Planning Evaluation [2025-04] [[paper](https://arxiv.org/abs/2504.21276)]
20. Datasets for Large Language Models [2024-02] [[paper](https://arxiv.org/abs/2402.18041)]
21. Synthetic Data Generation [2025-01] [[paper](https://ieeexplore.ieee.org/document/11080380)]
22. Cracks in The Stack [2025-05] [[paper](https://ieeexplore.ieee.org/document/11028470)]
23. Unseen Horizons [2025-04] [[paper](https://ieeexplore.ieee.org/document/11029836)]
24. DataRecipe [2024-10] [[paper](https://dl.acm.org/doi/10.1145/3691620.3695593)]
25. LLM-ProS [2025-05] [[paper](https://ieeexplore.ieee.org/document/11028406)]

### 🔍 RQ4: Detection Methods

Detection techniques are evolving from rigid static analysis to dynamic, model-driven, and hybrid evaluation frameworks. They form the diagnostic foundation of LLM quality governance and are classified into two categories:

#### 1. Code-Level Detection

Identifies defects in generated code (e.g., runtime failures, hallucinations, security vulnerabilities) using three main paradigms:

- **Dynamic Analysis**: Test-based execution (unit tests, functional benchmarks) and runtime monitoring to assess execution accuracy and resource efficiency.
- **Static Analysis**: Rule-based detection (via tools like SonarQube, Semgrep) and manual inspection to find syntax errors, vulnerabilities, and code smells without executing the code.
- **Model-based Detection**: "LLM-as-a-judge" techniques (direct, prompt-engineered, or fine-tuned evaluation) and lightweight ML classifiers for scalable semantic filtering.

#### 2. Data-Level Detection

Targets the integrity, provenance, and representativeness of the underlying training data:

- **Dynamic Analysis**: Execution-based validation (checking if scraped code compiles) and metric drift monitoring (detecting data leakage or contamination through training loss curves).
- **Static Analysis**: Rule-based detection, human review, and provenance tracing (using file hashes to identify duplicate or benchmark-contaminated data).
- **Model-based Detection**: High-throughput semantic screening using LLMs or lightweight classifiers to evaluate sample readability, information entropy, and potential hazards.

<br>

<div align="center">
  <img src="images/generated_code_issues_detection.png" alt="Taxonomy of Code Issue Detection Methods" width="100%">
  <p><em>Fig. 6. Taxonomy of Code Issue Detection Techniques</em></p>
</div>

<br>

<div align="center">
  <img src="images/data_quality_issues_detection.png" alt="Taxonomy of Dataset Issue Detection Methods" width="100%">
  <p><em>Fig. 7. Taxonomy of Training Data Issue Detection Techniques</em></p>
</div>

**📄 Papers Referenced in this Section:**

1. LLMs Meet Library Evolution [2024-06] [[paper](https://arxiv.org/abs/2406.09834)]
2. Less is More [2025-02] [[paper](https://arxiv.org/abs/2502.14212)]
3. Qwen [2023-09] [[paper](https://arxiv.org/abs/2309.16609)]
4. Qwen2 [2024-07] [[paper](https://arxiv.org/abs/2407.10671)]
5. DataMan [2025-02] [[paper](https://arxiv.org/abs/2502.19363)]
6. Phi-4 [2024-12] [[paper](https://arxiv.org/abs/2412.08905)]
7. Copilot Security [2022-04] [[paper](https://arxiv.org/abs/2204.04741)]
8. Copilot Evaluation [2025-01] [[paper](https://doi.org/10.1145/3524842.3528470)]
9. HalluCode [2024-04] [[paper](https://arxiv.org/abs/2404.00971)]
10. CodeHalu [2024-05] [[paper](https://arxiv.org/abs/2405.00253)]
11. EffiBench [2024-02] [[paper](https://arxiv.org/abs/2402.02037)]
12. Mercury [2024-02] [[paper](https://arxiv.org/abs/2402.07844)]
13. SStuBs [2023-03] [[paper](https://arxiv.org/abs/2303.11455)]
14. package hallucinations [2024-06] [[paper](https://arxiv.org/abs/2406.10279)]
15. HallTrigger [2024-07] [[paper](https://arxiv.org/abs/2407.04831)]
16. Large Language Models for Code [2023-02] [[paper](https://arxiv.org/abs/2302.05319)]
17. Purple Llama CYBERSECEVAL [2023-12] [[paper](https://arxiv.org/abs/2312.04724)]
18. Lost at C [2022-08] [[paper](https://arxiv.org/abs/2208.09727)]
19. AI Assistants Security [2022-11] [[paper](https://arxiv.org/abs/2211.03622)]
20. The Counterfeit Conundrum [2024-02] [[paper](https://arxiv.org/abs/2402.19475)]
21. Bugs in LLM-generated Code [2024-03] [[paper](https://arxiv.org/abs/2403.08937)]
22. GitHub Copilot, Amazon CodeWhisperer, ChatGPT [2023-04] [[paper](https://arxiv.org/abs/2304.10778)]
23. ChatGPT Code Quality [2023-08] [[paper](https://arxiv.org/abs/2308.04838)]
24. CloudAPIBench [2024-07] [[paper](https://arxiv.org/abs/2407.09726)]
25. CodeMirage [2024-08] [[paper](https://arxiv.org/abs/2408.08333)]
26. LLM-generated Code Efficiency [2024-04] [[paper](https://arxiv.org/abs/2404.06041)]
27. Syntactic Robustness [2024-04] [[paper](https://arxiv.org/abs/2404.01535)]
28. DeSec [2024-10] [[paper](https://arxiv.org/abs/2410.08858)]
29. Bias Unveiled [2024-11] [[paper](https://arxiv.org/abs/2411.10351)]
30. FairCoder [2025-01] [[paper](https://arxiv.org/abs/2501.05396)]
31. From Effectiveness to Efficiency [2024-06] [[paper](https://arxiv.org/abs/2406.00602)]
32. ENAMEL [2024-06] [[paper](https://arxiv.org/abs/2406.06647)]
33. DeVAIC [2024-04] [[paper](https://arxiv.org/abs/2404.07548)]
34. PTMs [2024-11] [[paper](https://arxiv.org/abs/2411.10565)]
35. Codequal Analyzer [2025-06] [[paper](https://arxiv.org/abs/2506.02211)]
36. Artificial-Intelligence Generated Code Considered Harmful [2024-09] [[paper](https://arxiv.org/abs/2409.19182)]
37. Unveiling Inefficiencies in LLM-Generated Code [2025-03] [[paper](https://arxiv.org/abs/2503.06327)]
38. Python Tests Quality [2025-06] [[paper](https://arxiv.org/abs/2506.14297)]
39. CoQuIR [2025-06] [[paper](https://arxiv.org/abs/2506.11066)]
40. REAL [2025-05] [[paper](https://arxiv.org/abs/2505.22704)]
41. CIDRe [2025-05] [[paper](https://arxiv.org/abs/2505.19757)]
42. Infinite-Instruct [2025-05] [[paper](https://arxiv.org/abs/2505.23177)]
43. Quality In, Quality Out [2025-03] [[paper](https://arxiv.org/abs/2503.11402)]
44. Security and Quality in LLM-Generated Code [2025-02] [[paper](https://arxiv.org/abs/2502.01853)]
45. SwallowCode [2025-05] [[paper](https://arxiv.org/abs/2505.02881)]
46. ROSE [2025-07] [[paper](https://arxiv.org/abs/2507.12561)]
47. Refining ChatGPT-Generated Code [2023-07] [[paper](https://arxiv.org/abs/2307.12596)]
48. Qwen3 [2025-05] [[paper](https://arxiv.org/abs/2505.09388)]
49. Qwen2.5 [2024-12] [[paper](https://arxiv.org/abs/2412.15115)]
50. TeleChat [2025-07] [[paper](https://arxiv.org/abs/2507.18013)]
51. Kimi K2 [2025-07] [[paper](https://arxiv.org/abs/2507.20534)]
52. ReCode [2025-06] [[paper](https://arxiv.org/abs/2506.20495)]
53. Seed-Coder [2025-06] [[paper](https://arxiv.org/abs/2506.03524)]
54. Data-efficient Fine-tuning [2025-04] [[paper](https://arxiv.org/abs/2504.12687)]
55. CRPE [2025-05] [[paper](https://arxiv.org/abs/2505.10594)]
56. DeepSeek-Coder [2024-01] [[paper](https://arxiv.org/abs/2401.14196)]
57. StarCoder 2 and The Stack v2 [2024-02] [[paper](https://arxiv.org/abs/2402.19173)]
58. CodeSmellEval [2024-12] [[paper](https://arxiv.org/abs/2412.18989)]
59. RPG [2025-05] [[paper](https://arxiv.org/abs/2505.10402)]
60. Repetition In Repetition Out [2023-10] [[paper](https://arxiv.org/abs/2310.10226)]
61. Every Sample Matters [2025-03] [[paper](https://arxiv.org/abs/2503.17793)]
62. WaveCoder [2023-12] [[paper](https://arxiv.org/abs/2312.14187)]
63. Brevity is the soul of wit [2024-07] [[paper](https://arxiv.org/abs/2407.00434)]
64. Benchmark Builders [2025-04] [[paper](https://arxiv.org/abs/2504.19444)]
65. Beyond Correctness [2024-07] [[paper](https://arxiv.org/abs/2407.11470)]
66. Generated Code Diversity [2024-08] [[paper](https://arxiv.org/abs/2408.14504)]
67. CodeMI [2024-04] [[paper](https://arxiv.org/abs/2404.14296)]
68. DataComp-LM [2024-06] [[paper](https://arxiv.org/abs/2406.11794)]
69. Codex [2021-07] [[paper](https://arxiv.org/abs/2107.03374)]
70. Path Planning Evaluation [2025-04] [[paper](https://arxiv.org/abs/2504.21276)]
71. CODEJUDGE [2024-01] [[paper](https://aclanthology.org/2024.emnlp-main.1118.pdf?utm_source=chatgpt.com)]
72. Datasets for Large Language Models [2024-02] [[paper](https://arxiv.org/abs/2402.18041)]
73. Synthetic Data Generation [2025-01] [[paper](https://ieeexplore.ieee.org/document/11080380)]
74. Cracks in The Stack [2025-05] [[paper](https://ieeexplore.ieee.org/document/11028470)]
75. Unseen Horizons [2025-04] [[paper](https://ieeexplore.ieee.org/document/11029836)]
76. MG-Verilog [2024-06] [[paper](https://ieeexplore.ieee.org/document/10691738)]
77. Code Generation Survey [2024-08] [[paper](https://dl.acm.org/doi/10.1145/3747588)]
78. DataRecipe [2024-10] [[paper](https://dl.acm.org/doi/10.1145/3691620.3695593)]
79. Training Data Extraction [2025-08] [[paper](https://dl.acm.org/doi/10.1145/3709018.3736331)]
80. aiXcoder-7B [2025-04] [[paper](https://ieeexplore.ieee.org/document/11121702)]
81. Imperfect Code Generation [2024-05] [[paper](https://ieeexplore.ieee.org/document/10554837)]
82. Inter-Dataset Code Duplication [2025-01] [[paper](https://ieeexplore.ieee.org/document/10759822)]
83. LLM-ProS [2025-05] [[paper](https://ieeexplore.ieee.org/document/11028406)]
84. ClassEval [2024-6] [[paper](https://ieeexplore.ieee.org/document/10549472)]
85. Uncovering Pretraining Code in LLMs [2025-11] [[paper](https://arxiv.org/abs/2511.07033)]
86. RealSec-Bench [2026-01] [[paper](https://arxiv.org/abs/2601.22706)]
87. ShortCoder [2026-01] [[paper](https://arxiv.org/abs/2601.09703)]
88. APIKG4SYN [2025-11] [[paper](https://arxiv.org/abs/2512.00380)]
89. MultiCodeIF [2025-07] [[paper](https://arxiv.org/abs/2507.00699)]
90. Beyond Functional Correctness [2024-06] [[paper](https://arxiv.org/abs/2407.00456)]
91. Adadec [2025-06] [[paper](https://arxiv.org/html/2506.08980v1)]
92. Code Copycat Conundrum [2025-04] [[paper](https://arxiv.org/abs/2504.12608)]
93. AllianceCoder [2025-03] [[paper](https://arxiv.org/abs/2503.20589)]
94. RustEvo^ 2 [2025-03] [[paper](https://arxiv.org/abs/2503.16922)]
95. RobGen [2025-03] [[paper](https://arxiv.org/abs/2503.20197)]
96. Llm Hallucinations in Practical Code Generation [2024-09] [[paper](https://arxiv.org/abs/2409.20550)]
97. COFFE [2025-02] [[paper](https://arxiv.org/abs/2502.02827)]
98. AATK Benchmark [2021-08] [[paper](https://dl.acm.org/doi/10.1145/3610721)]

### 🛠️ RQ5: Governance Strategies

We synthesize a **Multi-layered Governance Framework** spanning the entire data lifecycle and model inference stages to address quality defects:

#### 1. Code-Level Mitigation

- **Model-level**: SFT, RLHF/DPO, Reward-based optimization (combining execution correctness with static metrics), and Regularization-based stabilization to prevent mode collapse.
- **Generation-level**:
  - _Pre-generation_: Prompt Engineering, RAG, and Agent-based workflows.
  - _In-generation_: Adaptive decoding constraints and Iterative Self-reflection.
  - _Post-generation_: Automated AST-level repairs and sandbox execution filtering.

#### 2. Data-Level Mitigation

- **Cleaning & Filtering**: Execution-feedback elimination, static rule sanitization, and LLM-driven semantic cleaning to remove noise and vulnerabilities.
- **Data Balancing**: Stratified resampling across programming languages, domains, and difficulty levels to mitigate representation bias.
- **Data Enhancement**: Using LLMs or formatting tools to refactor, add docstrings, and standardize existing low-quality code.
- **Data Augmentation**: Expanding datasets via high-quality synthetic generation (rule/LLM-based) and integration of curated open-source repositories.

<br>

<div align="center">
  <img src="images/generated_code_issues_detection.png" alt="Taxonomy of Code Issue Mitigation Strategies" width="100%">
  <p><em>Fig. 8. Taxonomy of Code Issue Mitigation Strategies</em></p>
</div>

<br>

<div align="center">
  <img src="images/data_quality_issues_mitigation.png" alt="Taxonomy of Dataset Issue Mitigation Strategies" width="100%">
  <p><em>Fig. 9. Taxonomy of Training Data Issue Mitigation Strategies</em></p>
</div>

**📄 Papers Referenced in this Section:**
 
1. LLMs Meet Library Evolution [2024-06] [[paper](https://arxiv.org/abs/2406.09834)]
2. Less is More [2025-02] [[paper](https://arxiv.org/abs/2502.14212)]
3. Qwen [2023-09] [[paper](https://arxiv.org/abs/2309.16609)]
4. Qwen2 [2024-07] [[paper](https://arxiv.org/abs/2407.10671)]
5. DataMan [2025-02] [[paper](https://arxiv.org/abs/2502.19363)]
6. Phi-4 [2024-12] [[paper](https://arxiv.org/abs/2412.08905)]
7. SStuBs [2023-03] [[paper](https://arxiv.org/abs/2303.11455)]
8. package hallucinations [2024-06] [[paper](https://arxiv.org/abs/2406.10279)]
9. Large Language Models for Code [2023-02] [[paper](https://arxiv.org/abs/2302.05319)]
10. CloudAPIBench [2024-07] [[paper](https://arxiv.org/abs/2407.09726)]
11. AutoAPIEval [2024-09] [[paper](https://arxiv.org/abs/2409.15228)]
12. Codequal Analyzer [2025-06] [[paper](https://arxiv.org/abs/2506.02211)]
13. REAL [2025-05] [[paper](https://arxiv.org/abs/2505.22704)]
14. CIDRe [2025-05] [[paper](https://arxiv.org/abs/2505.19757)]
15. Infinite-Instruct [2025-05] [[paper](https://arxiv.org/abs/2505.23177)]
16. Quality In, Quality Out [2025-03] [[paper](https://arxiv.org/abs/2503.11402)]
17. SwallowCode [2025-05] [[paper](https://arxiv.org/abs/2505.02881)]
18. Refining ChatGPT-Generated Code [2023-07] [[paper](https://arxiv.org/abs/2307.12596)]
19. Qwen3 [2025-05] [[paper](https://arxiv.org/abs/2505.09388)]
20. Qwen2.5 [2024-12] [[paper](https://arxiv.org/abs/2412.15115)]
21. TeleChat [2025-07] [[paper](https://arxiv.org/abs/2507.18013)]
22. Kimi K2 [2025-07] [[paper](https://arxiv.org/abs/2507.20534)]
23. ReCode [2025-06] [[paper](https://arxiv.org/abs/2506.20495)]
24. Seed-Coder [2025-06] [[paper](https://arxiv.org/abs/2506.03524)]
25. Data-efficient Fine-tuning [2025-04] [[paper](https://arxiv.org/abs/2504.12687)]
26. CRPE [2025-05] [[paper](https://arxiv.org/abs/2505.10594)]
27. DeepSeek-Coder [2024-01] [[paper](https://arxiv.org/abs/2401.14196)]
28. Code Pretraining [2024-09] [[paper](https://arxiv.org/abs/2409.04556)]
29. StarCoder 2 and The Stack v2 [2024-02] [[paper](https://arxiv.org/abs/2402.19173)]
30. CodeSmellEval [2024-12] [[paper](https://arxiv.org/abs/2412.18989)]
31. RPG [2025-05] [[paper](https://arxiv.org/abs/2505.10402)]
32. Repetition In Repetition Out [2023-10] [[paper](https://arxiv.org/abs/2310.10226)]
33. Brevity is the soul of wit [2024-07] [[paper](https://arxiv.org/abs/2407.00434)]
34. Benchmark Builders [2025-04] [[paper](https://arxiv.org/abs/2504.19444)]
35. CodeCipher [2024-10] [[paper](https://arxiv.org/abs/2410.05797)]
36. DataComp-LM [2024-06] [[paper](https://arxiv.org/abs/2406.11794)]
37. RedStone [2024-12] [[paper](https://arxiv.org/abs/2412.03398)]
38. Code Llama [2023-08] [[paper](https://arxiv.org/abs/2308.12950)]
39. Codex [2021-07] [[paper](https://arxiv.org/abs/2107.03374)]
40. Path Planning Evaluation [2025-04] [[paper](https://arxiv.org/abs/2504.21276)]
41. CODEJUDGE [2024-01] [[paper](https://aclanthology.org/2024.emnlp-main.1118.pdf?utm_source=chatgpt.com)]
42. Synthetic Data Generation [2025-01] [[paper](https://ieeexplore.ieee.org/document/11080380)]
43. Cracks in The Stack [2025-05] [[paper](https://ieeexplore.ieee.org/document/11028470)]
44. MG-Verilog [2024-06] [[paper](https://ieeexplore.ieee.org/document/10691738)]
45. Code Generation Survey [2024-08] [[paper](https://dl.acm.org/doi/10.1145/3747588)]
46. DataRecipe [2024-10] [[paper](https://dl.acm.org/doi/10.1145/3691620.3695593)]
47. aiXcoder-7B [2025-04] [[paper](https://ieeexplore.ieee.org/document/11121702)]
48. Imperfect Code Generation [2024-05] [[paper](https://ieeexplore.ieee.org/document/10554837)]
49. Inter-Dataset Code Duplication [2025-01] [[paper](https://ieeexplore.ieee.org/document/10759822)]
50. LLM-ProS [2025-05] [[paper](https://ieeexplore.ieee.org/document/11028406)]
51. UCD-Training [2026-02] [[paper](https://arxiv.org/abs/2602.20799)]
52. ShortCoder [2026-01] [[paper](https://arxiv.org/abs/2601.09703)]
53. APIKG4SYN [2025-11] [[paper](https://arxiv.org/abs/2512.00380)]
54. MultiCodeIF [2025-07] [[paper](https://arxiv.org/abs/2507.00699)]
55. Beyond Functional Correctness [2024-06] [[paper](https://arxiv.org/abs/2407.00456)]
56. Adadec [2025-06] [[paper](https://arxiv.org/html/2506.08980v1)]
57. Code Copycat Conundrum [2025-04] [[paper](https://arxiv.org/abs/2504.12608)]
58. AllianceCoder [2025-03] [[paper](https://arxiv.org/abs/2503.20589)]
59. RustEvo^ 2 [2025-03] [[paper](https://arxiv.org/abs/2503.16922)]
60. RobGen [2025-03] [[paper](https://arxiv.org/abs/2503.20197)]
61. Llm Hallucinations in Practical Code Generation [2024-09] [[paper](https://arxiv.org/abs/2409.20550)]
62. COFFE [2025-02] [[paper](https://arxiv.org/abs/2502.02827)]

---

## 🤝 Contribution

We warmly welcome contributions from the community! If you have new research or have discovered missing classic papers, please follow these steps:

1. Fork this repository.
2. Add your paper to the corresponding RQ section following the existing table format.
3. Submit a Pull Request.
