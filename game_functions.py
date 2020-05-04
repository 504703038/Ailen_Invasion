import sys
import pygame
from time import sleep
from components import Alien, Bullet


def check_keydown_events(event, ai_settings, screen, ship):
    """ 响应键盘按下事件 """
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
    """ 响应键盘弹起事件 """
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


def check_play_button(ai_settings, stats, screen, ship, aliens,
                      play_button, mouse_x, mouse_y):
    """ 当玩家点击Play按钮时开始游戏 """
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # 开始游戏
        stats.game_active = True
        ai_settings.init_difficulty()
        # 隐藏鼠标
        pygame.mouse.set_visible(False)
        # 重置游戏状态
        stats.reset_stats()
        new_round(ai_settings, screen, ship, aliens)


def check_events(ai_settings, stats, screen, ship, aliens, play_button):
    """ 响应键盘和鼠标事件 """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ai_settings, screen, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, stats, screen, ship,
                              aliens, play_button, mouse_x, mouse_y)


def change_fleet_direction(ai_settings, aliens):
    """ 改变外星人运动方向并并下降10个像素点 """
    for alien in aliens:
        alien.y += ai_settings.alien_drop_speed
        alien.rect.y = alien.y
    ai_settings.alien_direction *= -1


def check_fleet_edges(ai_settings, aliens):
    """ 当外星人到达游戏屏幕边缘时，改变外星人运动方向 """
    for alien in aliens:
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def ship_hit(ai_settings, stats, screen, ship, aliens):
    """ 响应飞船撞击外星人事件 """
    # 判断飞船生命剩余
    if stats.ships_left > 0:
        # 飞船生命减1
        stats.ships_left -= 1
        # 重新开始这一轮游戏
        new_round(ai_settings, screen, ship, aliens)
    else:
        # 游戏结束
        stats.game_active = False
        # 显示光标
        pygame.mouse.set_visible(True)

    # 暂停
    sleep(0.5)


def check_game_status(ai_settings, stats, screen, ship, aliens):
    """ 检查游戏状态 """
    # 检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens)
        return

    # 外星人是否到达游戏屏幕底部
    screen_rect = screen.get_rect()
    for alien in aliens:
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens)
            return


def get_number_aliens_col(ai_settings, alien_width):
    """ 计算每行可容纳外星人的数量 """
    available_space_col = ai_settings.screen_width - 2 * alien_width
    number_aliens_col = int(available_space_col / (2 * alien_width))
    return number_aliens_col


def get_number_aliens_row(ai_settings, alien_height, ship_height):
    """ 游戏屏幕计算可以容纳多少行外星人 """
    available_space_row = ai_settings.screen_height - \
        3 * alien_height - ship_height
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


def create_fleet(ai_settings, screen, ship, aliens):
    """ 创建外星人军队 """
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


def new_round(ai_settings, screen, ship, aliens):
    """ 开启新的一轮 """
    # 清空外星人列表和子弹列表
    aliens.empty()
    ship.bullets.empty()
    # 初始化游戏难度
    # ai_settings.init_difficulty()
    # 初始化飞船位置
    ship.init_ship_position()
    # 创建一群外星人
    create_fleet(ai_settings, screen, ship, aliens)


def next_round(ai_settings, stats, screen, ship, aliens):
    # 删除所有子弹和外星人
    ship.bullets.empty()
    aliens.empty()
    # 重新加载一群外星人
    create_fleet(ai_settings, screen, ship, aliens)
    # 增加游戏难度
    stats.level += 1
    ai_settings.increase_difficulty()


def check_bullet_alien_collosion(ai_settings, stats, bullets, aliens):
    """ 响应子弹与外星人的碰撞 """
    # 检查是否有子弹击中外星人，如果击中就同时删除
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            if stats.score > stats.high_score:
                stats.high_score = stats.score


def draw_bullet(ai_settings, stats, bullets, aliens):
    """ 绘制子弹并删除已消失的子弹 """
    # 更新子弹位置
    bullets.update()
    # 检测子弹与外星人的碰撞
    check_bullet_alien_collosion(ai_settings, stats, bullets, aliens)

    # 绘制子弹
    for bullet in bullets:
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        else:
            bullet.draw_bullet()


def draw_aliens(ai_settings, aliens):
    """ 绘制外星人军队 """
    # 更新外星人军队位置
    aliens.update()
    check_fleet_edges(ai_settings, aliens)
    for alien in aliens:
        alien.blitme()


def update_screen(ai_settings, stats, screen, ship, aliens,
                  play_button, score_bord):
    """ 更新屏幕图像 """
    # 填充背景颜色
    screen.fill(ai_settings.bg_color)

    # 根据游戏状态绘制游戏屏幕
    if not stats.game_active:
        # 绘制Play按钮
        play_button.draw_button()
    else:
        # 绘制子弹
        draw_bullet(ai_settings, stats, ship.bullets, aliens)
        # 绘制飞船
        ship.blitme()
        # 绘制外星人
        draw_aliens(ai_settings, aliens)
        # 显示得分
        score_bord.show_board()

    # 绘制屏幕
    pygame.display.flip()
