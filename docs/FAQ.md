# FAQ

**Event**: [hackathon.holisticai.com](https://hackathon.holisticai.com/)

## Setup

**Q: How do I set up?**  
A: `pip install -r requirements.txt` → `cp .env.example .env` → Add your API keys → Start coding!

**Q: Which API keys do I need?**  
A: AWS Bedrock managed by Holistic AI (provided during hackathon). OpenAI, LangSmith, Valyu are optional.

**Q: Import errors?**  
A: Run `pip install -r requirements.txt` and check if all packages are installed.

## Tutorials

**Q: Where to start?**
A: Tutorial 1. Then follow your track:

- Track A: 01, 02, 03, 04, 06, 07
- Track B: 01, 02, 03, 04, 05
- Track C: 01, 06, 08

**Q: Notebooks not running?**  
A: Check kernel selection, dependencies (`pip install -r requirements.txt`), and `.env` file.

## API

**Q: How to use Bedrock API?**  
A: Add credentials to `.env`, then use `get_chat_model("claude-3-5-sonnet")`.  
[API Guide](../assets/api-guide.pdf)

**Q: Can I use OpenAI?**  
A: Yes. Set `OPENAI_API_KEY` and use `get_chat_model("gpt-5-mini", use_openai=True)`.

## Troubleshooting

**Q: ModuleNotFoundError?**  
A: `pip install -r requirements.txt` and restart your notebook kernel.

**Q: Jupyter won't start?**  
A: `pip install jupyter` → `cd tutorials && jupyter notebook`

**Q: API calls failing?**  
A: Check your `.env` file has correct API keys and credentials.

**Q: Tutorial 8 needs Ollama?**  
A: `ollama pull qwen3:0.6b`

## Help

- **Discord** (real-time): [Join our Discord](https://discord.com/invite/QBTtWP2SU6?referrer=luma)
- **GitHub Issues** (bugs/questions): [Submit an issue](https://github.com/holistic-ai/hackthon-2025/issues/new/choose)
- **API Guide**: [Link](../assets/api-guide.pdf)
