#!/usr/bin/env python3
import os
from pathlib import Path

def find_git_repos(start_dir):
    """Find all folders in the user's home directory containing a .git folder."""
    repos = []
    start = Path(start_dir).expanduser().resolve()

    for root, dirs, files in os.walk(start, topdown=True):
        # Skip hidden/system dirs for speed and safety
        dirs[:] = [d for d in dirs if not d.startswith('.') and d.lower() != 'node_modules']

        git_dir = Path(root) / ".git"
        if git_dir.is_dir():
            repos.append(str(Path(root).resolve()))
            # Don’t search inside found repos
            dirs[:] = []

    return repos


def main():
    home = Path.home()
    print(f"🔍 Searching for Git repositories in {home}...\n")
    found = find_git_repos(home)

    if found:
        print(f"✅ Found {len(found)} repositories:\n")
        for repo in found:
            print("•", repo)
    else:
        print("❌ No Git repositories found in your home directory.")


if __name__ == "__main__":
    main()
