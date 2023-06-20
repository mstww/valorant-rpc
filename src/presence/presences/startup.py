from ...localization.localization import Localizer

def presence(rpc,client=None,data=None,content_data=None,config=None):
    rpc.update(
        state=Localizer.get_localized_text("presences","startup","loading"),
        large_image="game_icon",
        large_text="VALORANT-rpc",
        buttons=[{
<<<<<<< HEAD
            'label':"Valorant Store Bot",
            'url':"https://discord.com/api/oauth2/authorize?client_id=640278989000146973&permissions=277025475648&scope=applications.commands%20bot"
=======
            'label': Localizer.get_config_value("presences","menu","button1"),
            'url': Localizer.get_config_value("presences","menu","link1")
>>>>>>> c3677c5 (Update)
        }] if Localizer.get_config_value("startup","show_github_link") else None
    )