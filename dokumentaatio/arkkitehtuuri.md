<img width="742" alt="kaavio2" src="https://user-images.githubusercontent.com/20990023/232882062-6e2e01bd-eb00-4c2c-aa15-35f840240024.png">

```mermaid
sequenceDiagram
  participant UI
  participant ScoreMenu
  participant Game
  participant GameLoop
  UI->>Game: play_game()
  Game->>GameLoop: start()
  GameLoop-->>Game: score
  Game-->>UI: score
  UI->>ScoreMenu: show_score_menu_view(score)
  ScoreMenu-->>UI: 
```
