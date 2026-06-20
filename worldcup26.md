---
layout: default
title: World Cup 26
permalink: /worldcup26/
---

My FIFA World Cup 2026 diary. I plan to log my thoughts on the tournament, the matches, and related moments.

<div class="diary">
{% for post in site.posts %}
{% if post.tags contains 'worldcup26' %}
  {%- comment -%}
    Diary kickoffs are logged in CEST (UTC+2). Jekyll renders post.date in the
    build machine's timezone (GitHub Pages builds in UTC), so derive the build
    offset from %z and shift the absolute epoch (%s) so the time is always shown
    as UTC+2 regardless of where the site is built.
  {%- endcomment -%}
  {%- assign tzraw = post.date | date: "%z" -%}
  {%- assign tz_sign = tzraw | slice: 0, 1 -%}
  {%- assign tz_h_secs = tzraw | slice: 1, 2 | times: 3600 -%}
  {%- assign tz_m_secs = tzraw | slice: 3, 2 | times: 60 -%}
  {%- assign build_off = tz_h_secs | plus: tz_m_secs -%}
  {%- if tz_sign == "-" -%}{%- assign build_off = 0 | minus: build_off -%}{%- endif -%}
  {%- assign shift = 7200 | minus: build_off -%}
  {%- assign kickoff = post.date | date: "%s" | plus: shift -%}
  <article class="diary-entry">
    <header class="diary-entry-head">
      <span class="diary-entry-match">{{ post.title | escape }}</span>
      <time class="diary-entry-time">{{ kickoff | date: "%-d %b · %H:%M" }} (UTC+2)</time>
    </header>
    <div class="diary-entry-body">
      {{ post.content }}
    </div>
  </article>
{% endif %}
{% endfor %}
</div>
