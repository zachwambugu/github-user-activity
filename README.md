
# GitHub User Activity CLI

# Overview

The GitHub User Activity CLI is a Python-based command-line application that fetches and displays the recent activity of a specified GitHub user. This tool is perfect for exploring public GitHub activity in an easy and interactive manner.

# Features

1. Fetch recent activity for any GitHub user.
2. Display event details such as:
      Pushed commits to a repository.
      Opened or closed issues.
      Starred repositories.
      Handles errors gracefully, such as:
      Invalid GitHub usernames.
      API rate limits.
      Network issues.
      Prerequisites
 # Before running the application, ensure you have the following:
Python 3 installed.
An active internet connection.

# Installation
1. Clone or download this repository to your local machine:
  **git clone zachwambugu/github-user-activity**
2. Navigate to the project directory:
  cd <project_directory>
3. Ensure the script file github-user-activity.py exists in the directory.

# Usage
Run the script using Python:
```python github-user-activity.py```
Enter the GitHub username when prompted:
Enter the GitHub username: <username>

The application will display the recent activity for the specified username, such as:

`Fetching activity for GitHub user: zachwambugu...
Pushed 3 commits to zachwambugu/Hello-World
Starred octocat/Hello-World
Opened an issue in zachwambugu/Hello-World`

# Error Handling
The application handles various errors gracefully:

###I nvalid Username:
  If the entered username does not exist on GitHub, you'll see:
  Error: User not found.
  
### API Rate Limit Exceeded:
If the GitHub API rate limit is exceeded, you'll see:
Error: Rate limit exceeded. Try again later.

### Network Issues:
If there is a network connectivity issue, you'll see:

### Network Error: <specific_error_message>

# Contributing
Fork the repository.
Create a feature branch:
git checkout -b feature/your-feature-name
Commit your changes:
git commit -m "Add your message here"
Push the branch:
git push origin feature/your-feature-name
Create a pull request.
## License
This project is open-source and available under the MIT License.

# Acknowledgments
GitHub API Documentation
Python's standard library modules: urllib and json.

