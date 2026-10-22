---
layout: blogpost
tags: [writes]
title: "Branches were for code, worktrees are for context"
subtitle: ""
---

**One clone, one branch at a time**

For years, my Git setup was one clone per repository with a GUI client on top of it. First Sourcetree, later GitHub Desktop. I separated my work with branches, and switching between them was basically my whole workflow.

A typical interruption looked like this. I'm in the middle of a feature, a bug comes in on a release branch, so I stash my changes, switch the branch, wait for the rebuild, fix the bug, push, switch back, pop the stash and try to remember where I was. Switching is also a mental shift. It's not enough to remember where I stopped. I also have to bring back the thoughts and reasoning I had in that context.

It worked like this for years. But only one context could exist on my machine at a time, and every switch threw the previous one away.

**How AI moved me into the terminal**

I never decided to stop using the GUI. It happened as a side effect of working with an AI coding assistant in the terminal. The assistant reads the repo, runs the build, commits and splits branches in the same place I'm already working, so opening another app just to look at Git started to feel unnecessary.

Today I barely open a Git GUI. Things I used to click through, like splitting a large feature branch into smaller branches that are easier to review, I now describe in a sentence and then go through the changes and check the result.

This is also how I started using worktrees. I had an assistant session open on a feature when I needed to look at something on another branch. Switching branches would have changed the files under that session, so I created a worktree in a separate folder instead. It worked so well that it became my default.

Worktrees are not new, but I had never thought about doing this before, because these interruptions didn't happen that often. Now they do, and I wanted to handle them better.

**Worktrees in 30 seconds**

A worktree is an additional working directory attached to the same repository. All worktrees share one `.git` folder, so there are no extra clones and nothing to fetch twice. But each one has its own checked-out branch, its own files and its own build output.

These are the only commands I need:

```bash
# new directory next to the main clone, on a new branch
git worktree add ../app-versionNumber -b fix/some-bug origin/release/versionNumber

# an existing branch
git worktree add ../app-feature feature/some-feature

# a detached checkout of a specific commit, e.g. a pull request to review
git worktree add --detach ../app-review <commit>

# what do I have?
git worktree list

# done with it
git worktree remove ../app-review
git worktree prune
```

Since all worktrees share one repository, a commit made in any of them is immediately visible in all the others.

**My setup: one folder per context**

My work folder now has several worktrees of the same repository. Each one is a context I come back to, rather than a branch:

- **`app-name`:** the main clone.
- **`app-review`:** for reviewing pull requests, without touching my own work.
- **`app-versionNumber`:** for a version that uses different package versions and needs its own installations.
- **`app-feature`:** for a big story with many tickets. I switch between its related branches here, and my unstaged changes stay in the folder.

The version worktree was the one that convinced me. When a version uses different package versions, switching to it in a single clone means installing the packages again, and then installing them again when I switch back. With its own worktree, the installations stay in that folder, and I can go back to it without setting anything up.

The feature worktree is the one I use the most. A big story with many tickets means several related branches. When I switch between them in this worktree, my unstaged changes stay there. And when something else comes up, I don't stash anything. I leave the feature folder as it is and continue from there later.

**Parallel contexts, not parallel agents**

Most posts about worktrees and AI are about running many agents at the same time, each in its own worktree, and merging whatever they produce. That's not how I work.

For anything that needs my attention, I work synchronously. I stay in one context at a time, guide the assistant, read what it does and make the decisions myself. I don't send agents off to work in parallel without me watching, unless the task is clearly separate and won't pull my attention away.

What I do have is several contexts, and I switch between them when I reach a milestone. Before, switching meant closing one context and setting up the next one from scratch. Now it's just opening another folder.

When I come back to a worktree, everything is still there:

- the branch and my uncommitted changes
- the notes and logs I left there
- the terminal history and the assistant session from last time

The last one turned out to be more important than I expected. The assistant can continue where we left off, because the folder looks exactly the same as when we stopped. So a worktree keeps not only the code, but the whole state of the work.

For me, the benefit isn't doing more things at once. It's being able to focus: getting back into a context takes seconds, instead of digging through stashed changes and spending ten minutes trying to remember where I was.

**What to watch out for**

Worktrees also have some costs. These are the ones I ran into:

- **Disk space.** Git objects are shared, but build output isn't. Every worktree has its own build folders and dependency caches, and that adds up quickly.
- **One branch, one worktree.** Git doesn't let you check out the same branch in two worktrees. Usually that's what you want anyway, but it surprises you the first time.
- **Stale entries.** If you delete a worktree folder manually, Git still lists it. I found one of these in my own setup while writing this post. `git worktree prune` cleans it up, and using `git worktree remove` avoids the problem in the first place.
- **Setup per folder.** Local config, IDE launch settings and untracked files aren't shared between worktrees. A new worktree needs its dependencies fetched and sometimes a first full build.

**Branches for code, worktrees for context**

I used to see a branch as the work itself. Now I see it as only one part of it. The rest is the build, the notes, the unfinished experiment and the conversation with the assistant. Switching between contexts without worktrees throws that away. With a worktree for each context, everything stays where I left it.
