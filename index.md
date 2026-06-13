---
layout: home
title: Home
---

Software developer writing about craft, apps, and things I learn along the way.

## Recent writing

<ul class="post-list home-list">
{% for post in site.posts limit:5 %}
  <li class="home-post-row">
    <a class="home-post-link" href="{{ post.url | relative_url }}">{{ post.title | escape }}</a>
    <span class="home-post-date">{{ post.date | date: "%b %d, %Y" }}</span>
  </li>
{% endfor %}
</ul>
