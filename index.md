---
layout: home
title: Home
---

Software developer writing about craft, apps, and things I learn along the way.

<div class="currently">
  <span class="currently-label">Currently</span>
  <p class="currently-note">Building <a href="{{ '/soccer-mappr/' | relative_url }}">Soccer Mappr</a> after hours, and watching the World Cup by night — keeping a <a href="{{ '/worldcup26/' | relative_url }}">match diary</a> as the tournament unfolds.</p>
</div>

## Recent writing

{% assign recent = site.posts | where_exp: "post", "post.tags contains 'writes' or post.tags contains 'til'" %}
<ul class="post-list home-list">
{% for post in recent limit:5 %}
  <li class="home-post-row">
    <a class="home-post-link" href="{{ post.url | relative_url }}">{{ post.title | escape }}</a>
    <span class="home-post-date">{{ post.date | date: "%b %d, %Y" }}</span>
  </li>
{% endfor %}
</ul>
