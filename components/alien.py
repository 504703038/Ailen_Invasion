import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """外星人"""

    def __init__(self, ai_settings, screen):
        """ 初始化外星人并设置起始位置 """
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图像
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 初始位置在游戏屏幕的左上角
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的准确位置
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges(self):
        """ 如果外星人位于游戏屏幕边缘则返回True """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        return False

    def update(self):
        """ 移动外星人 """
        self.x += (self.ai_settings.alien_direction *
                   self.ai_settings.alien_speed_factor)
        self.rect.x = self.x

    def blitme(self):
        """ 在制定位置绘制外星人 """
        # self.update()
        self.screen.blit(self.image, self.rect)
