---
title: "Training small models for fun and profit (the easy way)"
slug: training-small-models-for-fun-and-profit
author: Yoav
date: 2026-10-22T18:35:00+03:00
categories:
  - Dev
tags:
  - ai
  - models
---

Back in July 2026, Google announced they'll [retire the Gemini 2.5](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-versions) family on October 20th.

At [Base44](https://base44.com) we had one last feature that was still using Gemini 2.5 Flash Lite: autocomplete in the builder, called millions of times a day. We'd tried replacing it before, but nothing newer was fast enough. For autocomplete, a late suggestion is wasted: by the time it shows up, the user already typed past it.

Fast forward a few months - the model is about to get shut down, and we don't have a good alternative yet. 
What do we do? We train our own custom model of course!

Here's how we did it (in half a day):

### Step 1: Prepare the data (the hard part)

First, we needed training data. Luckily, autocomplete has a useful property: users often tell you exactly what they wanted by continuing to type. Those continuations give us real training targets, without relying on another model's output.

So we had ample data to begin with. It had to be cleaned up, of course: we removed <abbr title="Personally Identifiable Information">PII</abbr>, secrets, and all sorts of edge cases. 


### Step 2: Choose a model

First, we defined our expected usage and target cost. Then, we ran sample prompts on models that seemed to fit those requirements. We narrowed it down to a few, but for this specific use case, we quickly settled on [Qwen 3.5 2B](https://huggingface.co/Qwen/Qwen3.5-2B): it's a compact light model that's easy to train, cheap to serve, and fast to iterate on.


### Step 3: Train (the easy part)

Once we had our training data and base model, we used [serverless fine-tuning](https://docs.crusoecloud.com/serverless-fine-tuning/fine-tune-a-model/) from our friends at [Crusoe](https://crusoe.ai) (many providers offer similar SFT infra).

Each training run took around 20 minutes - and we did 5 in total, testing multiple variations on the training data to try and improve the results. In the end, we used the version from the 2nd run.

### Step 4: Deploy & Measure

Predicting a user's literal next words is not the same as writing a suggestion they'll accept. We built an acceptance grader, and then ran a quick feedback loop to verify that it actually predicts what users do.

After a quick A/B test (you'll reach significance fast when you're dealing with millions of requests per day) - we knew we had a winner.

### Results

- Latency: p50 of ~220ms, down from ~790ms (3.5× faster). p95: 460ms, down from 1,110ms.
- Next-word accuracy (grader): 41%, vs 29% for `gemini-2.5-flash-lite`.
- In the live A/B test: 52.6% of users accepted suggestions, up from 43.9%.

The interesting bit: the new model doesn't necessarily have to produce better suggestions every time. Because it's faster, it gets to show suggestions at more typing pauses. Even with a slightly lower acceptance rate per suggestion, more users end up accepting at least one.

**Total cost**: about $175.<br>
**Estimated savings**: around $300,000 a year at current usage.

### Gotchas

- **Inference becomes your job.** In most cases you'll need to start managing it yourself: providers bill by GPU hour for your own deployment, rather than per token.
- **No distillation shortcut.** You can't train on the existing big lab model's outputs. That's distillation, which most providers' terms of service forbid. You need data from real usage (or alternatively: distill from a larger open model with a permissive licence).
- **Evals are half the work.** Good data isn't enough: you also need a good way to tell good output from bad. Our acceptance grader (step 4) took as much effort as the training set.


### What's next

Autocomplete is just one example. We have hundreds of these small workloads in production, adding new ones almost daily. They all start on an off-the-shelf model from one of the providers we work with, but there's often an opportunity to do better on latency, quality, and cost with a small custom-trained model.

### Takeaway

<b>For a narrow, high-volume task where you already log inputs and real outcomes, a small fine-tuned model can beat the API it replaces on speed, cost, and quality.</b><br>The model is the easy part; the real work is data collection, measurement, and A/B infrastructure.

BTW, turns out I missed the memo: after the initial announcement, Google changed their mind and is keeping Gemini 2.5 for existing customers. Still, we ended up with a feature that's faster, cheaper, and measurably better. No regrets!
