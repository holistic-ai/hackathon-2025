# Execution Traces

LangSmith execution traces from simple to complex agent scenarios.

**Note**: Source code for the agent systems that generated these traces is available in [Track A](../../track_a_iron_man/).

## Trace Files

| File                     | Size  | Complexity  | Source System          | Code Location                                                                                      |
| ------------------------ | ----- | ----------- | ---------------------- | -------------------------------------------------------------------------------------------------- |
| `trace-very-simple.json` | 13KB  | Very Simple | **ReAct Agent**        | [`../../track_a_iron_man/examples/react_agent/`](../../track_a_iron_man/examples/react_agent/)     |
| `trace-simple.json`      | 65KB  | Simple      | **ReAct Agent**        | [`../../track_a_iron_man/examples/react_agent/`](../../track_a_iron_man/examples/react_agent/)     |
| `trace-normal.json`      | 251KB | Normal      | **Open Deep Research** | [`../../track_a_iron_man/examples/deep_research/`](../../track_a_iron_man/examples/deep_research/) |
| `trace-complex.json`     | 15MB  | Complex     | **Open Deep Research** | [`../../track_a_iron_man/examples/deep_research/`](../../track_a_iron_man/examples/deep_research/) |

**System Locations**:

- ReAct Agent code: [`../../track_a_iron_man/examples/react_agent/`](../../track_a_iron_man/examples/react_agent/)
- Open Deep Research code: [`../../track_a_iron_man/examples/deep_research/`](../../track_a_iron_man/examples/deep_research/)

## How to Use

### 1. Analyze Structure

Open trace files in a JSON viewer or text editor to understand:

- How LangSmith captures agent execution
- What data is recorded at each step
- How state transitions are tracked

### 2. Visualize in LangSmith

1. Import traces into LangSmith UI
2. View execution graphs and timelines
3. Analyze decision points and tool calls
4. Understand agent reasoning paths

### 3. Build Custom Visualizations

Use trace data to create:

- Trajectory diagrams
- Decision flow charts
- Tool usage statistics
- Performance metrics

### 4. Learn Patterns

Compare traces to understand:

- How complexity affects trace size
- What observability data is captured
- How to structure your own traces
- Best practices for transparency

## Trace Structure

Each trace contains:

- **Run metadata**: Start/end times, run type, inputs/outputs
- **Events**: Execution events and state changes
- **Child runs**: Nested agent executions
- **Tool calls**: Tool invocations and results
- **State transitions**: Agent state changes

## Example Usage

```python
import json

# Load a trace
with open('trace-simple.json', 'r') as f:
    trace = json.load(f)

# Analyze structure
print(f"Run type: {trace[0]['run_type']}")
print(f"Duration: {trace[0]['end_time'] - trace[0]['start_time']}")
print(f"Events: {len(trace[0]['events'])}")
```
