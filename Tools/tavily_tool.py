from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

cli = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


def travily_search(query):

    response = cli.search(
        query=query,
        max_results=5
    )

    results = []

    for i, r in enumerate(response["results"], 1):

        title = r.get("title", "unknown")
        url = r.get("url", "unknown")
        snippet = r.get("content", "").strip()

        if len(snippet) > 300:
            snippet = snippet[:300].rsplit(" ", 1)[0] + "..."

        results.append({
            "Title": title,
            "Url": url,
            "Snippet": snippet
        })

    return results