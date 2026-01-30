<!--
  Auto-generated file. Do not edit directly.
  Edit /home/jcook/Documents/git_repo/cookiecutter-cookiecutter/docs/jekyll/README.md instead.
  Run ```make readme``` to regenerate this file
-->
<h1 id="cookiecutter-cookiecutter">cookiecutter-cookiecutter</h1>

<p><a href="LICENSE.md"><img src="https://img.shields.io/github/license/jcook3701/cookiecutter-cookiecutter" alt="License" /></a></p>

<p><strong>Author:</strong> Jared Cook<br />
<strong>Version:</strong> 0.1.0</p>

<h2 id="overview">Overview</h2>

<p><strong>cookiecutter-cookiecutter</strong> is the cookiecutter template project to rule them all. Generates cookiecutter template projects and is able to be queried by generated projects for updates.</p>

<p><strong>Utilizes:</strong><br />
The <strong>cookiecutter-cookiecutter</strong> depends on the following repositories for its documentation and sub-features.</p>
<ul>
  <li><a href="https://github.com/jcook3701/github-docs-cookiecutter">Github docs</a> cookiecutter template generation.</li>
  <li><a href="https://github.com/jcook3701/nutri-matic">Nutri-Matic</a> cookiecutter utilities for streamlining development and utilization of Cookiecutter templates.
<!-- * [Sphinx docs](https://github.com/jcook3701/sphinx-cookiecutter) template generation. --></li>
</ul>

<p><strong>Maintains:</strong><br />
The <strong>cookiecutter-cookiecutter</strong> is used to maintain the build and ci/cd structure for the following projects.</p>
<ul>
  <li><a href="https://github.com/jcook3701/github-docs-cookiecutter">github-docs-cookiecutter</a> Github docs cookiecutter template generation.</li>
  <li><a href="https://github.com/jcook3701/sphinx-cookiecutter">sphinx-cookiecutter</a> sphinx cookiecutter template generation.</li>
  <li><a href="https://github.com/jcook3701/ansible-galaxy-cookiecutter">ansible-galaxy-cookiecutter</a> Ansible Galaxy cookiecutter template + integration with Github docs cookiecutter template generation.</li>
  <li><a href="https://github.com/jcook3701/python3-cookiecutter">python3-cookiecutter</a> Python3 cookiecutter template project + Github docs cookiecutter template generation + Sphinx docs cookiecutter template generation.<br />
<!-- * [typescript-cookiecutter](https://github.com/jcook3701/typescript-cookiecutter) Typescript cookiecutter template project + Github docs cookiecutter template generation.  --></li>
</ul>

<hr />

<p><strong>CI/CD Check List:</strong></p>

<ul>
  <li><img src="https://github.com/jcook3701/cookiecutter-cookiecutter/actions/workflows/dependency-check.yml/badge.svg" alt="dependency-check" /></li>
  <li><img src="https://github.com/jcook3701/cookiecutter-cookiecutter/actions/workflows/format-check.yml/badge.svg" alt="format-check" /></li>
  <li><img src="https://github.com/jcook3701/cookiecutter-cookiecutter/actions/workflows/lint-check.yml/badge.svg" alt="lint-check" /></li>
  <li><img src="https://github.com/jcook3701/cookiecutter-cookiecutter/actions/workflows/security-audit.yml/badge.svg" alt="security-audit" /></li>
  <li><img src="https://github.com/jcook3701/cookiecutter-cookiecutter/actions/workflows/spellcheck.yml/badge.svg" alt="spellcheck" /></li>
  <li><img src="https://github.com/jcook3701/cookiecutter-cookiecutter/actions/workflows/tests.yml/badge.svg" alt="tests" /></li>
  <li><img src="https://github.com/jcook3701/cookiecutter-cookiecutter/actions/workflows/typecheck.yml/badge.svg" alt="typecheck" /></li>
</ul>

<hr />

<h2 id="usage-examples">Usage Examples</h2>

<p><strong>Example 1:</strong> Pull from main branch.<br />
<strong>Note:</strong> <a href="https://github.com/jcook3701/nutri-matic">Nutri-Matic</a> is needed in active python environment.</p>

<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>cookiecutter git@github.com:jcook3701/cookiecutter-cookiecutter.git <span class="se">\</span>
    <span class="nt">--no-input</span> <span class="se">\</span>
    <span class="nv">project_name</span><span class="o">=</span><span class="s2">"test-project"</span> <span class="se">\</span>
    <span class="nv">description</span><span class="o">=</span><span class="s2">"Cookiecutter test project."</span>
</code></pre></div></div>

<p><strong>Example 2:</strong> Pull from develop branch.</p>

<div class="language-shell highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nv">$ </span>cookiecutter git@github.com:jcook3701/cookiecutter-cookiecutter.git <span class="se">\</span>
    <span class="nt">--checkout</span> develop <span class="se">\</span>
     <span class="nt">--no-input</span> <span class="se">\</span>
    <span class="nv">project_name</span><span class="o">=</span><span class="s2">"test-project"</span> <span class="se">\</span>
    <span class="nv">description</span><span class="o">=</span><span class="s2">"Cookiecutter test project."</span>
</code></pre></div></div>

<p><strong>Note:</strong> replace <code class="language-plaintext highlighter-rouge">test-project</code> or any of the other variables with real context configuration variables.</p>

<hr />

<h2 id="getting-started">Getting Started</h2>

<ul>
  <li><a href="https://jcook3701.github.io/cookiecutter-cookiecutter/manual/setup-guide/requirements">Requirements</a></li>
  <li><a href="https://jcook3701.github.io/cookiecutter-cookiecutter/manual/introduction/installation-guide">Installation guide</a></li>
</ul>

<h2 id="documentation">Documentation</h2>

<p>The cookiecutter-cookiecutter documentation is available at <a href="https://jcook3701.github.io/cookiecutter-cookiecutter">docs</a>.</p>

<h2 id="contributing">Contributing</h2>

<p>If you’re interested in contributing to the cookiecutter-cookiecutter project:</p>
<ul>
  <li>Start by reading the <a href="https://jcook3701.github.io/cookiecutter-cookiecutter/manual/developer-resources/contribute">contributing guide</a>.</li>
  <li>Learn how to setup your local environment, in our <a href="https://jcook3701.github.io/cookiecutter-cookiecutter/manual/contribute/developer-guide">developer guide</a>.</li>
  <li>Look through our <a href="https://jcook3701.github.io/cookiecutter-cookiecutter/manual/contribute/style-guides/index">style guide</a>.</li>
</ul>

<hr />

<h2 id="authors-notes">Authors Notes</h2>
<ol>
  <li>This code is currently intended to work with cookiecutter (v2.6+) from PyPi repositories.</li>
</ol>

<h2 id="license">License</h2>

<p>Copyright (c) 2025-2026, Jared Cook</p>

<p>This project is licensed under the <strong>AGPL-3.0-or-later License</strong>.
See the <a href="https://github.com/jcook3701/cookiecutter-cookiecutter/blob/master/LICENSE.md">LICENSE</a> file for the full license text.</p>

<p>SPDX-License-Identifier: AGPL-3.0-or-later</p>

<!--
### Helpful Emojis:

📡🐋🛢️🚢 🦊💼 👨🏼‍💻🚧 📌 🌱🌳 ⏳🔑 🔫⌚ 🧼🧽 🔌💉

--->
