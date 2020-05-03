import sys
import pygame
from bullet import Bullet
from alien import Alien


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


def draw_aliens(aliens):
    '''绘制外星人军队'''
    for alien in aliens:
        alien.blitme()
    # print(len(aliens))


def get_number_aliens_col(ai_settings, alien_width):
    '''计算每行可容纳外星人的数量'''
    available_space_col = ai_settings.screen_width - 2 * alien_width
    number_aliens_col = int(available_space_col / (2 * alien_width))
    return number_aliens_col


def get_number_aliens_row(ai_settings, alien_height, ship_height):
    '''游戏屏幕计算可以容纳多少行外星人'''
    available_space_row = ai_settings.screen_height - 3 * alien_height - ship_height
    number_aliens_row = int(available_space_row/(2*alien_height))
    return number_aliens_row


def create_alien(ai_settings, screen, aliens, alien_id, row):
    # 创建一个外星人并加入当前行
    alien = Alien(ai_settings, screen)
    alien.x = alien.rect.width + 2 * alien.rect.width * alien_id
    alien.rect.x = alien.x
    alien.y = alien.rect.height + 2 * alien.rect.height * row
    alien.rect.y = alien.y
    aliens.add(alien)


def create_fleet(ai_settings, screen, aliens, ship):
    '''创建外星人军队'''
    # 创建一个外星人，并计算一行可以容纳多少个外星人
    # 外星人间距为外星人宽度
    alien = Alien(ai_settings, screen)
    # alien_width = alien.rect.width
    # alien_height = alien.rect.height
    number_aliens_row = get_number_aliens_row(
        ai_settings,  alien.rect.height, ship.rect.height)
    number_aliens_col = get_number_aliens_col(ai_settings, alien.rect.width)
    # 创建第一行外星人
    for row in range(number_aliens_row):
        for alien_id in range(number_aliens_col):
            create_alien(ai_settings, screen, aliens, alien_id, row)


def update_screen(ai_settings, screen, ship, aliens):
    '''更新屏幕图像'''
    # 填充背景颜色
    screen.fill(ai_settings.bg_color)
    # 绘制子弹
    draw_bullet(ship.bullets)
    # 绘制飞船
    ship.blitme()
    # 绘制外星人
    draw_aliens(aliens)
    # 绘制屏幕
    pygame.display.flip()
