---
layout: writing
title: Posts
permalink: /writes/
---

<p class="section-intro">Longer pieces on building software.</p>

<ul class="post-list home-list">
    {% for post in site.posts %}
    {% if post.tags contains 'writes' %}
    <li class="home-post-row">
        <a class="home-post-link" href="{{ post.url | relative_url }}">{{ post.title | escape }}</a>
        <span class="home-post-date">{{ post.date | date: "%b %d, %Y" }}</span>
    </li>
    {% endif %}
    {% endfor %}
</ul>
