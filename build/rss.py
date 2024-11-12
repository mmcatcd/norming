import inspect


RSS_NAME = "static/rss.xml"
RSS_DATE_FORMAT = "%a, %d %b %Y"
AUTHOR_EMAIL = "michael@corribdigital.com"


def build_rss(episodes):
  episodes_rss = []

  for episode in episodes:
    itunes_image = f'<itunes:image href="{episode.cover_art}"/>' if episode.cover_art else ""
    
    episodes_rss.append(inspect.cleandoc(f"""<item>
      <title>{episode.title}</title>
      <link>https://normi.ng/{episode.name}</link>
      <description>{episode.description}</description>
      <content:encoded>{episode.description}</content:encoded>
      <enclosure url="{episode.audio_file}" length="5484751" type="audio/mpeg"/>
      <guid isPermaLink="true">https://normi.ng/{episode.name}</guid>
      <pubDate>{episode.date.strftime(RSS_DATE_FORMAT)} 09:00:00 GMT</pubDate>
      {itunes_image}
      <itunes:duration>{episode.duration}</itunes:duration>
      <itunes:summary>{episode.description}</itunes:summary>
    </item>
    """)
    )

  rss_string = inspect.cleandoc(f"""<?xml version="1.0" encoding="UTF-8"?>
  <rss xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:content="http://purl.org/rss/1.0/modules/content/" xmlns:atom="http://www.w3.org/2005/Atom" version="2.0" xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd" xmlns:anchor="https://anchor.fm/xmlns">
    <channel>
      <title>Norming</title>
      <link>https://normi.ng</link>
      <description>A succinct podcast about norms. One episode per month, 10 minutes per episode. No more, no less.</description>
      <language>en-us</language>
      <copyright>Norming</copyright>
      <managingEditor>{AUTHOR_EMAIL} (Michael McAndrew)</managingEditor>
      <webMaster>{AUTHOR_EMAIL} (Michael McAndrew)</webMaster>
      <pubDate>Sat, 01 Oct 2022 12:07:00 GMT</pubDate>
      <lastBuildDate>Sat, 01 Oct 2022 12:07:00 GMT</lastBuildDate>
      <ttl>60</ttl>
      <image>
        <url>https://normi.ng/img/coverart.jpg</url>
        <title>Norming</title>
        <link>https://normi.ng</link>
      </image>
      <atom:link href="https://normi.ng/rss.xml" type="application/rss+xml" rel="self"/>
      <itunes:author>Michael McAndrew</itunes:author>
      <itunes:image href="https://normi.ng/img/coverart.jpg"/>
      <itunes:owner>
        <itunes:name>Michael McAndrew</itunes:name>
        <itunes:email>{AUTHOR_EMAIL}</itunes:email>
      </itunes:owner>
      <itunes:explicit>false</itunes:explicit>
      <itunes:category text="Technology"/>
      {''.join(episodes_rss)}
    </channel>
  </rss>
  """)

  with open(RSS_NAME, "w") as html_file:
    html_file.write(rss_string)
