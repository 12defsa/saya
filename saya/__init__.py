# -*- coding: utf-8 -*-
# author: Ethosa

from .VK import (Vk, LongPoll, Event, PushEvent, VkAuthManager,
                 VkScript, Uploader, Button, Keyboard)

__copyright__ = "2020"
__version__ = "0.0.4"
__authors__ = ["Ethosa"]

if __name__ == '__main__':
    print(Vk, LongPoll, VkAuthManager, Event,
          PushEvent, VkScript, Uploader, Button,
          Keyboard)
