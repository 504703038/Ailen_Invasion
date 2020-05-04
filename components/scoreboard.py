import pygame.font
from pygame.sprite import Group
from components import Ship


class Scoreboard():
    """ 计分板 """

    def __init__(self, ai_settings, stats, screen):
        """ 初始化计分板 """
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats

        # 分数字体设置
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont('宋体', 48)

        # 将分数转换为图像
        # self.prep_score()
        # self.prep_high_score()
        # 创建飞船编组
        # self.prep_ships()

    def prep_score(self):
        """ 将分数渲染为图像 """
        # 渲染为图片
        rounded_score = int(round(self.stats.score, 0))
        score_str = "得分：{:,}".format(rounded_score)
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.ai_settings.bg_color)

        # 将得分放在右上角
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right
        self.score_rect.top = 20

    def prep_high_score(self):
        """ 将最高分渲染为图像 """
        # 渲染为图片
        rounded_high_score = int(round(self.stats.high_score, 0))
        high_score_str = "最高分：{:,}".format(rounded_high_score)
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color, self.ai_settings.bg_color)

        # 将最高分放在游戏屏幕顶部中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """ 将等级渲染为图像 """
        # 渲染为图片
        self.level_image = self.font.render(
            str(self.stats.level), True,
            self.text_color, self.ai_settings.bg_color)

        # 将等级放在得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """ 创建飞船编组 """
        self.ships = Group()
        for ship_id in range(self.stats.ships_left):
            ship = Ship(self.screen, self.ai_settings)
            ship.rect.x = 10 + ship_id * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_board(self):
        """ 在屏幕绘制计分板 """
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
