import pygame
from pygame.sprite import Group
from pygame.sprite import Sprite
from bullet import Bullet


class Ship(Sprite):
    """ 玩家飞船 """

    def __init__(self, screen, ai_settings):
        """ 初始化飞船设置 """
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # 将飞船放在屏幕底部中央
        self.init_ship_position()

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # 创建一个用于存储子弹的编组
        self.bullets = Group()
        # 子弹数量限制
        self.bullets_allowed = ai_settings.bullets_allowed

    def blitme(self):
        """ 在指定位置绘制飞船 """
        self.update()
        self.screen.blit(self.image, self.rect)

    def update(self):
        """ 根据移动标志调整飞船的位置 """
        # 向右移动
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
            self.rect.centerx = self.centerx
        # 向左移动
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed_factor
            self.rect.centerx = self.centerx
        # 向上移动
        if self.moving_up and self.rect.top > 0:
            self.bottom -= self.ai_settings.ship_speed_factor
            self.rect.bottom = self.bottom
        # 向下移动
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.bottom += self.ai_settings.ship_speed_factor
            self.rect.bottom = self.bottom

    def fire(self):
        """ 发射子弹 """
        # 如果没有到达子弹限制，就发射一发子弹
        if len(self.bullets) < self.bullets_allowed:
            new_bullet = Bullet(self.ai_settings, self.screen, self)
            self.bullets.add(new_bullet)

    def init_ship_position(self):
        """ 初始化飞船的位置 """
        # 将飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.centerx = float(self.rect.centerx)
        self.bottom = float(self.rect.bottom)
