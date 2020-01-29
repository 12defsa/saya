# -*- coding: utf-8 -*-
# author: Ethosa


class Button(dict):
    PRIMARY = "primary"
    SECONDARY = "secondary"
    POSITIVE = "positive"
    NEGATIVE = "negative"

    def __init__(self, btype="text", color="primary", **kwargs):
        """
        Creates a new Button object.

        Keyword Arguments:
            btype {str} -- button type. (default: {"text"})
            color {str} -- button color. (default: {"primary"})
        """
        if btype == "text":
            self["color"] = color
        self["action"] = kwargs
        self["action"]["type"] = btype

    def set_color(self, color="primary"):
        self["color"] = color
