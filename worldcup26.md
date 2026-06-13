---
layout: default
title: World Cup 26
permalink: /worldcup26/
---

My FIFA World Cup 2026 diary. Matches watched, moments, and notes from the tournament — logged as it happens, June 11 to July 19.

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
