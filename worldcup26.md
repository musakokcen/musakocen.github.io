---
layout: default
title: World Cup 26
permalink: /worldcup26/
---

My FIFA World Cup 2026 diary. I plan to log my thoughts on the tournament, the matches, and related moments.

<ul class="post-list home-list">
    {% for post in site.posts %}
    {% if post.tags contains 'worldcup26' %}
    <li class="home-post-row">
        <a class="home-post-link" href="{{ post.url | relative_url }}">{{ post.title | escape }}</a>
        <span class="home-post-date">{{ post.date | date: "%b %d, %Y" }}</span>
    </li>
    {% endif %}
    {% endfor %}
</ul>
