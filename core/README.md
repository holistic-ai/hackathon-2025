# Core - Optional Starter Code

> **For tutorials**: See [`../tutorials/README.md`](../tutorials/README.md)

Optional starter code for hackathon participants who want a quick starting point.

**Note**: Tutorials use official packages and are recommended for learning. This `core` folder is optional.

---

## Quick Start

```python
import sys
sys.path.insert(0, '../core')
from react_agent import create_react_agent
from valyu_tools import ValyuSearchTool

# Set HOLISTIC_AI_TEAM_ID and HOLISTIC_AI_API_TOKEN in .env
agent = create_react_agent(
    tools=[ValyuSearchTool()],
    model_name='claude-3-5-sonnet'
)

result = agent.invoke({'messages': [('user', 'What is quantum computing?')]})
print(result['messages'][-1].content)
```

## Installation

```bash
pip install -r requirements.txt
```

## Features

- AWS Bedrock API integration (managed by Holistic AI)
- Valyu search tool integration
- Multi-model support (Bedrock, OpenAI, Ollama)
- Structured output with Pydantic
- LangGraph orchestration

## Learn More

- **Tutorials**: [`../tutorials/README.md`](../tutorials/README.md) — **Start here!** Complete step-by-step guides
- **API Guide**: [`../assets/api-guide.pdf`](../assets/api-guide.pdf) — AWS Bedrock API documentation
- **Support**: [Discord](https://discord.com/invite/QBTtWP2SU6?referrer=luma) — Get help and ask questions
