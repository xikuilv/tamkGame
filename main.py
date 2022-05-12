# #!/usr/bin/python3
# -*- coding: UTF-8 -*-
# @Time   : {2022/5/12  19:48}
# @Author : {}
# @Email  : 824935520@qq.com
# @File   : {}

"""
    主逻辑类
        开始游戏
        结束游戏
    创建坦克类（我方坦克、敌方坦克）
        移动、射击
    创建子弹类
        移动
    创建墙壁
        属性
    创建爆炸效果类
        展示爆炸效果
    音效类
        播放音效
"""

"""
    新增功能：
        创建游戏窗口
        官方开发文档
        游戏引擎的功能模块
"""


import pygame

_display = pygame.display
window_bg_color = (0, 200, 0)
class MainGame:
    # 游戏主窗口
    window = None
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600

    def __init__(self):
        pass

    # 开始游戏
    def start_game(self):
        pygame.display.init()
        self.window = _display.set_mode([self.SCREEN_WIDTH, self.SCREEN_HEIGHT])
        _display.set_caption("Tank Game")

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.end_game()

            self.window.fill(window_bg_color)

            _display.flip()

    # 结束游戏
    def end_game(self):
        print("谢谢使用！")
        # 结束游戏
        exit()

class Tank:
    def __init__(self):
        pass

    # 坦克移动
    def tank_move(self):
        pass

    # 坦克射击
    def tank_shot(self):
        pass

    # 坦克展示
    def display_tank(self):
        pass


class MyTank(Tank):
    def __init__(self):
        super().__init__()
        pass


class EnemyTank(Tank):
    def __init__(self):
        super().__init__()
        pass


class Bullet:
    def __init__(self):
        pass

    # 子弹移动
    def bullet_move(self):
        pass

    # 子弹展示
    def display_bullet(self):
        pass


class Explode:
    def __init__(self):
        pass

    # 展示爆炸效果
    def display_explode(self):
        pass


class Wall:
    def __init__(self):
        pass

    # 展示墙壁
    def display_wall(self):
        pass


class Music:
    def __init__(self):
        pass

    # 播放音乐
    def play_music(self):
        pass

MainGame().start_game()
