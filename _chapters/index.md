---
layout: default
title: Chapters
permalink: /chapters/
description: A directory of selected chapters from Mysticism Demystified — on perception, identity, structure, and self.
---

Below are selected chapter previews from *Mysticism Demystified*:

<ul>
  {% for chapter in site.chapters %}
    {% unless chapter.url == '/chapters/' %}
      <li><a href="{{ chapter.url }}">{{ chapter.title }}</a></li>
    {% endunless %}
  {% endfor %}
</ul>
