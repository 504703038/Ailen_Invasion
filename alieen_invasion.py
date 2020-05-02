import sys
import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group


def run_game():
    # 初始化游戏并能够创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    # 设置游戏屏幕大小
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    # 设置游戏窗口名称
    pygame.display.set_caption('Alien Invasion')

    # 创建飞船
    ship = Ship(screen, ai_settings)
    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 开始游戏主循环
    while True:
        # 监听键盘个鼠标时间
        gf.check_events(ai_settings, screen, ship, bullets)
        # 更新屏幕图像
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
