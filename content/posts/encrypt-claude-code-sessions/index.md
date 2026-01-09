---
date: '2026-01-09T12:07:08+02:00'
draft: false
title: 'Claude Code sessions should be encrypted'
categories:
  - Dev
tags:
  - claude code
  - security
  - privacy
---

Claude Code is exploding in popularity right now, and people are using it for **much more than writing code**. 

{{<x user="lennysan" id="1978130461596745856" >}}

Whether it's to <a href="https://harper.blog/2025/12/03/claude-code-email-productivity-mcp-agents/">manage your email</a>, write <a href="https://x.com/GergelyOrosz/status/1939940353617920038">peer performance feedback</a>, or even be your <a href="https://x.com/DanielleMorrill/status/2007508036584341899">Chief of Staff</a>—people are putting sensitive, personal information into Claude Code. And the more we use it for non-coding work, the more the session files are **valuable and private**[^1].

{{< tweet user="mollycantillon" id="2008918474006122936" text="THE PERSONAL PANOPTICON. A few months ago, I started running my life out of Claude Code. Not out of intention to do so, it was just the place where everything met. And it just kept working..." >}}

As a daily AI assistant, session data is no longer just code. It's your personal archive, and it's stored in **plain text**.

### The problem

Claude Code session files are stored in plain text in your user folder. Take a look at `~/.claude/projects` (mac/linux) or `%USERPROFILE%\.claude\projects` (windows). These files can be read by any software you run—including that npm package you (or Claude!) just installed.

This is basically <a href="https://cwe.mitre.org/data/definitions/312.html">CWE-312</a>: Cleartext Storage of Sensitive Information. 

> The product stores sensitive information in cleartext within a resource that might be accessible to another control sphere
>
> <cite>— [Common Weakness Enumeration](https://cwe.mitre.org/data/definitions/312.html)</cite>

### What should change

Session files should be **encrypted** at rest, with the key stored in the system keychain. The same way Claude's API keys are.

I say this reluctantly, because I've used the access more than once for my own projects (like <a href="https://absolutelyright.lol/">absolutelyright.lol</a> or an <a href="https://github.com/yoavf/ai-sessions-mcp">MCP server to share sessions between coding agents</a>). But the openness is now becoming a security gap.

[^1]: Written by a human who likes em dashes.