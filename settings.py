class Settings():
    """ 储存《外星人入侵》的所有设置的类 """

    def __init__(self):
        """ 初始化游戏设置 """
        # 屏幕设置
        self.init_screen_settings()
        # 飞船设置
        self.init_ship_settings()
        # 子弹设置
        self.init_bullet_settings()
        # 外星人设置
        self.init_alien_settings()
        # 游戏难度设置
        self.init_difficulty()

    def init_screen_settings(self):
        """ 屏幕设置 """
        # 大小
        self.screen_width = 1200
        self.screen_height = 800
        # 背景颜色
        self.bg_color = (230, 230, 230)

    def init_ship_settings(self):
        """ 飞船设置 """
        # 飞船速度
        self.ship_speed_factor = 1.5
        # 飞船生命
        self.ship_limit = 3

    def init_bullet_settings(self):
        """ 子弹设置 """
        # 子弹的速度
        self.bullet_speed_factor = 1.5
        # 子弹大小
        self.bullet_width = 3
        self.bullet_height = 15
        # 子弹的颜色
        self.bullet_color = (60, 60, 60)
        # 最大子弹数量
        self.bullets_allowed = 10

    def init_alien_settings(self):
        """ 外星人设置 """
        # 外星人移动速度
        self.alien_speed_factor = 1
        # 外星人移动方向(1表示向右移动，-1表示向左移动)
        self.alien_direction = 1
        # 外星人下降速度
        self.alien_drop_speed = 10
        # 外星人分数
        self.alien_points = 10

    def increase_difficulty(self):
        """ 增加游戏难度 """
        # 加快外星人移动速度
        self.alien_speed_factor += self.increase_scale
        # 加快子弹速度
        self.bullet_speed_factor += self.increase_scale
        # 减少子弹数量
        if self.bullets_allowed > 1:
            self.bullets_allowed -= self.increase_scale
        # 提高外星人的分数
        self.alien_points += 10*self.increase_scale

    def init_difficulty(self):
        """ 设置游戏难度 """
        # 子弹速度
        self.bullet_speed_factor = 1.5
        # 外星人速度
        self.alien_speed_factor = 1
        # 子弹数量
        self.bullets_allowed = 10
        # 难度增加跨度
        self.increase_scale = 0.5
        # 外星人分数
        self.alien_points = 10
