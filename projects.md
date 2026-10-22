---
layout: work
title: "Projects"
permalink: /projects/
---

{% assign qb = site.posts | where_exp: "p", "p.url contains 'releasingQuizBurger'" | first %}
{% assign sm = site.posts | where_exp: "p", "p.url contains 'learningSoccerHeatmap'" | first %}
{% assign wc = site.posts | where_exp: "p", "p.url contains 'building-world-cup-diaries' " | first %}

<div class="mk-wide mk-grid-page" markdown="0">

  <header class="mk-hero">
    <h2 class="mk-eyebrow">Independent products</h2>
    <p class="mk-lede">Native apps I design, build and ship on my own, from product definition to App Store release. Each privacy-first, and each with a write-up on the blog.</p>
  </header>

  <div class="mk-grid">
    <article class="mk-card">
      <div class="mk-card-top">
        <img class="mk-card-icon" src="/assets/img/soccer-mappr/icon.png" alt="Heatiz icon">
        <span class="mk-status mk-status-live">Live</span>
      </div>
      <h3>Heatiz</h3>
      <p class="mk-card-desc">An Apple Watch match tracker that turns your GPS into a pitch heatmap. With goals, assists, positions and shareable cards. SwiftUI, HealthKit & CloudKit.</p>
      <div class="mk-card-links">
        <a class="mk-btn mk-btn-primary" href="https://apps.apple.com/app/apple-store/id6761580343?pt=124242658&ct=801i6&mt=8" target="_blank" rel="noopener">App Store ↗</a>
        <a class="mk-btn" href="/heatiz/">Overview</a>
      </div>
    </article>

    <article class="mk-card">
      <div class="mk-card-top">
        <img class="mk-card-icon" src="/assets/img/einbuergerungstest/icon.webp" alt="Einbürgerungstest icon">
        <span class="mk-status mk-status-live">Live</span>
      </div>
      <h3>Einbürgerungstest</h3>
      <p class="mk-card-desc">Prepare for the German naturalization exam with all 300+ official questions, a timed real-test simulation, multilingual translations and mistake tracking. Fully offline.</p>
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
      <h3>World Cup Diaries</h3>
      <p class="mk-card-desc">A SwiftUI diary app for the 2026 World Cup. Write (or speak) a note on a match and it publishes straight to my blog. Built with Xcode 27’s agent-driven Intelligence.</p>
      <div class="mk-card-links">
        <a class="mk-btn mk-btn-primary" href="/worldcup26/">Diary</a>
        <a class="mk-btn" href="https://github.com/musakokcen/WWDCWorldCup2026" target="_blank" rel="noopener">Source ↗</a>
        {% if wc %}<a class="mk-btn" href="{{ wc.url | relative_url }}">Story</a>{% endif %}
      </div>
    </article>
  </div>

  <header class="mk-hero mk-hero-next">
    <h2 class="mk-eyebrow">Work shipped with teams</h2>
    <p class="mk-lede">Applications I have shipped with teams, in full-time and freelance roles, across large-scale consumer platforms, telephony, sports and productivity domains. Deep native iOS work in Swift, SwiftUI and Objective-C, plus Android delivery with Flutter.</p>
  </header>

  <div class="project-list">
  <div class="project-item">
      <div class="project-icon">
          <img src="/assets/img/planty.webp" alt="Planty" loading="lazy">
      </div>
      <div class="project-details">
        <h3>Planty: Plant Identifier, Care <a href="https://apps.apple.com/gb/app/planty-plant-identifier-care/id1603599822" target="_blank">↗</a></h3>
        <p>Planty is a plant care guide and companion app that helps you identify plants around you, find information, and set up care reminders for any plant. <i>*** Featured by Apple in the App Store ***</i></p>
      </div>
  </div>

  <div class="project-item">
      <div class="project-icon">
          <img src="/assets/img/goodRec.webp" alt="GoodRec" loading="lazy">
      </div>
      <div class="project-details">
        <h3>GoodRec (ex Just Play) <a href="https://apps.apple.com/gb/app/goodrec-ex-just-play/id1510554246" target="_blank">↗</a></h3>
        <p>Play sports games near you, regardless of your skill level or gender. Filter by city and sport, sign up for a game, and play.</p>
      </div>
  </div>

  <div class="project-item">
      <div class="project-icon">
          <img src="/assets/img/mathhero.webp" alt="Math AI" loading="lazy">
      </div>
      <div class="project-details">
        <h3>Math AI: Problem Solver Helper <a href="https://apps.apple.com/gb/app/math-ai-problem-solver-helper/id1565102390" target="_blank">↗</a></h3>
        <p>A step-by-step math solver app for everything from simple arithmetic to advanced algebra and calculus. You can enter questions by scanning or using a LaTeX keyboard.</p>
      </div>
  </div>

  <div class="project-item">
      <div class="project-icon">
          <img src="/assets/img/easyScanner.webp" alt="Easy Scanner" loading="lazy">
      </div>
      <div class="project-details">
        <h3>Easy Scanner PDF Document Scan <a href="https://apps.apple.com/gb/app/easy-scanner-pdf-document-scan/id1180773759" target="_blank">↗</a></h3>
        <p>Scan documents and save them as multi-page, high-quality PDF, JPEG, or TXT files. Documents can be emailed, printed, faxed, exported to the camera roll, or uploaded to cloud services.</p>
      </div>
  </div>


  <div class="project-item">
      <div class="project-icon">
          <img src="/assets/img/LVS.webp" alt="LVStudio" loading="lazy">
      </div>
      <div class="project-details">
        <h3>LVStudio <a href="https://apps.apple.com/us/app/lvstudio/id1497816078" target="_blank">↗</a></h3>
        <p>Live View Studio (LVStudio) is an advanced suite for visual learning of physical skills, such as playing golf.</p>
      </div>
  </div>

  <div class="project-item">
      <div class="project-icon">
          <img src="/assets/img/ws.svg" alt="WannaShoot" loading="lazy" class="project-icon-light">
      </div>
      <div class="project-details">
        <h3>WannaShoot</h3>
        <p>A photographer app to record videos and photos of models remotely.</p> <i>discontinued after the pandemic</i>*
      </div>
  </div>

  <div class="project-item">
      <div class="project-icon">
          <img src="/assets/img/xbotgo.webp" alt="XbotGo" loading="lazy">
      </div>
      <div class="project-details">
        <h3>Blink Focus Xbot Go <a href="https://apps.apple.com/tm/app/xbotgo/id1581355712" target="_blank">↗</a></h3>
        <p>Smartphone-based auto-tracking and recording system for team sports videos.</p>
      </div>
  </div>
  </div>

</div>
