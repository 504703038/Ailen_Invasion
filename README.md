# English

## Ailen Invasion

A python game, which is a project case of [*Python Crash Course, 2nd Edition*](https://nostarch.com/pythoncrashcourse2e)。

In Alien Invasion, the player controls a rocket ship that appears at the bottom center of the screen. The player can move the ship right and left using the arrow keys and shoot bullets using the spacebar. When the game begins, a fleet of aliens fills the sky and moves across and down the screen. The player shoots and destroys the aliens. If the player shoots all the aliens, a new fleet appears that moves faster than the previous fleet. If any alien hits the player’s ship or reaches the bottom of the screen, the player loses a ship. If the player loses three ships, the game ends.

### Catalog description

- [Alien Invasion](./) `Project root directory`
  - [components](./components) `Component catalog`
    - [\_\_init\_\_.py](./components/__init__.py) 
    - [alien.py](./components/alien.py) `The class of Alien`
    - [bullet.py](./components/bullet.py) `The class of Bullet`
    - [button.py](./components/button.py) `The class of Button`
    - [scoreboard.py](./components/scoreboard.py) `The class of Scoreboard`
    - [ship.py](./components/ship.py) `The class of Ship`

  - [images](./images) `Sticker catalog`
    - [alien.bmp](./images/alien.bmp) `The Sticker of Alien`
    - [ship.bmp](./images/ship.bmp) `The Sticker of Ship`

  - [alien_invasion.py](./alien_invasion.py) `Game entry file`

  - [game_function.py](./game_function.py) `The function used in the game`

  - [game_stats.py](./game_stats.py) `The class of Gamestats`

  - [settings.py](./settings.py) `The class of Settings`



# 中文

## 外星人入侵

使用Python语言编写的游戏，《Python编程从入门到实践》(ISBN 978-7-115-42802-8)书中的项目案例。

在游戏《外星人入侵》中，玩家控制着一艘最初出现在屏幕底部中央的飞船。玩家可以使用箭头键左右移动飞船，还可使用空格键进行射击。游戏开始时，一群外星人出现在天空中，他们在屏幕中向下移动。玩家的任务是射杀这些外星人。玩家将所有外星人都消灭干净后，将出现一群新的外星人，他们移动的速度更快。只要有外星人撞到了玩家的飞船或到达了屏幕底部，玩家就损失一艘飞船。玩家损失三艘飞船后，游戏结束。

### 目录说明

- [Alien Invasion](./) `项目根目录`
  - [components](./components) `组件目录`
    - [\_\_init\_\_.py](./components/__init__.py) 
    - [alien.py](./components/alien.py) `外星人类`
    - [bullet.py](./components/bullet.py) `子弹类`
    - [button.py](./components/button.py) `按钮类`
    - [scoreboard.py](./components/scoreboard.py) `计分板类`
    - [ship.py](./components/ship.py) `飞船类`

  - [images](./images) `贴纸目录`
    - [alien.bmp](./images/alien.bmp) `外星人贴纸`
    - [ship.bmp](./images/ship.bmp) `飞船贴纸`

  - [alien_invasion.py](./alien_invasion.py) `游戏入口文件`

  - [game_function.py](./game_function.py) `游戏函数文件`

  - [game_stats.py](./game_stats.py) `游戏状态文件`

  - [settings.py](./settings.py) `游戏设置文件`



