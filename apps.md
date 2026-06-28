---
layout: work
title: "Side projects"
permalink: /apps/
---

{% assign qb = site.posts | where_exp: "p", "p.url contains 'releasingQuizBurger'" | first %}
{% assign sm = site.posts | where_exp: "p", "p.url contains 'learningSoccerHeatmap'" | first %}
{% assign wc = site.posts | where_exp: "p", "p.url contains 'building-world-cup-diaries' " | first %}

<div class="mk-wide mk-grid-page" markdown="0">

  <header class="mk-hero">
    <p class="mk-eyebrow">Side projects</p>
    <h1>Apps I build on the side</h1>
    <p class="mk-lede">Native apps I design and ship in my spare time — each privacy-first, and each with a write-up on the blog.</p>
  </header>

  <div class="mk-grid">

    <article class="mk-card">
      <div class="mk-card-top">
        <img class="mk-card-icon" src="/assets/img/soccer-mappr/icon.png" alt="Soccer Mappr icon">
        <span class="mk-status mk-status-live">Live</span>
      </div>
      <h2>Soccer Mappr</h2>
      <p class="mk-card-desc">An Apple Watch match tracker that turns your GPS into a pitch heatmap — with goals, assists, positions and shareable cards. SwiftUI, HealthKit & CloudKit.</p>
      <div class="mk-card-links">
        <a class="mk-btn mk-btn-primary" href="https://apps.apple.com/us/app/soccer-mappr/id6761580343" target="_blank" rel="noopener">App Store ↗</a>
        <a class="mk-btn" href="/soccer-mappr/">Overview</a>
        {% if sm %}<a class="mk-btn" href="{{ sm.url | relative_url }}">Story</a>{% endif %}
      </div>
    </article>

    <article class="mk-card">
      <div class="mk-card-top">
        <img class="mk-card-icon" src="/assets/img/einbuergerungstest/icon.webp" alt="Einbürgerungstest icon">
        <span class="mk-status mk-status-live">Live</span>
      </div>
      <h2>Einbürgerungstest</h2>
      <p class="mk-card-desc">Prepare for the German naturalization exam with all 300+ official questions, a timed real-test simulation, multilingual translations and mistake tracking — fully offline.</p>
      <div class="mk-card-links">
        <a class="mk-btn mk-btn-primary" href="https://apps.apple.com/us/app/quiz-b%C3%BCrger-lid-2026/id6758575798" target="_blank" rel="noopener">App Store ↗</a>
        <a class="mk-btn" href="/einbuergerungstest/">Overview</a>
        {% if qb %}<a class="mk-btn" href="{{ qb.url | relative_url }}">Story</a>{% endif %}
      </div>
    </article>

    <article class="mk-card">
      <div class="mk-card-top">
        <div class="mk-card-icon mk-icon-fallback" aria-hidden="true">⚽</div>
        <span class="mk-status mk-status-wip">Personal</span>
      </div>
      <h2>World Cup Diaries</h2>
      <p class="mk-card-desc">A SwiftUI diary app for the 2026 World Cup — write (or speak) a note on a match and it publishes straight to my blog. Built with Xcode 27’s agent-driven Intelligence.</p>
      <div class="mk-card-links">
        <a class="mk-btn mk-btn-primary" href="/worldcup26/">Diary</a>
        <a class="mk-btn" href="https://github.com/musakokcen/WWDCWorldCup2026" target="_blank" rel="noopener">Source ↗</a>
        {% if wc %}<a class="mk-btn" href="{{ wc.url | relative_url }}">Story</a>{% endif %}
      </div>
    </article>

  </div>

</div>
