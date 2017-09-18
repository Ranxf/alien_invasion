# import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()  # 创建一个Settings实例，并存在变量ai_settings中
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("alien_invasion")

    # 创建飞船
    ship = Ship(ai_settings, screen)

    # 创建一艘飞船
    # ship = Ship(screen)

    # 开始游戏的主循环
    while True:
        # # 监视键盘和鼠标事件
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()

        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)

        # # 每次循环时都重绘屏幕
        # screen.fill(ai_settings.bg_color)
        # ship.blitme()
        #
        # # 让最近绘制的屏幕可见
        # pygame.display.flip()

run_game()