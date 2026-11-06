# ROMSO Wikipedia Search — MCP Server

An official Model Context Protocol (MCP) server for **api.romso.com**. Enables AI Assistants (Claude Desktop, Cursor, Aider, custom LLM agents) to query the full English Wikipedia index via ROMSO's CPU-native, low-latency C11 engine.

- **API Endpoint:** `https://api.romso.com/`
- **Engine:** C11 Inverted List Retrieval Core
- **Operator:** ROMSO LTD (Larnaca, Cyprus)
- **Track Record & Architecture:** [Engineering History](https://romso.cy/romso-benchmark-engineering-note.html)

---

## Quick Setup

### 1. Requirements
Ensure Python 3.10+ is installed along with the MCP SDK:
```bash
pip install mcp
