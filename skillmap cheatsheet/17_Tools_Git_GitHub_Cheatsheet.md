# Cheatsheet: Git & GitHub

## Git (Version Control System)
*   **Purpose:** Tracks changes to files over time, allowing recall of specific versions.
*   **Local Tool:** Runs on your computer.
*   **Key Concepts:**
    *   **Repository (Repo):** Project folder tracked by Git.
    *   **Commit:** A snapshot of your project at a specific point in time.
    *   **Branch:** A parallel version of your project for isolated work.
    *   **Merge:** Integrating changes from one branch into another.

## Basic Git Commands
*   `git init`: Initialize a new local repository.
*   `git add <file>` / `git add .`: Stage changes for the next commit.
*   `git commit -m "message"`: Save staged changes as a new commit.
*   `git status`: Show status of working directory.
*   `git log`: View commit history.

## GitHub (Web-based Hosting & Collaboration)
*   **Purpose:** Hosts Git repositories online, provides collaboration tools.
*   **Features:** Repositories, Pull Requests, Issues, Project Boards, Actions.

## Basic GitHub Workflow
*   Create repo on GitHub.com.
*   `git clone <repo_url>`: Download remote repo to local.
*   `git push origin <branch_name>`: Upload local commits to remote.

## Intermediate Git/GitHub
*   **Branching:**
    *   `git branch <name>`: Create new branch.
    *   `git checkout <name>`: Switch branches.
    *   `git checkout -b <name>`: Create and switch.
*   **Merging:** `git merge <branch_to_merge>`.
*   **Pull Request (PR):** Request to merge changes from your branch to another's repo/branch (on GitHub).
*   **Forking:** Creating your own copy of someone else's repo on GitHub.
*   **Resolving Conflicts:** Manually fix conflicting lines during a merge.

## Proficiency Levels Summary

### 🔵 Basic
*   Understand the concept of version control.
*   Differentiate between Git (local tool) and GitHub (web platform).
*   Perform basic Git operations: `init`, `add`, `commit`, `status`, `log`.
*   Push local changes to a remote GitHub repository (`clone`, `push`).

### 🟡 Intermediate
*   Work effectively with **branches** (`branch`, `checkout`, `merge`).
*   Understand and participate in the **Pull Request (PR)** workflow for collaboration.
*   Resolve simple **merge conflicts**.
*   Use GitHub for basic project sharing and collaboration.

### 🟢 Strong
*   Utilize advanced Git commands (`rebase`, `cherry-pick`, `stash`, `revert`, `reset`).
*   Leverage GitHub features for project management (Issues, Projects, Wikis).
*   Integrate Git with automated workflows (e.g., **GitHub Actions** for CI/CD).
*   Understand best practices for collaborative development and code review processes.
*   Manage complex repository structures and contribute to open-source projects.
