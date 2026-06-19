---
layout: default
title: World Cup 26
permalink: /worldcup26/
---

My FIFA World Cup 2026 diary. I plan to log my thoughts on the tournament, the matches, and related moments.

<div class="diary">
{% for post in site.posts %}
{% if post.tags contains 'worldcup26' %}
  <article class="diary-entry">
    <header class="diary-entry-head">
      <span class="diary-entry-match">{{ post.title | escape }}</span>
      <time class="diary-entry-time">{{ post.date | date: "%-d %b · %H:%M" }} (UTC{{ post.date | date: "%z" | replace: "+0", "+" | replace: "-0", "-" | slice: 0, 2 }})</time>
    </header>
    <div class="diary-entry-body">
      {{ post.content }}
    </div>
  </article>
{% endif %}
{% endfor %}
</div>
