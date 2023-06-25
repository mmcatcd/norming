from dataclasses import dataclass
from datetime import datetime
import os

DATE_FORMAT = "%B %d, %Y"

@dataclass
class Episode:
  title: str
  date: datetime
  audio_file: str
  duration: str
  spotify: str
  description: str
  content: str
  file_path: str

  @staticmethod
  def from_markdown(md, file_path):
    return Episode(
      title=md["title"],
      date=md["date"],
      audio_file=md["audio_file"],
      duration=md["duration"],
      spotify=md["spotify"],
      description=md["description"],
      content=md.content,
      file_path=file_path,
    )
  
  @property
  def formatted_date(self):
    return self.date.strftime(DATE_FORMAT)
  
  @property
  def name(self):
    return os.path.basename(os.path.normpath(self.file_path)).replace(".md", "")
