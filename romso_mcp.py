import json
import urllib.request
import urllib.parse
from mcp.server.fastmcp import FastMCP

# Expressing server identity
mcp = FastMCP("ROMSO-Search")

@mcp.tool()
def search_wikipedia(query: str) -> str:
    """
    Search the full English Wikipedia snapshot via ROMSO's CPU-native C11 engine.
    Returns title, URL, and clean snippet text for the top results.
    """
    base_url = "https://api.romso.com/"
    params = urllib.parse.urlencode({"q": query, "format": "json"})
    url = f"{base_url}?{params}"
    
    req = urllib.request.Request(
        url, 
        headers={"User-Agent": "ROMSO-MCP-Client/1.0"}
    )
    
    try:
        with urllib.request.urlopen(req, timeout=5) as response:
            data = json.loads(response.read().decode("utf-8"))
            results = data.get("results", [])
            
            if not results:
                return "No results found."
            
            formatted = []
            for r in results[:5]:  # Top 5 Treffer für Context Window
                title = r.get("title", "No Title")
                link = r.get("url", "")
                content = r.get("content", "").strip()
                formatted.append(f"Title: {title}\nURL: {link}\nSnippet: {content}")
                
            return "\n\n---\n\n".join(formatted)
    except Exception as e:
        return f"Error querying ROMSO Search API: {str(e)}"

if __name__ == "__main__":
    mcp.run()
