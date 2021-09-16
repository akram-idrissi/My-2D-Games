import pygame
import sys
from time import sleep

from alien import Alien
from bullets import Bullet


def check_events(ship, alien, screen, bullets, settings, play_button, stats):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(stats, screen, settings, play_button, alien, bullets, ship, mouse_x, mouse_y)
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, settings, screen, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_play_button(stats, screen, settings, play_button, alien, bullets, ship, mouse_x, mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        settings.initialize_dynamic_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True
        alien.empty()
        bullets.empty()
        create_fleet(settings, screen, ship, alien)
        ship.center_ship()


def check_keydown_events(event, ship, settings, screen, bullets):
    if event.key == pygame.K_ESCAPE:
        pygame.quit()
        sys.exit()
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_s:
        fire_bullet(ship, settings, screen, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(settings, ship, screen, bullet, alien, play_button, stats, sb):
    clock = pygame.time.Clock()
    screen.fill(settings.bg_color)
    ship.blit_me()
    alien.draw(screen)
    for b in bullet.sprites():
        b.draw_bullet()
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()
    pygame.display.update()
    clock.tick(settings.fps)


def update_bullets(bullets, alien, settings, screen, ship, stats, sb):
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_collision(bullets, alien, settings, screen, ship, stats, sb)


def check_collision(bullets, alien, settings, screen, ship, stats, sb):
    collisions = pygame.sprite.groupcollide(bullets, alien, True, True)
    if collisions:
        for alien in collisions.values():
            stats.score += settings.alien_point * len(alien)
            sb.prep_score()
        check_high_score(stats, sb)
    if len(alien) == 0:
        bullets.empty()
        settings.increase_speed()
        create_fleet(settings, screen, ship, alien)


def fire_bullet(ship, settings, screen, bullet):
    if len(bullet) < settings.bullets_number:
        new_bullet = Bullet(screen, settings, ship)
        bullet.add(new_bullet)


def get_number_aliens_x(settings, alien_width):
    available_sapce_x = settings.screen_width - (2 * alien_width)
    return int(available_sapce_x / (2 * alien_width))


def create_fleet(ai_settings, screen, ship, aliens):
    alien = Alien(screen, ai_settings)
    # alien_width = alien.rect.width
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,
                                  alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number,
                         row_number)


def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(screen, ai_settings)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def update_alien(settings, alien, bullets, ship, stats, screen):
    check_fleet_edges(settings, alien)
    alien.update()
    if pygame.sprite.spritecollideany(ship, alien):
        ship_hit(settings, bullets, alien, screen, ship, stats)
    check_alien_bottom(settings, screen, alien, ship, bullets, stats)


def check_alien_bottom(settings, screen, alien, ship, bullets, stats):
    screen_rect = screen.get_rect()
    for a in alien.sprites():
        if a.rect.bottom >= screen_rect.bottom:
            ship_hit(settings, bullets, alien, screen, ship, stats)
            break


def ship_hit(settings, bullets, alien, screen, ship, stats):
    if stats.ship_left > 0:
        stats.ship_left -= 1
        bullets.empty()
        alien.empty()
        create_fleet(settings, screen, ship, alien)
        ship.center_ship()
        sleep(0.5)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_fleet_edges(settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edge():
            change_fleet_direction(settings, aliens)
            break


def change_fleet_direction(settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_speed
    settings.fleet_direction *= -1


def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
