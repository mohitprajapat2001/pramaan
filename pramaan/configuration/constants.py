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
