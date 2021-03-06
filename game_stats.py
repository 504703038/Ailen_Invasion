
class GameStats():
    """ 跟踪游戏的统计信息 """

    def __init__(self, ai_settings):
        """ 初始化统计信息 """
        self.ai_settings = ai_settings
        # 重置游戏信息
        self.reset_stats()
        # 游戏状态
        self.game_active = False
        # 游戏最高分
        self.high_score = 0
        # 游戏等级
        # self.level = 1

    def reset_stats(self):
        """ 初始化在游戏运行期间可能变化的统计信息 """
        self.ships_left = self.ai_settings.ship_limit
        # 初始化分数
        self.score = 0
        # 初始化游戏等级
        self.level = 1
