from django.utils.translation import gettext_lazy as _


class ThemeChoice:
    LIGHT = "light"
    DARK = "dark"
    CUPCAKE = "cupcake"
    NIGHT = "night"
    BUMBLEBEE = "bumblebee"
    EMERALD = "emerald"
    CORPORATE = "corporate"
    SYNTHWAVE = "synthwave"
    HALLOWEEN = "halloween"
    GARDEN = "garden"
    WINTER = "winter"
    FOREST = "forest"
    BLACK = "black"
    CMYK = "cmyk"

    THEME_CHOICES = [
        (LIGHT, _("Light")),
        (DARK, _("Dark")),
        (CUPCAKE, _("Cupcake")),
        (NIGHT, _("Night")),
        (BUMBLEBEE, _("Bumblebee")),
        (EMERALD, _("Emerald")),
        (CORPORATE, _("Corporate")),
        (SYNTHWAVE, _("Synthwave")),
        (HALLOWEEN, _("Halloween")),
        (GARDEN, _("Garden")),
        (WINTER, _("Winter")),
        (FOREST, _("Forest")),
        (BLACK, _("Black")),
        (CMYK, _("CMYK")),
    ]


class Languages:
    HINDI = "hi"
    ENGLISH = "en"

    LANGUAGE_CHOICES = [
        (HINDI, _("Hindi")),
        (ENGLISH, _("English")),
    ]


class PlaceHolders:
    THEME = _("Select Theme")
    LANGUAGE = _("Select Language")
    SEARCH = _("Search")
    NOTIFICATIONS = _("Notifications")
    PRIVACY = {
        "show_email": _("Show Email"),
        "show_phone": _("Show Phone"),
        "allow_messages": _("Allow Messages"),
    }


class Labels:
    THEME = _(
        "Please select a theme. <br><span class='text-xs'>(Note: Theme will be used for the entire site. and your profile card)</span>"
    )
    LANGUAGE = _("Language")
    SEARCH = _("Search")
    NOTIFICATIONS = _(
        "Allow to receive notifications. <br><span class='text-xs'>You may receive email notifications related to your account. We won't span you promise <i class='far fa-handshake'></i></span>"
    )
    PRIVACY = {
        "show_email": _("Allow other to see your email"),
        "show_phone": _("Allow other to see your phone number"),
        "allow_messages": _("Allow other to send you messages"),
    }


class SucccessMessages:
    """Configuration app success message"""

    CONFIGURATIONS_UPDATE = _("Configurations updated successfully")


class ValidationErrors:
    """Configuration app validation errors"""
