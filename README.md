# misc-notes [![netify notes](https://img.shields.io/badge/netify-notes-brightgreen.svg)](http://misc-notes.netlify.com/2020/01/13/%E6%9E%81%E7%AE%80vuejs%E5%85%A5%E9%97%A8/)

misc-notes is a Hexo-powered static blog that is published via Netlify. The repository contains both the Markdown content and the Hexo configuration and theme customisations used to generate the site. It is the working copy for the live site at [misc-notes.netlify.com](https://misc-notes.netlify.com/), which collects personal notes, quick references, and write-ups.

## Purpose

- Track the Markdown posts and accompanying assets that make up the misc-notes blog.
- Keep Hexo and NexT theme configuration in source control so the site can be rebuilt anywhere.
- Store helper scripts and docs for deploying the generated site via Netlify.

This repository is not a reusable theme or npm package; clone it if you want to examine or run the blog locally.

## Overview

- **Static site generator:** Hexo 4 (see `package.json`)
- **Theme:** NexT (Muse scheme) stored in `themes/next`
- **Deployment:** `hexo-deployer-git` pushes the generated site to Netlify
- **Content:** Markdown posts and assets live under `source/`

## Getting started

### Prerequisites
- Node.js 12 or newer
- npm (ships with Node)

### Install dependencies
```bash
npm install
```

### Run a local preview server
```bash
npm run server
```
Hexo serves the site at <http://localhost:4000> with live-reload.

### Clean and rebuild the site
```bash
npm run clean
npm run build
```

### Create new content
```bash
npx hexo new "Post Title"
npx hexo new page --path "page/path"
```

Generated Markdown files land in `source/_posts/` (or the specified page path). Each post receives an asset folder, so images and other files can be dropped alongside the post content.

## Deployment

The project uses `hexo-deployer-git` to push the generated `public/` directory to the branch that Netlify watches. Run:

```bash
npm run deploy
```

Ensure the deployment target is configured in `_config.yml` under the `deploy` section.

## Repository structure

- `_config.yml` – global Hexo configuration, permalink structure, plugins, etc.
- `source/` – blog posts, pages, and static assets.
- `scaffolds/` – templates used by `hexo new`.
- `themes/next/` – NexT theme with project-specific customisation.
- `rundown-memo.txt` – notes covering common Hexo, theme, and Netlify commands.

## Additional resources

- [Hexo documentation](https://hexo.io/docs/)
- [NexT theme documentation](https://theme-next.js.org/)
- [Netlify docs](https://docs.netlify.com/)
