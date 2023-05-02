<img width="633" alt="Screenshot 2023-05-02 at 23 24 39" src="https://user-images.githubusercontent.com/20990023/235777906-6d6c3737-979d-4d1f-9826-e8fef938c90e.png">


```mermaid
sequenceDiagram
  participant UI
  participant ScoreMenu
  participant DatabaseHandler
  participant Game
  participant GameLoop
  UI->>Game: play_game()
  Game->>GameLoop: start()
  GameLoop-->>Game: score
  Game-->>UI: score
  UI->>ScoreMenu: show_score_menu_view(score)
  ScoreMenu->>DatabaseHandler: add_score(names, score)
  DatabaseHandler->>ScoreMenu: 
  ScoreMenu->>DatabaseHandler: get_highest_score_team()
  DatabaseHandler-->>ScoreMenu: best_team
  ScoreMenu-->>UI: 
```
