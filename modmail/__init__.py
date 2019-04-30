from .modmail import Modmail
from redbot.core.data_manager import cog_data_path
import os
import json

# Throwback
def check_files():
    if not os.path.exists(
        os.path.join(cog_data_path(raw_name="ModMail"), "dictionary.json")
    ):
        # if not dictionary.json, let's just add default values
        with open(
            os.path.join(__path__[0], "dictionary.json"), "r"
        ) as default_dictionary:
            default = json.load(default_dictionary)
        with open(
            os.path.join(cog_data_path(raw_name="ModMail"), "dictionary.json"), "w"
        ) as new_dictionary:
            print("Creating default dict")
            json.dump(default, new_dictionary)


def setup(bot):
    check_files()
    bot.add_cog(Modmail(bot))
