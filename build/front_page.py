from collections import defaultdict
from datetime import date
import inspect
from jinja2 import Environment, FileSystemLoader


environment = Environment(loader=FileSystemLoader("templates/"))
DATE_DAY_MONTH_FORMAT = "%b %d"
FRONT_PAGE_NAME = "index.html"


def get_episodes_by_year(episodes):
  episodes = sorted(episodes, key=lambda ep: ep.date, reverse=True)
  years = defaultdict(list)

  for episode in episodes:
    years[episode.date.year].append(episode)
  return years


def build_front_page(episodes):
  episodes_by_year = get_episodes_by_year(episodes)
  current_year = str(date.today().year)

  template = environment.get_template("index.html")
  html_string = template.render(episodes_by_year=episodes_by_year, current_year=current_year, date_format=DATE_DAY_MONTH_FORMAT)

  with open(f"public/{FRONT_PAGE_NAME}", "w") as html_file:
    html_file.write(html_string)
