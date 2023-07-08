import glob
from datetime import date, datetime
import frontmatter
import os
import shutil

from build.dataclasses import Episode
from build.episodes import build_episodes
from build.front_page import build_front_page
from build.rss import build_rss

EPISODE_PATH = "episodes"

def _copy_static_files():
  shutil.copytree("static", "public", dirs_exist_ok=True)
  src_files = os.listdir("static")
  for file_name in src_files:
      full_file_name = os.path.join("static", file_name)
      if os.path.isfile(full_file_name):
          shutil.copy(full_file_name, "public")

episodes = sorted([
  Episode.from_markdown(frontmatter.load(file_path), file_path)
  for file_path in glob.glob(f"{EPISODE_PATH}/*.md")
], key=lambda e: e.date, reverse=True)

build_episodes(episodes)
build_front_page(episodes)
build_rss(episodes)

_copy_static_files()
