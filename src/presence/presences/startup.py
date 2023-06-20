from ...localization.localization import Localizer

def presence(rpc,client=None,data=None,content_data=None,config=None):
    rpc.update(
        state=Localizer.get_localized_text("presences","startup","loading"),
        large_image="game_icon",
        large_text="VALORANT-rpc",
        buttons=[{
            'label': Localizer.get_config_value("presences","menu","button1"),
            'url': Localizer.get_config_value("presences","menu","link1")
        }] if Localizer.get_config_value("startup","show_github_link") else None
    )