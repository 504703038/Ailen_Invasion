import sys
import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from alien import Alien
from pygame.sprite import Group
from game_stats import GameStats
from button import Button


def run_game():
    # 初始化游戏并能够创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    # 设置游戏屏幕大小
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    # 设置游戏窗口名称
    pygame.display.set_caption('Alien Invasion')

    # 创建游戏按钮
    play_button = Button(ai_settings, screen, 'Play')

    # 创建储存游戏信息的实例
    stats = GameStats(ai_settings)

    # 创建飞船
    ship = Ship(screen, ai_settings)

    # 创建外星人列表
    aliens = Group()

    # 开始游戏主循环
    while True:
        # 监听键盘和鼠标事件
        gf.check_events(ai_settings, stats, screen, ship, aliens, play_button)

        # 更新游戏屏幕
        gf.update_screen(ai_settings, stats, screen, ship, aliens, play_button)

        if stats.game_active:
            # 检查游戏状态
            gf.check_game_status(ai_settings, stats, screen, ship, aliens)

            # 如果击杀所有外星人则再添加一轮外星人
            if len(aliens) == 0:
                gf.next_round(ai_settings, screen, ship, aliens)
        else:
            pass

    # 游戏结束
    print('Game over.')


if __name__ == "__main__":
    run_game()
