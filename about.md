---
layout: default
title: About
permalink: /about/
---

# About Me

<p class="about-intro" style="font-size: 1.1rem; margin-bottom: 2rem;">
  Software developer based in Munich, focused on craft and building things that help people. Specialized in native iOS and, more recently, Flutter.
</p>

## Subscribe

<div class="subscribe-minimal" style="justify-content: flex-start; margin-bottom: 3rem;">
  <form action="https://your-newsletter-service.com/subscribe" method="post" target="_blank">
    <input type="email" name="email" placeholder="Subscribe to updates">
    <button type="submit">Subscribe</button>
  </form>
</div>

## Connect

<div class="social-links-list" style="margin-bottom: 3rem;">
  {% if site.github_username %}
    <a href="https://github.com/{{ site.github_username }}" style="margin-right: 1.5rem;">GitHub</a>
  {% endif %}
  {% if site.twitter_username %}
    <a href="https://twitter.com/{{ site.twitter_username }}" style="margin-right: 1.5rem;">Twitter</a>
  {% endif %}
  {% if site.linkedin_username %}
    <a href="https://linkedin.com/in/{{ site.linkedin_username }}" style="margin-right: 1.5rem;">LinkedIn</a>
  {% endif %}
</div>

## Contact

<p>
  Have a question or just want to say hi? <a href="mailto:{{ site.email }}">Send me an email</a>.
</p>
