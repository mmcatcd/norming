import glob
from datetime import date, datetime
import frontmatter

from build.dataclasses import Episode
from build.episodes import build_episodes
from build.front_page import build_front_page
from build.rss import build_rss

EPISODE_PATH = "episodes"

episodes = sorted([
  Episode.from_markdown(frontmatter.load(file_path), file_path)
  for file_path in glob.glob(f"{EPISODE_PATH}/*.md")
], key=lambda e: e.date, reverse=True)

build_episodes(episodes)
build_front_page(episodes)
build_rss(episodes)
