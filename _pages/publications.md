---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---


{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

<style>
.archive__item-title a {
  pointer-events: none;
  cursor: default;
  text-decoration: none;
  color: inherit;
}
</style>

<div style="font-size: 0.7em;">
{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
</div>
