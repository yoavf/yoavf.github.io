---
title: "Projects"
ShowReadingTime: false
ShowShareButtons: false
ShowPostNavLinks: false
ShowBreadCrumbs: false
ShowCodeCopyButtons: false
hidemeta: true
showtoc: false
---

[metrics.help](#metricshelp) • [prompet.ai](#prompetai) • [aisessions.dev](#aisessionsdev) • [AI Sessions MCP](#ai-sessions-mcp) • [pair.guide](#pairguide) • [Pair](#pair) • [absolutelyright.lol](#absolutelyrightlol) • [Auto PR Screenshots](#auto-pr-screenshots)

---

## [metrics.help](https://metrics.help)
*November 2025*

<a href="https://metrics.help"><img src="https://metrics.help/og/home.png" alt="metrics.help" width="250"></a>

A quick reference for understanding ML training metrics. Paste your log lines and get explanations and links for the metrics you're seeing.

Some metrics include graphs showing what healthy vs unhealthy progressions look like, helping you diagnose training runs at a glance.

[Visit Site](https://metrics.help)

---

## [prompet.ai](https://prompet.ai)
*November 2025*

<a href="https://prompet.ai"><img src="https://yoavf.github.io/prompet.ai/assets/og-image.png" alt="prompet.ai" width="250"></a>

An experiment in reinforcement learning: can a small vision-language model teach itself to draw?

I wired up a RL loop where Qwen3-VL (8B) generated SVG illustrations of cute pets, then rated those illustrations (converted to PNGs) on various criteria. The model acts as both creator and critic, iteratively improving its output through self-evaluation.

[Visit Site](https://prompet.ai)

---

## [aisessions.dev](https://aisessions.dev)
*October 2025*

<a href="https://aisessions.dev"><img src="https://aisessions.dev/opengraph-image?9a47dc8749dd6c69" alt="aisessions.dev" width="250"></a>

A web platform for sharing AI coding sessions with the world. Upload and publish transcripts from Claude Code, Codex, and other AI coding assistants.

Built to make it easy for developers to showcase their AI-assisted development workflows, learn from each other's sessions, and share interesting coding conversations. Inspired by [Amp](https://ampcode.com)'s approach to sharing AI sessions.

[View on GitHub](https://github.com/yoavf/ai-sessions) • [Visit Site](https://aisessions.dev)

---

## [AI Sessions MCP](https://github.com/yoavf/ai-sessions-mcp)
*October 2025*

<a href="https://github.com/yoavf/ai-sessions-mcp"><img src="https://repository-images.githubusercontent.com/1067867411/7942522a-4ee1-4e9c-b102-c8c7668a7f71" alt="AI Sessions MCP" width="250"></a>

A Model Context Protocol (MCP) server that provides access to your AI assistant CLI sessions from Claude Code, Gemini CLI, OpenAI Codex, and opencode.

Allows AI tools to search, list, and read your previous local coding sessions. Useful for finding past solutions, reviewing recent work, learning from previous conversations, and resuming interrupted tasks.

[View on GitHub](https://github.com/yoavf/ai-sessions-mcp)

---

## [pair.guide](https://pair.guide)
*September 2025*

<a href="https://pair.guide"><img src="https://pair.guide/og-image.png" alt="pair.guide" width="250"></a>

Notes on pair-coding with AI (previously humans.md). Bite-sized, practical lessons from coding with AI agents like Claude Code, Codex, and others.

[View on GitHub](https://github.com/yoavf/humans.md) • [Visit Site](https://pair.guide)

---

## [Pair](https://yoav.blog/pair)
*September 2025*

<a href="https://github.com/yoavf/pair"><img src="https://repository-images.githubusercontent.com/1051971878/a59fe8e3-41e6-43cf-a328-3fe3b34702d7" alt="Pair" width="250"></a>

A CLI utility that orchestrates coding agents working together in a pair programming session. The navigator and driver roles can each run on different providers, using the SDKs from Claude Code and opencode.

Features:
- Two-agent collaboration with distinct navigator and driver roles
- Multi-provider and multi-model (Claude Code, opencode)
- Flexible model configuration per role

[View on GitHub](https://github.com/yoavf/pair)

---

## [absolutelyright.lol](https://absolutelyright.lol)
*September 2025*

<a href="https://absolutelyright.lol"><img src="/images/projects/absolutelyright.png" alt="absolutelyright.lol" width="250"></a>

A scientifically rigorous tracking system for how often Claude Code validates my life choices.

Tracks how many times Claude Code says "absolutely right" vs just "right" in coding sessions. Built with Rust (Axum + SQLite backend), HTML/JS frontend with "hand-drawn" charts, and Python scripts for collecting data from Claude Code sessions.

[View on GitHub](https://github.com/yoavf/absolutelyright.lol) • [Visit Site](https://absolutelyright.lol)

---

## [Auto PR Screenshots](https://github.com/yoavf/auto-pr-screenshots-action)
*August 2025*

<a href="https://github.com/yoavf/auto-pr-screenshots-action"><img src="https://opengraph.githubassets.com/e151d96d1c2a1beff6e9e1c388bc61ab6bdd4334f9dffca0fb88e1dac86e3df3/yoavf/auto-pr-screenshots-action" alt="Auto PR Screenshots" width="250"></a>

A GitHub Action that automatically captures and posts screenshots of your web app to pull requests. Perfect when using AI tools to create PRs, making it easy to visually see the changes.

Features:
- Smart PR comments that update with each push
- Simple setup with minimal configuration

[View on GitHub](https://github.com/yoavf/auto-pr-screenshots-action)
