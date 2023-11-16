def start_screen(screen, oner, twor, ret, font, WIDTH, HEIGHT):
    # Clear the screen
    screen.fill((0, 0, 0))

    # Render and display "ENTER TO CONTINUE" text
    text_surface = font.render("Race Game", True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    screen.blit(text_surface, text_rect)
    text_surface2 = font.render("Player1: W to ready  Player2: Up arrow to ready", True, (255, 255, 255))
    text_rect2 = text_surface2.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text_surface2, text_rect2)

    if oner == True and twor == False:
        screen.fill((0, 0, 0))
        text_surface2 = font.render("PLAYER1 READY    Player2: Up arrow to ready", True, (255, 255, 255))
        screen.blit(text_surface2, text_rect2)
        return False
    if oner == False and twor == True:
        screen.fill((0, 0, 0))
        text_surface2 = font.render("Player1: W to ready    PLAYER2 READY", True, (255, 255, 255))
        screen.blit(text_surface2, text_rect2)
        return False
    if oner and twor and not ret:
        screen.fill((0, 0, 0))
        text_surface2 = font.render("PLAYER1 READY   PLAYER2 READY", True, (255, 255, 255))
        screen.blit(text_surface2, text_rect2)
        text_surface = font.render("Enter to start.", True, (255, 255, 255))
        screen.blit(text_surface, text_rect)
        return False
    if oner and twor and ret:
        return True