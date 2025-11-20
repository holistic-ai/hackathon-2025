# Tutorials

**Event Website**: [hackathon.holisticai.com](https://hackathon.holisticai.com/)

Self-contained Jupyter notebooks teaching agent development with LangGraph.

---

## Tutorial Sequence

1. **[Basic Agent](01_basic_agent.ipynb)** - Introduction to LangGraph ReAct agents
2. **[Custom Tools](02_custom_tools.ipynb)** - Create and use custom tools
3. **[Structured Output](03_structured_output.ipynb)** - Get validated JSON responses
4. **[Model Monitoring](04_model_monitoring.ipynb)** - Track tokens, costs, carbon emissions
5. **[Observability](05_observability.ipynb)** - Deep tracing and debugging
6. **[Benchmark Evaluation](06_benchmark_evaluation.ipynb)** - Test agents on PhD-level questions
7. **[Reinforcement Learning](07_reinforcement_learning.ipynb)** - Train agents using RL (Advanced/Optional)
8. **[Attack & Red Teaming](08_attack_red_teaming.ipynb)** - Test agent security with red teaming techniques

---

## Setup

### Prerequisites

- Python 3.8+
- **AWS Bedrock managed by Holistic AI** (recommended) - Credentials will be provided during the hackathon event
- **OpenAI API key** (optional alternative)
- LangSmith API key (optional, for tutorial 05)
- Valyu API key (optional, for some examples)

### Installation

```bash
# Install all dependencies from root directory
pip install -r ../requirements.txt

# Or install individually (not recommended)
pip install langgraph langchain-core langchain-openai python-dotenv requests tiktoken codecarbon
```

### Environment Setup

Create `.env` file in project root:

```bash
# AWS Bedrock managed by Holistic AI (credentials provided during hackathon)
HOLISTIC_AI_TEAM_ID=your-team-id-here
HOLISTIC_AI_API_TOKEN=your-api-token-here

# Alternative: OpenAI (optional)
OPENAI_API_KEY=sk-your-key-here

# Optional
VALYU_API_KEY=your-valyu-key-here
LANGSMITH_API_KEY=your-langsmith-key-here
```

**API Guide**: [../assets/api-guide.pdf](../assets/api-guide.pdf)

---

## Competition Tracks

**For detailed track descriptions**: [hackathon.holisticai.com](https://hackathon.holisticai.com/)

- **Track A (Iron Man)**: Tutorials 01, 02, 03, 04, 06, 07
- **Track B (Glass Box)**: Tutorials 01, 02, 03, 04, 05
- **Track C (Dear Grandma)**: Tutorials 01, 06, 08

---

## Resources

- **Event Website**: [hackathon.holisticai.com](https://hackathon.holisticai.com/)
- **Discord**: [Join our Discord](https://discord.com/invite/QBTtWP2SU6?referrer=luma)
- **API Guide**: [AWS Bedrock API (Holistic AI managed)](../assets/api-guide.pdf)
- **Technical Support**: [Discord](https://discord.com/invite/QBTtWP2SU6?referrer=luma)
- **Starting Kit**: [../core/README.md](../core/README.md)
