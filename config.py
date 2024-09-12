import re
import random
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", None))

# Get this value from @MissRose_Bot on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", None))

# Fill Queue Limit . Example - 15
QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", "10"))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://te.legra.ph/file/4226cedbc4b0b34be0da8.jpg",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/sex_video_leaks")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/sex_video_leaks")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = ["https://envs.sh/PNj.mp4", "https://envs.sh/PNc.mp4", "https://envs.sh/PNZ.mp4", "https://envs.sh/PN4.mp4", "https://envs.sh/PNl.mp4", "https://envs.sh/PN8.mp4", "https://envs.sh/PN7.mp4", "https://envs.sh/PNJ.mp4", "https://envs.sh/PNZ.mp4", "https://envs.sh/PNH.mp4", "https://envs.sh/PNf.mp4", "https://envs.sh/PNO.mp4", "https://envs.sh/PNm.mp4", "https://envs.sh/PNM.mp4", "https://envs.sh/PNM.mp4"]
STATS_IMG_URL = ["https://envs.sh/PNI.jpg", "https://envs.sh/PNB.jpg", "https://envs.sh/PNq.jpg", "https://envs.sh/P_d.jpg", "https://envs.sh/Pc3.jpg", "https://envs.sh/PNq.jpg", "https://envs.sh/P_2.jpg"]
PLAYLIST_IMG_URL = getenv(
    "PLAYLIST_IMG_URL", "https://envs.sh/PHd.jpg"
)
TELEGRAM_AUDIO_URL = getenv(
    "TELEGRAM_AUDIO_URL", "https://envs.sh/PHh.jpg"
)
TELEGRAM_VIDEO_URL = getenv(
    "TELEGRAM_VIDEO_URL", "https://envs.sh/PHQ.jpg"
)
STREAM_IMG_URL = getenv(
    "STREAM_IMG_URL", "https://envs.sh/PHE.jpg"
)
SOUNCLOUD_IMG_URL = getenv(
    "SOUNCLOUD_IMG_URL", "https://envs.sh/PHD.jpg"
)
YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL", "https://envs.sh/PN-.jpg"
)
SPOTIFY_ARTIST_IMG_URL = getenv(
    "SPOTIFY_ARTIST_IMG_URL", "https://envs.sh/PNV.jpg"
)
SPOTIFY_ALBUM_IMG_URL = getenv(
    "SPOTIFY_ALBUM_IMG_URL", "https://envs.sh/PNx.jpg"
)
SPOTIFY_PLAYLIST_IMG_URL = getenv(
    "SPOTIFY_PLAYLIST_IMG_URL", "https://envs.sh/PHu.jpg"
)


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
