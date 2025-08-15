#!/usr/bin/env python3
"""
Instant Search - Maximum Value Version
Opens everything you need in one command
"""

import webbrowser
import urllib.parse
import subprocess
import time
from datetime import datetime
import sys

def instant_search(query):
    """The most useful search tool - opens everything instantly"""
    
    print(f"\n🚀 INSTANT SEARCH: '{query}'")
    print(f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    # URL encode query
    q = urllib.parse.quote_plus(query)
    
    # Define all your search URLs
    searches = [
        # Your original 3 sites
        f"https://onesearch.cisco.com/searchpage/v1?queryFilter={q}",
        "https://circuit.cisco.com/app/home",
        "https://claude.ai/new",
        
        # Bonus useful searches
        f"https://www.google.com/search?q={q}",
        f"https://www.linkedin.com/search/results/all/?keywords={q}",
        f"https://github.com/search?q={q}",
        f"https://chat.openai.com/",
        f"https://www.perplexity.ai/search?q={q}",
        f"https://en.wikipedia.org/wiki/Special:Search?search={q}",
    ]
    
    print("🌐 Opening browser tabs...")
    
    # Open all tabs at once
    for i, url in enumerate(searches, 1):
        webbrowser.open(url)
        print(f"   {i}. {url.split('/')[2]}")
        time.sleep(0.3)  # Small delay
    
    print(f"\n✅ Opened {len(searches)} search tabs")
    print(f"📋 Your search term: '{query}'")
    print("💡 For AI chats: paste your query in the chat box")
    
    # Copy query to clipboard (macOS)
    try:
        subprocess.run(['pbcopy'], input=query.encode(), check=True)
        print("📎 Query copied to clipboard!")
    except:
        pass
    
    return len(searches)

def main():
    if len(sys.argv) > 1:
        query = ' '.join(sys.argv[1:])
        instant_search(query)
    else:
        print("⚡ INSTANT MULTI-SEARCH")
        print("Opens 8 search sites instantly!")
        print("\nUsage: s 'your search term'")
        print("\nQuick start:")
        
        while True:
            query = input("\n🔍 Search for: ").strip()
            if query.lower() in ['quit', 'exit', 'q']:
                break
            if query:
                instant_search(query)

if __name__ == "__main__":
    main()