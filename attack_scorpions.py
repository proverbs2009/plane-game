#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 作者：maxim
# 本文件介绍：创建“attack_scorpions”游戏的窗口

import pygame
from pygame.sprite import Group
from settings import Settings
from plane import Plane
import game_functions as gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Attack Scorptions")

    # 创建一个Play按钮
    play_button = Button(screen, "Play")

    # 创建一个用于存储游戏统计信息的实例,并创建记分牌
    stats = GameStats(ai_settings)
    scoreboard = Scoreboard(ai_settings, screen, stats)

    # 创建一架飞机
    plane = Plane(ai_settings, screen)

    # 创建一个星星编组
    stars = Group()
    # 创建星星群
    gf.create_star_fleet(ai_settings, screen, stars)

    # 创建一个陨石编组
    meteorites = Group()
    # 创建陨石群
    gf.create_meteorite_fleet(ai_settings, screen, meteorites)

    # 创建一个气球编组
    qiqius = Group()
    # 创建气球群
    gf.create_fleet(ai_settings, screen, plane, qiqius)

    # 创建一个储存子弹的编组
    bullets90 = Group()
    bullets0 = Group()
    bullets180 = Group()

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, scoreboard, play_button, plane, bullets90, bullets0, bullets180, qiqius, meteorites, stars)

        if stats.game_active:

            # 更新陨石状态
            gf.update_meteorites(ai_settings, screen, meteorites)

            # 更新飞机状态
            plane.update()

            # 更新子弹状态
            gf.update_bullets(ai_settings, screen, stats, scoreboard, plane, qiqius, bullets90, bullets0, bullets180, meteorites)

            # 更新气球状态
            gf.update_qiqius(ai_settings, stats, scoreboard, screen, plane, qiqius, bullets90, bullets0, bullets180)

        # 每次循环时都重绘屏幕
        # 让最近绘制的屏幕可见
        gf.update_screen(ai_settings, screen, stats, scoreboard, plane, stars, meteorites, qiqius, bullets90, bullets0, bullets180, play_button)

run_game()