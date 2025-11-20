# Example GitHub Issues

This document shows examples of how to properly use our GitHub issue templates. You can create similar issues when you need help during the hackathon.

**👉 See live examples**: We've created sample issues you can reference:
- [Issue #1: Question Example](https://github.com/holistic-ai/hackthon-2025/issues/1)
- [Issue #2: Bug Report Example](https://github.com/holistic-ai/hackthon-2025/issues/2)
- [Issue #3: Feature Request Example](https://github.com/holistic-ai/hackthon-2025/issues/3)

---

## Example 1: Question Issue

**📌 Live Example**: [See Issue #1](https://github.com/holistic-ai/hackthon-2025/issues/1)

**How to create**: Click "New Issue" → Select "Question" template

**Title**: `[QUESTION] How do I get AWS Bedrock API credentials?`

**Body**:
```markdown
## Your Question
I've cloned the repository and installed dependencies, but I'm not sure how to get the AWS Bedrock API credentials mentioned in the `.env.example` file.

## What I've Tried
- Checked the README.md
- Looked at the API guide PDF
- Searched through the documentation

## Additional Context
I'm registered for the hackathon on November 15-16. Do I get the credentials at the event or should I receive them via email?

**Tip**: For faster help, join our [Discord](https://discord.com/invite/QBTtWP2SU6?referrer=luma)
```

**Label**: `question`

**Expected Response**: You'll receive credentials during the hackathon. Contact Zekun Wu (`@zekunwu_73994`) on Discord after forming your team (3-5 members).

---

## Example 2: Bug Report Issue

**📌 Live Example**: [See Issue #2](https://github.com/holistic-ai/hackthon-2025/issues/2)

**How to create**: Click "New Issue" → Select "Bug Report" template

**Title**: `[BUG] ImportError when running tutorial 01_basic_agent.ipynb`

**Body**:
```markdown
## Describe the Bug
When I try to run the first cell in `tutorials/01_basic_agent.ipynb`, I get an ImportError saying `langchain_core` module not found.

## To Reproduce
Steps to reproduce:
1. Clone the repository
2. Run `pip install -r requirements.txt`
3. Start Jupyter with `jupyter notebook`
4. Open `tutorials/01_basic_agent.ipynb`
5. Run the first cell with imports
6. See ImportError

## Expected Behavior
The imports should work without errors and I should be able to run the tutorial.

## Environment
- **OS**: macOS 14.0
- **Python Version**: 3.11.5
- **Installation Method**: pip

## Error Message
```
ImportError: No module named 'langchain_core'
```

## What I've Tried
- Reinstalled dependencies with `pip install -r requirements.txt --force-reinstall`
- Checked if the package is in requirements.txt

## Additional Context
This is my first time working with LangChain. Not sure if I'm missing a step in the setup.
```

**Label**: `bug`

**Potential Solution**: Try reinstalling with a fresh virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt --force-reinstall
```

---

## Example 3: Feature Request (Custom Issue)

**📌 Live Example**: [See Issue #3](https://github.com/holistic-ai/hackthon-2025/issues/3)

**How to create**: Click "New Issue" → Select "Open a blank issue"

**Title**: `[FEATURE] Add example for multi-agent collaboration`

**Body**:
```markdown
## Feature Description
It would be helpful to have an example showing how multiple agents can collaborate on a complex task (e.g., research agent + summarization agent).

## Use Case
I'm working on Track A and want to build a multi-agent system, but I'm not sure how to coordinate between agents using LangGraph.

## Suggested Implementation
- Add `tutorials/09_multi_agent_collaboration.ipynb`
- Show state management between agents
- Include cost tracking for multiple agents

## Alternatives Considered
- Looking at Track A examples, but they focus on single agents
- Checked LangGraph documentation, but need hackathon-specific example

## Additional Context
This would be especially useful for teams building complex systems for Track A (performance) and Track B (observability).
```

**Label**: `enhancement`

---

## How to Create Issues

### Via GitHub Web Interface
1. Go to [Issues page](https://github.com/holistic-ai/hackthon-2025/issues)
2. Click **"New Issue"**
3. Select a template (**Bug Report** or **Question**)
4. Fill in the required fields
5. Click **"Submit new issue"**

### Via GitHub CLI (Advanced)
```bash
# Question issue
gh issue create \
  --title "[QUESTION] Your question title" \
  --body "Your question details" \
  --label "question"

# Bug report issue
gh issue create \
  --title "[BUG] Your bug description" \
  --body "Bug details and reproduction steps" \
  --label "bug"
```

---

## When to Use GitHub Issues vs Discord

| Situation | Use GitHub Issues | Use Discord |
|-----------|------------------|-------------|
| **Bug in code/tutorials** | ✅ Yes | Optional |
| **Feature request** | ✅ Yes | Optional |
| **Quick question during hackathon** | Optional | ✅ Yes (faster) |
| **Setup/installation help** | Optional | ✅ Yes (real-time) |
| **Technical documentation issue** | ✅ Yes | Optional |
| **Need API keys/SageMaker access** | ❌ No | ✅ Yes (DM @zekunwu_73994) |

---

## Tips for Good Issues

### ✅ Good Examples
- Clear, descriptive titles with `[BUG]`, `[QUESTION]`, or `[FEATURE]` prefix
- Step-by-step reproduction instructions
- Include error messages, environment details, what you've tried
- Check existing issues first to avoid duplicates

### ❌ Bad Examples
- Vague titles like "It doesn't work" or "Help needed"
- No reproduction steps or error messages
- Missing environment information (OS, Python version)
- Asking for API keys in public issues (use Discord DM instead)

---

## Get Help

- **💬 Discord** (recommended for real-time help): [Join our Discord](https://discord.com/invite/QBTtWP2SU6?referrer=luma)
- **🐛 GitHub Issues** (for bugs and questions): [Submit an issue](https://github.com/holistic-ai/hackthon-2025/issues/new/choose)
- **📧 Email** (urgent matters): zekun.wu@holisticai.com
- **On Discord**: **Zekun Wu** (`@zekunwu_73994`) for API keys, SageMaker access

---

**Last Updated**: November 13, 2025
