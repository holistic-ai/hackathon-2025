# Example Systems & Resources

Case studies and datasets demonstrating observability and tracing patterns.

**Note**: Code examples for the agent systems that generated the traces are available in [Track A](../track_a_iron_man/).

## Case Studies

### AgentGraph

**Location**: `agent_graph_AAAI.pdf`

A trace-to-graph platform for interactive analysis and robustness testing in agentic AI systems (AAAI 2026 Demo Track). Converts execution logs into interactive knowledge graphs with nodes representing agents, tasks, tools, inputs/outputs, and humans, enabling both qualitative failure detection and quantitative robustness evaluation.

**Paper**: [`agent_graph_AAAI.pdf`](agent_graph_AAAI.pdf) - AAAI 2026 Demo Track

**Video**: [Demo Video](https://youtu.be/btrS9pfDYJY?si=dDX4tIs-oS2O2d2p)

**Key Features**:

- Converts raw execution traces into interactive knowledge graphs
- Failure detection across five risk categories (agent error, planning error, execution error, retrieval error, hallucination)
- Optimization recommendations (prompt refinement, agent merging, task consolidation, tool enhancement, workflow simplification)
- Reference-based traceability linking graph elements to exact trace lines
- Perturbation testing (jailbreak attempts, counterfactual fairness tests)
- Causal attribution identifying components that drive behavioral changes

**Relevance to Track B**: Demonstrates how to transform raw execution traces into interpretable knowledge graphs, enabling visual analysis of agent behavior and true observability

### AgentSeer

An observability-based evaluation framework that decomposes agentic executions into granular action and component graphs, enabling systematic agentic-situational assessment of model- and agentic-level vulnerabilities in LLMs.

**Paper**: [arXiv:2509.04802](https://arxiv.org/abs/2509.04802) - Mind the Gap: Evaluating Model- and Agentic-Level Vulnerabilities in LLMs with Action Graphs

**Awards**: AAAI 2026 Demo Track, NeurIPS 2025 LLMEval, OpenAI RedTeaming Challenge Winner

**Demo**: [Hugging Face Spaces](https://huggingface.co/spaces/holistic-ai/AgentSeer)

**Video**: [Demo Video](https://www.youtube.com/watch?v=8pDTIIVRwmQ)

**Key Features**:

- Decomposes agentic executions into granular action and component graphs
- Systematic agentic-situational assessment framework
- Reveals fundamental differences between model-level and agentic-level vulnerability profiles
- Identifies "agentic-only" vulnerabilities that emerge exclusively in agentic contexts
- Cross-model validation on GPT-OSS-20B and Gemini-2.0-flash
- Demonstrates tool-calling showing 24-60% higher ASR (Attack Success Rate)
- Context-dependent attack effectiveness analysis

**Relevance to Track B**: Demonstrates how observability enables systematic evaluation of vulnerabilities, revealing that traditional model-level evaluation misses critical agentic-specific risks, and showing how action graphs enable comprehensive security assessment

## Datasets & Benchmarks

### Who_and_When Dataset

**Location**: [`failure_attribution/`](failure_attribution/) (GitHub submodule)

An agent trace database for automated failure attribution in multi-agent systems. Contains execution traces with fine-grained annotations identifying which agent caused failures and when critical errors occurred.

**GitHub Repository**: [mingyin1/Agents_Failure_Attribution](https://github.com/mingyin1/Agents_Failure_Attribution) - ICML 2025 Spotlight

**Code**: See [`failure_attribution/`](failure_attribution/) directory (submodule)

**Dataset**: [Who_and_When](https://huggingface.co/datasets/Kevin355/Who_and_When) - 184 annotated failure tasks from algorithm-generated and hand-crafted multi-agent systems

**Paper**: [arXiv:2505.00212](https://arxiv.org/pdf/2505.00212)

**Key Features**:

- Agent execution traces database with failure annotations
- Fine-grained failure annotations (who failed, when, why)
- Real-world multi-agent scenarios from GAIA and AssistantBench
- Automated failure attribution methods
- Foundation for evaluating observability and explainability systems

## How to Use

1. **Study the code**: Understand how each system implements observability
2. **Run the systems**: Execute the agents and generate your own traces
3. **Analyze traces**: Compare with provided traces in `../traces/`
4. **Learn patterns**: See how different complexity levels affect trace structure
