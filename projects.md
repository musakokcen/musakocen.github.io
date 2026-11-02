---
layout: work
title: "Projects"
permalink: /projects/
---

{% assign hz = site.posts | where_exp: "p", "p.url contains 'whyIBuiltHeatiz'" | first %}
{% assign qb = site.posts | where_exp: "p", "p.url contains 'releasingQuizBurger'" | first %}
{% assign wc = site.posts | where_exp: "p", "p.url contains 'building-world-cup-diaries' " | first %}

<div class="project-page" markdown="0">

  <section class="project-section">
    <h2>Independent products</h2>
    <p class="projects-intro">Native apps I design, build and ship on my own, from product definition to App Store release. Each privacy-first, and each with a write-up on the blog.</p>
    <div class="project-list">
      <article class="project-item">
        <div class="project-icon">
          <img src="/assets/img/soccer-mappr/icon.png" alt="" width="60" height="60">
        </div>
        <div class="project-details">
          <h3>Heatiz</h3>
          <p>An Apple Watch match tracker that turns your GPS into a pitch heatmap. With goals, assists, positions and shareable cards. SwiftUI, HealthKit &amp; CloudKit.</p>
          <p class="project-links">
            <a href="https://apps.apple.com/app/apple-store/id6761580343?pt=124242658&amp;ct=801i6&amp;mt=8" target="_blank" rel="noopener">App Store ↗</a>
            <a href="/heatiz/">Overview</a>
            {% if hz %}<a href="{{ hz.url | relative_url }}">Story</a>{% endif %}
          </p>
        </div>
      </article>

      <article class="project-item">
        <div class="project-icon">
          <img src="/assets/img/einbuergerungstest/icon.webp" alt="" width="60" height="60">
        </div>
        <div class="project-details">
          <h3>Einbürgerungstest</h3>
          <p>Prepare for the German naturalization exam with all 300+ official questions, a timed real-test simulation, multilingual translations and mistake tracking. Fully offline.</p>
          <p class="project-links">
            <a href="https://apps.apple.com/us/app/quiz-b%C3%BCrger-lid-2026/id6758575798" target="_blank" rel="noopener">App Store ↗</a>
            <a href="/einbuergerungstest/">Overview</a>
            {% if qb %}<a href="{{ qb.url | relative_url }}">Story</a>{% endif %}
          </p>
        </div>
      </article>

      <article class="project-item">
        <div class="project-icon">
          <img src="/assets/img/worldCupDiaries.png" alt="" width="60" height="60">
        </div>
        <div class="project-details">
          <h3>World Cup Diaries</h3>
          <p>A SwiftUI diary app for the 2026 World Cup. Write (or speak) a note on a match and it publishes straight to my blog. Built with Xcode 27’s agent-driven Intelligence.</p>
          <p class="project-links">
            <a href="/worldcup26/">Diary</a>
            <a href="https://github.com/musakokcen/WWDCWorldCup2026" target="_blank" rel="noopener">Source ↗</a>
            {% if wc %}<a href="{{ wc.url | relative_url }}">Story</a>{% endif %}
          </p>
        </div>
      </article>
    </div>
  </section>

  <section class="project-section">
    <h2>Work shipped with teams</h2>
    <p class="projects-intro">Applications I have shipped with teams, in full-time and freelance roles, across large-scale consumer platforms, telephony, sports and productivity domains. Deep native iOS work in Swift, SwiftUI and Objective-C, plus Android delivery with Flutter.</p>
    <div class="project-list">
      <article class="project-item">
        <div class="project-icon">
          <img src="/assets/img/planty.webp" alt="" width="60" height="60" loading="lazy">
        </div>
        <div class="project-details">
          <h3>Planty: Plant Identifier, Care</h3>
          <p>Planty is a plant care guide and companion app that helps you identify plants around you, find information, and set up care reminders for any plant.</p>
          <p class="project-links">
            <a href="https://apps.apple.com/gb/app/planty-plant-identifier-care/id1603599822" target="_blank" rel="noopener">App Store ↗</a>
            <span class="project-note">Featured by Apple in the App Store</span>
          </p>
        </div>
      </article>

      <article class="project-item">
        <div class="project-icon">
          <img src="/assets/img/goodRec.webp" alt="" width="60" height="60" loading="lazy">
        </div>
        <div class="project-details">
          <h3>GoodRec (ex Just Play)</h3>
          <p>Play sports games near you, regardless of your skill level or gender. Filter by city and sport, sign up for a game, and play.</p>
          <p class="project-links">
            <a href="https://apps.apple.com/gb/app/goodrec-ex-just-play/id1510554246" target="_blank" rel="noopener">App Store ↗</a>
          </p>
        </div>
      </article>

      <article class="project-item">
        <div class="project-icon">
          <img src="/assets/img/mathhero.webp" alt="" width="60" height="60" loading="lazy">
        </div>
        <div class="project-details">
          <h3>Math AI: Problem Solver Helper</h3>
          <p>A step-by-step math solver app for everything from simple arithmetic to advanced algebra and calculus. You can enter questions by scanning or using a LaTeX keyboard.</p>
          <p class="project-links">
            <a href="https://apps.apple.com/gb/app/math-ai-problem-solver-helper/id1565102390" target="_blank" rel="noopener">App Store ↗</a>
          </p>
        </div>
      </article>

      <article class="project-item">
        <div class="project-icon">
          <img src="/assets/img/easyScanner.webp" alt="" width="60" height="60" loading="lazy">
        </div>
        <div class="project-details">
          <h3>Easy Scanner PDF Document Scan</h3>
          <p>Scan documents and save them as multi-page, high-quality PDF, JPEG, or TXT files. Documents can be emailed, printed, faxed, exported to the camera roll, or uploaded to cloud services.</p>
          <p class="project-links">
            <a href="https://apps.apple.com/gb/app/easy-scanner-pdf-document-scan/id1180773759" target="_blank" rel="noopener">App Store ↗</a>
          </p>
        </div>
      </article>

      <article class="project-item">
        <div class="project-icon">
          <img src="/assets/img/LVS.webp" alt="" width="60" height="60" loading="lazy">
        </div>
        <div class="project-details">
          <h3>LVStudio</h3>
          <p>Live View Studio (LVStudio) is an advanced suite for visual learning of physical skills, such as playing golf.</p>
          <p class="project-links">
            <a href="https://apps.apple.com/us/app/lvstudio/id1497816078" target="_blank" rel="noopener">App Store ↗</a>
          </p>
        </div>
      </article>

      <article class="project-item">
        <div class="project-icon">
          <img src="/assets/img/ws.svg" alt="" class="project-icon-light" width="60" height="60" loading="lazy">
        </div>
        <div class="project-details">
          <h3>WannaShoot</h3>
          <p>A photographer app to record videos and photos of models remotely.</p>
          <p class="project-links">
            <span class="project-note">Discontinued after the pandemic</span>
          </p>
        </div>
      </article>

      <article class="project-item">
        <div class="project-icon">
          <img src="/assets/img/xbotgo.webp" alt="" width="60" height="60" loading="lazy">
        </div>
        <div class="project-details">
          <h3>Blink Focus Xbot Go</h3>
          <p>Smartphone-based auto-tracking and recording system for team sports videos.</p>
          <p class="project-links">
            <a href="https://apps.apple.com/tm/app/xbotgo/id1581355712" target="_blank" rel="noopener">App Store ↗</a>
          </p>
        </div>
      </article>
    </div>
  </section>

</div>
