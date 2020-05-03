import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    '''飞船发的射子'''

    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen = screen

        # 在(0,0)创建子弹，并设置其位置
        self.rect = pygame.Rect(
            0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.center = ship.rect.center
        self.rect.top = ship.rect.top
        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        '''向上移动子弹'''
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw_bullet(self):
        '''在屏幕上绘制子弹'''
        self.update()
        pygame.draw.rect(self.screen, self.color, self.rect)
