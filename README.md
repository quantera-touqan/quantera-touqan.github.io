# TouQan  QuantERA Project Website

Source for the [quantera-touqan.github.io](https://quantera-touqan.github.io) website, built with [Pelican](https://getpelican.com/) and the [Flex](https://github.com/alexandrevicenzi/Flex) theme.

## Adding a news post

All posts live in `WebsiteFiles/content/posts/` as Markdown files. Copy an existing file as a template:

```markdown
Title: Your Post Title
Date: YYYY-MM-DD HH:MM
Slug: your-post-slug

Your content here.
```

Use `{static}/images/filename.jpg` to reference images placed in `WebsiteFiles/content/images/`.

## Local development

Requires Python and [Pelican](https://getpelican.com/):

```bash
pip install pelican[markdown]
cd WebsiteFiles
pelican content -s pelicanconf.py   # build
pelican --listen -o output          # serve at http://127.0.0.1:8000
```

## Deployment

Pushing to the `main` branch triggers a **GitHub Actions** workflow (`.github/workflows/deploy.yml`) that:

1. Builds the site using `publishconf.py`
2. Pushes the output to the `gh-pages` branch

GitHub Pages must be configured to serve from the `gh-pages` branch. No custom domain is needed — the site is served at `https://quantera-touqan.github.io`.
