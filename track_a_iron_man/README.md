<div align="center">

<img src="../assets/images/Holistic-AI-Logo-Hackathon-2025-05.jpg" alt="Track A Logo" width="400"/>

</div>

# Track A: Agent Iron Man

<div align="center">
<h2>Agent that works. Agent that lasts.</h2>
</div>

**Build agents that don't break.**

Build AI agents that are fast, efficient, and robust in real-world environments. Optimize latency, cost, and carbon footprint while hardening systems against prompt attacks, broken tools, and chaotic inputs — design agents built for production reliability.

## What You'll Build

**Choose your use case, build a reliable agent.** This track is open-ended — you can pick any application domain (e.g., research assistance, code generation, data analysis, customer support, content creation) and build an agent that solves real problems.

**But here's the key: It's not about what your agent can do — it's about proving it works reliably.**

Your challenge is to demonstrate that your agent can be trusted in real-world use. Anyone can build an agent that works once. Can you build one that works consistently, handles failures well, and keeps working under pressure?

**How do you justify reliability?**

- **Consistency**: Same input → same (or consistently similar) output. Show us tests that prove this.
- **Error handling**: What happens when things go wrong? Show us your agent recovering from failures.
- **Performance under load**: Does it break when many people use it? Show us it scales.
- **Cost efficiency**: Can it run affordably? Show us the numbers.
- **Long-term stability**: Will it still work tomorrow? Show us it's built to last.

<details>
<summary><strong>📚 Finding the right balance & Frugal AI principles</strong> — <em>Click to expand</em></summary>

**Finding the right balance**: Do you really need a complex agent? Sometimes a simple solution works better. The key questions are:

- **What problem are you solving?** Start with the simplest agent that solves it well
- **What's "good enough"?** Perfect isn't always necessary — find the balance between performance and complexity
- **When to add complexity?** Only when simpler approaches fail or when the added complexity clearly improves results

**Frugal AI: Smart resource use.** You don't always need the biggest, most expensive model. Think about:

- **Right tool for the job**: Use smaller models for simple tasks, save powerful models for complex problems
- **Cost vs. performance**: Can you achieve good results with less? Often the answer is yes
- **Start simple, scale smart**: Build something that works well first, then optimize only where it matters

</details>

**Your submission should prove reliability**: Show us metrics, monitoring, error handling, consistency tests, and evidence that your agent is ready for production use.

## Recommended Tutorials

1. [01_basic_agent.ipynb](../tutorials/01_basic_agent.ipynb) - Foundation: Introduction to LangGraph ReAct agents
2. [02_custom_tools.ipynb](../tutorials/02_custom_tools.ipynb) - Build production tools: Create custom tools for your agents
3. [03_structured_output.ipynb](../tutorials/03_structured_output.ipynb) - Efficient data handling: Get validated JSON responses
4. [04_model_monitoring.ipynb](../tutorials/04_model_monitoring.ipynb) - **Performance tracking: Track tokens, costs, and carbon emissions** ⭐
5. [06_benchmark_evaluation.ipynb](../tutorials/06_benchmark_evaluation.ipynb) - Evaluation: Measure agent performance and improvements
6. [07_reinforcement_learning.ipynb](../tutorials/07_reinforcement_learning.ipynb) - Advanced optimization: RL concepts for agent training (Optional)

**Additional helpful tutorials**: [05_observability.ipynb](../tutorials/05_observability.ipynb), [08_attack_red_teaming.ipynb](../tutorials/08_attack_red_teaming.ipynb)

## AWS Tools & Frameworks

**Building Agents on AWS** — Comprehensive Guide

A complete guide to building production-ready AI agents on AWS infrastructure. Covers agent architecture, deployment strategies, and AWS service integration.

- **Guide**: [`Building Agents on AWS.pdf`](Building%20Agents%20on%20AWS.pdf) - AWS agent development tutorial
- **Relevance to Track A**: Essential resource for teams building agents on AWS. Covers deployment, scaling, and integration with AWS services. Perfect complement to the AWS tools listed below.

**AWS Strands Agents SDK**

A model-driven SDK for building and running AI agents with a flexible, lightweight, and model-agnostic approach. Supports multi-agent workflows, MCP server integration, and deployment to AWS Bedrock AgentCore.

