
import json, uuid, time

def dbRead(file: str = None):
    with open(file, "r") as f:
        dbdata = json.load(f)
    return dbdata


def returnObj(jsondb, usernm):
    user = None
    for i in range(len(jsondb)):
        if usernm == jsondb[i]["Username"]:
            user = jsondb[i]
    return user

def app_screen_geometry(app):
    # print(app)
    screen = app.primaryScreen()
    screen_geometry = screen.geometry()
    screen_width = screen_geometry.width()
    screen_height = screen_geometry.height()

    print(f"Display Resolution: {screen_width}x{screen_height}")
    return screen_geometry