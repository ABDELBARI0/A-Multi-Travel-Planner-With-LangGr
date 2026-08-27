from travily import Travily 
import os
from dotenv import load_dotenv

load_dotenv()

cli = Travily(
    api_key=os.getenv("TAVILY_API_KEY")
    )

def travily_search(query):
        
        response = cli.search(query=query , MaxResults=5 , )
        reuslts = []

        for i , r in enumerate(response["Results"],1):
                title = r.get("Title" , "unkown")
                url = r.get("Url" , "unkown")
                snippet = r.get("countent" , "").strip()

                if len(snippet) > 300:
                        snippet = snippet[:300].rsplit(" ",1)[0] + "..."
                        reuslts.append({
                            "Title": title,
                            "Url": url,
                            "Snippet": snippet
                        })

        return reuslts