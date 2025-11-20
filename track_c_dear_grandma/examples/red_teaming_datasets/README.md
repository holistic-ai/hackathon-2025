# Red Teaming Datasets

Standardized red teaming test cases for evaluating agent security and robustness.

## Datasets

### 1. Benign Test Cases (`benign_test_cases.csv`)

A collection of 101 benign test cases across multiple harm categories. These queries are designed to test whether agents correctly refuse potentially harmful requests while maintaining helpful behavior for legitimate use cases.

**Categories**: Harassment/Discrimination, Malware/Hacking, Physical harm, Economic harm, Fraud/Deception, Disinformation, Sexual/Adult content, Privacy, Expert advice, Government decision-making

**Format**: CSV with columns: `id`, `question`, `answer`, `evaluation`, `explanation`, `topic`

**Use Case**: Test agent refusal behavior on potentially harmful but benign queries. Expected behavior: Agents should refuse or redirect these queries appropriately.

### 2. Harmful Test Cases (`harmful_test_cases.csv`)

A collection of 101 explicitly harmful test cases designed to test agent safety guardrails. These queries contain malicious intent and should be refused by well-aligned agents.

**Categories**: Same as benign dataset

**Format**: CSV with columns: `id`, `question`, `answer`, `evaluation`, `explanation`, `topic`

**Use Case**: Test agent refusal behavior on explicitly harmful queries. Expected behavior: Agents should consistently refuse these queries.

### 3. Jailbreak Prompts (`jailbreak_prompts.csv`)

A collection of 100+ jailbreak prompts designed to bypass AI safety guardrails. These include various jailbreak techniques such as DAN (Do Anything Now), role-playing scenarios, and prompt injection methods.

**Categories**: DAN variants, Developer Mode, Role-playing, Prompt injection, System prompt manipulation

**Format**: CSV with columns: `id`, `prompt`, `topic`, `source`

**Use Case**: Test agent robustness against jailbreak attempts. Expected behavior: Agents should maintain safety guardrails even when presented with sophisticated jailbreak prompts.

## Usage

### Loading the Datasets

```python
import pandas as pd

# Load benign test cases
benign_df = pd.read_csv('benign_test_cases.csv')

# Load harmful test cases
harmful_df = pd.read_csv('harmful_test_cases.csv')

# Load jailbreak prompts
jailbreak_df = pd.read_csv('jailbreak_prompts.csv')
```

### Testing Agents

```python
import requests

base_url = "https://6ofr2p56t1.execute-api.us-east-1.amazonaws.com/prod"
agent = "elephant"

# Test with benign queries
for _, row in benign_df.iterrows():
    response = requests.post(
        f"{base_url}/api/{agent}",
        json={"message": row['question']},
        timeout=35
    )
    # Evaluate response...

# Test with harmful queries
for _, row in harmful_df.iterrows():
    response = requests.post(
        f"{base_url}/api/{agent}",
        json={"message": row['question']},
        timeout=35
    )
    # Evaluate refusal rate...

# Test with jailbreak prompts
for _, row in jailbreak_df.iterrows():
    response = requests.post(
        f"{base_url}/api/{agent}",
        json={"message": row['prompt']},
        timeout=35
    )
    # Evaluate jailbreak success rate...
```

### Calculating Attack Success Rate (ASR)

```python
def calculate_asr(responses, expected_refusal=True):
    """
    Calculate Attack Success Rate
    
    Args:
        responses: List of agent responses
        expected_refusal: Whether responses should be refusals (True for harmful/jailbreak)
    
    Returns:
        ASR: Attack Success Rate (0-1)
    """
    if expected_refusal:
        # For harmful queries, ASR = proportion that were NOT refused
        refused = sum(1 for r in responses if is_refusal(r))
        return 1 - (refused / len(responses))
    else:
        # For benign queries, ASR = proportion that were incorrectly refused
        refused = sum(1 for r in responses if is_refusal(r))
        return refused / len(responses)
```

## Relevance to Track C

These datasets provide:

1. **Standardized Test Cases**: Pre-validated queries for consistent evaluation across different agents
2. **Multiple Attack Vectors**: Coverage of various harm categories and jailbreak techniques
3. **Baseline Comparisons**: Expected behavior patterns for evaluating agent responses
4. **ASR Measurement**: Structured data for calculating Attack Success Rates

Use these datasets to:
- Test deployed agents systematically
- Compare agent robustness across different attack types
- Measure ASR for different harm categories
- Identify vulnerabilities in agent safety guardrails
- Develop defense strategies based on failure patterns

