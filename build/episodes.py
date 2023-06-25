from datetime import date

def get_html_string(episode):
  current_year = str(date.today().year)
  return f"""<html lang="en-us">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Norming</title>
    <link rel="stylesheet" type="text/css" href="main.css">
  </head>
  <body>
    <div class="content">
      <h1 class="title"><a href="./">∥<em>Norming</em>∥</a></h1>
      <date>{episode.formatted_date}</date>
      <h2>{episode.title}</h2>
      <div>
        <iframe style="border-radius:12px" src="{episode.spotify}" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
      </div>
      <br />
      <div class="episode-content">{episode.content}</div>
    </div>
    <footer>© {current_year} MMcA</footer>
  </body>
</html>"""

def build_episodes(episodes):
    for episode in episodes:
      html_string = get_html_string(episode)

      with open(f"{episode.name}.html", "w") as html_file:
        html_file.write(html_string)
