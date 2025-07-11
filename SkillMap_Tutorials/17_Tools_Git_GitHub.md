# Tools Tutorial: Git & GitHub

This tutorial breaks down Git and GitHub skills into different proficiency levels. Your goal is to reach a **Basic (🔵)** level of understanding.

---

## 🔵 Basic Proficiency: Understanding Version Control and Basic Commands

At this level, you understand the concept of version control, what Git and GitHub are, and can perform basic operations like cloning, adding, committing, and pushing changes.

### 1. What is Version Control?

*   **Concept:** Version control is a system that records changes to a file or set of files over time so that you can recall specific versions later. It's like having an "undo" button for your entire project, but with a history of every change.
*   **Why it's essential:**
    *   **Tracking Changes:** See who changed what, when, and why.
    *   **Collaboration:** Work on the same project with others without overwriting each other's work.
    *   **Reversibility:** Easily revert to previous versions if something goes wrong.

### 2. Git vs. GitHub

*   **Git:** The **version control system** itself. It's a command-line tool that runs locally on your computer. It manages the history of your project.
*   **GitHub:** A **web-based platform** that hosts Git repositories. It provides a user interface and tools for collaboration, sharing, and project management. Think of it as a social network for code.

### 3. Basic Git Workflow (Local)

*   **`git init`:** Initializes a new Git repository in your current directory. This creates a hidden `.git` folder that Git uses to track changes.
*   **`git add <file_name>` (or `git add .`):** Stages changes. You are telling Git, "I want to include this file's current state in the next snapshot."
*   **`git commit -m "Your commit message"`:** Records the staged changes as a new snapshot (a "commit") in your local repository's history. The message should describe the changes.
*   **`git status`:** Shows the status of your working directory and staging area (which files are modified, staged, or untracked).
*   **`git log`:** Shows the commit history.

### 4. Basic GitHub Workflow (Remote)

*   **Creating a Repository on GitHub:** Go to GitHub.com, click "New repository," give it a name, and create it.
*   **`git clone <repository_url>`:** Downloads a copy of a remote repository from GitHub to your local machine.
*   **`git push origin <branch_name>`:** Uploads your local commits to the remote repository on GitHub. (`origin` is the default name for the remote repository, `main` or `master` is the default branch name).

### Realistic Example: Starting a New Analysis Project

You are starting a new data analysis project for sales data. You want to track your Python scripts and notes.

1.  **Create a local folder:** `mkdir sales_analysis`
2.  **Initialize Git:** `cd sales_analysis` then `git init`
3.  **Create a file:** `touch sales_script.py`
4.  **Add content to `sales_script.py`** (e.g., `print("Hello Sales Data!")`)
5.  **Stage the file:** `git add sales_script.py`
6.  **Commit the changes:** `git commit -m "Initial commit: Added sales script"`
7.  **Create a new repository on GitHub** (e.g., `sales-analysis-project`).
8.  **Link local to remote:** Copy the `git remote add origin ...` command from GitHub and run it in your local terminal.
9.  **Push to GitHub:** `git push origin main` (or `master`)

Now your `sales_script.py` is on GitHub, and you have a version-controlled project.

---

## 🟡 Intermediate Proficiency: Branching, Merging, and Collaboration

At this level, you can work with branches, merge changes, resolve simple conflicts, and collaborate effectively with others.

### 1. Branching and Merging

*   **Concept:** Branches allow you to work on different features or bug fixes in isolation from the main codebase. When your work is complete and stable, you merge it back into the main branch.
*   **`git branch <branch_name>`:** Creates a new branch.
*   **`git checkout <branch_name>`:** Switches to an existing branch.
*   **`git checkout -b <new_branch_name>`:** Creates and switches to a new branch.
*   **`git merge <branch_to_merge>`:** Integrates changes from one branch into your current branch.

### 2. Resolving Merge Conflicts

*   **Concept:** Conflicts occur when Git cannot automatically merge changes because the same lines of code have been modified differently in two branches.
*   **Process:** Git will mark the conflicting sections. You manually edit the file to choose which changes to keep, then `git add` and `git commit` the resolved file.

### 3. Collaboration Workflow (Pull Requests)

