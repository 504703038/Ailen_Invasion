class Settings():
    '''储存《外星人入侵》的所有设置的类'''

    def __init__(self):
        '''初始化游戏设置'''
        # 屏幕设置
        # 大小
        self.screen_width = 1200
        self.screen_height = 800
        # 背景颜色
        self.bg_color = (230, 230, 230)

        # 飞船速度
        self.ship_speed_factor = 1.5

        # 子弹设置
        # 子弹的速度
        self.bullet_speed_factor = 1.5
        # 子弹大小
        self.bullet_width = 3
        self.bullet_height = 15
        # 子弹的颜色
        self.bullet_color = (60, 60, 60)
        # 最大子弹数量
        self.bullets_allowed = 5

        # 外星人设置
        # 外星人移动速度
        self.alien_speed_factor = 1
        # 外星人移动方向(1表示向右移动，-1表示向左移动)
        self.alien_direction = 1
        # 外星人下降速度
        self.alien_drop_speed = 10
