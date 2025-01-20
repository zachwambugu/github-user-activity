import sys
import urllib.request
import json

def fetch_github_activity(username):
    """
    Fetch recent GitHub activity for the given username.
    """
    url = f"https://api.github.com/users/{username}/events"
    
    try:
        # Send a GET request
        with urllib.request.urlopen(url) as response:
            if response.status == 200:
                # Parse JSON response
                data = json.load(response)
                return data
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print("Error: User not found.")
        elif e.code == 403:
            print("Error: Rate limit exceeded. Try again later.")
        else:
            print(f"HTTP Error: {e.reason} ({e.code})")
    except urllib.error.URLError as e:
        print(f"Network Error: {e.reason}")
    
    return None

def display_activity(events):
    """
    Display the recent activity from the fetched events.
    """
    if not events:
        print("No activity found or unable to fetch data.")
        return

    for event in events[:10]:  # Limit to the latest 10 events
        event_type = event["type"]
        repo_name = event["repo"]["name"]
        
        if event_type == "PushEvent":
            commits = len(event["payload"]["commits"])
            print(f"Pushed {commits} commits to {repo_name}")
        elif event_type == "IssuesEvent":
            action = event["payload"]["action"]
            print(f"{action.capitalize()} an issue in {repo_name}")
        elif event_type == "WatchEvent":
            print(f"Starred {repo_name}")
        else:
            print(f"{event_type} in {repo_name}")

def main():
    """
    Main function to handle CLI arguments and run the application.
    """
    if len(sys.argv) != 2:
        print("Usage: github-activity <username>")
        sys.exit(1)
    
    username = sys.argv[1]
    print(f"Fetching activity for GitHub user: {username}...")
    
    events = fetch_github_activity(username)
    display_activity(events)

if __name__ == "__main__":
    main()