- **Documentation**: [AWS Prescriptive Guidance - Strands Agents](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-frameworks/strands-agents.html)
- **Quick Start**: [Build and Deploy Production-Ready AI Assistant](https://aws.amazon.com/getting-started/hands-on/strands-agentic-ai-assistant/)
- **GitHub**: [strands-agents/docs](https://github.com/strands-agents/docs)
- **Installation**: `pip install strands-agents`
- **Key Features**: Multi-agent workflows, sequential pipelines, orchestrator patterns, MCP integration, Bedrock AgentCore deployment
- **Relevance to Track A**: Provides a production-ready framework for building reliable agents with built-in workflow management, error handling, and AWS integration. Excellent for teams wanting to leverage AWS infrastructure for agent deployment and scaling.

**Amazon Nova**

A family of multimodal generative AI models supporting text, image, and video generation. Includes Nova Lite (fast, cost-effective) and Nova Premier (advanced capabilities with 1M token context window).

- **Documentation**: [Amazon Nova User Guide](https://docs.aws.amazon.com/nova/latest/userguide/what-is-nova.html)
- **Models**: Nova Lite (`us.amazon.nova-lite-v1:0`), Nova Premier (`us.amazon.nova-premier-v1:0`)
- **APIs**: Converse API (conversational), Invoke API (direct inference)
- **Features**: Multimodal support (text, image, video), large context windows, fine-tuning capabilities
- **Relevance to Track A**: Cost-effective model options for building efficient agents. Nova Lite is optimized for speed and cost, making it ideal for production workloads requiring fast responses and low latency.

**AWS Bedrock**

Fully managed service for building and scaling generative AI applications. Provides access to foundation models from Amazon, Anthropic, Meta, Mistral AI, and more.

- **Documentation**: [AWS Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- **Models**: Claude (Anthropic), Llama (Meta), Mistral, Titan (Amazon), and more
- **Features**: Model access, fine-tuning, RAG, agents, guardrails
- **Relevance to Track A**: Primary platform for accessing LLMs during the hackathon. Managed by Holistic AI, provides reliable API access for building production-ready agents.

**AWS Bedrock AgentCore**

Runtime for deploying and running AI agents at scale. Supports Strands Agents SDK and provides infrastructure for agent execution.

- **Documentation**: [Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore.html)
- **Integration**: Works seamlessly with Strands Agents SDK
- **Features**: Serverless deployment, auto-scaling, monitoring
- **Relevance to Track A**: Production deployment platform for agents built with Strands or other frameworks. Handles infrastructure management, allowing teams to focus on agent logic and reliability.

## Example Systems & Resources

**Small Language Models are the Future of Agentic AI** (NVIDIA Research)

A position paper arguing that small language models (SLMs) are sufficiently powerful, inherently more suitable, and necessarily more economical for many invocations in agentic systems. Discusses the operational and economic impact of shifting from LLMs to SLMs, outlines a general LLM-to-SLM agent conversion algorithm, and advocates for heterogeneous agentic systems leveraging SLMs for routine tasks and LLMs for complex reasoning.

- **Website**: [NVIDIA Research](https://research.nvidia.com/labs/lpr/slm-agents/)
- **Paper**: [arXiv:2506.02153](https://arxiv.org/abs/2506.02153) - Small Language Models are the Future of Agentic AI
- **Key Recommendations**: Prioritize SLMs for cost-effective deployment, design modular agentic systems, leverage SLMs for rapid specialization
- **Relevance to Track A**: Directly addresses performance optimization, cost efficiency, and production deployment strategies. Demonstrates how SLMs can reduce latency, energy consumption, and infrastructure costs while maintaining agent capabilities. Essential for building efficient, scalable agent systems that balance performance with cost-effectiveness.

**AgentHarm Benchmark**

A benchmark for measuring harmfulness of LLM agents, including 110 explicitly malicious agent tasks (440 with augmentations) covering 11 harm categories including fraud, cybercrime, and harassment. Evaluates whether models refuse harmful agentic requests and whether jailbroken agents maintain their capabilities following an attack to complete multi-step tasks.

- **Paper**: [arXiv:2410.09024](https://arxiv.org/abs/2410.09024) - AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents (ICLR 2025)
- **Dataset**: [Hugging Face](https://huggingface.co/datasets/ai-safety-institute/AgentHarm)
- **Documentation**: [Inspect Evals](https://ukgovernmentbeis.github.io/inspect_evals/evals/safeguards/agentharm/)
- **Codebase**: [GitHub](https://github.com/UKGovernmentBEIS/inspect_evals/tree/main/src/inspect_evals/agentharm)
- **Relevance to Track A**: Provides a complete benchmark for testing agent robustness and safety. Can be used to evaluate how well agents handle malicious requests, maintain safety guardrails, and demonstrate production-ready security measures. Essential for hardening agents against adversarial prompts and ensuring they refuse harmful requests while maintaining legitimate capabilities.

## Code Examples

**ReAct Agent** ([`examples/react_agent/`](examples/react_agent/))

A simple ReAct (Reasoning + Acting) agent built with LangGraph. Processes user queries by reasoning, deciding on actions, executing tools (like Tavily web search), and repeating until providing a final answer.

**Open Deep Research** ([`examples/deep_research/`](examples/deep_research/))

An automated deep research assistant that orchestrates multi-step research tasks. Spawns sub-agents for specific questions, summarizes information, and generates complete markdown reports.

## Track-Specific Submission Focus

Include performance metrics (latency, token usage, cost, carbon footprint), monitoring dashboards or logs, error handling demonstrations, and comparisons with baselines.

For complete requirements, see [README.md](../README.md#-registration--submission) and [HACKATHON_RULES.md](../docs/HACKATHON_RULES.md).
