from datetime import date
from jinja2 import Environment, FileSystemLoader
import os

environment = Environment(loader=FileSystemLoader("templates/"))
STATIC_DIR = "public"

def get_html_string(episode):
  current_year = str(date.today().year)
  template = environment.get_template("post.html")

  return template.render(episode=episode, current_year=current_year)


def build_episodes(episodes):
    if not os.path.exists(STATIC_DIR):
      os.makedirs(STATIC_DIR)

    for episode in episodes:
      html_string = get_html_string(episode)

      with open(f"{STATIC_DIR}/{episode.name}.html", "w") as html_file:
        html_file.write(html_string)
