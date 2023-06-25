from collections import defaultdict
from datetime import date
import inspect


DATE_DAY_MONTH_FORMAT = "%b %d"
FRONT_PAGE_NAME = "index.html"


def get_episodes_by_year(episodes):
  episodes = sorted(episodes, key=lambda ep: ep.date, reverse=True)
  years = defaultdict(list)

  for episode in episodes:
    episode_html =inspect.cleandoc(f"""
    <li>
      <span class="episode-date">{episode.date.strftime(DATE_DAY_MONTH_FORMAT)}</span>
      <span class="intro">
        <a href="./{episode.name}.html">{episode.title}</a>
      </span>
    </li>\n""")

    years[episode.date.year].append(episode_html)
  return years


def build_front_page(episodes):
  episodes_by_year = get_episodes_by_year(episodes)
  current_year = str(date.today().year)

  html_string = inspect.cleandoc(f"""<html lang="en-us">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Norming</title>
    <link rel="stylesheet" type="text/css" href="main.css">
    </head>
    <body>
      <div class="content">
        <h1 class="title"><a href="./">∥<em>Norming</em>∥</a></h1>
        <div class="intro">
          <p>A succinct podcast about norms. One episode per month, 10 minutes per episode. No more, no less.</p>
        </div>
        <div class="episodes">
          {''.join(f'''
          <div>
            <h2>{year}</h2>
            <ul class="norming-episodes">
              {''.join(episode_html for episode_html in episodes)}
            </ul>
          </div>''' for year, episodes in episodes_by_year.items())
          }
        </div>
      </div>
      <footer>© {current_year} MMcA</footer>
    </body>
  </html>""")

  with open(FRONT_PAGE_NAME, "w") as html_file:
    html_file.write(html_string)
