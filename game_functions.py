import sys
import pygame
from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship):
    '''响应键盘按下事件'''
    if event.key == pygame.K_RIGHT:
        # 飞船开始向右移动
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 飞船开始向左移动
        ship.moving_left = True
    elif event.key == pygame.K_UP:
        # 飞船开始向上移动
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        # 飞船开始向下移动
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        # 创建一个子弹，并加入到编组bullets中
        ship.fire()
        # fire_bullet(ai_settings, screen, ship, bullets)


def check_keyup_events(event, ai_settings, screen, ship):
    '''响应键盘弹起事件'''
    if event.key == pygame.K_RIGHT:
        # 飞船停止向右移动
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        # 飞船停止向左移动
        ship.moving_left = False
    if event.key == pygame.K_UP:
        # 飞船停止向上移动
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        # 飞船停止向下移动
        ship.moving_down = False


def check_events(ai_settings, screen, ship):
    '''响应键盘和鼠标事件'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ai_settings, screen, ship)


def draw_bullet(bullets):
    '''绘制子弹并删除已消失的子弹'''
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        else:
            bullet.draw_bullet()
    print(len(bullets))


def update_screen(ai_settings, screen, ship, alien):
    '''更新屏幕图像'''
    # 填充背景颜色
    screen.fill(ai_settings.bg_color)
    # 绘制子弹
    draw_bullet(ship.bullets)
    # 绘制飞船
    ship.blitme()
    # 绘制外星人
    alien.blitme()
    # 绘制屏幕
    pygame.display.flip()
