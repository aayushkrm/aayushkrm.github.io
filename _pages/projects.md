---
layout: page
title: Projects
permalink: /projects/
description: Research and engineering projects spanning agentic AI, genomics, efficient ML, and backend systems.
nav: true
nav_order: 2
display_categories: [research, work]
horizontal: false
---

<!-- pages/projects.md -->
<div class="projects">
  {% if site.enable_project_categories and page.display_categories %}
    {% for category in page.display_categories %}
      <h2 class="sec-title" id="{{ category }}">{{ category | capitalize }}</h2>
      {% assign categorized_projects = site.projects | where: 'category', category %}
      {% assign sorted_projects = categorized_projects | sort: 'importance' %}
      <ul class="entries">
        {% for project in sorted_projects %}
          {% include projects.liquid %}
        {% endfor %}
      </ul>
    {% endfor %}
  {% else %}
    {% assign sorted_projects = site.projects | sort: 'importance' %}
    <ul class="entries">
      {% for project in sorted_projects %}
        {% include projects.liquid %}
      {% endfor %}
    </ul>
  {% endif %}
</div>
