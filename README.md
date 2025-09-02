# Holiday Hero Letterwriter (Action-Icon Inspired)

Users want a fun, personalized Christmas letter that evokes the high-energy, motivational, tongue-in-cheek persona of a famous Austrian-born action icon without directly impersonating or claiming to be that person. The agent should transform a user-provided topic into a festive letter that captures high-level stylistic traits (confidence, gym/motivation vibes, playful action references, warm holiday wishes) while complying with style-transformation and impersonation policies.

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your OpenAI API key
```

## Usage

```bash
python run.py "Your input message here"
```

## Development

This agent is built using the OpenAI Agents SDK and follows canonical patterns from the official documentation.

### Files
- `agent.py` - Main agent implementation
- `run.py` - Command-line interface
- `requirements.txt` - Dependencies
- `.env.example` - Environment configuration template
