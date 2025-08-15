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
        f"https://onesearch.cisco.com/searchpage/v1?queryFilter={q}",  # 1
        "https://circuit.cisco.com/app/home",  # 2
        f"https://www.perplexity.ai/search?q={q}",  # 3
        f"https://www.google.com/search?q={q}",  # 4
        "https://claude.ai/new",  # 5
        f"https://chat.openai.com/",  # 6
        f"https://github.com/search?q={q}",  # 7
        f"https://en.wikipedia.org/wiki/Special:Search?search={q}",  # 8
        f"https://www.linkedin.com/search/results/all/?keywords={q}",  # 9
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
    
    # Copy query to clipboard (cross-platform)
    try:
        import platform
        system = platform.system()
        
        if system == "Darwin":  # macOS
            subprocess.run(['pbcopy'], input=query.encode(), check=True)
        elif system == "Windows":  # Windows
            subprocess.run(['clip'], input=query.encode(), check=True, shell=True)
        elif system == "Linux":  # Linux
            # Try different clipboard utilities
            for cmd in [['xclip', '-selection', 'clipboard'], ['xsel', '--clipboard', '--input']]:
                try:
                    subprocess.run(cmd, input=query.encode(), check=True)
                    break
                except (subprocess.CalledProcessError, FileNotFoundError):
                    continue
        
        print("📎 Query copied to clipboard!")
    except:
        print("📎 Could not copy to clipboard (install xclip/xsel on Linux)")
        pass
    
    return len(searches)

def main():
    if len(sys.argv) > 1:
        query = ' '.join(sys.argv[1:])
        instant_search(query)
    else:
        print("⚡ INSTANT MULTI-SEARCH")
        print("Opens 9 search sites instantly!")
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