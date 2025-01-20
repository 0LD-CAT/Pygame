import pygame

# start
clock = pygame.time.Clock()
pygame.init()
# settings
screen = pygame.display.set_mode((852, 480))
pygame.display.set_caption("Crossout 3.0")
icon = pygame.image.load('Game/Images/Icon_Auger.png').convert_alpha()
pygame.display.set_icon(icon)

myfont = pygame.font.Font('Game/Images/BungeeTint-Regular.ttf', 40)
lose_font = pygame.font.Font('Game/Images/BebasNeue-Regular.ttf', 40)
lose_label = lose_font.render('You lose, LOX!', False, (255, 0, 255))
restart_label = lose_font.render('RESTART', False, (255, 0, 255))
restart_label_rect = restart_label.get_rect(topleft=(380, 250))
text_surface = myfont.render('Crossout 3.0', True, 'Red')

car = pygame.image.load('Game/Images/crossout-u2014-vehicle-transportation-wheel-machine-transparent-png-2718720 (1).png').convert_alpha()
car_timer = pygame.USEREVENT + 1
pygame.time.set_timer(car_timer, 5000)
cars_list = []

bullet = pygame.image.load('Game/Images/pngwing.com.png').convert_alpha()
bullets = []
bullets_kolvo = 10
palach = pygame.image.load('Game/Images/palach2.png').convert_alpha()
weapon = [palach, ]
weapon_sound = pygame.mixer.Sound('Game/Music and sounds/vystrel-iz-pushki.mp3')
probitie_sound = pygame.mixer.Sound('Game/Music and sounds/est-probitie-chistoe.mp3')

background = pygame.image.load('Game/Images/1cf907056af74619bf50b31fbbe7f3ef.jpg').convert()
walk_left = [
    pygame.image.load('Game/Images/player/Magenta_LUXURY_CLEAN_NORTHEAST_011.png').convert_alpha(),
    pygame.image.load('Game/Images/player/Magenta_LUXURY_CLEAN_NORTHEAST_011.png').convert_alpha(),
    pygame.image.load('Game/Images/player/Magenta_LUXURY_CLEAN_NORTHEAST_011.png').convert_alpha(),
    pygame.image.load('Game/Images/player/Magenta_LUXURY_CLEAN_NORTHEAST_0111.png').convert_alpha(),
    pygame.image.load('Game/Images/player/Magenta_LUXURY_CLEAN_NORTHEAST_0111.png').convert_alpha(),
    pygame.image.load('Game/Images/player/Magenta_LUXURY_CLEAN_NORTHEAST_0111.png').convert_alpha(),
    pygame.image.load('Game/Images/player/Magenta_LUXURY_CLEAN_NORTHEAST_0111.png').convert_alpha(),
    pygame.image.load('Game/Images/player/Magenta_LUXURY_CLEAN_NORTHEAST_0111.png').convert_alpha()
]
walk_right = [
    pygame.image.load('Game/Images/player/Magenta_LUXURY_CLEAN_SOUTHEAST_011.png').convert_alpha(),
    pygame.image.load('Game/Images/player/Magenta_LUXURY_CLEAN_SOUTHEAST_011.png').convert_alpha(),
    pygame.image.load('Game/Images/player/Magenta_LUXURY_CLEAN_SOUTHEAST_011.png').convert_alpha(),
    pygame.image.load('Game/Images/player/Magenta_LUXURY_CLEAN_SOUTHEAST_0111.png').convert_alpha(),
    pygame.image.load('Game/Images/player/Magenta_LUXURY_CLEAN_SOUTHEAST_0111.png').convert_alpha(),
    pygame.image.load('Game/Images/player/Magenta_LUXURY_CLEAN_SOUTHEAST_0111.png').convert_alpha(),
    pygame.image.load('Game/Images/player/Magenta_LUXURY_CLEAN_SOUTHEAST_0111.png').convert_alpha(),
    pygame.image.load('Game/Images/player/Magenta_LUXURY_CLEAN_SOUTHEAST_0111.png').convert_alpha()
]
walk_forward = [
    pygame.image.load('Game/Images/player/forward/Magenta_LUXURY_CLEAN_EAST_000.png').convert_alpha(),
    pygame.image.load('Game/Images/player/forward/Magenta_LUXURY_CLEAN_EAST_001.png').convert_alpha(),
    pygame.image.load('Game/Images/player/forward/Magenta_LUXURY_CLEAN_EAST_002.png').convert_alpha(),
    pygame.image.load('Game/Images/player/forward/Magenta_LUXURY_CLEAN_EAST_003.png').convert_alpha(),
    pygame.image.load('Game/Images/player/forward/Magenta_LUXURY_CLEAN_EAST_004.png').convert_alpha(),
    pygame.image.load('Game/Images/player/forward/Magenta_LUXURY_CLEAN_EAST_005.png').convert_alpha(),
    pygame.image.load('Game/Images/player/forward/Magenta_LUXURY_CLEAN_EAST_006.png').convert_alpha(),
    pygame.image.load('Game/Images/player/forward/Magenta_LUXURY_CLEAN_EAST_007.png').convert_alpha()
]
player_anim_count = 0
player_speed = 10
player_x = 100
player_y = 350
bg_x = 0
bg_music = pygame.mixer.Sound('Game/Music and sounds/OST CROSSOUT — Motorhead (www.lightaudio.ru).mp3')
bg_music.play()
lose_sound = pygame.mixer.Sound('Game/Music and sounds/29-bruh.mp3')
drift_sound = pygame.mixer.Sound('Game/Music and sounds/drift-na-avtomobile-variant-2-34228 (mp3cut.net) (2).mp3')
end_game_sound_mark = pygame.mixer.Sound('Game/Music and sounds/MARK.mp3')
# main
running = True
gameplay = True

