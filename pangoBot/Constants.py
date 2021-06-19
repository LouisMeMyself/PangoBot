# Server
LIVE_SERVER_ID = 786999832027463710
TEST_SERVER_ID = 829742012558475324

# Emojis
EMOJI_CHECK = "✅"
EMOJI_CROSS = "❌"
EMOJI_ACCEPT_GUIDELINES = "✅"

# Commands
PROFILE_PICTURE_COMMAND = "!pangopic"

# Roles
ROLE_FOR_CMD = "Bot Master"
VERIFIED_USER_ROLE = "Pango"

# Errors
ERROR_ON_PROFILE_PICTURE ="""How to use pangoBot for profile pictures:

1. Choose a HEX color or a RGB color in these formats: `#00FFFF`, `00FFFF`, `0 255 255` or `0,255,255`. [(color picker)](https://htmlcolorcodes.com/color-picker/)

2. Enter this command `!pangopic [color]` !
   You can enter `!pangopic random` to create a random and unique pango (more than 1E80 possibility)!

3. Save image + add as your Discord profile photo !"""


class Channels:
    def __init__(self, server_id, bot):
        if server_id == LIVE_SERVER_ID:
            server_nb = 0
        elif server_id == TEST_SERVER_ID:
            server_nb = 1
        else:
            raise Exception("Servers not found, pls check ids")

        self.__channel = {}
        for server in bot.guilds:
            if server.id == server_id:
                for channel in server.channels:
                    self.__channel[channel.id] = channel

        self.PANGOPIC_CHANNEL_ID = (854128212192002068, 842089026625470464)[server_nb]  # "👨🏻-profile-pictures"
        # self.SUGGESTION_CHANNEL_ID = (0, 1)[server_nb]  # "👨🏻-profile-pictures"
        # self.GUIDELINES_CHANNEL_ID = (0, 1)[server_nb]  # "📚-guidelines-and-resources"
        # self.COMMAND_CHANNEL_ID = (0, 1)[server_nb]  # "🤖-bot-commands"
        # self.GUIDELINES_MSG_ID = (0, 1)[server_nb]

    def get_channel(self, channel_id):
        return self.__channel[channel_id]


