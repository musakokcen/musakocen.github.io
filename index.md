---
layout: home
title: Home
---

Software developer writing about craft, apps, my hobbies, and things I learn along the way.

<div class="currently">
  <span class="currently-label">Currently</span>
  <p class="currently-note">I'm building <a href="{{ '/soccer-mappr/' | relative_url }}">Soccer Mappr</a> in my spare time to bring my passions together.</p>
</div>

## Recent writing

{% assign writes_posts = site.posts | where_exp: "post", "post.tags contains 'writes'" %}
{% assign til_posts = site.posts | where_exp: "post", "post.tags contains 'til'" %}
{% assign recent = writes_posts | concat: til_posts | sort: 'date' | reverse %}
<ul class="post-list home-list">
{% for post in recent limit:5 %}
  <li class="home-post-row">
    <a class="home-post-link" href="{{ post.url | relative_url }}">{{ post.title | escape }}</a>
    <span class="home-post-date">{{ post.date | date: "%b %d, %Y" }}</span>
  </li>
{% endfor %}
</ul>