while running:
    screen.blit(background, (bg_x, 0))
    screen.blit(background, (bg_x + 852, 0))
    screen.blit(text_surface, (300, 0))
    if gameplay:
        player_rect = walk_forward[0].get_rect(topleft=(player_x, player_y))
        screen.blit(weapon[0], (player_x + 25, player_y))
        if cars_list:
            for (i, el) in enumerate(cars_list):
                screen.blit(car, el)
                el.x -= 10
                if el.x < -10:
                    cars_list.pop(i)
                if player_rect.colliderect(el):
                    gameplay = False
                    bg_music.stop()
                    lose_sound.play()
                    end_game_sound_mark.play()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            screen.blit(walk_left[player_anim_count], (player_x, player_y))
        elif keys[pygame.K_d]:
            screen.blit(walk_right[player_anim_count], (player_x, player_y))
        else:
            screen.blit(walk_forward[player_anim_count], (player_x, player_y))

        if keys[pygame.K_s] and player_x > 10:
            player_x -= player_speed
        elif keys[pygame.K_w] and player_x < 800:
            player_x += player_speed
        elif keys[pygame.K_a] and player_y > 250:
            player_y -= player_speed
        elif keys[pygame.K_d] and player_y < 400:
            player_y += player_speed

        if player_anim_count == 7:
            player_anim_count = 0
        else:
            player_anim_count += 1

        bg_x -= 20
        if bg_x < -852:
            bg_x = 0

        if bullets:
            for (i, el) in enumerate(bullets):
                screen.blit(bullet, (el.x, el.y))
                el.x += 20
                if el.x > 890:
                    bullets.pop(i)
                if cars_list:
                    for (index, car_el) in enumerate(cars_list):
                        if el.colliderect(car_el):
                            cars_list.pop(index)
                            bullets.pop(i)
                            probitie_sound.play()

    else:
        screen.fill((255, 0, 0))
        screen.blit(lose_label, (350, 200))
        screen.blit(restart_label, restart_label_rect)

        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            player_x = 100
            player_y = 350
            cars_list.clear()
            bullets.clear()
            bg_music.play()
            bullets_kolvo = 10
            end_game_sound_mark.stop()

    pygame.display.update()

    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == car_timer:
            cars_list.append(car.get_rect(topleft=(900, 350)))
        if gameplay and event.type == pygame.KEYUP and event.key == pygame.K_SPACE and bullets_kolvo > 0:
            bullets.append(bullet.get_rect(topleft=(player_x + 59, player_y + 6)))
            bullets_kolvo -= 1
            weapon_sound.play(0)
        if (keys[pygame.K_a] or keys[pygame.K_d]) and gameplay:
            drift_sound.play()
        else:
            drift_sound.stop()
    clock.tick(10)
