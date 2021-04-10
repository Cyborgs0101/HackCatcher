from instabot import Bot
import os
import shutil


def clean_up(i):
    dir = "config"
    remove_me = "imgs\{}.REMOVE_ME".format(i)
    # checking whether config folder exists or not
    if os.path.exists(dir):
        try:
            # removing it so we can upload new image
            shutil.rmtree(dir)
        except OSError as e:
            print("Error: %s - %s." % (e.filename, e.strerror))
    if os.path.exists(remove_me):
        src = os.path.realpath("imgs\{}".format(i))
        os.rename(remove_me, src)





def Insta_Post(n):
    # enter name of your image bellow
    bot = Bot()
    bot.login(username="Enter Your Username", password="Enter Your Password")
    for i in range(n):
        image_name = "Path\imageName"
        clean_up(image_name)
        bot.upload_photo(image_name,
                         caption="Any Caption that you want")
