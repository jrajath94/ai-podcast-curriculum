# episodes.json schema

```json
[
  {
    "rank": 1,
    "title": "Episode title (verbatim from YouTube)",
    "url": "https://www.youtube.com/watch?v=<video_id>",
    "video_id": "<video_id>",
    "view_count": 1234567,
    "upload_date": "20240115",
    "guest": "Guest Name",
    "duration_s": 7200,
    "topics": ["topic1", "topic2", "topic3"],
    "transcript_file": "transcripts/<video_id>.txt"
  }
]
```

- `view_count`: integer from `yt-dlp --print %(view_count)s`, October 2026 or later. Never estimated.
- `upload_date`: YYYYMMDD from `%(upload_date)s`.
- `topics`: 3–6 lowercase tags naming what the episode is substantively about.
- Optional: `"mandatory": true` for user-required episodes included regardless of rank.