*   **Forking:** Creating your own copy of someone else's repository on GitHub.
*   **Cloning:** Downloading your forked repository to your local machine.
*   **Making Changes:** Work on a new branch, commit your changes, and push them to your forked repository on GitHub.
*   **Pull Request (PR):** On GitHub, you open a Pull Request from your branch to the original repository's main branch. This is a request to merge your changes. Others can review your code, comment, and suggest changes.
*   **Review and Merge:** After review, the owner of the original repository can merge your changes.

### Realistic Example: Collaborating on a Data Cleaning Script

You are working with a colleague on a data cleaning script (`clean_data.py`).

1.  **Create a new branch:** `git checkout -b feature/data-cleaning-fix`
2.  **Make changes:** You modify `clean_data.py` to handle a new type of missing value.
3.  **Commit and Push:** `git add clean_data.py`, `git commit -m "Handle new missing value type"`, `git push origin feature/data-cleaning-fix`
4.  **Create a Pull Request:** On GitHub, you open a PR from your `feature/data-cleaning-fix` branch to `main`.
5.  **Colleague Reviews:** Your colleague reviews your code, suggests a minor change.
6.  **You make the change, commit, and push again.** The PR updates automatically.
7.  **Merge:** Your colleague approves and merges the PR into `main`.
8.  **Update your local main:** `git checkout main`, `git pull origin main` (to get your colleague's changes and your merged changes).

---

## 🟢 Strong Proficiency: Advanced Git Operations, Project Management, and Automation

At this level, you can use advanced Git commands for complex scenarios, leverage GitHub for project management, and integrate Git into automated workflows.

### 1. Advanced Git Operations

*   **`git rebase`:** Rewrites commit history. Used to integrate changes from one branch onto another by moving or combining commits. Can make history cleaner but should be used with caution, especially on shared branches.
*   **`git cherry-pick`:** Applies a specific commit from one branch to another.
*   **`git revert`:** Creates a new commit that undoes the changes of a previous commit (safer than `reset` for shared history).
*   **`git reset`:** Undoes changes by moving the HEAD pointer. Can be dangerous if used incorrectly on shared history.
*   **`git stash`:** Temporarily saves changes that are not ready to be committed, allowing you to switch branches and come back to them later.

### 2. GitHub for Project Management

*   **Issues:** Use GitHub Issues to track bugs, feature requests, and tasks. You can assign issues, add labels, and link them to pull requests.
*   **Projects (Kanban Boards):** Organize issues and pull requests into Kanban-style boards to visualize workflow and progress.
*   **Wikis:** Create documentation for your project directly within GitHub.
*   **Actions (CI/CD):** Automate workflows directly within your repository (e.g., run tests automatically when a new code is pushed, deploy a dashboard).

### 3. Integrating Git into Automated Workflows

*   **CI/CD (Continuous Integration/Continuous Deployment):** Using Git as the backbone for automated testing and deployment pipelines.
*   **Data Versioning:** While Git is great for code, it's not ideal for large datasets. However, understanding Git helps you understand the principles of data versioning tools (e.g., DVC - Data Version Control).

### Realistic Example: Automating a Data Pipeline with GitHub Actions

You have a Python script (`update_dashboard_data.py`) that cleans data and updates a CSV file that feeds a Power BI dashboard. You want this script to run automatically every time you push changes to the `main` branch.

**Your Approach (Strong Proficiency):**

1.  **Create a GitHub Actions Workflow:** In your repository, create a `.github/workflows` directory and add a YAML file (e.g., `data_pipeline.yml`).
2.  **Define the Workflow:**
    ```yaml
    name: Run Data Pipeline

on:
  push:
    branches:
      - main

jobs:
  run-script:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    - name: Install dependencies
      run: pip install pandas
    - name: Run data update script
      run: python update_dashboard_data.py
    # Add steps here to upload the updated CSV to Power BI or another location
    ```
3.  **Push Changes:** Every time you push a commit to the `main` branch, GitHub Actions will automatically run this workflow, executing your Python script.

This demonstrates how Git and GitHub extend beyond just code versioning to become powerful tools for automating and managing entire data projects, a key skill for a modern data analyst.
